from flask import Flask, request
import requests

app = Flask(__name__)

server_list = ['http://localhost:6001/',
               'http://localhost:6002/',
               'http://localhost:6003/',
               'http://localhost:6004/',]

circular_i = 0
max_i = 2

'''
@app.route('/set-n-servers/<amount>', methods=['GET'])
def set_n_servers(amount):
    global max_i
    if not 0 < int(amount) < 5:
        return '', 422
    max_i = int(amount)
    return '', 200
'''

@app.route("/up",methods=['POST'])
def scale_up():
    global max_i
    content = request.json
    max_i = min(4, max_i + content['vm_number'])
    return "",200

@app.route("/down",methods=['POST'])
def scale_down():
    global max_i
    content = request.json
    max_i = max(1, max_i - content['vm_number'])
    return "",200

@app.route("/set-ip/<string:ip>",methods=['GET'])
def set_ip(ip):
    global server_list
    server_list = ['http://' + ip + ':6001/',
               'http://' + ip + ':6002/',
               'http://' + ip + ':6003/',
               'http://' + ip + ':6004/',]
    return '', 200

@app.route('/<path:url>', methods=['PUT', 'POST', 'GET', 'DELETE'])
def proxy_passthrough_endpoint(url):
    global circular_i, max_i, server_list

    target_url = server_list[circular_i]
    circular_i = (circular_i + 1) % max_i

    data = request.get_data()
    resp = requests.post(target_url + url, data=data)
    return (resp.content, resp.status_code, resp.headers.items())


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005)
