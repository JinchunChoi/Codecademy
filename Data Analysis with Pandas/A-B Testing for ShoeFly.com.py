import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

# print(ad_clicks.head(10))

# utm_count = ad_clicks.groupby('utm_source').user_id.count().reset_index()
# print(utm_count)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
# print(ad_clicks.head())

clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(
columns = 'is_click',
index = 'utm_source',
values = 'user_id').reset_index()

# print(clicks_pivot)
clicks_pivot['percent_clicked'] = (clicks_pivot[True] / (clicks_pivot[True]+clicks_pivot[False]))
# print(clicks_pivot)

# print(ad_clicks.head(10))
exp_count = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(exp_count)

ab_click = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index().pivot(
  columns = 'is_click',
  index = 'experimental_group',
  values = 'user_id').reset_index()
print(ab_click)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

# for A
a_clicks_pivot = a_clicks.groupby(['is_click','day']).user_id.count().reset_index().pivot(
columns = 'is_click',
index = 'day',
values = 'user_id').reset_index()

a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True] / (a_clicks_pivot[True]+a_clicks_pivot[False])

print(a_clicks_pivot)

# for B
b_clicks_pivot = b_clicks.groupby(['is_click','day']).user_id.count().reset_index().pivot(
columns = 'is_click',
index = 'day',
values = 'user_id').reset_index()

b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True] / (b_clicks_pivot[True]+b_clicks_pivot[False])

print(b_clicks_pivot)

# A is better except Tuesday
