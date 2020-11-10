from sqlalchemy import create_engine,Table,Column,Integer,String,ForeignKey,Float,ForeignKeyConstraint,MetaData,Date,CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker,Session
from sqlalchemy.orm import relationship

from database import Base

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
    Age = Column(Integer, CheckConstraint('Age >= 18 and Age <=110'))
    Phonenumber = Column(String(20),nullable=False)
    #Clients è in relazione con Sale tramite la SoldTo Table
    Sale = relationship("Sale", secondary = Soldto, back_populates='Clients')
    #Clients è in relazione con Houses tramite Ownedby table
    Houses = relationship("Houses", secondary= Ownedby, back_populates= 'Clients')
    #Clients è in relazione con Rentalcontract tramite Rentedby table
    Rentalcontract = relationship('Rentalcontract', secondary= Rentedby, back_populates = 'Clients')
    def __init__(self, SSN, Lastname, Firstname, City, State, Age, Phonenumber, Address= None):
        self.SSN = SSN
        self.Lastname = Lastname
        self.Firstname = Firstname
        self.City = City
        self.State= State
        self.Age = Age
        self.Phonenumber = Phonenumber
        if Address is not None:
            self.Address = Address

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
    Clients = relationship("Clients", secondary = Ownedby, back_populates='Houses')
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
    Startdate = Column(Date)
    Enddate = Column(Date)
    Annualcost = Column(Float)
    #one to many rel (child) w\ Employee
    Idemployee = Column(String(20), ForeignKey('Employee.Idemployee'),nullable=False)
    #many to many rel w\ Clients by means of Rentedby
    Clients = relationship('Clients', secondary=Rentedby, back_populates = 'Rentalcontract')
    __table_args__ = (ForeignKeyConstraint([Houseaddress, Housecity],
                                            [Houses.Houseaddress, Houses.Housecity]),
                       {})
    def __init__(self, Idrentalcontract, Houseaddress, Housecity, Startdate, Annualcost, Idemployee, Enddate = None):
        self.Idemployee = Idemployee
        self.Houseaddress = Houseaddress
        self.Housecity = Housecity
        self.Startdate = Startdate
        self.Annualcost = Annualcost
        self.Idemployee = Idemployee
        if Enddate is not None:
            self.Enddate = Enddate


class Sale(Base):
    __tablename__='Sale'
    Idsalecontract = Column(String(20),primary_key=True)
    Houseaddress = Column(String(40))
    Housecity = Column(String(40))
    Date = Column(Date)
    Cost = Column(Float)
    #one to many relationship w\ Employee (child)
    Idemployee = Column(String(20), ForeignKey('Employee.Idemployee'),nullable=False)
    #one to many relationship w\ Houses
    __table_args__ = (ForeignKeyConstraint([Houseaddress, Housecity],
                                            [Houses.Houseaddress, Houses.Housecity]),
                       {})
    #many to many relationship
    Clients = relationship('Clients', secondary = Soldto, back_populates='Sale')
    def __init__(self, Idsalecontract, Houseaddress, Housecity, Date, Cost, Idemployee):
        self.Idsalecontract = Idsalecontract
        self.Houseaddress = Houseaddress
        self.Housecity = Housecity
        self.Date = Date
        self.Cost = Cost
        self.Idemployee = Idemployee


#if you want to populate, otherwise comment it
from population import *