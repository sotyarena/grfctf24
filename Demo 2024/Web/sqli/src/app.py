from flask import Flask, render_template, send_from_directory, url_for, request, session
import sqlite3
import os

app = Flask(__name__)
rootPath = os.path.join(app.root_path, 'static')
app.jinja_env.globals['static_file'] = lambda filename: url_for('static', filename=filename)

def init_db():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
    c.execute('''INSERT INTO users (username, password) VALUES ('admin', 'password')''')
    conn.commit()
    conn.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            conn = sqlite3.connect('db.sqlite3')
            c = conn.cursor()
            
            query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
            c.execute(query)
            user = c.fetchone()
            conn.close()

            if user:
                return render_template('index.html')
            else:
                return render_template('login.html')
        
        except Exception as e:
            # Menangani error lainnya
            print(f"Error: {e}")
            return render_template('login.html')

    return render_template('login.html')

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(rootPath, 'robots.txt')

@app.route('/flag.txt')
def robots_txt():
    return send_from_directory(rootPath, 'flag.txt')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)

