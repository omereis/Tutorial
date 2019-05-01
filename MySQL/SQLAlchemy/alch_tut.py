# Source: https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91

import sqlalchemy as db

engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)
