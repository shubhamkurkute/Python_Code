# LinkedList each element is called node and node contains two fields Data and Next
# Data Contains the value to be stored in the node.
# Next contains a reference to next node.
# LinkedList is collection of nodes and First node is called head.
# Last node should have reference to pointing to 'None' to determine the end of list.
# LinkedList stores heterogenous data.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None