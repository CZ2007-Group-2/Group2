# Group2
This is Jovian's SQLite demo

# Schemas
The schemas can be found in demo/models.py

# How to run
0) Delete database.db if you want to recreate the database
1) Run main.py
2) Go to http://localhost:5000/creation
(Step 2 creates some default entries in the database for viewing)
3) It will redirect you to http://localhost:5000/, where it will print the first customer that made a complaint, and which employee made the complains

# Code
In views.py, there are some helper functions that create basic entries in our tables (except for orders because I was lazy)
A customer called Jovian will be created, and a complaint will be created for him.
A random employee will then be assigned to handle this complaint

# Database viewer
To view the DB for yourself, download https://sqlitebrowser.org/
Use the application to open database.db

# Screenshots
SQLite Demo\demo\screenshots\1.png
SQLite Demo\demo\screenshots\2.png
SQLite Demo\demo\screenshots\3.png
SQLite Demo\demo\screenshots\4.png