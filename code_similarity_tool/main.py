# ======================================
# FILE: main.py
# CHỨC NĂNG: GIAO DIỆN CHÍNH (MENU)
# ======================================

import os
import sys

# Thêm thư mục hiện tại vào sys.path để đảm bảo import được các module trong utils
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

try:
    from utils.project_compare import compare_projects
    from utils.document_compare import compare_documents
except ImportError as e:
    print(f"❌ Lỗi: Không tìm thấy các file trong thư mục 'utils'.")
    print(f"Chi tiết: {e}")
    sys.exit(1)

def clear_screen():
    # Xóa màn hình console cho sạch sẽ (Windows là 'cls', Linux/Mac là 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print("="*40)
        print("   TOOL KIỂM TRA ĐẠO CODE & BÁO CÁO   ")
        print("="*40)
        print("1. So sánh 2 Project Code (.py)")
        print("2. So sánh 2 File Báo cáo (.txt)")
        print("3. Thoát chương trình")
        print("-"*40)

        choice = input("Chọn chức năng (1/2/3): ").strip()

        if choice == '1':
            print("\n--- SO SÁNH PROJECT ---")
            p1 = input("Nhập đường dẫn Project 1 (VD: project1): ").strip()
            p2 = input("Nhập đường dẫn Project 2 (VD: project2): ").strip()
            
            if os.path.isdir(p1) and os.path.isdir(p2):
                compare_projects(p1, p2)
            else:
                print("❌ Lỗi: Một trong hai đường dẫn thư mục không tồn tại!")
            
            input("\nNhấn Enter để tiếp tục...")

        elif choice == '2':
            print("\n--- SO SÁNH BÁO CÁO ---")
            f1 = input("Nhập file báo cáo 1 (VD: documents/doc1.txt): ").strip()
            f2 = input("Nhập file báo cáo 2 (VD: documents/doc2.txt): ").strip()
            
            if os.path.isfile(f1) and os.path.isfile(f2):
                compare_documents(f1, f2)
            else:
                print("❌ Lỗi: Một trong hai file không tồn tại!")
            
            input("\nNhấn Enter để tiếp tục...")

        elif choice == '3':
            print("👋 Tạm biệt!")
            break
            
        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng thử lại.")
            input("\nNhấn Enter để tiếp tục...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nĐã dừng chương trình.")
        sys.exit(0)