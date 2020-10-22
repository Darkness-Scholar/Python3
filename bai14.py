'''
$14 // CÁC TÍNH CHẤT CỦA LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG

1. Tính đóng gói
- Tính đóng gói (Encapsulation): Là quy tắc yêu cầu trạng thái bên trong 
của một đối tượng được bảo vệ và tránh truy cập được từ code bên ngoài
(tức là code bên ngoài không thể trực tiếp đọc và thay đổi thuộc tính 
của đối tượng đó).
-> Tính đóng gói ngăn chặn dữ liệu bị sửa đổi trực tiếp
- Để thể hiện điều này, ta dùng dấu "__" trước thuộc tính đó
- VD: def __init__(self, thisName):
        self.__name = thisName
- Hãy chạy và xem ví dụ 1 bên dưới để hiểu rõ hơn

2. Tính kế thừa
- Tính kế thừa cho phép một lớp (class) có thể kế thừa các thuộc tính và phương 
thức từ các lớp khác đã được định nghĩa. Lớp đã có gọi là lớp cha, lớp mới phát 
sinh gọi là lớp con. Lớp con kế thừa tất cả thành phần của lớp cha, có thể 
mở rộng các thành phần kế thừa và bổ sung thêm các thành phần mới.
- Để tạo 1 class kế thừa, dùng cú pháp sau:
  class tên-class(class-được-kế-thừa):
- Cùng chạy và xem ví dụ 2 nhé
* Lưu ý: Ta hoàn toàn có thêm phương thức mới cho class con
3. Tính đa hình
- Tính đa hình là khái niệm mà hai hoặc nhiều lớp có những phương thức giống nhau 
nhưng có thể thực thi theo những cách thức khác nhau
- Chạy và xem ví dụ 3
'''
print("Ví dụ 1: ")
class Computer:
  def __init__(self, thisName):
    self.__name = thisName
    
  def printName(self):
    print(self.__name)
  
  def changeName(self, newName):
    self.__name = newName

newPC = Computer("Asus")
# Nếu in ra bằng print(newPC.__name) sẽ lỗi vì theo lí thuyết 
# code ngoài ko đc truy cập vào thuộc tính được đóng gói
# Chỉ có thể in ra khi dùng phương thức nội bộ *printName*
newPC.printName()
# Và tất nhiên nó cũng ko thể thay đổi bằng code ngoài, chỉ có
# thể làm việc đó bằng phương thức nội bộ
newPC.changeName("MSI")
# Thử in lại:
newPC.printName()

print("_" * 40)

print("Ví dụ 2: ")
class Father:
  def __init__(this, name, height, weight):
    this.name = name
    this.height = height
    this.weight = weight
  
  def setName(this, newName):
    this.name = newName
    
class Child(Father):
  def __init__(this, name, height, weight, rich):
    #Các thuộc tính của class con
    this.rich = rich #Thuộc tính mới
    super().__init__(name, height, weight)
    #Hàm super() này sẽ đạo nhái các thuộc tính của class cha   
    #Khi kế thừa, các phương thức sẽ tự giác được đạo nhái của class cha

newChild = Child("Tùng", 50, 165, True)
print(newChild.name)
newChild.setName("Hoàng") #Gọi thử phương thức đạo nhái của class cha
print(newChild.name)

print("_" * 40)

print("Ví dụ 3: ")
class One:
  def __init__(this, name):
    this.name = name
  def doSth(this):
    print(this.name, "is Learning Python")
    
class Two:
  def __init__(this, name):
    this.name = name
  def doSth(this):
    print(this.name, "is Playing Video Game")
    
obj1 = One("Tùng")
obj2 = Two("Đức")

def callObj():
  obj1.doSth()
  obj2.doSth()
  
callObj()
#Ta thấy dùng cùng gọi ra 1 phương thức nhưng
#kết quả trả về khác nhau
#Và đó là tính đa hình
