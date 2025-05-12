import pandas as pd
import random

# מאגר של שמות יהודיים פרטיים ושמות משפחה
first_names = ['Aharon', 'Moshe', 'David', 'Yosef', 'Shlomo', 'Itamar', 'Yitzhak', 'Dov', 'Avraham', 'Yaakov', 'Eli', 'Tzvi', 'Shimon', 'Chaim', 'Meir', 'Reuven', 'Daniel', 'Benjamin', 'Eliyahu', 'Yehuda']
last_names = ['Cohen', 'Levi', 'Mizrachi', 'Peretz', 'Shalom', 'Friedman', 'Rosenberg', 'Goldstein', 'Klein', 'Ben-David', 'Shapiro', 'Baruch', 'Ben-Avraham', 'Grossman', 'Weiss', 'Katz', 'Greenberg', 'Shulman', 'Halevi', 'Erez']

# קריאת נתוני ה-shul_data.csv
shul_data = pd.read_csv("shul_data.csv")

# מספר הרשומות שאנחנו רוצים ליצור
num_soldiers = 400

# רשימה שתאחסן את רשומות ה-soldiers
soldiers = []

# יצירת רשומות עבור Soldiers
for i in range(num_soldiers):
    soldier_id = i + 1  # נניח שה-SoldierID מתחיל מ-1
    first_name = random.choice(first_names)  # בוחר שם פרטי אקראי מתוך המאגר
    last_name = random.choice(last_names)  # בוחר שם משפחה אקראי מתוך המאגר
    rank = random.choice(['Private', 'Sergeant', 'Lieutenant', 'Captain', 'Major'])  # דרגות אקראיות
    role = random.choice(['Commander', 'Technician', 'Instructor', 'Medic', 'Support'])  # תפקידים אקראיים
    shul_id = random.choice(shul_data['ShulID'].tolist())  # בחירת שדה שול אקראי מתוך נתוני Shul

    # הוספת רשומה ל-list
    soldiers.append([soldier_id, first_name, last_name, rank, role, shul_id])

# יצירת DataFrame מ-List של Soldiers
soldiers_df = pd.DataFrame(soldiers, columns=['SoldierID', 'FirstName', 'LastName', 'Rank', 'Role', 'ShulID'])

# שמירת הנתונים לקובץ CSV חדש
soldiers_df.to_csv('soldiers_data.csv', index=False)

print("קובץ soldiers_data.csv נוצר בהצלחה עם 400 רשומות.")
