# Customer Information Management System

This project is a desktop application built with Python for entering, storing, and viewing customer information. It uses the `tkinter` library for its graphical user interface (GUI) and `sqlite3` for database management.

---

## File Breakdown

This repository contains three key files that work together to create the application.

### `FP5 Main.py`

This script is the **primary entry point** for the application, responsible for data entry.

* **Purpose**: To provide a user-friendly form for adding new customer records to the database.
* **Key Features**:
    * **Database Initialization**: On startup, the `setup_database` function checks if the `customers.db` file and the `customers` table exist. If not, it creates them automatically, preventing errors on the first run.
    * **Graphical User Interface**: It creates a window titled "Customer Information Management" with clearly labeled fields for Full Name, Birthday, Email, Phone Number, and Address. It also includes a dropdown menu for selecting a preferred contact method.
    * **Data Validation**: Before saving, the script checks to ensure that the **"Full Name"** and **"Email Address"** fields are not left empty. If they are, it displays an error message.
    * **Secure Database Insertion**: When data is submitted, it uses a parameterized SQL `INSERT` query. This method securely passes data to the database, which is a best practice to prevent SQL injection attacks.
    * **User Feedback**: After a successful submission, a confirmation pop-up appears, and the form is automatically cleared for the next entry.

### `readDatabase.py`

This script is a **read-only utility** for viewing the stored data.

* **Purpose**: To display all records from the `customers` table in a clear, easy-to-read format.
* **Key Features**:
    * **Data Retrieval**: It connects to the `customers.db` file and executes a `SELECT * FROM customers` query to fetch every record.
    * **Dynamic Table Generation**: The script intelligently reads the column names directly from the database schema. This means if you add a new column to your database table, this viewer will automatically include it without any code changes.
    * **Tabular Display**: It uses a `tkinter.ttk.Treeview` widget to present the data in a structured table, making it easy to browse multiple customer entries.
    * **Scrollable View**: A vertical scrollbar is included, ensuring all records are accessible even if the list is too long to fit in the window.

### `customers.db`

This is the **SQLite database file** that acts as the central storage for the application. 🗂️

* **Purpose**: To persistently store all customer information entered through `FP5 Main.py`.
* **Technology**: It is a lightweight, serverless, single-file database powered by SQLite 3.
* **Schema**: The database contains a single table named `customers` with the following columns:
    * `id`: An integer that serves as the unique primary key for each record. It auto-increments for every new entry.
    * `name`: A non-optional text field for the customer's full name.
    * `birthday`: A text field for the customer's birthday.
    * `email`: A non-optional text field for the customer's email.
    * `phone`: A text field for the customer's phone number.
    * `address`: A text field for the customer's address.
    * `contact_method`: A text field storing the preferred contact method.

---

## How to Use the Application

1.  **Ensure all three files** (`FP5 Main.py`, `readDatabase.py`, and `customers.db`) are located in the same folder.
2.  **To add a new customer**, execute `FP5 Main.py` from your terminal. This will open the data entry form.
    ```bash
    python "FP5 Main.py"
    ```
3.  **To view all saved customers**, execute `readDatabase.py`. This will launch the viewer window.
    ```bash
    python readDatabase.py
    ```