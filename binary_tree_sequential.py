# CÀI ĐẶT CÂY NHỊ PHÂN BẰNG CẤU TRÚC LUU TRỮ TUẦN TỰ (MẢNG)
# Sử dụng mảng để lưu trữ cây nhị phân
# Nếu nút cha ở vị trí i thì:
# - Con trái ở vị trí 2*i + 1
# - Con phải ở vị trí 2*i + 2
# - Nút cha ở vị trí (i-1)//2

class BinaryTreeSequential:
    def __init__(self, capacity=100):
        """Khởi tạo cây nhị phân với dung lượng mảng"""
        self.capacity = capacity
        self.tree = [None] * capacity
        self.size = 0
    
    def is_empty(self):
        """Kiểm tra cây có rỗng không"""
        return self.size == 0 or self.tree[0] is None
    
    def insert_root(self, data):
        """Thêm nút gốc vào cây"""
        if self.tree[0] is None:
            self.tree[0] = data
            self.size = 1
            return True
        else:
            print("Cây đã có nút gốc!")
            return False
    
    def insert_left(self, parent_index, data):
        """Thêm nút con trái cho nút tại parent_index"""
        if parent_index >= self.capacity:
            print("Chỉ số vượt quá dung lượng mảng!")
            return False
        
        if self.tree[parent_index] is None:
            print(f"Không có nút tại vị trí {parent_index}!")
            return False
        
        left_index = 2 * parent_index + 1
        
        if left_index >= self.capacity:
            print("Chỉ số con trái vượt quá dung lượng mảng!")
            return False
        
        if self.tree[left_index] is not None:
            print(f"Nút con trái tại vị trí {left_index} đã tồn tại!")
            return False
        
        self.tree[left_index] = data
        self.size += 1
        return True
    
    def insert_right(self, parent_index, data):
        """Thêm nút con phải cho nút tại parent_index"""
        if parent_index >= self.capacity:
            print("Chỉ số vượt quá dung lượng mảng!")
            return False
        
        if self.tree[parent_index] is None:
            print(f"Không có nút tại vị trí {parent_index}!")
            return False
        
        right_index = 2 * parent_index + 2
        
        if right_index >= self.capacity:
            print("Chỉ số con phải vượt quá dung lượng mảng!")
            return False
        
        if self.tree[right_index] is not None:
            print(f"Nút con phải tại vị trí {right_index} đã tồn tại!")
            return False
        
        self.tree[right_index] = data
        self.size += 1
        return True
    
    def preorder_traversal(self, index=0, result=None):
        """Duyệt cây theo thứ tự trước (Pre-order): Root -> Left -> Right"""
        if result is None:
            result = []
        
        if index >= self.capacity or self.tree[index] is None:
            return result
        
        # Thăm nút hiện tại
        result.append(self.tree[index])
        
        # Duyệt cây con trái
        self.preorder_traversal(2 * index + 1, result)
        
        # Duyệt cây con phải
        self.preorder_traversal(2 * index + 2, result)
        
        return result
    
    def inorder_traversal(self, index=0, result=None):
        """Duyệt cây theo thứ tự giữa (In-order): Left -> Root -> Right"""
        if result is None:
            result = []
        
        if index >= self.capacity or self.tree[index] is None:
            return result
        
        # Duyệt cây con trái
        self.inorder_traversal(2 * index + 1, result)
        
        # Thăm nút hiện tại
        result.append(self.tree[index])
        
        # Duyệt cây con phải
        self.inorder_traversal(2 * index + 2, result)
        
        return result
    
    def postorder_traversal(self, index=0, result=None):
        """Duyệt cây theo thứ tự sau (Post-order): Left -> Right -> Root"""
        if result is None:
            result = []
        
        if index >= self.capacity or self.tree[index] is None:
            return result
        
        # Duyệt cây con trái
        self.postorder_traversal(2 * index + 1, result)
        
        # Duyệt cây con phải
        self.postorder_traversal(2 * index + 2, result)
        
        # Thăm nút hiện tại
        result.append(self.tree[index])
        
        return result
    
    def display(self):
        """Hiển thị cấu trúc cây"""
        print("\n=== CẤU TRÚC CÂY (Lưu trữ tuần tự) ===")
        print("Mảng:", [self.tree[i] if i < self.capacity else None for i in range(min(20, self.capacity))])
        print(f"Số lượng nút: {self.size}")


# CHƯƠNG TRÌNH DEMO
if __name__ == "__main__":
    print("=" * 60)
    print("DEMO CÂY NHỊ PHÂN - CẤU TRÚC LƯU TRỮ TUẦN TỰ (MẢNG)")
    print("=" * 60)
    
    # Khởi tạo cây
    tree = BinaryTreeSequential(capacity=50)
    
    # Kiểm tra cây rỗng
    print("\n1. Kiểm tra cây rỗng:")
    print(f"   Cây có rỗng không? {tree.is_empty()}")
    
    # Thêm nút gốc
    print("\n2. Thêm nút gốc:")
    tree.insert_root(1)
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
    
    tree.insert_left(0, 2)   # Con trái của nút gốc (index 0)
    tree.insert_right(0, 3)  # Con phải của nút gốc (index 0)
    tree.insert_left(1, 4)   # Con trái của nút 2 (index 1)
    tree.insert_right(1, 5)  # Con phải của nút 2 (index 1)
    tree.insert_left(2, 6)   # Con trái của nút 3 (index 2)
    tree.insert_right(2, 7)  # Con phải của nút 3 (index 2)
    
    # Hiển thị cây
    tree.display()
    
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
    
    # Thử nghiệm thêm với cây phức tạp hơn
    print("\n" + "=" * 60)
    print("DEMO VỚI CÂY CHỨA CHUỖI")
    print("=" * 60)
    
    tree2 = BinaryTreeSequential(capacity=30)
    tree2.insert_root('A')
    tree2.insert_left(0, 'B')
    tree2.insert_right(0, 'C')
    tree2.insert_left(1, 'D')
    tree2.insert_right(1, 'E')
    tree2.insert_left(2, 'F')
    tree2.insert_right(2, 'G')
    tree2.insert_left(3, 'H')
    tree2.insert_right(3, 'I')
    
    print("\n   Cấu trúc cây:")
    print("          A")
    print("        /   \\")
    print("       B     C")
    print("      / \\   / \\")
    print("     D   E F   G")
    print("    / \\")
    print("   H   I")
    
    tree2.display()
    
    print("\n   Các phương thức duyệt:")
    print(f"   Pre-order:  {tree2.preorder_traversal()}")
    print(f"   In-order:   {tree2.inorder_traversal()}")
    print(f"   Post-order: {tree2.postorder_traversal()}")
    
    print("\n" + "=" * 60)
    print("HOÀN THÀNH DEMO!")
    print("=" * 60)
