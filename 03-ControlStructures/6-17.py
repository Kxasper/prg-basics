#nie mam pojęcia jak to zrobić
czas = input("Enter time (24-hour format hh:mm): ")  # np. 16:32

godziny = int(czas[0:2])
minuty = czas[3:5]

if godziny >= 12:
      pora = "pm"
else:
      pora = "am"

godziny_12 = godziny % 12
if godziny_12 == 0:
      godziny_12 = 12

print(f"Time in 12-hour format: {godziny_12}:{minuty}{pora}")