'''
$13 // LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG, CLASS TRONG PYTHON

1. Lập trình hướng đối tượng là gì?

Lập trình hướng đối tượng (OOP) là một kỹ thuật lập trình cho phép lập trình viên 
tạo ra các đối tượng trong code trừu tượng hóa các đối tượng
Để hiểu rõ hơn ta hãy đi tìm hiểu các phần sau đây

2. Đối tượng (object)

Đối tượng bao gồm thuộc tính và phương thức:
  - Thuộc tính: thông tin và đặc tính của đối tượng
                VD: chó có 4 chân, có đuôi,...
  - Phương thức: là thao tác và hành động mà đối tượng
  đó có thể thực hiện
                VD: chó có hành động sủa "gâu gâu"
                
2. Lớp (class)

- Lớp là 1 kiểu dữ liệu bao gồm các thuộc tính và phương thức được định nghĩa sẵn
- Ta có thể coi class như là 1 cái nguyên mẫu để tạo lên các đối tượng
- Để tạo ra 1 class, ta dùng cú pháp: class tên_class:
VD: 
  class Human:
    
- Để khai báo các thuộc tính cho class trong python, ta sử dụng: 
  cú pháp: def __init__(self, các_tham_số_thuộc_tính)
  + class luôn phải có 1 tham số là self (có thể đặt tên khác), self đc hiểu là chính class đó
VD: class Human:
      def __init__(self, name, gender):
        self.isName = name
        self.isGender = gender
        
- Để tạo ra 1 đối tượng, ta chỉ việc gọi ra tên class và truyền tham số thuộc tính:
VD: newHuman = Human("Tùng", "male")
    + Ta có: newHuman là 1 đối tượng được tạo ra bởi class Human
             newHuman có thuộc tính isName là "Tùng", isGender là "male", thử print nó ra nhé
               print(newHuman.isName)
               print(newHuman.isGender)
               
- Để khai báo phương thức trong class, ta viết nó như 1 hàm thông thường
VD: def speak(self, sth):
      print(self.name + "nói rằng: " + sth)
    
____________________ ĐỌC HIỂU:CLASS VÀ OBJECT ____________________

Class nghĩa là lớp, lớp trong tự nhiên gồm lớp bò sát, lớp chim, lớp
động vật có vú. Lớp chim đã sinh ra loài đại bàng, ta gọi loài đại
bàng là 1 đối tượng được tạo ra bởi lớp chim, lớp chim có thuộc tính
chung là 2 cánh, 2 chân, có mỏ,... và lớp chim có phương thức là bay
lượn, từ đây ta có ví dụ sau:
class Chim:
  def __init__(self, name, mo, chan, canh):
    self.name = name
    self.mo = mo
    self.chan = chan
    self.canh = canh
  def bay(self):
    print(self.name, "Đang bay")
 
newChim = Chim("Đại bàng", "nhọn", "10cm", "200cm")

Thêm 1 ví dụ nữa về điện thoại:
class Iphone:
  def __init__(self, name, inch, cpu, ram):
    self.name = name
    self.inch = inch
    self.cpu = cpu
    self.ram = ram
  
  def chup_anh():
    print("Chụp ảnh")
  def nghe_goi():
    print("Nghe gọi")

myPhone = Iphone("Iphone 9", 7.0, "Intel Core I8", "7GB")
'''

class Human: #Khởi tạo class Human
  def __init__(self, name, gender): #Khai báo thuộc tính
    self.isName = name
    self.isGender = gender
  def speak(self, sth): #Khai báo phương thức
    print(self.isName, "nói rằng:", sth)
    
newHuman = Human("Tùng", "male") #Tạo đối tượng bằng class
print(newHuman.isName) #Xuất ra thuộc tính isName củ đối tượng newHuman
print(newHuman.isGender) #Xuất ra thuộc tính isGender của đối tượng newHuman
newHuman.speak("Hello") #Gọi ra phương thức speak

print("\n   Tác giả: Tùng Hoàng >>>")
