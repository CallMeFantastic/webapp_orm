from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker,Session

#1 create engine and bind it to the already existed db
engine = create_engine("mysql://root:@127.0.0.1/LALuxuryHouses")
#2 two possible ways to declare a table, declarative base e mapper, in this case we're using declarative
# we create a Base class for our tables and also a metadata object for the 2nd way to declare a table
Base = declarative_base()
metadata = MetaData()


#Base.metadata.create_all(engine)
Base.metadata.clear()
Base.metadata.drop_all(engine)

"""

#create a session 
Session = sessionmaker(bind=engine)
session = Session()

session.add_all(
    Clients(SSN='12844CBA3', Lastname='Amata',Firstname='Giovanni',Address='Via Giuseppe malibondi 56',City='Catania',State='Italy',Age=22,Phonenumber='+39 345884251'),
    Clients(SSN='124663124', Lastname='Xi',Firstname='Wuah',Address='Chan seng SU 12442',State='Hong Kong ',City='Hong Kong',Age=33,Phonenumber='+39 63421231'),
    Clients(SSN='123gsaf21', Lastname='Alberti',Firstname='Giovanni',Address='Via Giuseppe Garibaldi 112',City='Hong Kong',State='Italy',Age=22,Phonenumber='+39 345884251'),
    Clients(SSN='5215dg612', Lastname='Amata',Firstname='Giovanni',City='Hong Kong',State='Italy',Age=22,Phonenumber='+39 345884251'),
    Clients(SSN='636we242f', Lastname='Amata',Firstname='Giovanni',Address='Via Giuseppe malibondi 56',City='Hong Kong',State='Italy',Age=22,Phonenumber='+39 345884251'),
    Clients(SSN='12465r345', Lastname='Amata',Firstname='Giovanni',City='Hong Kong',State='Italy',Age=24,Phonenumber='+39 345884251'),
    Clients(SSN='237485443', Lastname='Amata',Firstname='Giovanni',City='Hong Kong',State='Italy',Age=26,Phonenumber='+39 345884251'),
)
"""