from crypt import methods
from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)


# DISPLAY ROUTES ------------
@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template('index.html', users = users)

@app.route('/create_user')
def create_user():
    return render_template('create.html')

    # show
@app.route('/user/<int:id>')
def show_user(id):
    data = {
        "id" : id
    }
    user = User.get_one(data)
    return render_template('show_user.html', user = user)

@app.route('/user/create/edit/<int:id>')
def edit_user(id):
    user = User.get_one({"id": id })
    return render_template('edit_user.html', user = user)

# ACTION ROUTES -----------
@app.route('/user/create', methods =['POST'])
def create():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    print(request.form)
    User.save(data)
    return redirect('/')
    
    #update
@app.route('/user/update', methods=['POST'])
def update_user():
    User.update_users(request.form)
    print(request.form)
    return redirect ('/')

    #delete
@app.route('/user/<int:id>/delete')
def delete_user(id):
    User.delete_user({"id": id})
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)