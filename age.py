from tkinter import *
from tkcalendar import DateEntry

class main():
    def __init__(self, root):
        self.root = root
        self.root.title("Age calculator")
        self.root.geometry("300x500")
        self.root.config(bg='black')
        self.cake = PhotoImage(file='cake.png')

       
        Label(root, text="Date of birth", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=10)
        Label(root, text="Date", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=60)
        self.birth_date = DateEntry(root, background='black')
        self.birth_date.place(x=200, y=15)
        self.current_date = DateEntry(root, background='black')
        self.current_date.place(x=200, y=65)

        # Claculate button
        Button(root, text="Calculate", bg="#ff5d00", command=self.calculate).place(x=10, y=110, width=280)

        # main result frame
        result_frame = Frame(root, bg='#222426')
        result_frame.place(x=10, y=150, width=280, height=310)

        # sub frame 1 for Age section
        frame_1 = Frame(result_frame, bg='#222426', bd=1, relief=GROOVE)
        frame_1.place(x=0, y=0, width=140, height=150)
        Label(frame_1, text="Age", bg='#222426', fg='white', font=('arial 25 bold')).place(x=10, y=10)
        self.total_year = Label(frame_1, text="00", bg='#222426', fg='#ff5d00', font=('arial 30 bold'))
        self.total_year.place(x=10, y=60)
        Label(frame_1, text="years", bg='#222426', fg='white', font=('arial 10 bold')).place(x=70, y=80)
        self.total_month = Label(frame_1, text="00 months | 0 day", bg='#222426', fg='white', font=('arial 10 bold'))
        self.total_month.place(x=10, y=110)

        # sub frame 2 for Next birthday section
        frame_2 = Frame(result_frame, bg='#222426', bd=1, relief=GROOVE)
        frame_2.place(x=140, y=0, width=140, height=150)
        Label(frame_2, text="Next birthday", bg='#222426', fg='#ff5d00', font=('arial 10 bold')).place(x=25, y=20)
        Label(frame_2, image=self.cake, fg='white').place(x=55, y=50)
        self.next_birth_day = Label(frame_2, text="", bg='#222426', fg='white', font=('arial 12 bold'))
        self.next_birth_day.place(x=30, y=80)
        self.next_birth_day_left = Label(frame_2, text="0 month | 0 day", bg='#222426', fg='white', font=('arial 10 bold'))
        self.next_birth_day_left.place(x=20, y=110)

        # sub frame 3 for Summary section
        frame_3 = Frame(result_frame, bg='#222426', bd=1, relief=GROOVE)
        frame_3.place(x=0, y=150, width=280, height=160)
        Label(frame_3, text="Summary", bg='#222426', fg='#ff5d00', font=('arial 15 bold')).place(x=90, y=10)
        Label(frame_3, text="Years", bg='#222426', fg='white', font=('arial 10')).place(x=20, y=40)
        Label(frame_3, text="Months", bg='#222426', fg='white', font=('arial 10')).place(x=100, y=40)
        Label(frame_3, text="Weeks", bg='#222426', fg='white', font=('arial 10')).place(x=190, y=40)
        Label(frame_3, text="Days", bg='#222426', fg='white', font=('arial 10')).place(x=20, y=100)
        Label(frame_3, text="Hours", bg='#222426', fg='white', font=('arial 10')).place(x=100, y=100)
        Label(frame_3, text="Minutes", bg='#222426', fg='white', font=('arial 10')).place(x=190, y=100)

        self.summary_year = Label(frame_3, text="00", bg='#222426', fg='white', font=('arial 15 bold'))
        self.summary_year.place(x=20, y=60)
        self.summary_month = Label(frame_3, text="00", bg='#222426', fg='white', font=('arial 15 bold'))
        self.summary_month.place(x=100, y=60)
        self.summary_weeks = Label(frame_3, text="00", bg='#222426', fg='white', font=('arial 15 bold'))
        self.summary_weeks.place(x=190, y=60)
        self.summary_days = Label(frame_3, text="00", bg='#222426', fg='white', font=('arial 15 bold'))
        self.summary_days.place(x=20, y=120)
        self.summary_hours = Label(frame_3, text="00", bg='#222426', fg='white', font=('arial 15 bold'))
        self.summary_hours.place(x=100, y=120)
        self.summary_minutes = Label(frame_3, text="00", bg='#222426', fg='white', font=('arial 15 bold'))
        self.summary_minutes.place(x=185, y=120)

    def calculate(self):
        import datetime
        now = datetime.datetime.now()
        current = self.current_date.get_date()
        birth = self.birth_date.get_date()

        current_date = datetime.datetime.strptime(str(current), '%Y-%m-%d')
        birth_date = datetime.datetime.strptime(str(birth), '%Y-%m-%d')

        next_birthday_1 = datetime.datetime(current_date.year, birth_date.month, birth_date.day)
        next_birthday_2 = datetime.datetime(current_date.year+1, birth_date.month, birth_date.day)
        next_birthday = next_birthday_1 if next_birthday_1 > now else next_birthday_2

        days_left_for_next = next_birthday - current_date
        days_left = current_date - birth_date

        years = ((days_left.total_seconds())/(365.242*24*3600))
        years_int = int(years)
        months = (years - years_int)*12
        months_int = int(months)
        days = (months - months_int)*(365.242/12)
        days_int = int(days)
        hours = (days - days_int)*24
        hours_int = int(hours)
        minutes = (hours - hours_int)*60
        minutes_int = int(minutes)
        # seconds = (minutes - minutes_int)*60

        self.total_year.config(text=years_int)
        self.total_month.config(text=str(months_int)+" months | "+str(days_int)+" day")
        self.summary_year.config(text=years_int)
        self.summary_month.config(text=years_int*12+months_int)
        self.summary_weeks.config(text=days_left.days//7)
        self.summary_days.config(text=days_left.days)
        self.summary_hours.config(text=days_left.days*24)
        self.summary_minutes.config(text=int(days_left.total_seconds()//60))
        self.next_birth_day.config(text=next_birthday.strftime('%A'))
        self.next_birth_day_left.config(text=str(days_left_for_next.days//30) + ' month | ' + str(days_left_for_next.days%30) + ' days')


root = Tk()
obj = main(root)
mainloop()

