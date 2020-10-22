"""
$10 // VÒNG LẶP (2)

3. Vòng lặp For
- Sử dụng vòng lặp for để lặp qua các phần tử trong 1 list,
dict, string, tuple, set, range
-> Điều này rất khác so với các ngôn ngữ thông thường
(VD1):
  Str = "ABCDEFGHI"
  for x in Str:
    print(x)
    
a) Cú pháp:
  for biến_ảo in Tập_hợp:
    #Câu lệnh
    
    + biến_ảo: biến tự tạo khi dùng for, chỉ dùng trong phạm vi
    của vòng lặp
    + Tập_hợp: 1 list, string, dictionary,... hoặc range()
  (?): Hãy tạo 1 vòng lặp for in ra các phần tử trong dict
  
b) Từ khoá break, continue và else
  - Có nhiệm vụ và cách dùng tương tự như while
  
c) Từ khoá pass
  - Khi bạn không muốn viết gì trong vòng lặp thì hãy đặt nó vào
  (VD2):
    for z in "HoangTung":
      pass
      
4. Giới thiệu về range()
- Trước đây ta đã biết đến range() trong bài 1
- Đúng với tên gọi của nó, range() là phạm vi
- Cú pháp: range(start, end, step)
    + start: điểm bắt đầu, mặc định là 0
    + end: điểm kết thúc
    + step: bước nhảy giữa các phần tử, ko bắt buộc
- Kết quả sẽ trả 1 phạm vi [start, end)]
- Nếu truyền range(10) thì đc hiểu là range(0, 10, 1)
- start phải nhỏ hơn end, nếu bạn không muốn điều đó thì hãy truyền cho step 1 số âm
- Hãy xem các ví dụ để hiểu rõ hơn
(VD3):
  for j in range(1, 15, 2):
    print(j)
  print("_____________________\n")  
  for i in range(10, 1, -1):
    print(i)
(?): Hãy thử dùng range trong vòng lặp while
"""
print("VD1:")
Str = "ABCDEFGHI"
for x in Str:
  print(x)

List = [{"name":"Tùng", "age":21}, {"name":"Hương", "age":20}, {"name":"Thu", "age":20}]
for y in List:
  print(y)
  
print("VD2: ") 
for z in "Abcdefghi":
  pass
  
print("VD3: ")
for j in range(1, 15, 2):
  print(j)
print("_____________________\n")  
for i in range(10, 1, -1):
  print(i)
  
