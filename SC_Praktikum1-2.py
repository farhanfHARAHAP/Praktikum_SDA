# Import Here
import time

# Input here
print('By Harahap'.center(20,'='))
print('064002100017'.center(20,'='))
N = 150 + int(input('2 Digit NIM Anda: '))
print()

# The rest go here
print('[Perulangan]'.center(20,'='))
start = time.time()
for index in range(N):
    print(index,end=' ')
endtime = time.time()
elapsed = endtime - start
    
print('\n')
print('Hasil'.center(20,'='))
print('Starting time: %2.5f'%(start))
print('End time: %2.5f'%(endtime))
print('\nWaktu yang dibutuhkan: %2.5f'%(elapsed))

    