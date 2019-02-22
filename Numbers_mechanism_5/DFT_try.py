import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n = int(input('Enter the number of points for which the curve has to be drawn\t'))
x,y = [],[]

for i in range(n):
	ip = list(map(float,input('Enter the x and y co-rdinates separated by a space :\t').split()))
	x.append(ip[0]),y.append(ip[1])
	
a = np.fft.fft(np.array(x) + 1j * np.array(y))
freqs = np.fft.fftfreq(n)
print(a),print(freqs)

t = np.linspace(0.0, 2 * np.pi, 1000)
vals = np.sum(a / n * np.exp(1j * np.multiply.outer(t, n * freqs)), axis=1)

plt.plot(vals.real, vals.imag, "-")
plt.plot(x,y, ".")
plt.axis("equal")
plt.show()

