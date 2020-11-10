from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker,Session
from tables import Sale,Soldto,Rentalcontract,Rentedby,Ownedby,Houses,Clients,Employee,Base
from population import auxiliary_tables_population,basic_tables



#1 init processes 
#create engine and bind it to the already existed db, create Base needed for creating tables(classes) and commit table insertion, as well as
#it creates a session to the db
def init():
    # global Base
    global engine
    global session
    # Base = declarative_base()
    engine = create_engine("mysql://root:@127.0.0.1/LALuxuryHouses")
    Session = sessionmaker(bind=engine)
    session = Session()

#2, if needed, to start the creation of tables and (optionally the population of the entire db)
def create_database():
    Base.metadata.create_all(engine)


def drop_database():
    #to clear the database
    #from tables import *
    Base.metadata.drop_all(engine)
    Base.metadata.clear()


init()
create_database()
#basic_tables(session)  #fix problem that you have to use the comment basic tables and after auxiliary or you get an error
auxiliary_tables_population(engine)

session.commit()
