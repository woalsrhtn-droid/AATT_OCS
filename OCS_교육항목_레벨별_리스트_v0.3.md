# OCS 교육 항목 — 레벨별 리스트 v0.3

> 검토용 초안 (2026-10-08). 미결 사항(기준 매뉴얼·맵 도구·에러코드·기동 순서·맵 반영 경로·현장 화면)을 반영했습니다. 레벨 배정과 범위가 확정되면 Section / Module 분류와 배점으로 넘어갑니다.
> 항목별 교육 내용 전문과 근거 문서·페이지는 [OCS_교육항목_상세_v0.3.md](OCS_교육항목_상세_v0.3.md)에 있습니다.

## 요약

| 레벨 | 목표 | 측정 질문 | 항목 수 |
|---|---|---|---:|
| L1 | OCS 프로그램 숙지 | OCS 레이아웃(화면)에 있는 내용을 다 다룰 수 있는가 | 51 |
| L2-a | 맵·통행영역 수정 | Layout 같은 기능으로 맵을 수정할 수 있는가 | 18 |
| L2-b | 프로그램·시스템 구조 | Core / PLC Driver / MCS_IF 등 구조를 아는가 | 32 |
| L2-c | 현상별 진입 경로 | 문제가 생겼을 때 OCS 화면 어디를 찾아가야 하는지 아는가 | 20 |
| L3-a | 로그 분석·처리 | 직접 로그를 분석하고 문제를 처리할 수 있는가 | 41 |
| L3-b | Rose 서버 이중화 | Rose 이중화 프로그램을 다룰 수 있는가 | 13 |
| L3-c | RailTool layout 업데이트 | RailTool로 layout을 업데이트할 수 있는가 | 8 |
| 보조 | 7개 목표 밖 | 정기점검·네트워크 장비·설치 기준·SNMP/REST | 27 (L1 6 · L2 14 · L3 7) |
| **합계** | | | **210** (L1 57 · L2 84 · L3 69) |

LCS 체계가 105항목이었으니 약 2배입니다. Manual 폴더 8개 문서군에서 나온 후보 578개를 중복 통합한 결과이고, 이 단계에서는 일부러 줄이지 않았습니다(v0.3에서 RDT에 해당 없는 1건만 삭제, 부록 B). 빼거나 합칠 항목을 지정해 주시면 반영하겠습니다. 항목 ID는 검토 중 혼동이 없도록 삭제 후에도 번호를 당기지 않았습니다.

### 표시

| 표시 | 의미 | 항목 수 |
|---|---|---:|
| `자료없음` | 근거 자료가 없음 — 절차서를 새로 만들어야 평가 가능 | 1 |
| `충돌` | 두 자료가 서로 다른 값·순서를 제시 | 38 |
| `병기` | 에러코드 대역을 ErrTag_L30 / ErrorDescription 두 판으로 병기 (부록 A) | 11 |
| `버전` | 사용자 매뉴얼 판본 외의 버전 차이 — Rose 서비스명, 프로토콜 개정, 로그 형식, .NET, 장비 구성 등 | 10 |
| `근거약` | 자료가 스크린샷뿐이거나 초안 수준 | 40 |
| `추정` | 원자료가 "추정"으로 표기했거나 1개 사이트 표본 기반 | 35 |

표에는 생략했지만 `사이트의존`(IP·임계값 등 사이트별 값) 126건, `민감정보`(호스트명·IP·계정 — 타 사이트 배포 시 마스킹) 37건이 붙어 있습니다.

## 확정된 결정 (2026-10-08)

| # | 질문 | 결정 | 반영 내용 |
|---|---|---|---|
| 1 | 기준 매뉴얼 | **사용자 매뉴얼 3판 모두** (v04 / 중문통합 / MXA — 사실상 동일) | 판본 차이 표시를 지움. 사용자 매뉴얼에 있는 화면(Statistics, System>Cluster, Vehicle IO Tag, AltTransfer, Window>TerminalMsg)은 현장에 있다고 보고 그대로 유지 |
| 2 | 맵 도구 | **RailDesignTool** | LayOut Designer 절차는 뺐거나 삭제(L3c-06) |
| 3 | 에러코드 기준 | **두 판 병기** (`260103_ErrTag_L30.xlsx` / `ErrorDescription.xlsx`) | 대역 충돌만 걸려 있던 11건은 `충돌` → `병기`. 대조표는 부록 A |
| 4 | 프로그램 기동 순서 | **Core만 먼저**, PlcDriver·MCS_IF 순서는 무관 | L2b-04, L3b-12 본문·채점 기준 수정 |
| 5 | RDT 맵의 OCS 반영 | **Winlay 맵과 같은 절차로 OCS Layout>MapLoad** | L3c-05, L3c-07, L3c-08, L3c-09의 `자료없음` 해제. 반영 체인을 RDT 작도 → 오토블로킹 → JSON Export → Layout>MapLoad로 고정 |
| 6 | RDT 맵 검증 기능 | **없음** | L3c-06(Check Layout·Solid Detect) 삭제 — 부록 B. OCS 화면 Layout>Check는 L1-44·L2a-18에 유지 |

## 새로 확인이 필요한 것

| # | 질문 | 왜 생겼나 | 걸린 항목 |
|---|---|---|---|
| A | 현장 MCS_IF에 화면(창)이 있습니까? | MCS_IF 화면(View 탭 XcomCfgSmlFileManager, 상단 점등, MCS System Msg, MCMD 점등)은 사용자 매뉴얼에 없고 setup 가이드·설치 기준서에만 있음. MXA본은 MCS_IF를 'UI 없이 내부 구동'으로 적음 | L1-50, L1-51 |
| B | MapLoad에서 고르는 파일은 MDB입니까, RDT JSON입니까? | 매뉴얼 원문은 MDB 선택으로 적고 RDT 산출물은 JSON. 실습 전에 확인하면 되고 항목 구성에는 영향 없음 | L3c-07, L3c-08 |

### 자료가 없어서 지금은 평가할 수 없는 것

항목은 세워 두었지만 근거 문서가 없어 정답을 정할 수 없습니다. 교육 전에 절차서를 새로 써야 합니다.

- **Rose 단독 실행 후 이중화 복귀** (L3b-13) — 내려가는 절차만 있고 원복 절차가 어느 자료에도 없음
- **맵 반영 후 롤백** (L3c-07, L3c-09) — BackupPath 지정까지만 있고 백업에서 되돌리는 절차가 없음
- **로그로 원인 특정 이후의 조치 일부** (L3-a) — 합류부 점유 고착 해제, PlcCommLog WaitConnect 때 재시작 대상, 멈춘 Order 해소 순서

### v0.1에서 제가 판단해서 바꾼 것 (유지)

- **Layout 탭의 L1이 0개**였습니다. 정의상 "맵을 바꾸지 않는 화면 조작 = L1"이므로 Layout>Setting(화면 배율)과 Layout>Check 실행을 L1(L1-44)로 떼어내고, Layout>Run 배치·수정은 L2-a(L2a-18)에 남겼습니다.
- **AUX 레벨 기준 통일**: 설치할 때 기준대로 설정하는 것은 L2, 운영 중 설정을 바꾸는 것은 L3로 맞췄습니다.

---

## L1 — OCS 프로그램 숙지 (51항목)

**OCS 레이아웃(화면)에 있는 내용을 다 다룰 수 있는가** — 화면을 메뉴 경로로 열고, 필드·컬럼·색상 의미를 알고, 매뉴얼 절차대로 등록·조회·지령·저장을 수행한다.

| 탭 | 메인화면 | View | System | Object | Transfer | Report | Statistics | Window | Layout | PlayBack | Help | MCS_IF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 항목 수 | 5 | 1 | 8 | 12 | 2 | 5 | 4 | 6 | 1 | 2 | 3 | 2 |

### 메인 화면 (메뉴 밖 공통 영역)

| ID | 항목 | 할 수 있어야 하는 것 | 주의 |
|---|---|---|---|
| L1-01 | 메인 화면 8영역 식별 | 실화면에서 8영역을 하나씩 가리키며 이름과 용도를 말하고, 10개 메뉴 탭을 순서대로 열 수 있다. |  |
| L1-02 | Core/PLC/Host 연결 램프 | 대상 사이트 메인 화면에서 Core/Host 연결 램프를 찾아 깜빡임 여부로 연결 상태를 읽을 수 있다. | `근거약` |
| L1-03 | Layout 객체·색상 식별 | layout 영역에서 임의로 지정한 객체가 7종 중 무엇인지 말하고, Unuse/Home/Station Point를 색으로 구분할 수 있다. |  |
| L1-04 | 로그인 ID 등록·권한 | ID를 등록·로그인하고, 메뉴가 보이지 않을 때 권한 부족인지 확인하며, 우측 상단 자동 로그아웃 표시를 읽을 수 있다. |  |
| L1-05 | 메인 화면 찾기·확대·결과 확인 | 번호만 주어진 Point·Vehicle·CassetteID를 찾기 기능으로 화면에 띄우고, Home 등록·해제 결과를 Layout 색으로 확인할 수 있다. |  |

### View 탭

| ID | 항목 | 할 수 있어야 하는 것 | 주의 |
|---|---|---|---|
| L1-06 | View 탭 표시 항목 전환 | 지정한 정보(예: Segment 번호와 진행 방향)만 화면에 보이도록 View 탭을 설정하고 Default로 되돌릴 수 있다. |  |

### System 탭

| ID | 항목 | 할 수 있어야 하는 것 | 주의 |
|---|---|---|---|
| L1-07 | SystemInfo 자원 현황 확인 | SystemInfo HARDWARE에서 서버별 CPU/MEMORY/드라이브 사용률을 읽어 보고하고, ErrorList의 92001/93001/95001 행이 어느 자원 경고인지 짚을 수 있다. | `충돌` |
| L1-08 | System Color·Status 조회 | System>Status에서 Check를 실행해 DB 이름과 여유공간을 읽어 보고하고, Color 화면에서 Object 색을 바꾸고 저장할 수 있다. |  |
| L1-09 | 신규 Vehicle 등록 순서 | 교육 서버에서 CommGroup→Vehicle→Line In→Station→OrderGroup 순서로 차량 1대를 반송 가능한 상태까지 등록할 수 있다. |  |
| L1-10 | System Comm Group 등록 | Comm Group 1건을 등록·저장하고, 지정한 차량의 IpAddress/PortNumber/ProtocolType 설정값을 화면에서 찾아 읽을 수 있다. |  |
| L1-11 | System Order Group 등록 | Order Group을 생성해 Vehicle·Station·Home을 넣고 저장하며, 특정 Station이 어느 Group에 속하는지 화면에서 확인할 수 있다. |  |
| L1-12 | ErrorTag 개별 등록·컬럼 | ErrorTag에서 지정 ErrCode를 찾아 8개 컬럼 값을 읽고 ErrorLevel로 중/경알람을 구분하며, 신규 Error 1건을 Insert할 수 있다. | `병기` |
| L1-13 | Tag Excel 일괄 편집 | 교육 서버에서 DOWNLOAD TAG→Excel 편집→OPEN TAG→CHECK TAG→OVERWRITE 9단계를 수행하고 CHECK TAG 결과로 이상 유무를 판단할 수 있다. |  |
| L1-14 | Parameter 진입·UI 표시값 | 지정한 Parameter(예: BlockingParam>PushWeight, ZoomFocusLevel)를 메뉴 경로로 찾아 현재 값을 읽어 보고할 수 있다. |  |

### Object 탭

| ID | 항목 | 할 수 있어야 하는 것 | 주의 |
|---|---|---|---|
| L1-15 | Vehicle Line In/Out·Prevent | 지정 차량을 Line Out(PM/BM·Comment 입력)→Line In하고 Prevent Call을 켜고 끈 뒤 InOutHistory에서 해당 Comment를 조회할 수 있다. |  |
| L1-16 | Vehicle 보조 명령·Clean | Vehicle popup에서 지정 차량의 Clean Mode를 On/Off하고, Sub Vehicle Command의 각 명령(Forcible Entry 포함)이 무엇을 하는지 말하며 매뉴얼 절차대로 실행할 수 있다. | `근거약` |
| L1-17 | Vehicle Set/Etc·IO 탭 | Set 탭에서 IoGroupNumber를 지정·저장한 뒤 IO 탭에서 IO 이름과 ON(초록) 비트를 읽고, Set/Etc 옵션 각각이 무엇을 바꾸는지 말할 수 있다. | `근거약` `추정` |
| L1-18 | Station 속성·Station Mode | 지정 Station의 속성값을 읽어 설명하고, Station Mode를 InService↔OutService로 전환한 뒤 화면에서 결과를 확인할 수 있다. |  |
| L1-19 | Station 포트·OnlineName 확인 | 지정 EQP Port·Transfer Buffer의 Duplicate/LongStay TimeOut/OnlineName 값을 읽고 Naming Rule과 대조해 오기·누락을 찾아낼 수 있다. |  |
| L1-20 | Point Type 7종 식별 | 지정 Point의 Type을 Object>Point에서 읽고 7종 각각의 주행 의미를 말할 수 있다. |  |
| L1-21 | CPS 상태 판독 | Object>CPS에서 각 CPS 상태를 읽고, DOWN/FAILOVER일 때 차량 진입 가능 여부를 말할 수 있다. |  |
| L1-22 | MTL 필드·배출 가능 상태 | Object>MTL 상태값 5개를 읽어 현재 차량 배출(또는 진입)이 가능한 상태인지 판정할 수 있다. |  |
| L1-23 | PLC 연결 파라미터 확인 | 지정 PLC Unit의 6개 연결 필드를 읽고 의미를 말하며, IP/Port 오기 시 PlcTag 값이 안 올라온다는 점을 화면에서 확인할 수 있다. |  |
| L1-24 | Ping Unit 등록 | 교육 서버에서 Ping Unit 1건을 등록·저장하고 Window>PingList에 나타나는지 확인할 수 있다. |  |
| L1-25 | PLC Tag Group 묶어보기 | 관심 비트 몇 개를 PLC Tag Group으로 묶어 저장하고 ON/OFF 상태를 화면에서 읽을 수 있다. |  |
| L1-26 | Graphic·Memo 표시 | 기존 Text Box의 Screen Name·FontAlignment를 바꿔 UI 문구를 수정하고, 객체에 Memo를 삽입할 수 있다. |  |

### Transfer 탭

| ID | 항목 | 할 수 있어야 하는 것 | 주의 |
|---|---|---|---|
| L1-27 | Transfer Command 수동 지령 | FROMTO/FROM/TO/MOVE/HOME 지령을 각각 생성해 OrderList에서 진행을 확인하고, HOME이 다른 Home으로 간 경우 정상인지 설명할 수 있다. |  |
| L1-28 | CycleMove 등록·시작·정지 | Call Disable 차량에 CycleMove를 등록해 시작·정지하고, CycleList에서 CURRENTCOUNT/TOTALCOUNT로 진행 횟수를 읽을 수 있다. | `근거약` |

### Report 탭

| ID | 항목 | 할 수 있어야 하는 것 | 주의 |
|---|---|---|---|
| L1-29 | TransferHistory 조회 | 지정 CassetteID 또는 CommandID의 반송 이력을 조회해 각 단계 시각과 구간 소요시간을 읽어 보고할 수 있다. |  |
| L1-30 | ErrorHistory 조회·Comment | 지정 기간·차량의 Error 이력을 조건 조회하고, 한 건에 조치내용 Comment를 입력·저장할 수 있다. |  |
| L1-31 | HSMSHistory 검색 | 지정 CommandID의 상위 메시지를 HSMSHistory에서 찾아 S/F와 Recv/Send 순서대로 나열할 수 있다. |  |
| L1-32 | Report 운영 이력 공통 조회 | 지정된 Report 화면(InOutHistory·InformHistory·RunningHistory·NackHistory·HandOverHistory·CassetteHistory·PingHistory·UserHistory·CpuRamHistory·CommHistory·UIHistory·FailOverHistory·Move History·Safety History)을 메뉴 경로로 열어 조건 입력→SEARCH→SAVE(Excel)를 수행하고, LogParam 보존기간을 넘는 날짜는 조회되지 않음을 확인할 수 있다. | `근거약` |
| L1-33 | Blocking·CommErr 이력 조회 | 지정 차량의 블로킹 이력에서 BlockedBy 차량을 읽고, CommErrHistory에서 Set/CLEAR 쌍과 발생 Point·Segment를 조회할 수 있다. |  |

### Statistics 탭

| ID | 항목 | 할 수 있어야 하는 것 | 주의 |
|---|---|---|---|
| L1-34 | Statistics Vehicle 조회 | 지정 기간 차량 가동률을 조회해 Excel로 저장하고, 특정 차량의 ErrorRate·BlockRate 값을 읽어 보고할 수 있다. |  |
| L1-35 | Statistics Transfer 조회 | Date/Vehicle/Station 탭을 전환해 스탭별 평균 소요시간과 RetryCountFrom/To를 읽고 Excel로 저장할 수 있다. |  |
| L1-36 | Statistics Error·ErrorProfiler | 지정 기간 다발 알람 상위 코드를 Statistics>Error에서 찾고, 그 코드를 ErrorProfiler로 조회해 Excel로 저장할 수 있다. |  |
| L1-37 | Statistics Quality 지표 | Quality 화면을 조회해 4개 지표 값을 읽고, 표의 TransferCount·ErrorCount로 MCBF가 맞는지 손으로 검산할 수 있다. |  |

### Window 탭

| ID | 항목 | 할 수 있어야 하는 것 | 주의 |
|---|---|---|---|
| L1-38 | OrderList ORDER 탭·개입 | OrderList에서 지정 오더의 Step·Status·색을 읽어 상태를 말하고, Pause/Resume/Hand Over/DestUpdate/Delete를 절차대로 실행할 수 있다. |  |
| L1-39 | OrderList NACK 탭 | NACK 탭에서 거부된 CommandID와 MESSAGE를 읽어 보고하고 확인 후 CLEAR하며, 과거 건은 NackHistory로 찾을 수 있다. |  |
| L1-40 | AlarmList·ErrorList 판독 | 알람 목록에서 중알람과 오래된 경알람을 색으로 구분하고, FOCUS로 발생 호기 위치를 찾아 ERRCODE·EVENT·ELAPSEDTIME을 보고할 수 있다. |  |
| L1-41 | PingList 판독 | PingList에서 CURERRORCOUNT가 증가 중인 Unit을 찾아 SETERRORCOUNT까지 남은 여유를 말할 수 있다. |  |
| L1-42 | TerminalMsg·DockSetting | TerminalMsg에서 상위 메시지를 읽고 지우며, DockSetting으로 서브창 배치를 바꾸고 원복할 수 있다. |  |
| L1-43 | CommEvent 창 열기 | CommEvent를 열어 지정 차량의 최신 메시지 행을 찾아 CurPoint·TargetPoint·Mode 항목 위치를 짚을 수 있다. |  |

### Layout 탭

| ID | 항목 | 할 수 있어야 하는 것 | 주의 |
|---|---|---|---|
| L1-44 | Layout Setting·Check 조작 | Layout>Setting으로 화면 배율을 맞추거나 Reset하고, Layout>Check를 실행해 Message 목록을 열어 볼 수 있다. |  |

### PlayBack 탭

| ID | 항목 | 할 수 있어야 하는 것 | 주의 |
|---|---|---|---|
| L1-45 | PlayBack Run 재현 조작 | 지정 시각 전후 10분을 불러와 배속을 바꿔 재생하고, 특정 시점의 차량 위치와 Error를 화면에서 짚을 수 있다. |  |
| L1-46 | PlayBack Export | 지정 시각의 PlayBack 30분 분량을 Export하고 저장 경로에서 파일을 찾아 전달할 수 있다. |  |

### Help 탭

| ID | 항목 | 할 수 있어야 하는 것 | 주의 |
|---|---|---|---|
| L1-47 | Help Version 확인 | Help>Version에서 각 구성 프로그램 버전을 읽어 기록하고 Show로 최근 Update 내용을 확인할 수 있다. |  |
| L1-48 | Help Define 색상 정의 | layout 화면에서 지정한 객체 색을 Help>Define과 대조해 그 객체 상태를 말할 수 있다. |  |
| L1-49 | OCS 주요 용어 | 화면·매뉴얼에 나오는 약어(MCS, MCCS, MCP, MTL, NCP(CPS), PIO 등)를 보고 무엇인지 한 줄로 말할 수 있다. |  |

### MCS_IF 프로그램 화면 (OCS 메뉴 밖)

| ID | 항목 | 할 수 있어야 하는 것 | 주의 |
|---|---|---|---|
| L1-50 | MCS_IF Cfg/SML 등록 확인 | 교육 서버에서 cfg/sml을 등록해 Select=True로 만들고 Xcom Config Info·Xcom SML File로 적용 여부를 확인할 수 있다. | `충돌` |
| L1-51 | 상위(MCS) 연결 확인 절차 | 상위 연결 4단계(IP 전달→Change to Select→S1F17→MCMD 점등)를 수행하고, Simulator로 S2F49 오더를 보내 OrderList 생성까지 확인할 수 있다. | `충돌` |

---

## L2 (70항목)

구조를 알고 어디를 찾아가야 하는지 아는가. 맵·통행영역은 화면 기능으로 수정하되, 거동을 규정하는 Parameter 값은 바꾸지 않는다.

### L2-a 맵·통행영역 수정 (18항목)

**Layout 같은 기능으로 맵을 수정할 수 있는가**

| ID | 항목 | 할 수 있어야 하는 것 | 화면·도구 | 주의 |
|---|---|---|---|---|
| L2a-01 | RDT 화면·경로 구성 | RDT를 실행해 버전과 기본 데이터 경로를 확인하고, 지정된 Point·Segment ID를 Navigation 트리에서 찾아 Select and Zoom으로 화면에 띄울 수 있다. | RailDesignTool 2 — 메인 창 / Save Path Configuration / Navigation 트리 |  |
| L2a-02 | RDT 사이트 신규 생성 | 배경 CAD 파일과 차량 제원을 지정해 RDT에 새 사이트·도면을 만들고, Finish Configuration 요약이 입력값과 맞는지 대조할 수 있다. | RailDesignTool 2 — File > New > Layout Configuration / Vehicle(s) Configuration / Finish Configuration |  |
| L2a-03 | RDT 열기·저장·개정 | 수정 전에 Save As로 사본을 만들고, 수정 후에는 Details를 기록해 Save한 다음, Open 창의 Revision History에서 원하는 개정판을 찾아 다시 열 수 있다. | RailDesignTool 2 — File > Open / File > Save / Save As / 사이트 우클릭 > Import Json File | `근거약` `추정` |
| L2a-04 | 세그먼트 작도 | 지정된 차량·작도 종류·템플릿으로 직선과 곡선 세그먼트를 이어 그리고, 작도를 정상적으로 끝맺을 수 있다. | RailDesignTool 2 — Edit 리본(선택 그룹), Edit > Object > Segment / LayOut Designer |  |
| L2a-05 | 객체 선택·편집·일괄이동 | 여러 포인트를 선택해 좌표를 일괄 정렬하고, 잘못된 편집을 Undo로 되돌리며, 조회만 할 때는 Lock을 걸어 맵을 보호할 수 있다. | RailDesignTool 2 — 디자인 작업 창 / Navigation 팝업 / 일괄 작업 창(Point Editing, Label Editing, Move the entire layout) | `추정` |
| L2a-06 | Point·Segment 속성 | Point Attributes의 Incoming/Outgoing으로 분기·합류 지점을 판별하고, Segment Attributes에서 Start/End Point·템플릿·Length·Travel Time을 읽고 좌표·각도를 고칠 수 있다. | RailDesignTool 2 — Point Attributes / Segment Attributes(General, Segment Parts) |  |
| L2a-07 | 템플릿·방향·궤도 표시 | 작도한 구간에 진행 방향과 차량 궤도를 표시해 템플릿의 Forward Direction과 실제 진행 방향이 일치하는지 확인할 수 있다. | RailDesignTool 2 — Segment Template Attributes / Tool > Direction / Tool > Swept / 디자인 창 우클릭 |  |
| L2a-08 | Drawing Attributes 설정 | 요청받은 설정(배경 레이어 숨김, 작도 영역 좌표, 특정 템플릿만 표시)이 6개 탭 중 어디에 있는지 찾아가 변경할 수 있다. | RailDesignTool 2 — Setup > Layout > Drawing Attributes / View > Drawing, Drawing Info |  |
| L2a-09 | System>Unuse 진입금지 | 우회경로를 확인한 뒤 지정 구간을 전체 또는 특정 호기에 대해 Unuse로 설정·해제하고, Layout 색상으로 적용 여부를 검증할 수 있다. | 메뉴 탭 > System > Unuse |  |
| L2a-10 | System>Home 등록 | 반송 Port 배치를 근거로 Home Point를 추가·Unuse·삭제하고 OrderGroup에 등록한 뒤, Layout 색상으로 결과를 확인할 수 있다. | 메뉴 탭 > System > Home / System > Order Group |  |
| L2a-11 | System>Cluster 영역 | Deadlock 우려 구간을 Cluster Point 집합으로 등록하고 MaxVehicleCount를 지정해 저장한 뒤, 재조회해서 포인트가 실제로 저장되었는지 확인할 수 있다. | 메뉴 탭 > System > Cluster (Cluster Point / Dest Point / Cluster Info·Setting) | `근거약` `추정` |
| L2a-12 | StationWeightGroup | 지정된 From·To Station 반송에 대해 우회시킬 Segment를 StationWeightGroup으로 등록·저장할 수 있다. | 메뉴 탭 > System > StationWeightGroup |  |
| L2a-13 | Object>Point Type 변경 | 설비 배치와 맞지 않는 Point Type을 찾아 올바른 Type으로 변경·저장하고 반영을 확인할 수 있다. | 메뉴 탭 > Object > Point (Point Type) |  |
| L2a-14 | UserBlock·DisableBlock | 특정 Point·Segment의 AutoBlock 목록을 조회하고 UserBlock/DisableBlock을 추가·제외해 저장할 수 있으며, 최초설치 Layout 점검표의 Block 설정 여부를 확인할 수 있다. | 메뉴 탭 > Object > Point / Object > Segment (AutoBlock, UserBlock, DisableBlock, AddWeight) |  |
| L2a-15 | Safety·CPS Interlock 영역 | Safety 또는 CPS의 Interlock Down Segment 범위를 설정·변경하고, CPS GroupNumber를 지정해 저장한 뒤 상태값을 확인할 수 있다. | 메뉴 탭 > Object > Safety / Object > CPS / Order List > Step 탭 |  |
| L2a-16 | Object>MTL 유지보수 존 | MTL Maintenance Zone의 Segment/Point 범위와 PIOPoint·PointNumber·DetourPointNumber를 설정·저장하고, 재조회로 SegList·PointList 반영을 확인할 수 있다. | 메뉴 탭 > Object > MTL |  |
| L2a-17 | AutoParkArea 대기구간 | AutoParkAreaGroup을 만들어 ParkArea Point를 지정하고, Sub Command로 차량을 대기구간에 넣고 빼낼 수 있다. | 메뉴 탭 > System > AutoParkArea |  |
| L2a-18 | Layout Run 객체 배치·수정 | Layout>Run에서 UI Object를 추가·정렬·UPDATE·DELETE하고, 수정 후 Layout>Check Message로 잘못된 설정을 찾아 수정할 수 있다. | 메뉴 탭 > Layout > Run / Check / Setting | `근거약` `추정` |

### L2-b 프로그램·시스템 구조 (32항목)

**Core / PLC Driver / MCS_IF 등 구조를 아는가**

| ID | 항목 | 할 수 있어야 하는 것 | 화면·도구 | 주의 |
|---|---|---|---|---|
| L2b-01 | OCS 실행 단위와 통신 상대 | 실행 단위 5요소를 나열하고, 각 단위의 통신 상대·프로토콜·담당 로그(CoreForm/MCSIF_Form/Secom/PLCDRIVERFORM)를 MCS→OCS→Vehicle/PLC 구성도 위에 그려 설명할 수 있다. | (프로그램 단위) Core.exe / MCS_IF.exe / PlcDriver.exe / RCPGT, Help>Version, SystemInfo | `충돌` |
| L2b-02 | RCPGT 웹 UI 구조 | RCP UI가 IIS 위 웹앱이라는 구조를 설명하고, 'UI가 안 열린다/다른 PC에서만 안 열린다' 현상에서 IIS 찾아보기로 1차 확인한 뒤 IIS 기능 누락·응용 프로그램 등록·URL/도메인·App 2.0·Config.asp DB IP 중 확인 지점과 점검 순서를 지목할 수 있다. | IIS 관리자 > Default Web Site > 응용 프로그램 추가 / 127.0.0.1/rcpgt / Config.asp |  |
| L2b-03 | Config 파일과 폴더·DB 배치 | 프로세스별 config 파일 이름과 위치를 짚고, 'Core(또는 PlcDriver·MCS_IF)가 기동 직후 죽는다' 현상에서 해당 config의 DB IP/ID/PW 불일치를 1순위 확인 지점으로 지목할 수 있다. 서버 폴더·DB 7종의 배치도 설명할 수 있다. | Core.exe.config / PlcDriver.exe.config / MCS_IF.exe.config / Config.asp, SSMS(DB 목록), 탐색기 D:\Program | `추정` |
| L2b-04 | 기동 순서와 Core 상태 전이 | Core를 먼저 띄우는 규칙대로 기동을 재현하고, Core가 WARMINGUP에 머무는 상황에서 10.1~10.4 중 어느 조건이 전이를 막고 있는지, Unknown Vehicle Position 알람이 왜 떴는지를 파라미터 관계로 설명할 수 있다. | Core.exe / PlcDriver.exe / MCS_IF.exe, CORE WARMINGUP·RUNNING 상태 표시, System>Parameter>SystemParam 10.1~10.4, ErrorList |  |
| L2b-05 | MCS_IF cfg 경로·HSMS IP | 낯선 사이트에서 MCS_IF cfg 파일을 경로 규칙으로 찾아내고, 드라이버 HSMS IP(0.0.0.0/VIP)와 config의 DB 접속 IP를 구분해 각각 어떤 연결을 좌우하는지 설명할 수 있다. | MCS_IF\<사이트명>\<사이트명>.cfg, MCS_IF.exe.config |  |
| L2b-06 | XCom CfgSml·HostNetworkName | MCS_IF가 안 올라오거나 상위 연결이 안 될 때 확인할 구성 지점 3개(XCom CfgSml Manager의 Select=True, HostNetworkName 대소문자 일치, XCOM Driver 설치)를 지목하고 각각이 왜 연결을 막는지 설명할 수 있다. | MCS_IF > XCom CfgSml Manager (Name / Sys Type / Upload / Select), MCS_IF.exe.config (HostNetworkName), 네트워크 연결(Host NIC 이름) |  |
| L2b-07 | 서버·네트워크 망 구성 | AP/DB 서버별 설치 대상, LOCAL/HOST/Mirror/HeartBit 랜포트 용도, Rose 3망과 LocalVIP/HostVIP의 관계를 구성도로 그리고, '차량 통신만 안 됨 / 상위만 안 됨' 현상이 어느 망·포트에 해당하는지 짚을 수 있다. | 네트워크 연결 > 속성, 서버 관리자 > 로컬 서버(NIC), RoseMirrorHA 구성도 |  |
| L2b-08 | Rose 리소스·Group·서비스 | Rose 리소스 5종과 Virtual IP 4요소의 역할을 설명하고, 절체 단위가 Group이라는 점과 매뉴얼명↔현장 서비스명 대응을 짚으며, 운영 서비스 장애가 Failover로 이어지는 조건(3600s 내 3회)을 설명할 수 있다. | RoseMirrorHA 콘솔 Resources(Virtual IP/Data/NT Service/File Shared/Agent), services.msc | `충돌` `버전` |
| L2b-09 | MCCSParam FailOver 요청 체계 | MCCSParam 4개 항목과 FailOver 트리거 3조건을 설명하고, '서버 자원 과부하나 상위 단절이 왜 절체로 이어졌는가'를 SystemParam 경고 Level3·HostDisconnectTimeout과 연결해 설명할 수 있다. | System > Parameter > MCCSParam (UseFailOverRequest, FailOverFilePath, FailOverFileName, HostDisconnectTimeout) | `버전` |
| L2b-10 | 자원 경고 Parameter 구조 | CPU/Memory 경고의 Level+SecTime 2단 구조와 알람명, HDDWarningSpaceGB의 동작을 설명하고, 해당 값이 SystemParam 10.5~10.17에 있음을 지목할 수 있다. | System > Parameter > SystemParam (10.5~10.17), LogParam, ErrorList | `충돌` |
| L2b-11 | 차량 통신 구조·Comm Group | Comm Group 5개 필드가 통신 경로(AP>Bridge>Vehicle PLC)의 어디를 정하는지 설명하고, Polling/Event 혼합 방식·주기 파라미터 3종의 차이를 짚으며, 차량 미인식·통신 불량 시 Comm Group 설정과 Comm History를 대조 지점으로 지목할 수 있다. | System > Comm Group, System > Parameter > SocketParam 8.1~8.3, Report > Comm History | `추정` |
| L2b-12 | OHT 전문 헤더·CMD 코드 | OHT 전문의 바이트 인덱스 구조와 방향별 [8]바이트 의미(subcmd/cmdresult) 차이, 주요 CMD 코드와 역방향(0xA0~0xA2) 구조를 설명할 수 있다. | OHT PROTOCOL 사양서, CoreForm Comm 로그 [S:11]/[S:2A]/[S:12] |  |
| L2b-13 | STATUS 메시지·S= 상태·IO | STATUS TYPE 4종과 보고 시점, S= 상태 문자의 정상 순환, SDR/SD 차이, Vehicle IO Tag가 IO Index에 이름을 붙여 Object>Vehicle IO 탭에 연결되는 구조를 설명할 수 있다. | OHT PROTOCOL 사양서, CoreForm Comm 로그 S=, System > Vehicle IO Tag, Object > Vehicle > Set > TemporaryParam > IoGroupNumber |  |
| L2b-14 | 주행·정지·이적재 지령 규칙 | 분기부 일괄 지령과 경로 재지령 원칙, PAUSE와 INTERLOCK STOP의 정지 위치·알람 차이, PreCommand 사용 여부에 따른 이적재 시퀀스 차이와 재전송 루프를 설명할 수 있다. | OHT PROTOCOL 사양서, System > Parameter (PIOParam 6.4/6.5, VehicleCommandParam 15.1~15.4, VehicleControlParam 16.10/16.11), Report > Comm History |  |
| L2b-15 | JCR·MTU·RFID·SCAN 부가 구조 | JCR/JCP 통신 구조와 장비군별 명칭 차이, MTU 진입·RFID·SCAN·청소/진단 모듈 시나리오의 정상 메시지 흐름을 설명하고, 자기 사이트에 어느 시나리오가 적용되는지 구분할 수 있다. | OHT PROTOCOL 사양서 3장·4장, System > Parameter (TimeoutParam 12.19, VehicleControlParam 16.7/16.8) |  |
| L2b-16 | HSMS·SECS-II 메시지 구조 | HSMS 프레임·헤더 필드와 Stream별 의미를 설명하고, 지원 S/F 목록에서 메시지 방향을 짚으며, S9F1~F7(스펙 불일치)과 S9F9(Transaction Timer time-out)를 구분해 설명할 수 있다. | SFA VHC BASIC/MESSAGE SPEC, Report > HsmsHistory, D:/XComLog |  |
| L2b-17 | HSMS 타임아웃 T3~T8 | T3/T5/T6/T7/T8/LinkTest의 정의·통상값을 말하고, 각각이 걸렸을 때 '이벤트만 남는가, 연결이 끊기는가'를 구분해 설명할 수 있다. | MCS_IF cfg (HSMS Parameter), SFA VHC BASIC SPEC 3.4 |  |
| L2b-18 | SVID·CEID·RPTID·VID 체계 | SVID/CEID/RPTID/VID의 관계를 설명하고 VID 번호 구간과 S1F3 세트를 짚을 수 있다. CEID 번호를 보면 해당 사이트 스펙(BASIC SPEC/현장 기준)을 먼저 확인한 뒤 이벤트 계통을 분류할 수 있다. | SFA VHC BASIC SPEC 5~6장, RCP Program setup 가이드 6.2 | `충돌` |
| L2b-19 | SEMI 상태 모델 | TSC·Transfer Command·Vehicle 상태 모델의 상태와 전이 이벤트를 그리고, CANCEL과 ABORT가 적용되는 상태(NOT ACTIVE/ACTIVE)의 차이와 PAUSED 상태에서 명령이 Queue에만 쌓이는 이유를 설명할 수 있다. | SFA VHC BASIC SPEC 4장 |  |
| L2b-20 | 상위 접속 시퀀스 | 상위 Online 접속의 정상 메시지 순서를 TSCState(Paused/Auto)별로 재현하고, 각 단계(S1F13/F17, S2F41 RESUME, S2F49)가 일으키는 상태 전이와 오더 생성을 설명할 수 있다. | XcomPro Simulator (S1F13/S1F17/S2F41/S2F49), MCS_IF (MCMD 점등), Report > HsmsHistory | `충돌` |
| L2b-21 | 원격명령·반송 정상 이벤트 | S2F41 RCMD 8종과 S2F49 TRANSFER의 파라미터 구조를 설명하고, 정상 반송·Buffer 반송·ABORT/CANCEL/PAUSE/RESUME의 S6F11 이벤트 순서를 기준선으로 재현할 수 있다. | SFA VHC MESSAGE/SCENARIO SPEC, Report > HsmsHistory | `충돌` |
| L2b-22 | Unit·Port 이벤트와 알람 메시지 | Unit/Port 이벤트와 WaitIn/WaitOut, S5F5/F6, CstSize 코드가 각각 무엇을 MCS에 알리는지 설명하고, 해당 사이트 스펙에서 대응 CEID·RPTID를 찾아 짚을 수 있다. | SFA VHC SCENARIO/MESSAGE/BASIC SPEC, Report > HsmsHistory | `충돌` |
| L2b-23 | Tag 3단 등록·매핑 규칙 | Tag 3단 등록 순서와 4쌍 매핑 규칙을 설명하고, 설비 알람 하나가 Object→PlcTag→ErrorTag 중 어느 등록에 의존하는지 짚으며, Exist Sensor 태그 누락이 RCPSTATION 알람으로 이어지는 구조를 설명할 수 있다. | Object Tag, System > PLC Tag (OPEN TAG), System > ErrorTag, System > Parameter > StationControlParam 9.1 | `충돌` |
| L2b-24 | PlcTag 파일 컬럼·분류 체계 | PlcTag 14컬럼이 각각 무엇을 정하는지 설명하고, 로그의 태그명(예: STATION_765_ALARMID)에서 TagName·TagProperty를 갈라 값의 종류(번호/상태/문자열/비트)를 판단할 수 있다. | System > PLC Tag, 260103_PlcTag_L30.xlsx, PlcTag 로그 | `추정` |
| L2b-25 | PLC 통신 구성과 감시 | Object>PLC 필드와 PlcGroup·물리 PLC 대응, PLC 데이터 동기화 주기, 반복 끊김만 알람으로 올리는 감시 구조를 설명하고, PLC 연동 확인 시 열어야 할 로그(PLC Tag Log/PlcCommLog)를 지목할 수 있다. | Object > PLC, Object > Ping, System > Parameter > SystemParam 10.18/10.20/10.21, PlcGroup, File Log > PLC Tag Log / PlcCommLog |  |
| L2b-26 | 설비별 태그 주소·Safety 거동 | STATION/CPS/MTL/SAFETY·MONITOR 태그의 속성과 주소 배치 규칙을 설명하고, MTL 투입/배출 판정 5개 값과 Safety 이벤트 시 범위 안팎 차량의 거동 차이를 설명할 수 있다. | System > PLC Tag, Object > Station / CPS / MTL / Safety, PlcTag 로그, Window > OrderList Step 탭 | `추정` |
| L2b-27 | ErrType 분류·ErrCode 대역 | 알람의 Type만 보고 차량/설비/네트워크/서버 계통을 1차 분류할 수 있다. ErrCode 대역으로 계통을 좁히되 두 판의 대역이 다른 계열(SYSTEM·PING·PLCCOMM·STATIONALARM)은 사이트 System>ErrorTag 화면으로 확인하고, CPS·FireDoor·PING의 번호 환산 규칙을 설명할 수 있다. | Window > AlarmList (Type/ERRCODE), System > ErrorTag, Report > ErrorHistory, 260103_ErrTag_L30.xlsx / ErrorDescription.xlsx | `병기` |
| L2b-28 | ErrCode·ErrEvent와 알람 계통 | AlarmList의 ERRCODE와 EVENT 컬럼을 구분해 읽고, VEHICLE ErrEvent 대역으로 계통을 말하며, SYSTEM 알람에서 PlcTag 주소로 넘어가는 경로와 중/경알람 정의를 설명할 수 있다. | Window > AlarmList (ERRCODE/EVENT), Report > ErrorHistory, System > ErrorTag / PLC Tag, System > Parameter > VehicleEventParam 17.3~17.10, OrderControlParam 5.18 | `병기` `근거약` |
| L2b-29 | Parameter 그룹 체계·기술 포맷 | 현상(예: 상위 큐 적체, 합류부 정체, PLC 끊김)을 듣고 열어야 할 Parameter 그룹을 지목하고, 파라미터 기술의 '참고' 필드에서 선행조건·0=미사용 같은 전제를 읽어낼 수 있다. | System > Parameter (Param Group / NAME / Value / SAVE), OCS Parameter 매뉴얼 | `근거약` |
| L2b-30 | 배차·주행 거동 Parameter | Order Weight 계산식과 HandOver·합류·Home/Parking 규칙을 설명하고, PushWeight 값에 따른 밀어내기 거리 차이, EntranceLimit 체크 상태의 의미(Cluster 과차량), UseBothWay의 적용 대상을 화면 값과 연결해 설명할 수 있다. | System > Parameter (OrderControlParam 5.5~5.12, priorityParam 7.2, TimeoutParam 12.8/12.9/12.13, SocketParam 8.3, BlockingParam PushWeight, TrafficParam 13.1), System > Cluster (EntranceLimit / MaxVehicleCount / MaxVehicleReleaseCount) |  |
| L2b-31 | AltTransfer·OrderGroup 등록 구조 | 경유지 반송 구성(Station·TransferUnit 배치)을 보고 필요한 OrderGroup·AltTransfer 등록 수를 산정하고, '특정 경로만 반송 불가' 현상에서 AltTransfer 등록 누락을 확인 지점으로 지목할 수 있다. | System > OrderGroup, System > AltTransfer | `근거약` `추정` |
| L2b-32 | Station·PIO·Host 연동 규칙 | Station·Buffer·PIO·MTL 대기 규칙과 이중입고/공출고 처리 흐름, PreTransfer·PreHandOff·CarrierDestRequest 메시지 흐름을 설명하고, 각 규칙이 어느 Parameter 그룹에 있는지 지목할 수 있다. | System > Parameter (StationControlParam 9.2/9.3, TimeoutParam 12.4~12.16, PIOParam 6.6, VehicleEventParam 17.11/17.12, HostParam 2.6~2.8, OrderControlParam 5.16/5.17), Station 설정(StrParm2) |  |

### L2-c 현상별 진입 경로 (20항목)

**문제가 생겼을 때 OCS 화면 어디를 찾아가야 하는지 아는가**

| ID | 항목 | 할 수 있어야 하는 것 | 화면·도구 | 주의 |
|---|---|---|---|---|
| L2c-01 | OCS 로그 4갈래 지도 | 현상 5건(예: 차량 정지 진행 중, 어제 반송 거부, 상위 S1F17 미수신 등)을 듣고 4갈래(File Log / DB History / UI 실시간 / XCom 로그) 중 1차 진입 갈래와 그 물리 위치나 화면을 지목할 수 있다. | File Log(RcpLogPath) / Report 탭 / Window>ErrorList·OrderList / D:\XComLog |  |
| L2c-02 | CoreForm 22종 용도 | CoreForm 로그 이름을 듣고 소속 군과 '이 로그를 여는 상황'을 말할 수 있다. 차량 문제의 1차 로그로 Comm을 지목하고, Test 로그는 운영 판단 근거에서 뺄 수 있다. | CoreForm 로그 폴더 (Comm, CommT, ..., MsgSend) | `충돌` `추정` |
| L2c-03 | MCSIF·PLC·Secom 로그와 용량 | 상위·PLC 문제를 듣고 MCSIF_Form / PLCDRIVERFORM / Secom 중 열 로그를 지목할 수 있다. Secom 로그를 열기 전에 시각·SystemBytes를 먼저 특정하는 진입 순서를 말할 수 있다. | MCSIF_Form / PLCDRIVERFORM / Secom 로그 폴더 | `충돌` |
| L2c-04 | 증상별 로그 진입 순서 9종 | 9개 증상 중 하나를 제시받으면 열어야 할 로그 3~4종을 순서대로 지목할 수 있다. | CoreForm / MCSIF_Form / PLCDRIVERFORM / Secom 로그 |  |
| L2c-05 | LogParam 로그 위치·보존기간 | 조사 대상 날짜가 주어지면 LogParam에서 RcpLogPath, 기록 스위치, 해당 LogPeriod* 값을 읽어 File Log가 남아 있는 위치와 대응 Report의 조회 가능 여부를 판정할 수 있다. | System > Parameter > LogParam (RcpLogPath, LogTrafficData, LogRecvData, LogDebuggingData, LogPeriod*) |  |
| L2c-06 | Report 보조 이력 질문 매핑 | 운영 질문 8개를 듣고 답이 있는 Report 화면과 확인할 컬럼을 지목할 수 있다. | Report > InOutHistory / InformHistory / RunningHistory / HandOverHistory / CassetteHistory / PingHistory / UserHistory / CpuRamHistory |  |
| L2c-07 | UIHistory로 변경자 추적 | '설정이 바뀐 뒤 문제가 생겼다'는 현상을 듣고 UIHistory에서 MessageName 검색어를 골라 변경 사용자·IP·시각을 짚어낼 수 있다. | Report > UIHistory (MessageName 검색) |  |
| L2c-08 | MCS 명령 거부 NackHistory | MCS 명령 거부 현상에서 NackHistory를 1차 화면으로 지목하고, PostOrderAbnormal 값을 확인해 이력이 비어 있는 이유를 가를 수 있다. | Report > NackHistory / Parameter > OrderControl 5.14 PostOrderAbnormal |  |
| L2c-09 | FailOver·절체 이상 진입점 | FailOver 또는 절체 이상 현상을 듣고 OCS 쪽(Report>FailOverHistory의 MODULE·COMMENT)과 Rose 쪽(Console>Log) 중 어디로 갈지 지목하고, MODULE 값으로 넘어간 프로그램을 짚을 수 있다. | Report > FailOverHistory (DATETIME/MODULE/COMMENT) / RoseMirrorHA Console > Log | `충돌` `근거약` |
| L2c-10 | 상위 통신 이력 진입 3갈래 | 상위 통신 문제를 듣고 XComLog 경로, HSMS History 화면, Wcf Log / Wcf Exception Log 중 열 곳과 찾을 문자열을 지목할 수 있다. | D:\XComLog / RCP UI > HSMS History / File Log > Wcf Log·Wcf Exception Log |  |
| L2c-11 | 차량 통신 이상 진입 경로 | 차량 통신 현상을 CommError와 No Response로 나누고, 진행 중이면 Comm History, 과거 구간 조회면 CommErrHistory, 원문이 필요하면 CommT 로그로 진입처를 지목할 수 있다. | Report > Comm History / Report > CommErrHistory / CommT·Ping·Warning 로그 |  |
| L2c-12 | UVP와 CommError 구분 | ErrorList의 알람 이름만으로 Unknown Vehicle Position과 CommError를 구분하고 각각의 진입 갈래(기동·위치 등록 vs 통신 경로)를 지목할 수 있다. | Window > ErrorList(AlarmList) / System > Parameter > SystemParam 10.1~10.4 | `병기` |
| L2c-13 | 차량·오더 타임아웃 알람 대응 | 4개 알람(LongStay / All Port Loading Fail / Unlocated Order is exist / Noway Timeout) 각각에 대해 대응 TimeoutParam 항목과 먼저 열 화면(OrderList·ErrorList·맵 Unuse)을 짝지을 수 있다. | Window > OrderList / ErrorList, System > Parameter > TimeoutParam 12.1·12.2·12.3·12.14·12.15 | `충돌` `병기` |
| L2c-14 | 상위·분기 타임아웃 알람 대응 | 상위 무명령 알람과 분기제어(JCP/JCR) 계열 알람을 듣고 대응 파라미터(12.17, 12.19, JunctionOccupyWaitTimeOutSec)와 진입처(상위 로그, PntOccupy)를 지목할 수 있다. | Window > ErrorList / System > Parameter > TimeoutParam 12.17·12.19, JunctionParam / PntOccupy 로그 | `병기` `근거약` `추정` |
| L2c-15 | 명령 후 무동작 MasterStop | '명령은 있는데 차량이 안 움직임' 현상에서 MasterStop 로그를 지목하고, LogDebuggingData 값으로 로그가 있는지를 판정할 수 있다. | Parameter > 12. Timeout Param 12.18 / 3. Log Param 3.3 LogDebuggingData / MasterStop 로그 | `근거약` |
| L2c-16 | 서버 리소스 알람 진입 | 92xxx~95xxx 서버 알람을 듣고 설비가 아니라 SystemParam 임계값, CpuRamHistory, Event 로그로 가야 함을 지목할 수 있다. | System > Parameter > SystemParam / Report > CpuRamHistory / Core Event 로그 | `충돌` |
| L2c-17 | PLCCOMM 알람→PlcGroup | PLCCOMM 알람 코드를 보고 해당 PLC(PlcGroup)를 지목하고 Object>PLC 화면과 PLC 로그 순서로 진입할 수 있다. | Window > AlarmList / Object > PLC / PlcTag·ReadWrite·PlcCommLog 로그 | `병기` |
| L2c-18 | 알람 원인 설명 찾기 | 알람 코드를 받고 ErrorDescription.xlsx에서 Description을 찾아내며, 설명이 비어 있는 계열(SYSTEM/STATIONALARM)은 다른 자료로 넘겨야 함을 지목할 수 있다. | Window > AlarmList (ERRTEXT) / ErrorDescription.xlsx Description 컬럼 | `병기` |
| L2c-19 | 기동 이상 단계 지목 | '자동 운전이 안 걸린다' 현상에서 4단계 상태값(XCOM SELECTED / CORE RUNNING / MCMD REMOTE / TSC AUTO) 중 멈춘 단계를 짚고, 그 단계에 맞는 로그나 화면을 지목할 수 있다. | MCS_IF / CORE 상태 표시, Core-Event·Core-TaskMgr 로그, Windows 이벤트 로그 | `근거약` |
| L2c-20 | DB Exception 로그 진입 | DB 이상이나 업데이트 후 이상 현상에서 날짜별 Exception 폴더를 지목하고, 반출·전달(에스컬레이션) 대상을 말할 수 있다. | D:\Program\Log\Core\<날짜>\Exception (DB Exception LOG) |  |

---

## L3 (62항목)

직접 처리할 수 있는가. 로그 판독·원인 특정·조치, 설정값 변경, Rose 조작, 맵 실 반영 전부.

### L3-a 로그 분석·처리 (41항목)

**직접 로그를 분석하고 문제를 처리할 수 있는가**

| ID | 항목 | 할 수 있어야 하는 것 | 화면·도구 | 주의 |
|---|---|---|---|---|
| L3a-01 | Comm 상태보고 필드 판독 | Comm 로그 상태보고 원문 한 줄과 CommHistory Message 한 줄을 받아 E/S/JOB/CP/DP/TP/ST/SEG/B= 비트를 필드별로 해석하고, 차량이 인터락·PAUSE·에러 중 어느 상태인지 판정할 수 있다. | CoreForm Comm 로그 [R:01] / Window>CommEvent / Report>CommHistory | `근거약` |
| L3a-02 | 오더 생애주기·정체 단계 판정 | 한 차량의 Comm 로그 시계열을 받아 오더 1건의 시작~종료를 재구성하고, 멈춘 단계와 원인 방향(배차/주행/이적재 PIO)을 특정할 수 있다. | CoreForm Comm 로그 (CP·DP·ST·TP·S·P 열) | `충돌` |
| L3a-03 | 명령 전문 분해·응답 판정 | OHT 명령 HEX 전문과 응답 전문을 바이트 단위로 분해해 명령 종류·경로·JobNumber를 읽고, 응답 코드 또는 응답 누락으로 명령 실패 원인을 판정할 수 있다. | CoreForm Comm 로그 [S:xx]/[R:xx] (Packet 기록 시) / OHT PROTOCOL 사양서 |  |
| L3a-04 | 상태 전문 TYPE 0x01/0x02 판독 | TYPE 0x01/0x02 상태 전문을 받아 AS 작업상태와 ST 비트 조합(OR)을 분해하고, 포인트 필드 변화로 차량 위치와 화물 ID를 판정할 수 있다. | OHT PROTOCOL 사양서 TYPE 0x01/0x02 / Comm 로그 Packet | `충돌` |
| L3a-05 | 맵 업데이트 차단·프로토콜 불일치 | Version 전문의 RES 값과 Comm Log의 'Invalid Message Size Received'를 근거로 특정 차량의 맵 업데이트 중단이나 프로토콜 불일치 원인을 특정할 수 있다. | OHT PROTOCOL TYPE 0x04 / Comm Log / System>Parameter>8. Socket Param>8.10 StatusPacketCheckSize | `버전` |
| L3a-06 | 합류부 점유 판독·고착 판정 | PntOccupy 로그와 점유 요청/응답 전문으로 합류부 통과 순서를 재구성하고, 합류 대기가 정상 대기인지 점유 고착·Door 닫힘·정보 불일치인지 특정할 수 있다. | CoreForm PntOccupy 로그 / OHT PROTOCOL 0xA1·0xA2·JCR 0x02·0x03 | `근거약` `추정` |
| L3a-07 | 통신 지연 서버/차량/무선 판정 | CommT·Warning·CommErrHistory를 집계·대조해 통신 지연의 원인이 서버측 부하인지, 특정 차량인지, 특정 무선 구간(AP)인지 특정할 수 있다. | CoreForm CommT / Warning 로그 / Comm 말미 대괄호 / Report>CommErrHistory / PowerShell Select-String | `추정` |
| L3a-08 | Ping 2채널 판독·단절 판정 | Ping 로그를 차량별 채널 1/2로 짝지어 PingList·PingHistory와 대조하고 '이중화만 깨짐'과 '통신 단절'을 판정해, 단절이면 CMD 구간 분리(L3a-09)로 넘기는 결정을 내릴 수 있다. | CoreForm Ping 로그 / Window>PingList / Report>PingHistory / CMD(ping, tracert, telnet, netstat, arp, nbtstat) | `추정` |
| L3a-09 | CMD 결과로 장애 구간 특정 | 여러 CMD 결과를 조합해 장애 구간(서버·AP·Bridge·차량 PLC·포트·IP 충돌)을 특정하고 조치·에스컬레이션 대상을 결정할 수 있다. | CMD 진단 명령 세트 |  |
| L3a-10 | Event 자원·큐·Old Data Delete 판정 | Event 로그의 CPU/RAM/DB·HQ·PQ 값과 Old Data Delete 소요시간을 계산·대조해 서버 느림이 일시 부하인지, DB 삭제 작업 때문인지, 큐 적체(어느 큐)인지 판정할 수 있다. | D:\Program\Log\Core\날짜별\Event / SystemInfo>HARDWARE / ErrorList / 로그 파일 뷰어>DeleteOldHistoryPlayBackJob | `충돌` `버전` `근거약` |
| L3a-11 | MCCSParam FailOver 트리거 판정 | FailOverHistory 1건과 MCCSParam·System Param 설정값을 대조해 FailOver가 CPU / Memory / Host Disconnect 중 어느 트리거로 요청됐는지 특정하고, 임계값 조정이 필요한지 에스컬레이션 여부를 판단할 수 있다. | Parameter > 4. MCCS Param(4.1~4.4) / 10. System Param(10.7, 10.10, 10.13, 10.16) / Report > FailOverHistory / FailOver 요청 INI 파일 | `충돌` `버전` `근거약` |
| L3a-12 | UIException 중문 예외 해독 | UIException의 중문 다중 라인 예외를 해독해 DB 연결 단절 여부를 판정하고, 발생 빈도를 계수해 무시할지 DB/네트워크 점검으로 에스컬레이션할지 결정할 수 있다. | CoreForm UIException 로그 | `추정` |
| L3a-13 | 정상 기준 대비 이상·노이즈 분리 | 여러 로그의 집계치를 정상 기준과 비교해 이상 항목을 골라내고, 그중 근본원인·증상·노이즈를 분리해 원인 후보 하나를 근거와 함께 제시할 수 있다. | Event·Ping·CommT·PntOccupy·VehicleEvent·OrderNack·MsgSend·Finder·MoveHistory·Warning·CommException 로그 | `추정` |
| L3a-14 | 조인 키로 다중 로그 재구성 | 주어진 사건 하나(예: 실행되지 않은 Host 지시)에 대해 조인 키를 골라 3개 이상 로그를 이어 붙이고, 시간순 타임라인으로 사건을 재구성할 수 있다. | CoreForm / MCSIF_Form / PLCDRIVERFORM / Secom 로그 전체, grep·PowerShell Select-String | `병기` |
| L3a-15 | Order [N.] 끊긴 단계 특정 | Order 로그를 작업번호로 추적해 5단계 중 끊긴 단계를 특정하고, 원인 방향(배차 실패/주행 정체)과 다음에 열 로그를 근거와 함께 제시할 수 있다. | CoreForm Order 로그 [N. nnnn] ↔ Comm JOB= | `근거약` |
| L3a-16 | Host 지시 거부 판정·에스컬레이션 | OrderNack·MCSSystem을 CmdID·EventNumber로 조인해 Host 지시 거부 사유를 특정하고, OrderGroup 설정을 대조해 OCS 내부 조치 대상인지 MCS(상위) 에스컬레이션 대상인지 결정할 수 있다. | CoreForm OrderNack / MCSIF_Form MCSSystem 로그 / Report>NackHistory / System>OrderGroup / Parameter 5.15 |  |
| L3a-17 | 배차·인계 추적과 가중치 조정 | SelectOrder·HandOver·OrderFail을 작업번호로 이어 배차 선택 근거와 인계 이력을 재구성하고, 떠도는 작업을 판정해 HandOverWeight·Priority 파라미터 조정안을 제시할 수 있다. | CoreForm SelectOrder / HandOver / OrderFail 로그 / System>Parameter>7. Priority Param, 13. Traffic Param 13.13 | `추정` |
| L3a-18 | 정체 레일·경로 계산 판독 | MoveHistory 집계와 Finder·TM 원문으로 정체 레일과 경로 이상(탐색 지연, 계산 중단 지점)을 특정할 수 있다. | CoreForm MoveHistory / Finder / TM 로그 | `추정` |
| L3a-19 | 블로킹 원인·PushWeight 검증 | BlockingHistory 연쇄 추적과 BlockRate 교차검증으로 블로킹 원인 차량과 성격을 특정하고, PushWeight 조정 결과를 검증하거나 Move 명령으로 우회 조치할 수 있다. | Report>BlockingHistory / Statistics>Vehicle>BlockRate / System>Parameter>BlockingParam>PushWeight | `근거약` `추정` |
| L3a-20 | HomeChange 홈 재배치 판독 | HomeChange 로그로 차량이 그 위치에 대기하게 된 경위(대피·연쇄 재배치·가상 포인트)를 판정할 수 있다. | CoreForm HomeChange 로그 | `추정` |
| L3a-21 | VehicleEvent 혼잡도 해석 | VehicleEvent의 VEHICLE_30/31 건수와 연쇄 해제 시점을 집계해 라인 정체의 심화와 해소 구간을 특정할 수 있다. | CoreForm VehicleEvent 로그 | `추정` |
| L3a-22 | Host 메시지 체인 추적 | MsgRecv·MsgSend·WCFMsgTransfer·XML을 이어 Host 지시의 도착 여부, 송신 적체, 채널별 이벤트 처리 실패, 수동 조작 주체를 판정할 수 있다. | CoreForm MsgRecv / MsgSend, MCSIF_Form WCFMsgTransfer / WCFMsgTransferXML 로그 | `추정` |
| L3a-23 | SECS 전문 SysByte 체인 판독 | SecsMsgTransfer·SECS-II·SECS-I를 SystemBytes로 조인해 특정 보고 1건의 송신·응답·거부 여부를 바이트 수준까지 판정할 수 있다. | MCSIF_Form SecsMsgTransfer / Secom SECS-II / SECS-I 로그 | `충돌` |
| L3a-24 | S9·HSMS 타임아웃 원인 판정 | 끊김 로그와 S9 메시지를 보고 상위 통신 이상이 스펙 불일치(S9F1~F7)인지 타임아웃(S9F9·T3~T8·LinkTest)인지 가르고, 어느 타임아웃이 걸렸는지와 멈춘 메시지를 역추적할 수 있다. | Secom SECOMDRIVER 로그 / SECS-II 로그 / HSMS Parameter(T3, T5, T6, T7, T8, Link Test) |  |
| L3a-25 | PlcTag 알람 구간·ErrTag 조인 | PlcTag ST·ALARMID 시계열과 ErrTag 조회로 설비 알람의 내용과 발생~복구 구간을 확정하고, 자료 불일치(ErrTag/ErrorDescription, Comment/TagProperty)로 인한 오판을 피할 수 있다. | CoreForm PlcTag 로그 / System>ErrorTag / System>PLC Tag / 260103_ErrTag_L30.xlsx | `병기` `추정` |
| L3a-26 | Not Define 알람 처리 | Not Define 알람을 'ErrorTag 미등록 + 원래 이벤트 발생'으로 해석해 발생 ErrType·ErrEvent를 찾아내고, 원래 이벤트 처리와 별개로 매핑 규칙과 차량 담당자 확인 절차에 따라 ErrorTag(필요 시 17.x Parameter)를 보완할 수 있다. | Window>AlarmList / System>ErrorTag / System>PLC Tag / Parameter>17. VehicleEvent Param | `추정` |
| L3a-27 | 카세트 ID PLC 경로 추적 | PlcTag·MsgTransfer·ReadWrite·PlcCommLog를 이어 카세트 ID 불일치가 센서, DB 기록, PLC 통신 중 어디서 생겼는지 특정할 수 있다. | CoreForm PlcTag, PLCDRIVERFORM MsgTransfer / ReadWrite / PlcCommLog 로그 / System>PLC Tag | `근거약` |
| L3a-28 | HCACK·CPACK 거부 원인 판정 | S2F42/S2F50 응답의 HCACK와 CPACK 쌍을 읽어 MCS 명령이 거부된 원인 파라미터와 중복 지령 유형을 특정할 수 있다. | SECS-II 로그 S2F42 / S2F50 / SECS Data Items 참조표 | `충돌` `근거약` |
| L3a-29 | 반송·차량 VID 코드 판정 | S6F11/S1F4의 VID 값으로 반송이 어떤 사유(Host/수동/자동/PIO Timeout)로 끝났는지, 지령 주체가 MCS인지 OCS 수동인지, 차량이 Jam/Stuck/통신단절 중 어느 상태인지 판정할 수 있다. | SECS-II 로그 S6F11 / S1F3·S1F4 | `충돌` |
| L3a-30 | S6F11 CEID·RPTID 본문 판독 | S6F11 원문을 받아 CEID와 RPTID로 리포트 포맷을 결정하고 본문 필드(위치·상태·ResultCode 등)를 판독할 수 있다. | SECS-II 로그 S6F11 / 에뮬레이터 SECS-II 통신 로그 | `충돌` `근거약` `추정` |
| L3a-31 | 알람 3중 보고 대조 | 한 알람의 S5F1·AlarmSet·UnitAlarmSet 3건을 짝짓고 ALCD 비트를 분해해 발생/해제와 카테고리, 진행 중 반송에 미친 영향을 판정할 수 있다. | SECS-II 로그 S5F1 / S6F11 / MsgSend 로그 | `충돌` `추정` |
| L3a-32 | PIO Interlock 자동 복구 추적 | ResultCode=64와 CarrierLoc으로 적재/하역 실패를 구분하고, Once Retry → AbortLocation → Manual Handling 단계 중 현재 위치를 판정해 수동 개입 시점과 방법(MCS 재지령/OCS Manual Transfer)을 결정할 수 있다. | SECS-II 로그 S6F11·S2F49 / TSC(OCS) Manual Transfer / Parameter>6. PIO Param 6.1~6.3 | `충돌` |
| L3a-33 | BCR NG·UNKNOWN ID 추적 | CEID 조합과 IDReadStatus/ResultCode로 BCR NG 유형을 판정하고, UNKNOWN CarrierID를 분해해 유령 카세트의 발생 시점과 경위를 추적할 수 있다. | SECS-II 로그 S6F11(151~154, 203, 251, 107) / OrderNack CstID | `충돌` |
| L3a-34 | Empty Retrieval·Double Storage 판정 | TransferPaused 이후 이벤트 조합으로 Empty Retrieval과 Double Storage를 구분하고, STB Double Storage에서 Manual Order 생성이 필요한 시점을 결정할 수 있다. | SECS-II 로그 S6F11·S2F41 / OCS Manual Order 생성 | `충돌` |
| L3a-35 | Cancel·Abort 유형·주체 식별 | CEID 254 선행 여부, REPLACE 값, 후속 이벤트로 취소·중단의 유형과 주체(MCS/OCS 운전자/Vehicle Removed)를 식별하고, 3중 DB 정합성이 맞는지 판정할 수 있다. | SECS-II 로그 S6F11(254, 101~106, 154, 153, 208, 209) / TSC Transfer Command Delete / MCP CarrierRemoved | `충돌` |
| L3a-36 | Controller Down→Up 복구 검증 | Controller 재기동(또는 Rose Failover) 후 SECS 로그로 복구 시퀀스를 재구성하고, 다운 전 명령이 모두 다시 보고되어 운전이 재개됐는지 검증할 수 있다. | SECS-II 로그 / SECOMDRIVER 로그 / S1F3·S1F4 | `충돌` |
| L3a-37 | 안전 파라미터 쌍 해제 위험 | 안전 관련 파라미터 쌍의 의존 관계와 해제 시 위험을 설명하고, 변경 요청을 받았을 때 짝 파라미터·차량 프로토콜 지원·충돌 위험을 확인해 승인 여부를 판단할 수 있다. | System>Parameter>12. Timeout / 16. VehicleControl / 17. VehicleEvent Param / Window>CommEvent |  |
| L3a-38 | 경로 소실 위험 값 판단 | Noway Timeout 발생 시 UnuseByStationPenaltyMSec 과대 설정을 원인 후보로 특정하고, 경로 소실을 부르는 Penalty·PassPoint 변경 요청의 위험을 판단할 수 있다. | System>Parameter>13. Traffic Param 13.15 / 10. System Param 10.19 / ErrorList | `추정` |
| L3a-39 | 경로·점유 거동 파라미터 튜닝 | 블로킹·우회·정체·재가속·정위치 실패 현상에 대해 조정할 파라미터와 방향(증감)을 근거와 함께 제시하고, 하드웨어 점검으로 에스컬레이션할 경계를 판단할 수 있다. | System>Parameter>5. OrderControlParam / 12. Timeout / 13. Traffic / 16. VehicleControl / OHS CheckAllocPoint | `근거약` |
| L3a-40 | 분석용 로그·기록량 조정 | 분석 목적에 필요한 디버깅·Packet·리소스 로그를 켜고 분석 후 원복하며, 차량 대수에 맞춰 로그 기록량과 MonitoredVehicle 전송 분할을 조정할 수 있다. | System>Parameter>2. Host Param / 3. Log Param / 8. Socket Param / 11. TaskMgrParam |  |
| L3a-41 | 디스크 용량 관련 설정 조정 | HDD 여유 용량과 SQL 사양을 근거로 백업 주기·보존기간·PlayBack 삭제량 값을 산정·변경하고 그 영향(HDD 경고)을 예측할 수 있다. | System > Parameter > DataBaseParam / LogParam / SystemParam(HDDWarningSpaceGB) | `충돌` |

### L3-b Rose 서버 이중화 (13항목)

**Rose 이중화 프로그램을 다룰 수 있는가**

| ID | 항목 | 할 수 있어야 하는 것 | 화면·도구 | 주의 |
|---|---|---|---|---|
| L3b-01 | Console 접속·상태 판정 | Replace IP 환경에서 Heartbeat IP로 콘솔에 로그인하고, Server/Group/Agent/NICs 4요소를 읽어 '이중화 정상/비정상'과 그 근거 요소를 제시할 수 있다. | RoseMirrorHA Control Center > 호스트명 우클릭 > Login / Console 상태 화면(Server·Group·Agent·NICs) | `근거약` |
| L3b-02 | Group 기동·정지·강제기동 | Group 상태(Online/Offline, 한 노드 장애)가 주어지면 Bring In / Bring Out / Force Start 중 허용되는 명령을 골라 중문 UI에서 실행하고, Delete가 운영서비스 중지를 요구한다는 점을 들어 운영 중 사용 금지를 설명할 수 있다. | Rose Console > Group 우클릭 > Bring In(带入) / Bring Out(带出) / Force Start(强制启动) / Delete | `버전` `근거약` |
| L3b-03 | 수동 절체·역절체 | 복제 정상을 확인한 뒤 수동 절체를 실행하고, 절체 후 서비스를 확인한 다음 역절체로 원래 Active 노드에 서비스를 되돌릴 수 있다. | Rose Console > Group 우클릭 > Fail Over / Take Over (현장: 切换) | `근거약` |
| L3b-04 | Failover 후 서비스 검증 | 절체 직후 VIP로 RCP UI 접속 여부와 FailOverHistory 기록을 확인해 서비스가 새 Active 노드로 정상 인계됐는지 판정하고, 반송 명령 생존 검증(L3a-36)이 필요한지 결정할 수 있다. | VIP로 RCP UI 접속 / Report > FailOverHistory / SECS(HSMS) 로그 | `충돌` `추정` |
| L3b-05 | Replication 조작·판독 | Full Mirror·Verify를 실행하고 진행률을 읽으며, Transmit 색상(녹색/노란색)과 Target Side Pause 표시로 복제가 정상인지 일시중지인지 판정하고 Resume으로 되돌릴 수 있다. | Rose Console > Group 우클릭 > Full Mirror / Verify / Transmit / Target Write Disk |  |
| L3b-06 | Snapshot 생성·스케줄·관리 | 작업 전 수동 스냅샷을 생성하고, 스케줄·저장 한도를 확인·변경하며, Snapshot Manage에서 DELETE만 사용하고 REVERT를 쓰지 않을 수 있다. | Rose Console > Group 우클릭 > Snapshot > Take Snapshot / Scheduling Snapshot / Snapshot Manage |  |
| L3b-07 | Recover Snapshot 복구 | Downtime 승인을 전제로 Recover Snapshot 마법사를 끝까지 진행하면서 Recover Mode를 매뉴얼 지시대로(Compare file content 선택, Recover to specified path 해제) 설정하고, 5개 옵션 각각의 매뉴얼 정의를 말할 수 있다. | Rose Console > Group 우클릭 > Snapshot > Recover Snapshot |  |
| L3b-08 | 계획 작업(Update·Patch) | Windows Update와 DB Patch 작업에서 Downtime 필요 여부를 가르고, 각 절차를 순서대로 수행하며 절체·Verify를 넣어야 하는 지점을 지목할 수 있다. | Rose Console(Bring Out / Bring In / Verify / Failover) + services.msc(SQL Server 서비스) |  |
| L3b-09 | 장애 유형별 판정·대처 | 장애 노드(Active/Standby)와 장애 망(Public/Heartbeat/Mirror), OS Hang 여부가 주어지면 Failover 발생 여부와 운영 영향을 판정하고 1차 조치(강제종료·강제 재시작·Mirror 망 복구 우선)를 결정할 수 있다. | RoseMirrorHA Console(Server·Group·NICs 상태, Log 영역) / ncpa.cpl(Host, Heartbeat, Mirror) / Windows 서버 콘솔 | `근거약` |
| L3b-10 | Rose 통신 전제 점검 | Failover 미동작 상황에서 보안솔루션·방화벽의 Rose 포트 5개와 설치 경로·프로세스 등록을 점검해 누락 항목을 찾아 시정하고, 매뉴얼 프로세스명과 현장 서비스명을 대조할 수 있다. | Windows Firewall Inbound 규칙 / 보안솔루션 예외 등록 / Server Manager > NIC Teaming | `충돌` |
| L3b-11 | DB 미러링 경로 점검 | Sp_helpfile과 SSMS 속성으로 DB 파일이 미러링 경로에 있는지 판정하고, StandBy 미러디스크 접근 시험으로 이중화가 실제로 걸렸는지 판정할 수 있다. | SSMS > DB 우클릭 > 속성 > 파일 / Server 우클릭 > 속성 > 데이터베이스 설정 / Sp_helpfile / StandBy 서버 미러디스크 |  |
| L3b-12 | 서버 단독 실행 | 단독 실행 5단계를 순서대로 수행하고, 단계를 빠뜨리거나 단계 순서를 바꿨을 때 생기는 결과(서비스 정지, DB 미기동, IP 미할당)를 말할 수 있다. 프로그램 기동은 Core를 먼저 띄웠는지만 채점한다. | Rose Console > Group(IMS) 우클릭 > 带出 / services.msc / ncpa.cpl / D:\Program\Core·MCS_IF·PLCDRIVER |  |
| L3b-13 | 단독 실행 후 이중화 복귀 | 단독 실행 상태에서 이중화로 되돌리는 역순 절차를 단계별로 제시하고, 단계마다 근거 문서가 있는지 없는지 구분하며, 복귀 후 Verify로 복제 정합성을 확인할 수 있다. | services.msc / ncpa.cpl / Rose Console > Group 우클릭 > Bring In(带入) / Full Mirror / Verify | `자료없음` `근거약` `추정` |

### L3-c RailTool layout 업데이트 (8항목)

**RailTool로 layout을 업데이트할 수 있는가**

| ID | 항목 | 할 수 있어야 하는 것 | 화면·도구 | 주의 |
|---|---|---|---|---|
| L3c-01 | 차량 제원 변경 영향 판단 | 제시된 제원 변경(예: Length 또는 Front detection distance 증가)이 Swept·오토블로킹 결과에 주는 영향을 설명하고, 변경 후 재계산·재검증 절차를 수행할 수 있다. | RailDesignTool > Steer Drive Vehicle(s) Configuration / Differential Drive / QUAD 설정창 (Length, Width, Rear·Front detection distance, Reference Point, Lock/Release) |  |
| L3c-02 | Safety Margin 설정 | Safety Margin 값을 변경해 오토블로킹을 재계산하고, 변경 전후의 블로킹 결과 차이를 확인할 수 있다. | RailDesignTool > Setup > Layout > [Auto-Blocking Configuration] / Drawing Attributes > Auto Blocking Configuration > General > Safety Margin |  |
| L3c-03 | 오토블로킹 생성·Swept 검증 | Auto Blocking 창에서 Progress Unit의 의미를 말하고 값을 정해 오토블로킹 목록을 생성한 뒤, 지정된 Point/Segment의 Swept를 띄워 궤도 유형을 식별하고, 인접 궤도와의 겹침으로 블로킹 결과의 타당성을 판정할 수 있다. | RailDesignTool > 사이트 우클릭 > Auto Blocking (Progress Unit, Start Auto-Blocking List Creation, Point Swept, Segment Swept, Show All, Clear, View Logs, Export, Cancel) | `근거약` `추정` |
| L3c-04 | 오토블로킹 계산로그 판독 | 오토블로킹 계산 로그에서 중단된 단계를 짚어내고, View Logs 결과에서 지정 세그먼트의 블로킹 대상 세그먼트를 찾아낼 수 있다. | RailDesignTool > Auto-Blocking / Export JSON File 로그 창, View Logs > 'Segment Blocking Segment' 목록 |  |
| L3c-05 | Export JSON 산출 | 오토블로킹 계산이 완료된 맵을 Export JSON File 절차로 내보내고, 산출 파일의 경로와 생성 여부를 확인할 수 있다. | RailDesignTool > 사이트 우클릭 > Export Json File / 'Export JSON File' 창 (Json File, Search, Progress Unit, Start Auto-Blocking List Creation, Export, Cancel) | `근거약` |
| L3c-07 | MapLoad 반영·백업 확보 | 테스트 서버에서 MDB 파일과 BackupPath를 지정해 MapLoad(MDB->SQL)를 수행하고, 반영 전 MDB 저장 날짜·파일명 확인과 반영 후 백업 폴더 생성 확인을 빠뜨리지 않으며, 복귀에 쓸 직전 MDB와 백업 위치를 지목할 수 있다. | OCS UI System -> MapLoad / Core > System 탭 > MabLoad / Layout > MapLoad (MDB File Path, BackupPath, MDB->SQL 또는 UPDATE) | `근거약` `추정` |
| L3c-08 | MapLoad 실패 조치 | MapLoad가 실패했을 때 AccessDatabaseEngine 설치 여부·비트·Office 충돌을 점검하고, 재설치 조치를 결정·수행할 수 있다. | AccessDatabaseEngine 설치본, Core > MapLoad |  |
| L3c-09 | 실 시스템 영향 판정 | 제시된 맵 작업 목록의 각 조작이 도구 내부에서 끝나는지 실 시스템에 영향을 주는지 판정하고, 실 반영 조작에 필요한 선행 조치를 제시할 수 있다. | RailDesignTool File > Open / Save ↔ 사이트 우클릭 > Auto Blocking, Export Json File / OCS System -> MapLoad | `추정` |

---

## 보조 — 7개 목표 밖 (27항목)

정기점검·네트워크 장비·설치 기준·SNMP/REST. 발주자 7개 목표 어디에도 딱 맞지 않지만 현장 운영에 필요한 것들입니다. 설치할 때 기준대로 하는 것은 L2, 운영 중 설정을 바꾸는 것은 L3로 매겼습니다.

| ID | 레벨 | 항목 | 할 수 있어야 하는 것 | 주의 |
|---|---|---|---|---|
| AUX-01 | L1 | DB·Agent 서비스 기동 점검 | services.msc와 SSMS 작업 활동 모니터를 열어 DB/Agent 서비스 상태와 실패한 Job을 찾아 정상/비정상을 판정할 수 있다. |  |
| AUX-02 | L1 | MDF·LDF·테이블 증가 점검 | SQLData/SQLLog 폴더와 SSMS 테이블 사용량을 조회해 비정상 증가 중인 DB 파일·테이블을 지목할 수 있다. | `근거약` |
| AUX-06 | L1 | 설치 기준·필수 S/W 확인 | 설치 기준서와 레지스트리를 보고 서버에 필수 S/W·버전이 갖춰졌는지 체크리스트로 판정하고 비인가 S/W를 지적할 수 있다. | `충돌` `버전` |
| AUX-11 | L1 | 반입 전 현장·IP·Port 신청 | 서버 반입·IP·Port·Wips 신청에 필요한 확인 항목과 제출 정보를 체크리스트로 빠짐없이 준비하고 Server IP를 설정·확인할 수 있다. |  |
| AUX-19 | L1 | MOXA 장비 접속·자료 Export | 노트북 IP를 맞춰 MOXA AP/스위치 콘솔에 접속하고 Troubleshooting Export 파일을 확보할 수 있다. | `근거약` |
| AUX-22 | L1 | Switch/HUB 모니터 화면 판독 | 모델별 메뉴 경로로 포트 Count·Monitor·SFP 화면을 열어 항목·색상 의미를 읽고 점검 캡처를 남길 수 있다. | `근거약` |
| AUX-03 | L2 | History DB·Agent Job 연쇄 | History 테이블이 안 생기거나 안 지워질 때 Agent Job 등록·실행 → LogParam 보존기한 순으로 원인 위치를 설명하고 해당 Job을 지목할 수 있다. |  |
| AUX-04 | L2 | SQL 메모리 점유·상한 판정 | SQL Server 메모리 점유와 최대 서버 메모리 설정을 비교해 무제한(2147483647) 설정의 위험을 지적하고 사양 기준 상한 설정 필요 여부를 판정할 수 있다. | `충돌` `근거약` |
| AUX-05 | L2 | DB 백업 계획·경로 확인 | 유지관리 계획과 DBBackupFolder/DBBackupFolder2 설정을 읽어 백업 7종 파일 생성 여부와 2차 경로 분리 여부를 판정할 수 있다. |  |
| AUX-07 | L2 | 기반 S/W 설치와 위협 매핑 | 기반 S/W를 순서대로 설치하고, 장애 증상(Core/MDB 로드 실패, UI 미실행, 상위 통신 실패)을 보고 미설치·오설치된 항목을 지목할 수 있다. | `충돌` |
| AUX-08 | L2 | MSSQL Server 2016 설치 | MSSQL 2016을 기준서대로 설치하면서 Agent 자동 시작과 데이터 경로를 미러링 경로로 지정해야 하는 이유를 설명할 수 있다. |  |
| AUX-12 | L2 | 방화벽 해제와 Ping 판정 | 방화벽을 설정 절차대로 해제하고 ping 결과 문구로 통신 정상/비정상 및 ICMP 차단 상황을 판정할 수 있다. |  |
| AUX-13 | L2 | 서버 운영 설정·UPS 점검 | RDP 포트·NIC 전원관리·UPS 자동종료 설정 상태를 점검하고, 전원 이중화 여부에 따라 UPS 자동 종료 설정이 맞는지 판정할 수 있다. |  |
| AUX-14 | L2 | NIC Teaming 구성 | NIC Teaming을 기준 모드로 구성·확인하고, 해제 전 IP 기록 등 주의사항을 지켜 작업할 수 있다. |  |
| AUX-15 | L2 | CMD 진단 명령 세트 | 현상(무응답, 포트 미개방, IP 충돌 의심)에 맞는 CMD 명령을 골라 실행하고 결과 문구(ESTABLISHED, 요청 시간 만료 등)를 읽을 수 있다. |  |
| AUX-16 | L2 | 상위·차량 없는 시뮬 환경 | XCom Simulator와 Simulation.exe로 MCS·실차 없이 OCS를 기동하고 오더 1건 반송까지 재현하는 교육·검증 환경을 구성할 수 있다. |  |
| AUX-17 | L2 | 5GHz 채널 설계 원칙 | DFS/SFS 차이와 채널표를 근거로 OCS-OHT용 4채널과 E84 PIO용 165채널 분리 설계를 설명하고 DFS 채널 사용을 부적합으로 판정할 수 있다. | `추정` |
| AUX-18 | L2 | AP·Bridge 역할과 알람 분리 | PING 알람 문구(OHT / OHT Bridge / AP)를 보고 문제 위치를 차량 탑재 Bridge와 트랙사이드 AP로 1차 분리해 설명할 수 있다. | `병기` `추정` |
| AUX-24 | L2 | Turbo Ring·Loop Protection | 유선 Ring 이중화 구조와 Ring 단절 시 신호가 남는 위치(Relay Warning, Event Log)를 설명하고 해당 화면을 지목할 수 있다. |  |
| AUX-25 | L2 | EQ 감시 체계 구조 | EQ Group/EQ Tag/Error Tag 3층 구조와 장비별 감시 항목·프로토콜·정상값을 설명하고, EQ 알람을 보고 해당 EQ Tag(OID/엔드포인트)를 지목할 수 있다. | `충돌` `버전` `근거약` |
| AUX-09 | L3 | DB 구축 쿼리 실행·실패 대응 | DB 구축 쿼리 3단계를 직접 실행하고, 실패 시 경로 함정 제거와 개별 쿼리 실행으로 구축을 완료할 수 있다. |  |
| AUX-10 | L3 | UI 설치·배포 오류 조치 | UI 설치·실행 오류 메시지를 보고 4종 중 어느 것인지 판별해 해당 조치(신뢰 사이트 추가, 캐시 정리 등)를 직접 수행할 수 있다. |  |
| AUX-20 | L3 | MOXA AP/Bridge 설정 변경 | AP/Bridge 무선 파라미터를 기준값으로 설정·저장하고, 통신 단절 영향을 고려해 펌웨어 업그레이드 시점을 정해 수행할 수 있다. |  |
| AUX-21 | L3 | Cisco Switch/AP 설정 | Cisco 스위치 VLAN·access/trunk 구성과 WLC에서 AP 채널·출력 조정을 CLI/웹으로 수행할 수 있다. | `충돌` `버전` |
| AUX-23 | L3 | 스위치 로그로 원인 계층 판정 | 스위치 Event Log·포트 통계와 OCS 통신 알람 시각을 대조해 장애 원인을 OCS측/네트워크 포트/물리 계층으로 특정할 수 있다. | `근거약` |
| AUX-26 | L3 | EQ 감시 체인 검증 | 장비측 SNMP/REST 응답을 직접 검증해 미수신 원인을 장비측/OCS측으로 가르고, 허용된 방식(Normal Value 변경)으로 알람 체인을 시험할 수 있다. | `버전` `근거약` |
| AUX-27 | L3 | EQ 알람 대응·에스컬레이션 | EQ 알람 종류별로 정해진 확인 순서를 수행해 장비 상태를 판정하고 에스컬레이션 여부와 대상을 결정할 수 있다. |  |

---

## 부록 A — 에러코드 대역 대조표 (두 판 병기)

`260103_ErrTag_L30.xlsx` 2,277행 / `ErrorDescription.xlsx` 2,403행에서 ErrType별 ErrCode 최소~최대(행 수)를 뽑았습니다. 교재에서는 두 값을 나란히 적고, 실제 판정은 사이트 System>ErrorTag 화면에 등록된 값으로 하게 합니다.

| ErrType | 260103_ErrTag_L30 | ErrorDescription | 차이 |
|---|---|---|---|
| VEHICLE | 1~720 (428) | 1~720 (428) | 같음 |
| CPSDOWN | 1000~1027 (28) | 1000~1027 (28) | 같음 |
| CPSFAILOVER | 1028~1055 (28) | 1028~1055 (28) | 같음 |
| SYSTEM | 3001~4574 (1574) | 3001~4500 (1500) | **다름** |
| PING | 7001~7120 (120) | 7001~7112 (112) | **다름** |
| PLCCOMM | 7500~7507 (8) | 7500~7505 (6) | **다름** |
| SYSTEMALARM | 8071~8104 (34) | 없음 | ErrTag에만 있음 |
| STATIONALARM | 8105~8130 (26) | 5000~5273 (274) | **다름** |
| SAFETY | 9000~9003 (4) | 없음 | ErrTag에만 있음 |
| RCP | 91001~91012 (7) | 91001~91012 (7) | 같음 |
| CPU | 92001~92003 (3) | 92001~92003 (3) | 같음 |
| MEMORY | 93001~93003 (3) | 93001~93003 (3) | 같음 |
| HOSTQ | 94001~94001 (1) | 94001~94001 (1) | 같음 |
| HDD | 95001~95001 (1) | 95001~95001 (1) | 같음 |
| RCPSTATION | 96001~96008 (4) | 96001~96008 (4) | 같음 |
| ORDER | 96002~96003 (2) | 96002~96003 (2) | 같음 |
| RCPPLC | 96006~96007 (2) | 96006~96007 (2) | 같음 |
| SEGMENT | 96009~96009 (1) | 96009~96009 (1) | 같음 |
| POINT | 96010~96010 (1) | 96010~96010 (1) | 같음 |
| JCRCOMM | 96101~96101 (1) | 96101~96101 (1) | 같음 |
| MCSIF | 100001~100001 (1) | 100001~100001 (1) | 같음 |

ErrorDescription에만 `Description`(원인 설명) 컬럼이 있습니다. ErrTag에만 있는 코드(SYSTEMALARM, SAFETY, PING·PLCCOMM·SYSTEM의 늘어난 번호)는 설명이 없습니다.

## 부록 B — 삭제한 항목

| ID | 항목 | 할 수 있어야 하는 것 (삭제 전) | 삭제 이유 |
|---|---|---|---|
| L3c-06 | Check Layout·Solid 검증 | MDB 반영 전에 Check Layout, Auto-Blockings, Solid Detect를 순서대로 수행하고, 하나라도 미완료이면 반영을 중단하는 판정을 내릴 수 있다. | RailDesignTool에는 맵 검증 기능(Check Layout·Solid Detect)이 없음(2026-10-08 사이트 확인). LayOut Designer 기준 절차라 현 사이트 도구에 해당 없음. OCS 화면 Layout>Check는 L1-44·L2a-18에 그대로 있음. |

삭제 항목의 전문은 `_work/items_v0.3.json`의 `deleted`에 남아 있어 되살릴 수 있습니다.
