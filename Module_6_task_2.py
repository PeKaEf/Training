from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, Float
engine = create_engine('sqlite:///stations.db', echo = True)
meta = MetaData()
conn = engine.connect()

stations = Table(
   'stations', meta, 
   Column('id', Text, primary_key = True), 
   Column('latitude', Float), 
   Column('longitude', Float),
   Column('elevation', Integer), 
   Column('name', String),
    Column('country', String), 
   Column('state', String),
)

measures = Table(
   'measures', meta, 
   Column('station', Text, primary_key = True), 
   Column('date', Text),
   Column('Float', Integer), 
   Column('tobs', String),
)
meta.create_all(engine)

result = engine.execute('SELECT * FROM person WHERE id >= :id', id=3)

rows = result.fetchall()

result.close()