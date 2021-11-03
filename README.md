# Predict house price
Trong dự án này, nhóm đang tìm cách làm sạch dữ liệu thô, gán giá cho mỗi thư mục ảnh chứa giá nhà và phân loại ảnh. Sau đó áp dụng mô hình để dự đoán giá nhà.
## Task 1: Clean data and perform some simple estimation
Công việc cho task này bao gồm việc chuyển đổi các giá trị ví dụ ở price_unit thành chung 1 đơn vị, dọn các cột có "Thỏa thuận" . . . plot các diagrams
Sử dụng các thuật toán như Linear Regression, Lasso, Regression Tree lên dataset mới tạo ra. Xem xét về tính đúng đắn trước việc thực hiện với dùng thêm dataset là ảnh.
## Task 2: Labeling image
Công việc label lại các file hình ảnh được làm local trên máy tính thông qua một đoạn code. Từ việc preprocess, nhóm xuất được 1 file csv chứa property_code và price_unit liên quan tới ảnh. <br/>
directory là đường dẫn chứa thư mục có các folder mà tên mỗi folder là property_code.<br/>
[![directory.png](https://i.postimg.cc/5NxPrz01/directory.png)](https://postimg.cc/BtVcLXHw)<br/><hr>
Chạy rename_folder.py code sẽ đổi tên thư mục chứa ảnh từ property_code thành price_unit. Ảnh trên biểu thị các thư mục ban đầu, ảnh dưới là kết quả sau khi chạy đoạn code đổi tên<br/><br/>
[![folder1.png](https://i.postimg.cc/tJ1h09L3/folder1.png)](https://postimg.cc/MfScVJZH)<br/><br/>
[![folder2.png](https://i.postimg.cc/tTJ6PXRK/folder2.png)](https://postimg.cc/vgRDwwVh)<br/><br/>
Trong đó, ví dụ 2_11, 2 là price_unit biểu thị giá thuê là 2 triệu/tháng, 11 là số được thêm vào để hạn chế trùng tên thư mục từ việc có nhiều ngôi nhà cho thuê giá giống nhau.<br/>
<hr>
Chạy rename_file.py sẽ hiện lên 1 giao diện để tương tác với người dùng, việc label thông qua giao diện của nhóm nhằm có được độ chính xác.<br>
<br>
