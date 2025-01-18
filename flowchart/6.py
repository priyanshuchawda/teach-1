import graphviz

def flowchart_stack_operations_short():
    dot = graphviz.Digraph(comment='Stack Operations Flowchart (Short)', graph_attr={'rankdir': 'TB'})

    # Nodes
    dot.node('A', 'Start', shape='oval')
    dot.node('B', 'stack = []', shape='rectangle')
    dot.node('C', 'Display Menu', shape='parallelogram')
    dot.node('D', 'Get Choice', shape='input')
    dot.node('E', 'Choice?', shape='diamond')
    dot.node('F1', 'Push Item', shape='rectangle')
    dot.node('F2', 'Pop Item', shape='rectangle')
    dot.node('F3', 'Display Stack', shape='rectangle')
    dot.node('F4', 'Exit', shape='rectangle')
    dot.node('G', 'End', shape='oval')
    dot.node('X', 'Invalid Choice', shape='output')

    # Edges
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')

    dot.edge('E', 'F1', label='1')
    dot.edge('F1', 'C')

    dot.edge('E', 'F2', label='2')
    dot.edge('F2', 'C')

    dot.edge('E', 'F3', label='3')
    dot.edge('F3', 'C')

    dot.edge('E', 'F4', label='4')
    dot.edge('F4', 'G')

    dot.edge('E', 'X', label='Other')
    dot.edge('X', 'C')

    dot.render('stack_operations_flowchart_short', view=True)

if __name__ == "__main__":
    flowchart_stack_operations_short()