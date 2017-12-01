# Import Flask Library
#from flask import Flask
# create a Flask application instance
#app = Flask(__name__)
# define a route through the app.route decorator
#from server import app
#@app.route("/")
#def index():
    #return "<h1>Hello World!</h1>"
# launch the integrated development web server
# and run the app on http://localhost:8085
#if __name__=="__main__":
#  app.run(debug=True,port=8085)
#from server import app
#@app.route("/")
#def index():
#    return "<h1> Hello world </h1>"
from flask import Flask, redirect, render_template, request, url_for
from server import app
import math
calc_input = ""


@app.route("/", methods=["GET", "POST"])
def calculator():
	global calc_input
	mystr = ""
	buttons = "1 2 3 C 4 5 6 + 7 8 9 - 0 * / = ( ) sin tan cos log sqrt CE ".split(" ")
	if request.method == "POST":
		if (request.form["button"] == "="):
			for i in calc_input:
				mystr += str(i)
			calc_input = []
			calc_input.append(eval(mystr))
		elif (request.form["button"] =="C"):
			calc_input = calc_input[:-1]
		elif (request.form["button"] == "CE"):
			calc_input = ""
		else:
			calc_input += (request.form["button"])

	return render_template("index.html" , output=calc_input, buttons=buttons, length=len(buttons))
    
