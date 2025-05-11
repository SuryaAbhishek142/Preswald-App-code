import pandas as pd
import plotly.express as px
from preswald import connect, get_df, table, text, plotly

connect()

df = pd.read_csv('data/student_depression_dataset.csv')  # Local read


filtered_df = df[(df['Academic Pressure'] >= 4) & (df['Work Pressure'] >= 4)]
text("# My Data Analysis App")

fig = px.scatter(df, x='Age', y='CGPA', color='Depression',
                 title='Age vs. CGPA colored by Depression',
                 labels={'Age': 'Age', 'CGPA': 'CGPA'})

fig.update_traces(textposition='top center', marker=dict(size=12))
fig.update_layout(template='plotly_white')

plotly(fig)
table(df)