class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverselinkedlist(head : 'Node') -> 'Node':
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Example usage:
if __name__ == "__main__":
    # Creating a linked list: 1 -> 2 -> 3 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    # Reversing the linked list
    new_head = reverselinkedlist(head)

    # Printing the reversed linked list: 3 -> 2 -> 1 -> None
    current = new_head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

