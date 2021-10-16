# MIT License
#
# Copyright (C) 2021 <FacuFalcone - CaidevOficial>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pandas as pd
from MyWget import myWget as m
file = 'https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos.xlsx'
df = pd.read_excel('Clase_01/Datos.xlsx')
# prints the first 5 rows of the dataframe
print(f'{df}\n\n')

# prints an specific row of the dataframe
index = 0
print(f'Student at index {index}')
print(f'{df.loc[index]}\n\n')

# prints an specific column of the dataframe
print(f'Chemistry at index {index}')
print(f"{df.loc[0]['Quimica']}\n\n")

# prints a dictionary with the dataframe
print('Lists of column Legajo')
d = df.to_dict('list')
print(f"{d['Legajo']}\n\n")

print('Obtain the average of values from all the elements of the list.')
print(f"{df.mean()}\n\n")

print('Obtain the average of values from all the elements of the specified key.')
print(f"Average Chemistry: {sum(d['Quimica'])/6}\n\n")

# prints records (rows) with a specific index
print('Record at the index 2 printed as a dict.')
r = df.to_dict('recods')
print(f"{r[2]}\n\n")

print('Prints students one by one.')
for student in r:
    print(f"Student: {[student]}\n")

# Index the dataframe by a specific column instead of the normal numeric index.
frame = pd.read_excel('Clase_01/Datos.xlsx', index_col='Nombre')
student = frame.loc['Sol']

print('Print the dataframe indexed by the column Nombre')
print(f"{frame}\n\n")

print('Print student Sol')
print(student)
print(f"Chemistry note: {student['Quimica']}\n\n")
