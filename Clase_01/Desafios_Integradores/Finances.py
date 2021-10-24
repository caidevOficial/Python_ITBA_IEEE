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
from pandas.core.frame import DataFrame

def updateTransactions(users, transactions) -> DataFrame:
    """
    Updates the values of the transactions of the users.
    """
    for transaction in transactions:
        em = transaction['Emisor']
        rec = transaction['Receptor']
        amount = transaction['Monto']
        users[em]['Presupuesto'] -= amount
        users[rec]['Presupuesto'] += amount

    return pd.DataFrame.from_dict(users, orient='index')

if __name__ == "__main__":
    # Read the data
    users_file = pd.read_excel("Clase_01/Docs/Finanzas.xlsx", "Usuarios", index_col="Usuario")
    transactions_file = pd.read_excel("Clase_01/Docs/Finanzas.xlsx", "Transferencias")

    users = users_file.to_dict('index')
    transactions = transactions_file.to_dict('records')

    print('Original DF Users: ')
    print(users_file)
    print('Original DF Transactions: ')
    print(transactions_file)

    print('Modified DF: ')
    print(updateTransactions(users, transactions))

