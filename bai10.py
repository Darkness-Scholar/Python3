"""
$10 // VÒNG LẶP (1)

1. Vòng lặp là gì
- Vòng lặp trong trong lập trình là làm đi làm lại 1 lệnh hoặc
tập hợp lệnh với số lần (điểm dừng) quy định
- Có 2 dạng vòng lặp: while và for

2. Vòng lặp While
(?): In ra các số từ 1 đến 10
- Thay vì viết 10 dòng print thì ta sẽ dùng vòng lặp
  i = 1
  while i <= 10:
    print(i)
    i += 1
    
   | Cho i = 1 để vòng lặp biết được nó xuất phát từ 1
   | i <= 10 nghĩa là vòng lặp sẽ kết thúc nếu i ko <= 10
   | hay nói cách khác là phạm vi vòng lặp là i € [0;10]
   | In ra i
   | Bước nhảy của vòng lặp, mỗi lần lặp i sẽ tăng lên 1 giá trị
   
=> Cú pháp:
  biến_khởi_tạo = giá trị khởi tạo
  while biến_khởi_tạo phạm_vi_vòng_lặp:
    câu lệnh
    bước_nhảy_vòng_lặp
    
(VD1): Hãy in ra các số theo quy tắc 20, 18, 16, ... 0
 x = 20
 while x >= 0:
   print(x)
   x -= 2
 
- Từ khoá break: Tạm dừng vòng lặp nếu gặp 1 điều kiện gì đó
                 Nó giống việc bạn đang đá bóng thì gặp mưa lên bạn ko đá nữa
(VD2): 
  x = 20
  while x >= 0:
    print(x)
    x -= 2 
    if x == 8:
      break
      
- Từ khoá continue: Bỏ qua lần lặp này nếu gặp 1 điều kiện nào đó
                    Giống việc bạn đi chợ, bạn gặp đồ ko ngon lên bạn bỏ qua và 
                    tiếp tục đi chợ
(VD3):
  x = 20
  while x >= 0:
    if x == 8:
      x -= 2
      continue
    print(x)
    x -= 2
        
    *Lưu ý: nếu ko viết bước lặp trước continue, vòng lặp có thể tạm dừng vì
    lần lặp này đã bị bỏ qua, đồng nghĩa với việc bước nhảy của lần này cũng 
    bị bỏ qua => ko đc nhảy => Mãi dừng ở vòng lặp trước đó

- Nếu vòng lặp không có bước nhảy, bạn sẽ gặp rắc rối, hãy xem VD
(VD4):
  y = 20
  while y >= 0:
    print(y)
    
    *Lưu ý: khi 1 chương trình có vòng lặp không bước nhảy được chạy lên, thiết bị
    của bạn sẽ bị đơ vì nó cứ chạy, chạy, và chạy cho đến khi ra khỏi phạm vi vòng lặp
    nhưng tất nhiên là sẽ ko vượt qua được vì ko bước nhảy => Sinh ra lag
    (?): Nếu Liên minh huyền thoại bị kẻ xấu đưa vào dữ liệu code một vòng lặp này
    kết quả sẽ là gì ?
    
- Từ khoá else trong vòng lặp:
    Khi kết thúc vòng lặp, các lệnh sau else đc thực hiện
(VD5):
  i = 1
  while i < 10:
    print(i)
    i += 1
  else:
    print("Đã dừng")
    
"""

print("Ví dụ 1:")
x = 20
while x >= 0:
  print(x)
  x -= 2
  
print("Ví dụ 2:")
x = 20
while x >= 0:
  print(x)
  x -= 2 
  if x == 8:
    break
    
print("Ví dụ 3:")
x = 20
while x >= 0:
  if x == 8:
     x -= 2
     continue
  print(x)
  x -= 2
  
print("Ví dụ 4: Không nên xoá dấu thăng để chạy vì sẽ gây đơ máy")
#y = 20
#while y >= 0:
  #print(y)
  
print("Ví dụ 5:")
i = 1
while i < 10:
  print(i)
  i += 1
else:
  print("Đã dừng")
    
