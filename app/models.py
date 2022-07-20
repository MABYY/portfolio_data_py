from sqlalchemy import TIMESTAMP, text, Column, Integer, String, ForeignKey 
from .database import Base

class User(Base):
    __tablename__ ="usersData"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable = False, unique= True)
    password = Column(String, nullable = False)
    role = Column(String, default = 'user', nullable=False)

class Fund(Base):
    __tablename__ = "fundData"
    id =Column(Integer, primary_key=True)
    Api = Column(Integer, nullable=False, unique= True)
    Nombre_Fondo = Column(String, nullable = False, unique= True)
    Fecha = Column(String, nullable = False)
    date = Column(TIMESTAMP(timezone=True),
                nullable=False, 
                server_default=text('now()'))
