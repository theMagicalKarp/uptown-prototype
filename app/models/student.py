from google.appengine.ext import db

class Student(db.Model):
    name = db.StringProperty(required=True)
    age = db.IntegerProperty(required=True)


def fetch_students_by_age(age):
    return Student.all().filter('age', age).fetch(limit=None)

def fetch_students(limit=100, offset=0):
    return Student.all().fetch(limit=limit, offset=offset)

def create_student(name, age):
    new_student = Student(name=name, age=int(age))
    new_student.put()

    return new_student