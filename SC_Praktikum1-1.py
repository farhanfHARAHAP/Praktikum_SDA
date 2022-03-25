
import matplotlib.pyplot as plt
import numpy as np
import time
import random

data = [150, 300, 500, 700, 750, 1000, 1300, 1600, 2000, 2500]
varListRataWaktu = []

print()
print(' Result '.center(50,'='))
print('%2s%20s' % ('Farhan F Harahap','064002100017'))

def formula(x):
    hasil = 0
    for i in range (len(x)-1):
        hasil += abs(x[i+1]-x[i])
    return hasil

print()
print("%12s%16s" % ('Data Size', 'Time(s)'))
print()
varTotalWaktu = 0
for x in range(len(data)):
    a = data[x]
    for i in range(5):
        varRandInt = np.random.randint(0, 1000, a)
        start = time.time()
        formula(varRandInt)
        elapsed = time.time() - start
        varTotalWaktu += elapsed
    varRataWaktu = varTotalWaktu / 5
    varListRataWaktu.append(varRataWaktu)
    print("%12d%16.9f" % (data[x], varRataWaktu))
    
print()
print(' Plot '.center(50,'='))
print()

yPlot = data
xPlot = varListRataWaktu

plt.plot(xPlot,yPlot,color = 'tab:blue')
plt.title('Runtime Result')
plt.show()

    


