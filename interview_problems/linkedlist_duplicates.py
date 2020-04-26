# Write a method called remove_duplicates() that removes all duplicate nodes from a sorted linked list

# i need to start at the beginning(head) and check
# if the data are the same remove the node 
# then set the pointer to the next one and 
# then check the next node until
# all the nodes pointing to data are unique

def duplicate_checker(self):
    current = self.head
    
    while current.next != None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
            
            
            
            
    