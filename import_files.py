import pandas as pd
import psycopg2
import sqlalchemy as sa

engine = sa.create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

# Read the CSV file into a pandas DataFrame
bus_may17 = pd.read_csv('./Bus_Data/2023-05-17-bus-positions.csv')

# Insert the DataFrame into a PostgreSQL table
bus_may17.to_sql('bus_may17', engine, if_exists='replace')
