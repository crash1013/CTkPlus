# CTkPlus
## CustomTkinter Widget Collection
A collection of widgets for the CustomTkinter UI library, enhancing the look and feel of traditional tkinter widgets.

## The widgets
* CTkCalandar
* CTkDialog
* CTkFontPicker
* CTkSettings
* CTkYesNo

## The Demo Application
* CTkPlusDemp.py

### CTkCalendar
CTkCalendar is a widget for selecting a date. It is based on the module tkCalendar.

![CTkCalendar screenshot](images/CTkCalendar.png)

#### Using CTkCalendar

```python
import customtkinter
from CTkCalendar import CTkCalendarDialog
from CTkDialog import CTkDialog
from datetime import date

class CalendarDialog(customtkinter.CTk):
    def __init__(self, appearance_mode='system'):
        super().__init__()

        self.custom_font = customtkinter.CTkFont(family='Ariel', size=18, weight='bold')
        self.grid_columnconfigure(0, weight=1)
        self.calendar_button_frame = customtkinter.CTkFrame(self)
        self.calendar_button_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        self.calendar_button_frame.grid_columnconfigure(0, weight=1)

        self.calendar_button = customtkinter.CTkButton(self.calendar_button_frame, text="Calendar", command=self.on_calendar, font=self.custom_font)
        self.calendar_button.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

    def on_calendar(self):
        dialog = CTkCalendarDialog(self, title='Date Selector', font=self.custom_font, initial_date=date.today())
        CTkDialog(self, "Selected Date", f"You selected '{dialog.result}'", font=self.custom_font)
       

app = CalendarDialog('light')
app.title("CTkPlus Calendar")
app.mainloop()
        


```





