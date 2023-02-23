# - - - - - - - SECTION 1: MODULES AND PACKAGES - - - - - - -
# - - - - - - - PCAP-31-03 1.2 Perform evaluations using the math module
import math
import timeit

"""factorial()"""
print(f'\nmath.factorial(4): {math.factorial(4)}')
print(timeit.timeit('output=4*3*2*1'))

"""ceil()"""
print(f'\nmath.ceil(6): {math.ceil(6)}')
print(f'math.ceil(-11): {math.ceil(-11)}')
print(f'math.ceil(4.23): {math.ceil(4.23)}')
print(f'math.ceil(-11.495): {math.ceil(-11.495)}')
print(f'math.ceil(0.99): {math.ceil(0.99)}')
print(f'math.ceil(-0.99): {math.ceil(-0.99)}')

"""floor()"""
print(f'\nmath.floor(4): {math.floor(4)}')
print(f'math.floor(-17): {math.floor(-17)}')
print(f'math.floor(5.532): {math.floor(5.532)}')
print(f'math.floor(-6.432): {math.floor(-6.432)}')
print(f'math.floor(0.99): {math.floor(0.99)}')
print(f'math.floor(-0.99): {math.floor(-0.99)}')

"""trunc()"""
print(f'\nmath.trunc(12.32): {math.floor(12.32)}')
print(f'math.trunc(-43.24): {math.floor(-43.24)}')

"""sqrt()"""
print(f'\nmath.sqrt(64): {math.sqrt(64)}')

"""hypot()"""
print(f'\nmath.hypot(1,1): {math.hypot(1,1)}')
print(f'\nmath.hypot(3,4): {math.hypot(3,4)}')



