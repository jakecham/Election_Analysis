counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

print('---------------------------')

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

print('---------------------------')

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

print('---------------------------')

if "Arapahoe" in counties and "El Paso" not in counties:
    print("only Arapahoe is in the list of coutnies.")
else:
    print("Arapahoe is in the list of counties and El Pasi is not in the list of counties.")
