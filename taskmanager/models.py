class Task:
    def __init__(self, id, title, description, due_date, completed, owner_id):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed
        self.owner_id = owner_id

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
