import os
import time
from QuanLySinhVien import QuanLySinhVien
from SinhVien import SinhVien
# khởi tạo một đối tượng QuanLySinhVien để quản lý sinh viên
qlsv = QuanLySinhVien()
qlsv.update_list_from_file()
while (1==1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN PY")
    print("*************************MENU**************************")
    print("**  1. Them sinh vien.                               **")
    print("**  2. Cap nhat thong tin sinh vien boi ID.          **")
    print("**  3. Xoa sinh vien boi ID.                         **")
    print("**  4. Tim kiem sinh vien theo ten.                  **")
    print("**  5. Sap xep sinh vien theo diem trung binh (GPA). **")
    print("**  6. Sap xep sinh vien theo ten.                   **")
    print("**  7. Sap xep sinh vien theo ID.                    **")
    print("**  8. Hien thi danh sach sinh vien.                 **")
    print("**  9. Ghi danh sach sinh vien vao file              **")
    print("**  10. Đọc file danh sach sinh vien vao             **")
    print("**  0. Thoat                                         **")
    print("*******************************************************")
     
    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        os.system("cls") # Windows
        print("\n1. Them sinh vien.")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
        time.sleep(3)
        os.system("cls")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cap nhat thong tin sinh vien. ")
            print("\nNhap ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)

        else:
            print("\nSanh sach sinh vien trong!")

    elif (key == 3):
        os.system("cls")
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa sinh vien.")
            print("\nNhap ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh vien co id = ", ID, " da bi xoa.")
    
            else:
                print("\nSinh vien co id = ", ID ," khong ton tai.")
    
        else:
            print("\nSanh sach sinh vien trong!")

    elif (key == 4):
        os.system("cls")
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien theo ten.")
            print("\nNhap ten de tim kiem: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)

        else:
            print("\nSanh sach sinh vien trong!")

    elif (key == 5):
        os.system("cls")
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())

        else:
            print("\nSanh sach sinh vien trong!")

    elif (key == 6):
        os.system("cls")
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())

        else:
            print("\nSanh sach sinh vien trong!")

    elif (key == 7):
        os.system("cls")
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ID.")
            qlsv.sortByID()
            qlsv.showSinhVien(qlsv.getListSinhVien())

        else:
            print("\nSanh sach sinh vien trong!")

    elif (key == 8):
        os.system("cls")
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
            time.sleep(3)
        else:
            print("\nSanh sach sinh vien trong!")

    elif (key == 9):
        os.system("cls")
        qlsv.ghifile(qlsv.getListSinhVien())
        print("\nBan da ghi vao file thanh cong!")
    
    elif (key==10):
        os.system('cls')
        qlsv.read_file()
        print("---------------------------Danh sach sinh vien---------------------------\n")

    elif (key == 0):
        os.system("cls")
        print("\nBan da chon thoat chuong trinh!")
        time.sleep(3)
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")
os.system("cls")