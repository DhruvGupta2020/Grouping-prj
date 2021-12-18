import pandas as pd
import plotly.express as px
df = pd.read_csv("data.csv")
g = df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
print(g)

s=px.scatter(g, x="student_id", y="level" ,color="attempt",size="attempt")
s.show()
