import tkinter as tk
from tkinter import ttk
import sqlite3

def view_customers():
    """
    Connects to the database and fetches all customer records.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('customers.db')
        cursor = conn.cursor()

        # Execute query to select all data from the 'customers' table
        # IMPORTANT: Replace 'customers' if your table has a different name.
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()

        # Get column names from the cursor description
        # This makes the code adaptable if your table columns change.
        column_names = [description[0] for description in cursor.description]

        return column_names, rows

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return [], []
    finally:
        if conn:
            conn.close()

def main():
    """
    Creates the main GUI window to display the customer data.
    """
    window = tk.Tk()
    window.title("Customer Database Viewer")
    window.geometry("800x500") # Set a default size for the window

    # Create a frame to hold the treeview and scrollbar
    frame = ttk.Frame(window, padding="10")
    frame.pack(expand=True, fill='both')

    # Fetch the data from the database
    columns, customer_data = view_customers()

    if not columns:
        # Display an error message if no columns were found (e.g., table doesn't exist)
        error_label = ttk.Label(frame, text="Could not load data. Ensure 'customers.db' exists and contains a 'customers' table.", font=("Arial", 12))
        error_label.pack(pady=20)
        window.mainloop()
        return

    # Create the Treeview widget (the table)
    tree = ttk.Treeview(frame, columns=columns, show='headings')

    # --- Set up the table headings ---
    for col in columns:
        tree.heading(col, text=col.capitalize()) # Makes the column titles capitalized
        tree.column(col, width=100, anchor='center') # Adjust width and alignment as needed

    # --- Insert the data into the table ---
    for row in customer_data:
        tree.insert("", tk.END, values=row)

    # --- Add a vertical scrollbar ---
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    
    # Place the treeview and scrollbar in the frame using grid layout
    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar.grid(row=0, column=1, sticky='ns')

    # Configure the grid to allow the treeview to expand
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Start the GUI event loop
    window.mainloop()

# Run the main function when the script is executed
if __name__ == "__main__":
    main()