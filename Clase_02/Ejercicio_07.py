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

# We create our vector
x = np.linspace(0, 3*3.14, 100)
# Then, we create our functions to be plotted
y1 = np.sin(x)
y2 = np.cos(x)

# Set the size of our plot
plt.figure(figsize=(10, 5))

# sets the first column to show the first function
plt.subplot(1, 2, 1)
# Then the title of the plot
plt.title("Sin(x)")
# Then, we plot the function
plt.plot(x, y1, 'b.')
# Then we set the label of the 'X' axis & 'Y' axis
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.subplot(1, 2, 2)
plt.title("Cos(x)")
plt.plot(x, y2, 'rh')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# We can setup the limits of the axis 'X' and 'Y' like:
# min_x, max_x, min_y, max_y
plt.axis([-1, 6, -1, 1])

# Also we can activate the grid like:
plt.grid(True)
# Remember that we need to activate one grid for each subplot

# We can adjust the padding between the plots
plt.tight_layout()

# Finally, we show the plot
plt.show()

