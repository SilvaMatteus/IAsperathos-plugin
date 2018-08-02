from flask import Flask, request
import requests

app = Flask(__name__)

server_list = ['http://localhost:6002',
               'http://localhost:6002',
               'http://localhost:6003',
               'http://localhost:6004',]

circular_i = 0
max_i = 1


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/set-n-servers/<amount>', methods=['GET'])
def set_n_servers(amount):
    global max_i
    if not 0 < int(amount) < 5:
        return '', 403
    max_i = int(amount)
    return '', 200


@app.route('/fitness', methods=['POST', 'GET'])
def fitness():
    global circular_i, max_i, server_list

    target_url = server_list[circular_i]
    circular_i = (circular_i + 1) % max_i

    response = requests.get(target_url, headers=request.headers, data=request.data)
    return response.content, response.status_code


if __name__ == '__main__':
    app.run()
