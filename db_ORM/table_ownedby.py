from sqlalchemy import create_engine,Table,Column,Integer,String,TIMESTAMP,ForeignKey,Float,ForeignKeyConstraint,MetaData,Date,CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import Base

#composite table using metadata

Ownedby = Table('Ownedby',Base.metadata,
    Column('Houseaddress',String(40),nullable=False),
    Column('Housecity',String(40),nullable=False),
    Column('ClientSSN',String(9),ForeignKey('Clients.SSN'),nullable=False),
    ForeignKeyConstraint(['Houseaddress', 'Housecity'], ['Houses.Houseaddress', 'Houses.Housecity'])
    )