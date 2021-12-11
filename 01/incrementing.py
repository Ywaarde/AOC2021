data = open('input.txt', 'r').readlines()

measurements = [int(m) for m in data]

prev_m = measurements[0]
incr_v = 0
for measurement in measurements[1:]:
    if measurement > prev_m:
        incr_v += 1
    prev_m = measurement


prev_trio = measurements[0] + measurements[1] + measurements[2]
incr_trio = 0
for m in range(1, 1998):
    trio = measurements[m] + measurements[m + 1] + measurements[m + 2]
    if trio > prev_trio:
        incr_trio += 1
    prev_trio = trio

print('first task')
print(incr_v)

print('second task')
print(incr_trio)