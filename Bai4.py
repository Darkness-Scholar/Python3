'''
$4 / HÀM (FUNCTION)
1. Định nghĩa và cách dùng
- Hàm là tập hợp các câu lệnh,mà chỉ khi gọi đến
tên hàm thì các câu lệnh này mới được thực thi
- Cú pháp: 
  def tên_hàm(x1, x2, x3, ..., xN):
    #Các câu lệnh
  + Trong đó tên hàm được đặt theo quy tắc đặt tên
  cho biến
  + x1, x2, x3, ..., xN là những tham số và nó không
  bắt buộc
- Cách gọi hàm: tên_hàm(các tham số truyền vào nếu có)
- Ví dụ 1: Hàm có tham số

def human(name, age):
  print(name)
  print(age)
#Ta có thể gọi hàm ở bất kì đâu
human("Tùng", 21)

- Ví dụ 2: Hàm không có tham số

def hello():
  print("Xin chào")
#Ta có thể gọi hàm ở bất kì đâu
hello()

- Lưu ý: các câu lệnh trong một hàm phải luôn được
thụt lề so với lệnh khai báo hàm và giới hạn của
hàm sẽ kết thúc trước 1 câu lệnh ko đc thụt lề
- Ví dụ:
  
def something():
  print("Something")
  print("Something")
a = 7

2. Tham số là gì?
- Tham số là 1 chuỗi, 1 số, 1 list, ... hoặc thậm
chí là 1 hàm khác
- Tên của tham số không bị giới hạn nhưng ko đc 
đặt trùng tên
3. Hàm return
- Hàm này có chức năng trả về cho bạn 1 thứ gì đó
- Chạy thử ví dụ sau:
  def function(something):
    return something
  print(function("Hello!!!"))

4. Hàm gọi hàm
- 1 Hàm có thể gọi 1 hàm khác, xem ví dụ
  def menu():
    print("1. Say Hello")
    print("2. Say Bye")
  
  def main():
    menu()
    
5. Hàm nhận hàm làm tham số
- Ví dụ:
  def say(x):
    return x
    
  def main(x):
    print(x)
  
  main(say("Sth"))
    
'''
def say():
  return "Hello"
    
def main(x):
  print(x)
  
main(say())
    






