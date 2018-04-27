from flask import Flask, render_template, redirect, request
from werkzeug import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os
import csv
from collections import namedtuple

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app) 

class Note(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	body = db.Column(db.Text)

class FileEntry(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	customer_id = db.Column(db.Integer)
	first_name = db.Column(db.String(100))
	last_name = db.Column(db.String(100))
	street_address = db.Column(db.String(200))
	state = db.Column(db.String(30))
	zip_code = db.Column(db.Integer)
	requested_change = db.Column(db.String(10))
	product_id = db.Column(db.Integer)
	product_name = db.Column(db.String(100))
	purchase_price = db.Column(db.Integer)
	#This should be some other datatype, I was just having trouble pinning down which kind of date type to use so I left it as a string for the Proof of Concept
	transaction_time = db.Column(db.String(100))


@app.route("/", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":

    	title = request.form["title"]
        body = request.form["body"]

        note = Note(title=title, body=body)

        db.session.add(note)
        db.session.commit()

        return redirect("/")
    else:
        return render_template("create_note.html")

@app.route('/test')
def test_page():
	return render_template('test.html')

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploading_file():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		print 'file uploaded successfully'

		with open(f.filename,'rb') as file:
			reader = csv.reader(file, delimiter='\t')
			for row in reader:
				row_as_list = list(row)
				customer_id = row_as_list[0]
				first_name = row_as_list[1]
				last_name = row_as_list[2]
				street_address = row_as_list[3]
				state = row_as_list[4]
				zip_code = row_as_list[5]
				requested_change = row_as_list[6]
				product_id = row_as_list[7]
				product_name = row_as_list[8]
				purchase_price = row_as_list[9]
				transaction_time = row_as_list[10]

				file_entry = FileEntry(customer_id = customer_id, first_name = first_name, last_name = last_name, street_address = street_address, state = state, zip_code = zip_code, requested_change = requested_change, product_id = product_id, product_name = product_name, purchase_price = purchase_price, transaction_time = transaction_time)

				db.session.add(file_entry)
				db.session.commit()

		return redirect("/")


if __name__ == "__main__":
	app.run(debug=True)

