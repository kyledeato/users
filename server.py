from crypt import methods
from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template('index.html', users = users)



@app.route('/create_user')
def create_user():
    return render_template('create.html')

@app.route('/user/create', methods =['POST'])
def create():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
    }
    print(request.form)
    User.save(data)

    return redirect('/')







if __name__ == "__main__":
    app.run(debug=True)