"""
Task 4: Tech Conference Registration
The Jos Tech Conference registered participants under ticket categories:

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}

During the first day:
- A "Guest" participant named "Daisy" joined.
- The "Student" participant canceled their registration.
- The organizers created a record for the day before removing the most recently added participant from the live system.
"""

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}
new_participants = {"Guest": "Daisy"}
participants.update(new_participants)
print(participants)
participants.pop("Student")
print(participants)
participants.pop("Guest")
print(participants)


# print(participants_snapshot)
# print(participants)
