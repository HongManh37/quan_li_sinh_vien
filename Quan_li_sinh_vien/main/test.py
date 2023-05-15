import math

class SinhVien:
    ListSinhVien = []
    def __init__(self, id, name, sex, age, diemToan, diemLy, diemHoa):
        self._id = id
        self._name = name
        self._sex = sex
        self._age = age
        self._diemToan = diemToan
        self._diemLy = diemLy
        self._diemHoa = diemHoa
        self._diemTB = 0
        self._hocLuc = ""
    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.ListSinhVien[0]._id
            for sv in self.ListSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    
    def soLuongSinhVien(self):
        return self.ListSinhVien.__len__()
    
    def findByID(self, id):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.ListSinhVien:
                if (sv._id == id):
                    searchResult = sv
        return searchResult
    
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
                self.ListSinhVien.append(sv)
    
    def updateSinhVien(self, id):
        # Tìm kiếm sinh viên trong danh sách listSinhVien
        sv:SinhVien = self.findByID(id)
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
            print("Sinh vien co id = {} khong ton tai.".format(id))

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
        self.ListSinhVien.append(sv)

    # Hàm tính điểm TB cho sinh viên
    def tinhDTB(self, sv):
        diemTB = (sv._diemToan + sv._diemLy + sv._diemHoa)/3
        # làm tròn điểm trung binh với 2 chữ số thập phân
        sv._diemTB = math.ceil(diemTB * 100) / 100
 
    #Hàm xếp loại học lực cho sinh vien
    def xepLoaiHocLuc(self, sv):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung Binh"
        else:
            sv._hocLuc = "Yeu"

    def getListSinhVien(self):
        return self.ListSinhVien
    
    #hàm ghi sinh viên vào file
    def ghifile (self, listSV):
        manh = "D:\Quan_li_sinh_vien\sinhvien.txt"
        with open(manh, "w+") as f:
            contents = f.read()
            if contents:
                if (self.soLuongSinhVien() > 0):
                    for sv in listSV:
                        f.write("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                                    .format(sv._id, sv._name, sv._sex, sv._age, sv._diemToan, sv._diemLy, 
                                            sv._diemHoa,sv._diemTB, sv._hocLuc))
                        f.write("\n")
            else:
                f.write("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                    .format("ID", "Name", "Sex", "Age", "Toan", "Ly", "Hoa", "Diem TB", "Hoc Luc"))
                f.write("\n")
                if (self.soLuongSinhVien() > 0):
                    for sv in listSV:
                        f.write("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                                    .format(sv._id, sv._name, sv._sex, sv._age, sv._diemToan, sv._diemLy, 
                                            sv._diemHoa,sv._diemTB, sv._hocLuc))
                        f.write("\n")
        #đóng file
        f.close()

    #hàm đọc sinh viên trong file
    def read_file (self):
        manh = "D:\Quan_li_sinh_vien\sinhvien.txt"
        with open(manh, "r+") as f:
            print(f.read())
            f.seek(0)
        f.close()

    #hàm tìm kiếm sinh viên trong file bằng id
    def show_search_student_by_id(self, id):
        manh = "D:\Quan_li_sinh_vien\sinhvien.txt"
        with open(manh, "r") as file:
            file.readline()
            for line in file:
                manh = line.strip().split()
                if int(manh[0]) == id:
                    print(f"ID: {manh[0]}, Name: {manh[1]}, Sex: {manh[2]}, Age: {manh[3]}, Toan: {manh[4]}, Hoa: {manh[5]}, Ly: {manh[6]}, Diem TB: {manh[7]}, Hoc luc: {manh[8]}")
                    return
            file.seek(0)
        print(f"No student with ID {id} found.")
        file.close()
                
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

    #hàm trả về id của sinh viên cuối cùng trong danh sách
    def maxId(self):
        manh = "D:\Quan_li_sinh_vien\sinhvien.txt"
        maxId = 1
        with open(manh, "r") as file:
            file.readline()
            for line in file:
                manh = line.strip().split()
                if int(maxId) < int(manh[0]):
                    maxId = manh[0]
            return maxId
        
    
sv = SinhVien(0, 0, 0, 0, 0, 0, 0)
sv.update_list_from_file()
# print(sv.soLuongSinhVien())
#sv.nhapSinhVien()
id = int(input("Nhap id cua sinh vien: "))
sv.updateSinhVien(id)
sv.showSinhVien(sv.getListSinhVien())
sv.ghifile(sv.getListSinhVien())
#print(sv.maxId())
#with open(manh, "r+") as f:
    #contents = f.read()
    #if contents:
       # if (sv.soLuongSinhVien() > 0):
            #for sv in sv.ListSinhVien:
                #f.write("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                            #.format(sv._id, sv._name, sv._sex, sv._age, sv._diemToan, sv._diemLy, 
                                    #sv._diemHoa,sv._diemTB, sv._hocLuc))
                #f.write("\n")
    #else:
        #f.write("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
            #.format("ID", "Name", "Sex", "Age", "Toan", "Ly", "Hoa", "Diem TB", "Hoc Luc"))
        #f.write("\n")
        #if (sv.soLuongSinhVien() > 0):
           # for sv in sv.ListSinhVien:
                #f.write("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                            #.format(sv._id, sv._name, sv._sex, sv._age, sv._diemToan, sv._diemLy, 
                                   #sv._diemHoa,sv._diemTB, sv._hocLuc))
                #f.write("\n")
#f.close()
