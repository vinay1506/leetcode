def linkedlistcycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

# Example usage:
if __name__ == "__main__":
    # Creating a linked list with a cycle for demonstration
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = head.next  # Creating a cycle here

    if linkedlistcycle(head):
        print("Cycle detected in the linked list.")
    else:
        print("No cycle detected in the linked list.")
        