import json
from bottle import route, run, template

with open ("speed.txt", "r") as f:
    speeds = f.readlines()
data = [json.loads(x) for x in speeds]

str_template = """
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <title>SPEEDTEST</title>
  <link rel = "stylesheet"
   type = "text/css"
   href = "https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.css" />
</head>
<body>
  <canvas id="line-chart" width="1910" height="916"></canvas>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.js"></script>
  <script>
  var b = JSON.parse('{}')
"""
second = """
  
new Chart(document.getElementById("line-chart"), {
  type: 'line',
  data: {
    labels: b.map(e=>e.time),
    datasets: [{ 
        data: b.map(e=>e.speed),
        label: "Аюдаг",
        borderColor: "#3e95cd",
        fill: false
      }, 
    ]
  },
  options: {
    title: {
      display: true,
      text: 'Скорость интернета в Аюдаге'
    }
  }
});
</script>
</body>
</html>
"""

@route('/')
def index():
    return str_template.format(json.dumps(data)) + second

run(host='localhost', port=80, debug=True)
