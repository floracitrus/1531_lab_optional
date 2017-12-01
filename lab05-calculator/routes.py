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
calc_input = []
flag = False

@app.route("/", methods=["GET", "POST"])
def calculator():
	global calc_input
	global flag
	if flag == True: 
		calc_input = []
		flag = False
	mystr = ""
	buttons = "1 2 3 C 4 5 6 + 7 8 9 - 0 * / = ( ) sin tan cos log sqrt CE ".split(" ")
	if request.method == "POST":
		if (request.form["button"] == "="):
			for i in calc_input:
				mystr += i
			calc_input = []
			calc_input.append(eval(mystr))
			flag = True
		elif (request.form["button"] =="C"):
			calc_input.pop()
		elif (request.form["button"] == "CE"):
			del calc_input[:]
		else:
			calc_input.append(request.form["button"])

	return render_template("index.html" , output=calc_input, buttons=buttons, length=len(buttons))
    
