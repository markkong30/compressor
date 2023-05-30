import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess


def compress_files():
    # Ask the user for a password using a GUI input dialog
    password = tk.simpledialog.askstring(
        "Password", "Enter a password for the ZIP file:", show="*"
    )

    if password:
        files = filedialog.askopenfiles()
        if files:
            # Get the directory path of the first selected file
            directory_path = os.path.dirname(files[0].name)

            # Get the base name of the first selected file
            base_name = os.path.basename(files[0].name)

            # Remove the file extension from the base name
            file_name = os.path.splitext(base_name)[0]

            # Compose the output file name
            output_file_name = os.path.join(directory_path, f"{file_name}.zip")

            # Check if the output zip already exists and create a unique name
            index = 1
            while os.path.exists(output_file_name):
                output_file_name = os.path.join(
                    directory_path, f"{file_name}_{index}.zip"
                )
                index += 1

            # Compress the files using the zip command-line tool with password
            subprocess.call(
                ["zip", "-j", "-P", password, output_file_name]
                + [file.name for file in files]
            )

            # Show a message box with the completion message
            message = f"Files compressed successfully!\nOutput: {output_file_name}"
            messagebox.showinfo("Compression Completed", message)
            close_button.pack(pady=10)

    else:
        messagebox.showwarning(
            "No Password Entered", "No password was entered. Compression aborted."
        )


# Create the tkinter window
window = tk.Tk()
window.title("File Compressor")
window.geometry("300x150")

# Create a button to trigger the file selection and compression
button = tk.Button(window, text="Select Files", command=compress_files)
button.pack(pady=10)

close_button = tk.Button(window, text="Close", command=window.destroy)

# Start the tkinter event loop
window.mainloop()
