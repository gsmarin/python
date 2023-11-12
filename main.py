from fastapi import FastAPI, Path
from api import users, courses, sections


app = FastAPI(title="Fast API LMS",
              description="LMS for managging students and courses",
              version="0.0.1", 
              contact={
                  "name":"Giorbis Marin",
                  "email": "gsmarin85@gmail.com"
              },
              license_info={"name": "GRPS"})

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)