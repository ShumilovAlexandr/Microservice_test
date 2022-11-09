from flask import Flask
import requests


def create_application():
    app = Flask(__name__)


    @app.route("/api/meta", method=["GET"])
    def get():
        ...

    return app



if __name__ == '__main__':
    app = create_application()
    app.run()