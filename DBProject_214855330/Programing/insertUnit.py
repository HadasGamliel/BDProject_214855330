import random

unit_names = [
    "Military Rabbinate HQ", "IDF Kashrut Supervision Unit", "Burial and Memorial Unit", "Halachic Response Unit", "Religious Advisory Unit", "Field Rabbinate - Northern Command", "Field Rabbinate - Central Command", "Field Rabbinate - Southern Command", "Field Rabbinate - Home Front Command", "Field Rabbinate - Air Force", "Field Rabbinate - Navy", "Chaplaincy Support Unit", "Military Conversion Center", "Jewish Identity Development Branch", "Shabbat Observance Supervision Team" ]


base_locations = [
    "Tel Aviv", "Jerusalem", "Haifa", "Beer Sheva", "Eilat",
    "Ashdod", "Tzfat", "Netanya", "Petah Tikva", "Ariel"
]

output_file = "insert_units.sql"

with open(output_file, "w", encoding="utf-8") as file:
    for unit_id in range(1, 401):
        name = random.choice(unit_names) + f" {unit_id}"
        location = random.choice(base_locations)
        sql = f"INSERT INTO Units (UnitID, UnitName, BaseLocation) VALUES ({unit_id}, '{name}', '{location}');\n"
        file.write(sql)

print(f"✅ 400 INSERT statements for Units saved to {output_file}")
