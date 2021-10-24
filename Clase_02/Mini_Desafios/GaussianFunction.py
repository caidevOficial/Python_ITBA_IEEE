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

def gaussianFunction(x, mu, sigma):
    """[summary]
    Calculates the value of the gaussian function in the point x.
    Args:
        x (array): [Vector of x values]
        mu (int): [Mean of the gaussian function]
        sigma (int): [Standard deviation of the gaussian function]
    Returns:
        [float]: [Value of the gaussian function]
    """
    return np.exp(-(x - mu)**2 / (2 * sigma**2))

if __name__ == "__main__":
    # Generate a normal distribution with mean 0 and standard deviation 1
    mu, sigma = 0, 1
    x = np.linspace(-5, 5, 100)
    y = gaussianFunction(x, mu, sigma)

    # Graficamos
    plt.plot(x, y, 'b--')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Gaussian Function for range [-5, 5]')
    plt.savefig('Clase_02/Docs/GaussianFunction.png', dpi=300)
    plt.show()

