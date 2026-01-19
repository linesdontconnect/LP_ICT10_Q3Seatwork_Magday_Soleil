import tkinter as tk
from tkinter import ttk, messagebox

# Teams dictionary
teams = {
    "7 TOPAZ": "Green Hornets",
    "7 RUBY": "Blue Bears",
    "7 SAPPHIRE": "Red Bulldogs",
    "7 EMERALD": "Yellow Tigers",
    "8 TOPAZ": "Blue Bears",
    "8 RUBY": "Red Bulldogs",
    "8 SAPPHIRE": "Green Hornets",
    "8 EMERALD": "Yellow Tigers",
    "9 TOPAZ": "Yellow Tigers",
    "9 RUBY": "Green Hornets",
    "9 SAPPHIRE": "Blue Bears",
    "9 EMERALD": "Red Bulldogs",
    "10 TOPAZ": "Blue Bears",
    "10 RUBY": "Red Bulldogs",
    "10 SAPPHIRE": "Yellow Tigers",
    "10 EMERALD": "Green Hornets"
}

def check_eligibility():
    registered = reg_var.get()
    medical = med_var.get()
    grade_section = grade_var.get()

    if registered == "No":
        result_label.config(text="You cannot join. Please register online first.", fg="red")
    elif medical == "No":
        result_label.config(text="You cannot join. Please secure a medical clearance.", fg="red")
    else:
        team = teams.get(grade_section, None)
        if team:
            result_label.config(
                text=f"Congratulations! You are eligible to join.\nYour Intramurals team is: {team}",
                fg="green"
            )
        else:
            result_label.config(text="Invalid grade/section selected.", fg="red")

# GUI setup
root = tk.Tk()
root.title("Intramurals Eligibility Checker")

tk.Label(root, text="Registered Online?").grid(row=0, column=0, sticky="w")
reg_var = tk.StringVar(value="Yes")
ttk.Combobox(root, textvariable=reg_var, values=["Yes", "No"], state="readonly").grid(row=0, column=1)

tk.Label(root, text="Medical Clearance?").grid(row=1, column=0, sticky="w")
med_var = tk.StringVar(value="Yes")
ttk.Combobox(root, textvariable=med_var, values=["Yes", "No"], state="readonly").grid(row=1, column=1)

tk.Label(root, text="Grade Level & Section:").grid(row=2, column=0, sticky="w")
grade_var = tk.StringVar(value="7 TOPAZ")
grade_options = list(teams.keys())
ttk.Combobox(root, textvariable=grade_var, values=grade_options, state="readonly").grid(row=2, column=1)

tk.Button(root, text="Check Eligibility", command=check_eligibility).grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()