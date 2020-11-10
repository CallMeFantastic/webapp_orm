from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker,Session


#1 create engine and bind it to the already existed db, create Base needed for creating and commit table changes
Base = declarative_base()
engine = create_engine("mysql://root:@127.0.0.1/LALuxuryHouses")

#2, if needed, to start the creation of tables and (optionally the population of the entire db)
from tables import *
#3, if needed, to commit the creation of tables
Base.metadata.create_all(engine)

#to clear the database
#from tables import *
#Base.metadata.drop_all(engine)
#Base.metadata.clear()



#4, to create a session in order to insert delete update tuples in that session
Session = sessionmaker(bind=engine)
session = Session()

#to commit the changes of the session
session.commit()
