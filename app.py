from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="student_db"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    try:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']
        address = request.form['address']

        query = "INSERT INTO students (name, email, phone, course, address) VALUES (%s,%s,%s,%s,%s)"
        values = (name, email, phone, course, address)

        cursor.execute(query, values)
        db.commit()

        return render_template('index.html', message="✅ Student Registered Successfully!")

    except:
        return render_template('index.html', message="❌ Error occurred!")


@app.route('/students')
def students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    return render_template('view.html', students=data)


# 🔥 DELETE
@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    db.commit()
    return redirect('/students')


# 🔥 EDIT PAGE
@app.route('/edit/<int:id>')
def edit(id):
    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cursor.fetchone()
    return render_template('edit.html', student=student)


# 🔥 UPDATE
@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']
    address = request.form['address']

    cursor.execute("""
        UPDATE students 
        SET name=%s, email=%s, phone=%s, course=%s, address=%s
        WHERE id=%s
    """, (name, email, phone, course, address, id))

    db.commit()
    return redirect('/students')


if __name__ == '__main__':
    app.run(debug=True)