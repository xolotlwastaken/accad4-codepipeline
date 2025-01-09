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

@app.route('/items', methods=['GET', 'POST'])
def items():
    with sqlite3.connect(DATABASE) as conn:
        if request.method == 'POST':
            item_name = request.form['item_name']
            conn.execute('INSERT INTO items (name) VALUES (?)', (item_name,))
            conn.commit()
            return redirect(url_for('items'))
        
        cursor = conn.execute('SELECT * FROM items')
        items = cursor.fetchall()
    return render_template('items.html', items=items)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item_name = request.form['item_name']
        return redirect(url_for('items'))
    return render_template('add_item.html')

# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error="Page Not Found"), 404

if __name__ == '__main__':
    app.run(debug=True)
