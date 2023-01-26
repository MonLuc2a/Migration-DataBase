import sqlite3

print("\nWelcome to the database migration tool ! (^_^) \n")

# Choose the database name
db_name = input("Enter the name of the database: ")

# Connect to the database
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Open and read the file as a single buffer
with open('new-database.sql', 'r') as f:
    sqlFile = f.read()

# Execute the SQL commands
cursor.executescript(sqlFile)

# Close the connection
conn.close()

# Connect to the old and new databases
old_conn = sqlite3.connect('tpb2.db')
new_conn = sqlite3.connect(db_name)

# Create a cursor for each connection
old_cursor = old_conn.cursor()
new_cursor = new_conn.cursor()

# Select all the rows from the old 'game' table
old_cursor.execute('SELECT * FROM game')
data = old_cursor.fetchall()

# Insert the data into the new 'game' table
new_cursor.executemany('INSERT INTO game VALUES (?,?)', data)

# Select all the rows from the old 'tournament' table
old_cursor.execute('SELECT * FROM tournament')

# Iterate through each row in the old 'tournament' table
for row in old_cursor.fetchall():
    # Extract the values from the row
    idTournament = row[0]
    date = row[1]
    placeName = row[2]
    address = row[3]
    city = row[4]
    duration = row[5]
    IdGame = row[6]

    # Insert the 'placeName', 'address', and 'city' values into the new 'place' table
    new_cursor.execute('INSERT OR IGNORE INTO place (Name, Address, City) VALUES (?, ?, ?)', (placeName, address, city))

    # Get the new 'IdPlace' value
    new_cursor.execute('SELECT IdPlace FROM place WHERE Name=? AND Address=? AND City=?', (placeName, address, city))
    IdPlace = new_cursor.fetchone()[0]

    # Insert the remaining values into the new 'tournament' table
    new_cursor.execute('INSERT INTO tournament ( idPlace, IdGame, date, duration) VALUES ( ?, ?, ?, ?)', (IdPlace, IdGame, date, duration))


# Select all the rows from the old 'coach' table
old_cursor.execute('SELECT * FROM coach')

# Iterate through each row in the old 'coach' table
for row in old_cursor.fetchall():
    # Extract the values from the row
    idCoach = row[0]
    lastname = row[1]
    firstname = row[2]
    Gender = row[3]
    Age = row[4]
    Wage = row[5]
    LicenseDate = row[6]
    idGame = row[7]

    # Insert the values into the new 'employeeData' table
    new_cursor.execute('INSERT INTO employee_Data (IdEmployee, LastName, FirstName, Gender, Age, Wage) VALUES (?, ?, ?, ?, ?, ?)', (idCoach, lastname, firstname, Gender, Age, Wage))

    idEmployeeData = new_cursor.lastrowid
    # Insert the values into the new 'coach' table
    new_cursor.execute('INSERT INTO coach ( IdGame, LicenseDate, idEmployeeData) VALUES ( ?, ?, ?)', ( idGame, LicenseDate, idEmployeeData))

# Select all the rows from the old 'player' table
old_cursor.execute('SELECT * FROM player')

for row in new_cursor.fetchall():
    idEmployeeData = row[0]
# Iterate through each row in the old 'player' table
for row in old_cursor.fetchall():
    # Extract the values from the row
    idPlayer = row[0]
    lastname = row[1]
    firstname = row[2]
    Gender = row[3]
    Age = row[4]
    Wage = row[5]
    Ranking = row[6]
    idGame = row[7]

    # Insert the values into the new 'employeeData' table
    new_cursor.execute('INSERT INTO employee_Data (lastName, firstName, gender, age, wage) VALUES ( ?, ?, ?, ?, ?)', (lastname, firstname, Gender, Age, Wage))

    idEmployeeData = new_cursor.lastrowid
    # Insert the values into the new 'coach' table
    new_cursor.execute('INSERT INTO player (IdGame, Ranking, idEmployeeData) VALUES (?, ?, ?)', ( idGame, Ranking, idEmployeeData))

old_cursor.execute('SELECT * FROM staff')

for row in new_cursor.fetchall():
    idEmployeeData = row[0]
# Iterate through each row in the old 'staff' table
for row in old_cursor.fetchall():
    # Extract the values from the row
    idStaff = row[0]
    lastname = row[1]
    firstname = row[2]
    Gender = row[3]
    Age = row[4]
    Wage = row[5]

    # Insert the values into the new 'employeeData' table
    new_cursor.execute('INSERT INTO employee_Data (lastName, firstName, Gender, Age, Wage) VALUES ( ?, ?, ?, ?, ?)', (lastname, firstname, Gender, Age, Wage))

    # Add the idEmployeeData from the employeeData table to the staff table on the IdEmployeeData column
    idEmployeeData = new_cursor.lastrowid

    # Insert the values into the new 'coach' table
    new_cursor.execute('INSERT INTO staff (idStaff, idEmployeeData) VALUES (?, ?)', (idStaff, idEmployeeData))

# Commit the changes to the new database
new_conn.commit()


# Close the connections
old_conn.close()
new_conn.close()

print("\nMigration complete !")