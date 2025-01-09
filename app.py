from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database Initialization
DATABASE = 'database.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)')
        conn.commit()

init_db()

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error="Page Not Found"), 404

if __name__ == '__main__':
    app.run(debug=True)
