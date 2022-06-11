from tkinter import *
from tkcalendar import Calendar
from datetime import datetime
from model import holiday
#----------------------------------------------------------------

class gui_calendar:
    def open_form_size(self,master,width,height):
        w=width
        h=height
        ws=self.root.winfo_screenwidth()
        hs=self.root.winfo_screenheight()
        x=(ws/2)-(w/2)
        y=(hs/2)-(h/2)
        master.geometry("%dx%d+%d+%d" %(w,h,x,y))

    def __init__(self):
        self.root=Tk()
        self.open_form_size(self.root,400,400)
        self.root.title("Calendar")
        self.root.resizable(0,0)


        calendar=Calendar(self.root,selectmode='day',year=2020,month=1,day=1)
        calendar.grid(row=1,column=0,pady=10,columnspan=3)

        button_info=Button(self.root,text='more information',width=15)
        button_info.grid(row=7,column=0,pady=10,columnspan=3)
        button_info.bind('<Button>',lambda event: self.show_info(event,date=calendar.get_date()))

        self.message_date=Message(self.root,text='')
        self.message_date.grid(row=8,column=0,pady=10,padx=10)

        self.message_holiday=Message(self.root,text='')
        self.message_holiday.grid(row=8,column=1,pady=10)

        self.root.columnconfigure(1,weight=2)

        self.root.mainloop()        

    def show_info(self,event,date):
        calendar_user=datetime.strptime(date,"%m/%d/%y")
        mounth_user=calendar_user.month
        day_user=calendar_user.day
        date1=holiday("https://date.nager.at/api/v2/publicholidays/2020/US")
        res=date1.search(mounth_user,day_user)
        self.message_date.config(text='Selected date : \n\n'+date,bg='#eee',fg='green',width=100)  
        self.message_holiday.config(text='holiday name : \n\n'+res,bg='#eee',fg='blue',width=150)
