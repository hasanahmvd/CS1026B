month = (raw_input("Please enter the current month: "))

if month == "January" or month == "December" or month =="February" :
    print("In {}, it is winter, I suggest you go snowboarding".format(month))
elif month == "March" or month == "April" or month =="May" :
    print("In {}, it is spring, I suggest you go hiking".format(month))
elif month == "June" or month == "July" or month =="August" :
    print("In {}, it is summer, I suggest you go swimming".format(month))
elif month == "September" or month == "October" or month =="November" :
    print("In {}, it is autumn, I suggest you go biking".format(month))

