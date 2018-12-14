import sys
from calendar import monthrange


year_0 = 2010
year_1 = 2019



for year in range(year_0, year_1+1):
  for month in range(1, 12):
    for day in range(1, monthrange(year, month)[1] + 1):
      print("[{year}_{month:02d}_{day:02d}](http://hemeroteca.lavanguardia.com/edition.html?edition=LVG%20Barcelona&bd={day}&bm={month}&by={year}&page=1)".format(day=day, month=month, year=year), end = "")

      for page in range(1, 11):
        print(", [{year}_{month:02d}_{day:02d}](http://hemeroteca.lavanguardia.com/edition.html?edition=LVG%20Barcelona&bd={day}&bm={month}&by={year}&page={page})".format(day=day, month=month, year=year, page=page), end = "")

      print("")
  print("")
