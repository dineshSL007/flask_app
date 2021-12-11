from flask import Flask,render_template,flash


app = Flask(__name__)

app.secret_key = 'super secret key'

application = app


@app.route("/")
def homepage():
   return "Its working"
 
 

    
if __name__ == "__main__":
    app.run()  
