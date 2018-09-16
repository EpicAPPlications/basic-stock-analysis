import math
#import numpy
from time import time

seed(20000)
t0 = time()

#Parameters
SO = 100.
K = 105.
T = 1.0
r = 0.05
sigma = 0.2
M = 50
dt = T / M
I = 250000

#Simulating I paths with M time steps
S = zeros((M + 1, I))
S[0] = S0
for t in range (1, M + 1):
    z = random.standard_normal(I) #pseudorandom number generator
    S[t] = S[t - 1] * exp((r - 0.5 * sigma **2) * dt
                             + sigma * math.sqrt(dt) * z)

C0 = math.exp(-r * T) * sum(maximum(S[-1] - K, 0)) / I

#Results output
tnp1 = time() - t0
print "European Option Value %7.3f" % C0
print "Duration in Seconds   %7.3f" % tnp1
