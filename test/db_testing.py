from flask import Flask
from flask_mysqldb import MySQL
import os

app=Flask(__name__)

mysql=MySQL(app)

app.config['MYSQL_HOST']=os.environ['MYSQLHOST']
app.config['MYSQL_USER']=os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD']=os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB']=os.environ['MYSQLDB']

######################################################################################################################################################################
#########################################################################     CRUD TESTS     #########################################################################
######################################################################################################################################################################


def test_select():                                               #select test
    with app.app_context():
        cur= mysql.connection.cursor()
        num_of_records=cur.execute('SELECT * FROM Films')    #test made on the table that's not used for CRUD 
        mysql.connection.commit()
        cur.close()
        assert 28 == num_of_records                             #checks if the number of records in the database matches the number of entries expected to have in the table

def test_insert():                                              #insert test
    with app.app_context():
        cur= mysql.connection.cursor()
        cur.execute('SELECT * FROM Actors')                   #tests made on the table used for CRUD
        num_of_records=cur.fetchall()
        cur.execute('INSERT INTO Actors (Actor_Name) VALUES ("z-test")')  #inserts at an autoincrement ID the value 'test'
        mysql.connection.commit()
        cur.execute('SELECT * FROM Actors')
        new_num_records=cur.fetchall()
        cur.close()
    assert num_of_records[len(num_of_records)-1] != new_num_records[len(new_num_records)-1]


    
def test_delete():                                              #delete test
    with app.app_context():
        cur= mysql.connection.cursor()
        cur.execute('SELECT * FROM Actors')                   #tests made on the table used for CRUD
        num_of_records=cur.fetchall()
        cur.execute('DELETE FROM Actors WHERE Actor_ID= %s', [int(num_of_records[len(num_of_records)-1][0])])  #delete all entries in the table that have the name 'test'
        mysql.connection.commit()
        cur.execute('SELECT * FROM Actors')
        new_num_records=cur.fetchall()
        cur.close()
    assert num_of_records[len(num_of_records)-1][0] != new_num_records[len(new_num_records)-1][0]

def test_update():                                              #delete test
    with app.app_context():
        cur= mysql.connection.cursor()
        cur.execute('SELECT * FROM Actors')                   #tests made on the table used for CRUD
        num_of_records=cur.fetchall()
        cur.execute("UPDATE Actors SET Actor_Name=(%s) WHERE Actor_ID=(%s)", ['test', int(num_of_records[len(num_of_records)-1][0])])  #inserts at an autoincrement ID the value 'test'
        mysql.connection.commit()
        cur.execute('SELECT * FROM Actors')
        new_num_records=cur.fetchall()
        cur.close()
    assert num_of_records[len(num_of_records)-1] != new_num_records[len(new_num_records)-1]


#####################################################################################################################################################################
########################################################################     TABLE TESTS     ########################################################################
#####################################################################################################################################################################

def test_empty():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT concat('DROP TABLE IF EXISTS `', table_name, '`;') FROM information_schema.tables WHERE table_schema = 'SFIA1';")
        drops = cur.fetchall()
        mysql.connection.commit()
        cur.execute("SET FOREIGN_KEY_CHECKS = 0")
        mysql.connection.commit()
        for drop in drops:
            cur.execute(drop[0])
            mysql.connection.commit()
        cur.execute("SET FOREIGN_KEY_CHECKS = 1")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        empty = len(cur.fetchall())+1
        mysql.connection.commit()
        cur.close()
        assert empty

def test_create_actors():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DROP TABLE IF EXISTS Actors;")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        start = len(cur.fetchall())
        mysql.connection.commit()
        cur.execute("CREATE TABLE Actors (Actor_ID INT(3) AUTO_INCREMENT NOT NULL PRIMARY KEY, Actor_Name VARCHAR(50) UNIQUE NOT NULL);")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        end = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert abs(start - end) == 1

def test_actors_coherence():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DESCRIBE Actors;")
        col = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert col == 2

def test_create_films():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DROP TABLE IF EXISTS Films;")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        start = len(cur.fetchall())
        mysql.connection.commit()
        cur.execute("CREATE TABLE Films (Film_ID INT(3) AUTO_INCREMENT NOT NULL PRIMARY KEY, Film_Name VARCHAR(50) UNIQUE NOT NULL);")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        end = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert abs(start - end) == 1


def test_films_coherence():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DESCRIBE Films;")
        col = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert col == 2

def test_create_film_actor():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DROP TABLE IF EXISTS Film_Actor;")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        start = len(cur.fetchall())
        mysql.connection.commit()
        cur.execute("CREATE TABLE Film_Actor (FilmID INT(3), ActorID INT(3), FOREIGN KEY(FilmID) REFERENCES Films (Film_ID) ON DELETE CASCADE, FOREIGN KEY(ActorID) REFERENCES Actors(Actor_ID) ON DELETE CASCADE);")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        end = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert abs(start - end) == 1

def test_recipe_ingredients_coherence():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DESCRIBE Film_Actor;")
        col = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert col == 2