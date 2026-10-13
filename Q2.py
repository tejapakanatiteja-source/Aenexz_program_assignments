
# Student Marks Analysis

marks_list = [78, 35, 92, 40, 61]#list of marks of 5 students

marks_tuple = tuple(marks_list)#type casting the list to a tuple

print("Marks List:", marks_list)#printing the marks list
print("Type of List:", type(marks_list))#printing the type of the list

print("Marks Tuple:", marks_tuple)#printing the marks tuple
print("Type of Tuple:", type(marks_tuple))#printing the type of the tuple

print("Highest Marks:", max(marks_list))#printing the highest marks
print("Lowest Marks:", min(marks_list))#printing the lowest marks

# Count students who scored at least 40
count = (
    (marks_list[0] >= 40) +
    (marks_list[1] >= 40) +
    (marks_list[2] >= 40) +
    (marks_list[3] >= 40) +
    (marks_list[4] >= 40)
)

print("Students scoring at least 40:", count)#printing the count of students scoring at least 40

# Check whether all marks are between 0 and 100
valid_marks = (
    marks_list[0] >= 0 and marks_list[0] <= 100 and
    marks_list[1] >= 0 and marks_list[1] <= 100 and
    marks_list[2] >= 0 and marks_list[2] <= 100 and
    marks_list[3] >= 0 and marks_list[3] <= 100 and
    marks_list[4] >= 0 and marks_list[4] <= 100
)

print("All marks are valid:", valid_marks)#printing only valid marks between 0 and 100

# A list is mutable, so its elements can be changed.
marks_list[0] = 80
print("Modified List:", marks_list)

# A tuple is immutable, so its elements cannot be changed.
# The following statement raises a TypeError if uncommented:
# marks_tuple[0] = 80

print("Original Tuple:", marks_tuple)
