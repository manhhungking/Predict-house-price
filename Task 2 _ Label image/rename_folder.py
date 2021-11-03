import os
import pandas as pd
import shutil


name_change = []
need_delete = []


def rename(path, rename_cols):
    for root, subdirectories, files in os.walk(path):
        if len(files) == 0:
            need_delete.append(path)
            return

    head, tail = os.path.split(path)
    property_code = int(tail)
    row = rename_cols.loc[rename_cols['property_code'] == property_code]

    if row.empty:
        need_delete.append(path)
        return

    folder_new_name = str(int(row['price_unit']))
    new_path = os.path.join(head, folder_new_name)
    for i in range(1, 1000):
        if os.path.isdir(new_path):
            folder_new_name = str(int(row['price_unit'])) + '_' + str(i)
            new_path = os.path.join(head, folder_new_name)

    name_change.append(str(tail) + '__' + str(folder_new_name))

    os.rename(path, new_path)


directory = "D:\Label folder\Table"

sub_directory_list = []

data = pd.read_csv('updatecsv.csv')
rename_columns = data[['property_code', 'price_unit']]

for root, subdirectories, files in os.walk(directory):
    for subdirectory in subdirectories:
        sub_directory_list.append(str(os.path.join(root, subdirectory)))

for i in range(len(sub_directory_list)):
    rename(sub_directory_list[i], rename_columns)

for nc in name_change:
    print(nc)
print('--------------------------------------------')
for nd in need_delete:
    print(nd)
    shutil.rmtree(nd)
# for root, subdirectories, files in os.walk(n):
#     if len(files) == 0:
#         print('There are no files')
#     else:
#         print('Stored files')


# for root, subdirectories, files in os.walk(directory):
#     for subdirectory in subdirectories:
#         sub_directory_list.append(subdirectory)
#
# for i in range(len(sub_directory_list)):
#     print(sub_directory_list[i])

# data = pd.read_csv('updatecsv.csv')
# rename_columns = data[['property_code', 'price_unit']]
#
# property_code = int('26768990')
#
# row = rename_columns.loc[rename_columns['property_code'] == property_code]
# new_name = str(int(row['price_unit']))
#
# print(new_name)
# print(os.path.split(sub_directory_list[0]))




