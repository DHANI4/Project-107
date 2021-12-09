import pandas as pd
import plotly.express as px
import csv

df=pd.read_csv("Data.csv")
p=df.groupby(["student_id","level"],as_index = False).mean
print(p)

fig=px.scatter(p,x="student_id",y="level",size="attempt",color="attempt")
fig.show()