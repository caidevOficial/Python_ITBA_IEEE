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
import MyWget as m

link = 'https://covid.ourworldindata.org/data/ecdc/full_data.csv'
# m.myWget(link)

# Reads a csv, then converts it to a dataframe
df = pd.read_csv('Clase_01/full_data.csv')

# config pandas
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 100)

print(df)

# To know the size of the dataframe (rows, columns) use:
print('To know the size of the dataframe (rows, columns) use:')
print(df.shape)

# To know the amount of cells [Rows x Columns] use:
print('To know the amount of cells use:')
print(df.size)

# To know the info of each column use:
print('To know the info of each column use:')
print(df.info())

# Operates the values of the columns
print('Operates the values of the columns')
res1 = df['new_cases'].sum()/2
res2 = df['total_cases'].max()
print (res1, res2)

# Exclusive selection
print('Exclusive selection, prints the dataframe bassed on a condition.')

print('\nCondition 1: Location = Argentina')
argentinaDF = df[df['location'] == 'Argentina']
print(argentinaDF)

print('\nCondition 2: Prints the days that the new cases = max Cases registered in Argentina')
print(argentinaDF[argentinaDF['new_cases'] == argentinaDF['new_cases'].max()])

