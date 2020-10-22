'''
$12 // HÀM KHUYẾT DANH LAMBDA

1. Khái niệm
- Đôi khi để gán cho biến 1 hàm, ta bắt buộc dùng hàm khuyết danh
- Nói tóm lại, đây có thể coi là 1 giá trị ở dạng hàm
- Hàm này tuy không cần đặt tên nhưng phải sử dụng từ khoá lambda

2. Cú pháp
- Ta dùng: lambda các_tham_số: code
- Có thể gọi hàm này nếu nó đc gán vào biến, cú pháp: tên_biến(tham số nếu có)
- Ví dụ:
  vd1 = lambda: print("Hello")

3. Return về 1 lambda
- Ví dụ:
  def function():
    return lambda: 3 + 2
  
  result = function()
  print(result())
- Lúc này giá trị của result sẽ là hàm lambda
'''
print("Ví dụ phần 2:")
vd1 = lambda: print("Hello")
vd1()

vd2 = lambda a,b: a + b
print(vd2(3,4))
print("\n ---------------------------- \n")
print("Ví dụ phần 3:")
def function():
  return lambda: 3 + 2
  
result = function()
print(result())
print("\n Tác giả: Tùng Hoàng \n Biên soạn và dịch thuật")
