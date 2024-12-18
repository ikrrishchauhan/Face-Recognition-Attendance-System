from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os
import subprocess


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACEROLL - Face Recognition System")

        # first image
        img = Image.open(r"/Users/ikrrishnchauhan/Downloads/FACE_RECOGNITION-SYSTEM-master/picss/p2.jpeg")
        img = img.resize((500, 130), resample=Image.LANCZOS)

        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second image
        img1 = Image.open(r"/Users/ikrrishnchauhan/Downloads/FACE_RECOGNITION-SYSTEM-master/picss/p2.jpeg")
        img1 = img1.resize((500, 130), resample=Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open(r"/Users/ikrrishnchauhan/Downloads/FACE_RECOGNITION-SYSTEM-master/picss/p2.jpeg")
        img2 = img2.resize((500, 130), resample=Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # bg image
        img3 = Image.open(r"/Users/ikrrishnchauhan/Downloads/FACE_RECOGNITION-SYSTEM-master/picss/p6.jpeg")
        img3 = img3.resize((1530, 710), resample=Image.LANCZOS)

        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="Face Recognition Attendance System", font=("times new roman", 35),
                          bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1380, height=45)

        # student button
        img4 = Image.open(r"/Users/ikrrishnchauhan/Downloads/FACE_RECOGNITION-SYSTEM-master/picss/p8.jpeg")
        img4 = img4.resize((220, 220), resample=Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=100, y=100, width=220, height=220)

        b1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2",
                    font=("times new roman", 15, "bold"), bg="white", fg="black")
        b1.place(x=100, y=300, width=220, height=40)

        # Detect face button
        img5 = Image.open(r"/Users/ikrrishnchauhan/Downloads/FACE_RECOGNITION-SYSTEM-master/picss/p12.jpeg")
        img5 = img5.resize((220, 220), resample=Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b1.place(x=600, y=100, width=220, height=220)

        b1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data,
                    font=("times new roman", 15, "bold"), bg="white", fg="black")
        b1.place(x=600, y=300, width=220, height=40)

        # Attendance face button
        img6 = Image.open(r"/Users/ikrrishnchauhan/Downloads/FACE_RECOGNITION-SYSTEM-master/picss/p13.jpeg")
        img6 = img6.resize((220, 220), resample=Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        b1.place(x=1000,y=100,width=220,height=220)
        
        b1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data,
                    font=("times new roman", 15, "bold"), bg="white", fg="black")
        b1.place(x=1000, y=300, width=220, height=40)

        # Train face button
        img8 = Image.open(r"/Users/ikrrishnchauhan/Downloads/FACE_RECOGNITION-SYSTEM-master/picss/p15.jpeg")
        img8 = img8.resize((220, 220), resample=Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b1.place(x=100, y=380, width=220, height=220)

        b1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data,
                    font=("times new roman", 15, "bold"), bg="white", fg="black")
        b1.place(x=100, y=580, width=220, height=40)

        # Photos face button
        img9 = Image.open(r"/Users/ikrrishnchauhan/Downloads/FACE_RECOGNITION-SYSTEM-master/picss/p18.jpeg")
        img9 = img9.resize((220, 220), resample=Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b1.place(x=600, y=380, width=220, height=220)

        b1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img,
                    font=("times new roman", 15, "bold"), bg="white", fg="black")
        b1.place(x=600, y=580, width=220, height=40)

        # Exit face button
        img11 = Image.open(r"/Users/ikrrishnchauhan/Downloads/FACE_RECOGNITION-SYSTEM-master/picss/p17.jpeg")
        img11 = img11.resize((220, 220), resample=Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iexit)
        b1.place(x=1000, y=380, width=220, height=220)

        b1 = Button(bg_img, text="Exit", cursor="hand2", command=self.iexit,
                    font=("times new roman", 15, "bold"), bg="white", fg="black")
        b1.place(x=1000, y=580, width=220, height=40)

    def open_img(self):
        subprocess.run(["open", "data"])

    def iexit(self):
        self.iexit = messagebox.askyesno("Face Recognition", "Are you sure exit this Project?")
        if self.iexit > 0:
            self.root.destroy()
        else:
            return

    # ============Functions Buttons============

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()