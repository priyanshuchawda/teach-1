import graphviz

def flowchart_string_manipulation():
    dot = graphviz.Digraph(comment='String Manipulation Flowchart', graph_attr={'rankdir': 'TB'})

    # Snippet 1: Convert to Uppercase
    dot.node('A', 'Start', shape='oval')
    dot.node('B', 'str1 = "Bharat Mata ki Jay!!!"', shape='rectangle')
    dot.node('C', 'Upper_lambda = lambda string: string.upper()', shape='rectangle')
    dot.node('D', 'result1 = Upper_lambda(str1)', shape='rectangle')
    dot.node('E', 'print(result1)', shape='rectangle')

    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')

    # Snippet 2: Check if String Starts With
    dot.node('F', 'Start', shape='oval')
    dot.node('G', "starts_with = lambda string: True if string.startswith('P') else False", shape='rectangle')
    dot.node('H', 'result2_1 = starts_with("PES\'s")', shape='rectangle')
    dot.node('I', 'print(result2_1)', shape='rectangle')
    dot.node('J', 'result2_2 = starts_with(\'MCOE\')', shape='rectangle')
    dot.node('K', 'print(result2_2)', shape='rectangle')
    dot.node('L', 'End', shape='oval')

    dot.edge('F', 'G')
    dot.edge('G', 'H')
    dot.edge('H', 'I')
    dot.edge('I', 'J')
    dot.edge('J', 'K')

    # Connect the two snippets (optional, can be sequential or separate)
    dot.edge('E', 'F', label='Next Snippet')  # Sequential flow
    dot.edge('K', 'L')

    dot.render('string_manipulation_flowchart', view=True)  # Save and view the flowchart

if __name__ == "__main__":
    flowchart_string_manipulation()