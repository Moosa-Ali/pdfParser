from fastapi import FastAPI

# initiate object
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
