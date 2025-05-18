# Instructions

#  Using this REST Countries API, create the functionality which will write 10 random countries to your 
# database.

#  These are the attributes which you should populate your tables with: name, capital, flag, subregion, 
# population.

#CREATE TABLE countries (
#    id SERIAL PRIMARY KEY,
#    name VARCHAR(100),
#    capital VARCHAR(100),
#    flag TEXT,
#    subregion VARCHAR(100),
#    population BIGINT
#);

import requests
import random
import psycopg2


conn = psycopg2.connect(
    dbname="restaurant_db",
    user="postgres",
    password="P0st2o25",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


response = requests.get("https://restcountries.com/v3.1/all")
data = response.json()
#print(data)

selected_countries = random.sample(data, 10)
#print(selected_countries)

for country in selected_countries:
    name = country.get("name", {}).get("common", "None")
    capital = country.get("capital", ["None"])[0]
    flag = country.get("flags", {}).get("png", "None")
    subregion = country.get("subregion", "None")
    population = country.get("population", 0)


    cur.execute("""
        INSERT INTO countries (name, capital, flag, subregion, population)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, capital, flag, subregion, population))

conn.commit()
cur.close()
conn.close()

print("10 countries inserted !!!")