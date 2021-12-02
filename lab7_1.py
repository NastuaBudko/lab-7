from numpy import *
import matplotlib.pyplot as plt
import pylab


x = linspace(0, 4, 51)
y = (x**(1/2)*sin(10*x))
plt.plot(x, y, 'g--', label='x^(1/2)*sin(10*x)')

plt.axis([0, 4, -2, 2])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік')
plt.legend()

plt.savefig('figure.png')
plt.show()
