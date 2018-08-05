from flask import Flask,json
import sys
import paramiko
from threading import Thread
from time import sleep

app = Flask(__name__)


ssh = paramiko.SSHClient()
last_fit = 0
read_fitness_log = "ls -1 /tmp/app_log/fitness.txt"
time_interval = 5

class IAsperathosMonitor(object):
    
    def __init__(self, app_address, app_username, app_pass):
        read_fitness_log = "ls - 1 /tmp/app_log/fitness.txt"
        self.__app_address = app_address
        self.__app_username = app_username
        self.__app_pass = app_pass

    def get_fit(self):
        global last_fit
        ssh.connect(self.__app_address, self.__app_username, password=self.__app_pass)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(read_fitness_log)
        ssh_stdin.close()
        last_fit = float(ssh_stdout.read())


class Server(Thread):
    def __init__(self,num_threads, port_number):
        Thread.__init__(self)
        self.num = num_threads
        self.__port_number = port_number
    def run(self):
        app.run(host="127.0.0.1",port=self.__port_number)


@app.route("/fitness",methods=['GET'])
def last_fitness_endpoint():
    json_fitness = { "fitness": last_fit }
    return app.response_class( response=json.dumps(json_fitness), status=200, mimetype='application/json')



if __name__ == "__main__":
    if(len(sys.argv) != 4):
        print("Invalid execution : \n Example : ./monitor_plugin <app_adress> <app_username> <app_pass>")
        exit()
    server = Server(1,5000)
    server.start()
    monitor = IAsperathosMonitor( sys.argv[1], sys.argv[2], sys.argv[3] )
    while True:
        monitor.get_fit()
        sleep(time_interval)
