#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer(), primary_key = True)
    name = Column(String())

if __name__ == '__main__':
    engine = create_engine("sqlite:///students.db")
    Base.metadata.create_all(engine) 