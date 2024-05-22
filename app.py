from flask import Flask, render_template, request, url_for, redirect, jsonify
import sqlite3

app = Flask(__name__)

# TODO: Handle opening/closing database connection
def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (
                        id INTEGER PRIMARY KEY,
                        data TEXT)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET'])
def home():
    # TODO: Read information in local storage
    # TODO: Convert local storage information into a variable
    # TODO: Pass variable into page
    return render_template("index.html")

@app.route('/download', methods=['GET', 'POST'])
def current_data():
    if request.method == 'POST':
        # TODO: Open connection to online database
        # TODO: Download info for other hospitals
        # TODO: Write info to local storage
        return redirect("/download")
    else:
        # TODO: Read information in local storage
        # TODO: Convert local storage information into a variable
        # TODO: Pass variable into page
        return render_template("download.html")
    

@app.route('/upload', methods=['GET', 'POST'])
def current_data():
    if request.method == 'POST':
        if """Save button pressed""":
            # TODO: Take form submission data and write to variables
            # TODO: Write info to local storage
            return redirect("/upload")
        if """Upload button pressed""":
            # TODO: Take form submission data and write to variables
            # TODO: Write info to local storage
            # TODO: Open connection to online database
            # TODO: Upload info for own hospital/station to database
            # TODO: Close connection to online database
            return redirect("/upload")
    else:
        # TODO: Read information in local storage
        # TODO: Convert local storage information into a variable
        # TODO: Pass variable into page
        return render_template("download.html")


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
