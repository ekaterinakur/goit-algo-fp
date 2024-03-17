class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    # 1. Реверсування однозв'язного списку, змінюючи посилання між вузлами
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 2. Алгоритм сортування вставками для однозв'язного списку
    def sorted_insert(self, sorted_head, new_node):
        if not sorted_head or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            return new_node

        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return sorted_head


    def insertion_sort(self):
        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            sorted_head = self.sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# 3. Об'єднання двох відсортованих однозв'язних списків в один відсортований список
def merge_sorted_lists(head1, head2):
    dummy_node = Node()
    tail = dummy_node

    while True:
        if not head1:
            tail.next = head2
            break
        if not head2:
            tail.next = head1
            break

        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next

    return dummy_node.next

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

list1 = [33, 20, 15, 10, 5]
list2 = [3, 8, 15, 18, 26]

def main():
    llist1 = LinkedList()
    for el in list1:
        llist1.insert_at_end(el)

    llist2 = LinkedList()
    for el in list2:
        llist2.insert_at_end(el)

    print("Перший вихідний список:")
    llist1.print_list()
    print("Другий вихідний список:")
    llist2.print_list()

    # Реверсування першого списку
    llist1.reverse()
    print("Після реверсування першого списку:")
    llist1.print_list()

    # Сортування першого списку
    llist1.insertion_sort()
    print("Після сортування вставками першого списку:")
    llist1.print_list()

    # Об'єднання відсортованих списків
    merged_head = merge_sorted_lists(llist1.head, llist2.head)
    print("Після об'єднання відсортованих списків:")
    print_linked_list(merged_head)

if __name__ == "__main__":
    main()
