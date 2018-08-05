from flask import Flask,json
import sys
import paramiko

app = Flask(__name__)

ssh = paramiko.SSHClient()

last_fit = 0
read_fitness_log = "ls - 1 /tmp/app_log/fitness.txt"

def get_fit_from_app(app_server, app_username, app_pass):
    ssh.connect(app_server, app_username, password=app_pass)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(read_fitness_log)
    ssh_stdin.close()
    last_fit = float(ssh_stdout.read())


@app.route("/fitness",methods=['GET'])
def last_fitness_endpoint():
    json_fitness = { "fitness": last_fit }
    return app.response_class( response=json.dumps(json_fitness), status=200, mimetype='application/json')


if __name__ == "__main__":
    if(len(sys.argv) != 4):
        print("Invalid execution : \n Example : ./monitor_plugin <app_adress> <app_username> <app_pass>")
    #app.run()
