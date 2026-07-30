from fastapi import FastAPI
app = FastAPI()


@app.get("/Home")
def read():
    return{"message":"Welcome to courses management System"}

l=[]
@app.get("/courses")
def courses():
    return{"courses":l}

@app.post("/addcourses/{course_name}")
def addcourse(course_name:str):
    l.append(course_name)
    return f"message:{course_name} added successfully"

@app.put("/updatecourse/{oldcourse_name}/{newcourse_name}")
def updatecourse(oldcourse_name:str,newcourse_name:str):
    if oldcourse_name in l:
        index=l.index(oldcourse_name)
        l[index]=newcourse_name
        return f"message:{oldcourse_name} updated successfully to {newcourse_name}"
    else:
        return f"message:{oldcourse_name} not found"

@app.delete("/deletecourse/{course_name}")
def delete(course_name:str):
    if course_name in l:
        l.remove(course_name)
        return f"message:{course_name} deleted successfully"
    else:
        return f"message:{course_name} not found"
    


