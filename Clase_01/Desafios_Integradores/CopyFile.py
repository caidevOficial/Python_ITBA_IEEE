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

import os
import shutil

def copyFile(src) -> bool:
    """[summary]
    This function copies a file from a source to a destination.
    Args:
        src (str): [Name of the source file to be copied]

    Returns:
        bool: [True if the file was copied successfully, False otherwise]
    """
    for i in range(1, 20):
        actualFileName = src.split('/')[-1]
        prefix = f'Copy {i} - '
        newFileName = f'{prefix}{actualFileName}'
        pathToCopy = f'{src.replace(actualFileName, newFileName)}'
        if not os.path.exists(pathToCopy):
            #newFileName = src.replace(src, pathToCopy)
            shutil.copy(src, pathToCopy)
            return True
    return False

if __name__ == '__main__':
    if copyFile('Clase_01/Desafios_Integradores/Docs/Datos.xlsx'):
        print('File copied successfully')
    else:
        print('File not found')