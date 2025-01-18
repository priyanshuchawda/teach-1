import plotly.express as px

data = {'Language': ['Python', 'C++', 'Java', 'JavaScript'], 'Users': [215, 130, 245, 210]}
fig = px.pie(data, values='Users', names='Language', title='Programming Language Popularity')
fig.show()
