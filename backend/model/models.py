from sqlalchemy import Column, Integer, String, ForeignKey, Time, Boolean
from database.database import Base
from sqlalchemy import Column, Integer, String, Time, ForeignKey
from sqlalchemy.orm import relationship



# class 

# class Doctor(Base):
#     __tablename__ = 'doctors'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     district = Column(String, nullable= False)
#     address = Column(String, nullable=False)
#     price = Column(Integer, nullable= False)
#     inclusive_medicine = Column(Boolean, nullable=False)
#     inclusive_medicine_day = Column(Integer)
#     category = Column(String, nullable= False)
#     language = Column(String, nullable=False)
#     numbers = relationship("Numbers", backref="doctor")
#     opening_times = relationship("OpeningTime", backref="doctor")

# class Numbers(Base):
#     __tablename__ = 'numbers'
#     id = Column(Integer, primary_key=True)
#     number = Column(Integer, nullable=False)
#     doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)

# class OpeningTime(Base):
#     __tablename__ = 'opening_time'
#     day_of_week = Column(String(10), nullable=False, primary_key=True)
#     opening_time = Column(Time, nullable=False, primary_key= True)
#     closing_time = Column(Time, nullable=False, primary_key= True)
#     doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False, primary_key=True)

