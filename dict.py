symbol_to_name = {
    "H": "Hydrogen",
    "He": "Helium",
    "Li": "Lithium",
    "C": "Carbon",
    "O": "Oxygen",
    "N": "Nitrogen"
}

print(symbol_to_name)
print(symbol_to_name.keys())
print(symbol_to_name.values())
print(symbol_to_name.items())

symbol_to_name.update({"Ni": "Nickel"})

print(symbol_to_name)

del symbol_to_name["Li"]
print(symbol_to_name)

print(symbol_to_name["He"])

print(sorted(symbol_to_name.items()))
print(sorted(symbol_to_name.values()))
print(sorted(symbol_to_name.keys()))



for k,v in symbol_to_name.items():
    print("key is %s and value is %s" %(k,v))

if "He" in symbol_to_name:
    print(symbol_to_name["He"])
else:
    print("Key doesn't exist")