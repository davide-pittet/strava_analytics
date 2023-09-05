import pandas as pd
import seaborn as sns
import json
import datetime
import matplotlib.pyplot as plt


# Retrieve 2022 and 2023 activities
with open('activities2022.json', 'r') as f:
    activities2022_json = json.load(f)

df_2022 = pd.DataFrame(activities2022_json)

with open('activities2023.json', 'r') as f:
    activities2023_json = json.load(f)

df_2023 = pd.DataFrame(activities2023_json)

pd.set_option('display.max_columns', None)
print(list(df_2022.columns))

# Cleaning data
df_2022 = df_2022.iloc[::-1].reset_index(drop=True)
df_2022['average_speed'] = df_2022['average_speed'].multiply(3.6)

date = list()
day_number = [0]
start_day_str = df_2022.loc[0].at['start_date_local']
start_day = datetime.datetime.strptime(start_day_str, '%Y-%m-%dT%H:%M:%SZ')

for ind in range(len(df_2022.index)):
    date_str = df_2022.loc[ind].at['start_date_local']

    year = date_str[0:4]
    month = date_str[5:7]
    day = date_str[8:10]
    date.append(day + '/' + month + '/' + year)

    if ind > 0:
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
        diff = str(date_obj - start_day).split()
        day_number.append(int(diff[0]))


df_2022['start_date'] = date
df_2022['day_number'] = day_number
df_2022['season'] = ['2022 season' for x in range(len(df_2022.index))]


df_2023 = df_2023.iloc[::-1].reset_index(drop=True)
df_2023['average_speed'] = df_2023['average_speed'].multiply(3.6)

date = list()
day_number = [0]
start_day_str = df_2023.loc[0].at['start_date_local']
start_day = datetime.datetime.strptime(start_day_str, '%Y-%m-%dT%H:%M:%SZ')

for ind in range(len(df_2023.index)):
    date_str = df_2023.loc[ind].at['start_date_local']
    year = date_str[0:4]
    month = date_str[5:7]
    day = date_str[8:10]
    date.append(day + '/' + month + '/' + year)

    if ind > 0:
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
        diff = str(date_obj - start_day).split()
        day_number.append(int(diff[0]))

df_2023['start_date'] = date
df_2023['day_number'] = day_number
df_2023['season'] = ['2023 season' for x in range(len(df_2023.index))]


# Flat runs 2022 vs 2023
col = ['distance', 'moving_time', 'total_elevation_gain', 'start_date', 'day_number', 'average_speed',
       'average_heartrate', 'suffer_score', 'average_cadence', 'season']

flat_z2_2022 = df_2022.loc[(df_2022['total_elevation_gain'] < 100) & (131 < df_2022['average_heartrate']) &
                           (df_2022['average_heartrate'] < 150), col]

flat_z2_2023 = df_2023.loc[(df_2023['total_elevation_gain'] < 100) & (131 < df_2023['average_heartrate']) &
                           (df_2023['average_heartrate'] < 150), col]

flat_z2 = pd.concat([flat_z2_2022, flat_z2_2023])

flat_z3_2022 = df_2022.loc[(df_2022['total_elevation_gain'] < 100) & (150 < df_2022['average_heartrate']) &
                           (df_2022['average_heartrate'] < 170), col]

flat_z3_2023 = df_2023.loc[(df_2023['total_elevation_gain'] < 100) & (150 < df_2023['average_heartrate']) &
                           (df_2023['average_heartrate'] < 170), col]

flat_z3 = pd.concat([flat_z3_2022, flat_z3_2023])

# Plotting
sns.set_theme()

sns.relplot(data=flat_z2, x="day_number", y="average_speed", hue='season')
sns.relplot(data=flat_z3, x="day_number", y="average_speed", hue='season')

plt.show()

# Average pace z2, average pace z3, number of runs z2, number of runs z3
flat_z2_mean_2022 = flat_z2_2022['average_speed'].mean()
flat_z3_mean_2022 = flat_z3_2022['average_speed'].mean()
flat_z2_mean_2023 = flat_z2_2023['average_speed'].mean()
flat_z3_mean_2023 = flat_z3_2023['average_speed'].mean()

number_Z2_2022 = len(flat_z2_2022.index)
number_Z3_2022 = len(flat_z3_2022.index)
number_Z2_2023 = len(flat_z2_2023.index)
number_Z3_2023 = len(flat_z3_2023.index)

mean_speed = [flat_z2_mean_2022, flat_z3_mean_2022, flat_z2_mean_2023, flat_z3_mean_2023]
number = [number_Z2_2022, number_Z3_2022, number_Z2_2023, number_Z3_2023]
zone = ['Z2', 'Z3', 'Z2', 'Z3']
season = ['2022', '2022', '2023', '2023']

mean_speed_df = pd.DataFrame({'mean_speed': mean_speed, 'season': season, 'zone': zone, 'number': number})

fig2 = sns.barplot(data=mean_speed_df, x='zone', y='mean_speed', hue='season')
plt.show()

fig3 = sns.barplot(data=mean_speed_df, x='zone', y='number', hue='season')
plt.show()
