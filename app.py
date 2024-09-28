from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    courses = ["c","c++","java","python","html","css"]
    return render_template("index.html",courses=courses)
@app.route('/about')
def about():
    
    return render_template("about.html")

# @app.route('/users/<name>')
# def users(name):
#     return "<h3>welcome {}</h3>".format(name)
@app.route('/users/<name>')
def users(name):
    return "<h3>welcome {}</h3>".format(name[50])

if __name__=='__main__':
    app.run(debug=True)