Class Node:
  def __init__(self, data):
    self.data = data
    self.next = None #default value for next node
    
def count_nodes(head):
  count = 1
  current = head
  while current.next is not None:
    current = current.next
    count=+1
  return count

NodeA = Node(6)
NodeB = Node(3)
NodeC = Node(1)

NodeA.next = NodeB
NodeB.next = NodeC

print("the lenght of linked list is: ")
print(count_nodes(NodeA))
