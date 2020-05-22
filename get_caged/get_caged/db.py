import sqlite3


def initialize_db():
    conn = sqlite3.connect('cage.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS nicholas_cage_images
                 (id integer PRIMARY KEY, 
                 width integer NOT NULL, 
                 height integer NOT NULL, 
                 aspect_ratio float NOT NULL, 
                 image_data blob NOT NULL,
                 face_height_coord integer NOT NULL,
                 face_width_coord integer NOT NULL)''')

    conn.commit()
