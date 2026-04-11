class SinhVien:
    def __init__(self, ten, mssv):
        self.ten = ten
        self.mssv = mssv

    def thong_tin(self):
        return f"Sinh viên: {self.ten} - MSSV: {self.mssv}"

sv1 = SinhVien("Nguyen Van A", "123456")
print(sv1.thong_tin())