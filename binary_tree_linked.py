# CÀI ĐẶT CÂY NHỊ PHÂN BẰNG CẤU TRÚC LƯU TRỮ MÓC NỐI (NODE)
# Sử dụng Node và con trỏ để lưu trữ cây nhị phân

class Node:
    """Lớp Node đại diện cho một nút trong cây nhị phân"""
    def __init__(self, data):
        self.data = data
        self.left = None   # Con trỏ trái
        self.right = None  # Con trỏ phải


class BinaryTreeLinked:
    """Lớp cây nhị phân sử dụng cấu trúc móc nối"""
    
    def __init__(self):
        """Khởi tạo cây nhị phân rỗng"""
        self.root = None
        self.size = 0
    
    def is_empty(self):
        """Kiểm tra cây có rỗng không"""
        return self.root is None
    
    def insert_root(self, data):
        """Thêm nút gốc vào cây"""
        if self.root is None:
            self.root = Node(data)
            self.size = 1
            return self.root
        else:
            print("Cây đã có nút gốc!")
            return None
    
    def insert_left(self, parent_node, data):
        """Thêm nút con trái cho parent_node"""
        if parent_node is None:
            print("Nút cha không tồn tại!")
            return None
        
        if parent_node.left is not None:
            print("Nút con trái đã tồn tại!")
            return None
        
        new_node = Node(data)
        parent_node.left = new_node
        self.size += 1
        return new_node
    
    def insert_right(self, parent_node, data):
        """Thêm nút con phải cho parent_node"""
        if parent_node is None:
            print("Nút cha không tồn tại!")
            return None
        
        if parent_node.right is not None:
            print("Nút con phải đã tồn tại!")
            return None
        
        new_node = Node(data)
        parent_node.right = new_node
        self.size += 1
        return new_node
    
    def preorder_traversal(self, node=None, result=None, first_call=True):
        """Duyệt cây theo thứ tự trước (Pre-order): Root -> Left -> Right"""
        if first_call:
            node = self.root
            result = []
        
        if node is None:
            return result
        
        # Thăm nút hiện tại
        result.append(node.data)
        
        # Duyệt cây con trái
        self.preorder_traversal(node.left, result, False)
        
        # Duyệt cây con phải
        self.preorder_traversal(node.right, result, False)
        
        return result
    
    def inorder_traversal(self, node=None, result=None, first_call=True):
        """Duyệt cây theo thứ tự giữa (In-order): Left -> Root -> Right"""
        if first_call:
            node = self.root
            result = []
        
        if node is None:
            return result
        
        # Duyệt cây con trái
        self.inorder_traversal(node.left, result, False)
        
        # Thăm nút hiện tại
        result.append(node.data)
        
        # Duyệt cây con phải
        self.inorder_traversal(node.right, result, False)
        
        return result
    
    def postorder_traversal(self, node=None, result=None, first_call=True):
        """Duyệt cây theo thứ tự sau (Post-order): Left -> Right -> Root"""
        if first_call:
            node = self.root
            result = []
        
        if node is None:
            return result
        
        # Duyệt cây con trái
        self.postorder_traversal(node.left, result, False)
        
        # Duyệt cây con phải
        self.postorder_traversal(node.right, result, False)
        
        # Thăm nút hiện tại
        result.append(node.data)
        
        return result
    
    def display(self, node=None, level=0, prefix="Root: "):
        """Hiển thị cấu trúc cây theo dạng đệ quy"""
        if node is None:
            if level == 0:
                node = self.root
                print("\n=== CẤU TRÚC CÂY (Lưu trữ móc nối) ===")
                print(f"Số lượng nút: {self.size}")
                if self.root is None:
                    print("Cây rỗng!")
                    return
            else:
                return
        
        print(" " * (level * 4) + prefix + str(node.data))
        
        if node.left is not None or node.right is not None:
            if node.left:
                self.display(node.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            
            if node.right:
                self.display(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")
    
    def get_height(self, node=None):
        """Tính chiều cao của cây"""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        
        return max(left_height, right_height) + 1
    
    def count_leaves(self, node=None):
        """Đếm số lá trong cây"""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            return 1
        
        return self.count_leaves(node.left) + self.count_leaves(node.right)


# CHƯƠNG TRÌNH DEMO
if __name__ == "__main__":
    print("=" * 60)
    print("DEMO CÂY NHỊ PHÂN - CẤU TRÚC LƯU TRỮ MÓC NỐI (NODE)")
    print("=" * 60)
    
    # Khởi tạo cây
    tree = BinaryTreeLinked()
    
    # Kiểm tra cây rỗng
    print("\n1. Kiểm tra cây rỗng:")
    print(f"   Cây có rỗng không? {tree.is_empty()}")
    
    # Thêm nút gốc
    print("\n2. Thêm nút gốc:")
    root = tree.insert_root(1)
    print(f"   Đã thêm nút gốc: 1")
    print(f"   Cây có rỗng không? {tree.is_empty()}")
    
    # Thêm các nút con
    print("\n3. Xây dựng cây:")
    print("   Cấu trúc cây:")
    print("          1")
    print("        /   \\")
    print("       2     3")
    print("      / \\   / \\")
    print("     4   5 6   7")
    
    # Thêm con cho nút gốc
    node2 = tree.insert_left(root, 2)
    node3 = tree.insert_right(root, 3)
    
    # Thêm con cho nút 2
    node4 = tree.insert_left(node2, 4)
    node5 = tree.insert_right(node2, 5)
    
    # Thêm con cho nút 3
    node6 = tree.insert_left(node3, 6)
    node7 = tree.insert_right(node3, 7)
    
    # Hiển thị cây
    tree.display()
    
    # Thông tin về cây
    print(f"\n   Chiều cao cây: {tree.get_height()}")
    print(f"   Số nút lá: {tree.count_leaves()}")
    
    # Duyệt cây theo các phương thức
    print("\n4. DUYỆT CÂY:")
    print("\n   a) Duyệt tiền tự (Pre-order - NLR):")
    print("      Root -> Left -> Right")
    print(f"      Kết quả: {tree.preorder_traversal()}")
    
    print("\n   b) Duyệt trung tự (In-order - LNR):")
    print("      Left -> Root -> Right")
    print(f"      Kết quả: {tree.inorder_traversal()}")
    
    print("\n   c) Duyệt hậu tự (Post-order - LRN):")
    print("      Left -> Right -> Root")
    print(f"      Kết quả: {tree.postorder_traversal()}")
    
    # Thử nghiệm với cây chứa chuỗi
    print("\n" + "=" * 60)
    print("DEMO VỚI CÂY CHỨA CHUỖI")
    print("=" * 60)
    
    tree2 = BinaryTreeLinked()
    root2 = tree2.insert_root('A')
    
    # Mức 1
    nodeB = tree2.insert_left(root2, 'B')
    nodeC = tree2.insert_right(root2, 'C')
    
    # Mức 2
    nodeD = tree2.insert_left(nodeB, 'D')
    nodeE = tree2.insert_right(nodeB, 'E')
    nodeF = tree2.insert_left(nodeC, 'F')
    nodeG = tree2.insert_right(nodeC, 'G')
    
    # Mức 3
    nodeH = tree2.insert_left(nodeD, 'H')
    nodeI = tree2.insert_right(nodeD, 'I')
    
    print("\n   Cấu trúc cây:")
    print("          A")
    print("        /   \\")
    print("       B     C")
    print("      / \\   / \\")
    print("     D   E F   G")
    print("    / \\")
    print("   H   I")
    
    tree2.display()
    
    print(f"\n   Chiều cao cây: {tree2.get_height()}")
    print(f"   Số nút lá: {tree2.count_leaves()}")
    
    print("\n   Các phương thức duyệt:")
    print(f"   Pre-order:  {tree2.preorder_traversal()}")
    print(f"   In-order:   {tree2.inorder_traversal()}")
    print(f"   Post-order: {tree2.postorder_traversal()}")
    
    # Demo với cây biểu thức toán học
    print("\n" + "=" * 60)
    print("DEMO VỚI CÂY BIỂU THỨC TOÁN HỌC: (3 + 5) * (2 - 1)")
    print("=" * 60)
    
    expr_tree = BinaryTreeLinked()
    root_expr = expr_tree.insert_root('*')
    
    # Nhánh trái: 3 + 5
    plus_node = expr_tree.insert_left(root_expr, '+')
    expr_tree.insert_left(plus_node, 3)
    expr_tree.insert_right(plus_node, 5)
    
    # Nhánh phải: 2 - 1
    minus_node = expr_tree.insert_right(root_expr, '-')
    expr_tree.insert_left(minus_node, 2)
    expr_tree.insert_right(minus_node, 1)
    
    print("\n   Cấu trúc cây:")
    print("        *")
    print("       / \\")
    print("      +   -")
    print("     / \\ / \\")
    print("    3  5 2  1")
    
    expr_tree.display()
    
    print("\n   Các phương thức duyệt:")
    print(f"   Pre-order (tiền tố):  {expr_tree.preorder_traversal()}")
    print(f"   In-order (trung tố):  {expr_tree.inorder_traversal()}")
    print(f"   Post-order (hậu tố): {expr_tree.postorder_traversal()}")
    
    print("\n" + "=" * 60)
    print("HOÀN THÀNH DEMO!")
    print("=" * 60)
