#THIS CODE IS OWNED BY NURAFNI HASHIMA BINTI SUHIB (20DDT21F1010) FROM DDT4B FOR DFP40203 PYTHON PROGRAMMING.

import tkinter as tk

class main:
    def __init__(self, master):
        self.master = master
        master.title("Automatic Username")

        # create label frame to organize the layout
        self.frame = tk.LabelFrame(master, text="Username Suggestion")
        self.frame.pack(padx=20, pady=20)

        # create entry widgets for user input
        self.entry1 = tk.Entry(self.frame)
        self.entry2 = tk.Entry(self.frame)
        self.result = tk.Entry(self.frame, state="disabled")

        # create labels for the entry widgets
        tk.Label(self.frame, text="First Name :").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.frame, text="Second Name :").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.frame, text="Suggested :").grid(row=2, column=0, padx=5, pady=5)

        # add the entry widgets to the frame
        self.entry1.grid(row=0, column=1, padx=6, pady=6)
        self.entry2.grid(row=1, column=1, padx=6, pady=6)
        self.result.grid(row=2, column=1, padx=6, pady=6)
    

        # create buttons for combine, clearing and exiting
        self.combine_button = tk.Button(self.frame, text="Combine", command=self.combine)
        self.clear_button = tk.Button(self.frame, text="Clear", command=self.clear)

        # add the buttons to the frame
        self.combine_button.grid(row=3, column=0, padx=5, pady=5)
        self.clear_button.grid(row=3, column=1, padx=5, pady=5)

        # create a separate frame for the exit button
        self.exit_frame = tk.Frame(master)
        self.exit_frame.pack()

        # create an exit button and add it to the exit frame
        self.exit_button = tk.Button(self.exit_frame, text="Exit", command=master.quit)
        self.exit_button.pack(padx=10, pady=10)


    def combine(self):
        # get the input from the entry widgets and combine them
            name1 = str(self.entry1.get())
            name2 = str(self.entry2.get())
            result = name1 + name2 + '@gmail.com'
            # enable the result entry widget and display the result
            self.result.config(state="normal")
            self.result.delete(0, tk.END)
            self.result.insert(0, str(result))
            self.result.config(state="disabled")

    def clear(self):
        # clear all entry widgets
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.result.config(state="normal")
        self.result.delete(0, tk.END)
        self.result.config(state="disabled")

root = tk.Tk()
suggested_name= main(root)
root.mainloop()
