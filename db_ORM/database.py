from sqlalchemy import create_engine,Table,Column,Integer,String,TIMESTAMP,ForeignKey,Float,ForeignKeyConstraint,MetaData,Date,CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker,Session
from sqlalchemy.orm import relationship



Base = declarative_base()
#1 create engine and bind it to the already existed db
engine = create_engine("mysql://root:@127.0.0.1/LALuxuryHouses")

#----------------tables

Ownedby = Table('Ownedby',Base.metadata,
    Column('Houseaddress',String(40),nullable=False),
    Column('Housecity',String(40),nullable=False),
    Column('ClientSSN',String(9),ForeignKey('Clients.SSN'),nullable=False),
    ForeignKeyConstraint(['Houseaddress', 'Housecity'], ['Houses.Houseaddress', 'Houses.Housecity'])
    )

Soldto = Table('Soldto',Base.metadata,
    Column('ClientSSN',String(9),ForeignKey('Clients.SSN'),nullable=False),
    Column('Idsalecontract',String(20),ForeignKey('Sale.Idsalecontract'),nullable=False)
    )

Rentedby = Table('Rentedby',Base.metadata,
    Column('Idrentalcontract',String(20),ForeignKey('Rentalcontract.Idrentalcontract'),nullable=False),
    Column('ClientSSN',String(9),ForeignKey('Clients.SSN'),nullable=False)
    )

class Clients(Base):
    __tablename__ = 'Clients'
    SSN = Column(String(9),primary_key=True)
    Lastname = Column(String(20),nullable=False)
    Firstname = Column(String(20),nullable=False)
    Address = Column(String(40))
    City = Column(String(20),nullable=False)
    State = Column(String(20),nullable=False)
    Age = Column(Integer)
    CheckConstraint(Column('Age') >= 18)
    CheckConstraint(Column('Age')<=110)
    Phonenumber = Column(String(20),nullable=False)
    #Clients è in relazione con Sale tramite la SoldTo Table
    sales_associated = relationship("Sale", secondary = Soldto, back_populates='Clients')
    #Clients è in relazione con Houses tramite Ownedby table
    houses_associated = relationship("Houses", secondary= Ownedby, back_populates= 'Clients')
    #Clients è in relazione con Rentalcontract tramite Rentedby table
    rental_associated = relationship('Rentalcontract', secondary= Rentedby, back_populates = 'Clients')
    def __init__(self, SSN, Lastname, Firstname, Address, City, State, Age, Phonenumber):
        self.SSN = SSN
        self.Lastname = Lastname
        self.Firstname = Firstname
        self.Address = Address
        self.City = City
        self.State= State
        self.Age = Age
        self.Phonenumber = Phonenumber

class Employee(Base):
    __tablename__='Employee'
    Idemployee = Column (String(20),primary_key=True)
    Lastname = Column(String(20))
    Firstname = Column(String(20))
    Phonenumber = Column(String(20))
    #one to many rel between Employee and Sale, Employee parent
    sale_associated = relationship('Sale')
    #one to many rel btw Employee and Rentalcontract parent
    managing_empl = relationship('Rentalcontract')
    def __init__(self, Idemployee, Lastname, Firstname, Phonenumber):
        self.Idemployee = Idemployee
        self.Lastname = Lastname
        self.Firstname = Firstname
        self.Phonenumber = Phonenumber

class Houses(Base):
    __tablename__='Houses'
    Houseaddress = Column(String(40),primary_key=True)
    Housecity = Column(String(40),primary_key=True)
    Sizesquaremeters = Column(Float)
    Rooms = Column(Integer)
    #many to many relationship
    parents = relationship("Clients", secondary = Ownedby, back_populates='Houses')
    #one to many relationship with Sale (parent)
    sold_houses = relationship('Sale')
    #one to many relationship with RentalContract (parent)
    rented_houses = relationship('Rentalcontract')
    def __init__(self, Houseaddress, Housecity, Sizesquaremeters, Rooms):
        self.Houseaddress = Houseaddress
        self.Housecity = Housecity
        self.Sizesquaremeters = Sizesquaremeters
        self.Rooms = Rooms

class Rentalcontract(Base):
    __tablename__='Rentalcontract'
    Idrentalcontract= Column(String(20), primary_key=True)
    #one to many rel w\ houses (child)
    Houseaddress = Column(String(40), nullable= False)
    Housecity = Column(String(40),nullable=False)
    Startdate = Column(TIMESTAMP)
    Enddate = Column(TIMESTAMP)
    Annualcost = Column(Float)
    #one to many rel (child) w\ Employee
    Idemployee = Column(String(20), ForeignKey('Employee.Idemployee'),nullable=False)
    #many to many rel w\ Clients by means of Rentedby
    clients_associated = relationship('Clients', secondary=Rentedby, back_populates = 'Rentals')
    __table_args__ = (ForeignKeyConstraint([Houseaddress, Housecity],
                                            [Houses.Houseaddress, Houses.Housecity]),
                       {})
    def __init__(self, Idrentalcontract, Houseaddress, Housecity, Startdate, Enddate, Annualcost, Idemployee):
        self.Idemployee = Idemployee
        self.Houseaddress = Houseaddress
        self.Housecity = Housecity
        self.Startdate = Startdate
        self.Enddate = Enddate
        self.Annualcost = Annualcost
        self.Idemployee = Idemployee

class Sale(Base):
    __tablename__='Sale'
    Idsalecontract = Column(String(20),primary_key=True)
    Houseaddress = Column(String(40))
    Housecity = Column(String(40))
    Date = Column(TIMESTAMP)
    Cost = Column(Float)
    #one to many relationship w\ Employee (child)
    Idemployee = Column(String(20), ForeignKey('Employee.Idemployee'),nullable=False)
    #one to many relationship w\ Houses
    __table_args__ = (ForeignKeyConstraint([Houseaddress, Housecity],
                                            [Houses.Houseaddress, Houses.Housecity]),
                       {})
    #many to many relationship
    parents = relationship("Clients", secondary = Soldto, back_populates='Sales')
    def __init__(self, Idsalecontract, Houseaddress, Housecity, Date, Cost, Idemployee):
        self.Idsalecontract = Idsalecontract
        self.Houseaddress = Houseaddress
        self.Housecity = Housecity
        self.Date = Date
        self.Cost = Cost
        self.Idemployee = Idemployee


"""
Base.metadata.create_all(engine)

#create a session 
Session = sessionmaker(bind=engine)
session = Session()

session.add_all(
    Clients(SSN='12844CBA3', Lastname='Amata',Firstname='Giovanni',Address='Via Giuseppe malibondi 56',City='Catania',State='Italy',Age=22,Phonenumber='+39 345884251'),
    Clients(SSN='124663124', Lastname='Xi',Firstname='Wuah',Address='Chan seng SU 12442',State='Hong Kong ',City='Hong Kong',Age=33,Phonenumber='+39 63421231'),
    Clients(SSN='123gsaf21', Lastname='Alberti',Firstname='Damiano',Address='Via Giuseppe Garibaldi 112',City='Hong Kong',State='Italy',Age=22,Phonenumber='+39 345884251'),
    Clients(SSN='5215dg612', Lastname='Diamanti',Firstname='Federico',City='Milano',State='Italy',Age=22,Phonenumber='+39 53252112'),
    Clients(SSN='636we242f', Lastname='Giordani',Firstname='Giovanni',Address='Via Giuseppe malibondi 56',City='Hong Kong',State='Italy',Age=29,Phonenumber='+39 345884251'),
    Clients(SSN='12465r345', Lastname='Franceschino',Firstname='Alessio',City='Napoli',State='Italy',Age=24,Phonenumber='+39 632421412'),
    Clients(SSN='237485443', Lastname='Ciccioli',Firstname='Giuseppe',City='Matera',State='Italy',Age=17,Phonenumber='+39 166452342'),
)
session.commit()
session.quit()
"""