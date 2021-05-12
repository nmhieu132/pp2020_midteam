import sqlite3
from sqlite3 import Error
import cursor
database =r"C:\Users\DELL\Documents\db_file.db"
class insert:
    def insert_category(con,categorys):
        sql='''INSERT INTO Category(Id,CategoryName)
               VALUES(?,?) '''
        cursor.execute(sql,categorys)
        con.commit()
        return cursor.lastrowid
    def insert_customer(con,customers):
        sql='''INSERT INTO Customer(Id,Full_Nam,Phone,Number_people,Arrive_time
               VALUES(?,?,?,?,?) '''
        cursor.execute(sql,customers)
        con.commit()
        return cursor.lastrowid
    def insert_order(con,order):
        sql='''INSERT INTO Ordering(Id,CustomerId)
               VALUE(?,?) '''
        cursor.excute(sql,order)
        return cursor.lastrowid
    def insert_dishes(con,dish):
        sql='''INSERT INTO Dishes(Id,Dish_name,Price,Status,Description,CategoryId,ChefId
               VALUE(?,?,?,?,?,?,?) '''
        cursor.execute(sql,dish)
        return cursor.lastrowid
    def insert_orderedishes(con,odish):
        sql='''INSERT INTO Dishes_Ordering(Id,DishesId,OrderingId,Quantity,Price
               VALUE(?,?,?,?,?) '''
        cursor.execute(sql,odish)
        return cursor.lastrowid
    def insert_chefs(con,chef):
        sql='''INSERT INTO Chef(Id,Full_Name,Email,Phone,Salary)
               VALUE(?,?,?,?,?) '''
        cursor.execute(sql,chef)
        return cursor.lastrowid
    def insert_ingredients(con,ingredient):
        sql='''INSERT INTO Ingredient(Id,Ingredient_name,Description)
               VALUE(?,?,?) '''
        cursor.execute(sql,ingredient)
        return cursor.lastrowid
    def insert_dishesingredient(con,dingredient):
        sql='''INSERT INTO Dishes_Ingredient(Id,DishesId,IngredientId)
               VALUE(?,?,?) '''
        cursor.execute(sql,dingredient)
        return cursor.lastrowid
    def insert_comments(con,comment):
        sql='''INSERT INTO Comment(Id,CustomerId,DishesId,CreateAt,Content,Rate)
               VALUE(?,?,?,?,?,?) '''
        cursor.execute(sql,comment)
        return cursor.lastrowid