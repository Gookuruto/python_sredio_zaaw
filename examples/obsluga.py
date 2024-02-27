try:
    x = 10/0
except ValueError as e:
    print("mam wyjatek")
    print(e)
finally:
    print("Zawsze sie wykonam")


print("program dziala dalej.")