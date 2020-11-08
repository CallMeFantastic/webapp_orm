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

#composite foreign key dalla stessa tabella, esempio che ti servirà è quando vuoi creare una tabella in cui c'è una foreign key da una tabella e 2
#dalla stessa tabella, come fai a dire che due sono accoppiate e l'altra no è singola?  così! Ma nel caso del soldto non è l'approccio corretto
# Soldto = Table('Soldto', Base.metadata,
#     Column('ClientSSN', String(9),nullable=False),
#     Column('Idsalecontract', String(20),nullable=False),
#     ForeignKeyConstraint(['ClientSSN', 'Idsalecontract'], ['Clients.SSN', 'Sale.Idsalecontract'])
# )


Soldto = Table('Soldto',Base.metadata,
    Column('ClientSSN',String(9),ForeignKey('Clients.SSN'),nullable=False),
    Column('Idsalecontract',String(20),ForeignKey('Sale.Idsalecontract'),nullable=False)
    )


#verifica che sia corretta (3 indici di cui 2 accoppiati ma dubbio primary key? )
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

class Rentalcontract(Base):
    __tablename__='Rentalcontract'
    Idrentalcontract= Column(String(20), primary_key=True)
    #Houseaddress = Column(String(40), ForeignKey('Houses.Houseaddress'))
    #Housecity = Column(String(40), ForeignKey('Houses.Housecity'))
    Startdate = Column(TIMESTAMP)
    Enddate = Column(TIMESTAMP)
    Annualcost = Column(Float)
    #Idemployee = Column(String(20), ForeignKey('Employee.Idemployee'))
    #many to many rel w\ Clients by means of Rentedby
    clients_associated = relationship('Clients', secondary=Rentedby, back_populates = 'Rentals')

class Houses(Base):
    __tablename__='Houses'
    Houseaddress = Column(String(40),primary_key=True)
    Housecity = Column(String(40),primary_key=True)
    Sizesquaremeters = Column(Float)
    Rooms = Column(Integer)
    parents = relationship("Clients", secondary = Ownedby, back_populates='Houses')

class Sale(Base):
    __tablename__='Sale'
    Idsalecontract = Column(String(20),primary_key=True)
    Houseaddress = Column(String(40))
    Housecity = Column(String(40))
    Date = Column(TIMESTAMP)
    Cost = Column(Float)
    # Idemployee = Column(String(20),ForeignKey('Employee.Idemployee'))
    # __table_args__ = (ForeignKeyConstraint([Houseaddress, Housecity],
    #                                        [Houses.Houseaddress, Houses.Housecity]),
    #                   {})
    parents = relationship("Clients", secondary = Soldto, back_populates='Sales')

# class Employee(Base):
#     __tablename__='Employee'
#     Idemployee = Column (String(20),primary_key=True)
#     Lastname = Column(String(20))
#     Firstname = Column(String(20))
#     Phonenumber = Column(String(20))


Base.metadata.create_all(engine)