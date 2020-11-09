from sqlalchemy.orm import relationship
from sqlalchemy import create_engine,Table,Column,Integer,String,TIMESTAMP,ForeignKey,Float,ForeignKeyConstraint,MetaData,Date,CheckConstraint
from database import Base

from table_rentedby import Rentedby
from table_houses import Houses

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