
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

