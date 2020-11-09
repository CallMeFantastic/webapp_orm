from sqlalchemy import create_engine,Table,Column,Integer,String,TIMESTAMP,ForeignKey,Float,ForeignKeyConstraint,MetaData,Date,CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import Base



Soldto = Table('Soldto',Base.metadata,
    Column('ClientSSN',String(9),ForeignKey('Clients.SSN'),nullable=False),
    Column('Idsalecontract',String(20),ForeignKey('Sale.Idsalecontract'),nullable=False)
    )