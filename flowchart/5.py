import graphviz

def flowchart_string_manipulation_improved_snippet2():
    dot = graphviz.Digraph(comment='String Manipulation Flowchart (Improved Snippet 2)', graph_attr={'rankdir': 'TB'})

    # Snippet 1: Convert to Uppercase (Keeping this part for context if needed)
    dot.node('A', 'Start Snippet 1', shape='oval')
    dot.node('B', 'Initialize String', shape='rectangle')
    dot.node('C', 'Define Uppercase Lambda', shape='rectangle')
    dot.node('D', 'Call Uppercase Lambda', shape='rectangle')
    dot.node('E', 'Print Uppercase Result', shape='rectangle')

    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')

    # Snippet 2: Check if String Starts With (Improved)
    dot.node('F', 'Start Snippet 2', shape='oval')
    dot.node('G', 'Define Starts With Lambda', shape='rectangle')
    dot.node('H1', 'Call Starts With Lambda with "PES\'s"', shape='rectangle')
    dot.node('D1', 'Does "PES\'s" start with "P"?', shape='diamond')
    dot.node('I1_yes', 'Return True', shape='rectangle')
    dot.node('I1_no', 'Return False', shape='rectangle')
    dot.node('J1', 'Print Result (True)', shape='rectangle')

    dot.node('H2', 'Call Starts With Lambda with "MCOE"', shape='rectangle')
    dot.node('D2', 'Does "MCOE" start with "P"?', shape='diamond')
    dot.node('K1_yes', 'Return True', shape='rectangle')
    dot.node('K1_no', 'Return False', shape='rectangle')
    dot.node('L1', 'Print Result (False)', shape='rectangle')

    dot.node('M', 'End', shape='oval')

    dot.edge('F', 'G')
    dot.edge('G', 'H1')
    dot.edge('H1', 'D1')
    dot.edge('D1', 'I1_yes', label='Yes')
    dot.edge('D1', 'I1_no', label='No')
    dot.edge('I1_yes', 'J1')
    dot.edge('I1_no', 'J1')

    dot.edge('G', 'H2') # Edge from lambda definition to the second call
    dot.edge('H2', 'D2')
    dot.edge('D2', 'K1_yes', label='Yes')
    dot.edge('D2', 'K1_no', label='No')
    dot.edge('K1_yes', 'L1')
    dot.edge('K1_no', 'L1')

    # Connect the two snippets (optional, can be sequential or separate)
    dot.edge('E', 'F', label='Next Snippet')  # Sequential flow
    dot.edge('J1', 'M')
    dot.edge('L1', 'M')

    dot.render('string_manipulation_flowchart_improved_snippet2', view=True)  # Save and view the flowchart

if __name__ == "__main__":
    flowchart_string_manipulation_improved_snippet2()