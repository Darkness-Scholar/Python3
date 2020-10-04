'''
$6 // LIST, THAO TÁC VỚI LIST VÀ CÁC PHƯƠNG THỨC

1. Nhắc lại về list
List là 1 tập hợp nhiều phần tử nằm trong cặp ngoặc [...], với các phần tử được 
phân cách bởi dấu phẩy
Các phần tử trong list thuộc mọi kiểu dữ liệu như Boolean, Số, Chuỗi, Tuple, 
Dict, Set hoặc thậm chí là list
VD: 
listA = [10, True, (1, 2, 3), "String", {3, 2, 1}, {"name":"Tùng", "age":21}, [1, 2, 3]]

2. Các thao tác với list
Để tạo ra 1 list, ta có rất nhiều cách, điển hình:
  listA = list([1, 2, 3])
  listB = [1, 2, 3]
(?) Hãy tạo 1 list bên trong không có phần tử nào

Ta có thể thay đổi giá trị trong list bằng cú pháp list[thứ tự] = giá trị
VD:
  listA = ["Tùng", 1999]
  listA[0] = "Đức"
  listA[1] = 2002
  >>> Nếu phần tử cần thay đổi không tồn tại, sẽ gây ra lỗi
Khi gán listA với listB, sau đó chỉ cần thay đổi giá trị của 1 trong 2 list
thì list còn lại cũng sẽ bị thay đổi

3. Các phương thức (method) của list
3.1) len()
Phương thức len() trả về số phần tử có trong list
Cú pháp: len(list)
VD:
  listA = [1, 2, 3, 4, 5]
  sophantu = len(listA)
  print(sophantu)
  
3.2) count()
Phương thức count() trả về số lần xuất hiện của x trong list
Cú pháp: list.count(x)
VD:
  listA = [2, 2, 4, 5, 6]
  print(listA.count(2))
  
3.3) index()
Trả về số thứ tự của x trong list
Cú pháp: list.index(x)

3.4) copy()
Copy một list
Cú pháp: list.copy()

3.5) append(x)
Thêm 1 phần tử vào cuối list
Cú pháp: list.append(x)
VD:
  listA = [1, 2, 3]
  listA.append(4)
  print(listA)
  
3.6) extend()
Thêm tập hợp các phần tử vào cuối list
Cú pháp: list.extend([các phần tử])
VD:
  listA = [1, 2, 3]
  listA.extend([4, 5, 6])
  print(listA)
  
3.7) insert()
Thêm phần tử x vào vị trí thứ y trong list
Cú pháp: list.insert(x, y)
VD:
  listA = [1, 3, 4, 5]
  listA.insert(2, 1)
  print(listA)

3.8) pop()
Xoá phần tử thứ x trong list, nếu ko truyền x sẽ xoá p tử cuối
pop() trả về giá trị bị xoá
VD:
  listA = [1, 2, 3, 4, 5]
  X = listA.pop(-1)
  print(listA)
  print(X)
  
3.9) remove()
Xoá phần tử x (x xuất hiện đầu tiên) trong list
Cú pháp: list.remove()
VD:
  listA = ["Hoàng", "Tùng"]
  listA.remove("Tùng")
  print(listA)

3.10) reverse()
Đảo ngược các phần tử trong list
Cú pháp: list.reverse()
Ngoài ra ta có thể dùng list[::-1] 

3.11) sort()
Sắp xếp các phần tử theo thứ tự từ bé đến lớn
Nếu reverse = True đc truyền vào thì sẽ xếp từ lớn đến bé
VD:
  listA = [1, 3, 2, 6, 5, 4]
  listA = sort(reverse = True)
'''
listA = [1, 3, 2, 6, 5, 4]
listB = listA.sort(reverse = True)
print(listA)
