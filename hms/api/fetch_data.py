import json
import requests
from subprocess import Popen, PIPE

def getSUs():
    return open('SUs').readlines()

def get_all():
    all_data = []
    for su in getSUs():
        su = su.strip()
        uri = 'coap://['+su+']/data'
        process = Popen(['coap-client', '-m', 'get', '-B', '3', uri], stdout=PIPE, stderr=PIPE)
        stdout, _ = process.communicate()

        data = stdout.decode('UTF-8').split('\n')[1]
        if len(data.strip()) != 0:
            data = json.loads(data)
        all_data.append(data)
    return all_data
    

if __name__ == "__main__":
    print(get_all())