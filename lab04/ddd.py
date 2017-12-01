from flask import Flask, redirect, render_template, request, url_for
from server import app
import csv
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        zID = int(request.form["zID"])
        desc = request.form["desc"]

        #user_input.append([name, zID, description])
        with open('example.csv','a') as csv_out:
        	writer = csv.writer(csv_out)
        	writer.writerow([name, zID, desc])
               

        return redirect(url_for("hello"))
    return render_template("index.html")

@app.route("/Hello")
def hello():
	name = ""
	id = 0
	desc = ""
	array = []
	with open('example.csv','r') as csv_in:
		reader = csv.reader(csv_in)
		for row in reader:
			name = row[0];
			id = row[1];
			desc = row[2];
	return render_template("hello.html", name=name, id=id, desc=desc)

