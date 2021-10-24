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

def graphicGooAMZActions(dfG, dfA):
    """
    Function that plots the Google Actions vs Amazon Actions
    """
    plt.figure(figsize=(16, 8))
    amz = dfA.to_dict('list')
    goo = dfG.to_dict('list')

    gooX = [goo['Date'][0]]
    gooY = [goo['Open'][0]]
    amzX = [amz['Date'][0]]
    amzY = [amz['Open'][0]]

    # Define two list to save the points where the lines cross
    crossX = []
    crossY = []

    for i in range(1, len(goo['Date'])):
        gooX.append(goo['Date'][i])
        gooY.append(goo['Open'][i])
        amzX.append(amz['Date'][i])
        amzY.append(amz['Open'][i])

        if gooY[i] == amzY[i] or (gooY[i] > amzY[i] and gooY[i-1] < amzY[i-1]) or (gooY[i] < amzY[i] and gooY[i-1] > amzY[i-1]):
            crossX.append(gooX[i])
            crossY.append(gooY[i])
    
    plt.plot(gooX, gooY, 'r', label='Google Actions')
    plt.plot(amzX, amzY, 'b', label='Amazon Actions')
    plt.plot(crossX, crossY, 'm*', label='Same Value Actions')
            
    plt.xticks(gooX[::150], rotation=45, ha='right')
    plt.tight_layout()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    dfG = pd.read_csv('Clase_02/Docs/GOOGLE.csv')
    dfA = pd.read_csv('Clase_02/Docs/AMZN.csv')
    graphicGooAMZActions(dfG, dfA)