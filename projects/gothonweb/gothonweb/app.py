
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
	greeting = "Hello World"
	return render_template('index.html',greeting = greeting) 
	# return "hello world"	


if __name__ == '__main__' : 

	app.run()