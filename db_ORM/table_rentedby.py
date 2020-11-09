from sqlalchemy import create_engine,Table,Column,Integer,String,TIMESTAMP,ForeignKey,Float,ForeignKeyConstraint,MetaData,Date,CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import Base

Rentedby = Table('Rentedby',Base.metadata,
    Column('Idrentalcontract',String(20),ForeignKey('Rentalcontract.Idrentalcontract'),nullable=False),
    Column('ClientSSN',String(9),ForeignKey('Clients.SSN'),nullable=False)
    )