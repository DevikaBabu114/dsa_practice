"""You've devised a unique system to count days using your five fingers. Starting from a designated "Day 1", you cycle through your fingers in a specific order:ThumbIndex FingerMiddle FingerRing FingerPinky Finger
After the Pinky Finger, the count wraps around, and the next day (Day 6) is represented by the Thumb again, and so on.
Your task is to write a program that takes a day number (an integer representing the Nth day since the count began) and determines which finger corresponds to that day."""
day=int(input("enter:"))
d=["Pinky Finger","Thumb","Index Finger","Middle Finger","Ring Finger"]
print(d[day%5])