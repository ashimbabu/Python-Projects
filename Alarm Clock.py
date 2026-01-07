import time
from datetime import datetime

print("===== Alarm Clock =====")

alarm_time = input("Enter alarm time (HH:MM:SS in 24-hour format): ")

print("Alarm is set...")
print("Current time will be checked every second.\n")

while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    print("Current Time:", current_time)

    if current_time == alarm_time:
        print("\n⏰ Alarm Ringing! Wake up! ⏰")
        break

    time.sleep(1)
