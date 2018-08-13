'''
Created on Aug 10, 2018

@author: marcelo
'''
import sqlite3, json
from _pickle import dump


conn = sqlite3.connect('exercise3.sqlite')
cursor = conn.cursor()

def createDataBase():
    cursor.executescript('''
        DROP TABLE IF EXISTS User;
        DROP TABLE IF EXISTS Member;
        DROP TABLE IF EXISTS Course;
        
        CREATE TABLE User (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name   TEXT UNIQUE
        );
        
        CREATE TABLE Course (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            title  TEXT UNIQUE
        );
        
        CREATE TABLE Member (
            user_id     INTEGER,
            course_id   INTEGER,
            role        INTEGER,
            PRIMARY KEY (user_id, course_id)
        )
        ''')

file = open('roster_data.json').read()
jsonContent = json.loads(file)

print(json.dumps(jsonContent,indent=3))

print('Lenght:', len(jsonContent))
if len(jsonContent) < 1: 
    print('File is empt') 
    quit()

createDataBase()
for item in jsonContent:    
    name = item[0]
    title = item[1]
    role = item[2]
    
    cursor.execute('''INSERT OR IGNORE INTO Course (title)
    VALUES ( ? )''', ( title, ) )
    cursor.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    courseid = cursor.fetchone()[0]
    
    cursor.execute('INSERT OR IGNORE INTO USER (name) VALUES (?)', (name,))    
    cursor.execute('SELECT id FROM USER where name = ? ', (name,))
    userid = cursor.fetchone()[0]
       
    cursor.execute('INSERT OR IGNORE INTO member (user_id, course_id, role) VALUES (?,?,?)', (userid, courseid, role))
    
conn.commit()

cursor.close()
# start in 14:23
# finished in 15:27