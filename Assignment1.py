#Assignment-1

Sessions_Attended = {"sessions" : "1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499"}

#Varable to store the count of Number of  sessions
No_of_Sessions = 0

#Counting the number of sessions from the given dictionary
for values_dict in Sessions_Attended.values():
    values_list = values_dict.split(",")

    for index in values_list:
        No_of_Sessions = No_of_Sessions + 1

#Print the total number of sessions attended
print ("I have attended {} sessions".format(No_of_Sessions))

'''
No_of_Sessions = len(values_list)
print (No_of_Sessions)
'''
