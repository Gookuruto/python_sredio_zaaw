import json

# with open("data.pickle", "r+") as f:
#     content = f.readline()
#     f.write("Ale fajny napis\n")
#     f.seek(0, 0)
#     content_2 = f.read()
#
# print(content)
# print(content_2)

kuranci = [{"name": "Julia"}, {"name": "Cezar"}]

napis = json.dumps(kuranci,indent=2)
print(json.loads(napis))
