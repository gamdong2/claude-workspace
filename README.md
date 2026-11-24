# 🗂️ claude-workspace

Claude Code와 함께 작업하는 **메인 폴더**예요.
마케팅 업무 자동화, 포트폴리오, 작업 기록을 한곳에 모아 둡니다.

---

## 📁 폴더 구조

```
claude-workspace/
├── 📄 CLAUDE.md              ← Claude Code 지침서 (규칙, 소통 방식)
├── 📄 README.md              ← 지금 보는 파일 (폴더 안내)
├── 🚨 SECURITY.md            ← 키 노출 비상 매뉴얼
├── 🙈 .gitignore             ← GitHub에 올리지 않을 파일 목록
│
├── 📂 tasks/                 ← 작업 기록
│   ├── ✅ todo.md            ← 할 일 체크리스트
│   └── 📒 progress.md        ← 한 일 기록 (추가만 해요)
│
├── 📂 scripts/               ← 자동화 스크립트 (Python)
│   ├── 🌤️ weather.py         ← 날씨·미세먼지 → weather.txt 저장
│   └── 💬 send_discord.py    ← weather.txt → 디스코드로 전송
│
├── 📂 portfolio/             ← 포트폴리오 웹페이지
│   └── 🌐 index.html
│
├── 📂 docs/                  ← 참고 문서 (개인정보라 GitHub에는 안 올림)
└── 📕 부록A_GitHub_슬라이드.pdf
```

---

## 🙈 GitHub에 올리지 않는 파일

`.gitignore`에 등록되어 있어서 **내 컴퓨터에만** 있어요.

| 파일 | 이유 |
|---|---|
| `.env` | 🔒 비밀 키·웹훅 주소 보관함 |
| `*recovery-codes*` | 🔒 GitHub 계정 복구 코드 |
| `*.key`, `*.pem`, `id_rsa*` | 🔒 SSH 키·인증서 |
| `docs/resume.pdf`, `docs/sales.csv`, `자기소개서_*.md` | 👤 개인정보 |
| `weather.txt` | 매일 새로 만들어지는 결과물 |
| `*.bak`, `__pycache__/` | 백업·자동 생성 파일 |

---

## 📌 파일별 설명

| 파일 | 무엇인가요? | 언제 보나요? |
|---|---|---|
| `CLAUDE.md` | Claude Code가 매번 읽는 **규칙 모음** | 규칙을 바꾸고 싶을 때 |
| `SECURITY.md` | 키가 새어 나갔을 때 **따라 할 순서** | 🚨 비상시 |
| `tasks/todo.md` | 할 일 | 작업 **시작할 때** |
| `tasks/progress.md` | 지금까지 한 일 | 작업 **끝날 때** 기록 |
| `scripts/` | 매일 자동 실행되는 스크립트 | 자동화를 고칠 때 |
| `portfolio/index.html` | 내 포트폴리오 페이지 | 브라우저로 열어서 보기 |

---

## ⏰ 자동 실행 (Windows 작업 스케줄러)

- 작업 이름: `GwanggyoWeather`
- 매일 오전 9시: `weather.py` 실행 → `send_discord.py`로 디스코드 전송
- 디스코드 웹훅 주소는 `.env`의 `DISCORD_WEBHOOK_URL`에서 읽어요 (코드에 직접 쓰지 않음)

---

## 🔄 하루 작업 흐름

1. **시작:** `tasks/todo.md`에서 할 일 확인
2. **작업:** Claude Code와 한 단계씩 진행
3. **종료:** `tasks/progress.md` 맨 아래에 한 일 기록

---

## 🔒 꼭 기억할 것

- `.env`, `*.key`, `*.pem` 파일은 **아무에게도 보여주지 않아요** (Git에도 올리지 않아요)
- 키가 노출된 것 같으면 → **`SECURITY.md`를 열고** Claude에게 "키 노출 의심"이라고 말해요
