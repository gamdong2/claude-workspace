"""weather.txt 내용을 디스코드 채널로 보내기 (웹훅 사용).

- 웹훅 주소는 claude-workspace/.env 의 DISCORD_WEBHOOK_URL 에서만 읽음
  (코드에 주소를 직접 쓰지 않음, 화면/로그에도 주소를 남기지 않음)
- weather.txt 가 오늘 날짜가 아니면(날씨 가져오기 실패) 전송하지 않음
- 실패 내용은 weather_error.log 에 기록
"""
import json
import os
import re
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # claude-workspace
ENV_FILE = BASE_DIR / ".env"
WEATHER_FILE = BASE_DIR / "weather.txt"
ERR_FILE = BASE_DIR / "weather_error.log"

WEBHOOK_PREFIXES = (
    "https://discord.com/api/webhooks/",
    "https://discordapp.com/api/webhooks/",
)


def log_error(msg):
    with open(ERR_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now():%Y-%m-%d %H:%M}] 디스코드 전송 실패: {msg}\n")
    print("실패:", msg)
    raise SystemExit(1)


def mask(text, secret):
    """오류 메시지에 웹훅 주소가 섞여 나오지 않도록 가리기"""
    return text.replace(secret, "https://discord.com/api/webhooks/***") if secret else text


def load_webhook_url():
    url = os.environ.get("DISCORD_WEBHOOK_URL", "").strip()
    if not url and ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8-sig").splitlines():
            line = line.strip()
            if line.startswith("DISCORD_WEBHOOK_URL="):
                url = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not url:
        log_error(".env 의 DISCORD_WEBHOOK_URL 이 비어 있어요.")
    if not url.startswith(WEBHOOK_PREFIXES):
        log_error("DISCORD_WEBHOOK_URL 이 디스코드 웹훅 주소 형식이 아니에요.")
    return url


def build_message():
    if not WEATHER_FILE.exists():
        log_error("weather.txt 가 없어요.")
    lines = WEATHER_FILE.read_text(encoding="utf-8").strip().splitlines()

    # 첫 줄 예: [2026-11-24 12:50] 용인/광교
    m = re.match(r"\[(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2})\] (.+)", lines[0] if lines else "")
    if not m:
        log_error("weather.txt 형식을 읽을 수 없어요.")
    date, time, place = m.groups()
    if date != datetime.now().strftime("%Y-%m-%d"):
        log_error(f"weather.txt 가 오늘 정보가 아니에요({date}). 어제 정보는 보내지 않아요.")

    body = "\n".join(l for l in lines[1:] if not l.startswith("(출처"))
    return f"🌤️ **{place} 아침 날씨** ({date} {time})\n{body}\n-# 출처: Open-Meteo · 미세먼지는 모델 추정치"


def send(url, content):
    data = json.dumps({"content": content}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "User-Agent": "DiscordBot (local-weather-script, 1.0)",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        hint = {401: "웹훅 주소가 틀렸어요", 404: "웹훅이 삭제됐거나 주소가 틀렸어요",
                429: "너무 자주 보냈어요. 잠시 후 다시"}.get(e.code, "")
        log_error(mask(f"HTTP {e.code} {hint}".strip(), url))
    except Exception as e:
        log_error(mask(repr(e), url))


def main():
    url = load_webhook_url()
    content = build_message()
    status = send(url, content)
    print(f"전송 성공 (HTTP {status})")


if __name__ == "__main__":
    main()
