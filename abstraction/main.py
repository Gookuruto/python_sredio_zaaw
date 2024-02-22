import caluclator_abs


calulators = caluclator_abs.get_calulators()

for cal in calulators:
    print(cal.add())
    cal.wypisz()