import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
df_wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
df_steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

print(df_wood.head())
# print(df_wood['Rank'], df_steel['Rank'])
# print(df_wood[df_wood['Name' == 'El Toro']])
# print(df_wood[df_wood.Name == 'El Toro'])
def coaster_rank(coaster_name, park_name, df):
  rank = df_wood[(df_wood['Name'] == coaster_name) & (df_wood['Park'] == park_name)].Rank  
  year = df_wood[(df_wood['Name'] == coaster_name) & (df_wood['Park'] == park_name)]['Year of Rank']
  ax = plt.subplot()  
  ax.invert_yaxis()
  plt.plot(year, rank, marker='o')
  plt.show()
  
# coaster_rank('El Toro', 'Six Flags Great Adventure', df_wood)

def coaster2_rank(c1, c2, p1, p2, df):
  rank1 = df_wood[(df_wood['Name'] == c1) & (df_wood['Park'] == p1)].Rank  
  year1 = df_wood[(df_wood['Name'] == c1) & (df_wood['Park'] == p1)]['Year of Rank']
  rank2 = df_wood[(df_wood['Name'] == c2) & (df_wood['Park'] == p2)].Rank  
  year2 = df_wood[(df_wood['Name'] == c2) & (df_wood['Park'] == p2)]['Year of Rank']
  ax = plt.subplot()  
  ax.invert_yaxis()
  plt.plot(year1, rank1, color='r', label=c1)
  plt.plot(year2, rank2, color='b', label=c2)
  plt.legend()
  plt.show()
# coaster2_rank('El Toro', 'Boulder Dash', 'Six Flags Great Adventure', 'Lake Compounce', df_wood)


def top_rank(n, df):
  top_n_rank = df[df['Rank'] <= n]
  ax = plt.subplot()
  for coaster in set(top_n_rank['Name']):
    coaster_rank = top_n_rank[top_n_rank['Name'] == coaster]    
    ax.plot(coaster_rank['Year of Rank'], coaster_rank['Rank'],label = coaster)
  ax.invert_yaxis()
  plt.legend()
  plt.show()
# top_rank(5, df_wood)


rc_df = pd.read_csv('roller_coasters.csv')
print(rc_df.head())

def rc_hist(df):
  heights = df[df['height'] <= 140].dropna()
  # heights = rc_df[rc_df['height'] <= 140]
  plt.hist(heights['height'])
  plt.show()
# rc_hist(rc_df)


def rc_bar(park_name, df):
  park_coasters = df[df['park'] == park_name]
  park_coasters = park_coasters.sort_values('num_inversions', ascending=False)
  coaster_names = park_coasters['name']
  number_inversions = park_coasters['num_inversions']
  plt.bar(range(len(coaster_names)), number_inversions)
  plt.show()
# rc_bar('Parc Asterix', rc_df)


def rc_pie(df):
  oper_coaster = df[df['status'] == 'status.operating']
  close_coaster = oper_coaster = df[df['status'] == 'status.closed.definitely']
  status_counts = [len(oper_coaster), len(close_coaster)]
  plt.pie(status_counts, autopct='%0.1f%%', labels = ['Operating', 'Closed'])
  plt.show()
# rc_pie(rc_df)
  

def rc_scatter(df):
  df = df[df['height'] < 140].dropna()
  height = df['height']
  speed = df['speed']
  print(height, speed)
  plt.scatter(height, speed)
  plt.show()
rc_scatter(rc_df)
  
