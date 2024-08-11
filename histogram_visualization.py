import csv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import statistics
import numpy as np


data = dict()
attack_value_list = list()
tuples = 0

records = 164102  # default should be total sample size = 164102


filename = input("Enter filename inside anonymized_data folder: ")

with open("anonymized_data/" + filename) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        cluster_id = round(float(row['cluster_label']), 2)
        consumption = round(float(row['consumption']), 2)

        if cluster_id not in data:
            data[cluster_id] = [consumption]
        else:
            data[cluster_id].append(consumption)

        tuples = tuples + 1
        if tuples == records:
            break

for key in data:
    total_count = len(data[key])
    maxUsage = max(data[key])
    minUsage = min(data[key])
    avgUsage = round(sum(data[key]) / len(data[key]), 2)
    stanDev = round(statistics.stdev(data[key]))

    attack_value_list.append([key, stanDev])

    #print(f"{key} >>> total_count : {total_count},   maxUsage : {maxUsage},    minUsage : {minUsage},    avgUsage : {avgUsage}, standard_deviation : {stanDev}")
#(attack_value_list)


df = pd.DataFrame(attack_value_list, columns=['Cluster_label', 'standard_deviation'])

# Plotting a histogram with density plot
sns.histplot(df['standard_deviation'], bins=30, kde=True, color='green', edgecolor='black')


# Adding labels and title
plt.xlabel('Standard Deviation')
plt.ylabel('Density')
#plt.title('Histogram with density plot')

# Display the plot
plt.show()
