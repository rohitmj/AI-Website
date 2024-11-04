import google.generativeai as genai

api_key = "AIzaSyB9mamI7Qffu5Pd3GnP8dJAgWBTcvMERx0"
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("how to make the cat learn")
print(response.text)
