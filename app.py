from flask import Flask, jsonify, send_file, abort
from datetime import datetime
import uuid
import os

app = Flask(__name__)


files = {
    "0858cf1a-769c-46ab-88fb-12710f8f44a7": {
        "create_datetime": datetime.now().isoformat(),
        "size": 1234,
        "mimetype": "text/plain",
        "name": "example.txt",
        "path": "example.txt"
    }
}


@app.route('/file/<uuid>/stat/', methods=['GET'])
def file_stat(uuid):
    file_data = files.get(uuid)
    if file_data:
        return jsonify(file_data)
    else:
        abort(404)


@app.route('/file/<uuid>/read/', methods=['GET'])
def file_read(uuid):
    file_data = files.get(uuid)
    if file_data and os.path.exists(file_data['path']):
        return send_file(file_data['path'], as_attachment=True, download_name=file_data['name'], mimetype=file_data['mimetype'])
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='localhost', port=80)
