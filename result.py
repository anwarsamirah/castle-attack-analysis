import csv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = dict()
tuples = 0

records = 10000   #default should be total sample size = 164102
attack_value = 10

filename = input("Enter filename inside anonymized_data folder: ")

with open ("anonymized_data/"+filename) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        cluster_id = round(float(row['cluster_label']),2)
        consumption = round(float(row['consumption']),2)

        if cluster_id not in data:
            data[cluster_id] = [consumption]
        else:    
            data[cluster_id].append(consumption)

        tuples = tuples+1
        if tuples==records:
            break
        
for key in data:
    total_count = len(data[key])
    maxUsage = max(data[key])
    minUsage = min(data[key])
    avgUsage = round(sum(data[key]) / len(data[key]), 2)
    below_attack_value_count = len(list(filter(lambda x: x < attack_value, data[key])))
    percentage_attack_value = round((below_attack_value_count / total_count) * 100, 2)

    print(f"{key} >>> total_count : {total_count},   maxUsage : {maxUsage},    minUsage : {minUsage},    avgUsage : {avgUsage},     below_attack_value_count : {below_attack_value_count},    percentage_attack_value : {percentage_attack_value}%")
