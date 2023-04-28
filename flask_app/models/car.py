# import the function that will return an instance of a connection
from flask_app import flash
from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint


DATABASE = "rent_cars"

class Car:
    
    
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price=data['price']
        self.user=data['first_name']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    def show_title(self):
        return self.title
    #! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO cars (title, description, price, user_id) VALUES (%(title)s,  %(description)s, %(price)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
       
    #! READ ALL 
    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM cars JOIN users ON users.id = cars.user_id;"
    #     results = connectToMySQL(DATABASE).query_db(query)
    #     pprint(results)
    #     cars = []
    #     for car_dict in results:
    #         cars.append(cls(car_dict))
    #     return cars
    
    # #! READ ONE
    # @classmethod
    # def get_car(cls, id):
    #     query = "SELECT * FROM cars JOIN users ON users.id = cars.user_id WHERE cars.id = %(id)s;"
    #     data = {'id': id}
    #     result = connectToMySQL(DATABASE).query_db(query, data)
    #     print(result[0])
    #     paint = Paint(result[0])
    #     return paint
    
    # #! UPDATE
    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE cars SET title=%(title)s, description=%(description)s, price=%(price)s WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db(query, data)
    
    # #! DELETE
    # @classmethod
    # def delete(cls, id):
    #     query = "DELETE FROM cars WHERE id = %(id)s;"
    #     data = {
    #         'id':id
    #     }
    #     return connectToMySQL(DATABASE).query_db(query, data)
        
    # @staticmethod
    # def validate_car(car:dict):
    #     is_valid = True
    #     if len(car['title']) < 1:
    #         flash("title must be present")
    #         is_valid = False
    #     if len(car['description']) < 5:
    #         flash("description must be longer than 5 characters")
    #         is_valid = False
    #     if len(car['price']) <= 0:
    #         flash("please add a price")
    #         is_valid = False
       
        
    #     return is_valid