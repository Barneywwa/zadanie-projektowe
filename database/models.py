from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Sklep(Base):
    __tablename__ = 'sklepy'
    id = Column(Integer, primary_key=True)
    adres = Column(String)
    nazwa_sieci = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

class Pracownik(Base):
    __tablename__ = 'pracownicy'
    id = Column(Integer, primary_key=True)
    imie = Column(String)
    nazwisko = Column(String)
    adres_zamieszkania = Column(String)
    adres_pracy = Column(String, ForeignKey('sklepy.adres'))
    latitude = Column(Float)
    longitude = Column(Float)
    sklep = relationship("Sklep")

class Dostawca(Base):
    __tablename__ = 'dostawcy'
    id = Column(Integer, primary_key=True)
    nazwa_dostawcy = Column(String)
    adres_dostawcy = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

class Dostawa(Base):
    __tablename__ = 'dostawy'
    id = Column(Integer, primary_key=True)
    adres_dostawy = Column(String, ForeignKey('sklepy.adres'))
    nazwa_dostawcy = Column(String, ForeignKey('dostawcy.nazwa_dostawcy'))
    sklep = relationship("Sklep")
    dostawca = relationship("Dostawca")

engine = create_engine('postgresql://postgres:postgres@localhost:5432/zadanie-projektowe')
Session = sessionmaker(bind=engine)
session = Session()