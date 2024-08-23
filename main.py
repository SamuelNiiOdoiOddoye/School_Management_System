# Import statements
import json
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog  # Importing simpledialog separately
import uuid # Importing the uuid module for generating unique student Ids

class SchoolManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("God's Grace School Management System")
        self.master.geometry("600x400")
        self.students = []
        self.teachers = []
        self.total_income = 0
        self.total_expense = 0
        
        #load existing student records from file
        self.load_student_records()
        
       
        self.create_widgets()

    #Code to load student_records  
    def load_student_records(self):
        try:
            with open("student_records.json","r") as file:
                self.students = json.load(file)
        except FileNotFoundError:
            #If the file is doesn't exist, initialize an empty list
            self.students = []    
        
        
    #Code to save student records    
    def save_student_records(self):
        with open("student_records.json","w") as file:
            json.dump(self.students, file , indent=4)                

    #Code to create widgets
    def create_widgets(self):
        # Define color variables
        bg_color = "#808080"  # Light gray for background
        text_color = "#333333"  # Dark gray for text
        btn_bg_color = "#4CAF50"  # Green for buttons
        btn_text_color = "white"  # White text for buttons

        # set background color for the main window
        self.master.configure(bg="#808080")
        
        #Title Label
        self.lbl_title = tk.Label(self.master, text="God's Grace School Management System", font=("Arial", 16), bg=bg_color , fg="#FF5733")
        self.lbl_title.pack()

        #Add student button
        self.btn_add_student = tk.Button(self.master, text="Add Student", command=self.add_student, bg="#FF5733", fg=btn_text_color)
        self.btn_add_student.pack()

        #Delete student button
        self.btn_delete_student = tk.Button(self.master, text="Delete Student", command=self.delete_student, bg="#FF5733", fg=btn_text_color)
        self.btn_delete_student.pack()
        
        #Modify student button
        self.btn_modify_student = tk.Button(self.master, text="Modify Student", command=self.modify_student, bg="#FF5733", fg=btn_text_color)
        self.btn_modify_student.pack()

        #View student records
        self.btn_view_student_records = tk.Button(self.master, text="View Student Records", command=self.view_student_records, bg="#FF5733", fg=btn_text_color)
        self.btn_view_student_records.pack()

        #Add teacher button
        self.btn_add_teacher = tk.Button(self.master, text="Add Teacher", command=self.add_teacher, bg="#FF5733", fg=btn_text_color)
        self.btn_add_teacher.pack()
        
        #modify teacher button
        self.btn_modify_teacher = tk.Button(self.master, text="Modify Teacher", command=self.modify_teacher, bg="#FF5733", fg=btn_text_color)
        self.btn_modify_teacher.pack()
        
        #view teacher records button    
        self.btn_view_teacher_records = tk.Button(self.master, text="View Teacher Records", command=self.view_teacher_records, bg="#FF5733", fg=btn_text_color)
        self.btn_view_teacher_records.pack()
        
        #view records button 
        self.btn_view_records = tk.Button(self.master, text="View Records", command=self.view_records, bg="#FF5733", fg=btn_text_color)
        self.btn_view_records.pack()

        #check profit/loss button
        self.btn_check_profit = tk.Button(self.master, text="Check Profit/Loss", command=self.check_profit_loss, bg="#FF5733", fg=btn_text_color)
        self.btn_check_profit.pack()


    #Code to add a new student record
    def add_student(self):
        #Gather Student information
        #if it's open, bring it to focus
        if hasattr(self, "add_student_window") and self.add_student_window.winfo_exists():
            self.add_student_records_window.lift()
            
        student_id = str(uuid.uuid4())[:8] # Generate unique student ID
        student_name = simpledialog.askstring("Add Student", "Enter student's name")
        if student_name is not None: #Check if input is None
            student_dob = simpledialog.askstring("Add Student ", "Enter student's date of birth (YYYY-MM-DD)")
            if student_dob is not None:
                student_class = simpledialog.askstring("Add Student ", "Enter students class/grade: ")
                if student_class is not None:
                    student_fees = simpledialog.askinteger("Add Student ", "Enter student's school fees")
                    if student_fees is not None:
                        student_gender = simpledialog.askstring("Add Student "," Enter student gender")
                        if student_gender is not None:
                            student_address = simpledialog.askstring("Add Student ", "Enter student's address")
                            if student_address is not None:
                                student_contact = simpledialog.askstring("Ask Student ", "Enter student's contact info")
                                if student_contact is not None:
                                    student_medical_info = simpledialog.askstring("Ask Student ", "Enter students medical info")
                                    student_email_address = simpledialog.askstring("Ask Student ", "Enter students email address")
                                    if student_email_address is not None:
                                        student_emergency_contact = simpledialog.askstring("Ask Student", "Enter student's emergency contact")
        
        # Create student dictionary
        student = {
            "ID" : student_id,
            "Name" : student_name,
            "DOB" : student_dob,
            "Class" : student_class,
            "Fees" : student_fees,
            "Gender" : student_gender,
            "Address" : student_address,
            "Contact" : student_contact,
            "MedicalInfo" : student_medical_info,
            "Email Address" : student_email_address,
            "Emergency Contact" : student_emergency_contact
        }
        
        #Add student to the list
        self.students.append(student)
        
        #save student records to file
        self.save_student_records()
        
        #show success message
        messagebox.showinfo("Success", f"Student {student_name} added successfully with ID {student_id}.")
        
        

        
        #Show success message
        messagebox.showinfo("Success " , f"Student {student_name} added successfully with ID {student_id} .")
        
        pass

    #Code to delete a student record
    def delete_student(self):
        student_name = simpledialog.askstring("Delete Student", "Enter Student's name to delete:")
        if student_name:
            deleted = False
            for student in self.students[:]:
                if student ["Name"] == student_name:
                    self.students.remove(student)
                    deleted = True
            if deleted:
                messagebox.showinfo("Succes", f"All records of student {student_name} have been deleted.")
            else:
                messagebox.showerror("Error", f"Student '{student_name}' not found.")            
    
    #Code to modify student records
    def modify_student(self):
        student_name = simpledialog.askstring("Modify Student","Enter student's name to modify:")
        if student_name:
           for student in self.students:
               if student["Name"] == student_name:
                   #Allow modification of student information
                   student["Name"] = simpledialog.askstring("Modify Student", "Enter student's new name:", initialvalue=student["Name"])
                   student["DOB"]=simpledialog.askstring("Modify Student", "Enter student's new date fo birth (YYYY-MM-DD):", initialvalue=student["DOB"])
                   student["Class"]=simpledialog.askstring("Modify Student", "Enter student's new class/grade:", initialvalue=student["Class"])
                   student["Fees"]=simpledialog.askstring("Modify Student","Enter student's new school fees:", initialvalue=student["Fees"])
                   student["Gender"]=simpledialog.askstring("Modify Student", "Enter student's new gender:", initialvalue=student["Gender"])
                   student["Address"]=simpledialog.askstring("Modify Student", "Enter student's new address:", initialvalue=student["Address"])
                   student["Contact"]=simpledialog.askstring("Modify Student", "Enter student's new contact:", initialvalue=student["Contact"])
                   student["MedicalInfo"]=simpledialog.askstring("Modify Student", "Enter student's new medical info:", initialvalue=student["MedicalInfo"])
                   student["Email Addres"]=simpledialog.askstring("Modify student", "Enter student's new email address:", initialvalue=student["Email Address"])
                   student["Emergency Contact"]=simpledialog.askstring("Modify Student","Enter student's new emergency contact:",initialvalue=student["Emergency contact"])
                   messagebox.showinfo("Success",f"Information of student {student_name} has been mofified.")
                   return
        messagebox.showerror("Error", f"Student '{student_name}' not found.")

    #Code to view student records
    def view_student_records(self):
        # Check if the student records window is already open
        if hasattr(self, "student_records_window") and self.student_records_window.winfo_exists():
            # If it's open, bring it to focus and return
            self.student_records_window.lift()
            return

        # Create a new window to display student records
        self.student_records_window = tk.Toplevel(self.master)
        self.student_records_window.title("Student Records")
        self.student_records_window.geometry("1000x800")  # Adjust the window size as needed

        # Create a frame to hold the student records
        records_frame = tk.Frame(self.student_records_window)
        records_frame.pack(fill=tk.BOTH, expand=True)

        # Add a scrollbar to the frame
        scrollbar = tk.Scrollbar(records_frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a canvas to scroll the frame
        canvas = tk.Canvas(records_frame, yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configure the scrollbar to scroll the canvas
        scrollbar.config(command=canvas.yview)

        # Create another frame inside the canvas to hold the student records
        student_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=student_frame, anchor=tk.NW)

        # Function to update the scroll region when the size of the student frame changes
        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        student_frame.bind("<Configure>", on_frame_configure)

        # Iterate over the students list and display their information
        for index, student in enumerate(self.students, start=1):
            student_label = tk.Label(student_frame, text=f"Student {index}:", font=("Arial", 12, "bold"))
            student_label.grid(row=index, column=0, sticky="w")

            # Display student information
            for row , (key, value) in enumerate(student.items(), start=index):
                info_label = tk.Label(student_frame, text=f"{key}: {value}" , wraplength=500 , justify="left")
                info_label.grid(row=row, column=1, sticky="w")

        # Update the scroll region to fit the contents of the student frame
        student_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    #Code to add a new teacher record
    def add_teacher(self):
        #Gather Teacher information
        teacher_id = str(uuid.uuid4())[:8] # Generate unique student ID
        teacher_name = simpledialog.askstring("Add Teacher", "Enter teacher's name")
        teacher_dob = simpledialog.askstring("Add Teacher", "Enter teacher's date of birth (YYYY-MM-DD)")
        teacher_class = simpledialog.askstring("Add Teacher ", "Enter teacher's class/grade: ")
        teacher_salary = simpledialog.askinteger("Add Teacher ", "Enter teacher's salary")
        teacher_gender = simpledialog.askstring("Add Teacher "," Enter teacher's gender")
        teacher_address = simpledialog.askstring("Add Teacher ", "Enter teacher's address")
        teacher_contact = simpledialog.askstring("Ask Teacher ", "Enter teacher's contact info")
        teacher_medical_info = simpledialog.askstring("Ask Teacher ", "Enter teacher's medical info")
        teacher_email_address = simpledialog.askstring("Ask Teacher ", "Enter teacher's email address")
        teacher_emergency_contact = simpledialog.askstring("Ask Teacher", "Enter teacher's emergency contact")
        
        
        # Create Teacher dictionary
        teacher = {
            "TID" : teacher_id,
            "Teacher Name" : teacher_name,
            "Teacher DOB" : teacher_dob,
            "Teacher Class" : teacher_class,
            "Teacher Salary" : teacher_salary,
            "Teacher Gender" : teacher_gender,
            "Teacher Address" : teacher_address,
            "Teacher Contact" : teacher_contact,
            "Teacher MedicalInfo" : teacher_medical_info,
            "Teacher Email Address" : teacher_email_address,
            "Teacher Emergency Contact" : teacher_emergency_contact
        }
        
        #Add teacher to the list
        self.teachers.append(teacher)
        
        #Show success message
        messagebox.showinfo("Success " , f"Teacher {teacher_name} added successfully with TID {teacher_id} .")
        
        pass
            
    #Code to delete a teacher record            
    def delete_teacher(self):
        teacher_name = simpledialog.askstring("Delete Teacher", "Enter Teacher's name to delete:")
        if teacher_name:
            deleted = False
            for teacher in self.teachers[:]:
                if teacher ["Teacher Name"] == teacher_name:
                    self.teachers.remove(teacher)
                    deleted = True
            if deleted:
                messagebox.showinfo("Succes", f"All records of teacher {teacher_name} have been deleted.")
            else:
                messagebox.showerror("Error", f"Teacher '{teacher_name}' not found.")           

    #Code to modify teacher record
    def modify_teacher(self):
        teacher_name = simpledialog.askstring("Modify Teacher","Enter teacher's name to modify:")
        if teacher_name:
           for teacher in self.teachers:
               if teacher["Teacher Name"] == teacher_name:
                   #Allow modification of Teacher information
                   teacher["Teacher Name"] = simpledialog.askstring("Modify Teacher", "Enter teacher's new name:", initialvalue=teacher["Teacher Name"])
                   teacher["Teacher DOB"]=simpledialog.askstring("Modify Teacher", "Enter teacher's new date fo birth (YYYY-MM-DD):", initialvalue=teacher["Teacher DOB"])
                   teacher["Teacher Class"]=simpledialog.askstring("Modify Teacher", "Enter teacher's new class/grade:", initialvalue=teacher["Teacher Class"])
                   teacher["Teacher Salary"]=simpledialog.askstring("Modify Teacher","Enter teacher's new salary:", initialvalue=teacher["Teacher Salary"])
                   teacher["Teacher Gender"]=simpledialog.askstring("Modify Teacher", "Enter teacher's new gender:", initialvalue=teacher["Teacher Gender"])
                   teacher["Teacher Address"]=simpledialog.askstring("Modify Teacher", "Enter teacher's new address:", initialvalue=teacher["Teacher Address"])
                   teacher["Teacher Contact"]=simpledialog.askstring("Modify Teacher", "Enter teacher's new contact:", initialvalue=teacher["Teacher Contact"])
                   teacher["Teacher MedicalInfo"]=simpledialog.askstring("Modify Teacher", "Enter teacher's new medical info:", initialvalue=teacher["Teacher MedicalInfo"])
                   teacher["Teacher Email Address"]=simpledialog.askstring("Modify Teacher", "Enter teacher's new email address:", initialvalue=teacher["Teacher Email Address"])
                   teacher["Teacher Emergency Contact"]=simpledialog.askstring("Modify Teacher","Enter teacher's new emergency contact:",initialvalue=teacher["Teacher Emergency contact"])
                   messagebox.showinfo("Success",f"Information of teacher {teacher_name} has been mofified.")
                   return
        messagebox.showerror("Error", f"Teacher '{teacher_name}' not found.")

    #Code to view teacher records
    def view_teacher_records(self):
        # Check if the student records window is already open
        if hasattr(self, "teacher_records_window") and self.teacher_records_window.winfo_exists():
            # If it's open, bring it to focus and return
            self.teacher_records_window.lift()
            return  
        
           # Create a new window to display student records
        self.teacher_records_window = tk.Toplevel(self.master)
        self.teacher_records_window.title("Student Records")
        self.teacher_records_window.geometry("1000x800")  # Adjust the window size as needed

        # Create a frame to hold the student records
        records_frame = tk.Frame(self.teacher_records_window)
        records_frame.pack(fill=tk.BOTH, expand=True)

        # Add a scrollbar to the frame
        scrollbar = tk.Scrollbar(records_frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a canvas to scroll the frame
        canvas = tk.Canvas(records_frame, yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configure the scrollbar to scroll the canvas
        scrollbar.config(command=canvas.yview)

        # Create another frame inside the canvas to hold the student records
        teacher_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=teacher_frame, anchor=tk.NW)

        # Function to update the scroll region when the size of the student frame changes
        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        teacher_frame.bind("<Configure>", on_frame_configure)

        # Iterate over the teacher list and display their information
        for index, teacher in enumerate(self.teachers, start=1):
            teacher_label = tk.Label(teacher_frame, text=f"Teacher {index}:", font=("Arial", 12, "bold"))
            teacher_label.grid(row=index, column=0, sticky="w")

            # Display teacher information
            for row , (key, value) in enumerate(teacher.items(), start=index):
                info_label = tk.Label(teacher_frame, text=f"{key}: {value}" , wraplength=500 , justify="left")
                info_label.grid(row=row, column=1, sticky="w")

        # Update the scroll region to fit the contents of the student frame
        teacher_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        
    #Code to view General Records    
    def view_records(self):
        # Ensure self.students and self.teachers are lists and not empty
        if not isinstance(self.students, list):
            self.students = []
        if not isinstance(self.teachers, list):
            self.teachers = []

        # Check if the records window is already open
        if hasattr(self, "records_window") and self.records_window.winfo_exists():
            self.records_window.lift()
            return

        # Create a new window to display records
        self.records_window = tk.Toplevel(self.master)
        self.records_window.title("View General Records")
        self.records_window.geometry("1000x800")  # Adjusted size for better visibility

        # Create a canvas widget
        canvas = tk.Canvas(self.records_window)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a scrollbar to the canvas
        scrollbar = tk.Scrollbar(self.records_window, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the records
        records_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=records_frame, anchor=tk.NW)

        # Function to update the scroll region when the size of the frame changes
        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        records_frame.bind("<Configure>", on_frame_configure)

        # Add labels for students and teachers
        self.lbl_students = tk.Label(records_frame, text="Students", font=("Arial", 14, "bold"))
        self.lbl_students.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.lbl_teachers = tk.Label(records_frame, text="Teachers", font=("Arial", 14, "bold"))
        self.lbl_teachers.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Display student records
        row_num = 1
        if self.students:
            for student in self.students:
                student_frame = tk.Frame(records_frame, bd=2, relief=tk.GROOVE)
                student_frame.grid(row=row_num, column=0, pady=5, padx=5, sticky="ew")

                for key, value in student.items():
                    tk.Label(student_frame, text=f"{key}: {value}").pack(anchor="w")

                row_num += 1
        else:
            tk.Label(records_frame, text="No student records found.").grid(row=row_num, column=0, pady=10, padx=10, sticky="w")

        # Display teacher records
        row_num = 1
        if self.teachers:
            for teacher in self.teachers:
                teacher_frame = tk.Frame(records_frame, bd=2, relief=tk.GROOVE)
                teacher_frame.grid(row=row_num, column=1, pady=5, padx=5, sticky="ew")

                for key, value in teacher.items():
                    tk.Label(teacher_frame, text=f"{key}: {value}").pack(anchor="w")

                row_num += 1
        else:
            tk.Label(records_frame, text="No teacher records found.").grid(row=row_num, column=1, pady=10, padx=10, sticky="w")

        # Update the Canvas scroll region to fit the entire frame
        records_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    #Code For the Profit/Loss module
    def check_profit_loss(self):
        profit_loss_window = tk.Toplevel(self.master)
        profit_loss_window.title("Profit/Loss Analysis")
        profit_loss_window.geometry("400x300")

        # Calculations
        total_income = sum(student["Fees"] for student in self.students)
        total_expense = sum(teacher["Teacher Salary"] for teacher in self.teachers)
        profit_loss = total_income - total_expense

        # Display results
        tk.Label(profit_loss_window, text=f"Total Income: {total_income}").pack(pady=10)
        tk.Label(profit_loss_window, text=f"Total Expenses: {total_expense}").pack(pady=10)
        tk.Label(profit_loss_window, text=f"Profit/Loss: {profit_loss}").pack(pady=10)

        if profit_loss > 0:
            tk.Label(profit_loss_window, text="Profit", fg="green").pack(pady=10)
        else:
            tk.Label(profit_loss_window, text="Loss", fg="red").pack(pady=10)

def main():
    root = tk.Tk()
    app = SchoolManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
