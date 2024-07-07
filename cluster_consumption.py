import csv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = list()
partial_record = True
number_of_records = 5000
tuples = 0

with open ("data.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        consumption = round(float(row['consumption']),2)/ 100
        cluster = round(float(row['cluster_label']),2)

        individual_info = [cluster, consumption]
        data.append(individual_info)

        if partial_record is not False:
            tuples = tuples+1
            if tuples == number_of_records:
                break


df = pd.DataFrame(data, columns=['Cluster', 'Consumption'])
sns.scatterplot(x="Cluster", y="Consumption", data=df)
plt.show()





