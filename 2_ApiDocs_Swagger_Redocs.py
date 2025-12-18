from fastapi import FastAPI
# from pydantic import EmailStr
app = FastAPI()
print("Api Docs Example Running...")


@app.get("/")
def index():
    print("Index endpoint called")
    return {"data": "Welcome to the API Documentation Example"}


@app.get("/items/{item_id}")
def show_item_with_id(item_id: int):
    print(f"Fetching item with id: {item_id}")
    return {"data": f"Item With Id {item_id}"}


print("-----------------------------/n-----------------------------")
print("Get email name and id example running...")


@app.get("user/{user_id}/email/{email_name}")
def show_data(user_id: int, email_name: str):
    print(f"user_id: {user_id}, email_name: {email_name}")
    return {"data": f"user id is {user_id} and email name is {email_name}"}
