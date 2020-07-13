from sqlalchemy import create_engine
import pandas as pd

#engine = create_engine("mysql+pymysql://dev:Dev@1234@@localhost/coal_dashboard?host=localhost?port=3306")
#engine.connect()

def fetch_data_db(text,db):

    engine = create_engine("mysql+pymysql://dev:Dev@1234@@localhost/{}?host=localhost?port=3306".format(db))
    engine.connect()

    data = pd.read_sql(text,engine)
    return data