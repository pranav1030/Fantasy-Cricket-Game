import sqlite3
conn_obj=sqlite3.connect("Players.db")
cursor_obj=conn_obj.cursor()

cursor_obj.execute('''CREATE TABLE match(
Player TEXT NOT NULL,
Scored INTEGER,
Faced INTEGER,
Fours INTEGER,
Sixes INTEGER,
Bowled INTEGER,
Maiden INTEGER,
Given INTEGER,
Wkts INTEGER,
Catches INTEGER,
Stumping INTEGER,
RO INTEGER);''')

l_o_t_m=(['Kholi', '102', '98', '8', '2', '0', '0', '0', '0', '0', '0', '1'],
['Yuvraj', '12', '20', '1', '0', '48', '0', '36', '1', '0', '0', '0'],
['Rahane', '49', '75', '3', '0', '0', '0', '0', '0', '1', '0', '0'],
['Dhavan', '32', '35', '4', '0', '0', '0', '0', '0', '0', '0', '0'],
['Dhoni', '56', '45', '3', '1', '0', '0', '0', '0', '3', '2', '0'],
['Axar', '8', '4', '2', '0', '48', '2', '35', '1', '0', '0', '0'],
['Panday', '42', '36', '3', '3', '30', '0', '25', '0', '1', '0', '0'],
['Jadeja', '18', '10', '1', '1', '60', '3', '50', '2', '1', '0', '1'],
['Kedar', ' 65', ' 60', ' 7', ' 0', ' 24', ' 0', ' 24', ' 0', ' 0', ' 0', ' 0'],
['Ashwin', '23', '42', '3', '0', '60', '0', '45', '6', '0', '0', '0'],
['Umesh', '0', '0', '0', '0', '54', '0', '50', '4', '1', '0', '0'],
['Bumrah', '0', '0', '0', '0', '60', '2', '49', '1', '0', '0', '0'],
['Bhuvaneshwar', '15', '12', '2', '0', '60', '1', '46', '2', '0', '0', '0'],
['Rohit', '46', '65', '5', '1', '0', '0', '0', '0', '1', '0', '0'],
['kartick', '29', '42', '3', '0', '0', '0', '0', '0', '2', '0', '1'])

try:
    for a in l_o_t_m:
        cursor_obj.execute('''INSERT INTO match(Player,Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wkts,Catches,Stumping,RO)
         VALUES (?,?,?,?,?,?,?,?,?,?,?,?);''',(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11]))
        conn_obj.commit()
    print("records succesfully addded in matches table")

except:
    print("Error in matches table")
    conn_obj.rollback()


cursor_obj.execute('''CREATE TABLE stats(
Player PRIMARY KEY,
Matches INTEGER,
Runs INTEGER,
Hundreds INTEGER,
Fifties INTEGER,
Value INTEGER,
Ctg TEXT NOT NULL);
''')

l_o_t_s=(['Kholi', '189', '8257', '28', '43', '120', 'BAT'],
['Yuvraj', '86', '3589', '10', '21', '100', 'BAT'],
['Rahane', '158', '5435', '11', '31', '100', 'BAT'],
['Dhavan', '25', '565', '2', '1', '85', 'AR'],
['Dhoni', '78', '2753', '3', '19', '75', 'BAT'],
['Axar', '67', '208', '0', '0', '100', 'BWL'],
['Panday', '70', '77', '0', '0', '75', 'BWL'],
['Jadeja', '16', '1', '0', '0', '85', 'BWL'],
['Kedar', '111', '675', '0', '1', '90', 'BWL'],
['Ashwin', '136', '1914', '0', '10', '100', 'AR'],
['Umesh', '296', '9496', '10', '64', '110', 'WK'],
['Bumrah', '73', '1365', '0', '8', '60', 'WK'],
['Bhuvaneshwar', '17', '289', '0', '2', '75', 'AR'],
['Rohit', '304', '8701', '14', '52', '85', 'BAT'],
['kartick', '11', '111', '0', '0', '75', 'AR'])

try:
    for b in l_o_t_s:
        cursor_obj.execute('''INSERT INTO stats (Player,Matches,Runs,Hundreds,Fifties,Value,Ctg)
         VALUES (?,?,?,?,?,?,?);''',(b[0],b[1],b[2],b[3],b[4],b[5],b[6]))
        conn_obj.commit()
    print('records added successfully in stats table')

except:
    print("error in stats table")
    conn_obj.rollback()

cursor_obj.execute('''CREATE TABLE teams(
Name TEXT NOT NULL,
Players TEXT NOT NULL,
Value INTEGER NOT NULL);''')

conn_obj.close()
