import csv
import random

# קריאה לקובץ ה-CSV של Units
with open('unit.csv', mode='r', newline='', encoding='utf-8') as unit_file:
    unit_reader = csv.DictReader(unit_file)
    units = list(unit_reader)

# קריאה לקובץ ה-CSV של Shul
with open('shul_data.csv', mode='r', newline='', encoding='utf-8') as shul_file:
    shul_reader = csv.DictReader(shul_file)
    shuls = list(shul_reader)

# יצירת קובץ CSV חדש ל-located_in
with open('located_in.csv', mode='w', newline='', encoding='utf-8') as located_in_file:
    fieldnames = ['UnitID', 'ShulID']
    writer = csv.DictWriter(located_in_file, fieldnames=fieldnames)

    # כתיבת כותרות לקובץ
    writer.writeheader()

    # יצירת 400 רשומות אקראיות
    for _ in range(400):
        unit = random.choice(units)
        shul = random.choice(shuls)

        # כתיבת רשומה אקראית לקובץ
        writer.writerow({
            'UnitID': unit['unitid'],
            'ShulID': shul['ShulID']
        })

print("הקובץ located_in.csv נוצר בהצלחה.")
