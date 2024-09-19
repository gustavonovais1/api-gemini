import PIL.Image, os
import google.generativeai as genai
API_KEY = os.getenv('api_key')

genai.configure(api_key=API_KEY)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro-vision')

img = PIL.Image.open('image.png')

response = model.generate_content(img)

print("Resposta 1:", response.text)

response = model.generate_content(["Faça uma análise do grafico da imagem", img])
response.resolve()

print("Resposta da pergunta", response.text)