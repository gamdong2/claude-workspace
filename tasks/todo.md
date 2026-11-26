# ✅ 오늘 할 일

> 작업 시작할 때 Claude Code가 이 파일을 먼저 확인해요.
> 끝난 항목은 `[x]`로 체크하고, 다 끝나면 `progress.md`에 기록해요.

---

## 2026-11-23 — 작업 환경 구축

- [x] `tasks/` 폴더 + `todo.md`, `progress.md` 만들기
- [x] `SECURITY.md` 비상 매뉴얼 쓰기
- [x] `README.md` 폴더 구조 안내 쓰기

## 2026-11-23 — fake_downloads 정리 (✅ 완료)

- [x] 1. 백업: `fake_downloads` 전체를 `fake_downloads_backup`으로 복사
- [x] 2. `images/`, `docs/`, `misc/` 폴더 만들기
- [x] 3. 이미지 5개 → `images/` (jpg, png, gif, webp)
- [x] 4. 문서 5개 → `docs/` (pdf, docx, xlsx, txt, pptx)
- [x] 5. 나머지 5개 → `misc/` (exe, zip, mp3, mp4, json)
- [x] 6. 확인: 개수 15개 맞는지, 남은 파일 없는지, 백업 그대로인지

## 2026-11-24 — 강남구 날씨·미세먼지 자동 저장 (✅ 완료)

- [x] 1. 스크립트 작성: `scripts/weather.py` (Open-Meteo, 키 없음, 추가 설치 없음)
- [x] 2. 직접 한 번 실행 → `weather.txt` 내용 확인
- [x] 3. Windows 작업 스케줄러에 "매일 오전 9시" 등록
- [x] 4. 스케줄러로 즉시 1회 실행해서 자동 실행도 되는지 확인
- [x] 5. 끄는 방법(등록 해제) 안내 + progress 기록

## 2026-11-24 — 날씨 디스코드 전송 (용인/광교, ✅ 완료)

- [x] 0. (Yura) 디스코드에서 웹훅 만들기 → `.env`에 직접 붙여넣기
- [x] 1. `.env` 빈 틀 만들기 (`DISCORD_WEBHOOK_URL=`)
- [x] 2. 새 파일 `scripts/send_discord.py` 작성 (weather.txt 읽어서 전송, `weather.py`는 그대로)
- [x] 3. 직접 실행 → 디스코드 채널에 메시지 왔는지 Yura가 확인
- [x] 4. 스케줄러 `GwanggyoWeather`로 새로 등록 (날씨 저장 → 디스코드 전송), 예전 `GangnamWeather` 삭제
- [x] 5. 스케줄러로 즉시 1회 실행해서 확인 + progress 기록

## 2026-11-24 — 포트폴리오 웹페이지 (✅ 완료)

- [x] 1. 새 폴더 `portfolio/` + 파일 1개 `portfolio/index.html` 만들기 (CSS 포함, 외부 설치 없음)
- [x] 2. 내용 채우기
  - 상단: 이름 · 직업(Marketing Specialist) · 한 줄 소개 + 숫자 성과 3개 (CPL -38%, 오가닉 2.3배, 팔로워 12만)
  - 자기소개: 이력서 내용 요약 (B2B SaaS 그로스, 데이터 기반 마케팅, AI 자동화)
  - 경력 3개: 테크노바(이력서) / 리브랜드(이력서) / 마케팅 인턴 1개(임의로 만든 내용)
  - 스킬 태그 (이력서 보유 스킬 표)
  - 연락처: 이메일 · 전화 · LinkedIn (이력서 본문 예시 정보만, 워터마크 정보는 제외)
- [x] 3. 반응형 확인 (휴대폰 너비에서 1열로 바뀌는지)
- [x] 4. 브라우저로 열기 → Yura가 화면 확인
- [x] 5. todo 체크 + progress 기록

## 2026-11-24 — GitHub private 레포 업로드 (✅ 완료)

- [x] 1. `.gitignore` 만들기 — `.env`, `*.key`, `*.pem`, `id_rsa*`, `*credentials*`, `*recovery-codes*`, `*.bak`, `__pycache__/` 제외 (+ Yura가 고른 개인정보 파일)
- [x] 2. `README.md`를 현재 폴더 구조에 맞게 정리 (기존 파일은 `README.md.bak`으로 백업)
- [x] 3. `git init` → `git add` → **올라갈 파일 목록을 Yura에게 보여주고 확인** (민감 파일 없는지)
- [x] 4. 첫 커밋: `Initial setup`
- [x] 5. `gh repo create`로 **private** 레포 생성 + push
- [x] 6. GitHub에서 private인지, `.env`·복구 코드가 없는지 확인 + progress 기록

## 2026-11-24 — 포트폴리오 다크모드 전환 버튼 (✅ 완료)

- [x] 0. main에서 지난 기록(todo·progress) 커밋 + push
- [x] 1. 새 브랜치 `feature/dark-mode-toggle` 만들기 (main은 그대로 둠)
- [x] 2. `portfolio/index.html`에 🌙/☀️ 버튼 추가 — 기본은 다크, 누르면 라이트, 고른 모드는 브라우저가 기억
- [x] 3. 확인: 다크·라이트 화면 캡처 + 버튼이 실제로 바뀌는지 확인
- [x] 4. 브랜치에 커밋 → main에 머지 → GitHub에 push
- [x] 5. GitHub main에 반영됐는지 확인 + progress 기록

## 2026-11-25 — Vercel 설정 (🟡 거의 완료 — MCP 승인만 남음)

> 참고: https://vercel.com/get-started.md (설정만, 배포·프로젝트 연결은 이번에 안 함)

- [x] 1. Vercel CLI 설치: `npm install --global vercel@latest` → `vercel --version`으로 확인
- [x] 2. 로그인: `vercel login` → **Yura가 브라우저에서 직접 로그인** → `vercel whoami`로 확인
  - 처음엔 한글 컴퓨터 이름 때문에 `ByteString` 에러 → 컴퓨터 이름을 `yura-s-gram-pro16`으로 바꾸고 재부팅 → `gamdong2`로 로그인 성공
- [x] 3. Vercel 플러그인: `vercel@claude-plugins-official` v0.56.0 이미 설치됨 (Claude Code 권유로 설치)
- [x] 4. Vercel MCP: 플러그인에 포함 (`https://mcp.vercel.com`) → 따로 추가 안 함
- [ ] 5. (선택) **Yura가 `/mcp`에서 Vercel 로그인(승인)** — 배포를 직접 하므로 보류 → 읽기 전용 `list_teams`로 연결 확인
- [x] 6. 결과 정리 + progress 기록
- [ ] 7. (Yura) 포트폴리오 배포 — Root Directory는 반드시 `portfolio`


## 다음에 할 일 (아이디어)

- [ ] `.env` 파일 만들고 API 키 넣기 (직접 입력, Claude에게 키를 보여주지 않기)
- [x] `.gitignore` 만들기 (`.env`, `*.key`, `*.pem` 같은 파일이 실수로 Git에 올라가지 않게)
- [ ] 오라클 SSH 키(`~/.ssh/oracle-server.key`) 연결 확인

---

<!-- 형식 예시
## YYYY-MM-DD — 작업 제목
- [ ] 할 일 1
- [ ] 할 일 2
-->

## 2026-11-26 — GitHub 레포를 Vercel GUI로 바로 배포할 수 있게 세팅

- [x] 1. 루트에 `vercel.json` (`outputDirectory: "portfolio"`, `framework: null`, 빌드 없음) → portfolio만 공개
- [x] 2. `.gitignore`에 `.vercel` 추가
- [x] 3. 임시 복사본에서 `vercel build`로 결과물에 portfolio 파일만 있는지 확인
- [ ] 4. 커밋 + push → Yura가 Vercel에서 Import → Deploy

## 2026-11-26 — CLI(`vercel --prod`) 배포용 세팅

- [x] 1. `.vercelignore` 허용 목록: `portfolio/`, `vercel.json`만 Vercel에 업로드 (`.env`·복구 코드 업로드 차단)
- [x] 2. Vercel 프로젝트 `yura-portfolio` 만들기 + `vercel link` → `.vercel/project.json` 생성 (배포는 안 함)
- [x] 3. GitHub 자동 배포가 켜졌는지 확인 (켜졌으면 꺼서 푸시해도 공개 안 되게)
- [x] 4. `vercel build`로 결과물에 index.html만 있는지 확인
- [x] 5. `.gitignore` 조정: `.vercel/project.json`만 GitHub에 올리고 나머지(.env·빌드 결과)는 계속 제외 → 커밋 + push

## 2026-11-26 — 포트폴리오 다크 배경 검정 → 남색

- [x] 1. 다크 모드 색 4개(배경·카드·테두리·강조 배경)를 남색 계열로 변경
- [x] 2. 다크·라이트 화면 캡처로 확인
- [x] 3. 커밋 + push (GitHub 자동 배포는 꺼져 있어 사이트에는 반영 안 됨)

## 2026-11-26 — 포트폴리오 방명록 (Supabase) (✅ 로컬 완료)

- [x] 1. `supabase/messages.sql` 작성: messages(id, name, content, created_at) + RLS(누구나 읽기·쓰기) + 작성시간 조작 방지 → **Yura가 SQL Editor에서 실행**
- [x] 2. `.env.local`에 `SUPABASE_URL`, `SUPABASE_ANON_KEY` 추가 (기존 VERCEL_OIDC_TOKEN 유지), GitHub 제외 확인
- [x] 3. `scripts/build-config.mjs`: `.env.local` → `portfolio/config.js` 생성 (config.js는 .gitignore)
- [x] 4. `portfolio/index.html` 맨 아래 방명록 폼 + 리스트 (textContent로 XSS 방지, 설정 없으면 안내 문구)
- [x] 5. 로컬 테스트: `config.js` 생성 → 로컬 서버(`python -m http.server`) → 글 읽기·쓰기 확인 (테스트 글 1개 작성)
- [x] 6. progress 기록 (**GitHub 푸시 안 함** — 푸시하면 자동 배포됨. Vercel 환경변수 설정은 다음 단계)
- [x] 7. Vercel 배포 사이트에도 방명록 켜기: Vercel 환경변수 등록 + `vercel.json` buildCommand로 config.js 생성
