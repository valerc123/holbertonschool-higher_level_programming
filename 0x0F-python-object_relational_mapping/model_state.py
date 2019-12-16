#!/usr/bin/python3
"""
    Create table ´states´ using SQLAlchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class representing the `states` table.
    Columns:
        id (int): /NOT NULL/AUTO_INCREMENT/PRIMARY_KEY/
        name (string): /VARCHAR(128)/NOT NULL/
    """
    # Declare the name of the table
    __tablename__ = 'states'

    # fileds of table ´states´
    id = Column(Integer, primary_key=True, nullable=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
