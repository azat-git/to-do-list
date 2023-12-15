from flask import Flask, render_template, request, redirect, url_for
import db

app = Flask(__name__)


@app.route('/')
def index():
    items = db.get_items()
    return render_template('index.html', items=items)


@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form.get('item_name')
    db.add_item(item_name)
    return redirect(url_for('index'))


@app.route('/remove/<int:item_id>')
def remove_item(item_id):
    db.remove_item(item_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.init_db()
    app.run(debug=True)
