from pushbullet import Pushbullet
import random
import time

PUSHBULLET_API_KEY = "o.NCYYPzeFVfhLIRk1SB6BS5SXZlsPdmNP"
pb = Pushbullet(PUSHBULLET_API_KEY)
def read_sensor_data():
    temperature = round(random.uniform(20.0, 45.0), 2)  
    return temperature
def send_notification(title, message):
    try:
        push = pb.push_note(title, message)
        print(f"Notification sent: {title} - {message}")
    except Exception as e:
        print(f"Failed to send notification: {e}")
def monitor_temperature(threshold=35.0):
    try:
        while True:
            temperature = read_sensor_data()
            print(f"Current Temperature: {temperature}°C")
            if temperature > threshold:
                title = "Temperature Alert!"
                message = f"Temperature has exceeded the threshold! Current Temperature:{temperature}°C"
                send_notification(title, message)
                time.sleep(5) 
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
monitor_temperature()
