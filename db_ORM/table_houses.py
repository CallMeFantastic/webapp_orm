from sqlalchemy.orm import relationship
from sqlalchemy import create_engine,Table,Column,Integer,String,TIMESTAMP,ForeignKey,Float,ForeignKeyConstraint,MetaData,Date,CheckConstraint
from database import Base

from table_ownedby import Ownedby

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
