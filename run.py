import os

from src.app import app

if __name__ == "__main__":
    try:
        app.run_server(debug=bool(os.environ['DEBUG']), host=os.environ['HOST'], port=os.environ['PORT'])
    except Exception:
        print('An argument is needed')