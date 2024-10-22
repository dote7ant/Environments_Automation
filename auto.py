import customtkinter as ctk
import subprocess
import sys
import os
import threading
from tkinter import filedialog
import time


# define the packages for each category default
data_science_packages = ['numpy', 'pandas', 'scipy', 'scikit-learn', 'matplotlib', 'seaborn']
flask_packages = ['flask', 'flask-sqlalchemy', 'flask-migrate', 'flask-wtf']
django_packages = ['django', 'djangorestframework', 'psycopg2']
scripting_packages = ['requests', 'beautifulsoup4', 'openpyxl', 'pdfplumber']

class EnvSetupApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Python Environment Setup")
        self.geometry("650x650")
        
        # configure grid layout
        self.grid_columnconfigure(0, weight=1)
        
        # create main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        # title
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="Python Environment Setup",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 30), sticky="ew")

        # category Selection
        self.category_label = ctk.CTkLabel(self.main_frame, text="Select Environment Category:")
        self.category_label.grid(row=1, column=0, padx=20, pady=(10, 5), sticky="w")
        
        self.category_var = ctk.StringVar(value="Data_Science")
        self.category_menu = ctk.CTkOptionMenu(
            self.main_frame,
            values=["Data_Science", "Flask", "Django", "Scripting"],
            variable=self.category_var
        )
        self.category_menu.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="ew")

        # custom Name Checkbox and Entry
        self.custom_name_var = ctk.BooleanVar(value=False)
        self.custom_name_checkbox = ctk.CTkCheckBox(
            self.main_frame,
            text="Custom Environment Name",
            variable=self.custom_name_var,
            command=self.toggle_name_entry
        )
        self.custom_name_checkbox.grid(row=3, column=0, padx=20, pady=(10, 5), sticky="w")
        
        # environment Name (initially hidden)
        self.name_frame = ctk.CTkFrame(self.main_frame)
        self.name_frame.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="ew")
        self.name_frame.grid_columnconfigure(0, weight=1)
        self.name_frame.grid_remove()  

        self.name_entry = ctk.CTkEntry(self.name_frame, placeholder_text="Enter environment name")
        self.name_entry.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        # requirements File Checkbox and Selection
        self.req_var = ctk.BooleanVar(value=False)
        self.req_checkbox = ctk.CTkCheckBox(
            self.main_frame,
            text="Use requirements.txt",
            variable=self.req_var,
            command=self.toggle_requirements
        )
        self.req_checkbox.grid(row=5, column=0, padx=20, pady=(10, 5), sticky="w")
        
        # requirements File Selection (initially hidden)
        self.req_frame = ctk.CTkFrame(self.main_frame)
        self.req_frame.grid(row=6, column=0, padx=20, pady=(0, 20), sticky="ew")
        self.req_frame.grid_columnconfigure(0, weight=1)
        self.req_frame.grid_remove()  
        
        self.req_entry = ctk.CTkEntry(self.req_frame, placeholder_text="Path to requirements.txt")
        self.req_entry.grid(row=0, column=0, padx=(20, 10), pady=10, sticky="ew")
        
        self.req_button = ctk.CTkButton(
            self.req_frame, 
            text="Browse",
            width=100,
            command=self.browse_requirements
        )
        self.req_button.grid(row=0, column=1, padx=(0, 20), pady=10)

        # directory Selection
        self.dir_label = ctk.CTkLabel(self.main_frame, text="Environment Location:")
        self.dir_label.grid(row=7, column=0, padx=20, pady=(10, 5), sticky="w")
        
        self.dir_frame = ctk.CTkFrame(self.main_frame)
        self.dir_frame.grid(row=8, column=0, padx=20, pady=(0, 20), sticky="ew")
        self.dir_frame.grid_columnconfigure(0, weight=1)
        
        self.dir_entry = ctk.CTkEntry(self.dir_frame, placeholder_text="Select directory")
        self.dir_entry.grid(row=0, column=0, padx=(20, 10), pady=10, sticky="ew")
        
        self.dir_button = ctk.CTkButton(
            self.dir_frame,
            text="Browse",
            width=100,
            command=self.browse_directory
        )
        self.dir_button.grid(row=0, column=1, padx=(0, 20), pady=10)

        # create Environment Button
        self.create_button = ctk.CTkButton(
            self.main_frame,
            text="Create Environment",
            command=self.start_creation,
            height=40
        )
        self.create_button.grid(row=9, column=0, padx=20, pady=(20, 10), sticky="ew")

        # progress Bar and Status
        self.progress_label = ctk.CTkLabel(self.main_frame, text="")
        self.progress_label.grid(row=10, column=0, padx=20, pady=(10, 5), sticky="w")
        
        self.progress_bar = ctk.CTkProgressBar(self.main_frame)
        self.progress_bar.grid(row=11, column=0, padx=20, pady=(0, 20), sticky="ew")
        self.progress_bar.configure(progress_color="white", fg_color="grey")
        self.progress_bar.set(0)

    def toggle_name_entry(self):
        if self.custom_name_var.get():
            self.name_frame.grid()
        else:
            self.name_frame.grid_remove()

    def toggle_requirements(self):
        if self.req_var.get():
            self.req_frame.grid()
        else:
            self.req_frame.grid_remove()

    def browse_requirements(self):
        filename = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filename:
            self.req_entry.delete(0, 'end')
            self.req_entry.insert(0, filename)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.dir_entry.delete(0, 'end')
            self.dir_entry.insert(0, directory)

    def create_environment(self):
        try:
            # get environment name based on checkbox
            if self.custom_name_var.get():
                env_name = self.name_entry.get()
                if not env_name:
                    self.update_status("Please enter an environment name", "red")
                    return
            else:
                env_name = f"{self.category_var.get()}-env"

            env_dir = self.dir_entry.get()
            if not env_dir:
                self.update_status("Please select a directory", "red")
                return

            env_path = os.path.join(env_dir, env_name)
            
            # update status
            self.update_status(f"Creating virtual environment: {env_name}")
            self.progress_bar.set(0.2)
            
            # Create virtual environment
            subprocess.run([sys.executable, "-m", "venv", env_path], check=True)
            self.progress_bar.set(0.4)

            # Determine packages to install
            if self.req_var.get():
                requirements_file = self.req_entry.get()
                if not requirements_file:
                    self.update_status("Please select a requirements.txt file", "red")
                    return
                with open(requirements_file, 'r') as f:
                    packages = [line.strip() for line in f.readlines() if line.strip()]
            else:
                if self.category_var.get() == "Data_Science":
                    packages = data_science_packages
                elif self.category_var.get() == "Flask":
                    packages = flask_packages
                elif self.category_var.get() == "Django":
                    packages = django_packages
                else:
                    packages = scripting_packages

            # install packages
            pip_path = os.path.join(env_path, "Scripts" if sys.platform.startswith('win') else "bin", "pip")
            
            progress_increment = 0.5 / len(packages)
            current_progress = 0.4

            for package in packages:
                self.update_status(f"Installing {package}...")
                subprocess.run([pip_path, "install", package], check=True)
                current_progress += progress_increment
                self.progress_bar.set(current_progress)

            self.progress_bar.set(1.0)
            self.update_status("Environment created successfully!", "white")
            
        except Exception as e:
            self.update_status(f"Error: {str(e)}", "red")
            self.progress_bar.set(0)

        finally:
            self.create_button.configure(state="normal")

    def update_status(self, message, color="white"):
        self.progress_label.configure(text=message, text_color=color)

    def start_creation(self):
        self.create_button.configure(state="disabled")
        threading.Thread(target=self.create_environment, daemon=True).start()

if __name__ == "__main__":
    # set appearance mode and default color theme
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("themes/violet.json")
    
    app = EnvSetupApp()
    app.mainloop()