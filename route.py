from flask_restful import Resource
from flask import request
from todo import Todo
from db import db


class HomeRoute(Resource):
    def get(self):
        todos = db.session.query(Todo).all()
        todos = [todo.to_json() for todo in todos]
        return {'data': todos}

    def post(self):
        title = request.form["title"]
        description = request.form["description"]
        done = request.form["done"]
        todo = Todo(title=title, description=description, done=done)
        db.session.add(todo)
        db.session.commit()
        return {'data': todo.to_json()}

class HomeRouteWithId(Resource):
    def get(self, id):
        data_object = db.session.query(Todo).filter(Todo.id == id).first()
        if (data_object):
            return {'data': data_object.to_json()}
        else:
            return {'data': 'Not found'}, 404

    def put(self, id):
        data_object = db.session.query(Todo).filter(Todo.id == id).first()
        if (data_object):
            for key in request.form.keys():
                setattr(data_object, key, request.form[key])
            setattr(data_object, 'updatedAt', db.func.now())
            db.session.commit()
            return {'data': data_object.to_json()}
        else:
            return {'data': 'Not found'}, 404

    def delete(self, id):
        data_object = db.session.query(Todo).filter(Todo.id == id).first()
        if (data_object):
            db.session.delete(data_object)
            db.session.commit()
            return {'data': 'DELETED'}
        else:
            return {'data': 'Not found'}, 404
