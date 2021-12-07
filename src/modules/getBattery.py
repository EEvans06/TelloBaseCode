from djitellopy import tello

drone = tello.Tello()
drone.connect()
battery = drone.get_battery()
print(battery)

# Battery Reminder
def baReminder():
    if battery < 80:
        print("Battery at: less than 80%")
    elif battery < 70:
        print("Battery at: less than 70%")
    elif battery < 60:
        print("Battery at: less than 60%:")
    elif battery < 50:
        print("Battery at: less than 50%")
    elif battery < 30:
        print("Battery at: less than 30%")
    elif battery < 20:
        print("Low Battery")
    elif battery < 10:
        print("Please Charge me...")
baReminder()