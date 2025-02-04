import os
import psutil
import time
import random
import secrets
import threading
import math
import numpy as np
import platform
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont
import sounddevice as sd
import wave
import matplotlib.pyplot as plt
import webbrowser
import socket
import shutil
import requests
import pyautogui
import smtplib
import pyttsx3
import urllib.request
from io import BytesIO
import sqlite3
import hashlib
import zipfile
import logging
import logging.handlers
import sqlite3
import tempfile
import mimetypes
import email
import imaplib

# ------------------- SETUP -------------------
root = tk.Tk()
root.title("Advanced Multifunctional System Utility")
root.geometry("800x600")

# ------------------- SYSTEM INFO -------------------
def get_system_info():
    system_info = f"""
    OS: {platform.system()}
    Version: {platform.version()}
    Processor: {platform.processor()}
    Python Version: {platform.python_version()}
    """
    system_label.config(text=system_info)

# ------------------- RANDOM DATA -------------------
def generate_random_data():
    rand_int = random.randint(1, 100)
    rand_float = random.uniform(1, 100)
    rand_color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    rand_hex = secrets.token_hex(8)
    random_label.config(text=f"Random Integer: {rand_int}\nRandom Float: {rand_float}\nRandom Color: {rand_color}\nRandom Hex: {rand_hex}")

# ------------------- QUOTE GENERATOR -------------------
def display_random_quote():
    quotes = [
        "The best time to plant a tree was 20 years ago. The second best time is now.",
        "Your limitation—it’s only your imagination.",
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Dream it. Wish it. Do it."
    ]
    quote = random.choice(quotes)
    quote_label.config(text=quote)

# ------------------- SYSTEM MONITOR -------------------
def system_monitor():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory().percent
    battery = psutil.sensors_battery()
    battery_percent = battery.percent if battery else "N/A"
    
    monitor_label.config(text=f"CPU Usage: {cpu_usage}%\nMemory Usage: {memory_info}%\nBattery: {battery_percent}%")

# ------------------- IMAGE MANIPULATION -------------------
def manipulate_image():
    # Create a random image with PIL
    img = Image.new('RGB', (100, 100), color=random.choice(['red', 'blue', 'green', 'yellow']))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((10, 40), "Hello!", fill="black", font=font)
    img.show()

# ------------------- PLAY SOUND -------------------
def play_sound():
    # Play a simple tone using sounddevice
    fs = 44100  # Sample rate
    seconds = 1  # Duration of sound
    t = np.linspace(0, seconds, int(fs * seconds), endpoint=False)
    signal = np.sin(2 * np.pi * 440 * t)  # 440 Hz tone (A4)
    sd.play(signal, fs)
    sd.wait()

# ------------------- FILE MANAGEMENT -------------------
def manage_files():
    file_path = "test_file.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("Hello, this is a test file!")
        file_status_label.config(text="File created: test_file.txt")
    else:
        file_status_label.config(text="File already exists.")

def delete_file():
    file_path = "test_file.txt"
    if os.path.exists(file_path):
        os.remove(file_path)
        file_status_label.config(text="File deleted successfully.")
    else:
        file_status_label.config(text="File does not exist.")

# ------------------- NETWORKING -------------------
def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        internet_status_label.config(text="Internet: Connected")
    except requests.exceptions.RequestException:
        internet_status_label.config(text="Internet: Disconnected")

def get_ip():
    ip_address = socket.gethostbyname(socket.gethostname())
    ip_label.config(text=f"IP Address: {ip_address}")

def open_website():
    webbrowser.open("https://www.google.com")

# ------------------- THREADING -------------------
def run_periodic_tasks():
    while True:
        time.sleep(5)
        generate_random_data()
        display_random_quote()
        system_monitor()

# ------------------- PLOTTING -------------------
def plot_random_data():
    data = [random.randint(1, 100) for _ in range(10)]
    plt.plot(data)
    plt.title("Random Data Plot")
    plt.show()

# ------------------- AUTOMATED TASKS -------------------
def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    messagebox.showinfo("Screenshot", "Screenshot saved as screenshot.png")

def send_email():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("your-email@gmail.com", "your-password")
        message = "Subject: Test Email\n\nThis is a test email."
        server.sendmail("your-email@gmail.com", "recipient-email@gmail.com", message)
        server.quit()
        messagebox.showinfo("Email", "Test email sent successfully!")
    except Exception as e:
        messagebox.showerror("Email", f"Failed to send email: {e}")

# ------------------- TEXT-TO-SPEECH -------------------
def text_to_speech():
    engine = pyttsx3.init()
    engine.say("Hello, welcome to the Advanced Multifunctional System Utility!")
    engine.runAndWait()

# ------------------- DATABASE -------------------
def create_database():
    conn = sqlite3.connect("example.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (name text, age integer)''')
    c.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
    conn.commit()
    conn.close()
    messagebox.showinfo("Database", "Database created and data inserted.")

# ------------------- LOGGING -------------------
def setup_logging():
    logger = logging.getLogger("my_log")
    logger.setLevel(logging.INFO)
    handler = logging.handlers.RotatingFileHandler("app.log", maxBytes=2000, backupCount=2)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("Logging started.")
    messagebox.showinfo("Logging", "Logging has been set up.")

# ------------------- FILE COMPRESSION -------------------
def compress_file():
    with zipfile.ZipFile("test.zip", "w") as zipf:
        zipf.write("test_file.txt")
    messagebox.showinfo("Compression", "File compressed into test.zip.")

# ------------------- ENCRYPTION -------------------
def encrypt_file():
    with open("test_file.txt", "rb") as f:
        file_data = f.read()
    encrypted_data = hashlib.sha256(file_data).hexdigest()
    with open("encrypted_test_file.txt", "w") as f:
        f.write(encrypted_data)
    messagebox.showinfo("Encryption", "File encrypted.")

# ------------------- TEMPORARY FILE -------------------
def create_temp_file():
    with tempfile.NamedTemporaryFile(delete=False) as tempf:
        tempf.write(b"Temporary file created.")
        temp_file_label.config(text=f"Temporary file created at: {tempf.name}")

# ------------------- UI LAYOUT -------------------
# System info label
system_label = tk.Label(root, font=("Courier", 12), anchor="w")
system_label.pack(pady=5)
get_system_info()

# Random data label
random_label = tk.Label(root, font=("Courier", 12), anchor="w")
random_label.pack(pady=5)
generate_random_data()

# Quote label
quote_label = tk.Label(root, font=("Helvetica", 14, "italic"))
quote_label.pack(pady=5)
display_random_quote()

# System monitor label
monitor_label = tk.Label(root, font=("Courier", 12), anchor="w")
monitor_label.pack(pady=5)
system_monitor()

# Buttons for actions
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

btn_image = tk.Button(buttons_frame, text="Generate Image", command=manipulate_image)
btn_image.grid(row=0, column=0, padx=10)

btn_sound = tk.Button(buttons_frame, text="Play Sound", command=play_sound)
btn_sound.grid(row=0, column=1, padx=10)

btn_file = tk.Button(buttons_frame, text="Manage File", command=manage_files)
btn_file.grid(row=1, column=0, padx=10)

btn_delete = tk.Button(buttons_frame, text="Delete File", command=delete_file)
btn_delete.grid(row=1, column=1, padx=10)

btn_internet = tk.Button(buttons_frame, text="Check Internet", command=check_internet)
btn_internet.grid(row=2, column=0, padx=10)

btn_ip = tk.Button(buttons_frame, text="Get IP Address", command=get_ip)
btn_ip.grid(row=2, column=1, padx=10)

btn_plot = tk.Button(buttons_frame, text="Plot Data", command=plot_random_data)
btn_plot.grid(row=3, column=0, padx=10)

btn_screenshot = tk.Button(buttons_frame, text="Take Screenshot", command=take_screenshot)
btn_screenshot.grid(row=3, column=1, padx=10)

btn_email = tk.Button(buttons_frame, text="Send Email", command=send_email)
btn_email.grid(row=4, column=0, padx=10)

btn_tts = tk.Button(buttons_frame, text="Text-to-Speech", command=text_to_speech)
btn_tts.grid(row=4, column=1, padx=10)

btn_db = tk.Button(buttons_frame, text="Create Database", command=create_database)
btn_db.grid(row=5, column=0, padx=10)

btn_logging = tk.Button(buttons_frame, text="Setup Logging", command=setup_logging)
btn_logging.grid(row=5, column=1, padx=10)

btn_compress = tk.Button(buttons_frame, text="Compress File", command=compress_file)
btn_compress.grid(row=6, column=0, padx=10)

btn_encrypt = tk.Button(buttons_frame, text="Encrypt File", command=encrypt_file)
btn_encrypt.grid(row=6, column=1, padx=10)

btn_temp_file = tk.Button(buttons_frame, text="Create Temp File", command=create_temp_file)
btn_temp_file.grid(row=7, column=0, padx=10)

# Status labels
file_status_label = tk.Label(root, font=("Courier", 10))
file_status_label.pack(pady=5)

internet_status_label = tk.Label(root, font=("Courier", 10))
internet_status_label.pack(pady=5)

ip_label = tk.Label(root, font=("Courier", 10))
ip_label.pack(pady=5)

temp_file_label = tk.Label(root, font=("Courier", 10))
temp_file_label.pack(pady=5)

# Run the periodic tasks in a separate thread
threading.Thread(target=run_periodic_tasks, daemon=True).start()

# Start the main loop
root.mainloop()
