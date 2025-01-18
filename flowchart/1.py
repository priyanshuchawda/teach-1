from graphviz import Digraph

# Create a directed graph
flowchart = Digraph('SimplifiedAverageMarksFlowchart', format='png')

# Add nodes (steps) to the flowchart
flowchart.node('Start', 'Start', shape='ellipse')
flowchart.node('OpenFile', 'Open students.txt File', shape='rectangle')
flowchart.node('Initialize', 'Initialize Variables\n- total_marks = 0\n- student_count = 0', shape='rectangle')
flowchart.node('ReadLine', 'Read Each Line', shape='rectangle')
flowchart.node('CheckValid', 'Is Line Valid? (3 parts: name, age, marks)', shape='diamond')
flowchart.node('UpdateVars', 'Update Variables\n- total_marks += marks\n- student_count += 1', shape='rectangle')
flowchart.node('CalculateAvg', 'Calculate Average Marks\nIf student_count > 0:\n  average_marks = total_marks / student_count\nElse:\n  average_marks = 0', shape='rectangle')
flowchart.node('WriteOutput', 'Write Average Marks to average_marks.txt', shape='rectangle')
flowchart.node('End', 'End', shape='ellipse')

# Add edges (connections) between the nodes
flowchart.edge('Start', 'OpenFile')
flowchart.edge('OpenFile', 'Initialize')
flowchart.edge('Initialize', 'ReadLine')
flowchart.edge('ReadLine', 'CheckValid')
flowchart.edge('CheckValid', 'UpdateVars', label='Yes')
flowchart.edge('CheckValid', 'CalculateAvg', label='No')
flowchart.edge('UpdateVars', 'ReadLine')
flowchart.edge('CalculateAvg', 'WriteOutput')
flowchart.edge('WriteOutput', 'End')

# Render the flowchart to a file
flowchart.render('simplified_average_marks_flowchart', view=True)