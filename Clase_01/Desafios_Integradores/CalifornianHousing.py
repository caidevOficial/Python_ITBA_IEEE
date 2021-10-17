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

def medianHouseValue(df)->None:
    """
    Returns the median house value.
    """
    print(f"- Valor medio de casa: {round(df['median_house_value'].median(), 2)}")

def howManyWithMedianHouseValue(df)->int:
    """
    Returns the number of houses with median house value greater than $80,000 
    and longitude higher or equal than -120 and less or equal to -118.
    """
    valueHigherThan80k = df[df['median_house_value'] > 80000]
    latitudebet120And118 = valueHigherThan80k[((valueHigherThan80k['longitude']>= -120) & (valueHigherThan80k['longitude']<= -118))]
    print(f"- Cantidad de casas con media superior a 80K: {latitudebet120And118.shape[0]}")
    return latitudebet120And118

def averageOfTotalRooms(df)->None:
    """
    Returns the average of total rooms per house.
    """
    print(f"- Promedio de habitaciones por casa: {round(df['total_rooms'].mean(), 2)}")

def mostValueHouse(df)->None:
    """
    Returns the most expensive house.
    """
    howManyExpensive = df[df['median_house_value'] == round(df['median_house_value'].max(), 1)]
    print(f"- Casa mas cara: {round(df['median_house_value'].max(), 1)}")
    print(f"- Cantidad con ese valor: {howManyExpensive.shape[0]}")
    
def varianceOfTotalRooms(df)->None:
    """
    Returns the variance of median house value.
    """
    print(f"- Variacion de habitaciones por casa: {round(df['median_house_value'].var(), 2)}")

if __name__ == "__main__":
    df = pd.read_excel('Clase_01/Desafios_Integradores/california_housing_train.xlsx')
    df_Filtered = howManyWithMedianHouseValue(df)
    averageOfTotalRooms(df_Filtered)
    mostValueHouse(df)
    medianHouseValue(df_Filtered)
    varianceOfTotalRooms(df)
    print("- Fin del programa")
