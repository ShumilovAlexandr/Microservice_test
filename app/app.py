import os
import pathlib
from flask import Flask

from conf import BASE_PATH


app = Flask(__name__)


@app.route("/api/meta", methods=["GET"])
def get_data():
    data = []
    dirname = pathlib.Path(BASE_PATH)
    for file in dirname.iterdir():
        if file.is_dir():
            folder_dir = ({
                'name': file.name,
                'type': 'folder',
                'time': os.stat(file).st_ctime
            })
            data.append(folder_dir)
        elif file.is_file():
            file_dir = ({
                'name': file.name,
                'type': 'file',
                'time': os.stat(file).st_ctime
            })
            data.append(file_dir)
    return data


if __name__ == '__main__':
    app.run()
