# 📒 작업 기록 (progress)

> 이 파일은 **추가만** 해요. 위의 기록은 지우거나 고치지 않아요.
> 새 기록은 맨 아래에 붙여요.

---

## 2026-11-23 — 작업 환경 구축

**한 일**
1. `tasks/` 폴더와 `todo.md`, `progress.md` 만듦
2. 키 노출 비상 매뉴얼 `SECURITY.md` 작성
3. 폴더 구조 안내 `README.md` 작성

**메모**
- `.env`와 `~/.ssh/oracle-server.key`는 아직 없음 → 나중에 만들 것
- 이 폴더는 아직 Git 저장소가 아님

---

## 2026-11-23 — 연습용 가짜 다운로드 폴더

**한 일**
1. `C:\Users\boar2\fake_downloads` 폴더 생성
2. 연습용 가짜 파일 15개 생성 (이미지 5, 문서 5, 기타 5 / 이름 충돌 테스트용 `photo1 (1).jpg` 포함)

**메모**
- 파일 내용은 한 줄 텍스트라 실제 프로그램으로는 열리지 않음 (분류 연습용)

---

## 2026-11-23 — fake_downloads 폴더 정리

**한 일**
1. 백업: `C:\Users\boar2\fake_downloads_backup` (15개, 원본과 동일 확인)
2. `images/` 5개, `docs/` 5개, `misc/` 5개로 분류 (덮어쓰지 않는 방식 `mv -n` 사용)
3. 확인: 루트에 남은 파일 0개, 덮어쓴 파일 없음

---

## 2026-11-23 — 백업 폴더 삭제

**한 일**
1. `C:\Users\boar2\fake_downloads_backup` 삭제 (사용자 확인 후, 원본 15개와 동일한지 먼저 확인)
2. 정리된 `fake_downloads` 15개는 그대로 유지

---

## 2026-11-23 — IT 마케팅 자기소개서 초안

**한 일**
1. `resume_sample.pdf`(샘플 인물 김수민) 기반 자기소개서 초안 작성
2. 저장: `자기소개서_IT마케팅_초안.md` (공백 포함 803자 / 제외 629자)

**메모**
- `[회사명]`, `[제품/서비스]` 채워 넣어야 함

---

## 2026-11-23 — 매출 CSV 분석

**한 일**
1. `docs/sales.csv` (66건, 2026-01~03) 월별 추이, 상품 TOP 5, 이상치 분석
2. 이상치 발견: ORD-2026-0059 매출 5,000,000 (수량1×단가129,000과 불일치) → 원본 확인 필요

---

## 2026-11-24 — 강남구 날씨·미세먼지 자동 저장

**한 일**
1. `scripts/weather.py` 작성 (Open-Meteo, API 키 없음, 표준 라이브러리만)
2. 결과 `weather.txt`에 덮어쓰기 저장 (실패 시 기존 파일 유지 + `weather_error.log` 기록)
3. 작업 스케줄러 `GangnamWeather` 등록: 매일 09:00, 놓친 실행은 켜진 뒤 보충
4. 직접 실행 + 스케줄러 즉시 실행 모두 성공 확인 (결과코드 0)

**메모**
- 미세먼지는 모델 추정치 (에어코리아 측정값 아님)
- 해제: `Unregister-ScheduledTask -TaskName GangnamWeather`

---

## 2026-11-24 — 날씨 위치 변경: 강남구 → 용인/광교

**한 일**
1. `scripts/weather.py` 백업 → `weather.py.bak`
2. 좌표를 광교중앙역 부근(37.2886, 127.0517)으로, 표시 이름을 "용인/광교"로 변경
3. 실행 확인 (종료코드 0, weather.txt 갱신)

**메모**
- 스케줄러 작업 이름은 아직 `GangnamWeather` (같은 스크립트를 실행하므로 내일 9시부터 광교 날씨로 저장됨)

---

## 2026-11-24 — 날씨 디스코드 전송

**한 일**
1. `.env` 생성 (DISCORD_WEBHOOK_URL — Yura가 직접 입력, 화면/로그에 노출 안 함)
2. 새 파일 `scripts/send_discord.py` 작성 (오늘 날짜 아니면 전송 안 함, 오류 시 주소 마스킹)
3. 수동 테스트 전송 성공 (HTTP 204, Yura가 채널 수신 확인)
4. 스케줄러 `GwanggyoWeather` 등록: 매일 09:00 weather.py → send_discord.py
5. 스케줄러 즉시 실행 성공 (결과코드 0, 오류 로그 0줄) → 예전 `GangnamWeather` 삭제

**메모**
- 해제: `Unregister-ScheduledTask -TaskName GwanggyoWeather`
- 웹훅 노출 의심 시: 디스코드 채널 편집 → 연동 → 웹후크에서 삭제 후 새로 만들기

---

## 2026-11-24 — 포트폴리오 웹페이지

- 새 파일 `portfolio/index.html` 작성 (HTML+CSS 한 파일, 설치 필요 없음)
- 내용: 이름 Yura(사용자 선택) + 이력서(`docs/resume.pdf`)의 직무·소개·경력·스킬·연락처
- 경력 3개: 테크노바, 리브랜드(이력서) + 브릿지애드 인턴(임의 작성 예시)
- 이력서 워터마크의 개인 이메일은 페이지에 넣지 않음
- 확인: Edge 헤드리스 스크린샷으로 PC(1280px)·휴대폰(390px) 레이아웃 확인, 다크모드 자동 적용

## 2026-11-24 — GitHub CLI(gh) 설치

- winget으로 `GitHub.cli` 설치 (v2.105.0, 위치: `C:\Program Files\GitHub CLI\gh.exe`)
- 확인: `gh --version` 실행 성공
- 남은 일: 새 터미널에서 `gh auth login`으로 GitHub 로그인 (Yura가 직접)

## 2026-11-24 — GitHub private 레포 업로드

- 새 파일 `.gitignore`: `.env`, 키·인증서, `*recovery-codes*`, 개인정보(이력서·sales.csv·자기소개서), `*.bak`, `__pycache__/`, `weather.txt` 제외
- `README.md` 폴더 구조 최신화 (예전 버전은 `README.md.bak`)
- `git init` → 커밋 `Initial setup` → `gh repo create`로 private 레포 생성·push
- 주소: https://github.com/gamdong2/claude-workspace
- 확인: 공개 설정 PRIVATE, GitHub에 올라간 파일 10개 중 `.env`·복구 코드·개인정보 파일 없음

## 2026-11-24 — 포트폴리오 다크모드 전환 버튼

- 브랜치 `feature/dark-mode-toggle`에서 `portfolio/index.html` 수정
  - 윈도우 설정 자동 따라가기 → 🌙/☀️ 버튼으로 전환 (기본 다크, 고른 모드는 브라우저 localStorage에 저장)
- 확인: Edge 헤드리스로 다크(기본)·라이트(클릭 후) PC 캡처, 390px iframe으로 휴대폰 레이아웃 확인 (넘침 없음)
  - 참고: 헤드리스 Edge는 창 너비를 약 500px 아래로 못 줄임 → 휴대폰 확인은 iframe으로 해야 정확
- main에 머지(`5939533`) → GitHub push, GitHub main과 로컬 main 일치 확인

## 2026-11-25 — 부록B PDF GitHub 업로드

- `pypdf` 설치(PDF 글자 추출용) → `부록B_Vercel_슬라이드.pdf`(15쪽) 텍스트 검사: 키·웹훅·이메일·전화 0건
- 참고: 슬라이드 속 이미지(스크린샷) 내용은 글자 검사로 확인 불가
- 커밋 `Add Appendix B Vercel slides` → push, GitHub main에 파일 있는 것 확인
