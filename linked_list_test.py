from linked_list import Node, LinkedList

# Test cases
# Set up some nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Set up a LinkedList
linked_list = LinkedList(node1)
linked_list.append(node2)
linked_list.append(node3)

# Test get_element
print(linked_list.head.next.next.value) # 3
print(linked_list.get_element(3).value) # 3
