# dailyfeedingest
Web app to ingest daily feeds 

Author - Tarif Ahmed
Date - 4.18.2018


1) Design

The application was designed to run locally on a laptop using SQLite and Flask as the underlying tools. The app currently launches a local webpage which allows the user to upload a file via upload form. The file is then parsed in Python using CSV reader, converted into a list, and each list entry is then inserted in the database


2) Implementation

Databse Initialization 

-Clone the app to your laptop from Git
-Navigate to the directory the app is located in and open a Shell command line 
-Execute the following code to initialize the database:

		python
		from main import db
		db.create_all() 

To validate whether the database was created successfully, please navigate back to the app directory and confirm the existance of the app.sqlite file.

Now launch the app:
	python main.py

The web interface can be accessed:
	http://localhost:5000/ 

From there, upload the file via the URL that labelled "Upload daily feed"

To check whether the app has correctly inserted the data into the database, you can load the app.sqlite file into a sqlite reader/viewer (free tools available at http://sqliteviewer.flowsoft7.com/)


3) Next steps

