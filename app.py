import streamlit as st
import requests

st.set_page_config(page_title="실시간 날씨", layout="centered")
st.title("🌤️ 실시간 날씨 확인")

# 1. IP 위치 추정
ipinfo = requests.get("https://ipinfo.io/json").json()
loc = ipinfo["loc"]
lat, lon = loc.split(',')

st.markdown(f"**🌍 위치 추정:** {ipinfo['city']}, {ipinfo['country']}")
st.write(f"위도: {lat}, 경도: {lon}")

# 2. 날씨 API 요청
API_KEY = "38074004a1479432e7b285767a9b8cf4"
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=kr"
res = requests.get(url).json()

# 3. 출력
st.subheader("📡 현재 날씨 정보")
weather = res['weather'][0]['description']
temp = res['main']['temp']
feels = res['main']['feels_like']
humidity = res['main']['humidity']
wind = res['wind']['speed']

st.write(f"🌡️ 온도: {temp}°C (체감 {feels}°C)")
st.write(f"💧 습도: {humidity}%")
st.write(f"🌬️ 바람: {wind} m/s")
st.write(f"☁️ 상태: {weather}")
