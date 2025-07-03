import random

# Define parts of the address
street_names = [
    "King Fahd Road", "Prince Sultan Street", "Abu Bakr Al Siddiq Road",
    "Tahlia Street", "King Abdulaziz Road", "Imam Saud Bin Abdulaziz Road",
    "Palestine Street", "King Saud Road", "King Abdullah Road",
    "Prince Mohammed Bin Fahd Street", "King Faisal Road", "Sari Street",
    "Omar Bin Abdulaziz Road", "Madinah Road", "Dhahran Street",
    "Anas Bin Malik Road", "Hira Street", "King Salman Road",
    "Dammam Road", "Al Imam Al Shafi'i Street"
]

districts = [
    "Al Olaya", "Al Rawdah", "Al Malaz", "Al Zahra", "Al Khobar Al Janubiyah",
    "Al Yasmin", "Al Rehab", "Al Ulaya", "Al Naseem", "Al Aqrabiyah",
    "Al Rawabi", "Al Bawadi", "Al Mugharrazat", "Al Safa", "Al Rakah Ash Shamaliyah",
    "Al Narjis", "Al Marwah", "Al Muruj", "Al Faisaliyah", "Al Manar"
]

cities_regions = [
    ("Riyadh", "Riyadh Region"),
    ("Jeddah", "Makkah Region"),
    ("Al Khobar", "Eastern Region"),
    ("Dhahran", "Eastern Region"),
    ("Dammam", "Eastern Region")
]

# Generate 100 addresses
addresses = []
for _ in range(100):
    number = random.randint(1000, 9999)
    street = random.choice(street_names)
    district = random.choice(districts)
    city, region = random.choice(cities_regions)
    address = f"{number}, {street}  {district} district, {city}, {region}"
    addresses.append(address)

addresses[:10]  # Display the first 10 for preview
