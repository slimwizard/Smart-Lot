# coding: utf-8
from sqlalchemy import Boolean, Column, ForeignKey, Integer, Numeric, SmallInteger, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Parking(Base):
    __tablename__ = 'parking'

    type_id = Column(SmallInteger, primary_key=True, server_default=text("nextval('parking_type_id_seq'::regclass)"))
    type_label = Column(Text, nullable=False)


class NethkenA(Base):
    __tablename__ = 'nethken_a'

    spot_id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    spot_number = Column(Integer, nullable=False)
    latitude = Column(Numeric(10, 6))
    longitude = Column(Numeric(10, 6))
    parking_type = Column(ForeignKey('parking.type_id'))
    occupied = Column(Boolean)

    parking = relationship('Parking')

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

