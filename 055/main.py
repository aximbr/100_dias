from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper 

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/")
def hello():
    return '<h1 style="text-align: center">Hello World!</h1> \
           <p>This is a paragraph.</p> \
           <img src=https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGZqMjdmOTFqdWJ6dm4ybnozaTMwbmg2d2IzeDNxZHRoa2llNTByZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kc6n0RKTFbDJC/giphy.gif>' 

@app.route("/username/<name>")
def great(name):
    return f"Hello {name}!"

@app.route('/post/<int:post_id>')
def show_double(post_id):
    # show the post with the given id, the id is an integer
    double = 2*post_id
    return 'Post %d' %double

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

#main()

if __name__ == "__main__":
    app.run(debug=True)