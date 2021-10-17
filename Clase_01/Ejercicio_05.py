
import pandas as pd

de = pd.read_excel('Clase_01/Datos.xlsx')

# You can filter the dataframe by using the where method of the dataframe
# The where method takes a function as an argument
# The function must return a boolean value
# The where method returns a new dataframe
de = de.where(de['Nombre'] == 'Sol')
print('Condition: Nombre = Sol')
print('Dataframe with only the condition visible, and the others values as NaN:')
print(de)

# You can also filter the dataframe by deleting the fields that have a NaN value
de = de[de['Nombre'].notna()]
print('Dataframe with only the condition visible, without the rows that have a NaN as a value in "Nombre":')
print(de)