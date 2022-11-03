import uvicorn
from quickshare.main import run




if __name__ == "__main__":
    uvicorn.run("main:run")
