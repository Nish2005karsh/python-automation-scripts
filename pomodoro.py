import time
def timer(minutes):
    print(f"⏳ Focus for {minutes} minutes!")
    time.sleep(minutes * 60)
    print("✅ Time’s up!")
timer(25)
timer(5)
