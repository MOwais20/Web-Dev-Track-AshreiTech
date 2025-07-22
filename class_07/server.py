from fastapi import FastAPI
from inventory import products


# FastAPI app instance banate hain
app = FastAPI()

# Route define karte hain
@app.get("/create-order")
def read_root():
    return {"products": products}

markAttendance = {
        "name": "Imtiaz",
        "status": False
    }

def find_student(id):
    pass


@app.get("/create-attendance")
def create_attendance():
    
    # find student by id
    find_student(12)
    
    markAttendance["status"] = True
    
    print(f"Attendance marked for {markAttendance['name']}: {markAttendance['status']}")
    
    return {"message": "Attendance created successfully!"}

# Agar ye file directly run ho to server start karo
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
# Note: Jupyter mein run karne ke liye upar wala code comment kar dein
print("FastAPI app created! Server start karne ke liye terminal mein: uvicorn main:app --reload")