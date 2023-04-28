from flask_app import app, render_template, redirect, request, session 
from flask_app.models.car import Car
from flask_app.models.user import User

#! CREATE
@app.route('/new')
def new():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('cars/new.html', users = User.get_all())

@app.route('/create', methods=['post'])
def create():
    print(request.form)
    if not Car.validate_car(request.form):
        return redirect('/new')
    Car.save(request.form)
    return redirect('/cars')

#! READ ALL
@app.route('/dashboard')        
def cars():
    if 'user_id' not in session:
        return redirect('/logout')
    # cars = Car.get_all()
    # print(cars)
    return render_template('dashboard.html', cars = cars) 

# #! READ ONE
# @app.route('/cars/<int:id>')
# def show(id):
#     car = Car.get_car(id)
#     print(car)
#     return render_template('cars/show.html', car = car)


# #! UPDATE

# @app.route('/cars/edit/<int:id>')
# def edit_car(id):
#     return render_template('cars/edit.html', cars = Car.get_car(id))

# @app.route('/update', methods=['post'])
# def update_car():
#     print(request.form)
#     if not Car.validate_car(request.form):
#         return redirect(f"/cars/edit/{request.form['id']}")
#     Car.update(request.form)
#     return redirect('/cars')

# #! DELETE 
# @app.route('/cars/delete/<int:id>')
# def destroy(id):
#     data = {'id': id}
#     Car.delete(id)
#     return redirect('/cars')