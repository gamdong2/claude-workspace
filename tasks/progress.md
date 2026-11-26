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

## 2026-11-25~26 — Vercel 설정

- Vercel CLI 66.6.0 전역 설치 (`npm install --global vercel@latest`)
- `vercel login` 실패 원인: 컴퓨터 이름이 한글(`유라의_그램_프로16`)이라 요청 헤더에 넣을 수 없음 (`ByteString` 에러)
  → Yura가 컴퓨터 이름을 `yura-s-gram-pro16`으로 바꾸고 재부팅 → `gamdong2`로 로그인 성공
- Vercel 플러그인(v0.56.0)과 Vercel MCP는 이미 설치돼 있음. MCP 승인(OAuth)은 보류
- 포트폴리오 배포는 Yura가 직접 하기로 함. 안내한 것: Root Directory `portfolio` 필수(안 하면 CLAUDE.md 등 공개됨), 연락처가 예시 정보(soomin)
- 추천: Vercel 2FA 켜기

## 2026-11-26 — Vercel GUI 배포용 세팅

- 루트에 `vercel.json`: `framework: null`, 빌드·설치 없음, `outputDirectory: "portfolio"` → Vercel에서 Import 후 Deploy만 누르면 portfolio만 공개
- `.gitignore`에 `.vercel/` 추가
- 확인: 임시 복사본에서 `vercel build` 성공, 결과물은 `index.html` 1개 (CLAUDE.md·tasks 없음)
- 근거 문서: vercel.com/docs/project-configuration/vercel-json, /docs/builds/configure-a-build

## 2026-11-26 — CLI(`vercel --prod`) 배포용 세팅

- `.vercelignore` 허용 목록: `portfolio/`, `vercel.json`만 Vercel에 업로드 (없으면 .env·복구 코드까지 업로드됨 — Vercel 문서 확인)
- Vercel 프로젝트 `yura-portfolio`(팀 yura-8dbd) 생성 + `vercel link` → `.vercel/project.json`
  - Vercel이 `.env.local`(VERCEL_OIDC_TOKEN) 생성 + `.gitignore`에 `.vercel`, `.env*` 자동 추가
- GitHub 자동 배포: Not connected (푸시해도 공개 배포 안 됨)
- `vercel build` 성공, 결과물 index.html 1개
- `.gitignore`: `.vercel/*` 제외 + `!.vercel/project.json`만 허용 → project.json만 GitHub에
- 배포 명령 (Yura): `vercel --prod` (claude-workspace 폴더에서)

## 2026-11-26 — 포트폴리오 다크 배경 검정 → 남색

- 다크 모드 색 변경: 배경 #121415→#0f1b33, 카드 #1a1d1f→#16264a, 테두리 #2b2f32→#263a63, 강조 배경 #17312e→#163a4a (라이트 모드는 그대로)
- 확인: Edge 캡처, 글자 대비 본문 14.3 · 회색 글씨 6.0~6.9 · 강조색 9.2 (기준 4.5 이상)

## 2026-11-26 — Vercel 프로젝트 정리 (yura-portfolio 삭제)

- 원인: Yura가 GUI로 만든 `claude-workspace`(GitHub 연결, main 푸시 시 자동 배포)와 내가 CLI로 만든 `yura-portfolio`(빈 프로젝트)가 따로 있었음
  - 내가 "자동 배포 꺼짐"이라고 한 건 yura-portfolio만 보고 한 잘못된 안내였음
- `.vercel/project.json` 백업(`.vercel/project.json.bak`) → `vercel link --project claude-workspace`로 다시 연결
- `vercel project rm yura-portfolio --confirm-name yura-portfolio`로 삭제 → 남은 프로젝트: claude-workspace 1개
- 이제 GitHub 푸시 = 자동 배포, `vercel --prod` = 같은 사이트 배포
- 공개 사이트 노출 검사: CLAUDE.md·SECURITY.md·tasks·.env·복구 코드 모두 404

## 2026-11-26 — 포트폴리오 방명록 (Supabase, 로컬)

- `supabase/messages.sql`: messages(id, name 1~30자, content 1~500자, created_at) + RLS 읽기·쓰기 허용, 수정·삭제 정책 없음, insert는 name·content 칼럼만 → Yura가 SQL Editor에서 실행
- `.env.local`에 SUPABASE_URL, SUPABASE_ANON_KEY 추가 (백업 `.env.local.bak`, 둘 다 GitHub 제외)
- `scripts/build-config.mjs`: .env.local → `portfolio/config.js` (gitignore), service_role 키면 중단
- `portfolio/index.html`: 맨 아래 방명록 폼+목록, 메뉴 링크, textContent로 XSS 방지, 설정 없으면 "준비 중"
- 테스트: 읽기 200, 쓰기 201, 작성시간 조작 401, 빈 이름 400, 수정·삭제 42501(막힘)
  - 첫 쓰기 테스트 400 원인: 윈도우 터미널이 curl 인자의 한글을 깨뜨림 (브라우저는 문제없음) → UTF-8 파일로 보내 해결
  - 테스트 글 2개(enc-test, Claude 테스트) DB에 남아 있음
- 로컬 서버: `python -m http.server 3000 --bind 127.0.0.1 -d portfolio` → http://127.0.0.1:3000/#guestbook
- GitHub 푸시 안 함
