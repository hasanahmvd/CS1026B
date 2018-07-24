# Add statements to complete the program.

from datetime import datetime
hour = datetime.now().hour

if hour < 12 :
    timeOfDay = "morning"
elif hour >= 12 and hour < 18 :
    timeOfDay = "afternoon"
else:
    timeOfDay = "evening"

# Place your code here

print("Good {}, world".format(timeOfDay))
