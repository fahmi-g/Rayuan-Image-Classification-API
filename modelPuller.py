import requests

url = "https://github.com/fahmi-g/Rayuan-Image-Classification-API/raw/main/model_experiment.h5"
response = requests.get(url)
open("test.h5", "wb").write(response.content)

print("Model is successfully pulled")