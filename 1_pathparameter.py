from fastapi import FastAPI

app = FastAPI()
print("Path Parameter Example Running...")


@app.get("/")
def index():
    return {"data": "block list"}


@app.get("/blog/blog_pubished")
def blog_pubished():
    # fetch all published blogs
    return {"data": "all published blogs"}


@app.get("/blog/{id}")
def show(id: int):
    # fetch blog with blod id
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id: int):
    # fetch comments for a specific blog id = id
    return {"data": f"comments for blog {id} "}
    # return {"data": {"1","2"}}
