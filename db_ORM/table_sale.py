from sqlalchemy.orm import relationship
from sqlalchemy import create_engine,Table,Column,Integer,String,TIMESTAMP,ForeignKey,Float,ForeignKeyConstraint,MetaData,Date,CheckConstraint
from database import Base

from table_soldto import Soldto
from table_houses import Houses

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