# CTkDialog.py
import customtkinter

class CTkDialog(customtkinter.CTkToplevel):
    def __init__(self, parent, title=None, message=None, font=None):
        super().__init__(parent)
        self.transient(parent)

        if title:
            self.title(title)

        if message:
            customtkinter.CTkLabel(self, text=message, font=font).pack(padx=10, pady=10)

        button = customtkinter.CTkButton(self, text="OK", command=self.destroy, font=font)
        button.pack(pady=10)
        
        # Center the dialog over parent
        #self.geometry("+%d+%d" % (parent.winfo_rootx() + 300, parent.winfo_rooty() + 200))
        #self.geometry("+%d+%d" % (parent.winfo_rootx() + parent.winfo_width()/2, parent.winfo_rooty() + parent.winfo_height()/2))
        self.center_on_parent(parent)        

        
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.grab_set()
        self.wait_window(self)

    def center_on_parent(self, parent):
        # Calculate position to center the dialog over the main application window
        parent_x = parent.winfo_x()
        parent_y = parent.winfo_y()
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()

        dialog_width = self.winfo_reqwidth()
        dialog_height = self.winfo_reqheight()

        position_x = parent_x + (parent_width / 2) - (dialog_width / 2)
        position_y = parent_y + (parent_height / 2) - (dialog_height / 2)

        # Set position
        self.geometry("+%d+%d" % (position_x, position_y))
