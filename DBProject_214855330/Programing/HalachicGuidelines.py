import csv
import random
from faker import Faker
import pandas as pd

# יצירת אובייקט faker כדי ליצור נתונים מזויפים
fake = Faker()

# טוען נתונים קיימים עבור SoldierID
soldiers_df = pd.read_csv('soldiers_data.csv')  # יש להניח שהקובץ שואל את רשומות ה- Soldiers

# יצירת רשומות עבור HalachicGuidelines
num_records = 400
halachic_guidelines_data = []

for i in range(num_records):
    guideline_id = i + 1
    title = fake.sentence(nb_words=3)
    description = fake.text(max_nb_chars=500)
    date_issued = fake.date_this_decade()
    soldier_id = random.choice(soldiers_df['SoldierID'].tolist())
    
    halachic_guidelines_data.append([
        guideline_id, 
        title, 
        description, 
        date_issued, 
        soldier_id
    ])

# כתיבת הנתונים לקובץ CSV
with open('halachic_guidelines.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['guidelineid', 'title', 'description', 'dateissued', 'soldierid'])
    writer.writerows(halachic_guidelines_data)

print("CSV עבור HalachicGuidelines נוצר בהצלחה")
