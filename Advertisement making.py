import os
import tkinter as tk
from tkinter import messagebox

class AdGenerator:
    def generate_text_ad(self, course_name, discount, website):
        ad_text = (
            f"Learn Professional Programming with {course_name}!\n"
            f"Enroll now and get {discount}% off.\n"
            f"Visit: {website}"
        )
        return ad_text

def generate_ad():
    course_name = entry_course_name.get()
    discount = entry_discount.get()
    website = entry_website.get()
    
    if not course_name or not discount or not website:
        messagebox.showerror("Input Error", "All fields are required!")
        return
    
    try:
        discount = int(discount)
    except ValueError:
        messagebox.showerror("Input Error", "Discount must be a number!")
        return

    generator = AdGenerator()
    text_ad = generator.generate_text_ad(course_name, discount, website)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, text_ad)

    # Save the text ad to a file
    if not os.path.exists('ads'):
        os.makedirs('ads')
    with open('ads/ad_text.txt', 'w') as file:
        file.write(text_ad)

    messagebox.showinfo("Success", "Advertisement generated and saved to ads/ad_text.txt")

# Set up the main application window
root = tk.Tk()
root.title("Advertisement Generator")

# Create and place labels and entry widgets for inputs
tk.Label(root, text="Course Name:").grid(row=0, column=0, padx=10, pady=5)
entry_course_name = tk.Entry(root)
entry_course_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Discount (%):").grid(row=1, column=0, padx=10, pady=5)
entry_discount = tk.Entry(root)
entry_discount.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Website:").grid(row=2, column=0, padx=10, pady=5)
entry_website = tk.Entry(root)
entry_website.grid(row=2, column=1, padx=10, pady=5)

# Create and place a button to generate the advertisement
btn_generate = tk.Button(root, text="Generate Advertisement", command=generate_ad)
btn_generate.grid(row=3, columnspan=2, padx=10, pady=10)

# Create a text widget to display the generated advertisement
text_output = tk.Text(root, width=50, height=10)
text_output.grid(row=4, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
