import psycopg2

from import_functions import import_clubs

def connect():
    global conn;
    conn = psycopg2.connect(database="football",
                            host="localhost",
                            user="football",
                            password="football",
                            port="15432")

def print_table():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clubs")
    results = cursor.fetchall()
    for result in results:
        print(result)

def search_club_by_name(name):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clubs WHERE name LIKE %(name)s", { 'name': '%{}%'.format(name)})
    result = cursor.fetchone()
    return result

def disconnect():
    conn.commit()
    conn.close()

if __name__ == '__main__':
    connect()
    print_table()
    print(search_club_by_name('1.'))
    disconnect()