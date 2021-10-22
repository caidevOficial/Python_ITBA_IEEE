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
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame

def printPointsOfTeams(newDataFrame:DataFrame):
    """
    Change the number of matches played by 'Velez Sarsfield', 'Boca Juniors', 'River Plate' and 'Estudiantes' to 14.
    Then only prints a dataframe [Team Name and Points] with teams that have its amount of matches different than 14.
    """
    newDataFrame.loc[['Velez Sarsfield', 'Boca Juniors', 'River Plate', 'Estudiantes'], ['Partidos']] = 14
    print(newDataFrame.loc[newDataFrame['Partidos']!=14, ['Puntaje']])

def printTeamsFixedErrors(newDataFrame:DataFrame):
    """
    Prints The erros that were fixed in the dataframe.
    """
    errors = newDataFrame['Diferencia de Gol'] != newDataFrame['Goles Convertidos'] - newDataFrame['Goles Recibidos']
    print(newDataFrame['Error'].mask(errors, 'Si'))

def printSpecificStudent(newDataFrame:DataFrame):
    #newDataFrame = pd.read_excel('Mini_Desafios/alu.xlsx', index_col='Apellido')
    print(newDataFrame)
    df = newDataFrame.to_dict('index')
    print(df['Lopez']['Matematica'])

def printTeams(newDataFrame:DataFrame):
    """
    Prints the teams that have the most amount of matches.
    """
    df = newDataFrame.to_dict('index')
    print(newDataFrame.idxmax()['Goles Recibidos'])

if __name__ == "__main__":
    teams = pd.read_excel('Clase_02/Mini_Desafios/Teams.xlsx', index_col='Equipo')
    students = pd.read_excel('Clase_02/Mini_Desafios/Students.xlsx', index_col='Apellido')
    printTeamsFixedErrors(teams)
    printSpecificStudent(students)
    printPointsOfTeams(teams)
    #printTeams(teams)