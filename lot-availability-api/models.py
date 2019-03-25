# coding: utf-8
from sqlalchemy import Boolean, Column, ForeignKey, Integer, Numeric, SmallInteger, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from decimal import Decimal

Base = declarative_base()
metadata = Base.metadata

class Parking(Base):
    __tablename__ = 'Parking'

    type_id = Column(SmallInteger, primary_key=True, server_default=text(
        "nextval('parking_type_id_seq'::regclass)"))
    type_label = Column(Text, nullable=False)

class Spots(Base):
    __tablename__ = 'Spots'

    spot_id = Column(UUID, primary_key=True,
                     server_default=text("uuid_generate_v4()"))
    spot_number = Column(Integer, nullable=False)
    latitude = Column(Numeric(10, 6))
    longitude = Column(Numeric(10, 6))
    parking_type = Column(ForeignKey('Parking.type_id'))
    availability = Column(Boolean)
    lot_id = Column(ForeignKey('Lots.lot_id'))

    parking = relationship('Parking')
    Lots = relationship('Lots')

    def as_dict(self):
        table_as_dict = {c.name: getattr(self, c.name)
                         for c in self.__table__.columns}
        for c in table_as_dict:
            if isinstance(table_as_dict[c], Decimal):
                table_as_dict[c] = float(table_as_dict[c])
        return table_as_dict

class Lots(Base):
    __tablename__ = 'Lots'
    lot_id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    lot_name = Column(Text, nullable=False)
    description = Column(Text)
    latitude = Column(Numeric(10, 6))
    longitude = Column(Numeric(10, 6))
    campus_id = Column(ForeignKey('Campuses.campus_id'))
    lot_number = Column(Numeric)

    Campuses = relationship('Campuses')


    def as_dict(self):
        table_as_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        for c in table_as_dict:
           if isinstance(table_as_dict[c], Decimal):
               table_as_dict[c] = float(table_as_dict[c])
        return table_as_dict

class Campuses(Base):
    __tablename__ = 'Campuses'
    campus_id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    campus_name = Column(Text, nullable=False)
    address = Column(Text)
    city = Column(Text)
    state = Column(Text)
    zipcode = Column(Numeric)

    def as_dict(self):
        table_as_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        for c in table_as_dict:
           if isinstance(table_as_dict[c], Decimal):
               table_as_dict[c] = float(table_as_dict[c])
        return table_as_dict