from flask import Flask, request, render_template,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def submit():
     if request.method == "POST":
          name = request.form.get("username")
          password = request.form.get("password")
          if name == "admin" and password == "1234":
               return render_template("thankyou.html")
          else:
               return render_template("no_auth.html")
     return render_template("login.html")




if __name__ == "__main__":
     app.run(debug=True)

