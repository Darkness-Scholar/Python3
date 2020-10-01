'''
$3 / BIẾN VÀ CÁC TỪ KHÓA TRONG PYTHON

I - BIẾN
1. Khái niệm
- Giả sử các con số, các chuỗi, các mảng,... của bạn là các sản phẩm
và giờ bạn muốn in lên nó 1 cái tên, và trong lập trình, cái tên đó
gọi là biến

2. Khai báo và gán giá trị cho biến
- Trong ngôn ngữ khác, khi khai báo biến ta không nhất thiết phải gán
giá trị cho nó nhưng trong Python là bắt buộc
- Cú pháp tên_biến = giá_trị
- Ví dụ:
    a = 3.14
    b = "Tùng"
    c = [1, 2, 3, 4]
    d = {"name": "Tùng", "age": 21}
- Tên biến không bắt đầu bằng số, không bao gồm các kí tự đặc biệt và
không trùng với các từ khóa (key word)
- Giữa các biến không được trùng tên nhau
- Sau khi khai báo, biến và giá trị của nó sẽ được lưu trong bộ nhớ RAM
trong đến khi chương trình tạm dừng

3. Thao tác với biến
- Xét ví dụ sau:
  a = 5
  print(a)
  b = 3
  (?): a += b sẽ có kết quả là bao nhiêu?
  (?): Đoán xem kết quả của print(a == b)
  
II - TỪ KHÓA
- Từ khóa là những thứ được định nghĩa sẵn trong lập trình
- Mỗi từ khóa đều ứng với 1 chức năng riêng

False      await      else       import     pass

None       break      except     in         raise

True       class      finally    is         return

and        continue   for        lambda     try

as         def        from       nonlocal   while

assert     del        global     not        with

async      elif       if         or         yield

- Các từ khóa thường gặp: if, elif, else, def, for, while, return, ...

'''
