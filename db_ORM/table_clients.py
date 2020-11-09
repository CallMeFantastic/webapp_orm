from sqlalchemy.orm import relationship
from sqlalchemy import create_engine,Table,Column,Integer,String,TIMESTAMP,ForeignKey,Float,ForeignKeyConstraint,MetaData,Date,CheckConstraint
from database import Base


from table_rentedby import Rentedby
from table_soldto import Soldto
from table_ownedby import Ownedby


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
    def __init__(self, SSN, Lastname, Firstname, Address, City, Age, Phonenumber):
        self.SSN = SSN
        self.Lastname = Lastname
        self.Firstname = Firstname
        self.Address = Address
        self.City = City
        self.Age = Age
        self.Phonenumber = Phonenumber
