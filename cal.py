import tkinter as tk
import subprocess
import math

calculation = ""
more_buttons_visible = False

def add_to_calculation(symbol):
    global calculation
    if symbol == "√":  # Check if the symbol is square root
        calculation += "math.sqrt("
    else:
        calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:  
            calculation = eval(calculation) 

            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation)
    except Exception as e:
            clear_field()
            text_result.insert(1.0,"Error" + str(e))
    
#Funciton for Clear Button
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
#End of Clear Button Function


#Functin for increasing geometry
def increase_geometry():
    global current_geometry
    if current_geometry == "300x400":
        current_geometry = "300x550"
    else:
        current_geometry = "300x400"
    root.geometry(current_geometry)
#End of Function for increasing geometry

#Functin of Invisible Buttons
def toggle_more_buttons_visibility():
    global more_buttons_visible
    if more_buttons_visible:
        hide_more_buttons()
    else:
        reveal_more_buttons()

def reveal_more_buttons():
    global more_buttons_visible
    num_buttons = len(more_buttons)
    center_y = (root.winfo_height() - (num_buttons * 30)) / 2 
    for i, button in enumerate(more_buttons):
        button.place(relx=0.5, rely=center_y/ root.winfo_height() + 0.1 * (i+1), anchor="center")
    more_buttons_visible = True

def hide_more_buttons():
    global more_buttons_visible
    for button in more_buttons:
        button.place_forget()
    more_buttons_visible = False
#End of function for Invisible Buttons

#Execution Of BMI Calculator
def execute_another_script():
    try:
        subprocess.run(['python', 'bmi.py'])
    except FileNotFoundError:
        print("Error: File not found")
#End of BMI Calculator

#Execution Of Age Calculating Calculator
def execute_another_script1():
    try:
        subprocess.run(['python', 'age.py'])
    except FileNotFoundError:
        print("Error: File not found")
#End of Age Calculating Calculator

#Adding Square Root
def add_square_root():
    add_to_calculation("math.sqrt(")
#End of Adding Square Root

#Adding Square Button
def add_square():
    number = text_result.get("1.0", "end-1c")
    if number.strip():  # Check if there's any input
        if number.isdigit():
            squared_number = int(number) ** 2
            text_result.delete("1.0", "end")
            text_result.insert("end", squared_number)
    else:
        pass
#End of Adding Square Button

#Adding Cube Button
def add_cube():
    number = text_result.get("1.0", "end-1c")
    if number.strip():  # Check if there's any input
        if number.isdigit():
            squared_number = int(number) ** 3
            text_result.delete("1.0", "end")
            text_result.insert("end", squared_number)
    else:
        pass
#End of Cube Button

#Adding Backspace Button
def backspace():
    global calculation
    calculation = calculation[:-1]  # Remove the last character
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
#End of Adding Back Space

#Adding Pi button
def pi():
    add_to_calculation("math.pi")
#End of Adding Pi button

#Adding Pi button
def tpi():
    add_to_calculation("2*math.pi")
#End of Adding Pi button

#Adding Log Button
def add_log():
    add_to_calculation("math.log"+ "(")
#End of adding Log Button

#Adding factorial
def add_factorial():
    add_to_calculation("math.factorial" +'(')
#End of Adding factorial

#Adding e
def e():
    add_to_calculation("math.e")

#Adding Trigonometric Functions
def sin_function():
    add_to_calculation("math.sin(math.radians()")

def cos_function():
    add_to_calculation("math.cos(math.radians()")

def tan_function():
    add_to_calculation("math.tan(math.radians()")

def sinh_function():
    add_to_calculation("math.sinh(")

def cosh_function():
    add_to_calculation("math.cosh(")

def tanh_function():
    add_to_calculation("math.tanh(")
#End of Trigonometric Functions

root= tk.Tk()
current_geometry = "300x400"
root.geometry(current_geometry)  
root.configure(bg="#1d3849") 

b_bg = "#205b7a"
b_bg_1 = "orange"
b_bg_2 = "#a2bbcf"

text_result = tk.Text(root, height=2, width =16,font=("Arial",24))
text_result.grid(columnspan=5, pady=10)

#Buttons

#First Row
btn_r = tk.Button(root, text="⭮", command=increase_geometry,width=5, font=("Arial"),background=b_bg_1)
btn_r.grid(row=2,column=1, padx=5, pady=5)
btn_sqr = tk.Button(root, text="√", command=add_square_root,width=5, font=("Arial"),background=b_bg)
btn_sqr.grid(row=2,column=2, padx=5, pady=5)
btn_sq = tk.Button(root, text="²", command=add_square,width=5, font=("Arial"),background=b_bg)
btn_sq.grid(row=2,column=3, padx=5, pady=5)
btn_c = tk.Button(root, text="⌫", command=backspace,width=5, font=("Arial"),background=b_bg)
btn_c.grid(row=2,column=4, padx=5, pady=5)


#Second Row
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1),width=5, font=("Arial"),background=b_bg)
btn_1.grid(row=3,column=1, padx=5, pady=5)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2),width=5, font=("Arial"),background=b_bg)
btn_2.grid(row=3,column=2, padx=5, pady=5)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3),width=5, font=("Arial"),background=b_bg)
btn_3.grid(row=3,column=3, padx=5, pady=5)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"),width=5, font=("Arial"),background=b_bg_2)
btn_plus.grid(row=3,column=4, padx=5, pady=5)

#Third Row
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4),width=5, font=("Arial"),background=b_bg)
btn_4.grid(row=4,column=1, padx=5, pady=5)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5),width=5, font=("Arial"),background=b_bg)
btn_5.grid(row=4,column=2, padx=5, pady=5)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6),width=5, font=("Arial"),background=b_bg)
btn_6.grid(row=4,column=3, padx=5, pady=5)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"),width=5, font=("Arial"),background=b_bg_2)
btn_minus.grid(row=4,column=4, padx=5, pady=5)


#Fourth Row
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7),width=5, font=("Arial"),background=b_bg)
btn_7.grid(row=5,column=1, padx=5, pady=5)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8),width=5, font=("Arial"),background=b_bg)
btn_8.grid(row=5,column=2, padx=5, pady=5)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9),width=5, font=("Arial"),background=b_bg)
btn_9.grid(row=5,column=3, padx=5, pady=5)
btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"),width=5, font=("Arial"),background=b_bg_2)
btn_mul.grid(row=5,column=4, padx=5, pady=5)

#Fifth Row
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0),width=5, font=("Arial"),background=b_bg)
btn_0.grid(row=6,column=2, padx=5, pady=5)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"),width=5, font=("Arial"),background=b_bg_2)
btn_div.grid(row=6,column=4, padx=5, pady=5)
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("),width=5, font=("Arial"),background=b_bg)
btn_open.grid(row=6,column=1, padx=5, pady=5)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"),width=5, font=("Arial"),background=b_bg)
btn_close.grid(row=6,column=3, padx=5, pady=5)

#Sixth Row
btn_equals = tk.Button(root, text="=", command=evaluate_calculation,width=12, font=("Arial"),background=b_bg_1)
btn_equals.grid(row=7,column=3, columnspan=2, padx=5, pady=5)
btn_clear = tk.Button(root, text="C", command=clear_field ,width=5, font=("Arial"),background=b_bg)
btn_clear.grid(row=7,column=2, padx=5, pady=5)
btn_more = tk.Button(root, text=":", command=toggle_more_buttons_visibility, width=5, font=("Arial"),background=b_bg)
btn_more.grid(row=7, column=1, padx=5, pady=5)
#Buttons

#Hidden Buttons

#First Row
btn_sin = tk.Button(root, text="Sinθ",command=sin_function,width=5, font=("Arial"),background=b_bg)
btn_sin.grid(row=8,column=1, padx=5, pady=5)
btn_cos = tk.Button(root, text="Cosθ", command=lambda: cos_function,width=5, font=("Arial"),background=b_bg)
btn_cos.grid(row=8,column=2, padx=5, pady=5)
btn_tan = tk.Button(root, text="Tanθ", command=tan_function,width=5, font=("Arial"),background=b_bg)
btn_tan.grid(row=8,column=3, padx=5, pady=5)
btn_pi = tk.Button(root, text="π", command=pi,width=5, font=("Arial"),background=b_bg)
btn_pi.grid(row=8,column=4, padx=5, pady=5)
#First Row

#Second Row
btn_sinh = tk.Button(root, text="sinh", command=sinh_function,width=5, font=("Arial"),background=b_bg)
btn_sinh.grid(row=9,column=1, padx=5, pady=5)
btn_cosh = tk.Button(root, text="cosh",command=cosh_function,width=5, font=("Arial"),background=b_bg)
btn_cosh.grid(row=9,column=2, padx=5, pady=5)
btn_tanh = tk.Button(root, text="tanh", command=tanh_function,width=5, font=("Arial"),background=b_bg)
btn_tanh.grid(row=9,column=3, padx=5, pady=5)
btn_log = tk.Button(root, text="log", command=add_log,width=5, font=("Arial"),background=b_bg)
btn_log.grid(row=9,column=4, padx=5, pady=5)
#Second Row

#Third Row
btn_cot = tk.Button(root, text="³", command=add_cube,width=5, font=("Arial"),background=b_bg)
btn_cot.grid(row=10,column=1, padx=5, pady=5)
btn_sec = tk.Button(root, text="2π",command=tpi,width=5, font=("Arial"),background=b_bg)
btn_sec.grid(row=10,column=2, padx=5, pady=5)
btn_cosec = tk.Button(root, text="e", command=e,width=5, font=("Arial"),background=b_bg)
btn_cosec.grid(row=10,column=3, padx=5, pady=5)
btn_log = tk.Button(root, text="x!", command=add_factorial,width=5, font=("Arial"),background=b_bg)
btn_log.grid(row=10,column=4, padx=5, pady=5)
#Third Row

#Hidden Buttons


#Code For Invisible Buttons
more_buttons = []
for i in range(2):
    if i == 0:  
        button = tk.Button(root, text=f"BMI Calculator",command=execute_another_script, background=b_bg_2)
    elif i== 1: 
        button = tk.Button(root, text=f"Age Calculator",command=execute_another_script1, background=b_bg_2)
    else:
        button = tk.Button(root, text=f"Button {i+1}", background=b_bg_2)
    button.place(relx=0.5, rely=0.5) 
    button.place_forget() 
    more_buttons.append(button)
#Code For Invisible Buttons

root.mainloop()
