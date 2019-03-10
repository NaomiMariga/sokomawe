from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
engine = create_engine('postgres://vdjvyibgfeyiio:2d3c12435e93fe44ec5b7546dc7e494d5a0f7bac28b60bb325333ca1cd3a4e2c@ec2-23-21-165-188.compute-1.amazonaws.com:5432/ds3fhh163hsb1?ssl=true&sslfactory=org.postgresql.ssl.NonValidatingFactory')
meta = MetaData()

users = Table(
   'users', meta, 
   Column('userid', Integer, primary_key=True),
   Column('firstname', String), 
   Column('surname', String),
   Column('idnumber', String), 
   Column('phonenumber', String), 
   Column('email', String), 
   Column('username', String), 
   Column('password', String)
)

items = Table(
   'items', meta, 
   Column('itemid', Integer, primary_key = True), 
   Column('userid', Integer,ForeignKey('users.userid', ondelete='CASCADE')),
   Column('itemdescription', String),
   Column('price', String), 
   Column('shippingfee', String), 
   Column('location', String)
)

images = Table(
   'images', meta,
   Column('imageid',Integer, primary_key=True),
   Column('itemid', Integer, ForeignKey('users.userid', ondelete='CASCADE')),
   Column('itemimagelink', String)
)
sessions = Table(
   'sessions', meta, 
   Column('sessionid', Integer, primary_key=True),
   Column('userid', Integer, ForeignKey('users.userid', ondelete='CASCADE')),
   Column('sessiontoken', String)
)
meta.create_all(engine)
