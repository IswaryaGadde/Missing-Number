#Iswarya (02-10-2023): Imported time to print the timetaken for excecution of this program
import time
#Iswarya (02-10-2023): Read input values
n = int(input('Enter input list length:'))
numbers = list(map(int, input('Enter list integers seperated by space:').split()))
start_time = time.time()
#Iswarya (02-10-2023):  Add up all of the numbers from 1 to n to find the expected total.
expected_sum = (n * (n + 1)) // 2

#Iswarya (02-10-2023):  Add up the n-1 numbers that are presented.
given_sum = sum(numbers)

#Iswarya (02-10-2023):  Calculate the missing number
missing_number = expected_sum - given_sum

#Iswarya (02-10-2023):  Print the missing number
print(missing_number)

#Iswarya (02-10-2023):  Print the "Time Taken" for this script 
print("--- %s seconds ---" % (time.time() - start_time))
