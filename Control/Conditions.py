import datetime


class Conditions:
    
    @staticmethod
    def WeekendCondition(date):
        day = date.weekday()
        new_date = None

        if day == WeekDayEnum.SATURDAY:
            new_date = date + datetime.timedelta(2)
        elif day == WeekDayEnum.SUNDAY:
            new_date = date + datetime.timedelta(1)
        else:
            new_date = date

        return f"{new_date.day}/{new_date.month}/{new_date.year}"

    @staticmethod
    def AlwaysWednesdayCondition(date):
        due_day = date.weekday()
        next_wednesday = WeekDayEnum.WEDNESDAY - due_day

        if next_wednesday < 0:
            next_wednesday += 7

        new_date = date + datetime.timedelta(next_wednesday)

        return f"{new_date.day}/{new_date.month}/{new_date.year}"

    @staticmethod
    def AlwaysThursdayCondition(date):
        due_day = date.weekday()
        next_thursday = WeekDayEnum.THURSDAY - due_day

        if next_thursday < 0:
            next_thursday += 7

        new_date = date + datetime.timedelta(next_thursday)

        return f"{new_date.day}/{new_date.month}/{new_date.year}"

    @staticmethod
    def AlwaysFridayCondition(date):
        due_day = date.weekday()
        next_friday = WeekDayEnum.FRIDAY - due_day

        if next_friday < 0:
            next_friday += 7

        new_date = date + datetime.timedelta(next_friday)

        return f"{new_date.day}/{new_date.month}/{new_date.year}"

    @staticmethod
    def Pay10and25Condition(date):
        due_date = date.day
        new_date = None

        if due_date < 10:
            new_date = datetime.date(date.year, date.month, 10)
        elif due_date >= 10 and due_date < 25:
            new_date = datetime.date(date.year, date.month, 25)
        elif due_date >= 25 and date.month < 12:
            new_date = datetime.date(date.year, date.month + 1, 10)

        if date.month == 12 and due_date >= 25:
            new_date = datetime.date(date.year + 1, 1, 10)

        new_date = Conditions.WeekendCondition(new_date)

        return new_date

    @staticmethod
    def Pay02and15Condition(date):
        due_date = date.day
        new_date = None

        if due_date < 2:
            new_date = datetime.date(date.year, date.month, 2)
        elif due_date >= 2 and due_date < 15:
            new_date = datetime.date(date.year, date.month, 15)
        elif due_date >= 15 and date.month < 12:
            new_date = datetime.date(date.year, date.month + 1, 2)

        if date.month == 12 and due_date >= 15:
            new_date = datetime.date(date.year + 1, 1, 2)

        new_date = Conditions.WeekendCondition(new_date)

        return new_date

    @staticmethod
    def Pay10and25Condition(date):
        due_date = date.day
        new_date = None

        if due_date < 10:
            new_date = datetime.date(date.year, date.month, 10)
        elif due_date >= 10 and due_date < 25:
            new_date = datetime.date(date.year, date.month, 25)
        elif due_date >= 25 and date.month < 12:
            new_date = datetime.date(date.year, date.month + 1, 10)

        if date.month == 12 and due_date >= 15:
            new_date = datetime.date(date.year + 1, 1, 10)

        new_date = Conditions.WeekendCondition(new_date)

        return new_date

    @staticmethod
    def EveryDay06Condition(date):
        due_date = date.day
        new_date = None

        if date.month == 12:
            new_date = datetime.date(date.year + 1, 1, 6)
        else:
            new_date = datetime.date(date.year, date.month + 1, 6)

        new_date = Conditions.WeekendCondition(new_date)

        return new_date


class WeekDayEnum:
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
