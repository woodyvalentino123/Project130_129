import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

del df["Star_name"]
del df["Mass"]
del df["Distance"]
del df["Radius"]

df = df.rename({
                'Star_name': "solar_system_name", 
                'Mass': "planet_discovery_method", 
                'Distance': "planet_orbital_inclination", 
                'Radius': "planet_density", 
            }, axis='columns')

df.to_csv('main2.csv') 
print(list(df))
print(df.shape)