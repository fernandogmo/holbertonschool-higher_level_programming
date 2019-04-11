#!/usr/bin/python3
"""Lists all the cities of a particular state from `hbtn_0e_4_usa` database."""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    target_state = (argv[4], )

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cursor = db.cursor()
    cursor.execute(("SELECT cities.id, cities.name "
                    "FROM states JOIN cities "
                    "ON states.id = cities.state_id "
                    "WHERE states.name = %s "
                    "ORDER BY cities.id ASC"), target_state)
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()
