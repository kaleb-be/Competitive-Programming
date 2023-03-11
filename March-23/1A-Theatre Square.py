import math

n, m, a = map(int, input().split())

# calculate the number of flagstones needed in each direction
num_flagstones_n = math.ceil(n / a)
num_flagstones_m = math.ceil(m / a)

# calculate the total number of flagstones needed
total_flagstones = num_flagstones_n * num_flagstones_m

print(total_flagstones)
