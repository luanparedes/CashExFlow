import datetime

from Helpers.WeekDayEnum import WeekDayEnum


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

        return Conditions.formated_date(new_date)

    @staticmethod
    def AlwaysWednesdayCondition(date):
        due_day = date.weekday()
        next_wednesday = WeekDayEnum.WEDNESDAY - due_day

        if next_wednesday < 0:
            next_wednesday += 7

        new_date = date + datetime.timedelta(next_wednesday)

        return Conditions.formated_date(new_date)

    @staticmethod
    def AlwaysThursdayCondition(date):
        due_day = date.weekday()
        next_thursday = WeekDayEnum.THURSDAY - due_day

        if next_thursday < 0:
            next_thursday += 7

        new_date = date + datetime.timedelta(next_thursday)

        return Conditions.formated_date(new_date)

    @staticmethod
    def AlwaysFridayCondition(date):
        due_day = date.weekday()
        next_friday = WeekDayEnum.FRIDAY - due_day

        if next_friday < 0:
            next_friday += 7

        new_date = date + datetime.timedelta(next_friday)

        return Conditions.formated_date(new_date)

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
    def EveryDay06Condition(date):
        due_date = date.day
        new_date = None

        if date.month == 12:
            new_date = datetime.date(date.year + 1, 1, 6)
        else:
            new_date = datetime.date(date.year, date.month + 1, 6)

        new_date = Conditions.WeekendCondition(new_date)

        return new_date

    @staticmethod
    def AlwaysMondayAndWednesdayCondition(date):
        due_day = date.weekday()
        next_monday = WeekDayEnum.MONDAY - due_day
        next_wednesday = WeekDayEnum.WEDNESDAY - due_day

        if next_wednesday < 0:
            next_wednesday += 7

        if next_monday < 0:
            next_monday += 7

        if next_monday < next_wednesday:
            new_date = date + datetime.timedelta(next_monday)
        else:
            new_date = date + datetime.timedelta(next_wednesday)

        return Conditions.formated_date(new_date)

    @staticmethod
    def formated_date(time):
        year = time.strftime("%Y")
        month = time.strftime("%m")
        day = time.strftime("%d")

        return f"{day}/{month}/{year}"
