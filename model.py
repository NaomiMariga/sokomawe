from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
engine = create_engine('postgresql+psycopg2://postgres:Theology@localhost:5432/sokomawe')
from sqlalchemy.orm import relationship
meta = MetaData()

users = Table(
   'users', meta, 
   Column('userid', Integer, primary_key = True), 
   Column('firstname', String), 
   Column('surname', String),
   Column('idnumber', String), 
   Column('phonenumber', String), 
   Column('email', String), 
   Column('username', String), 
   Column('password', String), 
)

items = Table(
   'items', meta, 
   Column('itemid', Integer, primary_key = True), 
   Column('userid', Integer), 
   Column('itemimagelink', String), 
   Column('itemdescription', String),
   Column('price', String), 
   Column('shippingfee', String), 
   Column('location', String), 
)

sessions = Table(
   'sessions', meta, 
   Column('sessionid', Integer, primary_key = True), 
   Column('userid', Integer, ForeignKey('users.userid', ondelete ='CASCADE')), 
   Column('sessiontoken', String), 

)
meta.create_all(engine)