import csv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = list()
tuples = 0

records = 10000   #default should be total sample size = 164102

filename = input("Enter filename inside anonymized_data folder: ")

with open ("anonymized_data/"+filename) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        consumption = round(float(row['consumption']),2)/ 100
        cluster = round(float(row['cluster_label']),2)

        individual_info = [cluster, consumption]
        data.append(individual_info)

        tuples = tuples+1
        if tuples==records:
            break


df = pd.DataFrame(data, columns=['Cluster', 'Consumption'])
sns.scatterplot(x="Cluster", y="Consumption", data=df)
plt.show()





