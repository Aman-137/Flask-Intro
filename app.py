from flask import Flask, redirect, url_for
### WSGI Application
app = Flask(__name__)

@app.route('/')
def welome():
    return "Welcome To My Youtube Channel.Please Please subscribe my channel."

### Building the url dynamically
### Variable rules and URL building

@app.route('/success/<int:score>')
def success(score):
    return "The Person has passed and the marks is "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is "+ str(score)

### Result Checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=marks))


if __name__ =='__main__':
    app.run(debug=True)