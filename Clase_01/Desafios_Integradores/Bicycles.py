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

def formatTimeString(seconds:int) -> str:
    """
    Converts seconds to a string with the format MM:SS.
    """
    m, s = divmod(seconds, 60)
    return "{:02.0f} minute(s) {:02.0f} seconds".format(m, s)

def getPercentajeTripsNormal(df):
    """
    Calcula el porcentaje de viajes normales.
    """
    percentaje = (df['Estado cerrado'] == 'NORMAL').sum()*100 / len(df)
    print(f"Porcentaje de viajes normales: {round(percentaje, 2)}%")

def medianDurationOfTrip(df):
    """
    Calcula la duración media de los viajes.
    """
    totalSeconds = round(df['Duración'].mean(), 2)
    print(f"Duración media de los viajes: {formatTimeString(totalSeconds)}")

def getAllHoursOfTrips(df):
    """
    Calculate the most common hour of trips.
    """
    differentHours = {}
    amountTrips = 0
    
    # Make a dictionary with the hours as a key and the amount of trips as a value
    for hour in df.to_dict('list')['Fecha de inicio']:
        hour = hour.split(' ')[1]
        if not hour in differentHours:
            differentHours[hour] = 1
        else:
            differentHours[hour] += 1
    # check the amount of trips per hour to get the most common hour
    for k,v in differentHours.items():
        if v > amountTrips:
            amountTrips = v
            mostFrequentHour = k
    print(f"Hora con mas viajes: {mostFrequentHour} con {amountTrips} viaje(s).")

def amountOfUniqueStations(df):
    """
    Calculate the amount of unique stations.
    """
    uniqueStations = df['Id de estación de inicio'].unique()
    print(f"Cantidad de estaciones unicas: {len(uniqueStations)}")

def printStationsByTrips(df):
    """
    Print the stations with the amount of trips.
    """
    stations = df.groupby('Nombre de estación de inicio')['Nombre de estación de inicio'].count()
    stations = stations.sort_values(ascending=False)
    print(stations)

if __name__ == "__main__":
    # Read csv file
    df = pd.read_csv('Clase_01/Desafios_Integradores/recorridos-realizados-2021-sample.csv')
    getPercentajeTripsNormal(df)
    medianDurationOfTrip(df)
    getAllHoursOfTrips(df)
    amountOfUniqueStations(df)
    printStationsByTrips(df)