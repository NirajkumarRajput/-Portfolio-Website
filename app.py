from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/resume.html')
def resume():
    return render_template('resume.html')

@app.route("/Experience.html")
def Experience():
    return render_template("Experience.html")

@app.route("/projects.html")
def projects():
    return render_template("projects.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route('/resume_1.html')
def resume_1():
    return render_template('resume_1.html')

@app.route('/email.html')
def email():
    return render_template("email.html")
if __name__ == '__main__':
    app.debug = True
    app.run()