from google.appengine.ext import db


# You can find more out about types and properties of google app engine 
# database models here! 
# https://developers.google.com/appengine/docs/python/datastore/typesandpropertyclasses
class Student(db.Model):
    name = db.StringProperty(required=True)
    age = db.IntegerProperty(required=True)


def fetch_students_by_age(age):
    return Student.all().filter('age', age).fetch(limit=None)

def fetch_students(limit=100, offset=0):
    return Student.all().fetch(limit=limit, offset=offset)

def create_student(name, age):
    new_student = Student(name=name, age=int(age)) # Create new database model!
    new_student.put() # Store it in the database!

    return new_student