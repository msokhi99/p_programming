# Without using List Comprehension: 
numbers=[1,2,3]
updated_numbers=[]
for number in numbers:
    new_num=number+1
    updated_numbers.append(new_num)
print(f"Updated Numbers: {updated_numbers}")

# With using List Comprehension: 
updated_numbers_using_list_comp=[number+1 for number in numbers]
print(f"Using List Comprehension: {updated_numbers_using_list_comp}")

# Doubling the value of a number using List Comprehension: 
doubled_values=[number*2 for number in range(1,5)]
print(f"Doubled Values: {doubled_values}")

# Conditional List Comprehension: 
names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
short_names=[name for name in names if len(name)<5]
print(f"Short Names: {short_names}")

capitalized_names=[name.upper() for name in names if len(name)>5]
print(f"Capitalized Names: {capitalized_names}")

# Squaring Numbers: 
squared_numbers=[num**2 for num in range(1,10)]
print(f"Squared Numbers: {squared_numbers}")

# Filtering Even Numbers:
filtered_even_numbers=[num for num in range(1,101) if num%2==0]
print(f"Filtered Even Numbers: {filtered_even_numbers}")

# Data Overlap: 
with open("./random_number_file_one.txt",mode="w") as file_one:
    for num in range(35,60):
        file_one.write(f"{str(num)}\n")
with open("./random_number_file_two.txt",mode="w") as file_two:
    for num in range(1,50):
        file_two.write(f"{str(num)}\n")

with open("./random_number_file_one.txt",mode="r") as file_one:
    number_list_one=[int(num) for num in file_one]
    print(f"File 1 Numbers: {number_list_one}")

with open("./random_number_file_two.txt",mode="r") as file_two:
    number_list_two=[int(num) for num in file_two]
    print(f"File 2 Numbers: {number_list_two}")

file_list_with_same_number=[num for num in number_list_one if num in number_list_two]
print(f"Files containing both the numbers: {file_list_with_same_number}")

# Dictionary Comprehension:
import random 
student_scores={name:random.choice(range(1,101)) for name in names}
print(f"Student Scores Dict: {student_scores}")

passed_students={name:score for (name,score) in student_scores.items() if score>60}
print(f"Passed Students: {passed_students}")

with open("random_file_containing_a_sentence.txt",mode="w") as current_file:
    current_file.write("Hello, my name is Mantej.")

with open("random_file_containing_a_sentence.txt",mode="r") as current_file:
    contents=current_file.read()
    sentence_words=contents.replace(",","").replace(".","").split()
    sentence_words_dict={word:len(word) for word in sentence_words}
print(sentence_words_dict)

random_number=random.randint(0,50)

weather_dict_in_celsius={"Monday":random_number,"Tuesday":random_number,"Wednesday":random_number,"Thursday":random_number,"Friday":random_number,"Saturday":random_number,"Sunday":random_number,}
weather_dict_in_fahrenheit={day:(weather_in_celsius*9/5)+32 for (day,weather_in_celsius) in weather_dict_in_celsius.items()}
print(f"Weather Dict in F: {weather_dict_in_fahrenheit}")
