import graphviz

def flowchart_string_manipulation_abstract():
    dot = graphviz.Digraph(comment='String Manipulation Flowchart (Abstract)', graph_attr={'rankdir': 'TB'})

    # Snippet 1: Convert to Uppercase
    dot.node('A', 'Start Snippet 1', shape='oval')
    dot.node('B', 'Initialize String', shape='rectangle')
    dot.node('C', 'Define Uppercase Lambda Function', shape='rectangle')
    dot.node('D', 'Call Uppercase Lambda', shape='rectangle')
    dot.node('E', 'Print Uppercase Result', shape='rectangle')

    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')

    # Snippet 2: Check if String Starts With
    dot.node('F', 'Start Snippet 2', shape='oval')
    dot.node('G', 'Define Starts With Lambda Function', shape='rectangle')
    dot.node('H', 'Call Starts With Lambda with "PES\'s"', shape='rectangle')
    dot.node('I', 'Print Result (Starts with "P"? - "PES\'s")', shape='rectangle')
    dot.node('J', 'Call Starts With Lambda with "MCOE"', shape='rectangle')
    dot.node('K', 'Print Result (Starts with "P"? - "MCOE")', shape='rectangle')
    dot.node('L', 'End', shape='oval')

    dot.edge('F', 'G')
    dot.edge('G', 'H')
    dot.edge('H', 'I')
    dot.edge('I', 'J')
    dot.edge('J', 'K')

    # Connect the two snippets (optional, can be sequential or separate)
    dot.edge('E', 'F', label='Next Snippet')  # Sequential flow
    dot.edge('K', 'L')

    dot.render('string_manipulation_flowchart_abstract', view=True)  # Save and view the flowchart

if __name__ == "__main__":
    flowchart_string_manipulation_abstract()