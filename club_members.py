# club_members.py

# Define students as tuples
students = [
    ("Alice", 20),
    ("Bob", 21),
    ("Charlie", 19),
    ("David", 22),
    ("Eve", 20)
]

# Create two sets representing different clubs
club_sports = {students[0], students[1], students[2]}
club_arts = {students[2], students[3], students[4]}

# List all members of each club
print("Sports Club Members:")
for member in club_sports:
    print(member)

print("\nArts Club Members:")
for member in club_arts:
    print(member)

# Find common members
common_members = club_sports & club_arts
print("\nCommon Members:")
for member in common_members:
    print(member)

# Find members unique to each club
unique_sports = club_sports - club_arts
unique_arts = club_arts - club_sports

print("\nMembers unique to Sports Club:")
for member in unique_sports:
    print(member)

print("\nMembers unique to Arts Club:")
for member in unique_arts:
    print(member)
