# CTkPlusDemo.py
import os
from datetime import date

import customtkinter
from CTkYesNo import CTkYesNo
from CTkDialog import CTkDialog
from CTkSettings import CTkSettings
from CTkCalendar import CTkCalendarDialog


class CTkPlusDemoApp(customtkinter.CTk):

    def __init__(self, appearance_mode='system'):
        super().__init__()
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.settings = CTkSettings.load_settings(filename=os.path.join(self.current_directory, 'settings.json'))
        theme_file = os.path.basename(self.settings['theme'])
        theme_file = os.path.join(self.current_directory, 'user_themes', theme_file)
        #make sure we can access the theme files 

        if 'geometry' in self.settings.keys():
            self.geometry(self.settings['geometry'])
        
        if not os.path.exists(theme_file):
            print(f"Can't find theme file: {self.settings['theme']}")
            self.settings['theme'] = 'blue'

        customtkinter.set_default_color_theme(theme_file)
        customtkinter.set_appearance_mode(mode_string=self.settings['mode'])
        font_dict=self.settings['font']
        self.custom_font = customtkinter.CTkFont(family=font_dict['family'], 
                                                 size=font_dict['size'],
                                                 weight=font_dict['weight'],
                                                 slant=font_dict['slant'],
                                                 underline=font_dict['underline'],
                                                 overstrike=font_dict['overstrike'])

        self.grid_columnconfigure(0, weight=1)
        self.demo_button_frame = customtkinter.CTkFrame(self)
        self.demo_button_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        self.demo_button_frame.grid_columnconfigure(0, weight=1)
        self.demo_button_frame.grid_rowconfigure([0, 1], weight=1)

        self.settings_button = customtkinter.CTkButton(self.demo_button_frame, text="Settings", command=self.on_settings, font=self.custom_font)
        self.settings_button.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        self.calendar_button = customtkinter.CTkButton(self.demo_button_frame, text="Calendar", command=self.on_calendar, font=self.custom_font)
        self.calendar_button.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        self.control_frame = customtkinter.CTkFrame(self)
        self.control_frame.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
        self.control_frame.grid_columnconfigure(0, weight=1)

        self.done_button = customtkinter.CTkButton(self.control_frame, text="Done", command=self.on_done, font=self.custom_font)
        self.done_button.grid(row=0, column=0, padx=10, pady=10, sticky='ew')


    def on_calendar(self):
        dialog = CTkCalendarDialog(self, title='Date Selector', font=self.custom_font, initial_date=date.today())
        CTkDialog(self, "Selected Date", f"You selected '{dialog.result}'", font=self.custom_font)

    def on_settings(self):
        dialog = CTkSettings(self, settings=self.settings, font=self.custom_font)

        if dialog.result:
            self.settings = dialog.settings
            font_dict = self.settings['font']
            customtkinter.set_appearance_mode(mode_string=self.settings['mode'])
            self.custom_font = customtkinter.CTkFont(family=font_dict['family'], 
                                                    size=font_dict['size'],
                                                    weight=font_dict['weight'],
                                                    slant=font_dict['slant'],
                                                    underline=font_dict['underline'],
                                                    overstrike=font_dict['overstrike'])
            CTkDialog(self, title='Success', message="Settings updated!", font=self.custom_font)
            self.settings['font']['family']= font_dict['family']
            self.settings['font']['size']= font_dict['size']
            self.settings['font']['weight']= font_dict['weight']
            self.settings['font']['slant']= font_dict['slant']
            self.settings['font']['underline']= font_dict['underline']
            self.settings['font']['overstrike']= font_dict['overstrike']
            CTkSettings.save_settings(filename=os.path.join(self.current_directory, 'settings.json'), settings=self.settings)
            if CTkYesNo(self, "Settings Changed", "Do you want to restart and apply them now?", font=self.custom_font).result == True:
                self.restart_app()

        else:
            CTkDialog(self, title='Failure', message="Settings were not changed!", font=self.custom_font)
        

    def on_done(self):
        self.settings['geometry'] = self.geometry()
        CTkSettings.save_settings(filename=os.path.join(self.current_directory, 'settings.json'), settings=self.settings)
        self.destroy()

if __name__=="__main__":
    app = CTkPlusDemoApp('light')
    app.title("CTkPlus Demo App")
    app.mainloop()




