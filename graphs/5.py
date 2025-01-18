import altair as alt
import pandas as pd

data = pd.DataFrame({
    'Language': ['Python', 'C++', 'Java', 'JavaScript'],
    'Users': [215, 130, 245, 210]
})

alt.Chart(data).mark_bar().encode(
    x='Language',
    y='Users'
).properties(title="Programming Language Popularity").show()
