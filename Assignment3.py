#Assignment-3

numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]

#Extracting Values of Dictionary from the List
for dict_in_list in numbers:
    for dict_val_str in dict_in_list.values():
        #do nothing
        pass 

#Converting string into list
dict_val_list = dict_val_str.split(",")

dict_val_list = dict_val_str.

#Blank lists to store the Even and Odd numbers
even_numbers = []
odd_numbers = []

#Function to Find & Print Even Numbers
def find_even_numbers (dict_val_list):
    for list_index in dict_val_list:
        if (int(list_index) % 2 == 0):
            even_numbers.append(int(list_index))
    print ( " The Even Numbers are : "+ str(even_numbers).strip('[]'))

#Call function to print even numbers
find_even_numbers(dict_val_list)