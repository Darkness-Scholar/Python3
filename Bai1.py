# Bài 1: KIỂU DỮ LIÊU CƠ BẢN TRONG PYTHON
''' Trong bài học này ta sẽ khám phá Datatype trong Python '''
''' Để kiểm tra kiểu dữ liệu, ta dùng lệnh type(thứ cần kiểm tra) '''

# 1. KIỂU SỐ HỌC
# a> Số nguyên (int)
# - Là các số nguyên trải dài từ âm vô cùng đến dương vô cùng
# - VD: 10
# - Ta có thể chuyển các dạng số khác về kiểu nguyên:
# - Cú pháp: int(Số cần chuyển)
# - Ví dụ: int("5") hoặc int(5.7)
# (?): Dùng lệnh print() để xuất ra kết quả của 2 ví dụ trên
# (?): Sử dụng type() và print để kiểm tra kiểu dữ kiệu của 2 ví dụ

# a> Số thập phân (float)
# - Là các con số trải từ âm đến dương vô cùng và tối đa sau
# giấu thập phân là 16 con số
# - VD: 5.5 12.1234567891234567 7.0
# - Hãy xem kết quả của phép tính sau:
print(7.00 + 8.00)

# c> Số phức (complex)
# - Trong toán lớp 12 ta đã tìm hiểu về số phức
# - Cho ví dụ sau: 2 + 3j
# (?): Sử dụng type(2 + 3j) và xem kết quả
# (?): Xác định phần thực và phần ảo của ví dụ
print(type(2 + 3j))

# 2. Kiểu chuỗi (string)
# - Chuỗi hay string là 1 chuỗi các kí tự từ a đến z, 0 đến 9, các kí tự đặc biệt
# - Chuỗi luôn được đặt trong cặp ngoặc "..." hoặc '...'
# - Ví dụ 1: "Địt mẹ chúng mày tuổi loz"
# - Ví dụ 2: "Tùng đẹp trai 18/2"
# - Các kí tự trong chuỗi đều có 1 số thứ tự, bắt đầu từ 0
# - Ví dụ 3: Trong chuỗi "Hoàng Văn Tùng", kí tự thứ 0 là H
# (?): Kí tự thứ 5 trong chuỗi "Hoàng Văn Tùng" là gì?
# - Khi ta xét chuỗi từ trái qua phải, stt bắt đầu từ 0
# - Khi ta xét chuỗi từ phải qua trái, stt bắt đầu từ -1
# - Để lấy kí tự thứ x trong chuỗi, ta dùng cú pháp "Chuỗi"[x]
# - Ta cũng có thể lấy ra nhiều kí tự bằng cú pháp "Chuỗi"[x:y]
#    + Trong đó x là điểm bắt đầu
#    + Còn y là điểm kết thúc
# (?): Xuất ra kí tự thứ 6 trong chuỗi "Hoàng Văn Tùng"
# (?): Xuất ra chữ Tùng trong chuỗi "Hoàng Văn Tùng

'''
3. Kiểu Boolean
- Kiểu Boolean chỉ gồm 2 giá trị True và False
- True là đúng, ứng với 1
- False, ứng với 0
- Boolean thường được dùng trong vòng lặp hoặc cấu trúc rẽ nhánh

4. Kiểu None
- Nghĩa là kiểu vô định

5. Kiểu danh sách (list)
- Trong các ngôn ngữ khác, list còn đc gọi là mảng(array)
- Hãy tưởng tượng list là 1 cái thùng, cái thùng này có thể chứa đc
string, số, ... các kiểu dữ liệu khác, nó là kho lưu trữ dữ liệu trong
hầu hết các ngôn ngữ lập trình
- Để tạo ra 1 list, ta dùng cặp ngoặc […]
- Ví dụ: ["Tùng Hoàng", 1999]
- Mỗi phần tử trong list được ngăn cách bởi dấu phẩy
- Mỗi phần tử đều được gắn với 1 số thứ tự (index)
- Index trải từ 0 đến N (Trái -> Phải) và -1 đến -N (Phải -> Trái)
- Cũng như string, để lấy các phần tử trong list, ta dùng [số thứ tự]
- Ví dụ 2: Hãy thử print(["Tùng", "Đẹp", "Trai"][1])
- Ví dụ 3: Hãy thử print(["Tùng", "Đẹp", "Trai"][1:3])
- Ngoài ra ta còn có cú pháp [x:y:z] trong đó z là bước nhảy khi lấy dữ liệu
- Giả sử ta có 1 list gồm 1,2,3,4,5,6,7,8 cho z = 2
    => Ta lấy ra được 1,3,5,7, thử nhé: print([1,2,3,4,5,6,7,8][0:7:2])

6. Kiểu tuple (bộ)
- Là 1 dạng đặc biệt của list nhưng dữ liệu bên trong nó là bất biến
- Một tuple có dạng (...)
- VD: ("Tùng", 1999)

7. Kiểu Set
- Khái niệm: set là 1 dạng list nhưng không tồn tại thứ tự
- Các phần tử bên trong set không trùng lặp và không thể bị thay đổi
mặc dù ta có thể thêm hoặc xóa
- Cú pháp: {...}
- Ví dụ: setA = {"Hoàng", "Văn", "Tùng", 1999}
- Do các phần tử trong set là bất biến lên không thể lưu trữ 1 list hoặc 1 Dictionary trong set
(?): Kết quả của print({1, 1, 1, 2, 3}) là gì?

8. Kiểu Dictionary
- Dictionary còn được gọi là object trong các ngôn ngữ lập trình khác, cũng như list, đây
là 1 trong 2 kiểu dữ liệu cần được quan tâm nhất trong bất cứ ngôn ngữ lập trình nào
- Các phần tử bên trong nó được cấu tạo bởi key:value và được đặt bên trong cặp {...} giống set
    + key: là 1 chuỗi hoặc số, các key trong dictionary không được trùng nhau
    + value: bất cứ 1 kiểu dữ liệu nào 
- Ví dụ 1 : {"name":"Hoàng Văn Tùng", "birtday":[18, 2, 1999], 1:{2:3, 3:4}}
- Để lấy các phần tử trong dictionary, ta có cú pháp: {Dictionary}[key]
- Ví dụ 2: 
    Cho {"name":"Tùng", "age":21, 1999:"Năm Sinh"}
    Gọi ra name: print({"name":"Tùng", "age":21, 1999:"Năm Sinh"}["name"])
    (?): Hãy lấy ra age và 1999

9. Kiểu phạm vi (range)
- Là phạm vi sử dụng số học trong Python, thường được dùng trong các vòng lặp
- Cú pháp: range(start, end)
    start: số bắt đầu
    end: số kết thúc
- Ví dụ: range(1, 5)
- Ngoài ra còn có range(start, end, step) trong đó step là bước nhảy 
- Kiểu dữ liệu này sẽ được học trong các bài về vòng lặp...

'''
