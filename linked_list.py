class Node:
   def __init__(self, data):
       self.data = data
       self.next = None
class LinkedList:
    def __init__(self):
       self.head = None
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    def remove_first(self):
        if self.head is None:
            return
        self.head = self.head.next
    def remove_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert(self, prev_node, data):
        if not prev_node:
            print("The given previous node must be in LinkedList.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

class sinhvien:
    def __init__(self, maSV, tenSV, NamSinh, GPA):
        self.maSV = maSV
        self.tenSV = tenSV
        self.NamSinh = NamSinh
        self.GPA = GPA
    def __str__(self):
        return f"MaSV: {self.maSV}, TenSV: {self.tenSV}, NamSinh: {self.NamSinh}, GPA: {self.GPA}"
    
def mergesort(linked_list):
    if linked_list.head is None or linked_list.head.next is None:
        return linked_list

    def split(head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None
        return head, middle

    def merge(left, right):
        dummy = Node(None)
        tail = dummy
        while left and right:
            if left.data.GPA <= right.data.GPA:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        return dummy.next

    def merge_sort_rec(head):
        if head is None or head.next is None:
            return head
        left, right = split(head)
        left = merge_sort_rec(left)
        right = merge_sort_rec(right)
        return merge(left, right)

    sorted_head = merge_sort_rec(linked_list.head)
    sorted_list = LinkedList()
    sorted_list.head = sorted_head
    return sorted_list
sv1 = Node(sinhvien("202412474", "Nguyen Van Anh", 2000, 2.1))
sv2 = Node(sinhvien("202412475", "Tran Thi Binh", 1999, 3.8))
sv3 = Node(sinhvien("202412476", "Le Van Cuong", 2001, 3.2))
sv4 = Node(sinhvien("202412477", "Pham Thi Duyen", 2000, 3.9))
sv5 = Node(sinhvien("202412478", "Hoang Van Em", 1998, 2.9))
sv6 = Node(sinhvien("202412479", "Vu Thi Giang", 2001, 3.6))
sv7 = Node(sinhvien("202412480", "Dang Van Hung", 1999, 3.4))
sv8 = Node(sinhvien("202412481", "Bui Thi Hoa", 2000, 3.7))
sv9 = Node(sinhvien("202412482", "Do Van Khoa", 1998, 2.0))
sv10 = Node(sinhvien("202412483", "Phan Thi Lan", 2001, 3.3))
sv11 = Node(sinhvien("202412484", "Truong Van Minh", 1999, 2.4))
list_sv = LinkedList()
for sv in [sv1, sv2, sv3, sv4, sv5, sv6, sv7, sv8, sv9, sv10]:
    list_sv.add_last(sv.data)
list_sv.display()
print("So sinh vien:", len(list_sv))
a = 0
for sv in list_sv:
    if sv.GPA > 3.2:
        a += 1
print("So sinh vien co GPA > 3.2:", a)

list_sv_sorted = mergesort(list_sv)
print("Danh sach sinh vien sau khi sap xep theo GPA:")
for sv in list_sv_sorted:
    print(sv)

current = list_sv_sorted.head
while current:
    if current.next.data.GPA > sv11.data.GPA:
        sv_tiep = current.next
        current.next = sv11
        sv11.next = sv_tiep
        break
    current = current.next
print("Danh sach sinh vien sau khi them sinh vien moi:")
for sv in list_sv_sorted:
    print(sv)
