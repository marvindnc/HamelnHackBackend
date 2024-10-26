import psycopg2

from models import ImageData

def connect(db_host, db_port):
    global conn;
    conn = psycopg2.connect(database="smartcomplaints",
                            host=db_host,
                            user="smartcomplaints",
                            password="password",
                            port=db_port)

def get_complaints():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM complaints")
    result = cursor.fetchall()
    return result

def get_images():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM images")
    result = cursor.fetchall()
    return result

def get_categories():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    result = cursor.fetchall()
    return result

def save_image(image_data):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO images (image, image_class, category) VALUES (%s,%s,%s)", (psycopg2.Binary(image_data.image),image_data.image_class, image_data.category))
    conn.commit()

def get_image(id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM images WHERE id = %s", (id,))
    result = cursor.fetchone()
    return result

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
    #image = open("/tmp/20241026_171143_IMG_6116.jpg", "rb").read()
    #image_data = ImageData(image=image, image_class="test", category="test")
    #save_image(image_data)
    #result = get_image(1)
    #with open("/tmp/test.jpg", 'wb') as file:
    #    file.write(result[1])