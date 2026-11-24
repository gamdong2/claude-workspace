"""용인/광교 날씨 + 미세먼지를 가져와 weather.txt에 저장 (덮어쓰기).

- 데이터: Open-Meteo (무료, API 키 불필요)
- 추가 설치 없음 (파이썬 기본 기능만 사용)
- 실패하면 기존 weather.txt는 그대로 두고 weather_error.log에 기록
"""
import json
import os
import urllib.request
from datetime import datetime
from pathlib import Path

# 광교중앙역 부근 좌표 (수원 영통구·용인 수지구 경계)
LAT, LON = 37.2886, 127.0517
PLACE = "용인/광교"

BASE_DIR = Path(__file__).resolve().parent.parent  # claude-workspace
OUT_FILE = BASE_DIR / "weather.txt"
ERR_FILE = BASE_DIR / "weather_error.log"

WEATHER_URL = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={LAT}&longitude={LON}"
    "&current=temperature_2m,apparent_temperature,relative_humidity_2m,"
    "precipitation,weather_code,wind_speed_10m"
    "&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max"
    "&timezone=Asia%2FSeoul&forecast_days=1"
)
AIR_URL = (
    "https://air-quality-api.open-meteo.com/v1/air-quality"
    f"?latitude={LAT}&longitude={LON}&current=pm10,pm2_5&timezone=Asia%2FSeoul"
)

# WMO 날씨 코드 → 한국어
WEATHER_CODES = {
    0: "맑음", 1: "대체로 맑음", 2: "구름 조금", 3: "흐림",
    45: "안개", 48: "짙은 안개",
    51: "약한 이슬비", 53: "이슬비", 55: "강한 이슬비",
    56: "약한 어는 이슬비", 57: "어는 이슬비",
    61: "약한 비", 63: "비", 65: "강한 비",
    66: "약한 어는 비", 67: "어는 비",
    71: "약한 눈", 73: "눈", 75: "강한 눈", 77: "싸락눈",
    80: "약한 소나기", 81: "소나기", 82: "강한 소나기",
    85: "약한 눈소나기", 86: "강한 눈소나기",
    95: "뇌우", 96: "우박 동반 뇌우", 99: "강한 우박 동반 뇌우",
}


def grade(value, limits):
    """환경부 기준 등급. limits = (좋음 상한, 보통 상한, 나쁨 상한)"""
    if value is None:
        return "정보 없음"
    good, normal, bad = limits
    if value <= good:
        return "좋음"
    if value <= normal:
        return "보통"
    if value <= bad:
        return "나쁨"
    return "매우나쁨"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "weather-script"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def build_report():
    w = fetch(WEATHER_URL)
    a = fetch(AIR_URL)
    cur, day, air = w["current"], w["daily"], a["current"]

    sky = WEATHER_CODES.get(cur["weather_code"], f"코드 {cur['weather_code']}")
    pm10, pm25 = air.get("pm10"), air.get("pm2_5")
    pm10_txt = f"{pm10:.0f}㎍/㎥ ({grade(pm10, (30, 80, 150))})" if pm10 is not None else "정보 없음"
    pm25_txt = f"{pm25:.0f}㎍/㎥ ({grade(pm25, (15, 35, 75))})" if pm25 is not None else "정보 없음"

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    return (
        f"[{now}] {PLACE}\n"
        f"날씨: {sky} | 기온 {cur['temperature_2m']}°C "
        f"(체감 {cur['apparent_temperature']}°C) | 습도 {cur['relative_humidity_2m']}% "
        f"| 바람 {cur['wind_speed_10m']}km/h\n"
        f"오늘: 최저 {day['temperature_2m_min'][0]}°C / 최고 {day['temperature_2m_max'][0]}°C "
        f"| 강수확률 {day['precipitation_probability_max'][0]}%\n"
        f"미세먼지 PM10: {pm10_txt} | 초미세먼지 PM2.5: {pm25_txt}\n"
        f"(출처: Open-Meteo, 미세먼지는 모델 추정치)\n"
    )


def main():
    try:
        report = build_report()
    except Exception as e:  # 실패 시 기존 weather.txt 보존
        with open(ERR_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now():%Y-%m-%d %H:%M}] 실패: {e!r}\n")
        raise SystemExit(1)

    # 임시 파일에 먼저 쓰고 바꿔치기 → 쓰는 도중 문제가 생겨도 기존 파일이 깨지지 않음
    tmp = OUT_FILE.with_suffix(".tmp")
    tmp.write_text(report, encoding="utf-8")
    os.replace(tmp, OUT_FILE)
    print(report)


if __name__ == "__main__":
    main()
