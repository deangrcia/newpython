import math

sample = [85, 90, 78, 92, 88]
sample_sum = 0
sample_size = len(sample)
mean = sum(sample)/sample_size
range = max(sample) - min(sample)
value_minus_mean_squared_total = 0

for show in sample:
    show -= mean
    value_minus_mean_squared_total += math.pow(show, 2)

variance = round(value_minus_mean_squared_total/(sample_size-1),2)
standard_deviation = round(math.sqrt(variance),2)


print(f"Range: {range}")
print(f"Mean: {mean}")
print(f"Standard Deviation: {standard_deviation}")
print(f"Variance: {variance}")