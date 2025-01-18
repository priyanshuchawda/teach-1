import pygal

pie_chart = pygal.Pie()
pie_chart.title = 'Programming Language Popularity'
pie_chart.add('Python', 215)
pie_chart.add('C++', 130)
pie_chart.add('Java', 245)
pie_chart.add('JavaScript', 210)
pie_chart.render_in_browser()  # Opens in a web browser
