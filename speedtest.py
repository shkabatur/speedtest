from subprocess import check_output
import json
from pprint import pprint

output = check_output("iperf3 -c 178.34.154.130 -J")

data = json.loads(output)

result = dict()

result['time'] = data["start"]["timestamp"]["time"]
result['speed'] = data["end"]["sum_received"]["bits_per_second"] / 1024 / 1024

print(json.dumps(result))



