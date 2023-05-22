import tkinter as tk

def generate_star_pattern():
    rows = int(entry.get())
    pattern = ""

    for i in range(rows):
        for j in range(i + 1):
            pattern += "* "
        pattern += "\n"

    result_label.configure(text=pattern)

window = tk.Tk()
window.title("Star Pattern")

instruction_label = tk.Label(window, text="Enter number of rows:")
instruction_label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Generate Pattern", command=generate_star_pattern)
button.pack()

result_label = tk.Label(window)
result_label.pack()

window.mainloop()
