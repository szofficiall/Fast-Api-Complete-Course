from fastapi import FastAPI

app = FastAPI()

print("Server is running...")


@app.get("/")
def root():
    return {"data": {"name": "Sultan Zaib"}}


a = root()
print("The root end point retturened:", a)
# print("About Page Working...")


@app.get("/about")
def about():
    return {"data": "About Page"}
# print("About page loaded successfully.")
