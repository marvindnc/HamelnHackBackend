import psycopg2

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

def save_complaint(complaint):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO complaints (description, capture_time, image, image_class, category) VALUES (%s, %s, %s, %s, %s) RETURNING id", 
                   (complaint.description, complaint.capture_time, psycopg2.Binary(complaint.image), complaint.image_class, complaint.category))
    id = cursor.fetchone()[0]
    conn.commit()
    return id
    

def get_complaint(id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM complaints WHERE id = %s", (id, ))
    result = cursor.fetchone()
    return result

def get_categories():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    result = cursor.fetchall()
    return result

def get_category(id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories WHERE id = %s", (id,))
    result = cursor.fetchone()
    return result

def get_image(id):
    cursor = conn.cursor()
    cursor.execute("SELECT image FROM complaints WHERE id = %s", (id,))
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