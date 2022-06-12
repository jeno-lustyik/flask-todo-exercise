from db import db
import uuid


class Todo(db.Model):
    id = db.Column(db.String(32), primary_key=True, default=str(uuid.uuid4()), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    done = db.Column(db.String(8), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updatedAt = db.Column(db.DateTime, nullable=False, default=db.func.now())

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': str(self.done),
            'createdAt': str(self.createdAt),
            'updatedAt': str(self.updatedAt)
        }
