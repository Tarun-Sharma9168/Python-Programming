import datetime
def time_for_milk_and_cookies(date):
      #Chritmas Eve is on December 24th not November 24th'
  return (date.day==24 and date.month==11)
print(time_for_milk_and_cookies(datetime.date(2012,12,24)))