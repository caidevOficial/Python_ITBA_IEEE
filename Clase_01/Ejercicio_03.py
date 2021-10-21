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
import random as rd

# Make a dataframe

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Pass': ['qwerty', 'asdfgh', 'zxcvbn', 'qwerty'],
    'Random': []
}

# Sets a random number for each row
for i in range(4):
    data['Random'].append(rd.randint(0, 100))

# Prints the dictionary before the conversion to dataframe
print('Prints the dictionary before the conversion to dataframe')
print(data)

# Converts the dictionary to dataframe
df = pd.DataFrame(data)

# Prints the dataframe
print('Prints the dictionary as a dataframe')
print(df)

# Saves the dataframe to a csv file
df.to_csv('data.csv', index=False)

# Saves the dataframe to a excel file
df.to_excel('data.xlsx', index=False)

# Saves the dataframe to a html file
df.to_html('data.html', index=False)

# Saves the dataframe to a json file
df.to_json('data.json', orient='records')

# Saves the dataframe to a sql file
df.to_sql('data', con=None, flavor='sqlite', if_exists='replace', index=True, index_label=None, chunksize=None, dtype=None)

