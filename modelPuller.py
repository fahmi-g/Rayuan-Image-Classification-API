import requests

url = "https://github.com/fahmi-g/Rayuan-Image-Classification-API/raw/main/model_final.h5"
response = requests.get(url)
open("latest_model.h5", "wb").write(response.content)

print("Model is successfully pulled.")