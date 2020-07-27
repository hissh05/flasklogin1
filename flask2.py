from flask import Flask,render_template, request, , jsonify 
from datetime import timedelta


app = Flask(__name__)
app.secret_key ="hello"
app.permanent_session_lifetime = timedelta(minutes=0.1)

@app.route("/login", methods=["POST","GET"])
def login():
	if request.method == "POST":
		
		user =request.form["nm"]
		pword= request.form["ps"]
		session["user"] = user
	
		if len(pword) < 6:
			return jsonify({'output':{"status":'201',"msg":'Failure: password should be of length 6'}})
		elif pword.isalpha() == True:
			return jsonify({'output':{"status":'202',"msg":'Failure: password to have 1 character and 1 number'}})
		else:
			if user == 'vaibhav' and pword == 'abcd12':
				return jsonify({'output':{"status":'200',"msg":'success'}})
			elif user.isdigit() == True:
				return jsonify({'output':{"status":'203',"msg":'Failure: only characters allowed in username'}})
			else:
				return jsonify({'output':{"status":'204',"msg":'Failure:username incorrect'}})
					
			
	else:
		
		return render_template("login1.html")
if __name__ == '__main__':
	app.run(debug=True) 