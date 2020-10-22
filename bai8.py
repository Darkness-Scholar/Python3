"""
$8 // CẤU TRÚC RẼ NHÁNH

1.Khái niệm
- Đứng trước moi vấn đề, bạn đều có nhiều cách giải quyết
và trong lập trình cũng vậy
- Giả sử ngày mai trời mưa, bạn ở nhà, nếu ko mưa thì bạn
đi chơi điện tử. Thì đó là sự rẽ nhánh trong real life

- Cấu trúc này được sử dụng rất phổ biến trong lập trình

2. Cú pháp và cách dùng
- Cú pháp cơ bản:
  if điều kiện:
    #Các tập hợp lệnh nếu điều kiện đúng
  
 - Cú pháp có else:
  if điều kiện:
    #Các tập hợp lệnh nếu điều kiện đúng
  else:
    #Các tập hợp lệnh nếu điều kiện sai

- Cú pháp có elif:
    if điều kiện:
      #Các tập hợp lệnh nếu điều kiện đúng
    elif điều kiện:
      #Các tập hợp lệnh nếu điều kiện đúng
      
 - Giải thích thuật ngữ:
   if được hiểu là nếu, nếu đúng thì sẽ chạy tập lệnh dưới nó
   else được hiểu là nếu không đúng thì chạy tập lệnh ở dưới
   elif được hiểu là nếu mà ... thì sẽ chạy tập lệnh dưới nó
   
   ✓ Hãy xem và chạy ví dụ ở dưới cùng của bài để hiểu hơn

(∆): Hãy sử dụng kiến thức bài này để tìm phim có trong 1 tập hợp
      *Gợi ý: Thêm tập hợp các tên phim vào list hoặc dict
              Sử dụng input() để nhập vào tên cần tìm
              Bài sẽ được giải trong bài thực hành sau
"""

#Ví dụ 1:
x = 5
y = 9
if x > 9:
  print("X lớn hơn Y")
else:
  print("Y lớn hơn hoặc bằng X")
  
#Ví dụ 2: Kiểm tra 1 số có chia cho 3 hay không

z = int(input("Nhập vào 1 con số bất kì"))
#Lấy dữ liệu người dùng nhập vào và chuyển về int
if z % 3 == 0:
  #Nếu số dư của z chia 3 = 0:
  print(z, " Chia hết cho 3: ")
  
#Ví dụ 3: Kiểm tra hạng của bạn theo số điểm

point = float(input("Nhập điểm của bạn: "))
if point == 10.0:
  print("Bạn đạt hạng SS")
elif point < 10 and point >= 8:
  #Trong toán học có thể diễn đạt là point € [8;10)
  print("Bạn đạt hạng S")
elif point < 8 and point >= 7.0:
  #Trong toán học có thể diễn đạt là point € [7;8)
  print("Bạn đạt hạng A")
elif point < 7 and point >= 5:
  #Trong toán học có thể diễn đạt là point € [5;7)
  print("Bạn đạt hạng B")
elif point < 5 and point >= 0:
  #Trong toán học có thể diễn đạt là point € [0;5)
  print("Bạn ngu vl và đạt hạng C")
else:
  #Nếu point ko trùng với tất cả điều kiện trên
  print("Điểm không hợp lệ")
