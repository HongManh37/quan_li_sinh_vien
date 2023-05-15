import os
import math
from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    # hàm update list từ file sinhvien
    def update_list_from_file(self):
        manh = "D:\Quan_li_sinh_vien\sinhvien.txt"
        with open(manh, "r") as file:
            file.readline()
            for line in file:
                manh = line.strip().split()
                svid = int(manh[0])
                name = str(manh[1])
                sex = str(manh[2])
                age = int(manh[3])
                diemToan = float(manh[4])
                diemLy = float(manh[5])
                diemHoa = float(manh[6])
                sv = SinhVien(svid, name, sex, age, diemToan, diemLy, diemHoa)
                self.tinhDTB(sv)
                self.xepLoaiHocLuc(sv)
                self.listSinhVien.append(sv)

    #hàm trả về id của sinh viên cuối cùng trong danh sách
    def maxId(self):
        manh = "D:\Quan_li_sinh_vien\sinhvien.txt"
        maxId = 1
        with open(manh, "r") as file:
            file.readline()
            for line in file:
                manh = line.strip().split()
                if int(maxId) < int(manh[0]):
                    maxId = int(manh[0])
            maxId += 1
            return maxId
        
    # Hàm tạo ID tăng dần cho nhân viên
    def generateID(self):
        maxId = self.maxId()
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
 
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
        
 
    def nhapSinhVien(self):
        # Khởi tạo một sinh viên mới
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        age = int(input("Nhap tuoi sinh vien: "))
        diemToan = float(input("Nhap diem toan: "))
        diemLy = float(input("Nhap diem Ly: "))
        diemHoa = float(input("Nhap diem Hoa: "))
        sv = SinhVien(svId, name, sex, age, diemToan, diemLy, diemHoa)
        self.tinhDTB(sv)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
 
    def updateSinhVien(self, ID):
        # Tìm kiếm sinh viên trong danh sách listSinhVien
        sv:SinhVien = self.findByID(ID)
        # Nếu sinh viên tồn tại thì cập nhập thông tin sinh viên
        if (sv != None):
            # nhập thông tin sinh viên
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            age = int(input("Nhap tuoi sinh vien: "))
            diemToan = float(input("Nhap diem toan: "))
            diemLy = float(input("Nhap diem Ly: "))
            diemHoa = float(input("Nhap diem Hoa: "))
            # cập nhật thông tin sinh viên
            sv._name = name
            sv._sex = sex
            sv._age = age
            sv._diemToan = diemToan
            sv._diemLy = diemLy
            sv._diemHoa = diemHoa
            self.tinhDTB(sv)
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co ID = {} khong ton tai.".format(ID))
 
    # Hàm sắp xếp danh sach sinh vien theo ID tăng dần
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
 
    #Hàm sắp xếp danh sach sinh vien theo tên tăng dần
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
        
 
    # Hàm sắp xếp danh sach sinh vien theo điểm TB tăng dần
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)
 
    # Hàm tìm kiếm sinh viên theo ID
    # Trả về một sinh viên
    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
 
    # Hàm tìm kiếm sinh viên theo tên
    # Trả về một danh sách sinh viên
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
 
    # Hàm xóa sinh viên theo ID
    def deleteById(self, ID):
        isDeleted = False
        # tìm kiếm sinh viên theo ID
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
 
    # Hàm tính điểm TB cho sinh viên
    def tinhDTB(self, sv:SinhVien):
        diemTB = (sv._diemToan + sv._diemLy + sv._diemHoa) / 3
        # làm tròn điểm trung binh với 2 chữ số thập phân
        sv._diemTB = math.ceil(diemTB * 100) / 100
 
    #Hàm xếp loại học lực cho nhân viên
    def xepLoaiHocLuc(self, sv:SinhVien):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung Binh"
        else:
            sv._hocLuc = "Yeu"
 
    # Hàm hiển thị danh sách sinh viên ra màn hình console
    def showSinhVien(self, listSV):
        # hien thi tieu de cot
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Age", "Toan", "Ly", "Hoa", "Diem TB", "Hoc Luc"))
        # hien thi danh sach sinh vien
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                      .format(sv._id, sv._name, sv._sex, sv._age, sv._diemToan, sv._diemLy, 
                              sv._diemHoa,sv._diemTB, sv._hocLuc))
        print("\n")
 
    # Hàm trả về danh sách sinh viên hiện tại
    def getListSinhVien(self):
        return self.listSinhVien
    
    #hàm ghi sinh viên vào danh sách
    def ghifile (self, listSV):
        manh = "D:\Quan_li_sinh_vien\sinhvien.txt"
        with open(manh, "w+") as f:
            contents = f.read()
            testId = self.maxId()
            testId -= 1
            if contents:
                if (self.soLuongSinhVien() > 0):
                    for sv in self.listSinhVien:
                        if testId < sv._id:
                            f.write("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                                    .format(sv._id, sv._name, sv._sex, sv._age, sv._diemToan, sv._diemLy, 
                                            sv._diemHoa,sv._diemTB, sv._hocLuc))
                            f.write("\n")
                            testId = sv._id
                        
            else:
                f.write("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                    .format("ID", "Name", "Sex", "Age", "Toan", "Ly", "Hoa", "Diem TB", "Hoc Luc"))
                f.write("\n")
                if (self.soLuongSinhVien() > 0):
                    for sv in self.listSinhVien:
                        f.write("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                                .format(sv._id, sv._name, sv._sex, sv._age, sv._diemToan, sv._diemLy, 
                                        sv._diemHoa,sv._diemTB, sv._hocLuc))
                        f.write("\n")
        f.close()
    
    #Hàm đọc file
    def read_file (self):
        manh = "D:\Quan_li_sinh_vien\sinhvien.txt"
        with open(manh, "r+") as f:
            print(f.read())
            f.seek(0)
        f.close()

    #hàm tìm kiếm sinh viên trong file bằng id
    def search_student_by_id(self, id):
        manh = "D:\Quan_li_sinh_vien\sinhvien.txt"
        with open(manh, "r") as file:
            file.readline()
            for line in file:
                manh = line.strip().split()
                if int(manh[0]) == id:
                    print(f"ID: {manh[0]}, Name: {manh[1]}, Sex: {manh[2]}, Age: {manh[3]}, Toan: {manh[4]}, Hoa: {manh[5]}, Ly: {manh[6]}, Diem TB: {manh[7]}, Hoc luc: {manh[8]}")
            file.seek(0)
        print(f"Khong tim thay sinh vien mang id: {id}.")



    #node:
    #key=lambda x: x._id
    #tương đương với
    #def ham(self, x:SinhVien):
    #    return x._id