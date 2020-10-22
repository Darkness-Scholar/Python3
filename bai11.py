'''
$11 // THAM SỐ (ARGUMENT)

1. Tham số là gì?
- Ở bài Hàm, chúng ta đã tìm hiểu qua cách hoạt động của tham số, vậy nó là gì?
- Có thể hiểu tham số là 1 biến, chỉ có thể hoạt động trong phạm vi 1 hàm
- Mặc định, hàm có bao nhiêu tham số thì phải truyền bấy nhiêu giá trị 
(theo thứ tự), giống như việc khai báo biến mà không truyền giá trị,
nó sẽ gây lỗi
- Xem ví dụ sau:
  
  def function(x):
    print("Hihi")
  
  function()
  
  + Do x không được gán cho giá trị nào khi gọi hàm lên xảy ra lỗi
  + Hãy thử khai báo biến y mà ko gán giá trị, nó cũng có kết quả là lỗi
  
2. Giá trị mặc định của tham số
- Xem ví dụ
  
  def function(x = 5, y = 3):
    print(x + y)
  function()

- Ta có thể gán giá trị mặc định cho tham số, trong trường hợp này, nếu
tham số ko được truyền vào giá trị khi gọi hàm, nó sẽ lấy giá trị mặc định

(?): Nếu gọi function(7, 3) thì kết quả của ví dụ trên là gì?

3. Cú pháp *Tên_tham_số
- Khi ta không xác định được cần truyền bao tham số, hãy sử dụng cú pháp này
- Chạy thử ví dụ: 
 
 def function(*thamso):
   print(thamso)
 function("Hello", True, 0.9)
 
- Các tham số được truyền vào sẽ được đưa vào 1 tuple, nghĩa là lúc này thamso
sẽ là 1 tuple chứa các phần tử được truyền vào

4. Truyền tham số bất quy tắc
- Xem ví dụ sau:
  def function(thamso1, thamso2, thamso3):
    print(thamso1, thamso2, thamso3)
  
  function(thamso3 = "Hello", thamso1 = "ABC", thamso2 = 123)

- Ta hoàn toàn có thể truyền tham số không theo thứ tự bằng cú pháp trên

5. Cú pháp **Tên_tham_số
- Nếu ta không thể xác định được cần truyền bao nhiêu tham số như ở phần 4
ta dùng cú pháp **Tên_tham_số
- Ví dụ:
def function5(**thamso):
  print(thamso)

function5(name = "Tùng", age = 21, birth = "18/02")

- Lúc này **thamso sẽ là 1 dict 
'''

print("Ví dụ phần 1: Lỗi")
#def function1(x):
#  print("Hihi")
  
#function1()
print("___________________________ \n")

print("Ví dụ phần 2:")
def function2(x = 5, y = 3):
  print(x + y)
  
function2()
print("___________________________ \n")

print("Ví dụ phần 3:")
def function3(*thamso):
  print(thamso)
  
function3("Hello", True, 0.9)
print("___________________________ \n")

print("Ví dụ phần 4:")
def function4(thamso1, thamso2, thamso3):
  print(thamso1, thamso2, thamso3)
  
function4(thamso3 = "Hello", thamso1 = "ABC", thamso2 = 123)
print("___________________________ \n")

print("Ví dụ phần 5:")
def function5(**thamso):
  print(thamso)

function5(name = "Tùng", age = 21, birth = "18/02")

print("\n Tác giả: Tùng Hoàng \n Biên soạn và dịch thuật")
