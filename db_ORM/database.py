from sqlalchemy import create_engine,Table,Column,Integer,String,TIMESTAMP,ForeignKey,Float,ForeignKeyConstraint,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker,Session
from sqlalchemy.orm import relationship

#1 create engine and bind it to the already existed db
engine = create_engine("mysql://root:@127.0.0.1/LALuxuryHouses")
#2 two possible ways to declare a table, declarative base e mapper, in this case we're using declarative
# we create a Base class for our tables and also a metadata object for the 2nd way to declare a table
Base = declarative_base()
metadata = MetaData()

#CLIENTS (SSN, Lastname, Firstname, Address, City, State, Age, PhoneNumber)
#SALE(IDSaleContract, HouseAddress, HouseCity, Date, Cost, IDEmployee)
#SOLDTO(IDSaleContract,ClientSSN)
#OWNEDBY(HouseAddress, HouseCity, ClientSSN)

Soldto = Table('Soldto',Base.metadata,
    Column('ClientSSN',String(9),ForeignKey('Clients.SSN'),nullable=False),
    Column('Idsalecontract',String(20),ForeignKey('Sale.Idsalecontract'),nullable=False)
    )

#verifica che sia corretta (3 indici di cui 2 accoppiati ma dubbio se sono primary key accoppiate (2)+1 )
Ownedby = Table('Ownedby',Base.metadata,
    Column('Houseaddress',String(40),nullable=False),
    Column('Housecity',String(40),nullable=False),
    Column('ClientSSN',String(9),ForeignKey('Clients.SSN'),nullable=False),
    ForeignKeyConstraint(['Houseaddress', 'Housecity'], ['Houses.Houseaddress', 'Houses.Housecity'])
    )

Rentedby = Table('Rentedby',Base.metadata,
    Column('Idrentalcontract',String(20),ForeignKey('Rentalcontract.Idrentalcontract'),nullable=False),
    Column('ClientSSN',String(9),ForeignKey('Clients.SSN'),nullable=False)
    )

class Houses(Base):
    __tablename__='Houses'
    Houseaddress = Column(String(40),primary_key=True)
    Housecity = Column(String(40),primary_key=True)
    Sizesquaremeters = Column(Float)
    Rooms = Column(Integer)
    #many to many relationship
    parents = relationship("Clients", secondary = Ownedby, back_populates='Houses')
    #one to many relationship with Sale
    sold_houses = relationship('Sale')
    #one to many relationship with RentalContract
    rented_houses = relationship('Rentalcontract')

class Employee(Base):
    __tablename__='Employee'
    Idemployee = Column (String(20),primary_key=True)
    Lastname = Column(String(20))
    Firstname = Column(String(20))
    Phonenumber = Column(String(20))
    #one to many rel between Employee and Sale, Employee parent
    sale_associated = relationship('Sale')
    #one to many rel btw Employee and Rentalcontract
    managing_empl = relationship('Rentalcontract')

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

class Clients(Base):
    __tablename__ = 'Clients'
    SSN = Column(String(9),primary_key=True)
    Lastname = Column(String(20))
    Firstname = Column(String(20))
    Address = Column(String(40))
    City = Column(String(20))
    State = Column(String(20))
    Age = Column(Integer)
    Phonenumber = Column(String(20))
    #Clients è in relazione con Sale tramite la SoldTo Table
    sales_associated = relationship("Sale", secondary = Soldto, back_populates='Clients')
    #Clients è in relazione con Houses tramite Ownedby table
    houses_associated = relationship("Houses", secondary= Ownedby, back_populates= 'Clients')
    #Clients è in relazione con Rentalcontract tramite Rentedby table
    rental_associated = relationship('Rentalcontract', secondary= Rentedby, back_populates = 'Clients')


Base.metadata.create_all(engine)