import customtkinter as ctk

# Set appearance
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Options: "blue", "green", "dark-blue"

class EmployeeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Employee Info App")
        self.geometry("400x400")

        self.num_employees = 0
        self.current_index = 0
        self.names = []
        self.ages = []

        self.create_initial_ui()

    def create_initial_ui(self):
        self.label = ctk.CTkLabel(self, text="👥 Enter number of employees:", font=ctk.CTkFont(size=16),text_color='light green')
        self.label.pack(pady=20)

        self.entry = ctk.CTkEntry(self, placeholder_text="e.g. 3")
        self.entry.pack(pady=10)

        self.submit_btn = ctk.CTkButton(self, text="Submit", command=self.set_number)
        self.submit_btn.pack(pady=10)

    def set_number(self):
        try:
            self.num_employees = int(self.entry.get())
            if self.num_employees <= 0:
                raise ValueError
            self.entry.destroy()
            self.submit_btn.destroy()
            self.ask_employee_info()
        except ValueError:
            self.label.configure(text="⚠️ Please enter a valid number!", text_color="red")

    def ask_employee_info(self):
        self.label.configure(text=f"Enter details for Employee {self.current_index + 1}:")

        self.name_entry = ctk.CTkEntry(self, placeholder_text="Name")
        self.name_entry.pack(pady=5)

        self.age_entry = ctk.CTkEntry(self, placeholder_text="Age")
        self.age_entry.pack(pady=5)

        self.next_btn = ctk.CTkButton(self, text="Next", command=self.collect_data)
        self.next_btn.pack(pady=10)

    def collect_data(self):
        name = self.name_entry.get().strip().title()
        try:
            age = int(self.age_entry.get())
            if age <= 0:
                raise ValueError
        except ValueError:
            self.label.configure(text="⚠️ Please enter a valid age!", text_color="red")
            return

        self.names.append(name)
        self.ages.append(age)

        self.name_entry.delete(0, 'end')
        self.age_entry.delete(0, 'end')

        self.current_index += 1

        if self.current_index < self.num_employees:
            self.label.configure(
                text=f"Enter details for Employee {self.current_index + 1}:",
                text_color="white"
            )
        else:
            self.name_entry.destroy()
            self.age_entry.destroy()
            self.next_btn.destroy()
            self.show_results()

    def show_results(self):
        agetotal = sum(self.ages)
        avg_age = round(agetotal / self.num_employees, 2)

        # Clear the window
        for widget in self.winfo_children():
            widget.destroy()

        # Header
        title = ctk.CTkLabel(self, text="👩‍💼 Employee Summary", font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=15)

        # Employee details frame
        details_frame = ctk.CTkScrollableFrame(self, corner_radius=10, width=460, height=220)
        details_frame.pack(pady=10)

        for i in range(self.num_employees):
            label = ctk.CTkLabel(details_frame, text=f"{i + 1}. {self.names[i]} — Age: {self.ages[i]}", anchor='w')
            label.pack(padx=10, pady=4, fill='x')

        # Stats frame
        stats_frame = ctk.CTkFrame(self, corner_radius=10)
        stats_frame.pack(pady=15, padx=20, fill='x')

        stats_title = ctk.CTkLabel(stats_frame, text="📊 Statistics", font=ctk.CTkFont(size=16, weight="bold"))
        stats_title.pack(pady=(10, 5))

        stat_texts = [
            f"Total Employees: {self.num_employees}",
            f"Total Combined Age: {agetotal}",
            f"Average Age: {avg_age}"
        ]
        for stat in stat_texts:
            label = ctk.CTkLabel(stats_frame, text=stat)
            label.pack(pady=3)

        # Restart button (optional)
        restart_btn = ctk.CTkButton(self, text="🔁 Start Over", command=self.restart_app)
        restart_btn.pack(pady=15)

    def restart_app(self):
        self.num_employees = 0
        self.current_index = 0
        self.names.clear()
        self.ages.clear()

        for widget in self.winfo_children():
            widget.destroy()

        self.create_initial_ui()

# Run the app
if __name__ == "__main__":
    app = EmployeeApp()
    app.mainloop()
