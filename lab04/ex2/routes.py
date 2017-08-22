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
import csv
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        integers = request.form["integers"].split(',')
        final = bubbleSort(integers)
        return render_template("second.html",final_list=final)
    return render_template("first.html")


def bubbleSort(li):
    final_list = []
    sorted = False  # We haven't started sorting yet

    while not sorted:
        sorted = True  # Assume the list is now sorted
        for element in range(0, len(li)-1):
            if int(li[element]) > int(li[element + 1]):
                sorted = False  # We found two elements in the wrong order
                temp = li[element + 1]
                li[element + 1] = li[element]
                li[element] = temp
                final_list.append(list(li))
    print(final_list)
    return final_list 

