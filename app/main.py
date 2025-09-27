from .server import app 



def main():
    import uvicorn
    uvicorn.run(app = app, host="0.0.0.0", port=8000)
    
    

# technically it is correct if we want to deploy it
    
    
main()