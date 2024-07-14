import csv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = dict()
attack_value_list = list()
tuples = 0

records = 164102   #default should be total sample size = 164102
attack_value = 7

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
        if tuples == records:
            break
        
for key in data:
    total_count = len(data[key])
    maxUsage = max(data[key])
    minUsage = min(data[key])
    avgUsage = round(sum(data[key]) / len(data[key]), 2)
    below_attack_value_count = len(list(filter(lambda x: x < attack_value, data[key])))
    percentage_attack_value = round((below_attack_value_count / total_count) * 100, 2)

    attack_value_list.append([key, percentage_attack_value])

    print(f"{key} >>> total_count : {total_count},   maxUsage : {maxUsage},    minUsage : {minUsage},    avgUsage : {avgUsage},     below_attack_value_count : {below_attack_value_count},    percentage_attack_value : {percentage_attack_value}%")

#print(attack_value_list)

df = pd.DataFrame(attack_value_list, columns=['Cluster_label', 'Percentage'])
#print(df.head())


#sns.barplot(x= "Cluster_label", y = "Percentage", data = df)




#sns.displot(data=df, x='Cluster_label', weights='Percentage', discrete=True, shrink=.8)



# sns.displot(
#     data=df,
#     x='Cluster_label',
#     weights='Percentage',
#     hue='Cluster_label',
#     kde=True,
#     height=4,
#     aspect=2
# )


sns.kdeplot(df['Percentage'])

# plt.title("Plot for percentage of attack value = 7")
# plt.xlabel("Cluster")
# plt.ylabel("Percentage")
plt.show()
