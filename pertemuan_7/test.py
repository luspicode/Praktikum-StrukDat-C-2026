class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def traversal(head):

    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


def nilai_terkecil(head):

    current = head
    minimum = head.data

    while current:

        if current.data < minimum:
            minimum = current.data

        current = current.next

    return minimum


def delete_node(head, key):

    if head.data == key:
        return head.next

    current = head

    while current.next:

        if current.next.data == key:
            current.next = current.next.next
            return head

        current = current.next

    return head


# membuat linked list
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1


print("Linked List:")
traversal(head)

print("Nilai terkecil:", nilai_terkecil(head))

head = delete_node(head, 3)

print("Setelah hapus 3:")
traversal(head)