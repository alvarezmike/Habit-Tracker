import webbrowser
from tkinter import messagebox, END
import requests
from datetime import datetime
import customtkinter
import tkinter
from tkcalendar import Calendar
import config


# constants
pixela_endpoint = "https://pixe.la/v1/users"
TODAY = datetime.now()
headers = {
    "X-USER-TOKEN": config.TOKEN

}

# -------------------------------------------------------------------------------------
# functions


def open_browser():
    """Open my pixela progress on web browser"""
    webbrowser.open(config.URL, new=1)


def format_date():
    """format date in a way that I can pass the input into pixela """
    cal.config(date_pattern="yyyyMMdd")
    date = cal.get_date()
    cal.config(date_pattern="dd/MM/yyyy")
    return date


def add_pixel():
    """Add entry to my pixela graph"""
    endpoint = f"https://pixe.la/v1/users/{config.USERNAME}/graphs/{config.ID}/"
    pixel_add = {
        "date": format_date(),
        "quantity": entry.get(),
    }
    requests.post(url=endpoint, json=pixel_add, headers=headers)
    entry.delete(0, END)
    messagebox.showinfo(message="Pixel added.")


def del_pixel():
    """Delete a pixel from the graph"""
    endpoint = f"https://pixe.la/v1/users/{config.USERNAME}/graphs/{config.ID}/{format_date()}"
    requests.delete(url=endpoint, headers=headers)
    messagebox.showinfo(message="Pixel deleted.")


def change_pixel():
    """Update a pixel from the graph"""
    endpoint = f"https://pixe.la/v1/users/{config.USERNAME}/graphs/{config.ID}/{format_date()}"
    pixel_update = {
        "quantity": entry.get(),
    }
    requests.put(url=endpoint, json=pixel_update, headers=headers)
    entry.delete(0, END)
    messagebox.showinfo(message="Pixel updated.")


# -------------------------------------------------------------------------------------
root_tk = tkinter.Tk()  # create the Tk window
root_tk.geometry("450x350")
root_tk.title("Coding Habit Tracker")
root_tk.resizable(width=False, height=False)


def button_function():
    """Function to test buttons"""
    print("button pressed")


# entry for # of hours coding
entry = customtkinter.CTkEntry(master=root_tk,
                               placeholder_text="Input:Number of hours",
                               width=160,
                               height=25,
                               border_width=2,
                               corner_radius=10)
entry.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

# calendar
cal = Calendar(root_tk, selectmode="day", year=TODAY.year, month=TODAY.month, day=TODAY.day)
cal.pack()


# Button to open web-browser and show progress
progress_btn = customtkinter.CTkButton(master=root_tk, text="View Progress", corner_radius=10, command=open_browser)
progress_btn.place(relx=0.5, rely=0.95, anchor=tkinter.CENTER)

# crud buttons
add_btn = customtkinter.CTkButton(master=root_tk, text="Add", corner_radius=5, command=add_pixel)
add_btn.place(relx=0.15, rely=0.65, anchor=tkinter.CENTER)

update_btn = customtkinter.CTkButton(master=root_tk, text="Update", corner_radius=5, command=change_pixel)
update_btn.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)

delete = customtkinter.CTkButton(master=root_tk, text="Delete", corner_radius=5, command=del_pixel)
delete.place(relx=0.85, rely=0.65, anchor=tkinter.CENTER)

root_tk.mainloop()
