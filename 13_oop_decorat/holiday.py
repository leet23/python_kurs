import holidays, datetime
pl_holidays = holidays.Polish()
today = datetime.date.today()
print(today, 'zajęcia się odbywają:', Student.academic_day(today))

saturday = datetime.datetime.strptime('2019-06-22', '%Y-%m-%d')
print(saturday, 'zajęcia się odbywają:', Student.academic_day(saturday))

sunday = datetime.date.today() - datetime.timedelta(days=1)
print(sunday, 'zajęcia się odbywają:', Student.academic_day(sunday))