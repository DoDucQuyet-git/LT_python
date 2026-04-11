class HocVien:
    # a) Tạo class hoc vien với các thuộc tính tương ứng
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop
    # b) Tạo phương thức show_info trả về đầy đủ thông tin
    def show_info(self):
        print("--- THÔNG TIN HỌC VIÊN ---")
        print(f"Họ tên    : {self.ho_ten}")
        print(f"Ngày sinh : {self.ngay_sinh}")
        print(f"Email     : {self.email}")
        print(f"Điện thoại: {self.dien_thoai}")
        print(f"Địa chỉ   : {self.dia_chi}")
        print(f"Lớp       : {self.lop}")
        print("-" * 26)
    # c) Tạo phương thức change_info với tham số mặc định
    def change_info(self, ho_ten=None, ngay_sinh=None, email=None, dien_thoai=None, dia_chi='Hà Nội', lop='IT12.x'):
        if ho_ten: self.ho_ten = ho_ten
        if ngay_sinh: self.ngay_sinh = ngay_sinh
        if email: self.email = email
        if dien_thoai: self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop
        print("=> Đã cập nhật thông tin thành công!")

# d) Chương trình chính
if __name__ == "__main__":
    hv1 = HocVien("Đỗ Đức Quyêt", "01/01/2005", "DDQ@gmail.com", "0912345678", "Ninh Bình", "IT10.1")
    print("Dữ liệu ban đầu:")
    hv1.show_info()
    hv1.change_info(ho_ten="Nguyen Van B")
    print("\nDữ liệu sau khi thay đổi (sử dụng tham số mặc định):")
    hv1.show_info()