from flask import Flask,render_template,flash
import sys
import os
sys.path.append(os.path.abspath("scripts/"))

from content_management import content_management


app = Flask(__name__)

app.secret_key = 'super secret key'


@app.route("/")
def homepage():
   return render_template("main.html")
 
 

@app.route("/dashboard/")
def dashboard():
    
    flash("welcome to dashboard flask message testing1")
    flash("welcome to dashboard flask message testing2")
    
    DICT_cotent = content_management()
    return render_template("dashboard.html",DICT_CONTENT = DICT_cotent)
 
 
@app.errorhandler(404)
def page_not_found(e):
     return "<p>404 ERROR</p>" + str(e)
      
 
@app.route("/slidebar/")
def slidebar():
    
    DICT_cotent = content_management()
    
    try:
      return render_template("dashboard.html",DICT_CONTENT = ddd)
    except Exception as e:
      return "<p>500 error</p>" + str(e)
    
if __name__ == "__main__":
    
    app.debug=True
    app.run()  

