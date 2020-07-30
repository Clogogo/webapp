import mysql.connector

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"

)
cursor = con.cursor()

word = input("Enter a word: ").strip()
query = cursor.execute("SELECT * from Dictionary where Expression = '%s'" % word)
results = cursor.fetchall()

if len(results) > 0:
    for arrange in results:
        print(arrange)
else:
    print("The Word was not Found")
