import tkinter as tk
from tkinter import scrolledtext
import random
import cv2
import numpy as np

# Sample chatbot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just a program, but I'm doing well!", "I'm fine, thank you! How about you?"],
    "your name": ["I'm ChatBot!", "You can call me ChatBot!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "who made you": ["I was created by Paras Dhiman!", "Paras Dhiman made me!"],
    "default": ["I'm not sure I understand that.", "Can you rephrase?", "I'm here to help, ask me anything!"]
}

# Chatbot response function
def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# GUI Application
class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Chatbot with Live Face Recognition")
        
        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", height=20, width=50)
        self.chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # Entry widget
        self.entry = tk.Entry(root, width=40)
        self.entry.grid(row=1, column=0, padx=10, pady=10)
        self.entry.bind("<Return>", self.send_message)
        
        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)
        
        # Face recognition button
        self.recognition_button = tk.Button(root, text="Turn On Face Recognition", command=self.start_face_recognition)
        self.recognition_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    
    def send_message(self, event=None):
        user_input = self.entry.get()
        if user_input.strip():
            self.display_message("You: " + user_input)
            self.entry.delete(0, tk.END)
            
            # Get chatbot response
            response = chatbot_response(user_input)
            self.display_message("Bot: " + response)
    
    def display_message(self, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state="disabled")
        self.chat_area.see(tk.END)
    
    def start_face_recognition(self):
        self.display_message("Bot: Starting face recognition...")
        train_and_recognize_face()

# Face Recognition with Live Training
def train_and_recognize_face():
    # Initialize face recognizer and cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Capture video
    cap = cv2.VideoCapture(0)

    print("Collecting training data. Look at the camera...")
    training_data = []
    labels = []
    sample_count = 0
    max_samples = 50  # Number of samples for training

    # Collect training data
    while sample_count < max_samples:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

        for (x, y, w, h) in faces:
            sample_count += 1
            face_roi = gray[y:y+h, x:x+w]
            training_data.append(face_roi)
            labels.append(1)  # Label for your face
            
            # Display the captured frame with a rectangle
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"Capturing ({sample_count}/{max_samples})", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("Training Mode", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if len(training_data) > 0:
        # Train recognizer
        recognizer.train(training_data, np.array(labels))
        print("Training complete. Starting recognition mode...")

        # Start recognition mode
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame.")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

            for (x, y, w, h) in faces:
                face_roi = gray[y:y+h, x:x+w]
                label, confidence = recognizer.predict(face_roi)
                
                # Recognize face
                if label == 1 and confidence < 50:  # Adjust threshold if necessary
                    cv2.putText(frame, "Paras Dhiman", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
                else:
                    cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)

            cv2.imshow("Recognition Mode", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
    else:
        print("No training data collected. Exiting.")

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
