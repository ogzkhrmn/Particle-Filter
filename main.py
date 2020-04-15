import numpy as np
import random
from matplotlib import pyplot as plot
import math


def sample(x):
    sum = 0
    for i in range(12):
        sum += random.uniform(-1 * x, x)
    return sum


a1 = 0.001
a2 = 0.001
a3 = 0.001
a4 = 0.001
nSamples = 1000
particles = np.zeros((3, 1000))
signals = [[3, 0, 15], [3, 4, 120], [1, 4, 200]]

plot.scatter(particles[0], particles[1], c=particles[2])

for j in range(3):

    for i in range(1000):
        sigmatrans = math.sqrt(pow(signals[j][0] - particles[0][i], 2) + pow(signals[j][1] - particles[1][i], 2))
        sigmarot1 = math.atan((signals[j][0] - particles[0][i]) / (signals[j][1] - particles[1][i])) - particles[1][i]
        sigmarot2 = signals[j][2] - particles[2][i] - sigmarot1

        sigmarot1u = sigmarot1 + sample(a1 * abs(sigmarot1) + a2 * sigmatrans)
        sigmatransu = sigmatrans + sample(a3 * sigmatrans + a4 * abs(sigmarot1 + sigmarot2))
        sigmarot2u = sigmarot2 + sample(a1 * abs(sigmarot2) + a2 * sigmatrans)

        particles[0][i] = particles[0][i] + sigmatransu * math.cos(particles[2][i] + sigmarot1u)
        particles[1][i] = particles[1][i] + sigmatransu * math.sin(particles[2][i] + sigmarot1u)
        particles[2][i] = particles[2][i] + sigmarot1u + sigmarot2u

    plot.scatter(particles[0], particles[1], c=particles[2])

plot.show()
