from fastapi import FastAPI, Path

app = FastAPI(title="Fast API LMS",
              description="LMS for managging students and courses",
              version="0.0.1", 
              contact={
                  "name":"Giorbis Marin",
                  "email": "gsmarin85@gmail.com"
              },
              license_info={"name": "GRPS"})

@app.get("/user", tags=["Get"])
async def get_user():
    return {"message":"All done!"}


@app.post("/user", tags=["Post"])
async def create():
    return {"message":"All done!"}


@app.get("/users/{id}")
async def get_user_by_id(
    id: int = Path(..., description="The ID of the user you want to retrieve")
):
    return {}