from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship
from database import Base, engine


class SportType(Base):

    __tablename__ = 'sport_types'

    id = Column(Integer, primary_key=True)
    unit_of_measurement = Column(String(20), nullable=False)
    name = Column(String(50), nullable=False)
    world_record = Column(Numeric(precision=10, scale=2))
    olympic_record = Column(Numeric(precision=10, scale=2))

    # One-to-Many relation with results
    results = relationship('Result', back_populates='sport_type')


class Result(Base):

    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    competition_name = Column(String(150), nullable=False)
    performance = Column(Integer, nullable=False)
    place = Column(Integer, nullable=False)
    date = Column(Date)
    venue = Column(String(150), nullable=False)

    # Many-to-One relation with sport_types
    sport_type_id = Column(Integer, ForeignKey('sport_types.id'))
    sport_type = relationship('SportType', back_populates='results')

    # Many-to-One with athletes
    athlete_id = Column(Integer, ForeignKey('athletes.id'))
    athlete = relationship('Athlete', back_populates='results')


class Athlete(Base):

    __tablename__ = 'athletes'

    id = Column(Integer, primary_key=True)
    win = Column(Integer, default=0)
    full_name = Column(String(150), nullable=False)
    birth_year = Column(Integer, nullable=False)
    country = Column(String(50), nullable=False)

    # One-to-Many with results
    results = relationship('Result', back_populates='athlete')


Base.metadata.create_all(engine)