#Lets go the mall Everbody - Robin schberbatsy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#Creating an Database file
DATABASE_URL = "sqlite:///./tasks.db"

#Now lets create the engine of the Ferrari Spider
engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False})

#Now lets create the sessions things
SessionLocal = sessionmaker(bind=engine,autoflush=True,autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()