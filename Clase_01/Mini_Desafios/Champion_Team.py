#*
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
from pandas.core.frame import DataFrame
from Soccer_Team import findDifference as fd

def findChampionTeam(df):
    """
    Find the champion of the team.
    """
    return df.loc[df['Puntos'] == df['Puntos'].max()]

def findLoserTeam(df):
    """
    Find the loser team.
    """
    return df.loc[df['Puntos'] == df['Puntos'].min()]

if __name__ == "__main__":
    # Read the data
    df = pd.read_excel('Clase_01/Docs/Soccer.xlsx')
    # Updates the goals difference
    df = fd(df)

    # Find the champion
    champion = findChampionTeam(df)
    # Print the result
    print('Champion:')
    print(champion)
    
    # Find the loser
    loser = findLoserTeam(df)
    # Print the result
    print('Loser:')
    print(loser)