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

    

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)  # Create a new node 
        new_node.next = self.head  # Next for new node becomes the   current head
        self.head = new_node  # Head now points to the new node

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
            return
        last = self.head 
        while last.next:  # Otherwise, traverse the list to find the last node
            last = last.next
        last.next = new_node  # Make the new node the next node of the last node

    def printList(self):
        temp = self.head # Start from the head of the list
        while temp:
            print(temp.data,end=' ') # Print the data in the current node
            temp = temp.next # Move to the next node
        print()  # Ensures the output is followed by a new line

if __name__ == '__main__':
    # Create a new LinkedList instance
        llist = LinkedList()

        # Insert each letter at the beginning using the method we created
        llist.insertAtBeginning('fox') 
        llist.insertAtBeginning('brown') 
        llist.insertAtBeginning('quick')  
        llist.insertAtBeginning('the')  
        llist.insertAtEnd("is mad")

    # Now 'the' is the head of the list, followed by 'quick', then 'brown' and 'fox'

    # Print the list
        llist.printList()
