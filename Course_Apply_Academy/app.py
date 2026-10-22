from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "course_apply_academy_demo_key"

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "123456789",  # Change this if your MySQL password is different
    "database": "course_apply_academy"
}

LOGIN_USERNAME = "THARUN"
LOGIN_PASSWORD = "THARUN123"

COURSES = [
    {"id": 1, "name": "Full Stack Web Development", "duration": "6 Months", "fee": 15000, "category": "Development", "description": "Learn HTML, CSS, JavaScript, Python and database basics."},
    {"id": 2, "name": "Python Programming", "duration": "3 Months", "fee": 8000, "category": "Programming", "description": "Build a strong foundation in Python programming."},
    {"id": 3, "name": "Java Full Stack", "duration": "6 Months", "fee": 18000, "category": "Development", "description": "Learn Java, web development and SQL database concepts."},
    {"id": 4, "name": "Data Science", "duration": "5 Months", "fee": 20000, "category": "Data & AI", "description": "Explore data analysis, visualization and machine learning basics."},
    {"id": 5, "name": "UI/UX Design", "duration": "3 Months", "fee": 9000, "category": "Design", "description": "Learn user interface design and user experience principles."},
    {"id": 6, "name": "Cyber Security Basics", "duration": "4 Months", "fee": 12000, "category": "Security", "description": "Understand security fundamentals and safe computing practices."},
]

def get_db():
    return mysql.connector.connect(**DB_CONFIG)

@app.route("/", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        if username == LOGIN_USERNAME and password == LOGIN_PASSWORD:
            session["username"] = username
            return redirect(url_for("home"))
        error = "Invalid Username or Password"
    return render_template("login.html", error=error)

@app.route("/home")
def home():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("home.html", courses=COURSES)

@app.route("/apply/<int:course_id>", methods=["GET", "POST"])
def apply(course_id):
    if "username" not in session:
        return redirect(url_for("login"))
    course = next((c for c in COURSES if c["id"] == course_id), None)
    if course is None:
        return "Course not found", 404
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        qualification = request.form.get("qualification", "").strip()
        if not all([name, email, phone, qualification]):
            flash("Please fill all fields.", "danger")
            return render_template("apply.html", course=course)
        try:
            con = get_db()
            cur = con.cursor()
            cur.execute(
                """INSERT INTO applications
                   (login_username, student_name, email, phone, qualification, course_name, course_fee)
                   VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                (session["username"], name, email, phone, qualification, course["name"], course["fee"])
            )
            con.commit()
            cur.close()
            con.close()
            return redirect(url_for("success"))
        except mysql.connector.Error as e:
            return render_template("apply.html", course=course, db_error="Database error. Check MySQL password and run database.sql. Details: " + str(e))
    return render_template("apply.html", course=course)

@app.route("/applications")
def applications():
    if "username" not in session:
        return redirect(url_for("login"))
    try:
        con = get_db()
        cur = con.cursor(dictionary=True)
        cur.execute("SELECT * FROM applications ORDER BY id DESC")
        rows = cur.fetchall()
        cur.close()
        con.close()
        return render_template("applications.html", applications=rows)
    except mysql.connector.Error as e:
        return render_template("applications.html", applications=[], db_error="Database error: " + str(e))

@app.route("/success")
def success():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("success.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
