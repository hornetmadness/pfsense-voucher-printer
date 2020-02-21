import config
import arrow
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

def connect_db():
  if not database_exists(config.db_string):
      create_database(config.db_string)
  
  db = create_engine(config.db_string, echo=config.db_debug)
  return db

Base = declarative_base()
class Vouchers(Base):
  __tablename__ = "vouchers"
  id = Column(Integer, primary_key=True)
  vid = Column(String, nullable=False)
  time = Column(Integer,nullable=False)
  date_added = Column(DateTime, nullable = False, default=func.now())
  date_disabled = Column(DateTime, nullable = False, default=func.now())
  disabled = Column(Integer, default = 0, nullable = False)


engine = connect_db()
Vouchers.__table__.create(bind=engine, checkfirst=True)
