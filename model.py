from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
engine = create_engine('postgres://mrmxrraryrctfp:462c22bcbb7087f9cfe34768c1117ee63bce61a468dfa794ed268ffd15086845@ec2-54-225-237-84.compute-1.amazonaws.com:5432/dcsm203ro91dic')
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
   Column('userid', Integer,ForeignKey('users.userid', ondelete ='CASCADE')), 
   Column('itemdescription', String),
   Column('price', String), 
   Column('shippingfee', String), 
   Column('location', String), 
)

images = Table(
'images', meta,
Column('imageid',Integer, primary_key=True),
Column('itemid', Integer, ForeignKey('users.userid', ondelete ='CASCADE')),
Column('itemimagelink', String), 

)
sessions = Table(
   'sessions', meta, 
   Column('sessionid', Integer, primary_key = True), 
   Column('userid', Integer, ForeignKey('users.userid', ondelete ='CASCADE')), 
   Column('sessiontoken', String), 

)
meta.create_all(engine)