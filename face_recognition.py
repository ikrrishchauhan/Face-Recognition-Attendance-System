from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        img_top = Image.open(r"/Users/ikrrishnchauhan/Downloads/FACE_RECOGNITION-SYSTEM-master/picss/p27.jpeg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)
        
        img_bottom = Image.open(r"/Users/ikrrishnchauhan/Downloads/FACE_RECOGNITION-SYSTEM-master/picss/p28.jpeg")
        img_bottom = img_bottom.resize((880, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=630, y=55, width=880, height=700)
        
        b1 = Button(f_lbl, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 18, "bold"), bg="darkgreen", fg="black")
        b1.place(x=365, y=620, width=200, height=40)
        
    # =========attendance=============
    def mark_attendance(self, student_id, roll, name, department):
        try:
            with open("sheet.csv", "a") as f:
                now = datetime.now()
                date_string = now.strftime("%d/%m/%Y")
                time_string = now.strftime("%H:%M:%S")
                f.write(f"\n{student_id},{roll},{name},{department},{time_string},{date_string},Present")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred while marking attendance: {str(e)}")
        
    # =========face recognition==========
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            
            coord = []
            
            for(x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100*(1-predict/300))
                
                conn = mysql.connector.connect(host="localhost",username="root",password="9050081640",database="FaceRecognition")
                my_cursor = conn.cursor()
                
                my_cursor.execute("select Student_ID from student where Student_ID="+ str(id))
                i = my_cursor.fetchone()
                if i is not None and isinstance(i, list):
                    i = "+".join(i)
                else:
                    pass
        
                my_cursor.execute("select Name from student where Student_ID="+ str(id))
                n = my_cursor.fetchone()
                if n is not None and isinstance(n, list):
                    n = "+".join(n)
                else:
                    pass
                
                my_cursor.execute("select Roll from student where Student_ID="+ str(id))
                r = my_cursor.fetchone()
                if r is not None and isinstance(r, list):
                    r = "+".join(r)
                else:
                    pass
                
                my_cursor.execute("select Department from student where Student_ID="+str(id))
                d = my_cursor.fetchone()
                if d is not None and isinstance(d, list):
                    d = "+".join(d)
                else:
                    pass   
                

                
                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                    cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                    cv2.putText(img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)   
                    
                coord = [x, y, w, h]
            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml") 
        
        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)
            
            if cv2.waitKey(100) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()