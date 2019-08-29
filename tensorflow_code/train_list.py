import os
class_names_to_ids = {'0': 0, '1': 1, '2': 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                      "A": 10, "B": 11, "D": 12, "F": 13, "J": 14, "R": 15, "V": 16, "Y": 17}
data_dir = '/home/jdmking/Desktop/gjh/Train_data/'
output_path = '/home/jdmking/Desktop/gjh/list.txt'
fd = open(output_path, 'w')
for class_name in class_names_to_ids.keys():
    images_list = os.listdir(data_dir + class_name)
    for image_name in images_list:
        fd.write('{}/{} {}\n'.format(class_name, image_name, class_names_to_ids[class_name]))
fd.close()