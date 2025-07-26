import sqlite3

conn = sqlite3.connect('jarvis.db')
cursor = conn.cursor()

#To open windows app by using path
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'vlc','C:\\Program Files\\VideoLAN\\VLC\\vlc.exe')"
# cursor.execute(query)
# conn.commit()

#To open web application using the URL
query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), urls VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'canva','https://www.canva.com/')"
# cursor.execute(query)
# conn.commit()
