#!/usr/bin/python3
"""Lists all the cities from `hbtn_0e_4_usa` database."""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities JOIN states "
                   "ON states.id = cities.state_id "
                   "ORDER BY cities.id ASC")
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()
