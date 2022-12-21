from typing import Union
import threading
from fastapi import FastAPI

app = FastAPI()
ev = threading.Event()

def bg():
    while not ev.is_set():
        print("HELLO")
        # sleep 1 s
        ev.wait(1)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

threading.thread(target=bg).start()

# sleep 5 seconds
ev.wait(5)
ev.set()