import csv
employees = [
    {"name": "John Doe", "salary": 50000},
    {"name": "Jane Smith", "salary": 60000},
    {"name": "Alice Johnson", "salary": 70000},
    {"name": "Bob Brown", "salary": 55000},
    {"name": "Emily Davis", "salary": 65000}
]
data_list = [
    ["name", "salary", "position"],
    ["Anna", "3500", "kasjerka"],
    ["Mateusz", 5000, "budowlaniec"],
    ["Weronika", 20000, "prezes"]
]

with open('salary.csv',"w",newline='') as f:
    writer = csv.writer(f,quoting = csv.QUOTE_NONNUMERIC)
    writer.writerows(data_list)


with open("salary.csv","r") as f:
    reader = csv.reader(f)
    for item in reader:
        print(reader.line_num)
        print(item)


with open("salary.csv","a") as f:
    writer = csv.writer(f)
    writer.writerow(["Maciej","15000","Programista"])

with open("salary.csv","a") as f:
    for item in ["Arkadiusz","15000","Programista"]:
        f.write(f"{item},")


