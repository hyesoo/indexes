import sys
from calendar import monthrange


year_0 = 2010
year_1 = 2019


print("""
<html>
  <head>
    <title>La vanguardia</title>
  </head>
  <body>
""")

for year in range(year_0, year_1+1):
  print("""
    <div>
      <h1>{year}</h1><pre>""".format(year=year))

  for month in range(1, 12):
    print("""<h2>{month:02d}</h2>""".format(month=month), end = "")

    for day in range(1, monthrange(year, month)[1] + 1):
      print("""<a href="http://hemeroteca.lavanguardia.com/edition.html?edition=LVG%20Barcelona&bd={day}&bm={month}&by={year}&page=1">{year}/{month:02d}/<strong>{day:02d} page 1</strong></a>""".format(day=day, month=month, year=year), end = "")

      for page in range(1, 11):
        print(""", <a href="http://hemeroteca.lavanguardia.com/edition.html?edition=LVG%20Barcelona&bd={day}&bm={month}&by={year}&page={page}">{page}</a>""".format(day=day, month=month, year=year, page=page), end = "")

      print("")

  print("</pre></div>")
  print("")

print("""
  </body>
</html>
""")
