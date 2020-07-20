"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        # Your code goes here
        else:
            self.head = new_element
            
    def get_position(self, position):
        count = 1
        temp = self.head
        while temp and count <= position:
            if count == position:
                return temp
            else:
                temp = temp.next
                count = count + 1
        return None 
        
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        pass
    
    def insert(self, new_element, position):
        count = 1
        temp = self.head
        if position > 1:
            while temp and count < position:
                if count == position-1:
                    new_element.next = temp.next
                    temp.next = new_element
                temp = temp.next
                count = count +1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        pass
    
    
    def delete(self, value):
        
        temp = self.head
        last = None
        if temp.value == value:
            if last:
                last.next = temp.next
            else:
                self.head = temp.next


        """Delete the first node with a given value."""
        # Your code goes here
        pass
