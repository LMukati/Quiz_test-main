from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import logging

# here the connection of url of postgresql
SQL_ALCHMEY_DATABASE_URL = "postgresql://postgres:12345@localhost:5432/Quize_info"

# STEP 1
# HERE CREATE THE ENGINE OF DATABASE
engine = create_engine(SQL_ALCHMEY_DATABASE_URL,echo=False)

# INSTABLISHED THE CONNECTION OF THE DATABASE
db = engine.connect()
# STEP2  
# CREASTE THE SESSIONMAKER FOR DATABASE
Session = sessionmaker(autocommit = False,autoflush =False,bind=engine)
# STEP3 
# CREATE THE DECLAREATIVE BASE OF DATABASE CONNETION ...

session = Session()

# STEP4

# CREATE THE ROLLBACK FOR DATABASE CONNECTION

def close_session():
    try:
        session.close()
        db.close()
        engine.dispose()
    except Exception as e:
        logging.warning("Exception error close the database !")