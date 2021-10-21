#
# MIT License
#
# Copyright (C) 2021 <FacuFalcone - CaidevOficial>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# You should have received a copy of the MIT license
# along with this program.  If not, see <https://opensource.org/licenses/MIT>.
#
# @author Facundo Falcone <CaidevOficial> 

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
