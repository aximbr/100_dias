from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/username/<name>")
def great(name):
    return f"Hello {name}!"

@app.route('/post/<int:post_id>')
def show_double(post_id):
    # show the post with the given id, the id is an integer
    double = 2*post_id
    return 'Post %d' %double

#main()

if __name__ == "__main__":
    app.run(debug=True)