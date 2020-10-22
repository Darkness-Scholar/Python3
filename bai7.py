'''$7 // DICTIONARY VÀ CÁC PHƯƠNG THỨC 

Thao tác với Dict 

Tạo 1 dict:  

Thông thường:  

DictA = {...} 

VD: Student = {“Tung” :  [1999, 18, 2], “Huong”: [1999, 12, 10]} 

Sử sụng constructor: 

DictA = dict(key1 = value1, key2 = value2, keyN = valueN) 

VD: Student = dict(Tung = [1999, 18, 2], Huong = [1999, 12, 10])

Thêm hoặc sửa phần tử:
  Cú pháp: dict[key] = value
    Nếu phần tử này ko tồn tại, nó sẽ được thêm vào
    Nếu phần tử đã tồn tại, nó sẽ bị thay đổi
    
2. Các phương thức(method)
2.1) get()
- Cú pháp: Dict.get(key)
- Method get() sử dụng để lấy 1 phần tử trong dict theo key
- Ví dụ:
  D = {1: "Kẹo", 2: "Bánh", 3: "Đồ chơi"}
  Item = D.get(1)
  print(Item)
  
2.2) copy()
- Sử dụng copy để sao chép 1 dict

2.3) pop()
- Xoá phần tử có key được truyền vào
- Cú pháp: Dict.pop(key)


Xem thêm ...
'''
Student = dict(Tùng = [1999, 18, 2], Hương = [1999, 12, 10])
print(Student)
Student["Tùng"] = 1999
var = Student.get("Tùng")
print(var)
print(Student)
