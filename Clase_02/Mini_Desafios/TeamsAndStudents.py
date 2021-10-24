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
import numpy as np

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
    #newDataFrame = pd.read_excel('Docs/alu.xlsx', index_col='Apellido')
    print(newDataFrame)
    df = newDataFrame.to_dict('index')
    print(df['Lopez']['Matematica'])

def printTeams(newDataFrame:DataFrame):
    """
    Prints the teams that have the most amount of matches.
    """
    df = newDataFrame.to_dict('index')
    print(newDataFrame.idxmax()['Goles Recibidos'])

def printTeamsNoNaN(newDataFrame:DataFrame):
    """
    Prints Teams that have no NaN values.
    """
    df = newDataFrame.to_dict('index')
    print(newDataFrame.dropna(subset=['Puntaje', 'Diferencia de Gol']))

def printApprovedStudents(newDataFrame:DataFrame):
    """
    Prints the students that have a score greater than or equal to 70.
    """
    df = newDataFrame
    print(df['Nombre'].value_counts().idxmax())
    df2 = df[(df['P1']>=6) & (df['P2']>=6) & (df['TP']>=6)]
    print(df2)

def testMatrix():
    table = np.array([[4, 6, 5], [8, 8, 8], [5, 7, 8]])
    df = pd.DataFrame(table, columns=['Matematica', 'Fisica', 'Quimica'])

    df2 = pd.DataFrame(df, columns=['Quimica', 'Matematica'])
    df2.to_excel('Clase_02/Docs/aluTest.xlsx')

if __name__ == "__main__":
    teams = pd.read_excel('Clase_02/Docs/Teams.xlsx', index_col='Equipo')
    teamsNaN = pd.read_excel('Clase_02/Docs/TeamsNaN.xlsx', index_col='Equipo')
    students = pd.read_excel('Clase_02/Docs/Students.xlsx', index_col='Apellido')
    students2 = pd.read_excel('Clase_02/Docs/Students2.xlsx', index_col='Legajo')
    printTeamsFixedErrors(teams)
    printSpecificStudent(students)
    printPointsOfTeams(teams)
    #printTeams(teams)
    printTeamsNoNaN(teamsNaN)
    printApprovedStudents(students2)
    testMatrix()