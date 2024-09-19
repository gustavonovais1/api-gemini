import os
import google.generativeai as genai
API_KEY = os.getenv('api_key')

data = {
  "series": [
    "2024-03-01",
    "2024-03-02",
    "2024-03-03",
    "2024-03-04",
    "2024-03-05",
    "2024-03-06",
    "2024-03-07",
    "2024-03-08",
    "2024-03-09",
    "2024-03-10",
    "2024-03-11",
    "2024-03-12",
    "2024-03-13",
    "2024-03-14",
    "2024-03-15",
    "2024-03-16",
    "2024-03-17",
    "2024-03-18",
    "2024-03-19",
    "2024-03-20",
    "2024-03-21",
    "2024-03-22",
    "2024-03-23",
    "2024-03-24"
  ],
  "values": {
    "Impressions": {
      "2024-03-01": 8246,
      "2024-03-02": 0,
      "2024-03-03": 0,
      "2024-03-04": 8723,
      "2024-03-05": 0,
      "2024-03-06": 4762,
      "2024-03-07": 75565,
      "2024-03-08": 22711,
      "2024-03-09": 0,
      "2024-03-10": 0,
      "2024-03-11": 22297,
      "2024-03-12": 34760,
      "2024-03-13": 26106,
      "2024-03-14": 17347,
      "2024-03-15": 13224,
      "2024-03-16": 0,
      "2024-03-17": 0,
      "2024-03-18": 82800,
      "2024-03-19": 58785,
      "2024-03-20": 58862,
      "2024-03-21": 30751,
      "2024-03-22": 29682,
      "2024-03-23": 0,
      "2024-03-24": 0
    }
  }
}

genai.configure(api_key=API_KEY)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content(f"Olá você poderia analisar dados em json desse grafico e explicar de forma analitica as metricas, veja os dados {data}", stream=True)

for chunk in response:
    print(chunk.text)
    print("_"*80)