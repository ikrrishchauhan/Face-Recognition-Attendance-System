import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np
import mysql.connector
 
class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        img_top = Image.open(r"/Users/ikrrishnchauhan/Downloads/FACE_RECOGNITION-SYSTEM-master/picss/p26.jpeg")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)
        
        b1 = Button(self.root, text="TRAIN DATA", cursor="hand2", command=self.train_classifier,
                    font=("times new roman", 30, "bold"), bg="blue", fg="black")
        b1.place(x=0, y=380, width=1530, height=60)
        
        img_bottom = Image.open(r"/Users/ikrrishnchauhan/Downloads/FACE_RECOGNITION-SYSTEM-master/picss/p26.jpeg")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir = "data"
        
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory not found.")
            return

        faces = []
        ids = []

        for file in os.listdir(data_dir):
            if file.endswith(".jpg") or file.endswith(".png"):
                try:
                    image_path = os.path.join(data_dir, file)
                    img = Image.open(image_path).convert('L')
                    image_np = np.array(img, 'uint8')
                    face_id = int(os.path.splitext(file)[0].split('.')[1])

                    faces.append(image_np)
                    ids.append(face_id)

                    cv2.imshow("Training", image_np)
                    cv2.waitKey(1)
                except Exception as e:
                    print(f"Error processing image {file}: {e}")

        ids = np.array(ids)

        # Train the classifier and Save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
