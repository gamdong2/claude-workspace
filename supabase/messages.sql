-- ============================================
-- 방명록 테이블: messages
-- Supabase 대시보드 → SQL Editor → 붙여넣고 Run
-- ============================================

-- 1) 테이블
create table if not exists public.messages (
  id          bigint generated always as identity primary key,
  name        text        not null check (char_length(btrim(name)) between 1 and 30),
  content     text        not null check (char_length(btrim(content)) between 1 and 500),
  created_at  timestamptz not null default now()
);

-- 최신 글부터 빠르게 불러오기
create index if not exists messages_created_at_idx on public.messages (created_at desc);

-- 2) RLS 켜기: 아래 정책으로 허용한 것만 가능
alter table public.messages enable row level security;

-- 누구나 읽기
drop policy if exists "messages_read_all" on public.messages;
create policy "messages_read_all"
  on public.messages for select
  to anon, authenticated
  using (true);

-- 누구나 쓰기
drop policy if exists "messages_insert_all" on public.messages;
create policy "messages_insert_all"
  on public.messages for insert
  to anon, authenticated
  with check (true);

-- 수정·삭제 정책은 일부러 없음 → 방문자는 고치거나 지울 수 없음
-- (관리는 Supabase 대시보드 Table Editor에서)

-- 3) 권한: 읽기는 전체, 쓰기는 name·content만 (작성시간·번호 조작 방지)
revoke all on public.messages from anon, authenticated;
grant select on public.messages to anon, authenticated;
grant insert (name, content) on public.messages to anon, authenticated;
