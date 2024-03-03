import statistics

grades=[85, 93, 88, 97, 92, 78, 88, 100, 89, 75]
stddev=statistics.stdev(grades)
print("variance of data is ",statistics.variance(grades,stddev))