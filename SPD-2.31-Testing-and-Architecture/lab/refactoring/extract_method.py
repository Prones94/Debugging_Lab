import math
​
def get_student_grades():
    # Get students' grades from user input
    grade_list = []
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list
​
def get_mean(grade_list):
    # Calculate mean
    sum_of_grades = 0
    for grade in grade_list:
        sum_of_grades = sum_of_grades + grade
    mean = sum_of_grades / len(grade_list)
    return mean
​
def get_standard_deviation(grade_list, mean):
    # Calculate standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    standard_deviation = math.sqrt(sum_of_sqrs / len(grade_list))
    return standard_deviation
​
def print_stat():
    grade_list = get_student_grades()
    print('****** Grade Statistics ******')
    mean = get_mean(grade_list)
    print("The grades's mean is:", mean)
    standard_deviation = get_standard_deviation(grade_list, mean)
    print('The population standard deviation of grades is: ', round(standard_deviation, 3))
    print('****** END ******')
​
print_stat()
