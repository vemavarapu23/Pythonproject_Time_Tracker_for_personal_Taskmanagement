import time
from datetime import datetime
import json
import os

class simpletimetracker :
    def __init__(self):
        self.activities = {}
        self.current_activity = None
        self.start_time = None

    def start_activity(self,name):
        self.current_activity = name
        self.start_time = datetime.now()

        print(f"Started {name} at {self.start_time.strftime('%H:%M')}")

    def stop_activity(self):
        if self.current_activity:
           end_time = datetime.now()
           duration = end_time - self.start_time
           minutes = duration.total_seconds() / 60
        if self.current_activity not in self.activities:
            self.activities[self.current_activity] = []
            self.activities[self.current_activity].append({
                'start': self.start_time.strftime('%H:%M'),
                'end': end_time.strftime('%H: %M'),
                  'minutes':(minutes)
            })
            print(f"Stopped {self.current_activity}")
            print(f"Time spent: {round(minutes)} minutes")
            self.current_activity = None
            self.start_time = None
        else:
            print("No activity is running!")
            return

    def show_activities(self):
        if not self.activities:
            print("No activities recorded yet!")
            return

        print("\n--- Activity Summary ---")
        for activity, sessions in self.activities.items():
            # Calculate total time for this activity
            total_minutes = sum(session['minutes'] for session in sessions)
            print(f"\n{activity}:")
            print(f"Total time: {total_minutes} minutes")
            print("Sessions:")
            for session in sessions:
                print(f"  {session['start']} - {session['end']}: {session['minutes']} minutes")
def main():
    tracker = simpletimetracker()
    while True:
        print("\nWhat would you like to do?")
        print("1: Start activity")
        print("2: Stop activity")
        print("3: Show summary")
        print("4: Exit")

        choice = input("Choose (1-4): ")
        if choice == '1':
            name = input("Activity name: ")
            tracker.start_activity(name)
        elif choice == '2':
            tracker.stop_activity()

        elif choice == '3':
            tracker.show_activities()

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
      main()
