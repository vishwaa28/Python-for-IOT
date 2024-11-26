from flask import Flask, render_template, redirect, url_for, send_file
import sqlite3
import cv2
import numpy as np
from datetime import datetime
import os

app = Flask(__name__)
DATABASE = 'iot_images.db'
IMAGE_FOLDER = 'static/images/'

# Initialize SQLite database
def initialize_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            image_path TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Capture image from default camera and save to file
def capture_image():
    cap = cv2.VideoCapture(0)  # 0 is the default camera
    ret, frame = cap.read()
    cap.release()
    
    if ret:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        image_filename = f'image_{timestamp}.jpg'
        image_path = os.path.join(IMAGE_FOLDER, image_filename)
        
        # Save image to static folder
        cv2.imwrite(image_path, frame)
        return image_path
    else:
        print("Failed to capture image")
        return None
    
    


# Save image record to database
def save_image_to_db(image_path):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO Images (timestamp, image_path) VALUES (?, ?)", (timestamp, image_path))
    conn.commit()
    conn.close()

# Retrieve all images from database
def retrieve_images_from_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Images where id>9")
    records = cursor.fetchall()
    conn.close()
    return records

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['GET', 'POST'])
def capture():
    image_path = capture_image()
    if image_path:
        save_image_to_db(image_path)
        return render_template('capture.html', image_path=image_path)
    else:
        return "Failed to capture image"

@app.route('/view')
def view():
    images = retrieve_images_from_db()
    return render_template('view.html', images=images)

if __name__ == '__main__':
    initialize_database()
    if not os.path.exists(IMAGE_FOLDER):
        os.makedirs(IMAGE_FOLDER)
    app.run(debug=True)
