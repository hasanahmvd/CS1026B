# Replace the placeholders with code and run the Python program

episode4 = {"Luke","Leia","Han","Chewie","C3PO","R2-D2","Vader","Greedo","Kenobi"}
episode5={"Luke","Leia","Han","Chewie","C3PO","R2-D2","Vader","Tauntaun","Yoda","Lando"}
episode6={"Luke","Leia","Han","Chewie","C3PO","R2-D2","Vader","Palpatine","Ackbar","Jabba","Rancor","Boba","Yoda"}

# Code to create intersection
interEp45 = episode4.intersection(episode5)

# Code to compute the difference between episode 6 and the intersection of 4 and 5
final = episode6.difference(interEp45)

print(final)
