from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('local_data.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (
                        id INTEGER PRIMARY KEY,
                        category TEXT,
                        score1 INTEGER,
                        score2 INTEGER,
                        score3 INTEGER,
                        score4 INTEGER)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET'])
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM my_table')
    data = cursor.fetchall()
    conn.close()
    return render_template("index.html", data=data)

@app.route('/download', methods=['GET', 'POST'])
def download_data():
    if request.method == 'POST':
        # TODO: Open connection to online database
        # Example: Assuming download_data function retrieves data from an online source
        new_data = [
            ('Category1', 85, 90, 88, 92),
            ('Category2', 80, 85, 87, 89)
        ]
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.executemany('INSERT INTO my_table (category, score1, score2, score3, score4) VALUES (?, ?, ?, ?, ?)', new_data)
        conn.commit()
        conn.close()
        return redirect("/download")
    else:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM my_table')
        data = cursor.fetchall()
        conn.close()
        return render_template("download.html", data=data)

@app.route('/upload', methods=['GET', 'POST'])
def upload_data():
    if request.method == 'POST':
        category = request.form['category']
        score1 = int(request.form['score1'])
        score2 = int(request.form['score2'])
        score3 = int(request.form['score3'])
        score4 = int(request.form['score4'])

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO my_table (category, score1, score2, score3, score4) VALUES (?, ?, ?, ?, ?)', 
                        (category, score1, score2, score3, score4))
        conn.commit()
        conn.close()

        if 'upload' in request.form:
            # TODO: Open connection to online database
            # TODO: Upload info for own hospital/station to online database
            # Example: Assuming upload_data function uploads data to an online source
            pass

        return redirect("/upload")
    else:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM my_table')
        data = cursor.fetchall()
        conn.close()
        return render_template("upload.html", data=data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
