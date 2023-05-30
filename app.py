from flask import Flask, send_file, render_template, jsonify
import pandas as pd
import psycopg2
import sqlalchemy as sa
from flask_cors import CORS


engine = sa.create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

df = pd.read_csv('2023-05-17-bus-positions_1.csv')
df = df.dropna(subset = 'route_id')

app = Flask(__name__, template_folder='templates') 
CORS(app)

# --name-- flask, create an app using the file name


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/<bus_route>')
def greeting(bus_route): 
    df2 = df[df['route_id'].str.contains(bus_route)]
    return jsonify(df2.to_dict(orient='records'))

# ^ Creating dynamic content based on the user
# ? usually a parameter in the URL 

@app.route('/get_bus_data/<route>')
def getBus(route):
    df = pd.read_sql(f"""
    select bus_may17."route_id", bus_may17."latitude", bus_may17."longitude" from bus_may17
    where "latitude" IS NOT NULL AND "route_id" = '{route}' LIMIT 10
    """, engine)
    return jsonify(df.to_dict(orient='records'))




if __name__ == '__main__':
    app.run(debug = True)

# If this file is our main running file.
# Jango requires a bunch of other commands
# Nodejs express - python but for javascript - to run on a computer you need this. 
# Javascript on the computer instead of the browser
# He's editing an app.js script...express and flask you can build a lot of stuff on top.

# It's inefficient to read stuff in pandas b/c it's reading in RAM.
# Once something happens, your changes aren't saved. If you don't have enough RAM, 2GB, etc. 
# It becomes really great for your memory.

# Adapt so you can query using SQL Alchemy, etc. backend database languages.

# We want SQL b/c it's easy to query things

# pip freeze > requirement.txt 
# single instead of double for value 

# he is connecting to an amazon web service database


# SQL Injection is to santize your inputs before you run anything 

# Creating a database from cvs. We need to look at DOCKER.



