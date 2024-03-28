from sqlalchemy import Column, String, Integer, Date, DateTime, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base


class Country(Base):
    __tablename__ = 'country'
    country_id = Column(Integer, autoincrement=True, primary_key=True)
    country_name = Column(String)


class Status(Base):
    __tablename__ = 'status'
    status_id = Column(Integer, autoincrement=True, primary_key=True)
    status_name = Column(String)
    cost = Column(Float)


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    status_id = Column(Integer, ForeignKey('status.status_id'))
    fname = Column(String)
    lname = Column(String)
    tellNo = Column(String, unique=True, nullable=False)
    email = Column(Integer, unique=True, nullable=False)
    reg_date = Column(DateTime)

    status_pk = relationship(Status, lazy='subquery')


class Hotels(Base):
    __tablename__ = 'hotels'
    hotel_id = Column(Integer, primary_key=True, autoincrement=True)
    country_id = Column(Integer, ForeignKey('country.country_id'))
    hotel_name = Column(String)
    cost = Column(Float)
    address = Column(String)

    country_pk = relationship(Country, lazy='subquery')


class TourAgent(Base):
    __tablename__ = 'agent'
    agent_id = Column(Integer, primary_key=True, autoincrement=True)
    country_id = Column(Integer, ForeignKey('country.country_id'))
    agent_name = Column(String)
    agent_tellNo = Column(String)
    agent_email = Column(String, unique=True, nullable=False)
    tour_cost = Column(Float)

    country_pk = relationship(Country, lazy='subquery')


class Sights(Base):
    __tablename__ = 'sights'
    sight_id = Column(Integer, autoincrement=True, primary_key=True)
    country_id = Column(Integer, ForeignKey('country.country_id'))
    sight_name = Column(String)
    sight_info = Column(Text)
    sight_address = Column(String)

    country_pk = relationship(Country, lazy='subquery')
































