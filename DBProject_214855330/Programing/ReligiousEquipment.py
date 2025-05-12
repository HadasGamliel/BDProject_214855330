import csv
import random
from faker import Faker
import pandas as pd

# יצירת אובייקט faker כדי ליצור נתונים מזויפים
fake = Faker()

# טוען נתונים קיימים עבור ShulID ו- EventID
shuls_df = pd.read_csv('Shul_data.csv')  # יש להניח שהקובץ שואל את רשומות ה- Shul
events_df = pd.read_csv('event3.csv')  # יש להניח שהקובץ שואל את רשומות ה- Events

# יצירת רשומות עבור ReligiousEquipment
num_records = 400
religious_equipment_data = []

for i in range(num_records):
    equipment_id = i + 1
    equipment_name = fake.word().capitalize() + " Equipment"
    quantity = random.randint(1, 100)
    storage_location = fake.city() + " Storage"
    shul_id = random.choice(shuls_df['ShulID'].tolist())
    event_id = random.choice(events_df['eventid'].tolist())

    religious_equipment_data.append([
        equipment_id,
        equipment_name,
        quantity,
        storage_location,
        shul_id,
        event_id
    ])

# כתיבת הנתונים לקובץ CSV
with open('religious_equipment.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['equipmentid', 'equipmentname', 'quantity', 'storagelocation', 'Shulid', 'eventid'])
    writer.writerows(religious_equipment_data)

print("CSV עבור ReligiousEquipment נוצר בהצלחה")
