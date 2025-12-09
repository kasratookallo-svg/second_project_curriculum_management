
#--------------------------------------------------------------------------------------------------

#                               Curriculum Application
#                <<<<<<         Made by Kasra Tookallo           >>>>>>
#                                   2025 the year
#                                    12/6/2025
#--------------------------------------------------------------------------------------------------
from study_model import *
from study_controller import LessonController
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

print("Start.")
print("-" * 150)
#-------------------------------------------------------------------------------------------
#                                               Reset command for table
def reset_table():
    lesson_name.set("")
    lesson_code.set(0)
    teacher_name.set("")
    lesson_credits.set(0)
    status, study_list = LessonController.find_all()

    for row in table.get_children():
        table.delete(row)

    if status:
        for lesson in study_list:
            table.insert("", END, values=lesson)
    else:
       messagebox.showerror("Error","No lesson found")

#------------------------------------------------------------------------------------------
#                                               Getting Lesson Data
study_list = []
def receive_data():
    try :
        lesson = Curriculum(
            lesson_name.get() ,
            lesson_code.get() ,
            teacher_name.get(),
            lesson_credits.get()
        )
        lesson.validation()
        study_list.append(lesson)
        lesson.save()
        print("-" * 150)

        #To insert Data into the table
        table.insert(""  , END , values=lesson.to_tuple())
        messagebox.showinfo("Data Saved." , "Lesson saved in the table successfully.")
        print("Your Curriculum includes : ",study_list)
        print("-" * 150)
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:{e}")

def select_lesson(event):
    lesson = table.item(table.focus())["values"]
    lesson_name.set(lesson[0])
    lesson_code.set(lesson[1])
    teacher_name.set(lesson[2])
    lesson_credits.set(lesson[3])

def save_click():
    status, message = LessonController.save(
        lesson_name.get(),
        lesson_code.get(),
        teacher_name.get(),
        lesson_credits.get(),
    )
    if status:
        reset_table()
        messagebox.showinfo("Lesson Save", message)
    else:
        messagebox.showerror("Lesson Saving Error", message)


def edit_click():
    status, message = LessonController.edit(
        lesson_name.get(),
        lesson_code.get(),
        teacher_name.get(),
        lesson_credits.get(),
    )
    if status:
        reset_table()
        messagebox.showinfo("Lesson Edit", message)
    else:
        messagebox.showerror("Lesson Editing Error", message)


def remove_click():
    status, message = LessonController.remove(lesson_code.get())
    if status:
        reset_table()
        messagebox.showinfo("Lesson Remove", message)
    else:
        messagebox.showerror("Lesson Remove Error", message)

# ---------------------------

def total_credit():
    pass

#------------------------------------------------------------------------------------------------------
#                                             Table Starts Here
Window = Tk()
#Main Heading
Window.title("Welcome to Curriculum App")
Window.geometry("435x518")
Window.configure(bg="purple")

# Label & Entry 1
Label(Window, text="Lesson Name\n{3,30}char.",fg="darkblue",background="grey").place(x=10, y=100,width=85)
lesson_name = StringVar()
ttk.Combobox(Window, textvariable=lesson_name,
             values=( "Computer Programming.Python", "Math I" , "Math II", "Engineering Mathematics" ,"Physics I","Physics II" , "Statics" )).place(x=100, y=100, width=160)

# Label & Entry 2
Label(Window, text="Lesson Code\n>0",fg="darkblue",background="grey").place(x=10, y=150,width=85)
lesson_code = IntVar()
ttk.Combobox(Window, textvariable=lesson_code,values=("352536","789485","158794","5789","976","145","29864")).place(x=100, y=150,width=160)

# Label & Entry 3
Label(Window, text="Teacher Name\n{3,30}char.",fg="darkblue",background="grey").place(x=10, y=200 ,width=85)
teacher_name = StringVar()
ttk.Combobox(Window, textvariable=teacher_name, values=("Mr.Messbah","Ms.Miri","Mr.Akbari","Ms.Gohari")).place(x=100, y=200, width=160)

# Label & Entry 4
Label(Window, text="Lesson Credits\n>0",fg="darkblue",background="grey").place(x=10, y=250,width=85)
lesson_credits = IntVar()
ttk.Combobox(Window, textvariable=lesson_credits, values=("1","2","3")).place(x=100, y=250,width=160)
#---------------------------------------------------------------------------------------------------------------------------
#                                           Description
Label(Window, text="Please Pay Attention!!!"
                   "\n\n\nAfter executing the program,"
                   "\nyour data won't be saved"
                   "\nfor future reference"
                   "\nautomatically,"
                   "\n\n---unless---"
                   "\nyou 'Submit' it to databse.",
      fg="darkblue",background="lightblue").place(x=265, y=100,height=190,width=159)

Label(Window, text="Instruction:"
                   "\n1-Enter Study_Related Information."
                   "\n2-Click on 'Show in Table' to represent your studies."
                   "\n3-Select on your study in the table."
                   "\n4-Your study's detail appears on each icon."
                   "\n5-Submit your study case_by_case to database.",
      fg="darkblue", background="grey").place(x=10, y=400, height=100, width=415)

#---------------------------------------------------------------------------------------------------------------------------------

#Buttons
Button(Window, text="Show in Table", command=receive_data , width=58,fg="darkblue", background="lightgreen").place(x=10, y=305)
Button(Window, text="Submit to Database", command=save_click,fg="darkblue", background="grey").place(x=10, y=350 ,width=140)
Button(Window, text="Edit Lesson", command=edit_click,fg="darkblue", background="grey").place(x=152, y=350 ,width=125)
Button(Window, text="Remove from Database" , command=remove_click,fg="darkblue", background="grey").place(x=280, y=350 ,width=144)


#Headings _Region Table
table = ttk.Treeview(Window , columns=(1,2,3,4)
                     , height=10 , show="headings")
#Column 1
table.heading(1, text="Lesson Name")
table.column(1, width=170)

#Column 2
table.heading(2, text="Lesson Code")
table.column(2, width=50)

#Column 3
table.heading(3, text="Teacher Name")
table.column(3, width=50)

#Column4
table.heading(4, text="Credits")
table.column(4, width=10)

table.place(x=10, y=10 , width=415, height=75)
table.bind("<<TreeviewSelect>>", select_lesson)

reset_table()
Window.mainloop()
