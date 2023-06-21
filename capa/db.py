import os

from dotenv.main import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# agreguen un archivo .env a la misma altura del .gitignore
# agregen el .env al .gitignore
# en el archivo .env tienen que poner lo siguiente: 
#                                     USER_POSTGRES=suUsuario
#                                     PASS_POSTGRES=suPass
# asi tal cual como esta, sin comillas ni nada
# si les funciona avisen y les paso la cuenta de mp por el tutorial

load_dotenv()
user_postgres=os.environ['USER_POSTGRES']
pass_postgres=os.environ['PASS_POSTGRES']


SQLALCHEMY_DATABASE_URL = f"postgresql://{user_postgres}:{pass_postgres}@localhost:5432/capa"

engine = create_engine( SQLALCHEMY_DATABASE_URL )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_tables():
  Base.metadata.create_all(bind=engine)
    
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

