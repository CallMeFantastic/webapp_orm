from sqlalchemy.orm import relationship
from sqlalchemy import create_engine,Table,Column,Integer,String,TIMESTAMP,ForeignKey,Float,ForeignKeyConstraint,MetaData,Date,CheckConstraint
from database import Base

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