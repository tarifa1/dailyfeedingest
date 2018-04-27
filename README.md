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

To check whether the app has correctly inserted the data into the database, you can load the app.sqlite file into a sqlite reader/viewer - free tools available at: 

	http://sqliteviewer.flowsoft7.com/


3) Next steps

A) The database is not fully functional to the extent we'd want this app to be. It currently accepts all files that match the expected feed format to the exact column. Adding in features to reject files not meeting this standard would be ideal.

B) The DB also needs to work with a few other tables. In round two of this app, we would create dedicated tables for customers and products and then use the table from the file upload as a staging table that then makes the final inserts/updates into the dedicated tables

-An example of this normalization is made available in the form of the file: db_normalization_plan.xlsx which is available in the main directory

C) There should be testing for all of methods

D) Upload/progress bar for the file upload would be great.

E) Modifying this to work on MySQL instead of SQLite would allow for this to scale up to a production level app instead of a local app ; this is why SQLAlchemy was used, to make that easier