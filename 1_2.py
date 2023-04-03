import pymssql
import pandas as pd


server = '156.17.130.185:23333'
user = 'BIStud'
password = 'BIStudP@s'
conn = pymssql.connect(server, user, password, "AdventureWorks2014")
sql_query = pd.read_sql_query('''
                              SELECT TerritoryID, Name, CountryRegionCode, SalesYTD, SalesLastYear 
                              FROM Sales.SalesTerritory
                              '''
                              , conn)
df = pd.DataFrame(sql_query)
print(df)
df.to_csv('sales-territory.csv', index=False, sep=';')
conn.close()
