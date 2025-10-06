# Friday Project 5: Customer Information Management System

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# --- 1. Database Setup ---
def setup_database():
    """
    Connects to the SQLite database and creates the 'customers' table
    if it doesn't already exist.
    """
    try:
        # Creates or connects to a database file named 'customers.db'
        conn = sqlite3.connect('customers.db')
        cursor = conn.cursor()

        # SQL command to create a table.
        # 'IF NOT EXISTS' prevents an error if the table is already there.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                birthday TEXT,
                email TEXT NOT NULL,
                phone TEXT,
                address TEXT,
                contact_method TEXT
            )
        ''')

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        print("Database setup successful.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

# --- 2. GUI Application Class ---
class CustomerApp:
    def __init__(self, root):
        """
        Initializes the main application window and its widgets.
        """
        self.root = root
        self.root.title("Customer Information Management")
        self.root.geometry("450x450") # Set a default size for the window

        # Create a main frame to hold all widgets with some padding
        main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        main_frame.pack(fill="both", expand=True)

        # --- Widget Creation ---

        # Labels and Entry fields for customer data
        ttk.Label(main_frame, text="Full Name:").grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = ttk.Entry(main_frame, width=40)
        self.name_entry.grid(row=0, column=1, pady=5)

        ttk.Label(main_frame, text="Birthday (YYYY-MM-DD):").grid(row=1, column=0, sticky="w", pady=5)
        self.birthday_entry = ttk.Entry(main_frame, width=40)
        self.birthday_entry.grid(row=1, column=1, pady=5)

        ttk.Label(main_frame, text="Email Address:").grid(row=2, column=0, sticky="w", pady=5)
        self.email_entry = ttk.Entry(main_frame, width=40)
        self.email_entry.grid(row=2, column=1, pady=5)

        ttk.Label(main_frame, text="Phone Number:").grid(row=3, column=0, sticky="w", pady=5)
        self.phone_entry = ttk.Entry(main_frame, width=40)
        self.phone_entry.grid(row=3, column=1, pady=5)

        ttk.Label(main_frame, text="Address:").grid(row=4, column=0, sticky="nw", pady=5)
        self.address_text = tk.Text(main_frame, width=30, height=5) # Using tk.Text for multi-line address
        self.address_text.grid(row=4, column=1, pady=5)

        # Dropdown menu for preferred contact method
        ttk.Label(main_frame, text="Preferred Contact:").grid(row=5, column=0, sticky="w", pady=5)
        self.contact_method_var = tk.StringVar()
        contact_options = ["Email", "Phone", "Mail"]
        self.contact_method_menu = ttk.OptionMenu(main_frame, self.contact_method_var, contact_options[0], *contact_options)
        self.contact_method_menu.grid(row=5, column=1, sticky="ew", pady=5)

        # Submit Button
        self.submit_button = ttk.Button(main_frame, text="Submit", command=self.submit_data)
        self.submit_button.grid(row=6, column=1, sticky="e", pady=20)

    def clear_form(self):
        """Clears all input fields after submission."""
        self.name_entry.delete(0, tk.END)
        self.birthday_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_text.delete("1.0", tk.END)
        self.contact_method_var.set("Email") # Reset dropdown to the first option

    def submit_data(self):
        """
        Handles data validation, database insertion, and form clearing.
        """
        # --- Retrieve data from GUI fields ---
        name = self.name_entry.get()
        birthday = self.birthday_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        # The '1.0' means 'line 1, character 0'. 'end-1c' removes the automatic newline from the Text widget.
        address = self.address_text.get("1.0", "end-1c")
        contact_method = self.contact_method_var.get()

        # --- Simple Data Validation ---
        if not name or not email:
            messagebox.showerror("Validation Error", "Name and Email fields are required.")
            return # Stop the function if validation fails

        # --- Store data in the database ---
        try:
            conn = sqlite3.connect('customers.db')
            cursor = conn.cursor()

            # The '?' are placeholders to prevent SQL injection attacks.
            cursor.execute('''
                INSERT INTO customers (name, birthday, email, phone, address, contact_method)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, birthday, email, phone, address, contact_method))

            conn.commit()
            conn.close()

            # Show a success message and clear the form
            messagebox.showinfo("Success", "Customer information submitted successfully!")
            self.clear_form()

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to insert data: {e}")

# --- 3. Main Execution Block ---
if __name__ == "__main__":
    # Ensure the database and table are ready before launching the GUI
    setup_database()

    # Create the main Tkinter window
    root = tk.Tk()

    # Create an instance of the application class
    app = CustomerApp(root)

    # Start the Tkinter event loop
    root.mainloop()