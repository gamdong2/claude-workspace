// .env.local(로컬) 또는 환경변수(Vercel)에서 Supabase 정보를 읽어
// portfolio/config.js 를 만들어요. config.js 는 GitHub에 올리지 않아요(.gitignore).
//
// 사용법:  node scripts/build-config.mjs

import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const envFile = join(root, ".env.local");
const outFile = join(root, "portfolio", "config.js");

// .env.local 읽기 (있으면). 이미 설정된 환경변수가 우선.
const env = {};
if (existsSync(envFile)) {
  for (const line of readFileSync(envFile, "utf8").split(/\r?\n/)) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*"?([^"]*)"?\s*$/);
    if (m) env[m[1]] = m[2];
  }
}
const url = process.env.SUPABASE_URL || env.SUPABASE_URL || "";
const anonKey = process.env.SUPABASE_ANON_KEY || env.SUPABASE_ANON_KEY || "";

// 실수로 관리자 키(service_role)를 넣으면 멈춤 — 웹페이지에 들어가면 안 되는 키
try {
  const payload = JSON.parse(Buffer.from(anonKey.split(".")[1] || "", "base64url").toString());
  if (payload.role && payload.role !== "anon") {
    console.error(`🚨 SUPABASE_ANON_KEY의 role이 "${payload.role}"이에요. anon 키만 넣어주세요.`);
    process.exit(1);
  }
} catch {
  // 새 형식(sb_publishable_...) 키는 JWT가 아니라 검사 생략
}
if (anonKey.startsWith("sb_secret_")) {
  console.error("🚨 secret 키예요. publishable/anon 키만 넣어주세요.");
  process.exit(1);
}

writeFileSync(
  outFile,
  "// 자동 생성 파일 (scripts/build-config.mjs) — 직접 고치지 마세요\n" +
    `window.SUPABASE_CONFIG = ${JSON.stringify({ url, anonKey })};\n`
);

const mask = (s) => (s ? s.slice(0, 8) + "***" : "(비어 있음)");
console.log(`✅ portfolio/config.js 생성 — URL: ${mask(url)}, anon key: ${mask(anonKey)}`);
if (!url || !anonKey) console.log("⚠️ 값이 비어 있어요. 방명록은 '준비 중' 안내만 보여요.");
