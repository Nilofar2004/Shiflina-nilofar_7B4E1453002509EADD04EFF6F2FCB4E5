#Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.

class Student:
  
 def __init__(self,name,roll_no,cgpa):
  self.name=name
  self.roll_no=roll_no
  self.cgpa=cgpa

def sort_students(studentlist):
  sorted_students= sorted(studentlist,
                         key=lambda student:student.cgpa,reverse=True)
  return sorted_students

#example usage
students=[Student("abi\t","a365f\t",8.9),
          Student("kabi\t","b37u8\t",9.2),
          Student("sabi\t","c754c\t",6.7),
          Student("nabi\t","d676g\t",8.1)]

sorted_students= sort_students(students)

for student in sorted_students:
  print("NAME:",student.name,"ROLL_NO:",student.roll_no,"CGPA:",student.cgpa)
  