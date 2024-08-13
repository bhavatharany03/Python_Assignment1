from student_management import StudentManagementSystem

if __name__ == "__main__":
    sms = StudentManagementSystem()

    # Adding Students
    sms.add_student("Parkavi","parkavi@gmail.com")
    sms.add_student("Shraddha","shraddha@gmail.com")
    sms.add_student("Iqbal","iqbal@gmail.com")

    # Adding Courses
    sms.add_course("Data Science")
    sms.add_course("Networking")
    sms.add_course("Data Structure")


    # Enrolling Students in Courses
    sms.enroll_student_in_course("1", "1")  
    sms.enroll_student_in_course("2", "2")  
    sms.enroll_student_in_course("3","3")   
    sms.enroll_student_in_course("2", "3")  

    # Assigning Grades
    sms.assign_grade("1", "1", 85)  
    sms.assign_grade("2", "2", 90)  
    sms.assign_grade("3", "3", 84)  
    sms.assign_grade("2", "3", 67)

    # Calculating GPA
    sms.calculate_gpa("1")  
    sms.calculate_gpa("2")  
    sms.calculate_gpa("3")  
