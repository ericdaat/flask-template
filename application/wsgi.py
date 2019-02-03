from application import create_app
from waitress import serve

if __name__ == "__main__":
    application = create_app()
    serve(application)