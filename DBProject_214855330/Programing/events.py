import pandas as pd
import random
from datetime import datetime, timedelta

# קריאה מהקבצים
shul_df = pd.read_csv('Shul_data.csv')  # ShulID, Capacity, PrayerTimes
units_df = pd.read_csv('unit.csv')  # unitid, unitname, baselocation
located_df = pd.read_csv('located_in.csv')  # UnitID, ShulID

# טווח תאריכים לאירועים
start_date = datetime.today()
event_titles = [
    "Rosh Chodesh Prayer", "Torah Lesson", "Halacha Seminar", "Lecture on IDF and Judaism",
    "Battalion Shabbaton", "Evening of Songs and Remembrance", "Megillah Reading", "Hanukkah Event",
    "Special Prayer for Soldiers", "Joint Selichot", "Lecture with Military Rabbi",
    "Melaveh Malka Meal", "Joint Study Session"
]

events = []

event_id = 1
while len(events) < 400:
    shul = shul_df.sample(1).iloc[0]
    shul_id = shul['ShulID']

    # מיקום האירוע: נחפש את היחידה שמחוברת לשול הזה ונביא ממנה את המיקום
    located_rows = located_df[located_df['ShulID'] == shul_id]
    if located_rows.empty:
        continue

    unit_id = located_rows.sample(1).iloc[0]['UnitID']
    unit_row = units_df[units_df['unitid'] == unit_id]

    if unit_row.empty:
        continue

    location = unit_row.iloc[0]['baselocation']

    event = {
        'eventid': event_id,
        'eventname': random.choice(event_titles),
        'eventdate': (start_date + timedelta(days=random.randint(1, 120))).strftime("%Y-%m-%d"),
        'Location': location,
        'Shulid': shul_id
    }

    events.append(event)
    event_id += 1

# שמירה ל־CSV
events_df = pd.DataFrame(events)
events_df.to_csv('event.csv', index=False, encoding='utf-8-sig')

print("נוצרו בהצלחה", len(events), "אירועים בקובץ event.csv")
