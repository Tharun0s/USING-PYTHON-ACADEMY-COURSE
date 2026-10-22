COURSE APPLY ACADEMY - FLASK + MYSQL

FEATURES
1. Login page
2. Six available courses
3. Apply form for each course
4. Application details saved to MySQL
5. View all submitted applications
6. Logout

LOGIN
Username: THARUN
Password: THARUN123

SETUP (Windows / VS Code)
1. Extract this ZIP.
2. Open the extracted Course_Apply_Academy folder in VS Code.
3. Open MySQL Workbench or MySQL Command Line.
4. Run the full database.sql file.
5. Open app.py and check DB_CONFIG:
   user = root
   password = 123456789
   Change password to your actual MySQL root password if different.
6. Open Terminal in the project folder and run:
   py -m pip install -r requirements.txt
7. Run:
   py app.py
8. Open browser:
   http://127.0.0.1:5000

IMPORTANT
- MySQL server must be running.
- The demo login is hardcoded in app.py; it does not use a users table.
- Applications are stored in the course_apply_academy database.
- Bootstrap styling uses an internet CDN.
