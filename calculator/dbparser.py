import sqlite3
from calculator.models import Food

conn = sqlite3.connect('food_database.db')
c = conn.cursor()
all_data = c.execute("SELECT * FROM food_database")

for f in all_data:
    a = Food(name=str(f[0]), protein=float(f[1]), carbs=float(f[2]), fat=float(f[3]), kcal=int(f[4]))

    print(f)