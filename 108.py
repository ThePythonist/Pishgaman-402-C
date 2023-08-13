def show_gregorian(birth):
    import datetime
    thisyear = int(datetime.datetime.now().year)
    age = thisyear - birth
    print(age)

show_gregorian(2006)
