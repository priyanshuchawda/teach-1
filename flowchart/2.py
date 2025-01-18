import pydot

# Create a graph
graph = pydot.Dot(graph_type='digraph')

# Define nodes
start = pydot.Node('Start', shape='ellipse')
initialize = pydot.Node('Initialize', shape='rectangle', label='Initialize Variables\n- total_marks = 0\n- num_students = 0')
open_file = pydot.Node('OpenFile', shape='rectangle', label='Open Input File\nOpen students.txt in read mode')
check_lines = pydot.Node('CheckLines', shape='diamond', label='Are there lines in the file to process?')
process_line = pydot.Node('ProcessLine', shape='rectangle', label='Process Line\nRead a line and strip unnecessary spaces\nSplit the line into name, age, and marks')
validate_format = pydot.Node('ValidateFormat', shape='diamond', label='Is the line properly formatted (contains 3 parts)?')
update_variables = pydot.Node('UpdateVariables', shape='rectangle', label='Update Variables\nConvert marks to an integer or float\nAdd marks to total_marks\nIncrement num_students by 1')
calculate_average = pydot.Node('CalculateAverage', shape='rectangle', label='Calculate Average Marks\nIf num_students > 0, calculate:\naverage_marks = total_marks / num_students\nOtherwise, set average_marks = 0')
write_output = pydot.Node('WriteOutput', shape='rectangle', label='Write to Output File\nOpen average_marks.txt in write mode\nWrite: "Average Marks: {average_marks:.2f}"')
end = pydot.Node('End', shape='ellipse')

# Add nodes to the graph
graph.add_node(start)
graph.add_node(initialize)
graph.add_node(open_file)
graph.add_node(check_lines)
graph.add_node(process_line)
graph.add_node(validate_format)
graph.add_node(update_variables)
graph.add_node(calculate_average)
graph.add_node(write_output)
graph.add_node(end)

# Add edges
graph.add_edge(pydot.Edge(start, initialize))
graph.add_edge(pydot.Edge(initialize, open_file))
graph.add_edge(pydot.Edge(open_file, check_lines))
graph.add_edge(pydot.Edge(check_lines, process_line, label='Yes'))
graph.add_edge(pydot.Edge(check_lines, calculate_average, label='No'))
graph.add_edge(pydot.Edge(process_line, validate_format))
graph.add_edge(pydot.Edge(validate_format, update_variables, label='Yes'))
graph.add_edge(pydot.Edge(validate_format, check_lines, label='No'))
graph.add_edge(pydot.Edge(update_variables, check_lines))
graph.add_edge(pydot.Edge(calculate_average, write_output))
graph.add_edge(pydot.Edge(write_output, end))

# Save the flowchart to a file
graph.write_png('average_marks_flowchart_pydot.png')
