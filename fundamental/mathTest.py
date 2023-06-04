# Division is decimal by default
print('5 / 2 = ', 5 / 2)

# Double slash rounds down
print('5 // 2 = ', 5 // 2)

# Most languages round toward 0 by default
# but Python always round down even for negative numbers
print('-3 // 2 = ', -3 // 2)

# A workaround for rounding toward 0 is using decimal division
# and then convert to int
print('int(-3 / 2) = ', int(-3 / 2))

# Modulo is similar to other languages
print('10 % 3 = ', 10 % 3)

# Except for negative value
print('-10 % 3 = ', -10 % 3)

# To be consistent with other languages' modulo
import math
print('math.fmod(-10, 3) = ', math.fmod(-10, 3))

# More math helper
print('math.floor(3 / 2) = ', math.floor(3 / 2))
print('math.ceil(3 / 2) = ', math.ceil(3 / 2))
print('math.sqrt(2) = ', math.sqrt(2))
print('math.pow(2, 3) = ', math.pow(2, 3))

# Max, min int
print('Max Int = ', float('inf'))
print('Min Int = ', float('-inf'))

# Python numbers are infinite so they never overflow
print('math.pow(2, 200) = ', math.pow(2, 200))

# But it's still less than inf
print('Is math.pow(2, 3) less than inf? ', math.pow(2, 200) < float('inf'))