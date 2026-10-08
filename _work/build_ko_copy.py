"""제출용(영문) 파일과 같은 서식으로 한국어 열람용 사본을 만든다. 셀 값만 바꾼다."""
import openpyxl
SRC = 'Training_Plan/RCP_Training_Plan_19-30_Oct_2026.xlsx'
OUT = 'Training_Plan/RCP_Training_Plan_19-30_Oct_2026_KO.xlsx'
wb = openpyxl.load_workbook(SRC)
T = {
'Management Overview': {
 'A2': 'MK TECH | RCP 교육 제안서', 'A4': '교육 기간', 'B4': '2026년 10월 19~30일 (평일 10일)', 'D4': '기대 교육 성과',
 'A5': '장소', 'B5': '말레이시아 페낭 사이트',
 'D5': '1주차: RCP 랩 서버, MSSQL DB, 애플리케이션, UI를 구축하고 사이트(차량·태그·PLC)를 등록하며 OCS 전 화면을 조작한다.',
 'A6': '트레이너', 'B6': '박재민', 'A7': '교육생', 'B7': 'Thines, Areez, Farizal, Darwin, Gun Ho',
 'D7': '2주차: 맵 편집(OCS 설정, RailDesignTool, MapLoad), MCS 시뮬레이터로 HSMS 추적, 알람·장애 진단, Rose MirrorHA 조작.',
 'A8': '코디네이터', 'B8': 'Darwin', 'A9': '목적', 'B9': 'MMP가 RCP를 직접 셋업·유지보수·트러블슈팅할 수 있는 역량 확보.',
 'D9': '교육생별: 개인 실기 시험을 독립적으로 완료하고 복구 절차를 설명한다.',
 'A10': '트레이너 배경', 'B10': '리프터 프로젝트의 AATT 신규 인력. RCP 셋업 경험 보유.',
 'A11': '일정 여건', 'B11': '이번 주부터 11월까지 페낭 체류 예정. 12월 인도 프로젝트 시작.',
 'D11': '인수인계: 셋업 가이드, 맵 변경 체크리스트, 장애 가이드, 결과표.',
 'A12': '일일 시간표(안)', 'B12': '09:00~12:00, 13:00~16:00 (말레이시아 시간)', 'A13': '교육 시간',
 'A16': '교육 전 준비', 'B16': '담당', 'C16': '기한', 'D16': '요건 / 산출물', 'E16': '상태', 'F16': '비고',
 'A17': '일정 확정', 'B17': 'Darwin + 박재민', 'D17': '범위·날짜·트레이너 일정 합의', 'F17': '프로젝트 업무와 조율.',
 'A18': '랩 준비', 'B18': 'Darwin', 'D18': '테스트 망이 연결된 교육용 VM(Windows Server), MSSQL 2016 설치 미디어, IIS, Office / AccessDatabaseEngine, RailDesignTool 설치 PC 2대', 'F18': '격리된 테스트 환경 사용.',
 'A19': 'RCP 자료 준비', 'B19': '박재민', 'D19': 'RCP 설치 파일과 버전, 기반 소프트웨어 목록, 샘플 DB·맵·태그 Excel, 매뉴얼, XCom Simulator와 Simulation.exe', 'F19': '사이트 RCP 버전은 Darwin과 확인.',
 'A20': 'HSMS 테스트 준비', 'B20': '박재민 + Darwin', 'D20': '랩 서버에 XCom Simulator(MCS 시뮬레이터)와 cfg/sml 파일·메시지 예시, 9일차용 Rose MirrorHA 테스트 페어(또는 운영 페어 읽기 전용 접근)', 'F20': '시뮬레이터와 Rose 콘솔 접근 확인.',
 'A21': '교육생 차출', 'B21': 'MMP 관리자', 'D21': '하루 6시간 확보, 운영 대체 인력 배치', 'F21': '5명 모두 공통 모듈 참석.',
 'A22': '접근 권한 확인', 'B22': 'Darwin', 'D22': '개인별 랩 접근 권한과 백업/복구 기준선. 사이트 확인 사항(MCS_IF UI 창 유무, MapLoad 파일 형식 MDB/JSON, AltTransfer 화면 유무). IP·호스트명 마스킹한 사이트 로그 샘플', 'F22': '교육생마다 실습 시간 필요.',
 'A25': '계획 전제와 후속',
 'A26': '박재민이 기술 순서를 채워 넣은 제안 일정이다. 내용은 OCS 사용자 매뉴얼, 설치 기준서, setup 가이드, Parameter 매뉴얼, RailDesignTool 매뉴얼, Rose MirrorHA 운영 가이드를 따른다.',
 'A27': '합격 기준(안): 지식 70% 이상, 실기 80% 이상, 필수 체크 전부 통과, 트레이너 사인오프.',
 'A28': '지식 전달은 랩 데이터로 한다. 맵·DB 변경은 백업, 검증, 롤백 실습을 포함한다.',
 'A29': '11월: 트레이너가 인도로 떠나기 전에 부족한 부분에 대한 감독 지원과 재시험을 잡는다.',
},
'Daily Training Plan': {
 'A2': 'RCP | 2주 일별 교육 계획', 'A3': '트레이너: 박재민 | 전 세션: Thines, Areez, Farizal, Darwin, Gun Ho | 시간: 말레이시아 시간',
 'A5': '일차', 'B5': '날짜', 'C5': '모듈', 'D5': '09:00~12:00 | 설명·시연', 'E5': '13:00~15:00 | 실습', 'F5': '15:00~16:00 | 복습 / 테스트', 'G5': '일일 산출물', 'H5': '시간', 'I5': '상태', 'J5': '실제 비고',
 'C6': '아키텍처·서버 준비',
 'D6': 'RCP/OCS 구성요소(Core, PlcDriver, MCS_IF, UI, DB)와 각각의 통신 상대. 서버·네트워크 구성. config 파일과 폴더. 기동 순서와 Core 상태. 설치 기준서, 반입 전 체크리스트',
 'E6': '랩 서버를 설치 기준서와 대조: 필수 소프트웨어, 방화벽, NIC Teaming, RDP, UPS. CMD 진단(ping, netstat). 구성요소 흐름도 그리기',
 'F6': '교육생별로 구성요소 흐름과 기동 순서를 설명하고 서버 체크리스트를 제시',
 'G6': '아키텍처 스케치 + 서버 준비 체크리스트',
 'C7': 'DB 구축·유지보수',
 'D7': '기준서대로 MSSQL 2016 설치(Agent 자동 시작, 데이터 경로는 미러 디스크). DB 구축 쿼리. 백업 계획과 폴더. History 테이블과 Agent Job. SQL 메모리 상한. 로그 보존기간·디스크 설정',
 'E7': 'MSSQL 설치, 3단계 DB 구축 실행, 심어 둔 경로 오류 수정. 백업 폴더 설정. 서비스, MDF/LDF 증가, Agent Job 점검. 백업에서 복구',
 'F7': '교육생별로 교육 DB를 백업에서 복구하고 백업·보존 설정을 설명',
 'G7': 'DB 셋업 가이드 + 백업/복구 증빙',
 'C8': '애플리케이션 설치·사이트 구성',
 'D8': '기반 소프트웨어와 RCP 설치 순서. IIS에 UI 배포와 대표적 UI 오류 4종. 시뮬레이터 환경(XCom Simulator, Simulation.exe). 사이트 등록: CommGroup → Vehicle → Station → OrderGroup. Tag 3단 등록과 PlcTag 파일. PLC 연결 필드',
 'E8': '교육생별로 깨끗한 랩 서버에 RCP를 설치하고 Core 기동, UI 배포, 차량 1대와 PLC 유닛 1개 등록, Excel로 태그 적재, 시뮬레이터로 오더 1건 실행',
 'F8': '깨끗한 상태에서 RCP 기동. 심어 둔 설정 오류(DB IP / config / 태그 매핑)를 찾아냄',
 'G8': '애플리케이션 + 사이트 셋업 체크리스트',
 'C9': 'OCS 화면 조작 (1)·파라미터',
 'D9': '메인 화면, 상태 램프, 객체 색상, 찾기. 로그인과 권한. View / Layout Setting / DockSetting. System 메뉴: SystemInfo, Status, Color. Parameter 메뉴 구조와 배차·주행 파라미터(읽기만)',
 'E9': 'Object 메뉴 실습: Vehicle Line In/Out, Prevent, Sub Command, Clean. Station 모드. Point/CPS/MTL 상태. PLC, Ping 유닛, Tag 그룹 등록',
 'F9': '화면 드릴: 트레이너가 필드나 동작을 말하면 교육생이 찾아가 설명',
 'G9': '화면 체크리스트 1부',
 'C10': 'OCS 화면 조작 (2)·1주차 체크포인트',
 'D10': 'Transfer 지령과 CycleMove. Report 이력. ErrorHistory / HSMSHistory. Statistics. OrderList와 NACK. AlarmList, ErrorList, PingList, CommEvent. PlayBack. Help Version / Define',
 'E10': '시뮬레이터에서 수동 반송과 CycleMove. 이력·통계 조회. PlayBack Export',
 'F10': '1주차 체크포인트: 교육생별로 서버 → DB → 애플리케이션 → 사이트 셋업과 주요 화면을 순서대로 시연',
 'G10': '화면 체크리스트 2부 + 1주차 체크포인트 기록',
 'C11': '맵 생성·변경·업데이트',
 'D11': '맵 구조. OCS 쪽 통행 설정: Unuse, Home, Cluster, StationWeightGroup, AutoPark, Point type, UserBlock, Safety/CPS/MTL 영역, Layout Run. RailDesignTool 기본. 차량 제원과 Safety Margin. 오토블로킹',
 'E11': '랩 OCS에서 통행 설정 편집. RDT에서 사이트 맵 열기, 세그먼트 작도, 오토블로킹 실행, JSON Export. 랩 서버에서 BackupPath 지정해 MapLoad',
 'F11': '교육생별로 랩 서버에 맵 변경을 반영하고 롤백 경로와 운영 시스템 영향을 설명',
 'G11': '검증된 맵 + 변경/롤백 기록',
 'C12': 'HSMS: RCP ↔ MCS',
 'D12': 'MCS_IF 구성: cfg 경로, HSMS IP, XCom CfgSml, HostNetworkName. HSMS/SECS-II 프레임과 타임아웃 T3~T8. 접속 시퀀스(S1F13/F17, S2F41, S2F49)와 반송 이벤트. 상위 통신 문제가 드러나는 곳(NackHistory, HSMSHistory, XCom 로그)',
 'E12': '랩 OCS를 XCom 시뮬레이터에 연결. cfg/sml 등록, MCMD Remote까지 링크 올리기. S2F49 송신과 오더 추적. 심어 둔 단절에서 복구',
 'F12': '교육생별로 캡처한 교환 메시지를 설명하고 심어 둔 통신 장애를 복구',
 'G12': '통신 체크리스트 + 주석 단 HSMS 로그',
 'C13': '시뮬레이션·알람·트러블슈팅 진입점',
 'D13': '차량 통신 구조와 OHT 메시지 기초. 알람 분류(ErrType / ErrCode / ErrEvent). OCS 로그 지도(파일 로그 / DB 이력 / UI / XCom). 증상 → 차량·오더·서버·기동·PLC 문제별 첫 화면 또는 로그',
 'E13': '시뮬레이터에서 장애 스테이션 순환: 기동 실패, DB 연결, 차량 무응답, 오더 타임아웃, PLC 통신 알람. Comm 로그와 CommErrHistory 판독. ping / CMD로 통신 단절 구간 특정',
 'F13': '교육생별로 심어 둔 장애 2건을 진단하고 첫 화면/로그와 복구를 말함',
 'G13': '장애 격리 가이드 + 인시던트 기록',
 'C14': 'Rose MirrorHA·지식 테스트',
 'D14': 'Rose 리소스, 그룹, 가상 IP, FailOver 트리거. 콘솔 상태 판독. Bring In / Bring Out. 수동 절체와 역절체. 서비스 검증. 장애 유형과 1차 조치',
 'E14': 'Rose 테스트 페어에서: 상태 판독, 수동 절체·역절체, VIP로 RCP UI 접속과 FailOverHistory 확인',
 'F14': '지식 테스트(필기): 셋업, DB, 화면, 맵, HSMS, 알람, Rose. 점수와 부족한 부분 기록',
 'G14': '지식 점수 + Rose 체크리스트',
 'C15': '개인 실기·인수인계',
 'D15': '독립 종합 실기: 셋업 확인, 맵 편집, 차량/태그 등록, 시뮬레이션 오더 실행, 심어 둔 장애 해결과 복구. 트레이너 리뷰와 피드백',
 'E15': '오전에 개인 실기 5회(각 45분). 오후: 보완 재시험, 셋업 가이드·맵 변경 체크리스트·장애 가이드 인수인계',
 'F15': '트레이너가 실기 점수, 필수 체크, 사인오프 기록. 11월 후속(확장 항목) 배정',
 'G15': '개인 결과 + 인수인계 자료 + 조치 목록',
 'A17': '실습 조 편성: Thines + Areez / Farizal + Darwin / Gun Ho 순환. 조작자와 검토자를 번갈아 맡는다. 최종 시험은 전부 개인별.',
 'A18': '마지막 날 제안: 오전에 45분짜리 개인 실기 5회. 오후는 피드백, 보완 재시험, 인수인계.',
},
'Assessment Tracker': {
 'A2': 'RCP | 개인 평가 추적표', 'A3': '기준(안) | 시험 후 결과 입력. 점수는 0~100. 아직 기록된 결과 없음.',
 'A5': '교육생', 'B5': '출석(일)', 'C5': '1주차 체크포인트', 'D5': '지식 점수', 'E5': '실기 점수', 'F5': '필수 체크', 'G5': '트레이너 사인오프', 'H5': '결과', 'I5': '부족 / 후속 조치', 'J5': '재시험일',
 'A12': '실기 과제', 'B12': '배점', 'C12': '증빙', 'D12': '필수 요건', 'F12': '수료 규칙(안)',
 'A13': '서버 + 애플리케이션 + IIS', 'C13': '깨끗한 상태에서 Core / PlcDriver / MCS_IF 기동. 테스트 클라이언트에서 UI URL 접속', 'D13': '기동 순서와 config / 서비스 의존 관계 설명',
 'F13': '출석: 10일 중 9일 이상. 빠진 핵심 모듈은 사인오프 전에 보충.',
 'A14': 'DB CRUD + 복구', 'C14': '스크립트로 DB 구축. 차량·Station 레코드 등록. 백업 후 복구 검증', 'D14': '변경 전 백업. 무관한 데이터 보존. 복구 성공',
 'F14': '1주차 체크포인트 통과. 지식 70/100 이상. 실기 80/100 이상.',
 'A15': '맵 변경 + 롤백', 'C15': '통행 설정 또는 RDT 맵 변경을 Layout > MapLoad로 BackupPath 지정해 반영', 'D15': '연결성 확인(Layout > Check)과 롤백 시연',
 'F15': '필수 체크: 백업, 롤백, 복구를 포함한 필수 요건 전부 통과.',
 'A16': 'HSMS 통신', 'C16': 'XCom 시뮬레이터와 MCMD Remote까지 링크. S2F49 오더를 OrderList / HSMSHistory에서 추적', 'D16': '통신 점검 항목 설명과 재접속',
 'F16': '트레이너가 시험, 증빙, 보충 작업을 검토한 뒤 사인오프.',
 'A17': '시뮬레이션 + 장애 진단', 'C17': '시뮬레이터에서 테스트 오더 완료. 심어 둔 장애의 원인 증빙(로그 또는 화면)', 'D17': '첫 화면 / 로그를 지목하고 진단, 복구 검증',
 'F17': '기준 미달 시: 부족한 부분 기록, 연습 배정, 11월 재시험일 합의.',
 'A18': '인수인계 + 티치백', 'C18': '명확한 런북과 에스컬레이션 기록', 'D18': '무엇이 바뀌었는지 설명하고 증빙 제시',
 'A19': '실기 총점',
}}
n = 0
for sheet, cells in T.items():
    ws = wb[sheet]
    for k, v in cells.items():
        assert ws[k].value is not None and not str(ws[k].value).startswith('='), (sheet, k)
        ws[k] = v; n += 1
wb.save(OUT)
# 남은 영문 텍스트 셀 확인 (이름·상태값·수식 제외)
import re
left = []
for ws in wb.worksheets:
    for row in ws.iter_rows():
        for c in row:
            if isinstance(c.value, str) and not c.value.startswith('=') and not re.search(r'[가-힣]', c.value):
                left.append(f"{ws.title[:4]}!{c.coordinate}: {c.value}")
print('translated', n); print('\n'.join(left))
