# DotiDoit Legal Pages

도티두잇(DotiDoit, Android package `com.doti.doit`)의 공개 개인정보처리방침입니다.
운영자: **opensky**. 개인정보 문의: **eonseok.yoon@opensky.co.kr**.

저장소 이름 `dotimoti-legal`은 유지하지만 현재 게시된 방침의 대상은 도티모티가 아니라 **도티두잇**입니다.

## Google Play에 입력할 공개 URL

https://kizwond.github.io/dotimoti-legal/dotidoit/privacy/

GitHub Pages의 `main` / root 배포를 사용합니다. 공식 주소는 `dotidoit/privacy/`입니다. 이전 `dotitimer/privacy/` 주소는 새 주소로 자동 이동하며, 자동 이동을 지원하지 않는 환경을 위한 링크도 제공합니다. 기존 링크 호환성을 위해 이전 경로를 삭제하지 마세요.

## 정책 범위

- 미션·수행툴·사진·메모·위치·건강 데이터의 로컬 보관과 사용자 선택에 따른 처리.
- Health Connect의 심박·걸음·거리·활동 및 총 칼로리 읽기, 선행 구간 기록 조회, 출처·품질 정보.
- 장소·시간·NFC 도우미, 백그라운드 위치 기능, 카메라·알림 및 수행 관련 권한.
- 공인미션/이미지·업데이트 통신, OpenStreetMap 지도, Amazon S3 지형 타일, 선택형 DotiMoti 연동.
- ZIP 백업·기기 백업·공유·삭제의 범위와 이미 외부로 복사된 데이터의 별도 관리.

로컬 우선이라는 이유만으로 Play의 데이터 보안 항목에 모두 ‘수집 없음’이라고 답하지 마세요. 실제 출시 AAB, 포함 SDK, 네트워크 요청, 선택형 공유 및 Google의 정의를 확인해 별도로 작성해야 합니다. 이 문서 갱신만으로 모든 정책 심사를 통과했다는 뜻은 아닙니다.

## 앱 내부와 동기화

한국어·영어 본문 13개 절은 `doti_doit/app/src/main/java/com/doti/doit/PrivacyPolicyScreen.kt`와 일치하도록 관리합니다. 변경 시 양쪽 본문, 시행일, 연락처를 함께 수정하고 앱 소스 빌드와 공개 HTTP 응답을 확인하세요. 웹 갱신은 기존 설치 앱의 내장 문구를 자동 갱신하지 않습니다. 앱 문구는 다음 빌드에 포함됩니다.

2026-09-17 개정은 현재 구현에 맞춘 설명 정리이며 앱의 데이터 처리 기능을 새로 추가하지 않습니다.
