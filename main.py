#Importation des modules 
import pandas as pd
import mysql.connector
from mysql.connector import Error

#Chargement des données
Mm = pd.read_excel(r'C:/Users/LAB-MND/Desktop/travail/Mental_Health.xlsx')
print(Mm.columns)


print('----------------------------------------------------------------')
print(Mm.columns)

# Chargement du dataframe dans MYSQL
try:
    connexion = mysql.connector.connect(host='localhost',
                                       database='ma_base',
                                       user='root',
                                       password='')
    if connexion.is_connected():
        print('Connexion à MySQL réussie')
except Error as e:
    print(f"Erreur lors de la connexion à MySQL: {e}")

try:
    cursor = connexion.cursor()

    for i,row in Mm.iterrows():
        sql = """INSERT INTO mental(Sexe, Pays_repondant, Occupations, autonome, antecedant_mentale, traitement_mental) VALUES (%s,%s,%s,%s,%s,%s)"""
        #print(sql)
        cursor.execute(sql, tuple(row))

    connexion.commit()
    connexion.close()
    print("DataFrame chargé dans MySQL avec succès!")
except Exception as e:
    print(f"Erreur lors du chargement du DataFrame dans MySQL: {e}")



