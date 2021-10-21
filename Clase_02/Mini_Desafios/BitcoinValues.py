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

def graphicValueOfBitcoin(path:str):
    """[summary]
    Opens the file, reads the data regarding Bitcoin's values and plots it.
    Args:
        path (str): [The path of the file to be read]
    """
    # Import data
    df = pd.read_csv(path, sep=',', encoding='utf-8')
    
    # Get the max value of the bitcoin
    maxValue = df['High'].max()
    # Get the date of the max value
    dateOfMaxValue = df['Date'][df['High'] == maxValue].values[0]
    # Get the index of the max value
    indexHighPrice = df['Date'].values.tolist().index(dateOfMaxValue)
    message = f'The maximum value of Bitcoin was: {round(maxValue,3)} in {dateOfMaxValue}'
    
    plt.plot(df['Date'], df['High'], 'g--', label='High')
    plt.plot(df['Date'], df['Low'], 'r--', label='Low')
    plt.plot(df['Date'], df['Close'], 'b--', label='Close')
    plt.plot(indexHighPrice, maxValue, 'mo', label=f'Max Value ${maxValue}')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title(message)
    plt.tight_layout()
    plt.legend()
    print(f'The maximum value of Bitcoin was: {round(maxValue,3)} in {dateOfMaxValue}')
    plt.show()

if __name__ == "__main__":
    graphicValueOfBitcoin('Clase_02/Mini_Desafios/BTC.csv')