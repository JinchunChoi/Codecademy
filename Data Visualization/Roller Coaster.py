import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
df_wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
df_steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

print(df_wood['Rank'], df_steel['Rank'])
