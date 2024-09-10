# Dataset
data = [79, 65, 67, 45, 67]

# Map Function
def map_function(values):
    mapped_data = []
    for value in values:
        mapped_data.append(("Rata-rata", (value, 1)))
    return mapped_data

# Reduce Function
def reduce_function(mapped_data):
    total_sum = 0
    total_count = 0
    for key, (value, count) in mapped_data:
        total_sum += value
        total_count += count
    average = total_sum / total_count
    return ("Rata-rata", average)

# Proses MapReduce
mapped_data = map_function(data)
result = reduce_function(mapped_data)
print(result)
