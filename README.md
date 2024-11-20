# Face-Recognition-Attendance-System

I have created a Advance face recognition Attendance system in python OpenCV with Tkinter GUI and MySQL Database.
It is implemented with many features. Below is the brief about every single feature:

1.) Student Management system: In this section, details of the students (for ex Name,roll,id,section,address,phone,email,etc) is provided and then stored in the MySQL Database.
After filling all the details,you can save,update,delete and clear information also.Also,every student photo sample is collected there.

2.)Train Photo Samples: After collecting the photo samples in a different folder, you can train them. I used HarrCascade classifier for this purpose

3.)Take Attendance with Face Detection: While taking attendance, if the sample is already present it will show that student details on the screen and if an unknown face
is found which is not in the present data set then shows unknown face on screen. It will then record the student details and its attendance status in a different 
excel sheet. After that the attendance which is stored in that excel sheet can easily exported to MySQL Database.

-->I have used the LBPH Algorithm for face recognition

