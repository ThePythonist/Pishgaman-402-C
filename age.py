def show_jalali_age(birth):
    import jdatetime
    # now = str(jdatetime.date.today()).split("-")
    # thisyear = int(now[0])
    thisyear = int(jdatetime.datetime.now().year)
    age = thisyear - birth
    print(age)


def show_gregorian(birth):
    import datetime
    thisyear = int(datetime.datetime.now().year)
    age = thisyear - birth
    print(age)
