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

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def graphicPhonePrices(path:str):
    """
    This function is used to plot the graphic of the phone prices as a percentage of the total price.
    """
    df = pd.read_excel(path)
    print(df['Price'].value_counts(normalize=True, ascending=True))
    phoneExpensive = df.loc[df['Price'] == df['Price'].max()]
    phoneCheap = df.loc[df['Price'] == df['Price'].min()]
    
    plt.figure(figsize=(16, 8))
    plt.tight_layout()
    plt.pie(df['Price'].to_list(), labels=df['Model'].to_list(), autopct='%1.1f%%', shadow=True, startangle=90)
    plt.plot(phoneExpensive['Model'], phoneExpensive['Price'], 'y*', label='Expensive Phone')
    plt.plot(phoneCheap['Model'], phoneCheap['Price'], 'm*', label='Cheaper Phone')
    plt.title('Phones Model Prices')
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    graphicPhonePrices('Clase_02/Mini_Desafios/Phones.xlsx')