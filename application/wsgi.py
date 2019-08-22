from waitress import serve

from application import create_app



if __name__ == "__main__":
    application = create_app()
    serve(application)