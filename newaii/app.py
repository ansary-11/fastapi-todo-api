from fastapi import FastAPI,HTTPException

from schema import Task
app = FastAPI()



text_todos={"1": {"todo id": "First todo", "description": "This is the first todo", "done": False}, 
            "2": {"todo id": "Second todo", "description": "This is the second todo", "done": False},
            "3": {"todo id": "Third todo", "description": "This is the third todo", "done": False},
            "4": {"todo id": "Fourth todo", "description": "This is the fourth todo", "done": False},
            "5": {"todo id": "Fifth todo", "description": "This is the fifth todo", "done": False},
            "6": {"todo id": "Sixth todo", "description": "This is the sixth todo", "done": False},    
            "7": {"todo id": "Seventh todo", "description": "This is the seventh todo", "done": False},
            "8": {"todo id": "Eighth todo", "description": "This is the eighth todo", "done": False},
            "9": {"todo id": "Ninth todo", "description": "This is the ninth todo", "done": False},
            "10": {"todo id": "Tenth todo", "description": "This is the tenth todo", "done": False}
            }

@app.get("/todos")
def get_todos(limit: int = 10):
    return list(text_todos.values())[:limit]


@app.get("/todos/{todo_id}")
def get_todo(todo_id: str):
    todo = text_todos.get(todo_id)
    if todo:
        return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}")
def update_todo(todo_id: str, todo: Task):
        if todo_id not in text_todos:
            raise HTTPException(status_code=404, detail="Todo not found")
        text_todos[todo_id] = {"todo id": todo.title, "description": todo.description, "done": todo.done}
        return text_todos[todo_id] 

@app.post("/todos")
def create_todo(todo : Task):
    if todo.title in [p["todo id"] for p in text_todos.values()]:
        raise HTTPException(status_code=400, detail="Todo with this title already exists")
    todo_id = str(len(text_todos) + 1)
    text_todos[todo_id] = {"todo id": todo.title, "description": todo.description, "done": todo.done} 
    return text_todos[todo_id] 

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    if todo_id not in text_todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del text_todos[todo_id]
    return {"message": "Todo deleted successfully"}

    
