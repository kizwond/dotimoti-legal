# 모티도티 새 서버 계정 삭제 링크 — 2026-11-27

PostgreSQL 새 서버 전환으로 모티도티의 앱 밖 계정 삭제 URL을 `https://220.85.48.155/dotimoti-api/next/account/delete/`로 바꾼다. 앱99의 `MotiPrivacyPublication.deletionUrl`은 실제API base에서 계산한다.

실제 설치99 `MotiPublicPrivacyInstrumentedTest`가7언어20절 본문·시행일·공개URL·삭제URL을 추출했다. `sync_moti_privacy.py`→`build_moti_privacy.py`→`check_moti_privacy.py` 통과. 본문의 수집/목적/보관 범위와 시행일은 변경하지 않고 링크 및 원본 확인 versionCode만 갱신했다. 모티 데이터 삭제 안내의 링크도 동일하게 갱신했다.

모티 앱 소스: https://github.com/kizwond/doti_moti.git / `700e09a`.
서버 소스: https://github.com/kizwond/dotimoti-backend.git / `feat/motidoti-postgres-service`, `4873c35`.
새 API 실제 준비 응답200, 계정 삭제 페이지200을 확인한다. 로그인 없는 요청으로 계정이 삭제되는 구조가 아니며 본인 비밀번호/복구 인증이 필요하다.

두잇 공개 정책·다른 앱 파일과 기존 작업용`.worktrees/`는 이번 커밋에 포함하지 않는다.
