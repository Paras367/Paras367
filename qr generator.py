import qrcode
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")

        self.label = ttk.Label(root, text="Enter text or select an option:")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(root, width=40)
        self.entry.pack(pady=10)

        options = ["Text", "URL", "Phone Number", "Email"]
        self.option_var = tk.StringVar()
        self.option_var.set(options[0])

        self.option_menu = ttk.OptionMenu(root, self.option_var, *options)
        self.option_menu.pack(pady=10)

        self.generate_button = ttk.Button(root, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=10)

        self.qr_label = ttk.Label(root)
        self.qr_label.pack(pady=10)

    def generate_qr_code(self):
        # Get the selected option and input text
        option = self.option_var.get()
        data = self.entry.get()

        # Generate QR code based on the selected option
        if option == "Text":
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')

        elif option == "URL":
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')

        elif option == "Phone Number":
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(f"tel:{data}")
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')

        elif option == "Email":
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(f"mailto:{data}")
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')

        # Convert PIL image to Tkinter PhotoImage and display
        img = img.resize((250, 250))
        img_tk = ImageTk.PhotoImage(img)
        self.qr_label.config(image=img_tk)
        self.qr_label.image = img_tk

        # Save QR code image based on option
        if option == "Text":
            img.save("qrcode_text.png")
        elif option == "URL":
            img.save("qrcode_url.png")
        elif option == "Phone Number":
            img.save("qrcode_phone.png")
        elif option == "Email":
            img.save("qrcode_email.png")

        # Show success message
        messagebox.showinfo("QR Code Generated", "QR Code generated successfully!")

# Main function to run the application
def main():
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
