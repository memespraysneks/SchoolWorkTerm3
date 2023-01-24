import statistics
import time


num_trials = 10000
times = []
some_values = list(range(100000))
all_values = []

for i in range(num_trials):
    before = time.perf_counter()
    length = len(some_values)//2
    some_values.pop(-1)
    after = time.perf_counter()
    difference = after - before
    times.append(difference*1e6)
all_values.append([statistics.mean(times), statistics.median(times), statistics.stdev(times)])
times = []

for i in range(num_trials):
    before = time.perf_counter()
    length = len(some_values)//2
    some_values.pop(0)
    after = time.perf_counter()
    difference = after - before
    times.append(difference*1e6)
all_values.append([statistics.mean(times), statistics.median(times), statistics.stdev(times)])
times = []

for i in range(num_trials):
    before = time.perf_counter()
    length = len(some_values)//2
    some_values.pop(length)
    after = time.perf_counter()
    difference = after - before
    times.append(difference*1e6)
all_values.append([statistics.mean(times), statistics.median(times), statistics.stdev(times)])
times = []

vals = []
for i in range(num_trials):
    before = time.perf_counter()
    vals.append(1)
    after = time.perf_counter()
    vals.pop()
    difference = after - before
    times.append(difference*1e6)
all_values.append([statistics.mean(times), statistics.median(times), statistics.stdev(times)])
times = []

for i in range(num_trials):
    before = time.perf_counter()
    some_values.append(1)
    after = time.perf_counter()
    some_values.pop()
    difference = after - before
    times.append(difference*1e6)
all_values.append([statistics.mean(times), statistics.median(times), statistics.stdev(times)])
times = []

for i in range(num_trials):
    before = time.perf_counter()
    if 100 in some_values:
        pass
    some_values.pop(length)
    after = time.perf_counter()
    difference = after - before
    times.append(difference*1e6)
all_values.append([statistics.mean(times), statistics.median(times), statistics.stdev(times)])
times = []

print(all_values)