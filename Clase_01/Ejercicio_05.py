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