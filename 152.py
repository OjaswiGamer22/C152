from tkinter import *
root=Tk()
root.title("Multidimensional arrays")
root.geometry("500x500")
label1=Label(root)
label1.place(relx=0.5,rely=0.2,anchor=CENTER)
array_1d=["Aadityavardhan","Tanmay","Ash","Abhiraj"]
print(array_1d[1])
array_2d=[["adityavardan","F"],["Tanmay","A+"],["Ash","E"]]
print(array_2d[1][1])
array_3d=[[["Aadityavardhan","F","You need to study!!!"],["Tanmay","A+","Excellent"],["Ash","E","You need to study!!"],["Abhiraj","B+","Good"]]]
def generate_report():
    label1["text"]=array_3d[0][0][0]+" got grade "+array_3d[0][0][1]+" and "+array_3d[0][0][2]
    
button1=Button(root, bg="royalblue",text="Generate report card" ,command=generate_report)
button1.place(relx=0.5,rely=0.4,anchor=CENTER)

root.mainloop()
