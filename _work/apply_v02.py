"""v0.1 -> v0.2: 2026-10-08 확정 4건 반영.

1. 기준 매뉴얼 = MXA본  -> MXA본에 있는 기능의 '버전차이' 해소, MXA본에 장이 없는 기능은 'MXA외'로 표시
2. 맵 도구 = RailDesignTool -> '도구미확정' 해소, LayOut Designer/Winlay 전용 절차는 정리
3. 에러코드 = ErrTag_L30 / ErrorDescription 병기 -> 대역 충돌만 걸린 항목은 '자료충돌' 대신 '병기'
4. 기동 순서 = Core만 먼저, 나머지 순서 무관
"""
import json

d = json.load(open('_work/items_v0.1.json', encoding='utf-8'))
items = d['items']
I = {it['id']: it for it in items}


def flags(iid, add=(), remove=()):
    f = [x for x in (I[iid].get('flags') or []) if x not in remove]
    f += [x for x in add if x not in f]
    I[iid]['flags'] = f


def sub(iid, field, old, new):
    s = I[iid].get(field) or ''
    assert old in s, (iid, field, old)
    I[iid][field] = s.replace(old, new)


def note(iid, text):
    I[iid]['flag_note'] = text


# ---------------------------------------------------------------- 1. MXA본 기준
# MXA본에 있는 기능: 판본 차이가 더 이상 쟁점이 아님
for iid in ['L1-02', 'L1-03', 'L1-14', 'L1-16', 'L1-25', 'L1-26', 'L1-32', 'L1-37', 'L1-44', 'L1-47', 'L1-49',
            'L2a-17', 'L2a-18', 'L2b-01', 'L2b-29', 'L2c-05', 'L2c-09', 'L3b-04', 'L3c-07', 'AUX-10']:
    flags(iid, remove=['버전차이'])

sub('L1-02', 'content', ' v04본 8영역 설명에는 이 램프가 없으므로 대상 사이트 화면에 램프가 있는지 먼저 실측한 뒤 교육한다.', '')
sub('L1-02', 'objective', '(램프가 있는 버전에 한함)', '')
note('L1-02', 'MXA본 3.1 기준. PLC 램프 색은 원문에 없어 현장 화면으로 보충해야 한다.')
note('L1-03', '색상(황색/갈색/초록)은 MXA본 기준. 전체 색상 정의는 Help>Define(L1-48).')
sub('L1-14', 'content', 'Parameter는 System', 'Parameter(MXA본 15그룹)는 System')
note('L1-14', 'MXA본 6.10 기준 15그룹(v04는 DBInterfaceParam 포함 16그룹).')
note('L1-16', '근거 pptx 캡처 타이틀바에 현장 서버 호스트명·IP와 차량명이 보임 — 배포 시 마스킹. Sub Vehicle Command 구성은 MXA본 7.3.2 기준으로 가르치고 2026 현장 캡처와 다른 버튼은 현장 화면으로 보충. '
                 'Clean Mode가 할당·경로에 미치는 영향은 자료 없음. 분기진입 실패 판단 후 Forcible Entry 투입 결정은 L3-a.')
note('L1-25', 'MXA본 7.11 PlcTagmonitor / 7.12 PlcTagGroup 기준.')
note('L1-26', 'Text Box 신규 등록(Layout editor)은 L2-a.')
note('L1-32', 'MXA본 9장 Report 19종 기준. RCPHMI 현상6: InformLogHistory Insert가 테이블 null 미허용으로 실패한 기록이 있어 실습 전 동작 확인 필요.')
sub('L1-32', 'objective', ', MXA본은 Move History·Safety History', '·Move History·Safety History')
note('L1-37', 'v04본 근거. MXA본은 Statistics 장 자체가 없음(L1-34 참조).')
flags('L1-37', add=['MXA외'])
note('L1-44', 'MXA본 11.2 Check / 11.3 Setting 기준. Check 경고가 실제 결함인지 판정해 고치는 것은 L2-a(Layout Run 항목).')
note('L1-47', 'MXA본 13.1 기준(Core, Plc Driver, MCS_IF, DB, RCPGT 버전 표시). 구조적 의미는 L2-b.')
note('L1-49', 'MXA본 용어 설명 장 기준. 메뉴 화면이 아니라 매뉴얼 장이라 Help 탭에 붙임.')
note('L2a-17', 'MXA본 6.7 기준. PlcTagmonitor 실시간 확인과 Report>Move History 조회는 L1로 분리.')
note('L2a-18', 'MXA본 11.1 Run 기준. RCPHMI 현상7의 9992~9999번 point 경고는 정답 미확정이라 채점하지 않고 사례집으로 보냄. Layout>MapLoad는 L3-c.')
sub('L2b-29', 'content',
    'BlockingParam / DatabaseParam / DBInterfaceParam / HostParam / LogParam / MCCSParam / OrderControlParam / PIOParam / priorityParam / SocketParam / StationControlParam / SystemParam / TimeoutParam / TrafficParam / UIParam / VehicleControlParam 16그룹이다(v04 기준). Parameter 매뉴얼은 17범주(DataBase … TaskMgr / VehicleCommand / VehicleEvent)로 나누고, MXA본은 15그룹이다.',
    'BlockingParam / DatabaseParam / HostParam / LogParam / MCCSParam / OrderControlParam / PIOParam / PriorityParam / SocketParam / StationControlParam / SystemParam / TimeoutParam / TrafficParam / UIParam / VehicleControlParam 15그룹이다(MXA본 6.10 기준). v04본은 DBInterfaceParam을 더해 16그룹, Parameter 매뉴얼은 17범주(DataBase … TaskMgr / VehicleCommand / VehicleEvent)로 나눈다.')
flags('L2b-29', remove=['자료충돌'])
note('L2b-29', '그룹 목록은 MXA본 15그룹 기준. Parameter 매뉴얼 17범주는 항목 설명을 찾는 색인으로만 쓴다. OHT 점검 4종은 원자료에 이름만 있고 기능 설명은 조사자가 보충한 것이다(근거약함). Value 변경은 L3-a.')
note('L2b-01', 'Secom은 로그분석 매뉴얼에만 로그 주체로 나오고, setup 가이드·설치 기준서의 실행 단위 4개(Core/MCS_IF/PlcDriver/RCPGT) 목록에는 없다(자료충돌). 5요소 구성은 MXA본 2.2 기준. '
                 '사이트 호스트명(STOTA20100)·차량 번호대(U.50~114)는 마스킹 대상이다.')
note('L2c-05', '경로·보존일수는 사이트 설정값이다. 대응 Report는 MXA본 9장 기준(Move History 포함). 같은 내용이 Report 보존기간 모듈과 중복되지 않게 이 항목 하나로 묶었다.')
note('L2c-09', 'Report>FailOverHistory는 MXA본 9.19 기준. Rose Console Log는 \'조회 영역이 있다\'는 서술뿐이고 로그 경로·파일명은 자료에 없다. COMMENT의 서버명칭은 사이트마다 다르다.')
note('AUX-10', 'MXA본 TroubleShooting 장 기준.')

# MXA본에 장이 없는 기능: 지우지 않고 'MXA외'로 표시 → 현장 화면 실측 후 유지·삭제 결정
mxa_out = {
    'L1-17': 'MXA본에는 System>Vehicle IO Tag 장이 없음(v04 근거). Home Point 필드는 RCPHMI 메모의 \'필요한 듯\'·save 불가 기록뿐이라 평가 문항에서 제외하고 위치 인지만. IO 비트로 차량 이상을 판정하는 것은 L3-a.',
    'L1-34': 'MXA본은 메뉴 탭 목록에 Statics가 있으나 Statistics 장이 없음(v04 근거). L1-35~37도 같음.',
    'L1-35': 'MXA본 Statistics 장 없음(v04 근거). 평균 비교로 느린 구간·설비를 특정하는 것은 L3-a.',
    'L1-36': 'MXA본 Statistics 장 없음(v04 근거). 여러 축 결과로 알람 원인을 특정하는 것은 L3-a.',
    'L1-42': 'MXA본 10장에는 TerminalMsg가 없고 Docking Setting(10.6)만 있음. TerminalMsg 부분은 v04 근거.',
    'L2a-11': 'MXA본 6장에 System>Cluster 장이 없음(v04 근거). MaxVehicleLowCount/HighCount 같은 Cluster Info 수치를 바꿔 거동을 튜닝하는 것은 L3-a. C306 Insert 실패는 원인 미규명이라 채점하지 않는 주의사항으로만 쓴다. 화면 필드명 오기(MaxVehicleConut) 있음.',
    'L2b-13': 'IO Tag 부분은 MXA본에 장이 없음(v04 근거). STATUS·S= 부분은 프로토콜 사양서 근거라 영향 없음. S= 체계로 정체 지점을 판정하거나 IO 비트로 차량 이상을 판정하는 일은 L3-a.',
    'L2b-30': 'Cluster EntranceLimit 부분은 MXA본에 장이 없음(v04 근거). 나머지 Parameter는 MXA본 6.10에 있음. PushWeight·UseBothWay 등의 값을 조정해 현상을 해결하는 일은 L3-a. PushWeight 미동작 건은 RCPHMI에 미해결로 남아 있다.',
    'L2b-31': 'MXA본에 System>AltTransfer 장이 없음(표 안 1회 언급뿐). 경유지 반송이 있는 사이트에만 해당.',
}
for iid, n in mxa_out.items():
    flags(iid, add=['MXA외'], remove=['버전차이'])
    note(iid, n)
# MCS_IF 탭도 MXA본에 장이 없음
for iid in ['L1-50', 'L1-51']:
    flags(iid, add=['MXA외'])
    I[iid]['flag_note'] = ((I[iid].get('flag_note') or '') + ' MXA본에는 MCS_IF 탭 장이 없음(v04/setup 가이드 근거).').strip()

# ---------------------------------------------------------------- 2. 맵 도구 = RailDesignTool
for it in items:
    flags(it['id'], remove=['도구미확정'])

note('L2a-01', '기본 경로와 버전은 PC·사이트마다 다르다.')
sub('L2a-04', 'content', ' LayOut Designer에서는 Point → Segment → Navigator → Reflector 순서로 작도한다.', '')
I['L2a-04']['sources'] = [s for s in I['L2a-04']['sources'] if 'setup 가이드' not in s]
note('L2a-04', 'RDT 매뉴얼 기준. LayOut Designer 절차(setup 가이드 표19)는 사이트 도구가 RDT로 확정되어 뺐다.')
sub('L2a-14', 'content', 'AutoBlock(Winlay 상에서 차량·세그먼트 사이즈로 자동 생성된 Block Segment List)',
    'AutoBlock(맵 도구에서 차량·세그먼트 사이즈로 자동 계산된 Block Segment List — 현 사이트는 RailDesignTool 오토블로킹)')
note('L2a-14', 'AutoBlock 자동 계산(RailDesignTool)은 L3-c다. 매뉴얼 원문은 \'Winlay 상에서\'로 적혀 있다. 속도·차량 사이즈 값은 사이트별 기준이며, 그 값을 바꾸는 것은 L3다.')
sub('L2a-16', 'content', '먼저 Layout에서 MTL 객체를 생성한다.', '먼저 OCS Layout>Run에서 MTL 객체를 생성한다(MXA본 7.7).')
note('L2a-16', 'MTL 객체 선생성은 MXA본 7.7 \'Layout에서 MTL(MTU) 객체를 만들면\' 기준으로 OCS Layout 탭에서 한다.')
sub('L2b-25', 'flag_note', ' 맵 도구는 미확정이다.', '')
for iid in ['L3c-01', 'L3c-02', 'L3c-03', 'L3c-04']:
    pass  # RDT 매뉴얼 근거 항목: 플래그 해제만으로 충분
sub('AUX-07', 'flag_note', ' RailDesignTool이 현 사이트 맵 도구인지 미확정.', ' 현 사이트 맵 도구는 RailDesignTool이므로 2.7 설치는 맵 작업 PC에 필수.')

# RDT → OCS 반영 경로: RDT는 JSON만 내보내고, MXA본 MapLoad는 Winlay MDB를 받는다 → 연결 자료 없음
GAP = ('RDT 매뉴얼은 Export/Import Json File만 있고 MDB 출력이 없다. MXA본 11장은 \'Winlay로 작성한 MDB를 Core에서 불러온다(Layout>MapLoad, MDB → UPDATE)\'고만 적는다. '
       'RDT JSON이 OCS DB에 들어가는 경로(변환 도구, 메뉴, 재기동 여부, 이중화 양 노드 반영)는 어느 자료에도 없다.')
flags('L3c-05', add=['자료없음'])
note('L3c-05', 'Export까지만 채점한다. ' + GAP + ' 경로 E:\\test.json은 예시다.')
flags('L3c-07', add=['자료없음'], remove=['자료충돌'])
note('L3c-07', '메뉴는 MXA본 기준 Layout>MapLoad(MDB 선택·BackupPath·MDB → UPDATE). ' + GAP +
     ' 사이트 반영 절차를 받기 전까지는 MDB 기준 절차로 가르치고, 실습은 테스트 서버로 제한한다.')
flags('L3c-08', add=['자료없음'])
note('L3c-08', 'AccessDatabaseEngine은 MDB를 읽는 MapLoad 전제 조건이다. RDT JSON 반영 경로에서도 필요한지는 L3c-07의 반영 절차가 확정되어야 판단할 수 있다.')
flags('L3c-06', add=['자료없음'])
note('L3c-06', 'LayOut Designer(setup 가이드 표20) 기준 절차다. RDT 매뉴얼에는 Check Layout·Solid Detect 기능이 없다. RDT에서 같은 검증을 어떻게 하는지 확인되지 않으면 삭제 후보. '
               'OCS 화면 Layout>Check(L1-44)와는 별개다.')
sub('L3c-09', 'content', '수행하려는 조작이 이 체인(Winlay/LayOut Designer MDB → MapLoad 경로 또는 RDT JSON Export 경로)의 어느 단계인지 짚고',
    '수행하려는 조작이 이 체인(RDT 작도 → 오토블로킹 → JSON Export → OCS 반영)의 어느 단계인지 짚고')
sub('L3c-09', 'content', 'RDT/LayOut Designer에서', 'RDT에서')
note('L3c-09', '이 기준은 조사자가 매뉴얼을 종합해 만든 것이다. JSON Export 이후 OCS 반영 단계는 절차서가 없어(L3c-07) 그 단계의 선행 조치는 절차서 확보 후 문항으로 확정한다.')
flags('L3c-09', add=['자료없음'])

# ---------------------------------------------------------------- 3. 에러코드 병기
BAND = '코드 대역은 부록 A 대조표대로 260103_ErrTag_L30 / ErrorDescription 두 판을 병기한다.'
for iid in ['L1-12', 'L2b-27', 'L2b-28', 'L2c-12', 'L2c-13', 'L2c-14', 'L2c-17', 'L2c-18', 'L3a-14', 'L3a-25', 'AUX-18']:
    flags(iid, add=['병기'], remove=['자료충돌', '버전차이'])
flags('L2c-13', add=['자료충돌'])  # Noway timeout 15초 vs 20초는 별개 충돌

note('L1-12', BAND + ' ErrCode/ErrType/ErrEvent가 AlarmList·ErrorHistory와 이어지는 Tag 체계 설명은 L2-b.')
sub('L2b-27', 'content', '21종이다(ErrorDescription은 19종). 260103_ErrTag 기준 대역은 VEHICLE 1~720 / CPSDOWN 1000~1027 / CPSFAILOVER 1028~1055 / SYSTEM 3001~4574 / PING 7001~7120 / PLCCOMM 7500~7507 / SYSTEMALARM 8071~8104 / STATIONALARM 8105~8130(ErrorDescription은 5000~5273) / 9xxxx 서버·RCP 내부다.',
    '21종이다(ErrorDescription은 SYSTEMALARM·SAFETY가 없어 19종). 대역은 두 판을 병기한다(부록 A). 같은 대역: VEHICLE 1~720 / CPSDOWN 1000~1027 / CPSFAILOVER 1028~1055 / 9xxxx 서버·RCP 내부 / MCSIF 100001. '
    '다른 대역(ErrTag / ErrorDescription): SYSTEM 3001~4574 / 3001~4500, PING 7001~7120 / 7001~7112, PLCCOMM 7500~7507 / 7500~7505, STATIONALARM 8105~8130 / 5000~5273, SYSTEMALARM 8071~8104 / 없음, SAFETY 9000~9003 / 없음.')
sub('L2b-27', 'objective', '사이트 ErrTag 현행본을 확인한 뒤 ErrCode 대역으로 계통을 좁히고', 'ErrCode 대역으로 계통을 좁히되 두 판의 대역이 다른 계열(SYSTEM·PING·PLCCOMM·STATIONALARM)은 사이트 System>ErrorTag 화면으로 확인하고')
note('L2b-27', BAND + ' AP 대수(ErrTag 12 vs SNMP 목록 8)는 사이트별 확인.')
note('L2b-28', BAND + ' ErrCode/ErrEvent가 뒤바뀐 4건은 이 사이트 파일의 결함이다. E84 알람은 PIO 타이밍 차트가 없어 \'명명 규칙 이해\' 수준으로만 평가한다(근거약함).')
sub('L2b-28', 'content', 'SYSTEM(3001~4574)은', 'SYSTEM(ErrTag 3001~4574 / ErrorDescription 3001~4500)은')
note('L2c-12', BAND + ' RCP 91001~91012는 두 판이 같다. 검증자 missing 2건(\'UVP vs CommError\', WARMINGUP→RUNNING 파라미터)을 이 항목에 반영했다.')
note('L2c-13', '타임아웃 값은 사이트 설정이다. ErrorDescription의 Noway_Timeout 설명은 \'Finding path 후 15초\'인데 매뉴얼 예시는 20초다(자료충돌). ORDER 96002~96003은 두 판이 같다. '
               'PntOccupy 로그와 대조해 설정 문제인지 설비 문제인지 판정하는 일과 값 조정은 L3-a다.')
note('L2c-14', 'JCPHeartBeat 알람이 JCRCOMM 96101로 뜨는지는 자료에 명시가 없어 현장 확인이 필요하다. 96xxx 코드는 두 판이 같다. JunctionParam>JunctionOccupyWaitTimeOutSec은 ErrorDescription Description에만 있고 Parameter 매뉴얼 그룹 목록에는 없음.')
sub('L2c-17', 'content', 'ErrType=PLCCOMM은 ErrCode 7500~7507 8행이고', 'ErrType=PLCCOMM은 ErrTag 기준 ErrCode 7500~7507 8행(ErrorDescription은 7500~7505 6행 — FireDoor 2행 없음)이고')
note('L2c-17', BAND + ' PLC 8대 구성과 코드-그룹 대응은 AATT L30 사이트 값이다. 다른 사이트에서는 ErrTag·PlcTag로 다시 맞춰야 한다.')
note('L2c-18', BAND + ' Description 컬럼은 ErrorDescription에만 있으므로, ErrTag에만 있는 코드(SYSTEMALARM·SAFETY, PING 7113~7120 등)는 설명이 없다.')
note('L3a-14', BAND + ' _ALARMID ↔ ErrEvent 조인은 사이트 System>ErrorTag에 실제 등록된 값으로 한다(L3a-25). 키 목록을 외워 설명하는 부분은 L2-b, 실제로 이어 붙이는 실습이 L3-a이다.')
sub('L3a-25', 'content', '코드 조회는 현행 ErrTag로 하고, ErrorDescription.xlsx(STATIONALARM 5000~5273 대역)의 번호를 섞지 않는다.',
    'STATIONALARM 대역은 두 판이 다르므로(ErrTag 8105~8130 / ErrorDescription 5000~5273) 사이트 System>ErrorTag에 등록된 판으로 조회하고 두 판의 번호를 섞지 않는다.')
note('L3a-25', 'ST 1/3/2의 의미는 사례 1건 관측 기반 추정이다. ' + BAND + ' 채점은 \'사이트 ErrorTag 화면에서 확인한다\'는 절차형으로 한다. TagProperty/Comment 결함은 해당 사이트 파일의 데이터이다.')
note('AUX-18', 'Bridge=차량측 해석은 자료 조합 추론. PING 대역은 병기(ErrTag 7001~7120 / ErrorDescription 7001~7112). AP IP는 마스킹')

# ---------------------------------------------------------------- 4. 기동 순서: Core만 먼저
sub('L2b-04', 'content', '프로세스는 관리자 권한으로 1.Core.exe → 2.PlcDriver.exe → 3.MCS_IF.exe 순으로 실행한다.',
    '프로세스는 관리자 권한으로 Core.exe를 먼저 실행하고, PlcDriver.exe와 MCS_IF.exe는 그 뒤 어느 순서로 띄워도 된다(설치 기준서는 PlcDriver→MCS_IF, 단독 실행 매뉴얼은 MCS_IF→PlcDriver로 적혀 있으나 사이트 확인 결과 Core 선기동만 요건).')
sub('L2b-04', 'objective', '기동 순서를 재현하고', 'Core를 먼저 띄우는 규칙대로 기동을 재현하고')
flags('L2b-04', remove=['자료충돌'])
note('L2b-04', '기동 순서는 2026-10-08 확정: Core 선기동만 요건. 10.3 \'10초\', 10.4 \'50초\'는 매뉴얼 예시값이다(사이트별 확인). 값 변경은 L3-a 범위다.')
sub('L3b-12', 'content', '5) D:\\Program\\Core\\Core.exe → D:\\Program\\MCS_IF\\MCS_IF.exe → D:\\Program\\PLCDRIVER\\PlcDriver.exe 순서로 기동한다.',
    '5) D:\\Program\\Core\\Core.exe를 먼저 기동하고, 이어서 D:\\Program\\MCS_IF\\MCS_IF.exe와 D:\\Program\\PLCDRIVER\\PlcDriver.exe를 기동한다(둘 사이 순서는 무관).')
sub('L3b-12', 'objective', ' 5단계 안의 프로그램 기동 순서는 단독 실행 매뉴얼(Core→MCS_IF→PlcDriver)과 설치 기준서(Core→PlcDriver→MCS_IF)가 달라, 사이트 기준이 확정되기 전에는 채점하지 않는다.',
    ' 프로그램 기동은 Core를 먼저 띄웠는지만 채점한다.')
flags('L3b-12', remove=['자료충돌'])
note('L3b-12', '노드명 AGV03/AGV04, 그룹명 IMS, NIC 이름(BMS/Heartbeat/Host/iDRAC_Don\'t-Use/Local01/Mirror/Spare), 캡처 IP는 사이트 값이라 역할명으로 치환하고 IP는 마스킹. 폴더명은 매뉴얼마다 McsIF·PlcDrv / MCS_IF·PLCDRIVER로 다르니 현장 경로를 확인.')

# ---------------------------------------------------------------- 남은 '버전차이'는 OCS 매뉴얼 판본이 아닌 버전 차이
# (Rose 서비스명, 프로토콜 3.4.6, 로그 형식, MCCS↔Rose, .NET, 장비 구성 등) — 표시는 유지
d['log'].append({'v': '0.2', 'date': '2026-10-08', 'decisions': {
    '기준 매뉴얼': 'MXA본', '맵 도구': 'RailDesignTool', '에러코드': 'ErrTag_L30 / ErrorDescription 병기', '기동 순서': 'Core 선기동만 요건'}})

json.dump(d, open('_work/items_v0.2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

from collections import Counter
print(Counter(f for it in items for f in it.get('flags') or []))
print('버전 남은 항목:', [it['id'] for it in items if '버전차이' in (it.get('flags') or [])])
print('MXA외:', [it['id'] for it in items if 'MXA외' in (it.get('flags') or [])])
print('자료없음:', [it['id'] for it in items if '자료없음' in (it.get('flags') or [])])
