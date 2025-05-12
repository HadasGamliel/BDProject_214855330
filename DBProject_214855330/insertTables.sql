-- טבלת Units
INSERT INTO Units (UnitID, UnitName, BaseLocation) VALUES 
(1, 'מדור הלכה', 'בסיס צריפין'),
(2, 'מדור כשרות', 'בסיס מחנה רבין'),
(3, 'מדור תורה', 'בסיס תל השומר');

-- טבלת Shul
INSERT INTO Shul (ShulID, Capacity, PrayerTimes) VALUES 
(101, 120, 'שחרית: 07:00, מנחה: 13:00, ערבית: 19:00'),
(102, 80, 'שחרית: 06:45, מנחה: 12:45, ערבית: 18:30'),
(103, 100, 'שחרית: 07:15, מנחה: 13:15, ערבית: 19:15');

-- טבלת located_in
INSERT INTO located_in (UnitID, ShulID) VALUES 
(1, 101),
(2, 102),
(3, 103);

-- טבלת Soldiers
INSERT INTO Soldiers (SoldierID, FirstName, LastName, Rank, Role, ShulID) VALUES 
(1001, 'יוסי', 'כהן', 'סמל ראשון', 'רב מדור הלכה', 101),
(1002, 'אורי', 'לוי', 'רב סמל', 'משגיח כשרות', 102),
(1003, 'דוד', 'ישראלי', 'רב סרן', 'ראש מדור תורה', 103);

-- טבלת Events
INSERT INTO Events (EventID, EventName, EventDate, Location, SoldierID, ShulID) VALUES 
(201, 'תפילת יום כיפור', DATE '2024-10-12', 'בית כנסת צריפין', 1001, 101),
(202, 'שיעור תורה שבועי', DATE '2024-05-01', 'בית כנסת מחנה רבין', 1002, 102),
(203, 'הרצאה הלכתית לחנוכה', DATE '2024-12-05', 'בית כנסת תל השומר', 1003, 103);

-- טבלת ReligiousEquipment
INSERT INTO ReligiousEquipment (EquipmentID, EquipmentName, Quantity, StorageLocation, ShulID, EventID) VALUES 
(301, 'סידורים', 50, 'מחסן צריפין', 101, 201),
(302, 'תפילין', 10, 'מחסן מחנה רבין', 102, 202),
(303, 'ספרי תורה', 2, 'כספת תל השומר', 103, 203);

-- טבלת HalachicGuidelines
INSERT INTO HalachicGuidelines (GuidelineID, Title, Description, DateIssued, SoldierID) VALUES 
(401, 'כשרות בשטח', 'הנחיות להכשרת ציוד בשטח', DATE '2024-03-15', 1002),
(402, 'תפילה בזמן פעילות מבצעית', 'הקלות בתפילה לאור אילוצי בט"ש', DATE '2024-02-10', 1001),
(403, 'שמירת שבת בבסיס', 'עקרונות בסיסיים לשמירת שבת במתקנים צבאיים', DATE '2024-04-01', 1003);
