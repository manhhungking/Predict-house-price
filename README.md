# Predict house price
In this project, we are looking to clean raw data, assign a price to each photo folder containing house prices, and classify the images. Then apply the model to predict house prices.

## Task 1: Clean data and perform some simple estimation
I will briefly summarize steps we do in file [AnhTamtask1.ipynb](https://github.com/manhhungking/Predict-house-price/blob/main/Task%201%20_%20Clean%20data%20%2B%20apply%20model/AnhTamtask1.ipynb)
### Step 1: Import dataset
### Step 2: Select features
Features we gonna use are 'total_site_area', 'property_name', 'number_of_bedrooms', 'city', 'district', 'price_unit'
### Step 3: Clean NULL data
In this step, we delete rows that have "NA" value or white space like this ' ' 
### Step 4: Preprocessing price_unit, total_site_area, property_name, number_of_bedrooms and location(district + city)
#### For price_unit:
Because there are many units, we convert them to the same unit as "Triệu/tháng" but not to keep it.
![image](https://user-images.githubusercontent.com/67094879/140049461-4a21f74d-e8fc-4a10-9ec3-1ade9d24c77a.png)
#### For total_site_area:
We only remove the unit of area because they all have the same unit. 
#### For property_name:
We have 5 types of property_name, which are: "cho thuê văn phòng" or "Cho thuê văn phòng", "Cho thuê cửa hàng, ki ốt", "Nhà riêng", "Căn hộ", "Đất nền".
So we label them as number from 0 to 4.
#### For number_of_bedrooms:
There are not many things to do with these numbers except converting to float number and removing outliers on number_of_bedrooms.

#### For district + city:
There are many words that refer to the same place, so we fixed them to be the same.
After that, we concat district and city into 1 word is location.
![image](https://user-images.githubusercontent.com/67094879/140051674-f4ff6334-1d4d-4865-884b-4f3e5d23b617.png)
Next, we move those locations that have small replication that <= 10 into the same location named "other".

Because the data type is still a string, so we use **One-Hot Encoding** to convert data into number.
![image](https://user-images.githubusercontent.com/67094879/140052372-c732c148-e7fb-4cbf-9e5e-b86d30a05dc2.png)
### Step 5: Train data
Before training, we will split our dataset into training set and test set
![image](https://user-images.githubusercontent.com/67094879/140052525-5faaf928-5452-4b62-9dae-ab662b40dd3a.png)


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
