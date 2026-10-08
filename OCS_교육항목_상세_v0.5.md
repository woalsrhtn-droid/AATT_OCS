# OCS 교육 항목 — 상세 v0.5

> [OCS_교육항목_레벨별_리스트_v0.5.md](OCS_교육항목_레벨별_리스트_v0.5.md)의 항목별 교육 내용 전문, 근거 문서, 주의사항입니다. 통합된 항목은 통합 전 항목(v0.3 ID)별로 교육 내용을 그대로 나눠 실었습니다. 범위 Core는 10일 교육·평가 대상, Extended는 자료로만 넘기는 항목입니다. 기준 매뉴얼은 사용자 매뉴얼 3판(v04 / 중문통합 / MXA), 맵 도구는 RailDesignTool입니다.

## L1 OCS 프로그램 숙지

### L1-01 메인 화면 구성·연결 램프·객체 색·찾기

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: 메인화면  ·  **Section / Module**: Screen Operation / Main & View  ·  **범위**: Core  ·  **교육 일차**: 4
- **화면·도구**: OCS 메인 화면 (4.1 전체 UI 구성화면) / OCS 메인 화면 상단 Core / PLC / Host 표시 (MXA본) / OCS 메인 화면 layout 영역 (4.2 기본 UI 구성요소) / 메인 화면 ⑤화면 layout / ⑥찾기 / System > Home 결과 확인
- **할 수 있어야 하는 것**: ① 실화면에서 8영역을 하나씩 가리키며 이름과 용도를 말하고, 10개 메뉴 탭을 순서대로 열 수 있다. ② 대상 사이트 메인 화면에서 Core/Host 연결 램프를 찾아 깜빡임 여부로 연결 상태를 읽을 수 있다. ③ layout 영역에서 임의로 지정한 객체가 7종 중 무엇인지 말하고, Unuse/Home/Station Point를 색으로 구분할 수 있다. ④ 번호만 주어진 Point·Vehicle·CassetteID를 찾기 기능으로 화면에 띄우고, Home 등록·해제 결과를 Layout 색으로 확인할 수 있다.
- **표시**: 근거약함
- **주의**: [L1-02] MXA본 3.1 기준. PLC 램프 색은 원문에 없어 현장 화면으로 보충해야 한다. / [L1-03] 색상(황색/갈색/초록)은 MXA본 기준. 전체 색상 정의는 Help>Define(L1-19). / [L1-05] Layout 메뉴 탭의 Run/Check/Setting은 발주자 정의상 L2-a, MapLoad는 L3-c라서 L1 Layout 항목은 layout 화면 탐색·결과 확인으로 구성했다. Home Point Insert/Unuse 조작 자체는 C172 주 버킷(L2-a).

- **L1-01 메인 화면 8영역 식별**
  - 내용: OCS 메인 화면(4.1 전체 UI 구성화면)은 ①사용자 정보 및 로그인 ②메뉴 탭(View/System/Object/Transfer/Report/Statistics/Window/Layout/PlayBack/Help) ③OrderList ④화면 확대·축소(마우스 wheel scroll) ⑤화면 layout(Point·Segment·차량 움직임) ⑥Point/Segment/Vehicle/Station/CassetteID 찾기 ⑦ErrorList(실시간 Error) ⑧OCS 서버 CPU·Memory·HDD 사용률의 8영역으로 구성된다.
  - 할 수 있어야 하는 것: 실화면에서 8영역을 하나씩 가리키며 이름과 용도를 말하고, 10개 메뉴 탭을 순서대로 열 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p9
- **L1-02 Core/PLC/Host 연결 램프**
  - 내용: MXA본 3.1 전체화면구성 8번 항목: 'Core, PLC, Host' 연결 상태면 빨간 불(Core), 초록 불(Host)이 깜빡인다. PLC 램프 색은 원문에 없다. 램프가 꺼졌을 때 어느 로그로 가는지는 L2-c 범위다.
  - 할 수 있어야 하는 것: 대상 사이트 메인 화면에서 Core/Host 연결 램프를 찾아 깜빡임 여부로 연결 상태를 읽을 수 있다.
  - 근거: \_MANUAL\_User Manual\_V01\_MXA.docx 3.1 전체화면구성(기본화면) 8번 항목
- **L1-03 Layout 객체·색상 식별**
  - 내용: 화면 layout 객체 7종: ①Normal Point(OHT 정위치·이동 가능 위치) ②OHT ③STB(OHT가 이/적재하는 Buffer) ④EQP Station ⑤STB Point ⑥EQP Point ⑦Home Point(이/적재 후 대기 Point). MXA본은 Segment(point와 point를 잇는 선), Unuse Point(진입 불가, 황색), Home Point(갈색), Station Point(초록색) 색상을 추가로 명시한다.
  - 할 수 있어야 하는 것: layout 영역에서 임의로 지정한 객체가 7종 중 무엇인지 말하고, Unuse/Home/Station Point를 색으로 구분할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p10; \_MANUAL\_User Manual\_V01\_MXA.docx 3.2 화면 구성요소
- **L1-05 메인 화면 찾기·확대·결과 확인**
  - 내용: 화면 layout(⑤)은 마우스 wheel로 확대·축소하고, ⑥찾기에 Point/Segment/Vehicle/Station/CassetteID 번호를 넣고 Enter를 치면 해당 위치가 크게 표시된다. 설정 결과는 Layout 색으로 확인한다(예: System > Home Insert 후 Home Point는 갈색, 해제하면 회색).
  - 할 수 있어야 하는 것: 번호만 주어진 Point·Vehicle·CassetteID를 찾기 기능으로 화면에 띄우고, Home 등록·해제 결과를 Layout 색으로 확인할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p9, p13~15

### L1-02 로그인 ID 등록·권한

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: 메인화면  ·  **Section / Module**: Screen Operation / Main & View  ·  **범위**: Core  ·  **교육 일차**: 4
- **화면·도구**: 메인 화면 ①사용자 정보 및 로그인 (Login → 지금 등록 → Confirm)
- **할 수 있어야 하는 것**: ID를 등록·로그인하고, 메뉴가 보이지 않을 때 권한 부족인지 확인하며, 우측 상단 자동 로그아웃 표시를 읽을 수 있다.
- **표시**: 사이트의존
- **주의**: 메인 화면 로그인 영역은 메뉴 탭 소속이 아니어서 View로 분류. 화면별 권한 매핑표가 자료에 없음(data_gap) — 어느 화면이 어느 권한부터 보이는지는 현장 실측.

- **교육 내용**
  - 내용: 화면 우측 상단 로그인 → '지금 등록' → 정보 입력 → Confirm으로 ID를 등록한다. 권한은 Guest \< User \< Operator \< Engineer \< Manager 5단계이고 권한에 따라 선택 가능한 메뉴가 제한된다(Safety 설정 등은 권한 ID로 로그인해야 접근). 무작업 상태가 Parameter LogoutTimeover 시간만큼 지속되면 자동 로그아웃되며 남은 시간은 우측 상단에 표시된다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p11, p46(Safety 권한); OCS Parameter 매뉴얼 p.78 (14.3 LogoutTimeover)

### L1-03 화면 표시·배치·문구 설정 (View·Layout Setting/Check·DockSetting·Graphic)

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: View  ·  **Section / Module**: Screen Operation / Main & View  ·  **범위**: Core  ·  **교육 일차**: 4
- **화면·도구**: 메뉴 탭 > View (SegArrow, SegmentNumber / Layout·Object·Safety·Default·None·Total) / 메뉴 탭 > Layout > Setting / Check / Window > TerminalMsg / Window > DockSetting / Object > Graphic (Screen Name, FontAlignment) / Object > Memo
- **할 수 있어야 하는 것**: ① 지정한 정보(예: Segment 번호와 진행 방향)만 화면에 보이도록 View 탭을 설정하고 Default로 되돌릴 수 있다. ② Layout>Setting으로 화면 배율을 맞추거나 Reset하고, Layout>Check를 실행해 Message 목록을 열어 볼 수 있다. ③ TerminalMsg에서 상위 메시지를 읽고 지우며, DockSetting으로 서브창 배치를 바꾸고 원복할 수 있다. ④ 기존 Text Box의 Screen Name·FontAlignment를 바꿔 UI 문구를 수정하고, 객체에 Memo를 삽입할 수 있다.
- **주의**: [L1-44] MXA본 11.2 Check / 11.3 Setting 기준. Check 경고가 실제 결함인지 판정해 고치는 것은 L2-a(Layout Run 항목). / [L1-42] TerminalMsg는 v04본, Docking Setting은 MXA본 10.6 근거. / [L1-26] Text Box 신규 등록(Layout editor)은 L2-a.

- **L1-06 View 탭 표시 항목 전환**
  - 내용: 메뉴 탭 > View에서 SegArrow, SegmentNumber 등을 개별 체크해 켜고 끄며, Layout / Object / Safety / Default(기본 설정 항목) / None(아무것도 표시 안 함) / Total(전체 항목) 버튼으로 묶음 전환한다. 화면이 복잡해 원하는 정보가 안 보일 때 가장 먼저 쓰는 기능이다.
  - 할 수 있어야 하는 것: 지정한 정보(예: Segment 번호와 진행 방향)만 화면에 보이도록 View 탭을 설정하고 Default로 되돌릴 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p12
- **L1-44 Layout Setting·Check 조작**
  - 내용: Layout > Setting에서 CoordScale / BaseVehicleScale / PointScale / PointNumberScale / SegmentThickness를 사이트에 맞게 Confirm하거나 Reset한다(화면 표시 배율이며 맵 데이터는 바뀌지 않는다). Layout > Check에서 LayoutCheck를 실행하고 Message 목록을 확인한다.
  - 할 수 있어야 하는 것: Layout>Setting으로 화면 배율을 맞추거나 Reset하고, Layout>Check를 실행해 Message 목록을 열어 볼 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p106~108; 02. RCPHMI.txt 23~25행(현상 7)
- **L1-42 TerminalMsg·DockSetting**
  - 내용: Window > TerminalMsg는 MCS에서 받은 S10F3 Message를 확인하고 개별 삭제 또는 ALL CLEAR한다. Window > DockSetting은 각 서브창의 Docking 상태와 초기 창 Width/Height를 설정한다.
  - 할 수 있어야 하는 것: TerminalMsg에서 상위 메시지를 읽고 지우며, DockSetting으로 서브창 배치를 바꾸고 원복할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p103, p105
- **L1-26 Graphic·Memo 표시**
  - 내용: Object > Graphic: Layout editor에서 Text Box를 등록한 뒤 Screen Name에 문구를 넣고 FontAlignment로 표기 위치를 지정해 설비 명·전달내용을 UI에 표시한다. Object > Memo는 UI 등록 항목에 메모를 삽입한다.
  - 할 수 있어야 하는 것: 기존 Text Box의 Screen Name·FontAlignment를 바꿔 UI 문구를 수정하고, 객체에 Memo를 삽입할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p52

### L1-04 System 자원·Status·Color 조회

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: System  ·  **Section / Module**: Screen Operation / System Menu  ·  **범위**: Core  ·  **교육 일차**: 4
- **화면·도구**: System > SystemInfo (ALIVE / HARDWARE / SETTING(CPU-RAM) / SETTING(HDD)) / ErrorList / System > Color / System > Status (Check)
- **할 수 있어야 하는 것**: ① SystemInfo HARDWARE에서 서버별 CPU/MEMORY/드라이브 사용률을 읽어 보고하고, ErrorList의 92001/93001/95001 행이 어느 자원 경고인지 짚을 수 있다. ② System>Status에서 Check를 실행해 DB 이름과 여유공간을 읽어 보고하고, Color 화면에서 Object 색을 바꾸고 저장할 수 있다.
- **표시**: 사이트의존, 자료충돌, 민감정보
- **주의**: [L1-07] 검증자 overreach: CPU 경고 임계값(점검 매뉴얼 캡처 87/92/97%·180초 vs Parameter 매뉴얼 예시 80/85/90·100/110/120초)은 사이트별 설정값이라 '예시(사이트별 확인)'로만 표기. 임계값 변경은 L3. 호스트명(RCP-DB01/02)은 역할명으로 치환 필요.

- **L1-07 SystemInfo 자원 현황 확인**
  - 내용: System → SystemInfo를 열면 탭 ALIVE / HARDWARE / SETTING(CPU-RAM) / SETTING(HDD)가 있고, ALIVE는 Active-Active 시스템에서 가동 중인 프로그램 상태를 보여준다. HARDWARE 컬럼은 NAME, CPU, MEMORY, C Usage, D Usage, E Usage(서버 행 예: RCP-DB01/RCP-DB02, 사이트별 확인)다. 설정값 초과가 설정 시간(예: 180초, 사이트별 확인) 동안 유지되면 ErrorList에 ERRCODE 92001 'CPU Warning Level#1', 92002 'CPU Warning Level#2', 93001 'MEMORY Warning Level#1', 95001 'Insufficient HDD Disk Space'가 뜬다.
  - 할 수 있어야 하는 것: SystemInfo HARDWARE에서 서버별 CPU/MEMORY/드라이브 사용률을 읽어 보고하고, ErrorList의 92001/93001/95001 행이 어느 자원 경고인지 짚을 수 있다.
  - 근거: CPU\_RAM\_HDD 점검 메뉴얼\_20220607.pdf p.3, p.5~6, p.8~9; OCS 사용자 매뉴얼\_v04\_210114.pdf p39
- **L1-08 System Color·Status 조회**
  - 내용: System > Color: Object Name 선택 → 채도를 마우스 또는 수치로 변경 → SAVE. System > Status: Check 버튼을 눌러 해당 PC의 DataBaseName, 여유공간, 설치위치, 현재상태를 조회한다(OCS 화면에서 DB 여유공간을 보는 지점).
  - 할 수 있어야 하는 것: System>Status에서 Check를 실행해 DB 이름과 여유공간을 읽어 보고하고, Color 화면에서 Object 색을 바꾸고 저장할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p37~38; 검증자 missing 17 (System>Status)

### L1-05 차량 등록 체인 (CommGroup→Vehicle→Station→OrderGroup)

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: System  ·  **Section / Module**: System Setup / Site Configuration  ·  **범위**: Core  ·  **교육 일차**: 3
- **화면·도구**: System > Vehicle (Insert Vehicle Define) / CommGroup / Object > Vehicle Line In / Station / OrderGroup / System > Comm Group / System > Order Group
- **할 수 있어야 하는 것**: ① 교육 서버에서 CommGroup→Vehicle→Line In→Station→OrderGroup 순서로 차량 1대를 반송 가능한 상태까지 등록할 수 있다. ② Comm Group 1건을 등록·저장하고, 지정한 차량의 IpAddress/PortNumber/ProtocolType 설정값을 화면에서 찾아 읽을 수 있다. ③ Order Group을 생성해 Vehicle·Station·Home을 넣고 저장하며, 특정 Station이 어느 Group에 속하는지 화면에서 확인할 수 있다.
- **표시**: 사이트의존, 민감정보
- **주의**: [L1-10] IP·Port 실값은 배포 시 마스킹. / [L1-11] From/To 동일 Group 할당 규칙의 구조 설명은 L2-b, AltTransfer 등록 수 산정(C262)은 L2 버킷.

- **L1-09 신규 Vehicle 등록 순서**
  - 내용: System > Vehicle(Insert Vehicle Define)에서 VehicleNumber(실제 Vehicle Number와 동일), SlotCount(이/적재 가능 Slot 수), VehicleType(OHT/OHS/AGV/MCT 등), CommGroup(CommGroup Number)을 지정한다. 등록 순서는 CommGroup 등록 → VehicleSetting 등록 → 차량 Line In → Station 추가·설정 → OrderGroup 등록이며, CommGroup이 없으면 Vehicle을 추가할 수 없다.
  - 할 수 있어야 하는 것: 교육 서버에서 CommGroup→Vehicle→Line In→Station→OrderGroup 순서로 차량 1대를 반송 가능한 상태까지 등록할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p20; OCS 설치 기준서 p.36 (4장 절차 12)
- **L1-10 System Comm Group 등록**
  - 내용: System > Comm Group에서 CommGroupNumber(Vehicle Number와 일치시키면 구분 용이), LimitTime(Vehicle 통신 LimitTime), IpAddress, PortNumber, ProtocolType(Vehicle Type에 맞게)을 입력하고 Insert → SAVE한다. 차량 통신 장애 때 설정값을 확인하는 1차 화면이며, CommErrHistory와 대조해 원인을 특정하는 것은 L3-a다.
  - 할 수 있어야 하는 것: Comm Group 1건을 등록·저장하고, 지정한 차량의 IpAddress/PortNumber/ProtocolType 설정값을 화면에서 찾아 읽을 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p22; 검증자 missing 4 (Comm Group)
- **L1-11 System Order Group 등록**
  - 내용: System > Order Group에서 Group Number Insert → Group 선택 → Vehicle·Station·Home 추가(From·To Station 동시 추가 버튼 별도) → SAVE한다. Vehicle은 자기 Group의 Station 물량만 처리하고 From·To Station이 모두 같은 Group이어야 하며, 오더 완료 후 Group의 Home Point 중 가까운 곳을 우선 선택한다.
  - 할 수 있어야 하는 것: Order Group을 생성해 Vehicle·Station·Home을 넣고 저장하며, 특정 Station이 어느 Group에 속하는지 화면에서 확인할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p21

### L1-06 ErrorTag 등록·Tag Excel 일괄 편집

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: System  ·  **Section / Module**: System Setup / Site Configuration  ·  **범위**: Core  ·  **교육 일차**: 3
- **화면·도구**: System > ErrorTag ([ERROR TAG] 탭 / Control / Insert) / System > ErrorTag (DOWNLOAD TAG / OPEN TAG / CHECK TAG / OVERWRITE) / System > PLC Tag (OPEN TAG)
- **할 수 있어야 하는 것**: ① ErrorTag에서 지정 ErrCode를 찾아 8개 컬럼 값을 읽고 ErrorLevel로 중/경알람을 구분하며, 신규 Error 1건을 Insert할 수 있다. ② 교육 서버에서 DOWNLOAD TAG→Excel 편집→OPEN TAG→CHECK TAG→OVERWRITE 9단계를 수행하고 CHECK TAG 결과로 이상 유무를 판단할 수 있다.
- **표시**: 사이트의존, 병기
- **주의**: [L1-12] 코드 대역은 부록 A 대조표대로 260103_ErrTag_L30 / ErrorDescription 두 판을 병기한다. ErrCode/ErrType/ErrEvent가 AlarmList·ErrorHistory와 이어지는 Tag 체계 설명은 L2-b. / [L1-13] OVERWRITE는 Tag 테이블 전체에 영향 — 실습은 교육 서버 한정, 운영 서버 실행 권한은 별도 결정.

- **L1-12 ErrorTag 개별 등록·컬럼**
  - 내용: System > ErrorTag에 등록되지 않은 Error가 발생하면 'Not Defined Error'가 뜬다. 개별 등록은 [ERROR TAG] 탭 → Control → ErrCode, ErrType, ErrEvent, ErrLevel, ShowDelayTime, ErrText, ErrActionText 입력 → Insert다. Tag 파일 컬럼은 ErrCode, ErrType, ErrEvent, ErrText, ErrActionText, ErrorLevel, ShowDelayTime, Remark 8개이며 ErrorLevel 1=중알람, 9=경알람이다(예: 260103_ErrTag_L30은 ShowDelayTime 전부 0, ErrActionText≈ErrText — 사이트별 확인).
  - 할 수 있어야 하는 것: ErrorTag에서 지정 ErrCode를 찾아 8개 컬럼 값을 읽고 ErrorLevel로 중/경알람을 구분하며, 신규 Error 1건을 Insert할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p24; 260103\_ErrTag\_L30.xlsx 헤더; ErrorDescription.xlsx 시트 AATT\_L30 5행
- **L1-13 Tag Excel 일괄 편집**
  - 내용: ErrorTag 일괄 편집: ①[ERROR TAG] 탭 ②Control ③[DOWNLOAD TAG] ④Error Tag Excel File 다른 이름으로 저장 ⑤Excel 편집 후 저장 ⑥ERROR TAG - OPEN TAG ⑦OPEN TAG FILE로 파일 불러오기 ⑧CHECK TAG로 이상유무 확인 ⑨OVERWRITE 후 적용 확인. System > PLC Tag도 개별 Insert, 속성 수정 후 SAVE, OPEN TAG 일괄 적용이 ErrorTag와 같은 방식이다.
  - 할 수 있어야 하는 것: 교육 서버에서 DOWNLOAD TAG→Excel 편집→OPEN TAG→CHECK TAG→OVERWRITE 9단계를 수행하고 CHECK TAG 결과로 이상 유무를 판단할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p24~26; OCS 사용자 매뉴얼\_v04\_210114.docx '7.8 ErrorTag' 사용 방법 ①~⑨, '7.9 PLC Tag' ④

### L1-07 Parameter 진입·UI 표시값

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: System  ·  **Section / Module**: Parameters / Parameter System  ·  **범위**: Core  ·  **교육 일차**: 4
- **화면·도구**: System > Parameter > 카테고리 > 개별값
- **할 수 있어야 하는 것**: 지정한 Parameter(예: BlockingParam>PushWeight, ZoomFocusLevel)를 메뉴 경로로 찾아 현재 값을 읽어 보고할 수 있다.
- **주의**: v04본은 DBInterfaceParam 포함 16그룹, MXA본 6.10은 15그룹. 현장 화면의 그룹 수로 대조한다.

- **교육 내용**
  - 내용: Parameter(사용자 매뉴얼 기준 16그룹 — MXA본 6.10의 15그룹에 v04본 DBInterfaceParam)는 System > Parameter > 카테고리(예: BlockingParam) > 개별값(예: PushWeight)의 3단 경로로 연다. UI 표시 관련 값: LogoutTimeover(자동 로그아웃, 우측 상단 표시), ZoomFocusLevel(FOCUS 확대 배율, 0.1당 10%), LoginMsg(로그인 문구, 줄바꿈 \n), UseVehicleScreenName(True=Screen Name, False=Vehicle Number 표기)이며, 변경 후 적용이 안 되면 UI를 껐다 켠다. L1은 값을 찾아 읽는 데까지이고 거동 Parameter 변경은 L3다.
  - 근거: 02. RCPHMI.txt 5행; OCS Parameter 매뉴얼 p.78~80, p.82 (14.3, 14.5, 14.6, 14.8)

### L1-08 Object>Vehicle 조작 (Line In/Out·Prevent·Sub Command·Clean·Set/Etc·IO)

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: Object  ·  **Section / Module**: Screen Operation / Object Menu  ·  **범위**: Core  ·  **교육 일차**: 4
- **화면·도구**: Object > Vehicle > Commands (Line In / Line Out / Prevent Call / Prevent Push / Prevent Charge / SetFocus) / Report > InOutHistory / Object > Vehicle > Sub Vehicle Command / Vehicle popup (Clean On / Clean Off) / Object > Vehicle > Set / Etc / IO 탭, System > Vehicle IO Tag
- **할 수 있어야 하는 것**: ① 지정 차량을 Line Out(PM/BM·Comment 입력)→Line In하고 Prevent Call을 켜고 끈 뒤 InOutHistory에서 해당 Comment를 조회할 수 있다. ② Vehicle popup에서 지정 차량의 Clean Mode를 On/Off하고, Sub Vehicle Command의 각 명령(Forcible Entry 포함)이 무엇을 하는지 말하며 매뉴얼 절차대로 실행할 수 있다. ③ Set 탭에서 IoGroupNumber를 지정·저장한 뒤 IO 탭에서 IO 이름과 ON(초록) 비트를 읽고, Set/Etc 옵션 각각이 무엇을 바꾸는지 말할 수 있다.
- **표시**: 근거약함, 민감정보, 추정해석
- **주의**: [L1-16] 근거 pptx 캡처 타이틀바에 현장 서버 호스트명·IP와 차량명이 보임 — 배포 시 마스킹. Sub Vehicle Command 구성은 사용자 매뉴얼(v04본 8.3 아이콘표, MXA본 7.3.2·중문통합본 같은 설명) 기준으로 가르치고 2026 현장 캡처와 다른 버튼은 현장 화면으로 보충. Clean Mode가 할당·경로에 미치는 영향은 자료 없음. 분기진입 실패 판단 후 Forcible Entry 투입 결정은 L3-a. / [L1-17] System>Vehicle IO Tag는 v04본 근거. Home Point 필드는 RCPHMI 메모의 '필요한 듯'·save 불가 기록뿐이라 평가 문항에서 제외하고 위치 인지만. IO 비트로 차량 이상을 판정하는 것은 L3-a.

- **L1-15 Vehicle Line In/Out·Prevent**
  - 내용: Object > Vehicle > Commands에서 Line In(차량 등록)·Line Out(차량 삭제)을 하면 아이콘이 바뀐다. Prevent Call(자동 오더 할당 금지), Prevent Push(다른 차의 밀어내기 금지), Prevent Charge(Charge 금지, OHS 해당 없음)는 가능/금지 쌍 아이콘이고, SetFocus는 선택 호기를 확대 표시한다. SelectPMBM이 켜져 있으면 LineOut·Call Disable 때 PM/BM 선택창이 뜨고, 입력한 Comment는 Set 탭 '5. TempraryParam'과 Report > InOutHistory에서 확인한다.
  - 할 수 있어야 하는 것: 지정 차량을 Line Out(PM/BM·Comment 입력)→Line In하고 Prevent Call을 켜고 끈 뒤 InOutHistory에서 해당 Comment를 조회할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p43~44; OCS Parameter 매뉴얼 p.81 (14.7 SelectPMBM)
- **L1-16 Vehicle 보조 명령·Clean**
  - 내용: Object > Vehicle > Sub Vehicle Command: Forcible Entry(강제 분기진입, command - F), 작업 내용 확인, 경로 확인, 청소차량 On(Bst:3)/Off(Bst:2), 레일 진단차량 On(Bst:C)/Off(Bst:8). 속성으로 RFIDReading(적재 후 실 CSTID와 오더 CSTID 비교, OHS 해당 없음), CleanStatus(Normal/Clean/Dirty), Full Charger Point(OHT 해당 없음)가 있다. Clean Mode는 Menu bar → Object → Vehicle popup → Clean On → Yes, 해제는 Clean Off → Yes다.
  - 할 수 있어야 하는 것: Vehicle popup에서 지정 차량의 Clean Mode를 On/Off하고, Sub Vehicle Command의 각 명령(Forcible Entry 포함)이 무엇을 하는지 말하며 매뉴얼 절차대로 실행할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p44; Clean\_Vehicle\_Manual\_parkjaemin.pptx 슬라이드 2~3, 6~7
- **L1-17 Vehicle Set/Etc·IO 탭**
  - 내용: Object > Vehicle의 Set/Etc 옵션: Mask 차량은 Clean/Dirty/Nomal 설정에 따라 반송 할당 결정, SendUlCommandNotMoving(G 커맨드 없이 반송 명령 생성, MCT), Etc > CasstteSize Interlock(정해진 Size만 반송). IO 표시: System > Vehicle IO Tag에서 24바이트(192개) IO Index에 IOName·GroupName을 Vehicle Type별로 부여 → Set 탭 TemporaryParam > IoGroupNumber에 IO Tag의 VehicleNumber 입력 → SAVE → IO 탭에서 IO Name 변경과 활성 BIT 초록색을 확인한다. 같은 화면에 차량별 Home Point 필드가 있으나 동작·저장 조건은 미확정이다.
  - 할 수 있어야 하는 것: Set 탭에서 IoGroupNumber를 지정·저장한 뒤 IO 탭에서 IO 이름과 ON(초록) 비트를 읽고, Set/Etc 옵션 각각이 무엇을 바꾸는지 말할 수 있다.
  - 근거: RCP Program setup 가이드 p.33 (5.6 Vehicle 등록 및 설정); OCS 사용자 매뉴얼\_v04\_210114.pdf p27; 02. RCPHMI.txt 14~15행(현상 4)

### L1-09 Object>Station 속성·Mode·Port 확인

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: Object  ·  **Section / Module**: Screen Operation / Object Menu  ·  **범위**: Core  ·  **교육 일차**: 4
- **화면·도구**: Object > Station (Property / Commands / Station Mode) / Station > EQP Port / Transfer Buffer / Cassette > StationEvent, Vehicle·Station·TransferUnit > OnlineName
- **할 수 있어야 하는 것**: ① 지정 Station의 속성값을 읽어 설명하고, Station Mode를 InService↔OutService로 전환한 뒤 화면에서 결과를 확인할 수 있다. ② 지정 EQP Port·Transfer Buffer의 Duplicate/LongStay TimeOut/OnlineName 값을 읽고 Naming Rule과 대조해 오기·누락을 찾아낼 수 있다.
- **표시**: 사이트의존
- **주의**: [L1-18] OnlineName이 MCS 통신 ID라는 연결 구조 설명은 L2-b. / [L1-19] Naming Rule·LongStay 값은 사이트별. LongStay 알람↔파라미터 대응(검증자 missing 6)은 L2-c/L3-a에서 다루고 여기서는 필드 위치·의미만.

- **L1-18 Station 속성·Station Mode**
  - 내용: Object > Station 속성: StationNumber, PointNumber(이/적재 Point), Unuse, SlotCount, OnlineName(MCS 통신 ID), ScreenName(UI 표시 ID), StationType(Equipment/Stocker/Transfer 등), Direction, WorkType(투입·배출·투입배출), CassetteInfo, Priority, DuplicateFromOrderCount·DuplicateToOrderCount(설정치 이상 Nack). Station Mode 4종은 InputMode(Unload 가능), OutputMode(Load 가능), InService(반송 가능 보고), OutService(반송 불가 보고)이며 Commands에 Set Focus·All View가 있다.
  - 할 수 있어야 하는 것: 지정 Station의 속성값을 읽어 설명하고, Station Mode를 InService↔OutService로 전환한 뒤 화면에서 결과를 확인할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p45~46
- **L1-19 Station 포트·OnlineName 확인**
  - 내용: Station > EQP Port: Duplicate(수치보다 많은 반송이 내려오면 Nack), Online Name(오타·미작성 시 반송 불가), UsePrehandOffParam(PrehandOff 사용 여부). Station > Transfer Buffer: Online Name, LongStay TimeOut(카세트가 설정 시간 이상 머물면 Alarm), Cassette > StationEvent(Install/Remove/Alarm), TransBuffer Type은 상위 보고 setting 추가. OnlineName은 상위 보고에 쓰이므로 Naming Rule 스펙대로 TransferUnit·Station(Vehicle 포함)에 등록됐는지 점검한다.
  - 할 수 있어야 하는 것: 지정 EQP Port·Transfer Buffer의 Duplicate/LongStay TimeOut/OnlineName 값을 읽고 Naming Rule과 대조해 오기·누락을 찾아낼 수 있다.
  - 근거: RCP Program setup 가이드 p.31 표25·표26; RCP Program setup 가이드 p.36 (5.9 OnlineName 등록 및 확인) 표30

### L1-10 Object>Point·CPS·MTL 상태 판독

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: Object  ·  **Section / Module**: Screen Operation / Object Menu  ·  **범위**: Core  ·  **교육 일차**: 4
- **화면·도구**: Object > Point (Point Type) / Object > CPS (상태 RUN·DOWN·FAILOVER) / Object > MTL
- **할 수 있어야 하는 것**: ① 지정 Point의 Type을 Object>Point에서 읽고 7종 각각의 주행 의미를 말할 수 있다. ② Object>CPS에서 각 CPS 상태를 읽고, DOWN/FAILOVER일 때 차량 진입 가능 여부를 말할 수 있다. ③ Object>MTL 상태값 5개를 읽어 현재 차량 배출(또는 진입)이 가능한 상태인지 판정할 수 있다.
- **표시**: 사이트의존
- **주의**: [L1-21] Down Segment를 Segment List에 넣는 Interlock 영역 편집은 L2-a. / [L1-22] 후보 제목은 '4조건'이나 본문은 5조건 — 교재에서 5조건으로 정정.

- **L1-20 Point Type 7종 식별**
  - 내용: Object > Point의 Point Type은 Normal(기본 주행), Pass(정차 없이 통과, RCP는 Pass Point 명령 불가), Stop(일단 정지), Equipment(설비 이/적재), SideBuffer(STB 이/적재), MTL Maint(MTL Maint Zone), MTL Lifter 7종이다. Type을 바꾸는 조작(Point 선택→Point Type→SAVE)은 L2-a 맵 수정 범위다.
  - 할 수 있어야 하는 것: 지정 Point의 Type을 Object>Point에서 읽고 7종 각각의 주행 의미를 말할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p40~41
- **L1-21 CPS 상태 판독**
  - 내용: Object > CPS 상태는 RUN / DOWN / FAILOVER 3종이다. CPS DOWN이면 Interlock 영역 세그먼트에 Interlock이 걸려 차량 진입이 막히고, CPS가 그룹화되어 있으면 FAILOVER 상태에서도 정상 CPS가 동작 중일 때 차량 이동이 가능하며 Fail over된 CPS의 Rail 영역이 표기된다.
  - 할 수 있어야 하는 것: Object>CPS에서 각 CPS 상태를 읽고, DOWN/FAILOVER일 때 차량 진입 가능 여부를 말할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p48; OCS 사용자 매뉴얼\_v04\_210114.docx '8.6 CPS'
- **L1-22 MTL 필드·배출 가능 상태**
  - 내용: Object > MTL 필드: MTLNumber, ScreenName, OnlineName, Unuse, MTLType, SegList, PointList, PIOPoint(진입 전 PIO Point), PointNumber, DetourPointNumber(PIO 실패 후 우회 Point). 차량 배출 가능 MTL 상태(진입은 반대)는 OrderMode=Auto, Floor=UP, Exist=NoExist, TrackMode=Track Out, Available=Available 5조건이며 PlcTag의 MTL ORDERMODE/FLOOR/EXIST/TRACKMODE/AVAILABLE 태그 값과 대응한다.
  - 할 수 있어야 하는 것: Object>MTL 상태값 5개를 읽어 현재 차량 배출(또는 진입)이 가능한 상태인지 판정할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.docx '8.7 MTL' 사용 방법 표; 260103\_PlcTag\_L30.xlsx MTL 태그 6행

### L1-11 Object>PLC·Ping Unit·Tag Group 등록·확인

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: Object  ·  **Section / Module**: Screen Operation / Object Menu  ·  **범위**: Core  ·  **교육 일차**: 4
- **화면·도구**: Object > PLC (PlcName, PollingTime, IP, TcpPort, TcpPortRange, VehicleNumber) / Object > Ping / Object > PLC Tag Group / Object > PlcTagmonitor(MXA본)
- **할 수 있어야 하는 것**: ① 지정 PLC Unit의 6개 연결 필드를 읽고 의미를 말하며, IP/Port 오기 시 PlcTag 값이 안 올라온다는 점을 화면에서 확인할 수 있다. ② 교육 서버에서 Ping Unit 1건을 등록·저장하고 Window>PingList에 나타나는지 확인할 수 있다. ③ 관심 비트 몇 개를 PLC Tag Group으로 묶어 저장하고 ON/OFF 상태를 화면에서 읽을 수 있다.
- **표시**: 사이트의존, 민감정보
- **주의**: [L1-25] MXA본 7.11 PlcTagmonitor / 7.12 PlcTagGroup 기준.

- **L1-23 PLC 연결 파라미터 확인**
  - 내용: Object > PLC에서 PLC Unit별 PlcName(표기 이름), PollingTime(읽기 주기), IP, TcpPort, TcpPortRange(통신 실패 시 접속할 포트), VehicleNumber(FoolProof 적용 시, 예: VEH001)를 설정한다. IP·PORT가 적용돼야 PlcTag 데이터 READ가 가능하며, PLC UNIT은 Layout editor에서 먼저 등록돼 있어야 한다(L2-a).
  - 할 수 있어야 하는 것: 지정 PLC Unit의 6개 연결 필드를 읽고 의미를 말하며, IP/Port 오기 시 PlcTag 값이 안 올라온다는 점을 화면에서 확인할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p51; OCS 사용자 매뉴얼\_v04\_210114.docx '8.9 PLC'
- **L1-24 Ping Unit 등록**
  - 내용: Object > Ping: ①추가 버튼 ②Ping Unit Number 입력 ③등록된 Ping Object 중 세팅할 항목 선택 ④Setting에 Name과 IP Address 입력 ⑤SAVE. Ping Unit 세팅 전에 Layout editor에서 Ping Object가 먼저 등록돼 있어야 한다(L2-a).
  - 할 수 있어야 하는 것: 교육 서버에서 Ping Unit 1건을 등록·저장하고 Window>PingList에 나타나는지 확인할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.docx '8.8 Ping'; OCS 사용자 매뉴얼\_v04\_210114.pdf p50
- **L1-25 PLC Tag Group 묶어보기**
  - 내용: Object > PLC Tag Group은 PLC TAG Value를 Bit ON/OFF로 묶어 확인하는 화면이며 ①Group 선택 ②해당 TAG 선택 후 추가 ③SAVE 순서로 설정한다. MXA본에는 Object > PlcTagmonitor(Name, GraphicType, TagName, TagNumber, TagProperty)로 PlcTag 값을 UI에서 실시간 확인하는 화면이 추가로 있다.
  - 할 수 있어야 하는 것: 관심 비트 몇 개를 PLC Tag Group으로 묶어 저장하고 ON/OFF 상태를 화면에서 읽을 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p53; OCS 사용자 매뉴얼\_v04\_210114.docx '8.12 PLC Tag Group'; \_MANUAL\_User Manual\_V01\_MXA.docx PlcTagmonitor

### L1-12 Transfer 수동 지령·CycleMove

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: Transfer  ·  **Section / Module**: Screen Operation / Transfer & Report  ·  **범위**: Core  ·  **교육 일차**: 5
- **화면·도구**: Transfer > Transfer Command (FROMTO / FROM / TO / MOVE / HOME 탭, Send) / Transfer > CycleMove Command (Name, Unuse, Pause, TotalCycleMove, CurCycleMove) / Window > CycleList
- **할 수 있어야 하는 것**: ① FROMTO/FROM/TO/MOVE/HOME 지령을 각각 생성해 OrderList에서 진행을 확인하고, HOME이 다른 Home으로 간 경우 정상인지 설명할 수 있다. ② Call Disable 차량에 CycleMove를 등록해 시작·정지하고, CycleList에서 CURRENTCOUNT/TOTALCOUNT로 진행 횟수를 읽을 수 있다.
- **표시**: 근거약함, 민감정보
- **주의**: [L1-27] 수동 지령 시 상위로 올라가는 CEID 254(CommandType=EQ_TRANSFER) 흔적 판독은 L3-a. / [L1-28] RCPHMI 현상5(Resume 시 "error unhandled eventname = cyclelistcommand")는 원인 미해결.

- **L1-27 Transfer Command 수동 지령**
  - 내용: Transfer > Transfer Command에서 Auto 또는 Vehicle을 선택(카세트를 들고 있는 Vehicle 선택 금지)한다. FROMTO 탭에 From Station, To Station, 카세트 ID('Copy Selected CassetteID'로 자동 입력), 카세트 SIZE(MASK/HALF/FULL)를 넣고 Send하며, FROM은 이재만, TO는 적재만, MOVE는 Move Point, HOME은 HOMEPOINT를 지정한다. HOME은 RCP 내부 로직이 가까운 HOME으로 보내 지정한 Home으로 안 갈 수 있고 이는 정상 동작이다. 수동 오더는 OrderList에 'MNL'+생성시간 CommandID로 나타난다.
  - 할 수 있어야 하는 것: FROMTO/FROM/TO/MOVE/HOME 지령을 각각 생성해 OrderList에서 진행을 확인하고, HOME이 다른 Home으로 간 경우 정상인지 설명할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p54~56, p98; 3\_SFA\_VHC\_SCENARIO\_SPEC\_V3.5.pdf p.46 (9.2 No Command), p.61~62 (15.4 Manual Order Create)
- **L1-28 CycleMove 등록·시작·정지**
  - 내용: Transfer > CycleMove Command(Vehicle Call Disable 상태에서만): Vehicle 추가 → Name(목적, 예: 15K 구간 Glass Test), Unuse, Pause, TotalCycleMove 설정 → Move 포인트 추가. 시작은 Unuse Pause 해제 → TotalCycleMove > CurCycleMove 확인 → Save → Yes, 정지는 Unuse Pause 체크 → CurCycleMove 증가 확인 → Save → Yes다. 진행 상황은 Window > CycleList(VEHICLE, NAME, MOVEPOINTLIST, STEP, USECLEAN, USE, CURRENTCOUNT, TOTALCOUNT, Resume)에서 본다. 포인트 추가 시 Vehicle 진행방향을 고려하고 Unuse Point/Segment는 경로에서 제외한다(v04 p57).
  - 할 수 있어야 하는 것: Call Disable 차량에 CycleMove를 등록해 시작·정지하고, CycleList에서 CURRENTCOUNT/TOTALCOUNT로 진행 횟수를 읽을 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p57, p101; Clean\_Vehicle\_Manual\_parkjaemin.pptx 슬라이드 4~5, 8~9; 02. RCPHMI.txt 17~18행(현상 5)

### L1-13 Report 반송·운영 이력 조회 (Transfer·공통 이력·Blocking·CommErr)

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: Report  ·  **Section / Module**: Screen Operation / Transfer & Report  ·  **범위**: Core  ·  **교육 일차**: 5
- **화면·도구**: Report > TransferHistory / Report > InOutHistory / InformHistory(InformLogHistory) / RunningHistory / NackHistory / HandOverHistory / CassetteHistory / PingHistory / UserHistory / CpuRamHistory / Move History(MXA) / Report > BlockingHistory / Report > CommErrHistory
- **할 수 있어야 하는 것**: ① 지정 CassetteID 또는 CommandID의 반송 이력을 조회해 각 단계 시각과 구간 소요시간을 읽어 보고할 수 있다. ② 지정된 Report 화면(InOutHistory·InformHistory·RunningHistory·NackHistory·HandOverHistory·CassetteHistory·PingHistory·UserHistory·CpuRamHistory·CommHistory·UIHistory·FailOverHistory·Move History·Safety History)을 메뉴 경로로 열어 조건 입력→SEARCH→SAVE(Excel)를 수행하고, LogParam 보존기간을 넘는 날짜는 조회되지 않음을 확인할 수 있다. ③ 지정 차량의 블로킹 이력에서 BlockedBy 차량을 읽고, CommErrHistory에서 Set/CLEAR 쌍과 발생 Point·Segment를 조회할 수 있다.
- **표시**: 근거약함, 사이트의존, 민감정보
- **주의**: [L1-29] 구간 비교로 병목을 특정하는 것은 L3-a, 반송 지연 시 이 화면을 지목하는 것은 L2-c. / [L1-32] MXA본 9장 Report 19종 기준. RCPHMI 현상6: InformLogHistory Insert가 테이블 null 미허용으로 실패한 기록이 있어 실습 전 동작 확인 필요. / [L1-33] 반복 구간 집계·원인 특정은 L3-a(검증자 권고11 ③).

- **L1-29 TransferHistory 조회**
  - 내용: Report > TransferHistory 조건: 날짜/시간, From Station, To Station, VehicleNumber, OrderType, CassetteID, Trigger, CompleteType(미입력 또는 'ALL'은 전체). 결과: CommandID, OriginOrderType, OrderNumber, FinalLocation, 생성/최초할당/마지막할당/실행/From도착/From완료/To도착/To완료 시각과 구간별 소요시간, OnPositionFailCount, LightErrorCount/TimeSec, HeavyErrorCount/TimeSec, BlockingCount/TimeSec, HandOver.
  - 할 수 있어야 하는 것: 지정 CassetteID 또는 CommandID의 반송 이력을 조회해 각 단계 시각과 구간 소요시간을 읽어 보고할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p58~59
- **L1-32 Report 운영 이력 공통 조회**
  - 내용: Report 화면은 조건 입력 → SEARCH(→SAVE) 공통 패턴이다: InOutHistory(Line In/Out·Call Enable/Disable·Comment), InformHistory(인수인계 Message INSERT·CONFIRM), RunningHistory(1시간 단위 RunningDist/Time·ErrorTime·WorkTime·BlockTime·IdleTime), NackHistory(NackCode·MESSAGE), HandOverHistory, CassetteHistory(Install/Remove 위치·시각), PingHistory(PingStatus·ReplyTime), UserHistory(Login/Logout/AutoLogout), CpuRamHistory, CommHistory(날짜·시간, VehicleNumber 또는 'ALL' → DateTime·VehicleNumber·Message — v04 p68), UIHistory(날짜·시간, MessageName 검색어(예: 'Unuse') → UserID·IP·MessageName(클릭 시 상세)·RegTime — v04 p72), FailOverHistory(날짜·시간 → DATETIME·MODULE·COMMENT — v04 p76·MXA본 9.19). MXA본은 Move History(VehicleNumber/PointNumber/SegmentNumber 검색, SAVE로 엑셀)와 Safety History(9.18)가 추가된다. 조회 가능 기간은 System > Parameter > LogParam 보존기간에 따른다(사이트별 확인). 질문을 듣고 어느 Report로 갈지 고르는 것은 L2-c(L2c-03), 결과 원문 필드 해석(CommHistory Message 비트 등)은 L3-a다.
  - 할 수 있어야 하는 것: 지정된 Report 화면(InOutHistory·InformHistory·RunningHistory·NackHistory·HandOverHistory·CassetteHistory·PingHistory·UserHistory·CpuRamHistory·CommHistory·UIHistory·FailOverHistory·Move History·Safety History)을 메뉴 경로로 열어 조건 입력→SEARCH→SAVE(Excel)를 수행하고, LogParam 보존기간을 넘는 날짜는 조회되지 않음을 확인할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p62~74; \_MANUAL\_User Manual\_V01\_MXA.docx Report > Move History; 02. RCPHMI.txt 20~21행(현상 6); DB 점검 메뉴얼\_20220607.pdf p.4 (LogParam); 검증자 권고10 (Report 공통 조회 조작 L1 복원)
- **L1-33 Blocking·CommErr 이력 조회**
  - 내용: Report > BlockingHistory 조건: Blocking Time(지정 시간 이상/이하), VehicleNumber, PointNumber, SegmentNumber, CommandID / 결과: StartTime, EndTime, BlockingTime, BlockedBy(앞 차량), Point, Segment, CommandID. Report > CommErrHistory 조건: VehicleNumber, PointNumber, SegmentNumber / 결과: VehicleNumber, VehicleOnlineName, Point, Segment, ErrorSet(Set=CommError 발생, CLEAR=조치완료), DateTime.
  - 할 수 있어야 하는 것: 지정 차량의 블로킹 이력에서 BlockedBy 차량을 읽고, CommErrHistory에서 Set/CLEAR 쌍과 발생 Point·Segment를 조회할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p66, p69

### L1-14 ErrorHistory·HSMSHistory 조회·Comment

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: Report  ·  **Section / Module**: Screen Operation / Transfer & Report  ·  **범위**: Core  ·  **교육 일차**: 5
- **화면·도구**: Report > ErrorHistory / Report > HSMSHistory (Search Word / Stream / Function / Include MonitorEvent / InCludeEventReportAck)
- **할 수 있어야 하는 것**: ① 지정 기간·차량의 Error 이력을 조건 조회하고, 한 건에 조치내용 Comment를 입력·저장할 수 있다. ② 지정 CommandID의 상위 메시지를 HSMSHistory에서 찾아 S/F와 Recv/Send 순서대로 나열할 수 있다.
- **주의**: [L1-30] Trend 해석·원인 특정은 L3-a. / [L1-31] v04 10.16·중문 10.16·MXA 9.17 모두 존재(원본 확인). SxFy 본문(CEID/RCMD) 판독은 L3-a.

- **L1-30 ErrorHistory 조회·Comment**
  - 내용: Report > ErrorHistory 조건: 날짜/시간, CassetteID, KeepUp Time, Station, VehicleNumber, ErrorLevel(Light/Heavy), ErrorCode, ErrorCodeRange, StationRange. 결과: OnTime, OffTime, KeepUpTime, ErrCode·ErrType·ErrEvent·ErrText, CommandID, Point, Segment, ErrStationNumber, FromStation/ToStation, OrderType, ErrLevel(1=중알람, 9=경알람), Comment이며 조치내용을 Comment에 입력해 저장한다.
  - 할 수 있어야 하는 것: 지정 기간·차량의 Error 이력을 조건 조회하고, 한 건에 조치내용 Comment를 입력·저장할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p60~61
- **L1-31 HSMSHistory 검색**
  - 내용: Report > HSMSHistory는 상위(MCS)와 주고받은 XcomLog를 조회한다(v04 10.16·중문통합본 10.16·MXA본 9.17에 모두 있다). Search Word에는 CommandID / CassetteID / Vehicle OnlineName(MXA본은 Vehicle Number) 중 하나를 넣는데, CommandID로 검색하면 구분하기 쉽다. Stream과 Function은 따로 입력하고(S2F41이면 Stream '2', Function '41'), MessageName(스펙 참조)으로 메시지별 검색을 할 수 있다. Include MonitorEvent는 Monitored Vehicle Event만, InCludeEventReportAck는 Event Report에 대한 응답만 골라 보는 옵션이다. 결과는 RegTime, Stream, Function, MessageName, CommandID, CstID, UnitID, Type(Recv/Send)이다.
  - 할 수 있어야 하는 것: 지정 CommandID의 상위 메시지를 HSMSHistory에서 찾아 S/F와 Recv/Send 순서대로 나열할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p75

### L1-15 Statistics 조회·Excel 저장 (Vehicle·Transfer·Error·Quality)

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: Statistics  ·  **Section / Module**: Screen Operation / Statistics & Window  ·  **범위**: Core  ·  **교육 일차**: 5
- **화면·도구**: Statistics > Vehicle (Search / Save) / Statistics > Transfer (Date / Vehicle / Station 탭) / Statistics > Error / Statistics > ErrorProfiler (Search / Save) / Statistics > Quality (MTTR / MTTF / MTBF / MCBF)
- **할 수 있어야 하는 것**: ① 지정 기간 차량 가동률을 조회해 Excel로 저장하고, 특정 차량의 ErrorRate·BlockRate 값을 읽어 보고할 수 있다. ② Date/Vehicle/Station 탭을 전환해 스탭별 평균 소요시간과 RetryCountFrom/To를 읽고 Excel로 저장할 수 있다. ③ 지정 기간 다발 알람 상위 코드를 Statistics>Error에서 찾고, 그 코드를 ErrorProfiler로 조회해 Excel로 저장할 수 있다. ④ Quality 화면을 조회해 4개 지표 값을 읽고, 표의 TransferCount·ErrorCount로 MCBF가 맞는지 손으로 검산할 수 있다.
- **주의**: [L1-34] Statistics는 v04본 근거(MXA본에는 상세 장이 없음). L1-15~37도 같음. / [L1-35] v04본 근거. 평균 비교로 느린 구간·설비를 특정하는 것은 L3-a. / [L1-36] v04본 근거. 여러 축 결과로 알람 원인을 특정하는 것은 L3-a. / [L1-37] v04본 근거.

- **L1-34 Statistics Vehicle 조회**
  - 내용: Statistics > Vehicle에서 날짜 설정 → Search → Save(Excel). 뷰: 차량별 주행거리 및 시간(RunningDist(Km), RunningTime, WorkingCount, TotalRunningTime, TotalWorkingCount), 일별/차량별/일일 차량별 평균 가동률(차량동작: MoveRate/WorkRate/IdleRate/ErrorRate/BlockRate), 일일/차량별 평균 가동률(차량명령: TotalWork/FromTo/From/To/Move/Home/FullCharge·IdleCharge(AGV만)/NoOrder/Error/LineOut), 각각 Table·Chart.
  - 할 수 있어야 하는 것: 지정 기간 차량 가동률을 조회해 Excel로 저장하고, 특정 차량의 ErrorRate·BlockRate 값을 읽어 보고할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p77~83
- **L1-35 Statistics Transfer 조회**
  - 내용: Statistics > Transfer: Order 발생 횟수 및 시간(Date별·Vehicle별·(Date,Vehicle,OrderType)별 FromTo/From/To/Home/Move Count, Avg(FromTo), TotalTime)과 반송명령 스탭별 평균 소요시간(Date/Vehicle/Station 탭: 생성→최초할당 … To도착→To완료, AssignFromDistance, FromToDistance, ErrorCount/TimeSec, BlockingCount/TimeSec, Station 탭은 RetryCountFrom/RetryCountTo 추가)을 조회·저장한다.
  - 할 수 있어야 하는 것: Date/Vehicle/Station 탭을 전환해 스탭별 평균 소요시간과 RetryCountFrom/To를 읽고 Excel로 저장할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p84~87
- **L1-36 Statistics Error·ErrorProfiler**
  - 내용: Statistics > Error: 전체 알람 횟수·시간, 일별, (일별+차량별), 알람별(Code/Type/Event/Text/Count/ErrorTime), 차량별 Data·Chart. Statistics > ErrorProfiler: 날짜 설정 → Search → Save(Excel)로, 선택한 알람을 에러시간대별(발생~Clear 경과시간 구간), 시간대별, 요일별, 차량별(ErrorCount·ErrorTime·RunningDist(Km)·RunningHour·Count·OrderTime)로 조회한다.
  - 할 수 있어야 하는 것: 지정 기간 다발 알람 상위 코드를 Statistics>Error에서 찾고, 그 코드를 ErrorProfiler로 조회해 Excel로 저장할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p88~92, p95~97; OCS 사용자 매뉴얼\_v04\_210114.docx '11.5 ErrorProfiler'
- **L1-37 Statistics Quality 지표**
  - 내용: Statistics > Quality: MTTR=총 에러시간/에러횟수, MTTF=(총 가동시간-총 에러시간)/에러횟수(에러 0이면 총 가동시간), MTBF=고장 발생에서 다음 고장 발생까지 평균시간, MCBF=반송횟수/에러횟수(에러 0이면 반송횟수). Data는 Date, TransferCount, ErrorCount와 4개 지표, Chart 제공.
  - 할 수 있어야 하는 것: Quality 화면을 조회해 4개 지표 값을 읽고, 표의 TransferCount·ErrorCount로 MCBF가 맞는지 손으로 검산할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p93~94

### L1-16 OrderList 판독·개입·NACK 처리

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: Window  ·  **Section / Module**: Screen Operation / Statistics & Window  ·  **범위**: Core  ·  **교육 일차**: 5
- **화면·도구**: Window > OrderList > ORDER 탭 / Window > OrderList > NACK 탭
- **할 수 있어야 하는 것**: ① OrderList에서 지정 오더의 Step·Status·색을 읽어 상태를 말하고, Pause/Resume/Hand Over/DestUpdate/Delete를 절차대로 실행할 수 있다. ② NACK 탭에서 거부된 CommandID와 MESSAGE를 읽어 보고하고 확인 후 CLEAR하며, 과거 건은 NackHistory로 찾을 수 있다.
- **표시**: 사이트의존
- **주의**: [L1-38] OCS에서 Delete 시 상위로 CEID 254(CANCEL)가 먼저 올라가는 흔적 판독은 L3-a. 막힌 반송의 개입 명령 선택 판단은 L2-c. / [L1-39] NACK CODE를 Basic Spec과 대조해 해석하는 것은 L3-a.

- **L1-38 OrderList ORDER 탭·개입**
  - 내용: Window > OrderList ORDER 탭 컬럼: Command ID(Host 수신 또는 'MNL'+생성시간), Vehicle ID, Carrier ID, Origin Type(From/To/Move/Go Home/From To), Type, Step, Priority, Status(에러·수동 운전·블로킹 OHS 호기), Trig Time, Duration. Step 5종: 대기 중 / 주행 중 / 블로킹 정지 / 완료 중 / 경로 탐색 중. Duration이 OrderWarningTimeout을 넘으면 노란색, OrderAlertTimeout을 넘으면 빨간색이다(값 사이트별). 개입 명령: Delete, Pause(Queuing 오더는 할당 금지), Resume, Hand Over(재할당), DestUpdate(목적지 변경).
  - 할 수 있어야 하는 것: OrderList에서 지정 오더의 Step·Status·색을 읽어 상태를 말하고, Pause/Resume/Hand Over/DestUpdate/Delete를 절차대로 실행할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p98~99; OCS Parameter 매뉴얼 p.78 (14.1, 14.2); 3\_SFA\_VHC\_SCENARIO\_SPEC\_V3.5.pdf p.33 (6.2 CANCEL By TSC)
- **L1-39 OrderList NACK 탭**
  - 내용: Window > OrderList NACK 탭은 MCS 메시지에 대한 OCS 거부 이력을 실시간으로 보여준다: DATETIME, MSGTYPE, CSTID, COMMANDID, MESSAGE(거부 원인), NACK CODE(Basic Spec 참조), SOURCE(Unload Port), DEST(Load Port), CLEAR(확인 후 삭제). 과거 NACK은 Report > NackHistory로 조회한다.
  - 할 수 있어야 하는 것: NACK 탭에서 거부된 CommandID와 MESSAGE를 읽어 보고하고 확인 후 CLEAR하며, 과거 건은 NackHistory로 찾을 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p99

### L1-17 실시간 창 판독 (AlarmList·ErrorList·PingList·CommEvent)

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: Window  ·  **Section / Module**: Screen Operation / Statistics & Window  ·  **범위**: Core  ·  **교육 일차**: 5
- **화면·도구**: Window > AlarmList / 메인 화면 ⑦ErrorList (FOCUS / CLEAR) / Window > PingList / Window > CommEvent
- **할 수 있어야 하는 것**: ① 알람 목록에서 중알람과 오래된 경알람을 색으로 구분하고, FOCUS로 발생 호기 위치를 찾아 ERRCODE·EVENT·ELAPSEDTIME을 보고할 수 있다. ② PingList에서 CURERRORCOUNT가 증가 중인 Unit을 찾아 SETERRORCOUNT까지 남은 여유를 말할 수 있다. ③ CommEvent를 열어 지정 차량의 최신 메시지 행을 찾아 CurPoint·TargetPoint·Mode 항목 위치를 짚을 수 있다.
- **표시**: 사이트의존, 민감정보
- **주의**: [L1-40] 색 변화 시간(WarningErrorTimeover)은 사이트별 설정값. / [L1-41] IP 컬럼은 배포 시 마스킹. 2채널 IP 규칙으로 이중화 단절을 판정하는 것(검증자 missing 16)은 L1 범위 밖(L2-c/L3-a). / [L1-43] BSt 비트·Status 값 디코딩 등 원문 판독은 L3-a.

- **L1-40 AlarmList·ErrorList 판독**
  - 내용: Window > AlarmList는 Error 발생 시 자동 생성, 없으면 자동으로 사라진다. 경알람은 흰색으로 뜨다가 WarningErrorTimeover 경과 후 빨간색, 중알람은 처음부터 빨간색이다. 컬럼: NUMBER(Vehicle Number), NAME(OnlineName), ONTIME, ERRCODE(RCP 등록 코드), Type(발생 주체), EVENT(Vehicle→RCP Error Code Number), ERRTEXT, ELAPSEDTIME, FOCUS(클릭 시 해당 호기 확대, 배율은 ZoomFocusLevel). 메인 화면 ⑦ErrorList는 여기에 NUM, CLEAR 컬럼이 있다.
  - 할 수 있어야 하는 것: 알람 목록에서 중알람과 오래된 경알람을 색으로 구분하고, FOCUS로 발생 호기 위치를 찾아 ERRCODE·EVENT·ELAPSEDTIME을 보고할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p100; OCS Parameter 매뉴얼 p.79 (14.4 WarningErrorTimeover, 14.5 ZoomFocusLevel); CPU\_RAM\_HDD 점검 메뉴얼\_20220607.pdf p.5 (ErrorList 컬럼)
- **L1-41 PingList 판독**
  - 내용: Window > PingList 12컬럼: NUMBER, NAME, IP, TYPE, USE, INTERVAL(Ping 주기), SENDBYTE, RECVTIMEOUT(응답 제한 시간), CURERRORCOUNT(현재 Error Count), SETERRORCOUNT(Error 발생 기준값), REPLYTIMELIMIT(Error로 기록하는 응답시간 최대치), UPDATETIME. PING 알람은 1회 실패가 아니라 CURERRORCOUNT가 SETERRORCOUNT에 도달해야 뜬다.
  - 할 수 있어야 하는 것: PingList에서 CURERRORCOUNT가 증가 중인 Unit을 찾아 SETERRORCOUNT까지 남은 여유를 말할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.docx '12.4 PingList'; OCS 사용자 매뉴얼\_v04\_210114.pdf p102
- **L1-43 CommEvent 창 열기**
  - 내용: Window > CommEvent는 Vehicle과 실시간으로 주고받은 통신을 Number(Vehicle Number), RegTime, Message로 보여준다. Message에는 CurPoint, DirectionPoint, ChangeRoutePoint, TargetPoint, Mode(Auto/Manual), Status, Error, Dist, Speed, RACK, BSt, CstID 항목이 들어 있고, 과거 이력은 CommHistory로 조회한다.
  - 할 수 있어야 하는 것: CommEvent를 열어 지정 차량의 최신 메시지 행을 찾아 CurPoint·TargetPoint·Mode 항목 위치를 짚을 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p104

### L1-18 PlayBack 재현·Export

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: PlayBack  ·  **Section / Module**: Screen Operation / PlayBack & Help  ·  **범위**: Core  ·  **교육 일차**: 5
- **화면·도구**: PlayBack > Run (배속 1~16 / 시간설정 / 시간단위 1~30분 / 불러오기) / PlayBack > Export
- **할 수 있어야 하는 것**: ① 지정 시각 전후 10분을 불러와 배속을 바꿔 재생하고, 특정 시점의 차량 위치와 Error를 화면에서 짚을 수 있다. ② 지정 시각의 PlayBack 30분 분량을 Export하고 저장 경로에서 파일을 찾아 전달할 수 있다.
- **표시**: 사이트의존
- **주의**: [L1-45] 재현 결과로 원인을 단정하는 것은 L3-a. / [L1-46] 저장 경로는 사이트 Parameter 설정값.

- **L1-45 PlayBack Run 재현 조작**
  - 내용: PlayBack > Run은 Oder List(당시 Order), UI(당시 Layout·Vehicle 상태), Error(당시 Error)를 동시에 재현한다. 시간설정으로 실행 시각을 정하고 시간단위를 분 단위 1~30분으로 지정해 불러오기를 누른 뒤, PlayBack Control로 배속(1~16배속)·실행·일시정지를 조작하고 스크롤 바로 재생 시간을 이동한다.
  - 할 수 있어야 하는 것: 지정 시각 전후 10분을 불러와 배속을 바꿔 재생하고, 특정 시점의 차량 위치와 Error를 화면에서 짚을 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p109~110; 검증자 권고10 (PlayBack>Run L1 복원)
- **L1-46 PlayBack Export**
  - 내용: PlayBack > Export에서 시간을 선택하면 그 시각부터 30분 분량이 추출되고, Export를 누르면 메인 서버 하드에 저장된다(저장 경로는 Parameter에서 설정). 장애 상황을 본사·타 사이트로 넘길 때 쓴다.
  - 할 수 있어야 하는 것: 지정 시각의 PlayBack 30분 분량을 Export하고 저장 경로에서 파일을 찾아 전달할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p110

### L1-19 Help Version·Define·주요 용어

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: Help  ·  **Section / Module**: Screen Operation / PlayBack & Help  ·  **범위**: Core  ·  **교육 일차**: 5
- **화면·도구**: Help > Version (Show) / Help > Define / _MANUAL_User Manual_V01_MXA.docx '용어 설명' 장
- **할 수 있어야 하는 것**: ① Help>Version에서 각 구성 프로그램 버전을 읽어 기록하고 Show로 최근 Update 내용을 확인할 수 있다. ② layout 화면에서 지정한 객체 색을 Help>Define과 대조해 그 객체 상태를 말할 수 있다. ③ 화면·매뉴얼에 나오는 약어(MCS, MCCS, MCP, MTL, NCP(CPS), PIO 등)를 보고 무엇인지 한 줄로 말할 수 있다.
- **주의**: [L1-47] MXA본 13.1 기준(Core, Plc Driver, MCS_IF, DB, RCPGT 버전 표시). 구조적 의미는 L2-b. / [L1-49] MXA본 용어 설명 장 기준. 메뉴 화면이 아니라 매뉴얼 장이라 Help 탭에 붙임.

- **L1-47 Help Version 확인**
  - 내용: Help > Version은 각 Program 명과 Version을 표시하고, Show를 누르면 해당 버전과 이전 버전의 Update 내용을 보여준다. MXA본은 Core, Plc Driver, MCS_IF, DB, RCPGT 버전을 표시한다고 명시한다.
  - 할 수 있어야 하는 것: Help>Version에서 각 구성 프로그램 버전을 읽어 기록하고 Show로 최근 Update 내용을 확인할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p111; \_MANUAL\_User Manual\_V01\_MXA.docx Help>Version
- **L1-48 Help Define 색상 정의**
  - 내용: Help > Define은 Object 색상별 상태 정의표다. 범주: Point, Segment, AlramLamp, Charger, CPS, Door, MTL, PLC Group, Ping Unit(Normal/Bridge/Access Point/Hub), Safety(Hot Line, Junction Point, Light Curtain, Manual Key, Safety Mat, Slide Door, Teach Mode, Reel Sensor), Station(Evaporator, Station, Stocker, Transfer Buffer), Vehicle(OHS, MultiFTE, AGV).
  - 할 수 있어야 하는 것: layout 화면에서 지정한 객체 색을 Help>Define과 대조해 그 객체 상태를 말할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p112~114
- **L1-49 OCS 주요 용어**
  - 내용: MXA본 '용어 설명' 장: CIM, DATABASE, FDC, FTP, Graphic, HOST, IP, I/O, MCS, MCCS(Mantech Continuous Cluster Server, 고가용성 이중화 솔루션), MCP, MCT, MTL, MTU, MTS, NCP(CPS), PIO, POINT, PINGUNIT, PLCGROUP, SEGMENT, STATION, VEHICLE.
  - 할 수 있어야 하는 것: 화면·매뉴얼에 나오는 약어(MCS, MCCS, MCP, MTL, NCP(CPS), PIO 등)를 보고 무엇인지 한 줄로 말할 수 있다.
  - 근거: \_MANUAL\_User Manual\_V01\_MXA.docx '용어 설명' 장

### L1-20 MCS_IF Cfg/SML 등록·상위 연결 확인

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: MCS_IF  ·  **Section / Module**: Host Interface (HSMS) / MCS_IF Config  ·  **범위**: Core  ·  **교육 일차**: 7
- **화면·도구**: MCS_IF > View 탭 > XcomCfgSmlFileManager / Xcom Config Info / Xcom SML File / MCS_IF (상단 점등 / MCS System Msg / MCMD) / XcomPro Simulator / OrderList / Report > HSMSHistory
- **할 수 있어야 하는 것**: ① 교육 서버에서 cfg/sml을 등록해 Select=True로 만들고 Xcom Config Info·Xcom SML File로 적용 여부를 확인할 수 있다. ② 상위 연결 4단계(IP 전달→Change to Select→S1F17→MCMD 점등)를 수행하고, Simulator로 S2F49 오더를 보내 OrderList 생성까지 확인할 수 있다.
- **표시**: 사이트의존, 자료충돌, 민감정보
- **주의**: [L1-50] MCS_IF는 OCS UI와 별개 프로그램이며 그 안의 View 탭. cfg 경로·Sys Type은 사이트별. Xcom configuration으로 Message Spec과 비교하는 것은 L2-b. MCS_IF 프로그램 화면은 사용자 매뉴얼 3판에 없고 setup 가이드·설치 기준서에만 있다. MXA본 2.2(프로그램 구성도)는 "RCP GT를 제외한 프로그램들은 사용자 Interface가 없고, 내부적으로 구동되고 있는 프로그램"이라 적고 있어(MCS_IF 포함) 현장 MCS_IF 화면 유무를 확인해야 한다. / [L1-51] MCS_IF 화면은 OCS 메뉴 탭 밖. Server IP는 배포 시 마스킹. MCS_IF의 역할·통신 상대 설명과 드라이버 설정파일(IP 0.0.0.0)은 C230 주 버킷(L2-b). MCS_IF 프로그램 화면은 사용자 매뉴얼 3판에 없고 setup 가이드·설치 기준서에만 있다. MXA본 2.2(프로그램 구성도)는 "RCP GT를 제외한 프로그램들은 사용자 Interface가 없고, 내부적으로 구동되고 있는 프로그램"이라 적고 있어(MCS_IF 포함) 현장 MCS_IF 화면 유무를 확인해야 한다.

- **L1-50 MCS_IF Cfg/SML 등록 확인**
  - 내용: MCS_IF 실행 → View 탭 XcomCfgSmlFileManager(XCom CfgSml Manager) → Name, Sys Type 설정, Cfg·SML 파일 경로 입력 → NewItem/Upload → 등록한 시스템 활성화 → List에서 Select=True 확인 → View 탭 Xcom Config Info로 Config 적용, Xcom SML File로 SML 적용을 확인한다. MCS_IF가 안 뜨면 XCOM Driver 설치 여부와 Select=True를 먼저 확인한다.
  - 할 수 있어야 하는 것: 교육 서버에서 cfg/sml을 등록해 Select=True로 만들고 Xcom Config Info·Xcom SML File로 적용 여부를 확인할 수 있다.
  - 근거: RCP Program setup 가이드 p.44 (6.3 MCS Config, SML 확인) 표38; OCS 설치 기준서 p.24~25 (2.10); 검증자 missing 2 (MCS\_IF 상위 연결 설정)
- **L1-51 상위(MCS) 연결 확인 절차**
  - 내용: ipconfig /all로 공장망 Server IP를 확인해 MCS측에 MCS_IF 동작 서버 IP를 전달 → MCS_IF 상단 점등색과 MCS System Msg의 'Change to Select(HSMS)' 확인 → S1F17(RE-Quest Online) 입력 → MCMD 점등(REMOTE) 확인. 교육 서버에서는 XcomPro Simulator로 S1F17(MCMD REMOTE), S2F41(Count:6, Value:RESUME → TSC AUTO), S2F49(오더 정보 기입 후 Send)를 보내 RCP UI OrderList의 오더 생성·차량 반송과 Report > HSMSHistory를 확인한다.
  - 할 수 있어야 하는 것: 상위 연결 4단계(IP 전달→Change to Select→S1F17→MCMD 점등)를 수행하고, Simulator로 S2F49 오더를 보내 OrderList 생성까지 확인할 수 있다.
  - 근거: RCP Program setup 가이드 p.39 (6.1 상위와의 통신 연결 및 확인) 표33; OCS 설치 기준서 p.34, p.37~38 (4장 절차 8, 9, 14, 15)

## L2-a 맵·통행영역 수정

### L2a-01 RDT 기본 조작 (실행·사이트 생성·열기·저장·개정)

- **레벨**: L2  ·  **교육 방식**: 도구실습  ·  **탭**: 외부도구  ·  **Section / Module**: Map & Traffic Control / RDT Basics  ·  **범위**: Core  ·  **교육 일차**: 6
- **화면·도구**: RailDesignTool 2 — 메인 창 / Save Path Configuration / Navigation 트리 / RailDesignTool 2 — File > New > Layout Configuration / Vehicle(s) Configuration / Finish Configuration / RailDesignTool 2 — File > Open / File > Save / Save As / 사이트 우클릭 > Import Json File
- **할 수 있어야 하는 것**: ① RDT를 실행해 버전과 기본 데이터 경로를 확인하고, 지정된 Point·Segment ID를 Navigation 트리에서 찾아 Select and Zoom으로 화면에 띄울 수 있다. ② 배경 CAD 파일과 차량 제원을 지정해 RDT에 새 사이트·도면을 만들고, Finish Configuration 요약이 입력값과 맞는지 대조할 수 있다. ③ 수정 전에 Save As로 사본을 만들고, 수정 후에는 Details를 기록해 Save한 다음, Open 창의 Revision History에서 원하는 개정판을 찾아 다시 열 수 있다.
- **표시**: 사이트의존, 근거약함, 추정해석
- **주의**: [L2a-01] 기본 경로와 버전은 PC·사이트마다 다르다. / [L2a-02] C130(차량 제원)은 검증자 missing 반영으로 이 버킷 밖 후보를 연결한 것이다. 제원 값이 오토블로킹 계산 입력이 되는 의미와 검증은 L3-c와 겹치므로, 여기서는 입력 조작만 평가한다. 차량 제원 값은 사이트별로 확인한다. / [L2a-03] MapData 폴더는 매뉴얼에 설명이 없다. 'Save As가 사실상 백업 수단'이라는 평가는 조사자의 해석이다. 운영 맵 백업·롤백 절차로 쓰는 경우와 과거 Export본을 Import해 롤백하는 경우는 L3-c다.

- **L2a-01 RDT 화면·경로 구성**
  - 내용: 창 타이틀 'RAIL DESIGN TOOL 2 - [SFA - 라인 1]'(Site > Drawing 2계층)과 상태표시줄 버전 'ver 23.11_002 x64'를 확인한다. 메인 6영역(메뉴 바 / Navigation / 디자인 작업 창 / Design Attributes / 일괄 작업 창 / 상태표시줄 x·y·ratio)과 메뉴 File·Edit·View·Setup·Tool·Window·Help를 구분한다. 'Save Path Configuration'의 Path(예: E:\ManualWork, 사이트별 확인)를 Open Path로 확인하고, Navigation 트리 SFA > 라인 1 > Vehicle / SegmentTemplate / Segment / Point에서 ID로 객체를 찾아 Select / Zoom / Select and Zoom으로 이동한다.
  - 할 수 있어야 하는 것: RDT를 실행해 버전과 기본 데이터 경로를 확인하고, 지정된 Point·Segment ID를 Navigation 트리에서 찾아 Select and Zoom으로 화면에 띄울 수 있다.
  - 근거: 24-02-RailDesignTool-Manual.pdf p.1, p.4~9
- **L2a-02 RDT 사이트 신규 생성**
  - 내용: File > New를 실행하면 'Layout Configuration' 마법사가 열린다. Site / Drawing Name / Drawing File(\*.dxf/\*.dwg, Search) / Details를 입력하고 Steer Drive·Differential(Diff)·QUAD 차량 보유 여부를 체크한다. 이어지는 차량 창(예: 'Steer Drive Vehicle(s) Configuration')에서 대수, Vehicle Name, Length/Width, Rear·Front detection distance 등을 입력한다. 'Finish Configuration'에서 Site, Drawing File, Version 1.0, 'Configured Steer Drive (SD) vehicle(s) : SD1, SD2' 같은 요약을 확인한 뒤 Finish를 누른다.
  - 할 수 있어야 하는 것: 배경 CAD 파일과 차량 제원을 지정해 RDT에 새 사이트·도면을 만들고, Finish Configuration 요약이 입력값과 맞는지 대조할 수 있다.
  - 근거: 24-02-RailDesignTool-Manual.pdf p.11~15
- **L2a-03 RDT 열기·저장·개정**
  - 내용: 사이트 폴더 구조는 기본경로\SFA\{drawing file, 라인 1, revision.info}다. File > Open 창의 Revision History(Revision Number / Revision Date / Description)에서 개정판을 골라 연다. File > Save 창에서는 Details에 변경 내역을 적고 Ok를 눌러 revision.info에 기록한다. File > Save > Save As('Save as a different drawing name')로 새 Drawing Name 사본을 만들고, 사이트 우클릭 > Import Json File로 JSON(예: E:\test.json)을 읽어 들인다. 이 결과물은 모두 사이트 폴더 안에만 남는다.
  - 할 수 있어야 하는 것: 수정 전에 Save As로 사본을 만들고, 수정 후에는 Details를 기록해 Save한 다음, Open 창의 Revision History에서 원하는 개정판을 찾아 다시 열 수 있다.
  - 근거: 24-02-RailDesignTool-Manual.pdf p.6, p.8, p.16~17, p.27~28, p.35

### L2a-02 RDT 작도·편집·방향 확인

- **레벨**: L2  ·  **교육 방식**: 도구실습  ·  **탭**: 외부도구  ·  **Section / Module**: Map & Traffic Control / RDT Basics  ·  **범위**: Core  ·  **교육 일차**: 6
- **화면·도구**: RailDesignTool 2 — Edit 리본(선택 그룹), Edit > Object > Segment / RailDesignTool 2 — 디자인 작업 창 / Navigation 팝업 / 일괄 작업 창(Point Editing, Label Editing, Move the entire layout) / RailDesignTool 2 — Segment Template Attributes / Tool > Direction / Tool > Swept / 디자인 창 우클릭
- **할 수 있어야 하는 것**: ① 지정된 차량·작도 종류·템플릿으로 직선과 곡선 세그먼트를 이어 그리고, 작도를 정상적으로 끝맺을 수 있다. ② 여러 포인트를 선택해 좌표를 일괄 정렬하고, 잘못된 편집을 Undo로 되돌리며, 조회만 할 때는 Lock을 걸어 맵을 보호할 수 있다. ③ 작도한 구간에 진행 방향과 차량 궤도를 표시해 템플릿의 Forward Direction과 실제 진행 방향이 일치하는지 확인할 수 있다.
- **표시**: 추정해석, 사이트의존
- **주의**: [L2a-04] RDT 매뉴얼 기준. LayOut Designer 절차(setup 가이드 표19)는 사이트 도구가 RDT로 확정되어 뺐다. / [L2a-05] Move the entire layout을 쓰면 좌표계가 실 설비와 틀어진다는 위험은 조사자의 해석이다. 이동한 좌표계를 실 시스템에 반영할지 판단하는 것은 L3-c다. / [L2a-07] C148(Swept 5종)은 검증자 missing 반영으로 이 버킷 밖 후보를 연결한 것이다. 오토블로킹 검증 수단으로 쓰는 것은 L3-c다. Speed / Point Clearance Distance / Weight 값을 바꿔 경로·거동을 조정하는 것은 L3다. 템플릿 목록은 사이트별로 다르다.

- **L2a-04 세그먼트 작도**
  - 내용: Edit 리본 '선택' 그룹의 세 드롭다운(차량 'SD1' / 작도 종류 'Arc [x2y2]' / 세그먼트 템플릿 'SD1_Forward')을 먼저 정한다. 그다음 Edit > Object > Segment로 들어가 시작점에서 클릭해 방향을 정하고, 다음 위치에서 클릭을 해제해 이어 그리며, 우클릭이나 더블클릭으로 마친다. 진행 각도는 45도 단위로 회전하고 {Alt}로 미세 회전, {Shift}+첫 클릭으로 직선(종점 녹색)을 그리며, {ESC}는 한 단계씩 취소한다.
  - 할 수 있어야 하는 것: 지정된 차량·작도 종류·템플릿으로 직선과 곡선 세그먼트를 이어 그리고, 작도를 정상적으로 끝맺을 수 있다.
  - 근거: 24-02-RailDesignTool-Manual.pdf p.5~6, p.18, p.20
- **L2a-05 객체 선택·편집·일괄이동**
  - 내용: 선택은 클릭, {Ctrl}+클릭(추가·해제), {Shift}+드래그(영역 선택), {Ctrl}+{Shift}+드래그(영역 추가), {Esc}(전체 해제)로 한다. 이미 그린 세그먼트는 {Ctrl}+진행 방향 점 드래그로 곡선 길이를, {Ctrl}+방향키로 포인트 회전각을 고친다. 트리·디자인 창 팝업에서 Cut/Copy/Paste/Delete/New/Attributes를 쓰고, Undo/Redo와 Edit > Lock(리본 '잠그기 > Drawing')을 쓴다. 일괄 작업 창은 Point Editing(X/Y-coordinate Apply All, Horizontal/Vertical Spacing Alignment), Label Editing, Move the entire layout(number of moves, Move Up/Down/Left/Right)을 쓴다. 이전 값을 유지하려면 {Shift} 영역 선택을 쓴다.
  - 할 수 있어야 하는 것: 여러 포인트를 선택해 좌표를 일괄 정렬하고, 잘못된 편집을 Undo로 되돌리며, 조회만 할 때는 Lock을 걸어 맵을 보호할 수 있다.
  - 근거: 24-02-RailDesignTool-Manual.pdf p.5~6, p.8~10, p.19, p.21~24
- **L2a-07 템플릿·방향·궤도 표시**
  - 내용: Segment Template Attributes에는 Template Name, Forward Direction, Template Color, Segment Type, Speed[%], Point Clearance Distance, Weight가 있다(사이트 예: Diff1_Forward, Quad1_2\*SD=>Diff_Reverse). Tool > Direction > Show/Hide All Direction과 우클릭 > Direction으로 정·역방향을 표시한다. Tool > Swept > Show/Hide All Swept와 우클릭 > Swept로 궤도 5종(SD Forward / Diff Forward / 2\*SD → Diff Forward / Crabwise Forward / Diff → 2\*SD Forward)을 표시한다.
  - 할 수 있어야 하는 것: 작도한 구간에 진행 방향과 차량 궤도를 표시해 템플릿의 Forward Direction과 실제 진행 방향이 일치하는지 확인할 수 있다.
  - 근거: 24-02-RailDesignTool-Manual.pdf p.7, p.9, p.25~26, p.31, p.34

### L2a-03 RDT 속성 설정 (Point·Segment·Drawing)

- **레벨**: L2  ·  **교육 방식**: 도구실습  ·  **탭**: 외부도구  ·  **Section / Module**: Map & Traffic Control / RDT Basics  ·  **범위**: Core  ·  **교육 일차**: 6
- **화면·도구**: RailDesignTool 2 — Point Attributes / Segment Attributes(General, Segment Parts) / RailDesignTool 2 — Setup > Layout > Drawing Attributes / View > Drawing, Drawing Info
- **할 수 있어야 하는 것**: ① Point Attributes의 Incoming/Outgoing으로 분기·합류 지점을 판별하고, Segment Attributes에서 Start/End Point·템플릿·Length·Travel Time을 읽고 좌표·각도를 고칠 수 있다. ② 요청받은 설정(배경 레이어 숨김, 작도 영역 좌표, 특정 템플릿만 표시)이 6개 탭 중 어디에 있는지 찾아가 변경할 수 있다.
- **표시**: 사이트의존
- **주의**: [L2a-06] Speed[%]를 바꿔 실제 주행 거동을 조정하는 일은 L3다. L2에서는 읽고 확인하는 데까지만 한다. / [L2a-08] Auto Blocking Configuration 탭(Safety Margin)은 L3-c 대상이라 이 항목에서 뺐다. 좌표 범위와 CAD 파일은 사이트별로 확인한다.

- **L2a-06 Point·Segment 속성**
  - 내용: Point Attributes > General에는 Point ID, X/Y-coordinate, Angle[degrees], Opposite Angle 버튼, Segment Incoming/Outgoing('1 Template: SD1_Forward')이 있다. Segment Attributes > General에는 Segment ID, Start/End Point, Vehicle, Segment Template, Speed[%], Forward Direction, Length, Travel Time[s], Calculate Travel Time이 있다. Segment Parts 탭은 Type / Start Point / Start Angle / End Point / End Angle / Speed / Length 표를 보여 준다.
  - 할 수 있어야 하는 것: Point Attributes의 Incoming/Outgoing으로 분기·합류 지점을 판별하고, Segment Attributes에서 Start/End Point·템플릿·Length·Travel Time을 읽고 좌표·각도를 고칠 수 있다.
  - 근거: 24-02-RailDesignTool-Manual.pdf p.32~33
- **L2a-08 Drawing Attributes 설정**
  - 내용: Setup > Layout(또는 사이트 우클릭 > Attributes)으로 Drawing Attributes 6탭을 연다. Drawing Configuration에서는 Drawing File 지정과 레이어 체크(Show All/Hide All)를, Drawing에서는 Color RGB(Point, Swept, Swept Outline/Start/Last Vehicle Color)를 설정한다. Drawing Boundary에서는 Original DWG의 Min/Max X·Y와 Drawing Modification 작도 영역을, ID View Properties와 Object View Properties에서는 Points/Segments 표시와 템플릿별 표시를 정한다. View > Drawing([Point ID][Segment ID][Boundary][Swept])과 Drawing Info도 함께 쓴다.
  - 할 수 있어야 하는 것: 요청받은 설정(배경 레이어 숨김, 작도 영역 좌표, 특정 템플릿만 표시)이 6개 탭 중 어디에 있는지 찾아가 변경할 수 있다.
  - 근거: 24-02-RailDesignTool-Manual.pdf p.6~8, p.29~31

### L2a-04 System>Unuse·Home 설정

- **레벨**: L2  ·  **교육 방식**: 화면실습  ·  **탭**: System  ·  **Section / Module**: Map & Traffic Control / OCS Traffic Settings  ·  **범위**: Core  ·  **교육 일차**: 6
- **화면·도구**: 메뉴 탭 > System > Unuse / 메뉴 탭 > System > Home / System > Order Group
- **할 수 있어야 하는 것**: ① 우회경로를 확인한 뒤 지정 구간을 전체 또는 특정 호기에 대해 Unuse로 설정·해제하고, Layout 색상으로 적용 여부를 검증할 수 있다. ② 반송 Port 배치를 근거로 Home Point를 추가·Unuse·삭제하고 OrderGroup에 등록한 뒤, Layout 색상으로 결과를 확인할 수 있다.
- **표시**: 사이트의존
- **주의**: [L2a-10] 1.5~2배는 설계 예시이며 사이트별로 확인한다. Layout 색상 의미를 아는 것 자체는 L1이다.

- **L2a-09 System>Unuse 진입금지**
  - 내용: 메뉴 탭 > System > Unuse에서 All(전체 차량) 또는 특정 호기를 고르고, Unuse 대상 point·segment를 선택한 뒤 SAVE한다. 적용되면 Layout에서 해당 Point가 회색에서 황색으로 바뀐다. 매뉴얼 경고에 따라 반송지연이 생길 수 있으므로 우회경로를 먼저 확인한다. 변경 이력은 UIHistory와 연계된다.
  - 할 수 있어야 하는 것: 우회경로를 확인한 뒤 지정 구간을 전체 또는 특정 호기에 대해 Unuse로 설정·해제하고, Layout 색상으로 적용 여부를 검증할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p19, p72
- **L2a-10 System>Home 등록**
  - 내용: System > Home에서 Delete/Clear/Insert 조작창으로 Point 번호를 Insert해 Home Point를 추가하고, 추가한 뒤에는 반드시 Order Group에도 등록한다. Unuse는 포인트 선택 → Unuse 체크박스 → Save 순서다. Layout에서 Home은 갈색, 해제는 회색으로 보인다. 등록 기준 예시는 등록 차량 대수의 1.5~2배이고, 분기 바로 전 Point는 분기 감지 센서 알람 가능성이 있어 피한다. Station 포인트와 같은 포인트를 Home으로 쓰기도 한다.
  - 할 수 있어야 하는 것: 반송 Port 배치를 근거로 Home Point를 추가·Unuse·삭제하고 OrderGroup에 등록한 뒤, Layout 색상으로 결과를 확인할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p13~15; RCP Program setup 가이드 p.32(5.5 Home 등록)

### L2a-05 System 통행 제어 영역 (Cluster·StationWeightGroup·AutoParkArea)

- **레벨**: L2  ·  **교육 방식**: 화면실습  ·  **탭**: System  ·  **Section / Module**: Map & Traffic Control / OCS Traffic Settings  ·  **범위**: Core  ·  **교육 일차**: 6
- **화면·도구**: 메뉴 탭 > System > Cluster (Cluster Point / Dest Point / Cluster Info·Setting) / 메뉴 탭 > System > StationWeightGroup / 메뉴 탭 > System > AutoParkArea
- **할 수 있어야 하는 것**: ① Deadlock 우려 구간을 Cluster Point 집합으로 등록하고 MaxVehicleCount를 지정해 저장한 뒤, 재조회해서 포인트가 실제로 저장되었는지 확인할 수 있다. ② 지정된 From·To Station 반송에 대해 우회시킬 Segment를 StationWeightGroup으로 등록·저장할 수 있다. ③ AutoParkAreaGroup을 만들어 ParkArea Point를 지정하고, Sub Command로 차량을 대기구간에 넣고 빼낼 수 있다.
- **표시**: 사이트의존, 근거약함, 추정해석
- **주의**: [L2a-11] System>Cluster 화면·Point/Dest Point 조작·Simulation 경고는 v04본·중문통합본 7.2 근거. Info/Setting 구분, EntranceLimit, MaxVehicleCount=1 예시는 RCP_Parameter_Manual_v0.0.1 Cluster 근거(사용자 매뉴얼 Cluster Info에는 EntranceLimit 없음). MaxVehicleLowCount/HighCount 같은 Cluster Info 수치를 바꿔 거동을 튜닝하는 것은 L3-a. C306 Insert 실패는 원인 미규명이라 채점하지 않는 주의사항으로만 쓴다. 화면 필드명 오기(MaxVehicleConut) 있음. / [L2a-12] Weight 값을 조정해 반송 경로 문제를 해결하는 것은 L3-a다. / [L2a-17] MXA본 6.7 기준. PlcTagmonitor 실시간 확인과 Report>Move History 조회는 L1로 분리.

- **L2a-11 System>Cluster 영역**
  - 내용: System > Cluster에서 Cluster Point(영역 포함)와 Dest Point(목적지가 여기 있으면 영향받음)를 추가·삭제한다(Ctrl+Point / Shift+드래그, 영역 표시/해제 아이콘). Info(ClusterID, Name, EntranceLimit)와 Setting(MaxVehicleCount, MaxVehicleReleaseCount, Unuse)을 입력한다. 예를 들어 MaxVehicleCount=1이면 11호기가 영역을 벗어날 때까지 12·13호기는 진입하지 못한다. 매뉴얼은 '사전에 충분한 Simulation 후 설정'을 경고한다. 알려진 현상으로 Point Insert 후 Save하면 success가 표시되지만 포인트가 초기화되는 사례가 있고, 원인은 아직 밝혀지지 않았다.
  - 할 수 있어야 하는 것: Deadlock 우려 구간을 Cluster Point 집합으로 등록하고 MaxVehicleCount를 지정해 저장한 뒤, 재조회해서 포인트가 실제로 저장되었는지 확인할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p16~18; RCP\_Parameter\_Manual\_v0.0.1 Cluster(P61~114); 02. RCPHMI.txt 11~12행(현상 3)
- **L2a-12 StationWeightGroup**
  - 내용: System > StationWeightGroup에서 StationWeightGroup Number를 Insert하고, 그룹에 From·To Station을 추가한 다음 Segment를 추가하고 Weight를 할당해 Save한다. 특정 Station 반송이 생성될 때 해당 Segment에 가중치가 붙어 우회경로로 유도된다. Object>Segment의 AddWeight와 함께 경로 제어 수단을 이룬다.
  - 할 수 있어야 하는 것: 지정된 From·To Station 반송에 대해 우회시킬 Segment를 StationWeightGroup으로 등록·저장할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p23
- **L2a-17 AutoParkArea 대기구간**
  - 내용: System > AutoParkArea에서 AutoParkAreaGroup을 Insert하고 ParkArea Point를 지정한다. Sub Command로 SelfFocus(해당 Area로 이동), Vehicle(선택 Vehicle을 ParkArea Point로 이동), VehicleOut(선입 차량 양산 투입)을 쓴다. 반송량 증감에 따른 대기 구간을 설정하는 화면이다.
  - 할 수 있어야 하는 것: AutoParkAreaGroup을 만들어 ParkArea Point를 지정하고, Sub Command로 차량을 대기구간에 넣고 빼낼 수 있다.
  - 근거: \_MANUAL\_User Manual\_V01\_MXA.docx AutoParkArea(6.7)

### L2a-06 Object>Point Type·UserBlock/DisableBlock 설정

- **레벨**: L2  ·  **교육 방식**: 화면실습  ·  **탭**: Object  ·  **Section / Module**: Map & Traffic Control / OCS Traffic Settings  ·  **범위**: Core  ·  **교육 일차**: 6
- **화면·도구**: 메뉴 탭 > Object > Point (Point Type) / 메뉴 탭 > Object > Point / Object > Segment (AutoBlock, UserBlock, DisableBlock, AddWeight)
- **할 수 있어야 하는 것**: ① 설비 배치와 맞지 않는 Point Type을 찾아 올바른 Type으로 변경·저장하고 반영을 확인할 수 있다. ② 특정 Point·Segment의 AutoBlock 목록을 조회하고 UserBlock/DisableBlock을 추가·제외해 저장할 수 있으며, 최초설치 Layout 점검표의 Block 설정 여부를 확인할 수 있다.
- **표시**: 사이트의존
- **주의**: [L2a-13] Point Type 7종의 의미를 아는 것은 L1이다. 이 항목은 변경 조작을 평가한다. / [L2a-14] AutoBlock 자동 계산(RailDesignTool)은 L3-c다. 매뉴얼 원문은 'Winlay 상에서'로 적혀 있다. 속도·차량 사이즈 값은 사이트별 기준이며, 그 값을 바꾸는 것은 L3다.

- **L2a-13 Object>Point Type 변경**
  - 내용: Object > Point에서 Point Type 7종(Normal / Pass / Stop / Equipment / SideBuffer / MTL Maint / MTL Lifter) 가운데 설비 구성에 맞는 값을 고른다. 절차는 Point 선택 → Point Type 선택 → SAVE → 변경 확인이다. Pass Point에서는 정차 없이 지나치며 RCP가 Pass Point 명령을 내릴 수 없다. 선행조건: 10.19 PassPointReleaseInterlock에 등록되지 않은 Point는 Pass 등록·해제 시 "해당 포인트는 PointType을 변경할 수 없습니다" 팝업이 뜬다.
  - 할 수 있어야 하는 것: 설비 배치와 맞지 않는 Point Type을 찾아 올바른 Type으로 변경·저장하고 반영을 확인할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p40~41
- **L2a-14 UserBlock·DisableBlock**
  - 내용: Object > Point / Object > Segment에서 AutoBlock(맵 도구에서 차량·세그먼트 사이즈로 자동 계산된 Block Segment List — 현 사이트는 RailDesignTool 오토블로킹)을 확인한다. UserBlock으로 Block Segment를 추가하고 DisableBlock으로 제외하며, Segment 화면에서는 AddWeight를 쓴다. 매뉴얼 경고에 따라 AddWeight와 UserBlock은 Simulation 후 설정한다. 최초설치 Layout 점검 항목은 커브/직진 속도, 차량 사이즈, Point/Segment UserBlock/DisableBlock 설정 여부다.
  - 할 수 있어야 하는 것: 특정 Point·Segment의 AutoBlock 목록을 조회하고 UserBlock/DisableBlock을 추가·제외해 저장할 수 있으며, 최초설치 Layout 점검표의 Block 설정 여부를 확인할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p41~42; 01. RCP 최초설치 확인사항.txt 66~69행

### L2a-07 Safety·CPS Interlock·MTL 유지보수 존 설정

- **레벨**: L2  ·  **교육 방식**: 화면실습  ·  **탭**: Object  ·  **Section / Module**: Map & Traffic Control / OCS Traffic Settings  ·  **범위**: Core  ·  **교육 일차**: 6
- **화면·도구**: 메뉴 탭 > Object > Safety / Object > CPS / Order List > Step 탭 / 메뉴 탭 > Object > MTL
- **할 수 있어야 하는 것**: ① Safety 또는 CPS의 Interlock Down Segment 범위를 설정·변경하고, CPS GroupNumber를 지정해 저장한 뒤 상태값을 확인할 수 있다. ② MTL Maintenance Zone의 Segment/Point 범위와 PIOPoint·PointNumber·DetourPointNumber를 설정·저장하고, 재조회로 SegList·PointList 반영을 확인할 수 있다.
- **표시**: 민감정보, 사이트의존
- **주의**: [L2a-15] Safety ID 계정 정보는 타 사이트 배포 시 마스킹한다. Door·Beam Sensor 위치와 CPS별 수용 대수는 사이트별로 다르다. 그룹화하지 않으면 Failover 시 라인이 다운될 수 있다. RUN/DOWN/FAILOVER 상태를 읽는 것만은 L1이다. / [L2a-16] MTL 객체 선생성은 MXA본 7.7 'Layout에서 MTL(MTU) 객체를 만들면' 기준으로 OCS Layout 탭에서 한다.

- **L2a-15 Safety·CPS Interlock 영역**
  - 내용: Object > Safety에서는 권한 ID로 로그인한 뒤 Safety를 선택하고, Interlock 감지 시 Down할 Segment를 Segment List에 추가한다(Shift 중복선택, Shift+드래그). Info는 SafetyNumber / DeviceType / Name / Unuse / SegmentAreaList다. 범위는 보통 Beam Sensor에서 Beam Sensor까지이며, Safety ID로 로그인하지 않으면 Save 버튼이 보이지 않고 환경안전 허가가 필요하다. Object > CPS도 같은 구조로 Segment 범위를 잡고 GroupNumber(한 세트는 같은 수)를 지정해 저장하며, 상태는 RUN/DOWN/FAILOVER로 확인한다(이상하면 PlcTag 확인). 이벤트가 나면 범위 내 차량은 Interlock Stop Error, 범위 외 차량은 NoWayToDest가 되며 Order List > Step 탭에서 확인한다.
  - 할 수 있어야 하는 것: Safety 또는 CPS의 Interlock Down Segment 범위를 설정·변경하고, CPS GroupNumber를 지정해 저장한 뒤 상태값을 확인할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p46~48; RCP Program setup 가이드 p.35(5.8) 표29, p.38(5.11) 표32
- **L2a-16 Object>MTL 유지보수 존**
  - 내용: 먼저 OCS Layout>Run에서 MTL 객체를 생성한다(MXA본 7.7). 그다음 Object > MTL에서 해당 MTL을 선택하고, MTL Zone 영역에 들어갈 Segment List를 버튼으로 추가한다(버튼을 누른 뒤 Shift+마우스 드래그로 영역 설정). 이 항목에서 설정하는 값은 SegList·PointList(MTL Zone 영역), PIOPoint(차량이 MTL 진입 전 MTL과 PIO 하는 Point), PointNumber(MTL Point), DetourPointNumber(PIO 실패로 진입 실패 시 우회경로를 내릴 Point)다. 같은 화면의 MTLNumber·ScreenName·OnlineName(MCS 통신명)·Unuse·MTLType 읽기와 배출 가능 상태 5조건 판정은 L1-22에서 다룬다.
  - 할 수 있어야 하는 것: MTL Maintenance Zone의 Segment/Point 범위와 PIOPoint·PointNumber·DetourPointNumber를 설정·저장하고, 재조회로 SegList·PointList 반영을 확인할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p49

### L2a-08 Layout Run 객체 배치·수정

- **레벨**: L2  ·  **교육 방식**: 화면실습  ·  **탭**: Layout  ·  **Section / Module**: Map & Traffic Control / OCS Traffic Settings  ·  **범위**: Core  ·  **교육 일차**: 6
- **화면·도구**: 메뉴 탭 > Layout > Run / Check / Setting
- **할 수 있어야 하는 것**: Layout>Run에서 UI Object를 추가·정렬·UPDATE·DELETE하고, 수정 후 Layout>Check Message로 잘못된 설정을 찾아 수정할 수 있다.
- **표시**: 사이트의존, 추정해석, 근거약함
- **주의**: MXA본 11.1 Run 기준. RCPHMI 현상7의 9992~9999번 point 경고는 정답 미확정이라 채점하지 않고 사례집으로 보냄. Layout>MapLoad는 L3-c.

- **교육 내용**
  - 내용: Layout > Run에서 Object·Safety·Graphic을 배치하고 LEFT/TOP/WIDTH/HEIGHT/ANGLE과 좌·우·상하 정렬, 우클릭 Select로 크기를 맞춘 뒤 APPLY / UPDATE / DELETE한다. 수정 후 Layout > Check를 다시 실행해 Message로 잘못된 설정을 찾아 고친다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p106~108; 02. RCPHMI.txt 23~25행(현상 7)

## L2-b 프로그램·시스템 구조

### L2b-01 OCS 실행 단위·서버·네트워크 구성

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: 서버  ·  **Section / Module**: System Setup / Architecture  ·  **범위**: Core  ·  **교육 일차**: 1
- **화면·도구**: (프로그램 단위) Core.exe / MCS_IF.exe / PlcDriver.exe / RCPGT, Help>Version, SystemInfo / 네트워크 연결 > 속성, 서버 관리자 > 로컬 서버(NIC), RoseMirrorHA 구성도
- **할 수 있어야 하는 것**: ① 실행 단위 5요소를 나열하고, 각 단위의 통신 상대·프로토콜·담당 로그(CoreForm/MCSIF_Form/Secom/PLCDRIVERFORM)를 MCS→OCS→Vehicle/PLC 구성도 위에 그려 설명할 수 있다. ② AP/DB 서버별 설치 대상, LOCAL/HOST/Mirror/HeartBit 랜포트 용도, Rose 3망과 LocalVIP/HostVIP의 관계를 구성도로 그리고, '차량 통신만 안 됨 / 상위만 안 됨' 현상이 어느 망·포트에 해당하는지 짚을 수 있다.
- **표시**: 자료충돌, 사이트의존, 민감정보
- **주의**: [L2b-01] Secom은 로그분석 매뉴얼에만 로그 주체로 나오고, setup 가이드·설치 기준서의 실행 단위 4개(Core/MCS_IF/PlcDriver/RCPGT) 목록에는 없다(자료충돌). 5요소 구성은 MXA본 2.2 기준. 사이트 호스트명(STOTA20100)·차량 번호대(U.50~114)는 마스킹 대상이다. MCS_IF는 setup 가이드·설치 기준서에 자체 화면이 나와 MXA본 서술과 다르다 — 현장 MCS_IF 화면 유무 확인 필요(L1-20·L1-51과 같음). / [L2b-07] Active/Standby IP(192.168.5.111/112)와 대역은 마스킹 대상이다. 랜포트 번호 배정(1번 공장망, 2번 무선망 등)은 사이트별로 확인해야 한다.

- **L2b-01 OCS 실행 단위와 통신 상대**
  - 내용: OCS(RCP)는 CORE / RCP GT / PLC Driver / MCS_IF / DataBase로 구성된다. MXA본 2.2는 RCP GT 외 프로그램을 "사용자 Interface가 없고, 내부적으로 구동"되는 프로그램으로 적으며, 그 거동은 로그·Help>Version·SystemInfo로 간접 확인한다. 실행 경로는 D:\Program\Core, McsIF, PlcDrv, RCPGT\Local, RCPGT\Host다. 통신 상대는 다음과 같다. Core는 차량(TCP/IP, 무선 LAN)·DB를 상대하고 MabLoad 주체이며 Core-Event(CPU/RAM)·Core-TaskMgr 로그를 남긴다. MCS_IF는 MCS(HOST, HSMS/SECS), PlcDriver는 PLC Unit을 상대한다. Core↔MCS_IF는 WCF(Host Param 2.2 SendWcfMsgCount, 2.3 AutoClearWcfMsgFailCount)로 통신하고 Host 큐는 MSMQ를 전제로 한다(2.1 HostQWarningCount). 로그 생성 주체는 CoreForm(OHT↔OCS) / MCSIF_Form(HOST↔OCS) / Secom(SECS/HSMS 원문) / PLCDRIVERFORM(PLC↔OCS) 4개이고, OCS 기준 통신 방향으로 구분한다.
  - 할 수 있어야 하는 것: 실행 단위 5요소를 나열하고, 각 단위의 통신 상대·프로토콜·담당 로그(CoreForm/MCSIF_Form/Secom/PLCDRIVERFORM)를 MCS→OCS→Vehicle/PLC 구성도 위에 그려 설명할 수 있다.
  - 근거: \_MANUAL\_User Manual\_V01\_MXA.docx 2.2 프로그램 구성도; 01. RCP 최초설치 확인사항.txt 2~5행·12~24행; RCP Program setup 가이드 p.24~27, p.39 표33; OCS 설치 기준서 p.21~22 (2.9); RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 2; \_사양서\_ OHT PROTOCOL\_v01\_241022\_SW팀.pdf p.5 (1.1); OCS 사용자 매뉴얼\_v04\_210114.pdf p7 (2. H/W 구성); OCS Parameter 매뉴얼 p.13 (2.1~2.3)
- **L2b-07 서버·네트워크 망 구성**
  - 내용: 서버는 AP 서버(SSMS, RailDesignTool, XcomDriver, Program Config, MCS_IF System 등록)와 DB 서버(MSSQL Server 2016, DB 구축)로 나뉜다. 네트워크는 LOCAL(Vehicle·AP 대역)과 HOST(MCS IP)가 다른 랜포트를 쓰고, 서버 랜포트 4구는 Local / Host / Mirror / HeartBit 용도다. Rose 이중화는 Active·Standby 노드 간 Public / Heartbeat / Mirror 3망으로 분리되고, Data Replication은 Active→Standby로 흐른다. VIP는 LocalVIP·HostVIP 2개이며 nettime(시간동기화)은 LocalVIP로 설정한다.
  - 할 수 있어야 하는 것: AP/DB 서버별 설치 대상, LOCAL/HOST/Mirror/HeartBit 랜포트 용도, Rose 3망과 LocalVIP/HostVIP의 관계를 구성도로 그리고, '차량 통신만 안 됨 / 상위만 안 됨' 현상이 어느 망·포트에 해당하는지 짚을 수 있다.
  - 근거: OCS 설치 기준서 p.4~25 '대상' 필드, p.18 (2.6); RCP Program setup 가이드 p.8~9 (1.5, 1.6); \_MANUAL\_RoseMirrorHA\_운영가이드\_Windows\_\_v01\_20200316\_김연수.pdf p.4; 01. RCP 최초설치 확인사항.txt 34행, 41~42행

### L2b-02 Config·IIS·폴더 구성과 기동 실패 1차 확인

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: 서버  ·  **Section / Module**: System Setup / Architecture  ·  **범위**: Core  ·  **교육 일차**: 1
- **화면·도구**: IIS 관리자 > Default Web Site > 응용 프로그램 추가 / 127.0.0.1/rcpgt / Config.asp / Core.exe.config / PlcDriver.exe.config / MCS_IF.exe.config / Config.asp, SSMS(DB 목록), 탐색기 D:\Program
- **할 수 있어야 하는 것**: ① RCP UI가 IIS 위 웹앱이라는 구조를 설명하고, 'UI가 안 열린다/다른 PC에서만 안 열린다' 현상에서 IIS 찾아보기로 1차 확인한 뒤 IIS 기능 누락·응용 프로그램 등록·URL/도메인·App 2.0·Config.asp DB IP 중 확인 지점과 점검 순서를 지목할 수 있다. ② 프로세스별 config 파일 이름과 위치를 짚고, 'Core(또는 PlcDriver·MCS_IF)가 기동 직후 죽는다' 현상에서 해당 config의 DB IP/ID/PW 불일치를 1순위 확인 지점으로 지목할 수 있다. 서버 폴더·DB 7종의 배치도 설명할 수 있다.
- **표시**: 사이트의존, 민감정보, 추정해석
- **주의**: [L2b-02] 별칭(rcpgt)·경로는 사이트별로 확인해야 한다. Config.asp 안의 DB ID/PW는 마스킹 대상이다. .Net/IIS 설치 절차 자체는 AUX 설치 기준에서 다룬다. / [L2b-03] DB 7종 각각의 역할(Host=상위통신, Winlay=맵 등)은 이름만 보고 추정한 것이라 평가에서는 '7종 식별'까지만 묻는다. config 안의 ID/PW는 마스킹해야 하고, 드라이브·폴더 규칙은 사이트별로 확인해야 한다.

- **L2b-02 RCPGT 웹 UI 구조**
  - 내용: RCP UI(RCPGT)는 IIS의 Default Web Site에 응용 프로그램(별칭/경로)으로 등록된 웹 애플리케이션이다. 경로는 D:\Program\RCPGT\Local과 \Host 두 벌이고, 127.0.0.1/rcpgt(별칭)로 접속해 확인한다. 제어판>Windows 기능 켜기/끄기에서 '인터넷 정보 서비스'(+.Net Framework, 웹 관리도구)가 빠지면 RCPUI 실행 자체가 불가하다. Web Config(Config.asp)의 DB 접속 IP를 루프백으로 두면 서버 로컬에서만 열리고, DB Server IP를 넣어야 다른 PC에서 접속된다. 접속이 안 되면 1차로 IIS 관리의 응용프로그램 관리 탭에서 \*80(http) '찾아보기'를 누르거나 브라우저 주소창에 DB Server IP·접속 도메인을 입력해 확인하고, 그래도 안 되면 URL 오타 → IIS 등록 도메인 → App 2.0 지우기 → Config 정보 순서로 점검한다(실제 조치 수행은 L3/AUX 범위).
  - 할 수 있어야 하는 것: RCP UI가 IIS 위 웹앱이라는 구조를 설명하고, 'UI가 안 열린다/다른 PC에서만 안 열린다' 현상에서 IIS 찾아보기로 1차 확인한 뒤 IIS 기능 누락·응용 프로그램 등록·URL/도메인·App 2.0·Config.asp DB IP 중 확인 지점과 점검 순서를 지목할 수 있다.
  - 근거: RCP Program setup 가이드 p.18 (2.3 IIS Setting) 표6, p.27 (4.4) 표16·17; OCS 설치 기준서 p.12~16 (2.4); 01. RCP 최초설치 확인사항.txt 20~21행; RCP Program setup 가이드 p.28 (4.5 Web RCP UI 실행 확인) 표18, 본문 P267~272
- **L2b-03 Config 파일과 폴더·DB 배치**
  - 내용: 실행 단위와 설정 파일은 1:1이다: Core.exe.config(CORE) / PlcDriver.exe.config(PLC Driver) / MCS_IF.exe.config(MCS_IF) / Config.asp(RCPGT). 네 파일 모두 DB IP·SQL ID/P.W를 담고, 기본값은 루프백(127.0.0.1)이다. 이 값이 실제 DB 인스턴스와 맞지 않으면 해당 프로세스는 '실행 자체가 불가'하다. MCS_IF의 상위통신 cfg·SML 설정은 DB 접속 설정과 별개다. 배치 규칙은 D:\DataBase(aspnetdb .mdf/.ldf), D:\Program\{Backup, Core, McsIF, PlcDrv, RCPGT\Local, RCPGT\Host, UpdateFile\YYMMdd}, D:\UTIL이다. DB는 aspnetdb / Host / OrderList / RCP / Rundata / Winlay / WinlayUpdate 7종이다.
  - 할 수 있어야 하는 것: 프로세스별 config 파일 이름과 위치를 짚고, 'Core(또는 PlcDriver·MCS_IF)가 기동 직후 죽는다' 현상에서 해당 config의 DB IP/ID/PW 불일치를 1순위 확인 지점으로 지목할 수 있다. 서버 폴더·DB 7종의 배치도 설명할 수 있다.
  - 근거: RCP Program setup 가이드 p.24~26 (4.1~4.3) 표13~15; OCS 설치 기준서 p.21~22 (2.9); 01. RCP 최초설치 확인사항.txt 1행·12~24행; OCS Parameter 매뉴얼 p.10 (1.1, 1.2 백업 파일 목록); OCS 설치 기준서 p.26~29 (3장)

### L2b-03 기동 순서와 Core 상태 전이

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: System  ·  **Section / Module**: System Setup / Architecture  ·  **범위**: Core  ·  **교육 일차**: 1
- **화면·도구**: Core.exe / PlcDriver.exe / MCS_IF.exe, CORE WARMINGUP·RUNNING 상태 표시, System>Parameter>SystemParam 10.1~10.4, ErrorList
- **할 수 있어야 하는 것**: Core를 먼저 띄우는 규칙대로 기동을 재현하고, Core가 WARMINGUP에 머무는 상황에서 10.1~10.4 중 어느 조건이 전이를 막고 있는지, Unknown Vehicle Position 알람이 왜 떴는지를 파라미터 관계로 설명할 수 있다.
- **표시**: 사이트의존
- **주의**: 기동 순서는 2026-10-08 확정: Core 선기동만 요건. 10.3 '10초', 10.4 '50초'는 매뉴얼 예시값이다(사이트별 확인). 값 변경은 L3-a 범위다.

- **교육 내용**
  - 내용: 프로세스는 관리자 권한으로 Core.exe를 먼저 실행하고, PlcDriver.exe와 MCS_IF.exe는 그 뒤 어느 순서로 띄워도 된다(설치 기준서는 PlcDriver→MCS_IF, 단독 실행 매뉴얼은 MCS_IF→PlcDriver로 적혀 있으나 사이트 확인 결과 Core 선기동만 요건). Core는 CORE WARMINGUP에서 CORE RUNNING으로 전이하며, 조건은 SystemParam의 네 파라미터가 정한다. 10.1 SystemRunTimeoutSec 경과 후 위치 미상 차량 비율이 10.2 SystemRunVehiclePercent 미만이면 Run으로 넘어간다. 10.3 SystemRunWarminUpErrorVehicleTimeoutSec를 넘기면 ErrorList에 'Unknown Vehicle Position'이 뜬다. 10.4 SystemAutoRunTimeoutSec를 넘기면 위치 미상 차량이 있어도 자동으로 RUNNING이 된다(0=NotUse).
  - 근거: OCS 설치 기준서 p.31 (4장 절차 2); OCS Parameter 매뉴얼 p.43~45 (10.1~10.4)

### L2b-04 MCS_IF 구성 (cfg 경로·HSMS IP·XCom CfgSml·HostNetworkName)

- **레벨**: L2  ·  **교육 방식**: 현장점검  ·  **탭**: 서버  ·  **Section / Module**: Host Interface (HSMS) / MCS_IF Config  ·  **범위**: Core  ·  **교육 일차**: 7
- **화면·도구**: MCS_IF\\<사이트명>\\<사이트명>.cfg, MCS_IF.exe.config / MCS_IF > XCom CfgSml Manager (Name / Sys Type / Upload / Select), MCS_IF.exe.config (HostNetworkName), 네트워크 연결(Host NIC 이름)
- **할 수 있어야 하는 것**: ① 낯선 사이트에서 MCS_IF cfg 파일을 경로 규칙으로 찾아내고, 드라이버 HSMS IP(0.0.0.0/VIP)와 config의 DB 접속 IP를 구분해 각각 어떤 연결을 좌우하는지 설명할 수 있다. ② MCS_IF가 안 올라오거나 상위 연결이 안 될 때 확인할 구성 지점 3개(XCom CfgSml Manager의 Select=True, HostNetworkName 대소문자 일치, XCOM Driver 설치)를 지목하고 각각이 왜 연결을 막는지 설명할 수 있다.
- **표시**: 사이트의존, 민감정보, 자료충돌
- **주의**: [L2b-05] 검증자 missing(MCS_IF 상위 연결 설정)을 반영한 항목이다. cfg 폴더명과 VIP 값은 사이트별로 다르고 마스킹 대상이다. / [L2b-06] 검증자 missing 항목이다. Upload·등록 조작 자체는 L1 절차로 따로 뗄 수 있고, 본 항목은 구성 이해와 확인 지점 지목으로 한정한다. MCS_IF 프로그램 화면은 사용자 매뉴얼 3판에 없고 setup 가이드·설치 기준서에만 있다. MXA본 2.2(프로그램 구성도)는 "RCP GT를 제외한 프로그램들은 사용자 Interface가 없고, 내부적으로 구동되고 있는 프로그램"이라 적고 있어(MCS_IF 포함) 현장 MCS_IF 화면 유무를 확인해야 한다.

- **L2b-05 MCS_IF cfg 경로·HSMS IP**
  - 내용: MCS_IF의 HSMS 설정 cfg는 MCS_IF 폴더 안 사이트명 규칙(MCS_IF\\<사이트명>\\<사이트명>.cfg, 예: MCS_IF\MICRON\MICRON.cfg)을 따른다. 사이트마다 폴더명이 다르다. cfg의 HSMS IP에는 루프백(127.0.0.1)·Host IP·Virtual IP를 넣을 수 있고 0.0.0.0도 작동한다. 최초설치 확인사항 4번은 'MCSIF 드라이버 설정파일 IP : 0.0.0.0'(특정 NIC에 바인딩하지 않고 전 인터페이스에서 수신)을 점검 항목으로 둔다. 이 값은 MCS_IF.exe.config의 DB 접속 IP와 다른 항목이다.
  - 할 수 있어야 하는 것: 낯선 사이트에서 MCS_IF cfg 파일을 경로 규칙으로 찾아내고, 드라이버 HSMS IP(0.0.0.0/VIP)와 config의 DB 접속 IP를 구분해 각각 어떤 연결을 좌우하는지 설명할 수 있다.
  - 근거: OCS 설치 기준서 p.23 (2.9 절차 5); 01. RCP 최초설치 확인사항.txt 5행; RCP Program setup 가이드 p.25 (4.2)
- **L2b-06 XCom CfgSml·HostNetworkName**
  - 내용: MCS_IF와 MCS의 연결은 MCS_IF 실행 → XCom CfgSml Manager → Name·Sys Type 설정 + cfg·sml 파일 등록 → Upload → 등록 시스템 활성화 → Select가 True로 바뀌었는지 확인하는 순서로 구성된다. 참고 항목은 XCOM Driver 설치 여부이고, 관련 위협은 'MCS_IF 실행 실패'다. MCS_IF.exe.config의 HostNetworkName은 Host Network Card에 등록된 이름 그대로 넣어야 하며 대소문자를 구분한다. IP가 맞아도 이름 대소문자가 틀리면 상위 통신이 실패한다.
  - 할 수 있어야 하는 것: MCS_IF가 안 올라오거나 상위 연결이 안 될 때 확인할 구성 지점 3개(XCom CfgSml Manager의 Select=True, HostNetworkName 대소문자 일치, XCOM Driver 설치)를 지목하고 각각이 왜 연결을 막는지 설명할 수 있다.
  - 근거: OCS 설치 기준서 p.24~25 (2.10); OCS 설치 기준서 p.22 (2.9 절차 4)

### L2b-05 Rose 이중화 구조·FailOver 요청·자원 경고 체계

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: 서버  ·  **Section / Module**: Redundancy (Rose) / Rose Concept  ·  **범위**: Core  ·  **교육 일차**: 9
- **화면·도구**: RoseMirrorHA 콘솔 Resources(Virtual IP/Data/NT Service/File Shared/Agent), services.msc / System > Parameter > MCCSParam (UseFailOverRequest, FailOverFilePath, FailOverFileName, HostDisconnectTimeout) / System > Parameter > SystemParam (10.5~10.17), LogParam, ErrorList
- **할 수 있어야 하는 것**: ① Rose 리소스 5종과 Virtual IP 4요소의 역할을 설명하고, 절체 단위가 Group이라는 점과 매뉴얼명↔현장 서비스명 대응을 짚으며, 운영 서비스 장애가 Failover로 이어지는 조건(3600s 내 3회)을 설명할 수 있다. ② MCCSParam 4개 항목과 FailOver 트리거 3조건을 설명하고, '서버 자원 과부하나 상위 단절이 왜 절체로 이어졌는가'를 SystemParam 경고 Level3·HostDisconnectTimeout과 연결해 설명할 수 있다. ③ CPU/Memory 경고의 Level+SecTime 2단 구조와 알람명, HDDWarningSpaceGB의 동작을 설명하고, 해당 값이 SystemParam 10.5~10.17에 있음을 지목할 수 있다.
- **표시**: 사이트의존, 자료충돌, 버전차이, 민감정보
- **주의**: [L2b-08] 서비스명은 매뉴얼과 현장이 다르다(자료충돌/버전차이). Group명 IMS와 노드명 AGV03/AGV04는 역할명으로 치환해야 한다. 3600s/3회는 Default라 변경될 수 있다. 콘솔 조작은 L3-b 범위다. / [L2b-09] 검증자 missing 항목이다. MCCS 기준 서술이며, Rose 사이트에서 이 INI 요청이 어떻게 연동되는지는 자료에 없다. 값 변경과 실제 절체는 L3-b다. / [L2b-10] 검증자 overreach를 반영했다. 87/92/97·180초는 현장 캡처값이고 매뉴얼 예시는 80/85/90·100~120초, 최초설치 BASE는 70/80/90이다. 세 값 모두 '예시(사이트별 확인)'로 표기했다. LogParam은 Report 보존기간 항목과 겹칠 수 있다. 임계값 변경은 L3-a다.

- **L2b-08 Rose 리소스·Group·서비스**
  - 내용: RoseMirrorHA 리소스는 Virtual IP(Active IP / Alias / Virtual Mac Address / Replace IP), Data(Replication Data / Share Disk / Arbitral Disk, Arbitral Disk는 Split Brain 방지용 소유권 확인), NT Service, File Shared, Agent로 구성된다. 이 리소스들을 하나의 Group으로 묶으며 절체·기동·정지 단위는 Group이다(현장 콘솔: Group IMS, 노드 AGV03/AGV04). 서비스명은 매뉴얼의 MirrorService/MirrorHAService/MirrorMonitor와 현장 services.msc의 RoseCliService/RoseHAService/RoseMirrorService/RoseMonitorService가 다르다. NT Service 장애 시에는 reset timeout(Default 3600s) 안에서 3회 재시작을 시도한 뒤 Failover한다.
  - 할 수 있어야 하는 것: Rose 리소스 5종과 Virtual IP 4요소의 역할을 설명하고, 절체 단위가 Group이라는 점과 매뉴얼명↔현장 서비스명 대응을 짚으며, 운영 서비스 장애가 Failover로 이어지는 조건(3600s 내 3회)을 설명할 수 있다.
  - 근거: \_MANUAL\_RoseMirrorHA\_운영가이드\_Windows\_\_v01\_20200316\_김연수.pdf p.12~19, p.60; Server Independent Execution Manual\_240518.pptx 슬라이드 2, 4 내장 이미지
- **L2b-09 MCCSParam FailOver 요청 체계**
  - 내용: System>Parameter>MCCSParam은 RCP가 이중화 솔루션(MCCS, Mantech Continuous Cluster Server)에 FailOver를 요청하는 체계다. 4.1 UseFailOverRequest는 사용 여부이고, 트리거는 CPU Warning Level3, Memory Warning Level3, Host Disconnect 세 가지다. 4.2 FailOverFilePath는 요청 INI 파일 경로, 4.3 FailOverFileName은 파일명(확장자 포함, 예 FailOverReq.ini)이다. 4.4 HostDisconnectTimeout은 OCS↔MCS 끊김이 이 시간(초, 0=미사용) 이상 지속되면 FailOver를 요청하는 기준이다.
  - 할 수 있어야 하는 것: MCCSParam 4개 항목과 FailOver 트리거 3조건을 설명하고, '서버 자원 과부하나 상위 단절이 왜 절체로 이어졌는가'를 SystemParam 경고 Level3·HostDisconnectTimeout과 연결해 설명할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p31 (6) MCCSParam); OCS Parameter 매뉴얼 p.25 (4.1~4.4); \_MANUAL\_User Manual\_V01\_MXA.docx 용어 설명 MCCS
- **L2b-10 자원 경고 Parameter 구조**
  - 내용: SystemParam의 CPU 경고는 10.5~10.7 CPUWarnLevel1/2/3(%)와 10.8~10.10 CpuWarnLevel1~3SecTime(초)로, Memory 경고는 10.11~10.13 MemoryWarnLevel1~3와 10.14~10.16 SecTime으로 이루어진다. 사용률이 Level을 넘은 상태가 SecTime 이상 지속되면 ErrorList에 'CPU Warning Level1/2/3' / 'MEMORY Warning Level1/2/3'이 뜬다(SecTime 0=미사용). 10.17 HDDWarningSpaceGB(0=미사용)는 서버 HDD의 남은 용량이 설정값(GB) 이하이면 알람을 띄운다. 값은 예시이므로 사이트별로 확인한다: Parameter 매뉴얼은 80/85/90%·100/110/120초·HDD 50GB, 현장 캡처는 87/92/97%·180초·HDD 5GB, 최초설치 BASE는 70/80/90이다.
  - 할 수 있어야 하는 것: CPU/Memory 경고의 Level+SecTime 2단 구조와 알람명, HDDWarningSpaceGB의 동작을 설명하고, 해당 값이 SystemParam 10.5~10.17에 있음을 지목할 수 있다.
  - 근거: OCS Parameter 매뉴얼 p.45~49 (10.5~10.17); CPU\_RAM\_HDD 점검 메뉴얼\_20220607.pdf p.4~7, p.9; 01. RCP 최초설치 확인사항.txt 48~52행; DB 점검 메뉴얼\_20220607.pdf p.4, p.11

### L2b-06 차량 통신 구조·OHT 전문 (CMD·STATUS)

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: System  ·  **Section / Module**: Vehicle Interface / OHT Protocol  ·  **범위**: Core  ·  **교육 일차**: 8
- **화면·도구**: System > Comm Group, System > Parameter > SocketParam 8.1~8.3, Report > Comm History / OHT PROTOCOL 사양서, CoreForm Comm 로그 [S:11]/[S:2A]/[S:12] / OHT PROTOCOL 사양서, CoreForm Comm 로그 S=, System > Vehicle IO Tag, Object > Vehicle > Set > TemporaryParam > IoGroupNumber
- **할 수 있어야 하는 것**: ① Comm Group 5개 필드가 통신 경로(AP>Bridge>Vehicle PLC)의 어디를 정하는지 설명하고, Polling/Event 혼합 방식·주기 파라미터 3종의 차이를 짚으며, 차량 미인식·통신 불량 시 Comm Group 설정과 Comm History를 대조 지점으로 지목할 수 있다. ② OHT 전문의 바이트 인덱스 구조와 방향별 [8]바이트 의미(subcmd/cmdresult) 차이, 주요 CMD 코드와 역방향(0xA0~0xA2) 구조를 설명할 수 있다. ③ STATUS TYPE 4종과 보고 시점, S= 상태 문자의 정상 순환, SDR/SD 차이, Vehicle IO Tag가 IO Index에 이름을 붙여 Object>Vehicle IO 탭에 연결되는 구조를 설명할 수 있다.
- **표시**: 사이트의존, 민감정보, 추정해석
- **주의**: [L2b-11] 검증자 missing(System>Comm Group)을 반영했다. 'ComGroup 중복→포트 중복으로 미인식'은 RCPHMI 메모의 추정이다. IP/Port는 마스킹 대상이다. Insert/SAVE 입력은 L1, CommErrHistory 대조로 원인을 특정하는 일과 Bridge Ping 구간 진단은 L3-a다. / [L2b-12] 실제 HEX 전문을 바이트 단위로 분해하는 판독은 L3-a(C328 계열)에서 평가한다. / [L2b-13] IO Tag 부분은 v04본 근거. STATUS·S= 부분은 프로토콜 사양서 근거라 영향 없음. S= 체계로 정체 지점을 판정하거나 IO 비트로 차량 이상을 판정하는 일은 L3-a.

- **L2b-11 차량 통신 구조·Comm Group**
  - 내용: System>Comm Group 필드는 CommGroupNumber(Vehicle Number와 일치 권장) / LimitTime / IpAddress / PortNumber / ProtocolType(Vehicle Type·현장별)이다. 경로는 AP > Bridge > Vehicle PLC다. RCP↔차량은 TCP/IP(차량=Server, RCP=Client)로 통신하고, 차량이 AUTO Mode일 때만 제어하며 Active-Active 다중 접속을 허용한다. 방식은 Polling(상태요청)+Event(도착·이적재 완료 즉시 Status)이고, 상태요청이 끊기면 차량이 통신을 재생성한다. 주기는 8.1 PollingInterval(S) / 8.2 CommandPollingInterval(G·M·L·U) / 8.3 ParkingPollingInterval이며 Report>Comm History의 Data Time으로 확인한다. Com Group이 같은 차량을 둘 등록하면 인식에 실패한다(포트 중복으로 추정).
  - 할 수 있어야 하는 것: Comm Group 5개 필드가 통신 경로(AP>Bridge>Vehicle PLC)의 어디를 정하는지 설명하고, Polling/Event 혼합 방식·주기 파라미터 3종의 차이를 짚으며, 차량 미인식·통신 불량 시 Comm Group 설정과 Comm History를 대조 지점으로 지목할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p22; RCP Program setup 가이드 p.30 표22·24; 02. RCPHMI.txt 9행(현상 2); \_사양서\_ OHT PROTOCOL\_v01\_241022\_SW팀.pdf p.6 (1.2, 1.3); OCS Parameter 매뉴얼 p.38 (8.1~8.3)
- **L2b-12 OHT 전문 헤더·CMD 코드**
  - 내용: RCP→차량 전문은 '>'(0x3E), res[1], uid[2], sz[1], vehicle[2], cmd[1], subcmd[1], param[n] 구조다. 차량→RCP 전문은 '\<'(0x3C)로 시작하고 [8]이 cmdresult다(0x00 Success / 0x01~0x2F Defined Error / 0x30~0x9F User Defined Error). CMD 코드는 0x01/0x02 상태요청·응답, 0x11 이동, 0x12 경로변경, 0x13/0x14 PAUSE/RESUME, 0x15 CYCLESTOP, 0x17/0x18 인터락/해제, 0x21/0x22 From/To, 0x2A 목적지 이후 추가이동(Comm 로그 [S:2A] MOVE-M), 0x80 SubCommand(CMD 0x01=JCR 진입 1회성)다. 같은 번호라도 방향에 따라 요청/응답 의미가 바뀐다. 0xA0 MoveRequest와 0xA1/0xA2 점유 요청·해제는 차량이 먼저 올리고 RCP가 Reply한다.
  - 할 수 있어야 하는 것: OHT 전문의 바이트 인덱스 구조와 방향별 [8]바이트 의미(subcmd/cmdresult) 차이, 주요 CMD 코드와 역방향(0xA0~0xA2) 구조를 설명할 수 있다.
  - 근거: \_사양서\_ OHT PROTOCOL\_v01\_241022\_SW팀.pdf p.7~8, p.10, p.23, p.28, p.2 Revision; RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 6
- **L2b-13 STATUS 메시지·S= 상태·IO**
  - 내용: STATUS 응답의 TY[1]는 0x01 위치·Status / 0x02 CST 정보 / 0x03 IO 정보 / 0x04 Version이다. 보고 시점은 RCP 요청, 목적지 도착, 이적재 완료, CST 정보 변경이다. S= 상태 문자는 정상 사이클 G(주행)→A(정위치)→L(적재중)→O(적재완료)→U(하역중)→N(하역완료)→G이고, 그 외 I/X/E/B·C/Q·W가 있다. TYPE 0x01의 [40]SDR은 0xA3 속도비율 지령의 결과(1~100%)이며 [26][27]SD(실제 속도)와 다르다. IO 24바이트(192개)는 System>Vehicle IO Tag의 IOName/GroupName으로 명칭을 붙이고, Object>Vehicle>Set>TemporaryParam>IoGroupNumber에 IO Tag의 VehicleNumber를 넣어 적용한다.
  - 할 수 있어야 하는 것: STATUS TYPE 4종과 보고 시점, S= 상태 문자의 정상 순환, SDR/SD 차이, Vehicle IO Tag가 IO Index에 이름을 붙여 Object>Vehicle IO 탭에 연결되는 구조를 설명할 수 있다.
  - 근거: \_사양서\_ OHT PROTOCOL\_v01\_241022\_SW팀.pdf p.12~13, p.8, p.2 Revision 3.3; RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 6; OCS 사용자 매뉴얼\_v04\_210114.pdf p27

### L2b-07 차량 지령 규칙·부가 장치 시나리오 (JCR·MTU·RFID·SCAN)

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: 프로토콜  ·  **Section / Module**: Vehicle Interface / Protocol Deep-dive (Extended)  ·  **범위**: Extended
- **화면·도구**: OHT PROTOCOL 사양서, System > Parameter (PIOParam 6.4/6.5, VehicleCommandParam 15.1~15.4, VehicleControlParam 16.10/16.11), Report > Comm History / OHT PROTOCOL 사양서 3장·4장, System > Parameter (TimeoutParam 12.19, VehicleControlParam 16.7/16.8)
- **할 수 있어야 하는 것**: ① 분기부 일괄 지령과 경로 재지령 원칙, PAUSE와 INTERLOCK STOP의 정지 위치·알람 차이, PreCommand 사용 여부에 따른 이적재 시퀀스 차이와 재전송 루프를 설명할 수 있다. ② JCR/JCP 통신 구조와 장비군별 명칭 차이, MTU 진입·RFID·SCAN·청소/진단 모듈 시나리오의 정상 메시지 흐름을 설명하고, 자기 사이트에 어느 시나리오가 적용되는지 구분할 수 있다.
- **표시**: 사이트의존
- **주의**: [L2b-14] PreCommand·ChangeRoute 사용 여부는 사이트별로 다르다. Nack/NextBranchPoint 변화를 로그에서 판독하는 일과 재전송 간격을 실측 대조하는 일은 L3-a다. / [L2b-15] 검증자 missing(JCPHeartBeat)을 반영했다. RFID·SCAN·MTU 케이스는 적용 사이트(MICRON/TM18)가 명시된 사이트별 시나리오다. 실패 케이스를 로그로 추적하는 일은 L3-a다.

- **L2b-14 주행·정지·이적재 지령 규칙**
  - 내용: RCP는 분기부를 포함해 목적지까지 한 번에 지령하고, 경로 변경은 다음 분기부부터 재지령한다. ROUTE-CHANGE(0x12)가 필요한 상황은 ①주행 중 목적지 변경 ②목적지 통과 후 추가 주행 ③경로 불가·우회 없음 세 가지다. 분기점에 너무 가까우면 Nack이 오고 NextBranchPoint가 바뀌며, 경로 불가 시에는 MovePauseCmd→ResumeCmd 순으로 처리한다. 16.11 UseChangeRoute를 켜면 위치정보 세 번째 Point(ChangeRoutePoint)가 재지령 지점이 된다. 정지 명령은 PAUSE(정위치 정지+경알람, CANCEL/RESUME 수용)와 INTERLOCK STOP 0x17(즉시 정지, 0x18 해제 시 TARGETPOINT로)이 다르다. 15.1 UseFromToPreCommand는 도착 전 P-From/P-To를 선행 송신하고(미사용 시 도착→정위치 확인→이적재), 6.4 CheckWorkingTimeAfterSendCommand / 6.5 SendFromToCommandInterval은 U·L 상태 미전환 시 재전송 루프를 돈다(Comm History로 확인).
  - 할 수 있어야 하는 것: 분기부 일괄 지령과 경로 재지령 원칙, PAUSE와 INTERLOCK STOP의 정지 위치·알람 차이, PreCommand 사용 여부에 따른 이적재 시퀀스 차이와 재전송 루프를 설명할 수 있다.
  - 근거: \_사양서\_ OHT PROTOCOL\_v01\_241022\_SW팀.pdf p.6 (1.4), p.18 (3), p.22~23 (7~10); OCS Parameter 매뉴얼 p.35~36 (6.4, 6.5), p.83~84 (15.1~15.4), p.87~88 (16.10, 16.11)
- **L2b-15 JCR·MTU·RFID·SCAN 부가 구조**
  - 내용: JCR↔OCS는 차량과 다른 포트로 UDP 통신하며, 상태가 바뀔 때와 주기(10초, 설정값)마다 보고한다. AUTODOOR OPEN/CLOSE도 JCR을 통한다. 전문 헤더는 '{'(0x7B, JCR→OCS) / '}'(0x7D, OCS→JCR)이고 CMD는 0x01/0x02/0x03이다. 12.19 JCPHeartBeatTimeoutSec는 JCP(OHT 분기제어, 타 장비는 MCP/JCR) 끊김을 알람으로 올린다. MTU 진입은 PIO PNT까지 이동 → 1001→1002 부분 점유(진입까지 해제금지) → MTU 상태 확인 → 진입명령 → PIO → 점유해제 순서이고, 진입불가 시 경알람→우회→재시도한다. RFID FromTo CASE#1(MICRON)/#2(TM18)와 SCAN START(0x2C)→STOP(0x2D)는 읽기 실패 시 UNKNOWN을 보고한다. 16.7 UseCleanModule / 16.8 UsePatrolModule은 차량 Bit(MS[1] 청소모듈 유무·ON/OFF)로 Call Disable하며 VID 401 CarrierCleanStatus와 연동된다.
  - 할 수 있어야 하는 것: JCR/JCP 통신 구조와 장비군별 명칭 차이, MTU 진입·RFID·SCAN·청소/진단 모듈 시나리오의 정상 메시지 흐름을 설명하고, 자기 사이트에 어느 시나리오가 적용되는지 구분할 수 있다.
  - 근거: \_사양서\_ OHT PROTOCOL\_v01\_241022\_SW팀.pdf p.29~31, p.34~40, p.8, p.13; OCS Parameter 매뉴얼 p.61 (12.19), p.86~87 (16.7, 16.8), p.90 (17.7, 17.8); 1\_SFA\_VHC\_BASIC\_SPEC\_V3.2.pdf p.25, p.28 (VID 401, 374)

### L2b-08 HSMS·SECS-II 구조·타임아웃

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: 프로토콜  ·  **Section / Module**: Host Interface (HSMS) / HSMS Structure & Sequence  ·  **범위**: Core  ·  **교육 일차**: 7
- **화면·도구**: SFA VHC BASIC/MESSAGE SPEC, Report > HsmsHistory, D:/XComLog / MCS_IF cfg (HSMS Parameter), SFA VHC BASIC SPEC 3.4
- **할 수 있어야 하는 것**: ① HSMS 프레임·헤더 필드와 Stream별 의미를 설명하고, 지원 S/F 목록에서 메시지 방향을 짚으며, S9F1~F7(스펙 불일치)과 S9F9(Transaction Timer time-out)를 구분해 설명할 수 있다. ② T3/T5/T6/T7/T8/LinkTest의 정의·통상값을 말하고, 각각이 걸렸을 때 '이벤트만 남는가, 연결이 끊기는가'를 구분해 설명할 수 있다.
- **표시**: 사이트의존
- **주의**: [L2b-16] S9F1~F9의 이름 풀이는 검증자 지적문에 실린 조사본 표기를 따랐고, 후보 C365에는 S/F 번호만 있다. '스펙 불일치인가 타임아웃인가'를 실제 로그로 판정하는 일은 L3-a다. / [L2b-17] 검증자 missing(T3~T8)을 반영했다. 실제 값은 사이트 cfg에서 확인해야 한다. 끊김 로그를 보고 어느 타임아웃인지 역추적하거나 값을 바꾸는 일은 L3-a다.

- **L2b-16 HSMS·SECS-II 메시지 구조**
  - 내용: MCS 인터페이스에서 OCS는 TSC/EQ, MCS는 Host이며 TCP/IP로 연결된다. HSMS 메시지는 Message length(0~3바이트) + Header(4~13: Session ID(Device ID) 2 / Header Byte2 / Byte3 / PType / SType / System Bytes 4) + Text로 이루어지고, PType·SType이 0이면 SECS-II 데이터 메시지다. 표준은 SEMI E5 / E30 / E37 / E37.1 / E82다. Stream은 1 상태, 2 제어·진단, 5 알람, 6 데이터수집, 9 System Errors로 나뉜다. 지원 S/F는 S1F1~F18, S2F13~F50, S5F1~F6, S6F11/12, S9F1/F3/F5/F7/F9이고, S2F29/30·S2F33~36·S6F15/16은 NO USED다. S9는 F1 Unrecognized Device ID / F3 Stream / F5 Function / F7 Illegal Data / F9 Transaction Timer time-out이다.
  - 할 수 있어야 하는 것: HSMS 프레임·헤더 필드와 Stream별 의미를 설명하고, 지원 S/F 목록에서 메시지 방향을 짚으며, S9F1~F7(스펙 불일치)과 S9F9(Transaction Timer time-out)를 구분해 설명할 수 있다.
  - 근거: 1\_SFA\_VHC\_BASIC\_SPEC\_V3.2.pdf p.5~7 (1.2, 3.1~3.3); 2\_SFA\_VHC\_MESSAGE\_SPEC\_V3.4.pdf p.5~8 (1.1, 1.3)
- **L2b-17 HSMS 타임아웃 T3~T8**
  - 내용: HSMS 타임아웃은 6종이다. T3 Reply(기본 45s, 1~120)는 Timeout Event만 발생시킨다. T5 Connection Separation(10s)은 재접속 간격이다. T6 Control Transaction(5s), T7 Connection Idle(10s), T8 Network Intercharacter(5s)는 Timeout Event 후 Separate.Req를 보내고 TCP/IP 연결을 끊는다. Link Test(0~240, 통상 10s, 0=미수행)도 실패하면 연결을 끊는다. 통신 기준은 TSC 측 Passive only, Maximum Message Size 4096, Maximum Concurrent Opened Transactions 1024이며, Host Name·TCP Port·IP는 TBD(사이트별)다.
  - 할 수 있어야 하는 것: T3/T5/T6/T7/T8/LinkTest의 정의·통상값을 말하고, 각각이 걸렸을 때 '이벤트만 남는가, 연결이 끊기는가'를 구분해 설명할 수 있다.
  - 근거: 1\_SFA\_VHC\_BASIC\_SPEC\_V3.2.pdf p.8 (3.4 Communication Standard Summary); RCP Program setup 가이드 p.47 표53, 본문 P587

### L2b-09 SECS 데이터 체계·SEMI 상태 모델

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: 프로토콜  ·  **Section / Module**: Host Interface (HSMS) / SECS Deep-dive (Extended)  ·  **범위**: Extended
- **화면·도구**: SFA VHC BASIC SPEC 5~6장, RCP Program setup 가이드 6.2 / SFA VHC BASIC SPEC 4장
- **할 수 있어야 하는 것**: ① SVID/CEID/RPTID/VID의 관계를 설명하고 VID 번호 구간과 S1F3 세트를 짚을 수 있다. CEID 번호를 보면 해당 사이트 스펙(BASIC SPEC/현장 기준)을 먼저 확인한 뒤 이벤트 계통을 분류할 수 있다. ② TSC·Transfer Command·Vehicle 상태 모델의 상태와 전이 이벤트를 그리고, CANCEL과 ABORT가 적용되는 상태(NOT ACTIVE/ACTIVE)의 차이와 PAUSED 상태에서 명령이 Queue에만 쌓이는 이유를 설명할 수 있다.
- **표시**: 자료충돌, 사이트의존
- **주의**: [L2b-18] 검증자 overreach를 반영해 CEID 번호대를 두 자료로 나란히 적었다. 평가는 '번호대 암기'가 아니라 '현장 스펙 확인 후 분류'로 한다.

- **L2b-18 SVID·CEID·RPTID·VID 체계**
  - 내용: SVID는 상태 식별자, CEID는 수집 이벤트 식별자, RPTID는 SVID 묶음이고, VID(ECV/SV)는 RPTID 안 Item 형식을 정의한다. Send가 있으면 반드시 Receive가 있어야 한다. VID 구간은 GEM 1~50 / SEM 51~200 / SFA 201~300 / Supplier 301~이다. S1F3 요청 세트는 10종(4, 53, 118, 91, 6, 73, 76, 254, 371, 7)이고, ControlState는 1~5(5=online/remote)다. CEID 번호대는 자료마다 다르다: BASIC SPEC은 1~3 Control / 51~57 TSC / 101~111 Transfer / 151~154·251 Carrier / 201~212 Vehicle / 260·261 Port / 503·504 UnitAlarm / 270 MonitoredVehicles이고, setup 가이드는 101~ TSC / 201~ Transfer / 301~ Carrier / 501~ Non-Transition / 601~ Vehicle / 701~ Unit Alarm / 801~ Unit Transfer다. 어느 쪽이든 현장 상위 프로그램 기준이다.
  - 할 수 있어야 하는 것: SVID/CEID/RPTID/VID의 관계를 설명하고 VID 번호 구간과 S1F3 세트를 짚을 수 있다. CEID 번호를 보면 해당 사이트 스펙(BASIC SPEC/현장 기준)을 먼저 확인한 뒤 이벤트 계통을 분류할 수 있다.
  - 근거: RCP Program setup 가이드 p.40~43 표36·37; 1\_SFA\_VHC\_BASIC\_SPEC\_V3.2.pdf p.23~26 (5.2.1), p.37~41 (6장); 3\_SFA\_VHC\_SCENARIO\_SPEC\_V3.5.pdf p.8
- **L2b-19 SEMI 상태 모델**
  - 내용: TSC State Model은 NONE→TSC INIT(TSCAutoInitiated)→PAUSED(TSCPaused)→AUTO(RESUME, TSCAutoCompleted), AUTO→PAUSING(TSCPauseInitiated, 이동 중 Carrier만 계속)→PAUSED(TSCPauseCompleted, 새 명령은 Queue만)로 전이한다. Transfer Command는 QUEUED→WAITING(TransferInitiated)→TRANSFERRING(Transferring)으로 진행하며, NOT ACTIVE에서는 CANCEL(CANCELING), ACTIVE에서는 ABORT(ABORTING)로 끊고, 실패하면 이전 substate로 복귀한다. Vehicle은 위치축(ENROUTE/PARKED/ACQUIRING/DEPOSITING), 할당축(ASSIGNED/NOT ASSIGNED), 설치축(INSTALLED/REMOVED) 3축을 동시에 갖는다. 그 밖에 Carrier, Unit Alarm(ALARM·MAINTE), Blocking, Monitored, Charge(AGV) 모델이 있다.
  - 할 수 있어야 하는 것: TSC·Transfer Command·Vehicle 상태 모델의 상태와 전이 이벤트를 그리고, CANCEL과 ABORT가 적용되는 상태(NOT ACTIVE/ACTIVE)의 차이와 PAUSED 상태에서 명령이 Queue에만 쌓이는 이유를 설명할 수 있다.
  - 근거: 1\_SFA\_VHC\_BASIC\_SPEC\_V3.2.pdf p.10~18 (4.2~4.10)

### L2b-10 상위 접속·원격명령·이벤트 시퀀스

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: 프로토콜  ·  **Section / Module**: Host Interface (HSMS) / HSMS Structure & Sequence  ·  **범위**: Core  ·  **교육 일차**: 7
- **화면·도구**: XcomPro Simulator (S1F13/S1F17/S2F41/S2F49), MCS_IF (MCMD 점등), Report > HsmsHistory / SFA VHC MESSAGE/SCENARIO SPEC, Report > HsmsHistory / SFA VHC SCENARIO/MESSAGE/BASIC SPEC, Report > HsmsHistory
- **할 수 있어야 하는 것**: ① 상위 Online 접속의 정상 메시지 순서를 TSCState(Paused/Auto)별로 재현하고, 각 단계(S1F13/F17, S2F41 RESUME, S2F49)가 일으키는 상태 전이와 오더 생성을 설명할 수 있다. ② S2F41 RCMD 8종과 S2F49 TRANSFER의 파라미터 구조를 설명하고, 정상 반송·Buffer 반송·ABORT/CANCEL/PAUSE/RESUME의 S6F11 이벤트 순서를 기준선으로 재현할 수 있다. ③ Unit/Port 이벤트와 WaitIn/WaitOut, S5F5/F6, CstSize 코드가 각각 무엇을 MCS에 알리는지 설명하고, 해당 사이트 스펙에서 대응 CEID·RPTID를 찾아 짚을 수 있다.
- **표시**: 자료충돌, 사이트의존, 민감정보
- **주의**: [L2b-20] CEID 번호는 BASIC SPEC 기준이라 사이트 스펙과 충돌할 수 있다. EQPNAME 예시(A2LOHS01)는 마스킹 대상이다. Controller Down→Up 복구 시퀀스는 이 버킷 후보에 근거가 없어 L3 쪽에서 따로 세워야 한다. Simulator 조작은 L1, 끊긴 지점을 로그에서 찾는 일은 L3-a다. MCS_IF 프로그램 화면은 사용자 매뉴얼 3판에 없고 setup 가이드·설치 기준서에만 있다. MXA본 2.2(프로그램 구성도)는 "RCP GT를 제외한 프로그램들은 사용자 Interface가 없고, 내부적으로 구동되고 있는 프로그램"이라 적고 있어(MCS_IF 포함) 현장 MCS_IF 화면 유무를 확인해야 한다. / [L2b-21] CEID 번호는 BASIC SPEC 기준이다(현장 스펙과 충돌 가능). 포트 ID 형식도 사이트별로 다르다. HCACK=0x02 중복 거부나 지령 오류를 실제 로그로 판정하는 일은 L3-a다. / [L2b-22] CEID 번호대는 BASIC SPEC 기준이다. CstSize 코드 목록과 S5F6 예시 ALID(941/600 등)는 사이트값이다.

- **L2b-20 상위 접속 시퀀스**
  - 내용: OFFLINE→ONLINE 시퀀스(TSC=Paused)는 다음과 같다. Select.req → S1F13(MDLN 'MCS') / S1F14(MDLN 'RCP', ACK Binary 0=정상) → S1F17 / S1F18(ONLACK=0) → S6F11 OnlineRemote(3)·TSCAutoInitiated(54)·TSCPaused(56) → S2F31/32 시간 설정 → S1F3/4 VID 10종 → S2F41 RESUME(HCACK 0x04, 0x07=Already Auto) → TSCAutoCompleted(53). TSC가 이미 Auto이면 ONLACK=2가 오고, PAUSE(57→55)를 선행해 동기화한 뒤 RESUME한다. S1F2는 MDLN / SOFTREV / EQPNAME / MCMD(0 OFF-LINE, 1 ON-LINE REMOTE, 2 ON-LINE LOCAL)를 담는다. Simulator 검증에서는 S1F17로 MCMD REMOTE, S2F41 RESUME으로 TSC AUTO가 되고, S2F49로 오더가 생성된다.
  - 할 수 있어야 하는 것: 상위 Online 접속의 정상 메시지 순서를 TSCState(Paused/Auto)별로 재현하고, 각 단계(S1F13/F17, S2F41 RESUME, S2F49)가 일으키는 상태 전이와 오더 생성을 설명할 수 있다.
  - 근거: RCP Program setup 가이드 p.45~46 표40; 3\_SFA\_VHC\_SCENARIO\_SPEC\_V3.5.pdf p.7~10 (1.1, 1.2); 2\_SFA\_VHC\_MESSAGE\_SPEC\_V3.4.pdf p.9~10 (2.3 S1F2); OCS 설치 기준서 p.34, p.37~38 (4장 절차 8·9·14·15)
- **L2b-21 원격명령·반송 정상 이벤트**
  - 내용: S2F41 RCMD는 ABORT(COMMANDID, REPLACE) / CANCEL / PAUSE / RESUME(L[0]) / UPDATE(COMMANDID, CARRIERID, PRIORITY, DESTPORT, FINALLOCATION) / SCAN / INSTALL / REMOVE 8종이다. 반송 지령은 S2F49 TRANSFER로 내려오며 COMMANDINFO(COMMANDID / PRIORITY / REPLACE)와 TRANSFERINFO(CARRIERID / SOURCEPORT / DESTPORT / CASSETTE_SIZE / FINALLOCATION / CARRIERTYPE) 2블록으로 구성되고, 정상 응답은 S2F50 HCACK 0x04다. 정상 반송 이벤트 순서는 108 TransferInitiated → 204 Assigned → 201 Arrived → 111 Transferring → 202 / 153 / 203 → 205 → 201 → 206 / 154 / 207 → 210 Unassigned → 107 Completed다. Buffer 반송에는 152/151이 추가되고, ABORT는 103→101, CANCEL은 106→104, Buffer INSTALL/REMOVE는 151/152로 보고된다.
  - 할 수 있어야 하는 것: S2F41 RCMD 8종과 S2F49 TRANSFER의 파라미터 구조를 설명하고, 정상 반송·Buffer 반송·ABORT/CANCEL/PAUSE/RESUME의 S6F11 이벤트 순서를 기준선으로 재현할 수 있다.
  - 근거: 2\_SFA\_VHC\_MESSAGE\_SPEC\_V3.4.pdf p.26~36 (2.28, 2.30, 2.31); 1\_SFA\_VHC\_BASIC\_SPEC\_V3.2.pdf p.49~55 (8장); 3\_SFA\_VHC\_SCENARIO\_SPEC\_V3.5.pdf p.13~14, p.19~20, p.25~28
- **L2b-22 Unit·Port 이벤트와 알람 메시지**
  - 내용: VHC Unit Event에는 Vehicle Installed/Removed(208/209), PortInService/OutOfService(261/260), VehicleCannotCallSet/Clear(211/212), VehicleBlockingStarted/Ended(671/672), MonitoredVehicles(UnitID / CurrentDomain / NextDomain / AlarmID / AlarmText / CommunicationState / MainteState 7필드 주기 보고)가 있다. Manual Port는 Carrier WaitIn(158, RPTID 33) / WaitOut(159, RPTID 34)과 제거 시 CarrierRemoved(152)를 보고한다. S5F5(ALID 리스트, n=0이면 전체)와 S5F6(ALCD / ALID / ALTX)은 알람 목록 조회 메시지다. CstSize(VID 370) 코드는 0 Unknown, 2 Full, 3 Quarter 등이며 HCACK 49 / ResultCode 16과 연동된다.
  - 할 수 있어야 하는 것: Unit/Port 이벤트와 WaitIn/WaitOut, S5F5/F6, CstSize 코드가 각각 무엇을 MCS에 알리는지 설명하고, 해당 사이트 스펙에서 대응 CEID·RPTID를 찾아 짚을 수 있다.
  - 근거: 3\_SFA\_VHC\_SCENARIO\_SPEC\_V3.5.pdf p.20~22 (3.1~3.6), p.63 (16.1, 16.2); 1\_SFA\_VHC\_BASIC\_SPEC\_V3.2.pdf p.29 (VID 370), p.49 (7.3); 2\_SFA\_VHC\_MESSAGE\_SPEC\_V3.4.pdf p.38~40 (2.36, 2.37)

### L2b-11 Tag 등록·매핑·PlcTag 체계

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: System  ·  **Section / Module**: System Setup / Site Configuration  ·  **범위**: Core  ·  **교육 일차**: 3
- **화면·도구**: Object Tag, System > PLC Tag (OPEN TAG), System > ErrorTag, System > Parameter > StationControlParam 9.1 / System > PLC Tag, 260103_PlcTag_L30.xlsx, PlcTag 로그
- **할 수 있어야 하는 것**: ① Tag 3단 등록 순서와 4쌍 매핑 규칙을 설명하고, 설비 알람 하나가 Object→PlcTag→ErrorTag 중 어느 등록에 의존하는지 짚으며, Exist Sensor 태그 누락이 RCPSTATION 알람으로 이어지는 구조를 설명할 수 있다. ② PlcTag 14컬럼이 각각 무엇을 정하는지 설명하고, 로그의 태그명(예: STATION_765_ALARMID)에서 TagName·TagProperty를 갈라 값의 종류(번호/상태/문자열/비트)를 판단할 수 있다.
- **표시**: 자료충돌, 사이트의존, 추정해석
- **주의**: [L2b-23] Insert/OPEN TAG 조작 자체는 L1이다. / [L2b-24] 행 수와 분포는 이 사이트 파일 기준이다. DataTypeInfo=비트 오프셋 해석은 CPS1 주소를 추적해 귀납한 것이다(추정해석).

- **L2b-23 Tag 3단 등록·매핑 규칙**
  - 내용: PLC 정보를 시스템에 반영하려면 Object Tag → PLCTag → ErrorTag 순으로 등록한다. 매핑 4쌍은 Object:Item Name = PlcTag:TagName, Object:Item Number = PlcTag:TagNumber, PlcTag:Name = ErrorTag:ErrType, PlcTag:Value = ErrorTag:ErrEvent다. System>PLC Tag(Insert/SAVE/OPEN TAG)는 화면에 없는 PLC Driver의 입력 정의 테이블이다. 예를 들어 Station Exist Sensor는 TagName STATION / TagNumber=StationNumber / TagProperty EXISTSENSOR로 등록하고(Buffer Type Station), 9.1 InstallRemoveReportWaitTimeSec 안에 값이 안 바뀌면 RCPSTATION 알람(CST Install, Remove Time Out)이 뜬다.
  - 할 수 있어야 하는 것: Tag 3단 등록 순서와 4쌍 매핑 규칙을 설명하고, 설비 알람 하나가 Object→PlcTag→ErrorTag 중 어느 등록에 의존하는지 짚으며, Exist Sensor 태그 누락이 RCPSTATION 알람으로 이어지는 구조를 설명할 수 있다.
  - 근거: RCP Program setup 가이드 p.34 (5.7 Tag 등록) 본문 P326~336; OCS 사용자 매뉴얼\_v04\_210114.pdf p26; OCS Parameter 매뉴얼 p.42 (9.1)
- **L2b-24 PlcTag 파일 컬럼·분류 체계**
  - 내용: PlcTag 정의(예: 260103_PlcTag_L30.xlsx, 1,988행)는 TagName / TagNumber / TagProperty / Address / AddrType / DataType / DataTypeInfo / PlcGroupNumber / ReadWrite / Comment / Remark / Connection / ReadComplete / Value 14컬럼이다. TagName+TagProperty가 '어떤 설비의 어떤 항목', Address+AddrType+DataType+DataTypeInfo가 '어디서 몇 비트'를 정한다. TagName은 SYSTEM / STATION / CPS / MONITOR / SAFETY / MTL 6종이고, 본체는 설비 에러 비트(SYSTEM ERR 1,574개, 약 79%)다. TagProperty는 ERR / ST / ALARMID / EXIST / CSTID 등 14종이다. DataType은 BIT / INT / STR이며, DataTypeInfo는 BIT이면 워드 내 비트 오프셋(0~15), STR(CSTID)이면 20(문자열 길이)으로 해석된다.
  - 할 수 있어야 하는 것: PlcTag 14컬럼이 각각 무엇을 정하는지 설명하고, 로그의 태그명(예: STATION_765_ALARMID)에서 TagName·TagProperty를 갈라 값의 종류(번호/상태/문자열/비트)를 판단할 수 있다.
  - 근거: 260103\_PlcTag\_L30.xlsx 헤더·TagName/TagProperty/DataType 전수 집계; OCS 사용자 매뉴얼\_v04\_210114.docx 7.9 PLC Tag; RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 19, 21

### L2b-12 PLC 통신 구성·설비 태그 구조

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: Object  ·  **Section / Module**: System Setup / Site Configuration  ·  **범위**: Core  ·  **교육 일차**: 3
- **화면·도구**: Object > PLC, Object > Ping, System > Parameter > SystemParam 10.18/10.20/10.21, PlcGroup, File Log > PLC Tag Log / PlcCommLog / System > PLC Tag, Object > Station / CPS / MTL / Safety, PlcTag 로그, Window > OrderList Step 탭
- **할 수 있어야 하는 것**: ① Object>PLC 필드와 PlcGroup·물리 PLC 대응, PLC 데이터 동기화 주기, 반복 끊김만 알람으로 올리는 감시 구조를 설명하고, PLC 연동 확인 시 열어야 할 로그(PLC Tag Log/PlcCommLog)를 지목할 수 있다. ② STATION/CPS/MTL/SAFETY·MONITOR 태그의 속성과 주소 배치 규칙을 설명하고, MTL 투입/배출 판정 5개 값과 Safety 이벤트 시 범위 안팎 차량의 거동 차이를 설명할 수 있다.
- **표시**: 사이트의존, 민감정보, 추정해석
- **주의**: [L2b-25] PlcGroup↔설비 대응은 이 사이트 파일 기준이다. IP는 마스킹 대상이다. Layout editor 선등록은 L2-a이고 WaitConnect로 미연결 PLC를 판정하는 일은 L3-a다. / [L2b-26] 주소와 대수는 이 사이트(L30) 기준이다. Safety SegmentAreaList 편집은 L2-a, OrderList Step으로 가는 판단은 L2-c, 실측 비트로 MTL 투입 불가 원인을 특정하는 일은 L3-a다.

- **L2b-25 PLC 통신 구성과 감시**
  - 내용: Object>PLC에는 PlcName / PollingTime / IP / TcpPort / TcpPortRange(통신 실패 시 접속 포트) / VehicleNumber(FoolProof)를 등록하고, Object>Ping에는 Ping Unit Number / Name / IP Address를 등록한다. 둘 다 Layout editor에서 객체를 먼저 등록해야 한다. Melsec은 포트 2개 이상과 TcpPortRange가 필요하다. PlcGroupNumber 1~8은 물리 PLC에 대응하고(예: 1 CPS, 2 MTL, 3~6 OLUS1~4, 7~8 FireDoor), PlcCommLog의 'U. n'은 차량이 아니라 이 PLC 번호다. 10.18 PlcDataPollingTimeMSec는 동기화 주기이며 File Log>PLC Tag Log로 확인한다. 10.20 PlcConnectionEventCount / 10.21 PlcConnectionEventCheckTimeSec는 일정 시간 안에 반복된 끊김만 알람으로 올린다.
  - 할 수 있어야 하는 것: Object>PLC 필드와 PlcGroup·물리 PLC 대응, PLC 데이터 동기화 주기, 반복 끊김만 알람으로 올리는 감시 구조를 설명하고, PLC 연동 확인 시 열어야 할 로그(PLC Tag Log/PlcCommLog)를 지목할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p50~51; 01. RCP 최초설치 확인사항.txt 63~64행; RCP Program setup 가이드 p.30 표23; 260103\_PlcTag\_L30.xlsx PlcGroupNumber 집계; RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 21; OCS Parameter 매뉴얼 p.50 (10.18, 10.20, 10.21)
- **L2b-26 설비별 태그 주소·Safety 거동**
  - 내용: STATION 태그 8속성은 _ST(1 정상/3 알람) / _ALARMID / _CSTID / _EXIST / _USEUNUSE / _INOUT / _CSTSIZE / _FLOOR다. OLUS 컨베이어는 CV마다 주소가 50씩 증가하고(OLUS1_CV2 10101~10110), WRITE는 CST ID WRITE 16행뿐이다. CPS는 30대가 각각 ST 1개(addr 720~749)와 ERR 약 50비트(addr 714, 810~812, 4씩 증가)를 갖는다. MTL은 상태 6속성 ORDERMODE(1 AUTO/2 MANUAL/3 ERROR) / FLOOR / EXIST / TRACKMODE / AVAILABLE / STOPPER와 ERR 71비트로 구성된다. SAFETY·MONITOR는 MTL 라이트커튼(7604)과 방화도어 #1/#2(9000~9100)를 잡는다. Safety 이벤트가 발생하면 범위 안 차량은 RCP Interlock Stop Error, 범위 밖 차량은 진입 시 NoWayToDest로 멈춘다.
  - 할 수 있어야 하는 것: STATION/CPS/MTL/SAFETY·MONITOR 태그의 속성과 주소 배치 규칙을 설명하고, MTL 투입/배출 판정 5개 값과 Safety 이벤트 시 범위 안팎 차량의 거동 차이를 설명할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 19~20; 260103\_PlcTag\_L30.xlsx STATION/CPS/MTL/SAFETY/MONITOR 전수; OCS Parameter 매뉴얼 p.57 (12.9); OCS 사용자 매뉴얼\_v04\_210114.docx 8.5 Safety

### L2b-13 알람 분류 체계 (ErrType·ErrCode·ErrEvent)

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: Window  ·  **Section / Module**: Alarm & Troubleshooting / Alarm System  ·  **범위**: Core  ·  **교육 일차**: 8
- **화면·도구**: Window > AlarmList (Type/ERRCODE), System > ErrorTag, Report > ErrorHistory, 260103_ErrTag_L30.xlsx / ErrorDescription.xlsx / Window > AlarmList (ERRCODE/EVENT), Report > ErrorHistory, System > ErrorTag / PLC Tag, System > Parameter > VehicleEventParam 17.3~17.10, OrderControlParam 5.18
- **할 수 있어야 하는 것**: ① 알람의 Type만 보고 차량/설비/네트워크/서버 계통을 1차 분류할 수 있다. ErrCode 대역으로 계통을 좁히되 두 판의 대역이 다른 계열(SYSTEM·PING·PLCCOMM·STATIONALARM)은 사이트 System>ErrorTag 화면으로 확인하고, CPS·FireDoor·PING의 번호 환산 규칙을 설명할 수 있다. ② AlarmList의 ERRCODE와 EVENT 컬럼을 구분해 읽고, VEHICLE ErrEvent 대역으로 계통을 말하며, SYSTEM 알람에서 PlcTag 주소로 넘어가는 경로와 중/경알람 정의를 설명할 수 있다.
- **표시**: 사이트의존, 병기, 근거약함
- **주의**: [L2b-27] 코드 대역은 부록 A 대조표대로 260103_ErrTag_L30 / ErrorDescription 두 판을 병기한다. AP 대수(ErrTag 12 vs SNMP 목록 8)는 사이트별 확인. / [L2b-28] 코드 대역은 부록 A 대조표대로 260103_ErrTag_L30 / ErrorDescription 두 판을 병기한다. ErrCode/ErrEvent가 뒤바뀐 4건은 이 사이트 파일의 결함이다. E84 알람은 PIO 타이밍 차트가 없어 '명명 규칙 이해' 수준으로만 평가한다(근거약함).

- **L2b-27 ErrType 분류·ErrCode 대역**
  - 내용: ErrType(AlarmList의 Type, 즉 Error 발생 주체)은 SYSTEM / VEHICLE / PING / SYSTEMALARM / CPSDOWN / CPSFAILOVER / STATIONALARM / PLCCOMM / RCP / SAFETY / RCPSTATION / CPU / MEMORY / ORDER / RCPPLC / HOSTQ / HDD / SEGMENT / POINT / JCRCOMM / MCSIF 21종이다(ErrorDescription은 SYSTEMALARM·SAFETY가 없어 19종). 대역은 두 판을 병기한다(부록 A). 같은 대역: VEHICLE 1~720 / CPSDOWN 1000~1027 / CPSFAILOVER 1028~1055 / 9xxxx 서버·RCP 내부 / MCSIF 100001. 다른 대역(ErrTag / ErrorDescription): SYSTEM 3001~4574 / 3001~4500, PING 7001~7120 / 7001~7112, PLCCOMM 7500~7507 / 7500~7505, STATIONALARM 8105~8130 / 5000~5273, SYSTEMALARM 8071~8104 / 없음, SAFETY 9000~9003 / 없음. 하위 규칙으로 CPSDOWN은 코드-1000=CPS번호-1이고 28대까지만 정의돼 있다(PlcTag는 30대). FireDoor는 ErrEvent 801~/851~로 50 오프셋을 쓴다. PING은 OHT(채널1) / OHT Bridge(채널2) / HUB / AP로 구성된다.
  - 할 수 있어야 하는 것: 알람의 Type만 보고 차량/설비/네트워크/서버 계통을 1차 분류할 수 있다. ErrCode 대역으로 계통을 좁히되 두 판의 대역이 다른 계열(SYSTEM·PING·PLCCOMM·STATIONALARM)은 사이트 System>ErrorTag 화면으로 확인하고, CPS·FireDoor·PING의 번호 환산 규칙을 설명할 수 있다.
  - 근거: 260103\_ErrTag\_L30.xlsx ErrType·ErrCode 전수 집계; ErrorDescription.xlsx; OCS 사용자 매뉴얼\_v04\_210114.docx 12.2 AlarmList
- **L2b-28 ErrCode·ErrEvent와 알람 계통**
  - 내용: ERRCODE는 RCP에 등록된 번호이고 EVENT(ErrEvent)는 차량·설비가 보내는 번호다. 이 사이트 파일에서는 VEHICLE 4건(ErrEvent 1↔ErrCode 55, 3↔53, 53↔3, 55↔1)이 뒤바뀌어 있어, 어느 컬럼으로 조회했느냐에 따라 오판할 수 있다. VEHICLE ErrEvent 계통은 1~61 조향·센서·주행, 80~299 적재·서보·HW, 300~399 YMC 서보, 400~450 Regulator/ECO 전원, 500~720 E84 PIO(TD/TA/TC + ES·HO·GO·L_REQ·U_REQ + Improperly 등, 700번대 _Heavy)로 나뉜다. SYSTEM(ErrTag 3001~4574 / ErrorDescription 3001~4500)은 PlcTag ERR 비트의 1:1 사본이어서 ErrEvent=TagNumber로 PLC 주소까지 역추적한다. 17.3~17.10 Regulator / PIO / Patrol / EFU ErrorEventRangeMin/Max는 OCS가 차량 에러를 자동 분류하는 근거다. 중알람은 Status E 상태의 Error, 경알람은 G/A/I 상태의 Error다.
  - 할 수 있어야 하는 것: AlarmList의 ERRCODE와 EVENT 컬럼을 구분해 읽고, VEHICLE ErrEvent 대역으로 계통을 말하며, SYSTEM 알람에서 PlcTag 주소로 넘어가는 경로와 중/경알람 정의를 설명할 수 있다.
  - 근거: 260103\_ErrTag\_L30.xlsx VEHICLE·SYSTEM 행 대조; 260103\_PlcTag\_L30.xlsx TagProperty=ERR; ErrorDescription.xlsx E84 Description; OCS Parameter 매뉴얼 p.34 (5.18), p.89~91 (17.3~17.10)

### L2b-14 Parameter 체계·배차/주행 거동 Parameter

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: System  ·  **Section / Module**: Parameters / Parameter System  ·  **범위**: Core  ·  **교육 일차**: 4
- **화면·도구**: System > Parameter (Param Group / NAME / Value / SAVE), OCS Parameter 매뉴얼 / System > Parameter (OrderControlParam 5.5~5.12, priorityParam 7.2, TimeoutParam 12.8/12.9/12.13, SocketParam 8.3, BlockingParam PushWeight, TrafficParam 13.1), System > Cluster (EntranceLimit / MaxVehicleCount / MaxVehicleReleaseCount)
- **할 수 있어야 하는 것**: ① 현상(예: 상위 큐 적체, 합류부 정체, PLC 끊김)을 듣고 열어야 할 Parameter 그룹을 지목하고, 파라미터 기술의 '참고' 필드에서 선행조건·0=미사용 같은 전제를 읽어낼 수 있다. ② Order Weight 계산식과 HandOver·합류·Home/Parking 규칙을 설명하고, PushWeight 값에 따른 밀어내기 거리 차이, EntranceLimit 체크 상태의 의미(Cluster 과차량), UseBothWay의 적용 대상을 화면 값과 연결해 설명할 수 있다.
- **표시**: 근거약함, 사이트의존
- **주의**: [L2b-29] 그룹 목록은 사용자 매뉴얼 기준 16그룹(MXA본 6.10의 15그룹 + v04본 DBInterfaceParam). 현장 화면의 그룹 수로 대조한다. Parameter 매뉴얼 17범주는 항목 설명을 찾는 색인으로만 쓴다. OHT 점검 4종은 원자료에 이름만 있고 기능 설명은 조사자가 보충한 것이다(근거약함). Value 변경은 L3-a. / [L2b-30] Cluster 화면은 v04본·중문통합본 근거, EntranceLimit 필드 설명은 RCP_Parameter_Manual_v0.0.1 Cluster(Info) 근거(사용자 매뉴얼 3판의 Cluster Info에는 EntranceLimit 없음). 나머지 Parameter 설명은 OCS Parameter 매뉴얼 근거. PushWeight·UseBothWay 등의 값을 조정해 현상을 해결하는 일은 L3-a. PushWeight 미동작 건은 RCPHMI에 미해결로 남아 있다.

- **L2b-29 Parameter 그룹 체계·기술 포맷**
  - 내용: System>Parameter는 BlockingParam / DatabaseParam / DBInterfaceParam / HostParam / LogParam / MCCSParam / OrderControlParam / PIOParam / PriorityParam / SocketParam / StationControlParam / SystemParam / TimeoutParam / TrafficParam / UIParam / VehicleControlParam 16그룹이다(v04본 기준, MXA본 6.10은 DBInterfaceParam 없이 15그룹). Parameter 매뉴얼은 17범주(DataBase … TaskMgr / VehicleCommand / VehicleEvent)로 나눈다. 각 파라미터는 항목 / 내용 / 목적 / 사용예시 / 참고 5필드로 기술되며, '참고'(0=미사용, XX True 선행, Vehicle Protocol 확인 등)가 안전선이다. 최초설치 점검의 OHT 항목(ChangeRoute / PreCmd / FindPathExceptCase / TaskMgr 로그기록여부)도 이 체계 안에서 찾는다.
  - 할 수 있어야 하는 것: 현상(예: 상위 큐 적체, 합류부 정체, PLC 끊김)을 듣고 열어야 할 Parameter 그룹을 지목하고, 파라미터 기술의 '참고' 필드에서 선행조건·0=미사용 같은 전제를 읽어낼 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p28~36; OCS Parameter 매뉴얼 p.2~9 (목차), p.10~92 공통 포맷; 01. RCP 최초설치 확인사항.txt 54~58행
- **L2b-30 배차·주행 거동 Parameter**
  - 내용: Order Weight = Segment Travel Time + 경로 Penalty(TrafficParam) + Segment Add Weight + Priority Weight이고, 가장 낮은 Order를 먼저 할당한다(7.2 AdvantagePerPriority). HandOver에는 5.7 LimitSecTargetPointForHandOver / 5.8 LimitSecHandoverInError / 12.13 ErrorVehicleHandOverTimeoutSec가 관여하며 모두 From Order에만 적용된다. 합류 규칙은 5.9 emJoinRuleType(0 FIFO / 1 Priority)과 5.10 emOrderJoinRuleType(From / To / Move / Home)이고, 5.11 CheckOrderByStationWorkType은 5.12가 False일 때만 유효하다. Home·Parking 규칙은 5.5 SelectHomeInSameGroup / 5.6 SelectOtherHomePoint, 12.8/12.9 IdleVehicleWaitTimeout(InMTL), AutoParking(과차량 시 Tact 악화)이다. BlockingParam PushWeight는 전방 차량 밀어내기 시작 거리, Cluster EntranceLimit는 MaxVehicleCount 이상이면 자동 체크·MaxVehicleReleaseCount 이하면 해제되고, 13.1 UseBothWay는 AGV·MCT 같은 양방향 설비 전용이다.
  - 할 수 있어야 하는 것: Order Weight 계산식과 HandOver·합류·Home/Parking 규칙을 설명하고, PushWeight 값에 따른 밀어내기 거리 차이, EntranceLimit 체크 상태의 의미(Cluster 과차량), UseBothWay의 적용 대상을 화면 값과 연결해 설명할 수 있다.
  - 근거: OCS Parameter 매뉴얼 p.28~32 (5.5~5.12), p.37 (7.2), p.38 (8.3), p.56~58 (12.8, 12.9, 12.13), p.62 (13.1), p.88 (16.12); RCP\_Parameter\_Manual\_v0.0.1 BlockingParam > PushWeight, Cluster > EntranceLimit; 02. RCPHMI.txt 5~6행

### L2b-15 반송 경로·Station·PIO·Host 연동 규칙

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: System  ·  **Section / Module**: Station, Network & EQ (Extended) / Station & PIO Rules  ·  **범위**: Extended
- **화면·도구**: System > OrderGroup, System > AltTransfer / System > Parameter (StationControlParam 9.2/9.3, TimeoutParam 12.4~12.16, PIOParam 6.6, VehicleEventParam 17.11/17.12, HostParam 2.6~2.8, OrderControlParam 5.16/5.17), Station 설정(StrParm2)
- **할 수 있어야 하는 것**: ① 경유지 반송 구성(Station·TransferUnit 배치)을 보고 필요한 OrderGroup·AltTransfer 등록 수를 산정하고, '특정 경로만 반송 불가' 현상에서 AltTransfer 등록 누락을 확인 지점으로 지목할 수 있다. ② Station·Buffer·PIO·MTL 대기 규칙과 이중입고/공출고 처리 흐름, PreTransfer·PreHandOff·CarrierDestRequest 메시지 흐름을 설명하고, 각 규칙이 어느 Parameter 그룹에 있는지 지목할 수 있다.
- **표시**: 사이트의존, 근거약함, 추정해석, 자료충돌
- **주의**: [L2b-31] System>AltTransfer 화면은 사용자 매뉴얼 3판에 없고 setup 가이드 5.10(AltTransfer 등록 및 확인)에만 있다. v04본·MXA본에는 OrderControlParam의 HandleAltTransferOrder(AltPort Order Handling) 파라미터만 있다. 현장 화면 유무 확인 필요. 경유지 반송이 있는 사이트에만 해당. / [L2b-32] PreTransfer와 이중입고/공출고 보고는 사이트 SCENARIO SPEC에 따라 달라진다. 값 조정은 L3-a다.

- **L2b-31 AltTransfer·OrderGroup 등록 구조**
  - 내용: 중간 경유지가 있는 반송은 System>AltTransfer에 Transfer Unit과 Station을 포함한 모든 경로를 등록해야 하고, System>OrderGroup에서 전체 반송, 시작 포트>경유 버퍼, 경유 버퍼>목적지 포트를 확인한다. 예를 들어 1번 Station(1, 2)/TransferUnit 1과 2번 Station(2, 3, 4, 5)/TransferUnit 2 구성이면 OrderGroup 3개와 AltTransfer 10개가 필요하다. 하나라도 누락되면 그 경로의 반송이 불가하다.
  - 할 수 있어야 하는 것: 경유지 반송 구성(Station·TransferUnit 배치)을 보고 필요한 OrderGroup·AltTransfer 등록 수를 산정하고, '특정 경로만 반송 불가' 현상에서 AltTransfer 등록 누락을 확인 지점으로 지목할 수 있다.
  - 근거: RCP Program setup 가이드 p.37 (5.10 AltTransfer 등록 및 확인) 표31, 본문 P364~370
- **L2b-32 Station·PIO·Host 연동 규칙**
  - 내용: WaitIn은 Station이 CST를 받을 준비가 됐다는 보고, WaitOut은 내보낼 준비가 됐다는 보고다. 9.2 WaitInOutEventReverse는 이 보고를 Work Type과 반대로 내보내고, 12.4/12.5 Wait In/Out 송신 주기와 12.6 최초 지연이 함께 작동한다. 9.3 AutoCreateTransferTimeoutSec(Station StrParm2 옵션)는 대체 반송을 만들고, 12.11/12.12 WaitBufferInstall/RemoveTimeoutSec(TransferBuffer + Exist Tag 전제)는 Exist 값을 기다린다. 6.6 WaitTimeAfterPIOError는 같은 Port 재명령에 대비한 대기이고, 12.16 WaitLimitTimeoutSecInMTLPoint는 MTL PIO 대기 한계다. 17.11 EventNumDoubleStorage / 17.12 EventNumSourceEmpty가 설정되면 이중입고·공출고 때 명령을 삭제하고 MCS에 보고하며, 대체 반송은 MCS가 만든다. Host 연동은 2.6 UsePreTransferCommand(RCMD PRE_TRANSFER) / 2.7·2.8 SendPreHandOffTimeMSec, 5.16 DestRemainTime→CarrierDestRequest→Host Update(5.17 DestUpdateOnlyOnce=False일 때 유효)로 이루어진다.
  - 할 수 있어야 하는 것: Station·Buffer·PIO·MTL 대기 규칙과 이중입고/공출고 처리 흐름, PreTransfer·PreHandOff·CarrierDestRequest 메시지 흐름을 설명하고, 각 규칙이 어느 Parameter 그룹에 있는지 지목할 수 있다.
  - 근거: OCS Parameter 매뉴얼 p.16~17 (2.6~2.8), p.33 (5.16, 5.17), p.36 (6.6), p.42 (9.2, 9.3), p.55~60 (12.4~12.6, 12.11, 12.12, 12.16), p.91 (17.11, 17.12)

## L2-c 현상별 진입 경로

### L2c-01 OCS 로그 지도 (4갈래·CoreForm·MCSIF/PLC/Secom)

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: 로그파일  ·  **Section / Module**: Alarm & Troubleshooting / Log Map & Entry Points  ·  **범위**: Core  ·  **교육 일차**: 8
- **화면·도구**: File Log(RcpLogPath) / Report 탭 / Window>ErrorList·OrderList / D:\XComLog / CoreForm 로그 폴더 (Comm, CommT, ..., MsgSend) / MCSIF_Form / PLCDRIVERFORM / Secom 로그 폴더
- **할 수 있어야 하는 것**: ① 현상 5건(예: 차량 정지 진행 중, 어제 반송 거부, 상위 S1F17 미수신 등)을 듣고 4갈래(File Log / DB History / UI 실시간 / XCom 로그) 중 1차 진입 갈래와 그 물리 위치나 화면을 지목할 수 있다. ② CoreForm 로그 이름을 듣고 소속 군과 '이 로그를 여는 상황'을 말할 수 있다. 차량 문제의 1차 로그로 Comm을 지목하고, Test 로그는 운영 판단 근거에서 뺄 수 있다. ③ 상위·PLC 문제를 듣고 MCSIF_Form / PLCDRIVERFORM / Secom 중 열 로그를 지목할 수 있다. Secom 로그를 열기 전에 시각·SystemBytes를 먼저 특정하는 진입 순서를 말할 수 있다.
- **표시**: 사이트의존, 추정해석, 자료충돌
- **주의**: [L2c-01] RcpLogPath·XComLog 경로는 사이트 설치값. 4갈래 지도는 두 문서를 합쳐 만든 교육용 항목이다. / [L2c-02] Test 로그 'FromI=ToI인 케이스만 기록' 부분과 VehicleEvent 30번 연쇄 해제의 의미는 원자료에서 '추정'으로 표기돼 있다. 32종 체계는 로그분석 매뉴얼에만 있고, setup 가이드·설치 기준서의 실행 단위(Core/MCS_IF/PlcDriver/RCPGT)와 이름 체계가 맞지 않는다. C037/C040/C047은 판독 항목(L3-a)인데, 검증자가 지적한 '진입점 누락' 3종을 보완하려고 여는 상황만 여기에 연결했다. / [L2c-03] 용량은 Micron AATT 표본의 실측값이다. Secom은 로그분석 매뉴얼에만 나오고 setup 가이드·설치 기준서에는 실행 단위로 나오지 않는다(검증자 data_gap). 실제 프로그램 구성은 현장에서 확인해야 한다.

- **L2c-01 OCS 로그 4갈래 지도**
  - 내용: OCS 로그는 네 갈래로 흩어져 있다. ①File Log: RcpLogPath(예: D:\Program\Log, 사이트별 확인) 아래 Core 이벤트, Comm Log, Wcf Log, Wcf Exception Log, PLC Tag Log, SelectOrder Log. ②DB History: Report 탭의 Error/Transfer/Comm/Hsms/Move History, NackHistory, InOutHistory, PlayBack. ③UI 실시간: ErrorList, OrderList, Comm Event. ④XCom 로그: D:\XComLog. 현상을 들으면 이 네 갈래 중 어디부터 열지 먼저 고른다.
  - 할 수 있어야 하는 것: 현상 5건(예: 차량 정지 진행 중, 어제 반송 거부, 상위 S1F17 미수신 등)을 듣고 4갈래(File Log / DB History / UI 실시간 / XCom 로그) 중 1차 진입 갈래와 그 물리 위치나 화면을 지목할 수 있다.
  - 근거: OCS Parameter 매뉴얼 p.13, p.19, p.21~24, p.32, p.41, p.50, p.57, p.71, p.81; OCS 설치 기준서 p.32
- **L2c-02 CoreForm 22종 용도**
  - 내용: CoreForm 22종은 5개 군이다. 차량 통신(Comm, CommT, CommException), 반송 지시(Order, OrderNack, OrderFail, SelectOrder, HandOver), 주행·경로(MoveHistory, PntOccupy, Finder, TM, HomeChange, Test), 상태·감시(Event, Ping, Warning, VehicleEvent, PlcTag, UIException), Host 메시지(MsgRecv, MsgSend). 여는 상황: Comm은 '가장 중요한 로그'다. [R:01] 상태 전문(위치·속도·알람·작업번호), [S:11] MOVE / [S:2A] MOVE-M, [R:11] MOVE-REPLY가 남아 차량 문제의 시작점이 된다. HomeChange는 차량이 예상과 다른 곳에 대기할 때, VehicleEvent는 알람 등록/해제(DeleteAlarmDB = VEHICLE_n, RegistProcess)를 추적할 때, UIException은 UI·DB 연결 예외가 의심될 때 연다. Test(SamePath Index, FromI/ToI, Matrix)는 경로 매트릭스 검증용 출력이라 운영 판단 근거로 쓰지 않는다. 원문 필드 판독(HomeChanged2 A->B, VEHICLE_30 혼잡도 해석, 중문 예외 해독)은 L3-a에서 다룬다.
  - 할 수 있어야 하는 것: CoreForm 로그 이름을 듣고 소속 군과 '이 로그를 여는 상황'을 말할 수 있다. 차량 문제의 1차 로그로 Comm을 지목하고, Test 로그는 운영 판단 근거에서 뺄 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 3, 4, 13, 15, 18
- **L2c-03 MCSIF·PLC·Secom 로그와 용량**
  - 내용: MCSIF_Form 4종(MCSSystem, SecsMsgTransfer, WCFMsgTransfer, WCFMsgTransferXML), PLCDRIVERFORM 3종(ReadWrite, PlcCommLog, MsgTransfer), Secom 3종(SECS-II, SECS-I, SECOMDRIVER)이 있다. 일일 용량 감각: CoreForm 22종 2,546MB, MCSIF_Form 4종 288MB, Secom 3종 9,689MB, PLCDRIVERFORM 3종 24MB(사이트별 확인). 분석의 90%는 CoreForm에서 끝난다. Secom은 통째로 열 수 없다. CoreForm·MCSIF 쪽에서 시각과 SystemBytes를 먼저 특정한 뒤 그 구간만 연다.
  - 할 수 있어야 하는 것: 상위·PLC 문제를 듣고 MCSIF_Form / PLCDRIVERFORM / Secom 중 열 로그를 지목할 수 있다. Secom 로그를 열기 전에 시각·SystemBytes를 먼저 특정하는 진입 순서를 말할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 1, 2, 3

### L2c-02 증상별 로그 진입 순서·LogParam 로그 위치

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: 로그파일  ·  **Section / Module**: Alarm & Troubleshooting / Log Map & Entry Points  ·  **범위**: Core  ·  **교육 일차**: 8
- **화면·도구**: CoreForm / MCSIF_Form / PLCDRIVERFORM / Secom 로그 / System > Parameter > LogParam (RcpLogPath, LogTrafficData, LogRecvData, LogDebuggingData, LogPeriod\*)
- **할 수 있어야 하는 것**: ① 9개 증상 중 하나를 제시받으면 열어야 할 로그 3~4종을 순서대로 지목할 수 있다. ② 조사 대상 날짜가 주어지면 LogParam에서 RcpLogPath, 기록 스위치, 해당 LogPeriod\* 값을 읽어 File Log가 남아 있는 위치와 대응 Report의 조회 가능 여부를 판정할 수 있다.
- **표시**: 사이트의존
- **주의**: [L2c-05] 경로·보존일수는 사이트 설정값이다. 대응 Report는 MXA본 9장 기준(Move History 포함). 같은 내용이 Report 보존기간 모듈과 중복되지 않게 이 항목 하나로 묶었다.

- **L2c-04 증상별 로그 진입 순서 9종**
  - 내용: 증상별로 열 로그와 순서는 다음과 같다. 특정 차량이 안 움직임: Comm → PntOccupy → Order → Finder. 라인 전체 정체: MoveHistory → PntOccupy → VehicleEvent. 반송 지시가 안 나감: OrderNack → MCSSystem → SelectOrder. 작업이 계속 넘어감: HandOver → OrderFail → SelectOrder. 카세트 ID 오류: OrderNack → PlcTag → ReadWrite. Host 연동 문제: MsgSend → WCFMsgTransfer → SecsMsgTransfer → SECOMDRIVER. 무선 통신 불량: CommT → Ping → Warning. 장비(PLC) 이상: PlcTag → ReadWrite → PlcCommLog. 서버가 느림: Event → Warning → UIException.
  - 할 수 있어야 하는 것: 9개 증상 중 하나를 제시받으면 열어야 할 로그 3~4종을 순서대로 지목할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 26
- **L2c-05 LogParam 로그 위치·보존기간**
  - 내용: System>Parameter>LogParam에서 다음을 읽는다. 3.4 RcpLogPath(File Log 저장 경로, 예: D:\Program\Log)와 3.9 LogPeriodFileLog(Core 이벤트 File Log 보존 일수)는 세트로 본다. 기록 스위치는 LogTrafficData(Vehicle 상태값), LogRecvData(Order 관련), LogDebuggingData(Debugging용)다. DB 보존과 대응 Report: 3.10 LogPeriodPlayBack(PlayBack), 3.11 LogPeriodHistory(통합), 3.12 LogPeriodAlarmHistory → Report>Error History, 3.13 LogPeriodOrderHistory → Transfer History, 3.14 LogPeriodCommHistory → Comm History, 3.15 LogPeriodHsmsHistory → Hsms History, 3.16 LogPeriodMoveHistory → Move History. 설정한 기간이 지난 이력은 조회되지 않는다. 값을 바꾸는 것은 L3다.
  - 할 수 있어야 하는 것: 조사 대상 날짜가 주어지면 LogParam에서 RcpLogPath, 기록 스위치, 해당 LogPeriod\* 값을 읽어 File Log가 남아 있는 위치와 대응 Report의 조회 가능 여부를 판정할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p30~31; OCS Parameter 매뉴얼 p.19 (3.4), p.21~24 (3.9~3.16)

### L2c-03 Report 이력 질문 매핑·UIHistory 변경자 추적

- **레벨**: L2  ·  **교육 방식**: 화면실습  ·  **탭**: Report  ·  **Section / Module**: Alarm & Troubleshooting / Log Map & Entry Points  ·  **범위**: Core  ·  **교육 일차**: 8
- **화면·도구**: Report > InOutHistory / InformHistory / RunningHistory / HandOverHistory / CassetteHistory / PingHistory / UserHistory / CpuRamHistory / Report > UIHistory (MessageName 검색)
- **할 수 있어야 하는 것**: ① 운영 질문 8개를 듣고 답이 있는 Report 화면과 확인할 컬럼을 지목할 수 있다. ② '설정이 바뀐 뒤 문제가 생겼다'는 현상을 듣고 UIHistory에서 MessageName 검색어를 골라 변경 사용자·IP·시각을 짚어낼 수 있다.
- **표시**: 민감정보
- **주의**: [L2c-06] 검증자 fix10에 따라 화면 지목(L2-c)과 조회 조작(L1)을 나눴다. NackHistory는 L2c-08에서 따로 다룬다. / [L2c-07] 결과에 사용자 ID·IP가 나오므로 교재 캡처는 마스킹해야 한다.

- **L2c-06 Report 보조 이력 질문 매핑**
  - 내용: 질문별 Report 화면: 차량 Line In/Out·Call Enable/Disable이 언제, 왜 일어났나 → InOutHistory(Comment). 인수인계·특이사항 → InformHistory(Message, CONFIRM). 차량별 가동·에러·블록 시간 → RunningHistory(RunningDist/Time, ErrorTime·WorkTime·BlockTime·IdleTime, 1시간 단위). 재할당된 Order → HandOverHistory. CST Install/Remove 위치·시각 → CassetteHistory. Ping 상태·응답시간 → PingHistory(PingStatus·ReplyTime). 로그인 기록 → UserHistory(Login/Logout/AutoLogout). CPU·RAM 추이 → CpuRamHistory(Cpu Usage·Ram Usage). 조건 입력→SEARCH 조작 자체는 L1이다.
  - 할 수 있어야 하는 것: 운영 질문 8개를 듣고 답이 있는 Report 화면과 확인할 컬럼을 지목할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p62~74
- **L2c-07 UIHistory로 변경자 추적**
  - 내용: '누가, 언제, 무엇을 바꿨나'는 Report>UIHistory에서 찾는다. 대상은 Point/Segment Unuse, Vehicle Setting 같은 OCS UI 변경 이력이다. MessageName으로 검색하고, 예를 들어 특정 시간의 UnusePoint 위치는 MessageName에 'Unuse'로 검색한다. 결과 컬럼은 UserID, IP(UI 변경 사용자 IP), MessageName(Event Name, 클릭하면 상세), RegTime이다.
  - 할 수 있어야 하는 것: '설정이 바뀐 뒤 문제가 생겼다'는 현상을 듣고 UIHistory에서 MessageName 검색어를 골라 변경 사용자·IP·시각을 짚어낼 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p72

### L2c-04 상위 명령 거부·상위 통신 이력 진입점

- **레벨**: L2  ·  **교육 방식**: 화면실습  ·  **탭**: Report  ·  **Section / Module**: Alarm & Troubleshooting / Symptom Entry Points  ·  **범위**: Core  ·  **교육 일차**: 7
- **화면·도구**: Report > NackHistory / Parameter > OrderControl 5.14 PostOrderAbnormal / D:\XComLog / RCP UI > HSMS History / File Log > Wcf Log·Wcf Exception Log
- **할 수 있어야 하는 것**: ① MCS 명령 거부 현상에서 NackHistory를 1차 화면으로 지목하고, PostOrderAbnormal 값을 확인해 이력이 비어 있는 이유를 가를 수 있다. ② 상위 통신 문제를 듣고 XComLog 경로, HSMS History 화면, Wcf Log / Wcf Exception Log 중 열 곳과 찾을 문자열을 지목할 수 있다.
- **표시**: 사이트의존
- **주의**: [L2c-10] XComLog 경로는 설치값. HSMSHistory는 v04·중문·MXA 모두 존재(원본 확인).

- **L2c-08 MCS 명령 거부 NackHistory**
  - 내용: 상위(MCS) 명령이 거부됐거나 '반송 지시가 안 나감' 현상이면 UI>Report>NackHistory로 간다. 컬럼은 Order, NackCode, MESSAGE(거부 이유)다. 단, Parameter 5.14 PostOrderAbnormal이 True여야 Order AbnormalCase가 DB에 Nack 이력으로 남는다. 로그로 이어 볼 때는 OrderNack → MCSSystem → SelectOrder 순서로 연다.
  - 할 수 있어야 하는 것: MCS 명령 거부 현상에서 NackHistory를 1차 화면으로 지목하고, PostOrderAbnormal 값을 확인해 이력이 비어 있는 이유를 가를 수 있다.
  - 근거: OCS Parameter 매뉴얼 p.32 (5.14); OCS 사용자 매뉴얼\_v04\_210114.pdf p62~74 (NackHistory); RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 26
- **L2c-10 상위 통신 이력 진입 3갈래**
  - 내용: 상위 통신 패킷은 OCS File Log가 아니라 XCom 로그(D:\XComLog, 설치 시 MCS_IF cfg와 View->Configuration에서 경로 설정, VHC_SIMUL 폴더 사전 생성)에 남는다. S1F17(Request Online) 같은 메시지는 XcomLog에서 보거나, 같은 내용을 RCP UI의 HSMS History 화면에서 본다. WCF 전송은 File Log->Wcf Log(2.2 SendWcfMsgCount 전송 개수)에서 보고, 전송 실패 큐 정리는 File Log->Wcf Exception Log의 '[Info] Clear Host Send Queue, Increase SendFail' 문자열(2.3 AutoClearWcfMsgFailCount 동작)로 찾는다. 로그로 이어 볼 때는 MsgSend → WCFMsgTransfer → SecsMsgTransfer → SECOMDRIVER 순서로 연다.
  - 할 수 있어야 하는 것: 상위 통신 문제를 듣고 XComLog 경로, HSMS History 화면, Wcf Log / Wcf Exception Log 중 열 곳과 찾을 문자열을 지목할 수 있다.
  - 근거: RCP Program setup 가이드 p.39 표33, p.44 본문 P440; OCS 설치 기준서 p.32 (4장 절차 4), p.33 (절차 6); OCS Parameter 매뉴얼 p.13 (2.2, 2.3); RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 26

### L2c-05 서버 리소스·FailOver·DB Exception 진입점

- **레벨**: L2  ·  **교육 방식**: 화면실습  ·  **탭**: Report  ·  **Section / Module**: Alarm & Troubleshooting / Symptom Entry Points  ·  **범위**: Core  ·  **교육 일차**: 8
- **화면·도구**: Report > FailOverHistory (DATETIME/MODULE/COMMENT) / RoseMirrorHA Console > Log / System > Parameter > SystemParam / Report > CpuRamHistory / Core Event 로그 / D:\Program\Log\Core\\<날짜>\Exception (DB Exception LOG)
- **할 수 있어야 하는 것**: ① FailOver 또는 절체 이상 현상을 듣고 OCS 쪽(Report>FailOverHistory의 MODULE·COMMENT)과 Rose 쪽(Console>Log) 중 어디로 갈지 지목하고, MODULE 값으로 넘어간 프로그램을 짚을 수 있다. ② 92xxx~95xxx 서버 알람을 듣고 설비가 아니라 SystemParam 임계값, CpuRamHistory, Event 로그로 가야 함을 지목할 수 있다. ③ DB 이상이나 업데이트 후 이상 현상에서 날짜별 Exception 폴더를 지목하고, 반출·전달(에스컬레이션) 대상을 말할 수 있다.
- **표시**: 근거약함, 사이트의존, 자료충돌
- **주의**: [L2c-09] Report>FailOverHistory는 MXA본 9.19 기준. Rose Console Log는 '조회 영역이 있다'는 서술뿐이고 로그 경로·파일명은 자료에 없다. COMMENT의 서버명칭은 사이트마다 다르다. / [L2c-16] ErrorDescription은 Level3 행에도 CpuWarnLevel2/MemoryWarnLevel2로 적혀 있어 오기가 의심된다. 임계값은 Parameter 매뉴얼 예시(80/85/90)와 현장 캡처값(87/92/97)이 다르므로 교재에 확정값으로 쓰지 않는다(검증자 overreach 반영). / [L2c-20] 경로는 RcpLogPath 설정에 따라 바뀐다.

- **L2c-09 FailOver·절체 이상 진입점**
  - 내용: FailOver가 났으면 Report>FailOverHistory를 연다. DATETIME(FailOver 시각), MODULE(FailOver된 Program), COMMENT(서버명칭, Program 명칭, FailOver 원인, 결과 값)를 보고 Core, PLC Driver, MCS_IF 중 어느 프로그램이 넘어갔는지 짚는다. 이중화 절체·복제 동작 자체에 이상이 있으면 RoseMirrorHA Console의 Log 영역에서 Rose가 수행한 동작과 이벤트를 1차로 본다. MCCSParam과 대조해 원인을 확정하고 복구하는 일은 L3-b다.
  - 할 수 있어야 하는 것: FailOver 또는 절체 이상 현상을 듣고 OCS 쪽(Report>FailOverHistory의 MODULE·COMMENT)과 Rose 쪽(Console>Log) 중 어디로 갈지 지목하고, MODULE 값으로 넘어간 프로그램을 짚을 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p76; \_MANUAL\_RoseMirrorHA\_운영가이드\_Windows\_\_v01\_20200316\_김연수.pdf p.10
- **L2c-16 서버 리소스 알람 진입**
  - 내용: CPU 92001~92003(Warning Level1~3), MEMORY 93001~93003, HOSTQ 94001 Host_MSG_Send_Queue_Warning, HDD 95001 Insufficient_HDD_Disk_Space는 설비 알람이 아니라 서버 알람이다. 임계값은 System>Parameter>SystemParam의 CpuWarnLevel\*, MemoryWarnLevel\*에서 확인한다(값은 사이트별 확인). 추이는 Report>CpuRamHistory에서, 원문은 Core Event 로그(3초 주기 [CPU] [RAM] [DB] [HQ] [PQ])에서 본다. '서버가 느림' 로그 순서는 Event → Warning → UIException이다. 필드 판독과 정상치 비교(C026)는 L3-a다.
  - 할 수 있어야 하는 것: 92xxx~95xxx 서버 알람을 듣고 설비가 아니라 SystemParam 임계값, CpuRamHistory, Event 로그로 가야 함을 지목할 수 있다.
  - 근거: 260103\_ErrTag\_L30.xlsx CPU 92001~92003 / MEMORY 93001~93003 / HOSTQ 94001 / HDD 95001; ErrorDescription.xlsx 해당 행 Description; RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 8, 26
- **L2c-20 DB Exception 로그 진입**
  - 내용: DB 이상이 의심되거나 Program Update 뒤 비정상 여부를 판단해야 하면 D:\Program\Log\Core\\<해당날짜>\Exception에서 DB Exception LOG를 확인한다. 로그와 분석 내용은 반출해 담당 개발 S/W 엔지니어에게 전달한다. UI 쪽 DB 연결 예외는 CoreForm UIException 로그에 남는다. Exception 원문으로 원인을 특정하는 일은 L3-a다.
  - 할 수 있어야 하는 것: DB 이상이나 업데이트 후 이상 현상에서 날짜별 Exception 폴더를 지목하고, 반출·전달(에스컬레이션) 대상을 말할 수 있다.
  - 근거: DB 점검 메뉴얼\_20220607.pdf p.12; RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 18

### L2c-06 차량 통신 이상 진입 경로 (CommError·No Response·UVP)

- **레벨**: L2  ·  **교육 방식**: 화면실습  ·  **탭**: Report  ·  **Section / Module**: Alarm & Troubleshooting / Symptom Entry Points  ·  **범위**: Core  ·  **교육 일차**: 8
- **화면·도구**: Report > Comm History / Report > CommErrHistory / CommT·Ping·Warning 로그 / Window > ErrorList(AlarmList) / System > Parameter > SystemParam 10.1~10.4
- **할 수 있어야 하는 것**: ① 차량 통신 현상을 CommError와 No Response로 나누고, 진행 중이면 Comm History, 과거 구간 조회면 CommErrHistory, 원문이 필요하면 CommT 로그로 진입처를 지목할 수 있다. ② ErrorList의 알람 이름만으로 Unknown Vehicle Position과 CommError를 구분하고 각각의 진입 갈래(기동·위치 등록 vs 통신 경로)를 지목할 수 있다.
- **표시**: 병기
- **주의**: [L2c-11] 검증자 fix11③에 따라 CommErrHistory 집계와 구간 특정은 L3-a(C208)로 넘기고, 여기서는 화면 진입과 조회 조건만 다룬다. / [L2c-12] 코드 대역은 부록 A 대조표대로 260103_ErrTag_L30 / ErrorDescription 두 판을 병기한다. RCP 91001~91012는 두 판이 같다. 검증자 missing 2건('UVP vs CommError', WARMINGUP→RUNNING 파라미터)을 이 항목에 반영했다.

- **L2c-11 차량 통신 이상 진입 경로**
  - 내용: 8.5 CommErrTimeoutSec는 통신이 끊긴 뒤 설정 시간이 지나면 CommError를 띄우고, 8.6 CommRecvTimeoutSec는 차량 응답을 못 받으면 No Response 카운트를 올린다. 둘 다 Report>Comm History에서 확인한다(통신 끊김 시점 → 설정 시간 경과 후 CommError 발생). 과거 통신 에러의 발생과 해제는 Report>CommErrHistory에서 VehicleNumber/PointNumber/SegmentNumber로 조회하고 Point, Segment, ErrorSet(Set/CLEAR), DateTime을 본다. 로그로는 CommT → Ping → Warning 순서로 연다. Point/Segment별 반복 집계로 구간을 특정하는 일(C208)과 타임아웃 값을 조정하는 일은 L3-a다.
  - 할 수 있어야 하는 것: 차량 통신 현상을 CommError와 No Response로 나누고, 진행 중이면 Comm History, 과거 구간 조회면 CommErrHistory, 원문이 필요하면 CommT 로그로 진입처를 지목할 수 있다.
  - 근거: OCS Parameter 매뉴얼 p.39~40 (8.5~8.8); OCS 사용자 매뉴얼\_v04\_210114.docx 10.9 CommErrHistory; RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 26
- **L2c-12 UVP와 CommError 구분**
  - 내용: Unknown Vehicle Position(RCP 91001~91012 대역의 Unknown_Vehicle_Position, '등록된 포인트가 아닌 0, 8888 등')은 기동 시점부터 위치를 한 번도 받지 못한 차량에서 뜬다. 통신이 정상 연결된 뒤 끊기면 OCS가 기존 위치를 알고 있으므로 Unknown Vehicle Position 대신 CommError가 뜬다(10.3 참고). Unknown Vehicle Position은 기동 전이와 엮여 있다. 10.3 SystemRunWarminUpErrorVehicleTimeoutSec(예: 10) 초과 시 WARMINGUP 상태에서 ErrorList에 이 알람이 뜨고, 10.1 SystemRunTimeoutSec, 10.2 SystemRunVehiclePercent, 10.4 SystemAutoRunTimeoutSec(0=NotUse)가 Run 전환을 정한다. 따라서 UVP는 기동·위치 등록 쪽(Core 상태, 해당 차량 Comm [R:01])을, CommError는 통신 쪽(L2c-06 경로)을 본다.
  - 할 수 있어야 하는 것: ErrorList의 알람 이름만으로 Unknown Vehicle Position과 CommError를 구분하고 각각의 진입 갈래(기동·위치 등록 vs 통신 경로)를 지목할 수 있다.
  - 근거: OCS Parameter 매뉴얼 p.43~45 (10.1~10.4), p.44 (10.3 참고); ErrorDescription.xlsx RCP 7행 Description

### L2c-07 타임아웃 알람 대응 파라미터·진입처

- **레벨**: L2  ·  **교육 방식**: 화면실습  ·  **탭**: Window  ·  **Section / Module**: Alarm & Troubleshooting / Symptom Entry Points  ·  **범위**: Core  ·  **교육 일차**: 8
- **화면·도구**: Window > OrderList / ErrorList, System > Parameter > TimeoutParam 12.1·12.2·12.3·12.14·12.15 / Window > ErrorList / System > Parameter > TimeoutParam 12.17·12.19, JunctionParam / PntOccupy 로그
- **할 수 있어야 하는 것**: ① 4개 알람(LongStay / All Port Loading Fail / Unlocated Order is exist / Noway Timeout) 각각에 대해 대응 TimeoutParam 항목과 먼저 열 화면(OrderList·ErrorList·맵 Unuse)을 짝지을 수 있다. ② 상위 무명령 알람과 분기제어(JCP/JCR) 계열 알람을 듣고 대응 파라미터(12.17, 12.19, JunctionOccupyWaitTimeOutSec)와 진입처(상위 로그, PntOccupy)를 지목할 수 있다.
- **표시**: 사이트의존, 병기, 자료충돌, 추정해석, 근거약함
- **주의**: [L2c-13] 타임아웃 값은 사이트 설정이다. ErrorDescription의 Noway_Timeout 설명은 'Finding path 후 15초'인데 매뉴얼 예시는 20초다(자료충돌). ORDER 96002~96003은 두 판이 같다. PntOccupy 로그와 대조해 설정 문제인지 설비 문제인지 판정하는 일과 값 조정은 L3-a다. / [L2c-14] JCPHeartBeat 알람이 JCRCOMM 96101로 뜨는지는 자료에 명시가 없어 현장 확인이 필요하다. 96xxx 코드는 두 판이 같다. JunctionParam>JunctionOccupyWaitTimeOutSec은 ErrorDescription Description에만 있고 Parameter 매뉴얼 그룹 목록에는 없음.

- **L2c-13 차량·오더 타임아웃 알람 대응**
  - 내용: 차량·오더 쪽 타임아웃 알람은 파라미터와 확인 화면이 1:1로 대응한다(값은 매뉴얼 예시이며 사이트별로 확인). 'LongStay' ← TimeoutParam 12.1 LongStayTimeoutSec(명령 있는 차량의 무언정지, 예: 600) / 12.2 LongStayTimeoutSecInWorking(이적재 중, 예: 120). 확인 순서는 UI에서 무언정지 차량 → OrderList 진행 명령 → ErrorList LongStay. 'All Port Loading Fail' ← 12.3 LoadingFailTimeoutSec(CST 적재 중 명령 없음, 예: 30). OrderList에 해당 차량 명령이 없는지 확인한다(미아 CST). 'Unlocated Order is exist'(ORDER 96002) ← 12.14 UnAllocatedOrderTimeoutSec(예: 10, 0=사용 안함). OrderList에서 미할당 명령을 확인하고, 할당되면 알람이 자동 삭제된다. 'Noway Timeout Error' ← 12.15 NoWayVehicleTimeoutSec(예: 20, 0=사용 안함). OrderList Duration을 보고 맵의 Point/Segment Unuse를 의심한다(UIHistory에서 'Unuse' 검색과 연계).
  - 할 수 있어야 하는 것: 4개 알람(LongStay / All Port Loading Fail / Unlocated Order is exist / Noway Timeout) 각각에 대해 대응 TimeoutParam 항목과 먼저 열 화면(OrderList·ErrorList·맵 Unuse)을 짝지을 수 있다.
  - 근거: OCS Parameter 매뉴얼 p.53 (12.1), p.54 (12.2), p.55 (12.3), p.59 (12.14), p.60 (12.15); ErrorDescription.xlsx RCP 7행 / ORDER 96002 Description
- **L2c-14 상위·분기 타임아웃 알람 대응**
  - 내용: 'TransferCommand is not received' ← TimeoutParam 12.17 TransferCommandRecvTimeoutSec(예: 60, 0=사용 안함). OCS는 정상인데 상위가 명령을 내리지 않는 상황이므로 상위 쪽(XComLog / HSMS History / MsgRecv)으로 진입한다. Host 명령이 수신되면 알람이 리셋된다. JCP 연결 끊김 알람 ← 12.19 JCPHeartBeatTimeoutSec(설정 주기마다 JCP 상태 체크). JCP는 'OHT 분기제어 컨트롤러'이고 타 장비에서는 MCP, JCR로 부른다. SEGMENT 96009 / POINT 96010 ← Parameter>JunctionParam>JunctionOccupyWaitTimeOutSec(JCR에서 특정 Segment/Point 점유시간 초과)이므로 PntOccupy 로그로 간다. JCRCOMM 96101은 JCR 통신 응답 오류다.
  - 할 수 있어야 하는 것: 상위 무명령 알람과 분기제어(JCP/JCR) 계열 알람을 듣고 대응 파라미터(12.17, 12.19, JunctionOccupyWaitTimeOutSec)와 진입처(상위 로그, PntOccupy)를 지목할 수 있다.
  - 근거: OCS Parameter 매뉴얼 p.61 (12.17, 12.19); ErrorDescription.xlsx SEGMENT 96009 / POINT 96010 / JCRCOMM 96101 Description

### L2c-08 명령 후 무동작·기동 이상 진입점

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: System  ·  **Section / Module**: Alarm & Troubleshooting / Symptom Entry Points  ·  **범위**: Core  ·  **교육 일차**: 8
- **화면·도구**: Parameter > 12. Timeout Param 12.18 / 3. Log Param 3.3 LogDebuggingData / MasterStop 로그 / MCS_IF / CORE 상태 표시, Core-Event·Core-TaskMgr 로그, Windows 이벤트 로그
- **할 수 있어야 하는 것**: ① '명령은 있는데 차량이 안 움직임' 현상에서 MasterStop 로그를 지목하고, LogDebuggingData 값으로 로그가 있는지를 판정할 수 있다. ② '자동 운전이 안 걸린다' 현상에서 4단계 상태값(XCOM SELECTED / CORE RUNNING / MCMD REMOTE / TSC AUTO) 중 멈춘 단계를 짚고, 그 단계에 맞는 로그나 화면을 지목할 수 있다.
- **표시**: 근거약함, 자료충돌
- **주의**: [L2c-15] MasterStop 로그의 파일명과 저장 위치는 자료에 없다. / [L2c-19] 설치 기준서 절차는 XCom Simulator로 S1F17/S2F41을 보내는 시험 환경 기준이라 실 사이트에서는 MCS가 보낸다. Core-Event·Core-TaskMgr의 실제 파일 위치는 자료에 없다. 검증자 fix11①에 따라 L2-c로 배정했다. MCS_IF 프로그램 화면은 사용자 매뉴얼 3판에 없고 setup 가이드·설치 기준서에만 있다. MXA본 2.2(프로그램 구성도)는 "RCP GT를 제외한 프로그램들은 사용자 Interface가 없고, 내부적으로 구동되고 있는 프로그램"이라 적고 있어(MCS_IF 포함) 현장 MCS_IF 화면 유무를 확인해야 한다.

- **L2c-15 명령 후 무동작 MasterStop**
  - 내용: 차량이 명령을 받았는데 움직이지 않으면 MasterStop 로그로 간다. 12.18 HandleMasterStopWaitTimeoutSec 주기로 Vehicle의 MasterStop 상태('Vehicle의 상태 및 Command 유무 여부')를 확인하는데, 이 로그는 3.3 LogDebuggingData가 True일 때만 저장된다. 그래서 먼저 LogParam에서 LogDebuggingData 상태를 읽어 로그가 남아 있을지 판단한다. 함께 볼 로그 순서는 Comm → PntOccupy → Order → Finder다. 스위치를 켜는 것은 설정 변경이라 L3에 해당한다.
  - 할 수 있어야 하는 것: '명령은 있는데 차량이 안 움직임' 현상에서 MasterStop 로그를 지목하고, LogDebuggingData 값으로 로그가 있는지를 판정할 수 있다.
  - 근거: OCS Parameter 매뉴얼 p.61 (12.18); RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 26
- **L2c-19 기동 이상 단계 지목**
  - 내용: 설치나 재기동 후에는 ①Core·MCSIF·PLCDrv 3개 프로세스 실행 ②Core-Event 로그에 CPU/RAM 기록 ③Core-TaskMgr 로그 기록 ④Windows 이벤트 로그 특이사항 순서로 '떠 있음'과 '일하고 있음'을 가른다. 이어 상태 전이 4단계를 확인한다. Start XCom 후 MCS_IF→XCOM SELECTED와 CORE→CORE RUNNING, S1F17 수신 후 MCS_IF·CORE→MCMD REMOTE, S2F41(RESUME) 수신 후 MCS_IF·CORE→TSC AUTO. 멈춘 단계에 따라 진입처가 갈린다. CORE가 WARMINGUP에 머물면 SystemParam 10.1~10.4와 Unknown Vehicle Position을, XCOM SELECTED·MCMD REMOTE 단계면 XComLog/HSMS History를 본다.
  - 할 수 있어야 하는 것: '자동 운전이 안 걸린다' 현상에서 4단계 상태값(XCOM SELECTED / CORE RUNNING / MCMD REMOTE / TSC AUTO) 중 멈춘 단계를 짚고, 그 단계에 맞는 로그나 화면을 지목할 수 있다.
  - 근거: 01. RCP 최초설치 확인사항.txt 2~6행; OCS 설치 기준서 p.33~34 (4장 절차 7~9); OCS Parameter 매뉴얼 p.43~45 (10.1~10.4)

### L2c-09 설비·PLC 알람 진입점·원인 설명 찾기

- **레벨**: L2  ·  **교육 방식**: 화면실습  ·  **탭**: Object  ·  **Section / Module**: Alarm & Troubleshooting / Symptom Entry Points  ·  **범위**: Core  ·  **교육 일차**: 8
- **화면·도구**: Window > AlarmList / Object > PLC / PlcTag·ReadWrite·PlcCommLog 로그 / Window > AlarmList (ERRTEXT) / ErrorDescription.xlsx Description 컬럼
- **할 수 있어야 하는 것**: ① PLCCOMM 알람 코드를 보고 해당 PLC(PlcGroup)를 지목하고 Object>PLC 화면과 PLC 로그 순서로 진입할 수 있다. ② 알람 코드를 받고 ErrorDescription.xlsx에서 Description을 찾아내며, 설명이 비어 있는 계열(SYSTEM/STATIONALARM)은 다른 자료로 넘겨야 함을 지목할 수 있다.
- **표시**: 사이트의존, 병기
- **주의**: [L2c-17] 코드 대역은 부록 A 대조표대로 260103_ErrTag_L30 / ErrorDescription 두 판을 병기한다. PLC 8대 구성과 코드-그룹 대응은 AATT L30 사이트 값이다. 다른 사이트에서는 ErrTag·PlcTag로 다시 맞춰야 한다. / [L2c-18] 코드 대역은 부록 A 대조표대로 260103_ErrTag_L30 / ErrorDescription 두 판을 병기한다. Description 컬럼은 ErrorDescription에만 있으므로, ErrTag에만 있는 코드(SYSTEMALARM·SAFETY, PING 7113~7120 등)는 설명이 없다.

- **L2c-17 PLCCOMM 알람→PlcGroup**
  - 내용: ErrType=PLCCOMM은 ErrTag 기준 ErrCode 7500~7507 8행(ErrorDescription은 7500~7505 6행 — FireDoor 2행 없음)이고 전부 ErrorLevel 1(중알람)이다. 7500 CPS / 7501 MTL / 7502~7505 OLUS1~OLUS4 / 7506~7507 FireDoor1·FireDoor2 COMM Disconnected. 이 8개는 PlcTag의 PlcGroupNumber 1~8, 즉 같은 8개 PLC에 대응한다. 그래서 알람 코드만 보고 어느 PlcGroup의 태그가 멈췄는지 짚고 Object>PLC 화면으로 간다. 로그는 PlcTag → ReadWrite → PlcCommLog 순서로 연다.
  - 할 수 있어야 하는 것: PLCCOMM 알람 코드를 보고 해당 PLC(PlcGroup)를 지목하고 Object>PLC 화면과 PLC 로그 순서로 진입할 수 있다.
  - 근거: 260103\_ErrTag\_L30.xlsx PLCCOMM 8행(7500~7507); 260103\_PlcTag\_L30.xlsx PlcGroupNumber 1~8; RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 26
- **L2c-18 알람 원인 설명 찾기**
  - 내용: AlarmList(ERRTEXT)에 뜬 알람의 원인 설명은 ErrorDescription.xlsx의 Description 컬럼에서 찾는다. ErrTag와 같은 8컬럼에 Description이 붙은 파일로, 2,403행 중 441행만 채워져 있다(VEHICLE 428행 중 422행, RCP 7, CPU 3, MEMORY 3 등). 예: OCS_WRONGWAY_STOP = 'OCS에서 지령 내리는 path와 OHT의 path가 맞지않아 알람발생'. SYSTEM(PLC 설비 에러)과 STATIONALARM에는 Description이 없으므로 PLC/설비 담당 자료로 넘어가야 한다.
  - 할 수 있어야 하는 것: 알람 코드를 받고 ErrorDescription.xlsx에서 Description을 찾아내며, 설명이 비어 있는 계열(SYSTEM/STATIONALARM)은 다른 자료로 넘겨야 함을 지목할 수 있다.
  - 근거: ErrorDescription.xlsx 시트 AATT\_L30 Description 441행

## L3-a 로그 분석·처리

### L3a-01 Comm 로그 판독·오더 생애주기 재구성

- **레벨**: L3  ·  **교육 방식**: 로그실습  ·  **탭**: 로그파일  ·  **Section / Module**: Vehicle Interface / Comm Log Basics  ·  **범위**: Core  ·  **교육 일차**: 8
- **화면·도구**: CoreForm Comm 로그 [R:01] / Window>CommEvent / Report>CommHistory / CoreForm Comm 로그 (CP·DP·ST·TP·S·P 열)
- **할 수 있어야 하는 것**: ① Comm 로그 상태보고 원문 한 줄과 CommHistory Message 한 줄을 받아 E/S/JOB/CP/DP/TP/ST/SEG/B= 비트를 필드별로 해석하고, 차량이 인터락·PAUSE·에러 중 어느 상태인지 판정할 수 있다. ② 한 차량의 Comm 로그 시계열을 받아 오더 1건의 시작~종료를 재구성하고, 멈춘 단계와 원인 방향(배차/주행/이적재 PIO)을 특정할 수 있다.
- **표시**: 사이트의존, 근거약함, 자료충돌
- **주의**: [L3a-01] BP 미사용 근거(663,925건 전수 검사)는 이 사이트에만 해당하므로 타 사이트에서는 BP 사용 여부를 다시 확인해야 한다. MD=는 자료 설명이 한 줄뿐이라 근거약함. / [L3a-02] 자료충돌: 로그분석 매뉴얼은 'TP는 오더가 끝나면 0으로 빠진다'고 하고, OHT PROTOCOL 사양서는 'TargetPoint는 도착해도 유지되고 초기화 때만 0'이라고 한다. TP=0 판정 규칙은 현장 차량 프로토콜로 확인한 뒤 채점한다. 예시 로그 시각과 번호는 사이트 표본이다.

- **L3a-01 Comm 상태보고 필드 판독**
  - 내용: CoreForm Comm 로그 [R:01] 상태보고 한 줄을 고정 순서 E=(알람, 0=정상) → S=(주행 상태 G/A/L/O/U/N) → JOB=(작업번호) → 첫 대괄호 [CP, DP, BP(3번째, 이 사이트 미사용 항상 0), TP] → P=(속도)로 읽는다. 나머지 필드 의미: ST=(Station이 아니라 경로변경 분기, 재지령 가능한 마지막 지점), SEG=(현재 세그먼트), M=(A=Auto), D=(직전 바코드 이후 거리), N=/NP=(다음 명령/그 바코드), R=(화물 점유), B=(비트 01 정위치·02 에러·04 인터락·10 PAUSE), MD=(청소모듈). 같은 내용이 화면에서는 Window>CommEvent / Report>CommHistory Message '[CurPoint,DirectionPoint,ChangeRoutePoint,TargetPoint], M=, S=, E=, D=, Spd=, Ra=, BSt=, Cst=' 포맷으로 나오므로 둘을 대응시킨다.
  - 할 수 있어야 하는 것: Comm 로그 상태보고 원문 한 줄과 CommHistory Message 한 줄을 받아 E/S/JOB/CP/DP/TP/ST/SEG/B= 비트를 필드별로 해석하고, 차량이 인터락·PAUSE·에러 중 어느 상태인지 판정할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 4, 5; OCS 사용자 매뉴얼\_v04\_210114.pdf p68(CommHistory), p104(CommEvent)
- **L3a-02 오더 생애주기·정체 단계 판정**
  - 내용: JOB·TP·DP·ST 4개 값으로 오더 1건을 재구성한다(예: U.111 09:29:31~09:30:17, 오더 735129). 분기를 지날 때마다 DP·ST가 갱신되고, 남은 분기가 없으면 0이 되며, 도착하면 S가 G→A로 바뀐다. 이후 L→O를 거쳐 새 오더가 들어오면 4개 값이 다시 채워진다. 멈춘 차량은 마지막 줄 TP를 본다. TP=0이면 '지시 없음'(배차측)이고, TP≠0이면 '가는 중인데 못 감'(주행측)이다. 사이클 G→A→L→O→U→N 중 멈춘 단계가 고장 지점이고, 최우선 신호는 'S=G인데 P=0 지속'(지령은 받았으나 못 움직임)과 'S=L/U 정체'(PIO 미완료) 두 가지다.
  - 할 수 있어야 하는 것: 한 차량의 Comm 로그 시계열을 받아 오더 1건의 시작~종료를 재구성하고, 멈춘 단계와 원인 방향(배차/주행/이적재 PIO)을 특정할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 5, 6; \_사양서\_ OHT PROTOCOL\_v01\_241022\_SW팀.pdf p.13(TargetPoint 클리어 시점)

### L3a-02 OHT 전문(HEX) 판독·프로토콜 불일치 판정

- **레벨**: L3  ·  **교육 방식**: 로그실습  ·  **탭**: 프로토콜  ·  **Section / Module**: Vehicle Interface / Protocol Deep-dive (Extended)  ·  **범위**: Extended
- **화면·도구**: CoreForm Comm 로그 [S:xx]/[R:xx] (Packet 기록 시) / OHT PROTOCOL 사양서 / OHT PROTOCOL 사양서 TYPE 0x01/0x02 / Comm 로그 Packet / OHT PROTOCOL TYPE 0x04 / Comm Log / System>Parameter>8. Socket Param>8.10 StatusPacketCheckSize
- **할 수 있어야 하는 것**: ① OHT 명령 HEX 전문과 응답 전문을 바이트 단위로 분해해 명령 종류·경로·JobNumber를 읽고, 응답 코드 또는 응답 누락으로 명령 실패 원인을 판정할 수 있다. ② TYPE 0x01/0x02 상태 전문을 받아 AS 작업상태와 ST 비트 조합(OR)을 분해하고, 포인트 필드 변화로 차량 위치와 화물 ID를 판정할 수 있다. ③ Version 전문의 RES 값과 Comm Log의 'Invalid Message Size Received'를 근거로 특정 차량의 맵 업데이트 중단이나 프로토콜 불일치 원인을 특정할 수 있다.
- **표시**: 자료충돌, 버전차이
- **주의**: [L3a-04] TargetPoint 클리어 시점은 사양서(초기화 때만 0)와 로그분석 매뉴얼(오더 종료 시 0)이 서로 다르다(L3a-01 참조). / [L3a-05] StationMap(0xF3) 블록은 프로토콜 3.4.6 개정에서 추가되어 구버전 차량에는 없다.

- **L3a-03 명령 전문 분해·응답 판정**
  - 내용: 송신 [S:11]과 응답 [R:11] MOVE-REPLY를 짝지어 응답이 없으면 차량 미수신으로 판정한다. 응답 코드는 COOE / RESULT CMD CODE로 읽는다: 0x00 성공, 0x01 수행 불가, 0x02 UnknownHeader, 0x03 UnknownCMD, 0x04 차량번호 불일치, 0x05 Size 이상, 0x06 위치값 이상. 0x11 GOCOMMAND HEX는 바이트 단위로 분해한다(예: Sz=0x1B, Vehicle=0x0005, CMD=0x11, CNT=0x06, 1666=0x0682…1572=0x0624, NM[4]=JobNumber). 이때 Sz와 Cnt를 대조해 길이를 검증한다. 0x12 경로변경은 분기 이후 구간만 재지령하는지 확인한다(161 불가 시 121-171-240). 0x21 FROM / 0x22 TO는 [9][10]PNT·[11]VN·[12]EN·[16]~[19]NM으로 읽는다. 0x15 MOVE CANCEL을 받은 순간 TargetPoint가 '정지 가능 포인트'로 바뀌어 올라오는 것을 식별한다.
  - 할 수 있어야 하는 것: OHT 명령 HEX 전문과 응답 전문을 바이트 단위로 분해해 명령 종류·경로·JobNumber를 읽고, 응답 코드 또는 응답 누락으로 명령 실패 원인을 판정할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 6; \_사양서\_ OHT PROTOCOL\_v01\_241022\_SW팀.pdf p.9, p.11, p.16~22
- **L3a-04 상태 전문 TYPE 0x01/0x02 판독**
  - 내용: TYPE 0x01 전문을 인덱스별로 읽는다: [10][11]CP, [12][13]DP, [14][15]BP, [16][17]TP, [18]MD, [19]AS, [20]ST, [21]RS, [22][23]EC, [24][25]DT, [26][27]SD, [28]~[31]NM, [33]NAS, [34][35]NPT, [36][37]SP, [38][39]StopPoint, [40]SDR. AS 코드는 0x00 I, 0x01 G, 0x02 A, 0x03 L, 0x04 O, 0x05 U, 0x06 N, 0x07 X, 0x08 E, 0x09 B, 0x0A C, 0x0B Q, 0x0C W이다. ST는 비트 OR(0x01 정위치, 0x02 에러, 0x04 인터락정지, 0x08 충전중, 0x10 PAUSE)로 분해하며, 예를 들어 0x12는 에러+PAUSE이고 PAUSE(0x13)~RESUME(0x14) 사이에는 PAUSE 비트가 계속 ON이다. 예시표(10→240)로 분기 통과 후 DP·BP가 0으로 떨어지는 패턴을 추적한다. TYPE 0x02는 SL/SZ/ID로 읽고, ID만 ASCII이고 나머지는 BINARY이다.
  - 할 수 있어야 하는 것: TYPE 0x01/0x02 상태 전문을 받아 AS 작업상태와 ST 비트 조합(OR)을 분해하고, 포인트 필드 변화로 차량 위치와 화물 ID를 판정할 수 있다.
  - 근거: \_사양서\_ OHT PROTOCOL\_v01\_241022\_SW팀.pdf p.2(Revision 2.0), p.13, p.14, p.15, p.22
- **L3a-05 맵 업데이트 차단·프로토콜 불일치**
  - 내용: TYPE 0x04 Version 전문을 VERT 블록별로 읽는다(0xF1 Map, 0xF2 Program, 0xF3 StationMap). 블록마다 MAV/MIV/BDV/RVV/RES/SP가 붙는다. 버전정보는 최초 StatusRequest 응답, 맵업데이트 이후, OCS 요청 시에 올라온다. RES=0x01(FAIL)로 올라온 차량은 OCS가 더 이상 업데이트를 진행하지 않으므로, '이 차량만 맵 업데이트가 안 된다'의 원인으로 특정한다. 8.10 StatusPacketCheckSize가 켜져 있으면 Comm Log의 'Invalid Message Size Received, Type=[s]'를 차량측 프로토콜 버전 불일치로 판정한다.
  - 할 수 있어야 하는 것: Version 전문의 RES 값과 Comm Log의 'Invalid Message Size Received'를 근거로 특정 차량의 맵 업데이트 중단이나 프로토콜 불일치 원인을 특정할 수 있다.
  - 근거: \_사양서\_ OHT PROTOCOL\_v01\_241022\_SW팀.pdf p.15(TYPE 0x04 및 하단 주석); OCS Parameter 매뉴얼 p.41(8.10)

### L3a-03 합류부 점유 고착·홈 재배치 판독

- **레벨**: L3  ·  **교육 방식**: 로그실습  ·  **탭**: 로그파일  ·  **Section / Module**: Alarm & Troubleshooting / Log Analysis (Extended)  ·  **범위**: Extended
- **화면·도구**: CoreForm PntOccupy 로그 / OHT PROTOCOL 0xA1·0xA2·JCR 0x02·0x03 / CoreForm HomeChange 로그
- **할 수 있어야 하는 것**: ① PntOccupy 로그와 점유 요청/응답 전문으로 합류부 통과 순서를 재구성하고, 합류 대기가 정상 대기인지 점유 고착·Door 닫힘·정보 불일치인지 특정할 수 있다. ② HomeChange 로그로 차량이 그 위치에 대기하게 된 경위(대피·연쇄 재배치·가상 포인트)를 판정할 수 있다.
- **표시**: 추정해석, 사이트의존, 근거약함
- **주의**: [L3a-06] Deny 23,716/Confirm 10,723은 1개 사이트 1시간 표본이다. 점유 고착 해제 조치 절차는 어느 자료에도 없어(검증자 fix6), 조치 부분은 현장 인터뷰 산출물이 나와야 평가할 수 있다. 판정(고착 식별)까지만 채점한다. / [L3a-20] 검증자 missing 항목이다. 사유 코드 #n과 '1~2만대=가상 포인트'는 원자료상 추정이다. 가상 포인트 번호 대역은 사이트 맵에 따라 다르다.

- **L3a-06 합류부 점유 판독·고착 판정**
  - 내용: PntOccupy 원문 'UID=993B, \<\<-, U. 83, PNT=[1426,1293,1427], CMD=JCR-OCCU, TY=JCR, JCR=1030, DR=0'에서 UID(요청/응답 매칭), \<\<-(요청)/->>(응답), PNT=[SPNT,EPNT,APNT], CMD=JCR-OCCU/NONE-RELE, RESULT=Confirm/Deny/AlreadyConfirm을 읽는다. JCR 번호 하나로 필터해 통과 순서를 복원한다(U.81 Confirm → U.83 Deny 약 200ms 간격 재시도 → U.81 NONE-RELE → U.83 승인). Deny 반복 시간이 앞차 통과 시간과 같으면 정상이고, 해제 없이 Confirm이 지속되면 점유 고착이다. 프로토콜 측에서는 0xA1 TY(0x01 JCR/0x02 FireDoor/0x04 AutoDoor/0x05/0xFF), 응답 REP(0x01 승인, 0x11 동일차량 승인, 0x02 타차 점유, 0x21 DOOR 닫힘, 0xF1/0xF2 알 수 없는 바코드/차량, 0xE1~0xE3 정보없음·불일치), OPT=0x01(정선HW INTERLOCK 무시) 식별, 0xA2 해제 REP를 판독한다. REP 0x21이 나오면 JCR DOOR COMMAND 0x03(DRNM, 0x01 OpenReq)과 JCR STATUS TYPE 0x02 ST(0x01 Open/0x02 Close)를 이어 Door 개방 흐름을 추적한다.
  - 할 수 있어야 하는 것: PntOccupy 로그와 점유 요청/응답 전문으로 합류부 통과 순서를 재구성하고, 합류 대기가 정상 대기인지 점유 고착·Door 닫힘·정보 불일치인지 특정할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 9, 25; \_사양서\_ OHT PROTOCOL\_v01\_241022\_SW팀.pdf p.25~27, p.32~33
- **L3a-20 HomeChange 홈 재배치 판독**
  - 내용: HomeChange '09:29:49.760, [N. 0] U. 80, HomeChanged2 1291 -> 1431, CurPoint : 1291, CheckCurPnt : 0, ForEscape : 1 #4'에서 HomeChanged2 A->B(홈 포인트 변경), CurPoint(변경 시점 위치), ForEscape=1(대피 목적), #4/#-1(사유 코드)을 읽는다. 차량이 예상과 다른 곳에 대기할 때 연다. 초 단위로 연쇄 변경되는 것은 서로 비켜주는 정상 동작으로 판정한다. CurPoint가 21018·11153처럼 1~2만대이면 가상 포인트(라인아웃/대기구역)로 식별한다.
  - 할 수 있어야 하는 것: HomeChange 로그로 차량이 그 위치에 대기하게 된 경위(대피·연쇄 재배치·가상 포인트)를 판정할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 13

### L3a-04 통신 지연·단절 구간 특정 (CommT·Ping·CMD)

- **레벨**: L3  ·  **교육 방식**: 로그실습  ·  **탭**: 로그파일  ·  **Section / Module**: Vehicle Interface / Comm Log Basics  ·  **범위**: Core  ·  **교육 일차**: 8
- **화면·도구**: CoreForm CommT / Warning 로그 / Comm 말미 대괄호 / Report>CommErrHistory / PowerShell Select-String / CoreForm Ping 로그 / Window>PingList / Report>PingHistory / CMD(ping, tracert, telnet, netstat, arp, nbtstat) / CMD 진단 명령 세트
- **할 수 있어야 하는 것**: ① CommT·Warning·CommErrHistory를 집계·대조해 통신 지연의 원인이 서버측 부하인지, 특정 차량인지, 특정 무선 구간(AP)인지 특정할 수 있다. ② Ping 로그를 차량별 채널 1/2로 짝지어 PingList·PingHistory와 대조하고 '이중화만 깨짐'과 '통신 단절'을 판정해, 단절이면 CMD 구간 분리(L3a-04)로 넘기는 결정을 내릴 수 있다. ③ 여러 CMD 결과를 조합해 장애 구간(서버·AP·Bridge·차량 PLC·포트·IP 충돌)을 특정하고 조치·에스컬레이션 대상을 결정할 수 있다.
- **표시**: 추정해석, 사이트의존, 민감정보
- **주의**: [L3a-07] 검증자 overreach 지적 사항이다. PNT 편중을 음영 구간으로 보는 해석과 Reply/스레드 분리로 서버측을 판정하는 해석은 원자료상 '추정'이다. AP CPU 정상값과 Core 경고 44건/3일은 사이트 실측치다. AP 배치도가 없어 AP 번호까지 특정하지는 못한다. / [L3a-08] 검증자 missing 항목이다. IP 대역(10.1.0.NN/10.1.1.NN)은 이 사이트 규칙이라 배포본에서는 x.x.0.NN 형태로 마스킹하고 구조만 남긴다. '한쪽만 죽으면 이중화만 깨짐'은 원자료상 추정이다. 정상값 99.87%/14.1ms는 1시간 표본이다. ComGroup 중복 원인도 RCPHMI 메모의 추정이다. / [L3a-09] C253 주 버킷은 L2-b(경로 구조). 판정 시나리오는 자료에 표로 없음 — Case Bank 실습 설계 필요

- **L3a-07 통신 지연 서버/차량/무선 판정**
  - 내용: CommT '09:30:48.104, U. 51 TimeOut, M=A, S=G, PNT=1102'를 차량별·PNT별로 집계한다. PNT가 몰리는 구간은 전파 음영으로 의심하고(추정), Warning의 AP01~04_SNMP CPU 편차(예: 84%, 정상 예시 13~17%, 사이트별 확인) 및 Report>CommErrHistory의 ErrorSet Set/CLEAR를 Point/Segment별로 집계한 결과와 대조해 구간을 좁힌다. Warning은 Select-String -NotMatch '_SNMP'로 Core 경고 3종(ComThread Time Increased / ExecuteOrder Elapsed Time / Request timed out)만 남긴다. 'ComThread Time Increased... 3667ms, Reply=31ms, Step=StepComMgrRun->StepComMgrWaitRecvData'는 Reply가 정상이고 스레드만 지연된 것이므로 서버측으로 판정한다. 같은 시각 다수 차량에서 동시에 뜨면 서버측, 한 대만이면 그 차량 통신이다. Comm 말미 [처리시간ms, 통신주기ms]도 함께 대조한다.
  - 할 수 있어야 하는 것: CommT·Warning·CommErrHistory를 집계·대조해 통신 지연의 원인이 서버측 부하인지, 특정 차량인지, 특정 무선 구간(AP)인지 특정할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 4, 7, 17, 25; OCS 사용자 매뉴얼\_v04\_210114.pdf p69(CommErrHistory)
- **L3a-08 Ping 2채널 판독·단절 판정**
  - 내용: Ping 로그 '09:00:43.817, No.61, IP=10.1.0.61, Byte=32, Time=14, Status=Success'를 채널 규칙으로 읽는다. 10.1.0.NN은 차량 NN의 채널1(No.NN), 10.1.1.NN은 같은 차량의 채널2(No.1NN)다(예: No.50과 No.150은 같은 차량 — 원자료 '추정'). 차량별로 두 채널을 짝지어, 한쪽 채널만 TimedOut이면 통신 단절이 아니라 이중화만 깨진 상태로, 양쪽 모두 TimedOut이면 단절로 판정한다. 같은 판정을 Window>PingList(CURERRORCOUNT/SETERRORCOUNT)와 Report>PingHistory(PingStatus·ReplyTime)로 대조한다. 양쪽 단절로 판정되면 CMD 명령으로 AP > Bridge > Vehicle PLC 구간을 좁히는 작업(L3a-04)으로 넘긴다.
  - 할 수 있어야 하는 것: Ping 로그를 차량별 채널 1/2로 짝지어 PingList·PingHistory와 대조하고 '이중화만 깨짐'과 '통신 단절'을 판정해, 단절이면 CMD 구간 분리(L3a-04)로 넘기는 결정을 내릴 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 8, 25; OCS 사용자 매뉴얼\_v04\_210114.docx 10.12 PingHistory; RCP Program setup 가이드 p.30 표22·24, p.50~52 표42~51; 02. RCPHMI.txt 9행(현상 2)
- **L3a-09 CMD 결과로 장애 구간 특정**
  - 내용: 차량 무선 경로 AP > Bridge > Vehicle PLC에서 Vehicle PLC ping 실패 시 Bridge로 ping해 구간을 좁히고, tracert로 끊긴 홉, telnet/tcping으로 포트 미개방, netstat -an |findstr으로 서버측 포트 미대기, arp -a·nbtstat -A로 IP 충돌 PC를 가린다. 결과를 근거로 서버/네트워크/차량 중 어느 쪽에 에스컬레이션할지 결정한다.
  - 할 수 있어야 하는 것: 여러 CMD 결과를 조합해 장애 구간(서버·AP·Bridge·차량 PLC·포트·IP 충돌)을 특정하고 조치·에스컬레이션 대상을 결정할 수 있다.
  - 근거: RCP Program setup 가이드 p.30 표22·24; RCP Program setup 가이드 p.50~52 표42~51

### L3a-05 서버 자원·FailOver 트리거·예외 로그 판정

- **레벨**: L3  ·  **교육 방식**: 로그실습  ·  **탭**: 로그파일  ·  **Section / Module**: Alarm & Troubleshooting / Log Analysis (Extended)  ·  **범위**: Extended
- **화면·도구**: D:\Program\Log\Core\날짜별\Event / SystemInfo>HARDWARE / ErrorList / 로그 파일 뷰어>DeleteOldHistoryPlayBackJob / Parameter > 4. MCCS Param(4.1~4.4) / 10. System Param(10.7, 10.10, 10.13, 10.16) / Report > FailOverHistory / FailOver 요청 INI 파일 / CoreForm UIException 로그
- **할 수 있어야 하는 것**: ① Event 로그의 CPU/RAM/DB·HQ·PQ 값과 Old Data Delete 소요시간을 계산·대조해 서버 느림이 일시 부하인지, DB 삭제 작업 때문인지, 큐 적체(어느 큐)인지 판정할 수 있다. ② FailOverHistory 1건과 MCCSParam·System Param 설정값을 대조해 FailOver가 CPU / Memory / Host Disconnect 중 어느 트리거로 요청됐는지 특정하고, 임계값 조정이 필요한지 에스컬레이션 여부를 판단할 수 있다. ③ UIException의 중문 다중 라인 예외를 해독해 DB 연결 단절 여부를 판정하고, 발생 빈도를 계수해 무시할지 DB/네트워크 점검으로 에스컬레이션할지 결정할 수 있다.
- **표시**: 사이트의존, 근거약함, 버전차이, 자료충돌, 추정해석
- **주의**: [L3a-10] 로그분석 매뉴얼의 Event 로그 형식([CPU]/[RAM]/[DB][HQ][PQ])과 DB 점검 매뉴얼의 형식(CPU : %, Memory : %, Process, DBQ)이 다르다. 버전이나 시기 차이로 보이므로 현장 로그 형식을 먼저 확인한다. 임계값은 사이트 설정값이다(검증자 overreach: 87/92/97은 현장 캡처값, 매뉴얼 예시는 80/85/90). 자원 경고의 조치 절차는 문서에 없다. / [L3a-11] C483·C184는 다른 버킷 후보를 검증자 missing(MCCSParam FailOver 요청 체계)에 따라 연결함. OCS 문서는 MCCS(Mantech Continuous Cluster Server) 기준으로 쓰여 있어 현장 RoseMirrorHA가 FailOverReq.ini를 받아 절체하는지 확인할 자료가 없음. 임계값을 실제로 바꾸는 행위는 L3-a Parameter 조정으로 쪼갤 수 있음. FailOverHistory는 v04본 10.17·MXA본 9.19 근거. / [L3a-12] 검증자 missing 항목이다. 중문 로케일은 대만 사이트 OS 설정에 따른 것이라 다른 사이트에서는 한글·영문 예외로 나온다. 다중 라인 계수법은 원자료상 추정이다.

- **L3a-10 Event 자원·큐·Old Data Delete 판정**
  - 내용: Event 로그 '[CPU: 0.0/ 0.2] [RAM:2280M/59.8%] [DB: 0] [HQ: 0] [PQ: 0]'(3초 주기)를 읽는다. CPU는 Core/전체, RAM은 Core MB/전체 %이고, DB·HQ·PQ는 DB·Host·PLC 큐 대기 건수다. 큐가 0이 아니면서 증가하면 그 큐의 적체로 판정하고, RAM이 계속 증가하면 누수를 의심한다. 자원 알람(CPU/Memory 임계 예: 87/92/97%·180초, HDD 5GB 이하, 사이트별 확인)이 뜨면 일시 부하인지 실제 이상인지 가른다. Event Log의 'PlayBack Old Data Delete' → 'PlayBack Old Data Delete - Result = True' 간격을 계산해 1초 미만이면 정상으로 본다(예: 15:28:23.148 → 15:28:23.585). 삭제 전후 'CPU : 0.0%, Memory : 0.0%, Process : 0MB, DBQ : 0' 값도 비교한다. 로그 파일 뷰어 > DeleteOldHistoryPlayBackJob으로도 확인할 수 있다.
  - 할 수 있어야 하는 것: Event 로그의 CPU/RAM/DB·HQ·PQ 값과 Old Data Delete 소요시간을 계산·대조해 서버 느림이 일시 부하인지, DB 삭제 작업 때문인지, 큐 적체(어느 큐)인지 판정할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 8, 25; CPU\_RAM\_HDD 점검 메뉴얼\_20220607.pdf p.5~9; DB 점검 메뉴얼\_20220607.pdf p.13~15
- **L3a-11 MCCSParam FailOver 트리거 판정**
  - 내용: Parameter > 4. MCCS Param의 4.1 UseFailOverRequest(RCP → MCCS FailOver 요청 사용 여부), 4.2 FailOverFilePath / 4.3 FailOverFileName(요청 INI 파일 경로·이름, 예 FailOverReq.ini), 4.4 HostDisconnectTimeout(Seconds, 0=사용 안 함)을 확인한다. 트리거는 CPU Warning Level3(10.7 CPUWarnLevel3 + 10.10 지속시간), Memory Warning Level3(10.13 MemoryWarnLevel3 + 10.16 지속시간), Host Disconnect 3조건이다. 기준값은 매뉴얼 예시 80/85/90%·100/110/120초, 현장 캡처 87/92/97%·180초로 서로 다르므로 사이트별로 확인하고, Report > FailOverHistory의 COMMENT 원인과 대조해 의도치 않은 FailOver가 어느 트리거로 났는지 가른다.
  - 할 수 있어야 하는 것: FailOverHistory 1건과 MCCSParam·System Param 설정값을 대조해 FailOver가 CPU / Memory / Host Disconnect 중 어느 트리거로 요청됐는지 특정하고, 임계값 조정이 필요한지 에스컬레이션 여부를 판단할 수 있다.
  - 근거: OCS Parameter 매뉴얼 p.25 (4.1~4.4), p.46~49 (10.7, 10.10, 10.13, 10.16); OCS 사용자 매뉴얼\_v04\_210114.pdf p31 (MCCSParam), p76 (FailOverHistory)
- **L3a-12 UIException 중문 예외 해독**
  - 내용: UIException의 번체 중문 예외를 해독한다. 예: '在接收來自伺服器的要求時發生傳輸層級的錯誤。(provider: TCP Provider, error: 0 - 遠端主機已強制關閉一個現存的連線。)' + .Net SqlClient Data Provider + '於 System.Data.SqlClient...' 스택. 핵심 어휘는 傳輸層級的錯誤(전송 계층 오류), 遠端主機已強制關閉(원격 호스트가 강제 종료), 現存的連線(기존 연결), 逾時(타임아웃), 於(at, 스택 프레임)이다. 이 메시지는 DB 연결 단절로 판정한다. 건수는 타임스탬프로 시작하는 줄만 센다. 간헐 발생은 무해한 것으로 보고, 몰려 나오면 DB 서버·네트워크 점검으로 넘긴다.
  - 할 수 있어야 하는 것: UIException의 중문 다중 라인 예외를 해독해 DB 연결 단절 여부를 판정하고, 발생 빈도를 계수해 무시할지 DB/네트워크 점검으로 에스컬레이션할지 결정할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 18

### L3a-06 다중 로그 재구성·근본원인 분리 (분석 방법)

- **레벨**: L3  ·  **교육 방식**: 로그실습  ·  **탭**: 로그파일  ·  **Section / Module**: Alarm & Troubleshooting / Log Analysis (Extended)  ·  **범위**: Extended
- **화면·도구**: Event·Ping·CommT·PntOccupy·VehicleEvent·OrderNack·MsgSend·Finder·MoveHistory·Warning·CommException 로그 / CoreForm / MCSIF_Form / PLCDRIVERFORM / Secom 로그 전체, grep·PowerShell Select-String
- **할 수 있어야 하는 것**: ① 여러 로그의 집계치를 정상 기준과 비교해 이상 항목을 골라내고, 그중 근본원인·증상·노이즈를 분리해 원인 후보 하나를 근거와 함께 제시할 수 있다. ② 주어진 사건 하나(예: 실행되지 않은 Host 지시)에 대해 조인 키를 골라 3개 이상 로그를 이어 붙이고, 시간순 타임라인으로 사건을 재구성할 수 있다.
- **표시**: 사이트의존, 추정해석, 병기
- **주의**: [L3a-13] 기준값은 Micron AATT Taichung 1시간 표본이고 타 사이트 환산식이 없다(data_gaps). 채점은 '자기 사이트 기준값을 구해 적용하는 절차'로 하고 수치 암기는 묻지 않는다. CommException을 결과로 보는 해석은 원자료상 추정이다. / [L3a-14] 코드 대역은 부록 A 대조표대로 260103_ErrTag_L30 / ErrorDescription 두 판을 병기한다. _ALARMID ↔ ErrEvent 조인은 사이트 System>ErrorTag에 실제 등록된 값으로 한다(L3a-10). 키 목록을 외워 설명하는 부분은 L2-b, 실제로 이어 붙이는 실습이 L3-a이다.

- **L3a-13 정상 기준 대비 이상·노이즈 분리**
  - 내용: 13개 정상 기준값(예시, 1시간·차량 44대)을 로그 집계 결과에 적용해 이상 여부를 판정한다. 예: Core CPU 0.0~0.1%(20% 초과 지속), DB/HQ/PQ 0(증가), Ping 99.87%·14.1ms(99% 미만·50ms 초과), CommT 491건/h·차량당 18~24, VEHICLE_30 504건/h, OrderNack 3건/h, MsgSend Remain 0~1, Finder Tm 1ms 미만, MoveHistory 874~2,000ms, ComThread 0~수 건/일, CommException 2KB/일, AP CPU 13~17%. 원인 특정은 근본원인·증상·노이즈를 분리하는 원칙을 따른다. 진입점 로그를 순서대로 열고, 뒤 로그부터 보면 증상을 원인으로 오인한다. CommException 'Cannot access a disposed object... System.Net.Sockets.Socket'(1건 4~5줄이므로 타임스탬프 줄만 셈)은 연결 종료의 결과이지 원인이 아니다. Warning _SNMP 줄은 노이즈이고, 용량·건수가 큰 로그가 원인인 경우는 드물다.
  - 할 수 있어야 하는 것: 여러 로그의 집계치를 정상 기준과 비교해 이상 항목을 골라내고, 그중 근본원인·증상·노이즈를 분리해 원인 후보 하나를 근거와 함께 제시할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 7, 15, 17, 25, 26
- **L3a-14 조인 키로 다중 로그 재구성**
  - 내용: 로그 간 조인 키로 사건 하나를 여러 로그에 걸쳐 이어 붙인다. 작업번호는 Comm JOB= ↔ Order [N. nnnn] ↔ SelectOrder/HandOver [N. nnnn] ↔ OrderFail fail=로 잇는다. Host 명령은 OrderNack CmdID·EventNumber ↔ MCSSystem CmdID·EventNumber로 잇는다. 이벤트는 WCFMsgTransfer EvtNum ↔ WCFMsgTransferXML \<EVENTNUMBER>로, SECS 전문은 SecsMsgTransfer SysByte ↔ SECS-II SystemBytes ↔ SECS-I [SB=] ↔ SECOMDRIVER SystemByte로 잇는다. PLC는 PlcTag 태그명 ↔ ReadWrite TagName/ADDRESS, _ALARMID ↔ ErrTag ErrEvent로 잇고, 위치는 Comm SEG= ↔ MoveHistory Seg= ↔ TM SegList로 잇는다. grep으로 키를 따라가며 시간순 통합 타임라인을 만든다.
  - 할 수 있어야 하는 것: 주어진 사건 하나(예: 실행되지 않은 Host 지시)에 대해 조인 키를 골라 3개 이상 로그를 이어 붙이고, 시간순 타임라인으로 사건을 재구성할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 4, 10~14, 20~24

### L3a-07 Order·Host 거부·배차/인계 로그 추적

- **레벨**: L3  ·  **교육 방식**: 로그실습  ·  **탭**: 로그파일  ·  **Section / Module**: Alarm & Troubleshooting / Log Analysis (Extended)  ·  **범위**: Extended
- **화면·도구**: CoreForm Order 로그 [N. nnnn] ↔ Comm JOB= / CoreForm OrderNack / MCSIF_Form MCSSystem 로그 / Report>NackHistory / System>OrderGroup / Parameter 5.15 / CoreForm SelectOrder / HandOver / OrderFail 로그 / System>Parameter>7. Priority Param, 13. Traffic Param 13.13
- **할 수 있어야 하는 것**: ① Order 로그를 작업번호로 추적해 5단계 중 끊긴 단계를 특정하고, 원인 방향(배차 실패/주행 정체)과 다음에 열 로그를 근거와 함께 제시할 수 있다. ② OrderNack·MCSSystem을 CmdID·EventNumber로 조인해 Host 지시 거부 사유를 특정하고, OrderGroup 설정을 대조해 OCS 내부 조치 대상인지 MCS(상위) 에스컬레이션 대상인지 결정할 수 있다. ③ SelectOrder·HandOver·OrderFail을 작업번호로 이어 배차 선택 근거와 인계 이력을 재구성하고, 떠도는 작업을 판정해 HandOverWeight·Priority 파라미터 조정안을 제시할 수 있다.
- **표시**: 근거약함, 사이트의존, 민감정보, 추정해석
- **주의**: [L3a-15] 검증자 fix6: 멈춘 Order를 어떤 순서로 해소하는지는 어느 자료에도 없다. 단계 특정까지만 채점하고, 해소 절차는 현장 인터뷰 산출물이 나오면 추가한다. / [L3a-16] CstID 예시 'UNKNOWNSTOTA20100…'에는 사이트 호스트명이 들어 있으므로 배포 시 마스킹한다. 정상 3건/h는 표본값이다. / [L3a-17] 검증자 overreach 지적 사항이다. 'HO=[n] 3 이상이면 떠도는 중'과 TOCNT 의미는 원자료상 추정이다. PRIO 의미는 파라미터 설정에 따라 다르다. 따라서 HO 임계값은 정답으로 고정하지 않는다.

- **L3a-15 Order [N.] 끊긴 단계 특정**
  - 내용: Order 로그 정상 5단계를 원문 줄로 식별한다: ① '[N. 40624628] U. 62, HomeOrder Event Occured, Point=1157' ② 'Vehicle OrderEvent Received, EventType=NEW_ORDER, OrderType=HomeOrder' ③ 'NewOrder EventReceived, TargetPnt1=1157' ④ 'Step = WAIT_UNTIL_TARGET_REACHED' ⑤ 'OrderFinished, ... Finish=True, HandOverCnt=0'. Comm의 JOB= 값으로 [N. 번호]를 grep해 끊긴 단계를 특정한다. Event Occured에서 끝났으면 배차 실패(SelectOrder·OrderNack으로 이동), WAIT_UNTIL_TARGET_REACHED에서 멈췄으면 주행 정체(Comm·PntOccupy로 이동)이다. Write PLC CstID 줄은 PLC 기록 경로(L3a-10)와 잇는다.
  - 할 수 있어야 하는 것: Order 로그를 작업번호로 추적해 5단계 중 끊긴 단계를 특정하고, 원인 방향(배차 실패/주행 정체)과 다음에 열 로그를 근거와 함께 제시할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 4, 10
- **L3a-16 Host 지시 거부 판정·에스컬레이션**
  - 내용: OrderNack 원문에서 Type(FromOrder/ToOrder), CstID(UNKNOWN…은 미인식), Result(거부 사유), CmdID·EventNumber, Trig(HOST=상위/GT=수동)를 읽는다. 예: 'Result=Call Prevented, VehicleNumber = 50, CmdID = 737278', 'Result=Cannot find Cassette ID'. 같은 CmdID·EventNumber로 MCSIF MCSSystem의 'S2F49 TRANSFER Call Prevented', 'S2F41 ABORT Order Step is CompleteStep', 'S2F41 Remove Cannot find Cassette ID'와 조인한다. 5.15 CheckTransferDeliverOrderGroup(To 명령 해당)에 의한 'OrderGroup을 찾을 수 없음' Nack이 나오면 먼저 System>OrderGroup에서 해당 From/To Station이 같은 그룹에 등록돼 있는지 확인한다. OCS 설정 누락이면 보완한다(매뉴얼 사용예시 'OrderGroup 설정 확인'). 설정이 맞는데 명령이 그룹 밖 경로를 지정했으면 MCS 명령 오류로 보고 상위 담당자에게 확인을 요청한다(매뉴얼 참고 'MCS에서 명령이 잘못 내려왔을 시 담당자 확인요청'). 이력은 Report>NackHistory로 대조한다.
  - 할 수 있어야 하는 것: OrderNack·MCSSystem을 CmdID·EventNumber로 조인해 Host 지시 거부 사유를 특정하고, OrderGroup 설정을 대조해 OCS 내부 조치 대상인지 MCS(상위) 에스컬레이션 대상인지 결정할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 11, 22, 25; OCS Parameter 매뉴얼 p.33(5.15)
- **L3a-17 배차·인계 추적과 가중치 조정**
  - 내용: SelectOrder '[#0] ToVeh, [N. 735080] > U. 54, W= 28336, MW= 1518336, [ 1016, 0, 0]->[22112]'를 후보 전체에서 비교해 W=(최소 차량 선택)와 MW=(보정 포함 최종)로 '왜 저 차량이 갔나'를 답한다. HandOver 'ALLOCATE2, HO=[ 0], PRIO= 9, TOCNT=0' → 'HANDOVER2-FIRSTORDER' → 'U. 67, ALLOCATE2, HO=[ 1]'로 인계 이력을 재구성한다. OrderFail '[N. 731343] U.111, GetOrder with handOver fail=731342'의 fail= 번호로 인계 실패를 추적해 계속 떠도는 작업을 판정한다. 인계가 과도하면 13.13 HandOverWeight를 조정하고(SelectOrder Log로 근거 확인), 우선순위가 쌓이는 문제는 7.1 PriorityChangeTime / 7.2 AdvantagePerPriority를 사이트 규모에 맞춰 조정한다.
  - 할 수 있어야 하는 것: SelectOrder·HandOver·OrderFail을 작업번호로 이어 배차 선택 근거와 인계 이력을 재구성하고, 떠도는 작업을 판정해 HandOverWeight·Priority 파라미터 조정안을 제시할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 11, 12; OCS Parameter 매뉴얼 p.37(7.1, 7.2), p.71(13.13)

### L3a-08 정체 레일·블로킹·혼잡도 분석

- **레벨**: L3  ·  **교육 방식**: 로그실습  ·  **탭**: 로그파일  ·  **Section / Module**: Alarm & Troubleshooting / Log Analysis (Extended)  ·  **범위**: Extended
- **화면·도구**: CoreForm MoveHistory / Finder / TM 로그 / Report>BlockingHistory / Statistics>Vehicle>BlockRate / System>Parameter>BlockingParam>PushWeight / CoreForm VehicleEvent 로그
- **할 수 있어야 하는 것**: ① MoveHistory 집계와 Finder·TM 원문으로 정체 레일과 경로 이상(탐색 지연, 계산 중단 지점)을 특정할 수 있다. ② BlockingHistory 연쇄 추적과 BlockRate 교차검증으로 블로킹 원인 차량과 성격을 특정하고, PushWeight 조정 결과를 검증하거나 Move 명령으로 우회 조치할 수 있다. ③ VehicleEvent의 VEHICLE_30/31 건수와 연쇄 해제 시점을 집계해 라인 정체의 심화와 해소 구간을 특정할 수 있다.
- **표시**: 추정해석, 사이트의존, 근거약함
- **주의**: [L3a-18] MoveHistory의 #1과 TM의 Tr=(누적 주행시간)은 원자료상 추정이다. 정상 Time 874~2,000ms는 표본값이다. / [L3a-19] PushWeight 미동작은 RCPHMI의 미해결 이슈이고 최종 원인이 없다. 이 부분은 Case Bank에서 '정답 없음/분석 과정 연습'으로 평가하고, BlockedBy 연쇄 추적만 정답 채점한다. / [L3a-21] 검증자 missing 항목이다. '30번=혼잡도 지표', '연쇄 해제=행렬 해소'는 원자료상 추정이다. VEHICLE_nn 번호 체계와 건수는 사이트 ErrTag와 표본에 의존한다.

- **L3a-18 정체 레일·경로 계산 판독**
  - 내용: MoveHistory '09:03:56.911, U. 69 L Pnt= 1088, Seg= 87, Time= 874, #1'을 Seg별 Time 평균으로 집계해 느린 레일을 특정한다(예: U.57 7,997ms는 평균 874ms의 9배). Finder 'F=1271 T=1259 Seg=270 Pnt=1271', 'M=1271-1272-…-1259', 'Tm=0.4617, O'에서 출발/목적, 확정 경로, 탐색 ms(정상 1ms 미만), W=(F=T이면 20)를 읽는다. TM 'AllocSegW = 0, SegList = 271,272,…' → 'P=1271, S=271, C=1, Tr=0, Tm = 0.0035' → 'Brk. Pnt OutSegSize. Pnt=1436'에서 Brk. 지점을 '경로는 나왔는데 차량이 가지 않는' 계산 중단 지점으로 특정한다. Comm SEG=와 Seg=·SegList로 조인한다.
  - 할 수 있어야 하는 것: MoveHistory 집계와 Finder·TM 원문으로 정체 레일과 경로 이상(탐색 지연, 계산 중단 지점)을 특정할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 13, 14, 25
- **L3a-19 블로킹 원인·PushWeight 검증**
  - 내용: Report>BlockingHistory의 BlockedBy(앞 차량)를 연쇄로 거슬러 올라가 선두 유발 차량을 특정한다(StartTime/EndTime/BlockingTime/Point/Segment/CommandID). '밀어내기가 안 된다' 현상은 BlockingHistory 로그 유무와 Statistics>Vehicle BlockRate(예: 0%)를 교차해 블로킹 문제인지 아닌지 가설을 세우거나 기각한다. System>Parameter>BlockingParam>PushWeight는 값에 따라 밀어내기 시작 거리가 달라진다(예: 10000이면 1호기가 Pnt 1320에서, 30000이면 2호기가 Pnt 1309에서 시도). 매뉴얼대로 동작하지 않는 사례가 있으므로 값 조정 후 실제 거동을 검증하고, 미동작 시 막고 있는 차량에 Move 명령을 내려 우회한다.
  - 할 수 있어야 하는 것: BlockingHistory 연쇄 추적과 BlockRate 교차검증으로 블로킹 원인 차량과 성격을 특정하고, PushWeight 조정 결과를 검증하거나 Move 명령으로 우회 조치할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p66; 02. RCPHMI.txt 1~7행(현상 1); RCP\_Parameter\_Manual\_v0.0.1 BlockingParam>PushWeight
- **L3a-21 VehicleEvent 혼잡도 해석**
  - 내용: VehicleEvent '09:34:03.852, U. 85 DeleteAlarmDB = VEHICLE_189'(알람 해제), 'U. 50 RegistProcess'(차량 등록)를 읽는다. VEHICLE_30(전방 차량감지 정지)은 알람이라기보다 혼잡도 계측값으로 읽고 시간당 건수를 집계한다(표본 504건/h). VEHICLE_31(전방 사람감지, 표본 3건/h)은 따로 본다. 여러 차량의 VEHICLE_30이 연달아 해제되는 순간을 막혔던 행렬이 풀리는 시점으로 판정해 라인 정체 시작~해소 구간을 특정한다.
  - 할 수 있어야 하는 것: VehicleEvent의 VEHICLE_30/31 건수와 연쇄 해제 시점을 집계해 라인 정체의 심화와 해소 구간을 특정할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 15, 25

### L3a-09 상위 통신 로그 체인·S9/타임아웃 판정

- **레벨**: L3  ·  **교육 방식**: 로그실습  ·  **탭**: 로그파일  ·  **Section / Module**: Host Interface (HSMS) / SECS Deep-dive (Extended)  ·  **범위**: Extended
- **화면·도구**: CoreForm MsgRecv / MsgSend, MCSIF_Form WCFMsgTransfer / WCFMsgTransferXML 로그 / MCSIF_Form SecsMsgTransfer / Secom SECS-II / SECS-I 로그 / Secom SECOMDRIVER 로그 / SECS-II 로그 / HSMS Parameter(T3, T5, T6, T7, T8, Link Test)
- **할 수 있어야 하는 것**: ① MsgRecv·MsgSend·WCFMsgTransfer·XML을 이어 Host 지시의 도착 여부, 송신 적체, 채널별 이벤트 처리 실패, 수동 조작 주체를 판정할 수 있다. ② SecsMsgTransfer·SECS-II·SECS-I를 SystemBytes로 조인해 특정 보고 1건의 송신·응답·거부 여부를 바이트 수준까지 판정할 수 있다. ③ 끊김 로그와 S9 메시지를 보고 상위 통신 이상이 스펙 불일치(S9F1~F7)인지 타임아웃(S9F9·T3~T8·LinkTest)인지 가르고, 어느 타임아웃이 걸렸는지와 멈춘 메시지를 역추적할 수 있다.
- **표시**: 추정해석, 민감정보, 사이트의존, 자료충돌
- **주의**: [L3a-22] Ip=, USERNAME, PCNAME, IPADDRESS는 배포 시 마스킹한다. 'Remain 누적=Host 응답 지연'과 '채널 1만 실패' 해석은 원자료상 추정이다. / [L3a-23] 검증자 overreach 지적 사항이다. CEID 번호대는 BASIC SPEC(51·52 알람, 503·504 유닛알람, 201 도착)과 RCP setup 가이드(101~/201~/…/701~ 번호대)가 충돌하고, setup 가이드는 '현장 상위 프로그램 기준'이라고 명시한다. CEID 값은 사이트 SML로 확인해 채점한다. EQPNAME 'STOTA20100'은 마스킹한다. / [L3a-24] 검증자 missing 항목이다. 타임아웃 값은 기본값이며 사이트 설정은 다를 수 있다. S9 계열 종류를 아는 것은 L2-b, 실제 로그로 판정하는 것이 L3-a이다.

- **L3a-22 Host 메시지 체인 추적**
  - 내용: MsgRecv '[Recv] No.3450811, Msg Event Catched' → '[Info] ... Type = RemoteCommandTransferFromTo'로 Host 지시 도착을 확인한다. 'AliveCheck. Id=0'(약 10초 주기)가 끊기면 연동 단절로 판정한다. 'EventName = ManualCommandInsert, Ip = …'로 HMI 수동 조작 단말을 추적한다. MsgSend '[S] … gRpc Host Send Success, Name = EventTransferPaused, Remain = 0'에서 Remain 0~1이 정상이고 계속 쌓이면 Host 응답 지연이다. WCFMsgTransfer '[CoreToMCS] [ID=n] EvtNum : … EventName : …'에서 채널별 실패(예: [ID=1]만 'HandleReceiveCoreEventMsg failed NOT_DEFINE_XCOMPROC')를 찾아 인터페이스 정의 점검 대상으로 판정한다. 같은 EvtNum으로 WCFMsgTransferXML의 \<TRIGGER>(CORE=자동/ADMIN·GT=사람), \<USERNAME>, \<PCNAME>, \<IPADDRESS>를 조회해 조작 주체를 확정한다.
  - 할 수 있어야 하는 것: MsgRecv·MsgSend·WCFMsgTransfer·XML을 이어 Host 지시의 도착 여부, 송신 적체, 채널별 이벤트 처리 실패, 수동 조작 주체를 판정할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 16, 22, 23, 25
- **L3a-23 SECS 전문 SysByte 체인 판독**
  - 내용: SecsMsgTransfer '[ID=1] EvtNum : …, SysByte : …, [SEND] S6F11 CEID = 503, (CEID_Unit_Alarm_Clear)' → '[RECV] S5F2 Alarm Report Acknowledge ... OK'에서 [SEND]/[RECV] 짝을 맞춘다. [SEND] 뒤에 [RECV] S5F2가 없으면 Host 미수신이다. SysByte로 SECS-II 해석본 'SEND : D1 S6F11 W SystemBytes=11517666 \<L 3 \<U4 1 DATAID> \<U2 1 CEID '504'> … \<U2 1 RPTID '12'> … \<U2 1 ALARMID '30'> \<A 34 ALARMTEXT …>' → 'SENT : S6 F11 [11517666] ErrorCode=0'(≠0이면 Host 거부)로 이어 간다. SECS-I 바이너리 'SEND 00 01 86 0B … Length = 86 (S6F11W) [SB=11517704] / 41 0A 53 54 4F 54 41 …'는 바이트 단위로 해독하고(41=A 타입, 0A=길이 10, ASCII), RECD (S6F12) 짝 여부를 확인한다.
  - 할 수 있어야 하는 것: SecsMsgTransfer·SECS-II·SECS-I를 SystemBytes로 조인해 특정 보고 1건의 송신·응답·거부 여부를 바이트 수준까지 판정할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 23, 24
- **L3a-24 S9·HSMS 타임아웃 원인 판정**
  - 내용: 상위 통신 이상을 스펙 불일치와 타임아웃으로 가른다. 스펙 불일치는 S9F1 Unrecognized Device ID / S9F3 Unrecognized Stream Type / S9F5 Unrecognized Function Type / S9F7 Illegal Data(MHEAD 10바이트 동봉)이고, 트랜잭션 타임아웃은 S9F9 Transaction Timer time-out(SHEAD 동봉)이다. HSMS 타임아웃은 동작별로 판정한다: T3 Reply(기본 45s, 1~120)는 Timeout Event만 발생시킨다. T6 Control(5s), T7 Connection Idle(10s), T8 Network Intercharacter(5s), Link Test(10s, 0=미수행) 실패는 Separate.Req 후 TCP/IP 연결을 끊는다. T5(10s)는 재연결 대기 시간이다. SECOMDRIVER의 'HSMSDriver OnReadHsms LinkTest Restart Success'가 주기적으로 나오는지 확인하고, 'Before ReceiveEvent SystemByte: …'만 있고 After가 없으면 그 메시지에서 멈춘 것으로 판정한다.
  - 할 수 있어야 하는 것: 끊김 로그와 S9 메시지를 보고 상위 통신 이상이 스펙 불일치(S9F1~F7)인지 타임아웃(S9F9·T3~T8·LinkTest)인지 가르고, 어느 타임아웃이 걸렸는지와 멈춘 메시지를 역추적할 수 있다.
  - 근거: 2\_SFA\_VHC\_MESSAGE\_SPEC\_V3.4.pdf p.58~60(2.42~2.46 S9F1~S9F9); RCP Program setup 가이드 p.47 표53, 본문 P587; 1\_SFA\_VHC\_BASIC\_SPEC\_V3.2.pdf p.8(3.4 Communication Standard Summary); RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 24

### L3a-10 설비 알람·PLC 로그 추적 (PlcTag·Not Define·카세트 ID)

- **레벨**: L3  ·  **교육 방식**: 로그실습  ·  **탭**: System  ·  **Section / Module**: Alarm & Troubleshooting / Log Analysis (Extended)  ·  **범위**: Extended
- **화면·도구**: CoreForm PlcTag 로그 / System>ErrorTag / System>PLC Tag / 260103_ErrTag_L30.xlsx / Window>AlarmList / System>ErrorTag / System>PLC Tag / Parameter>17. VehicleEvent Param / CoreForm PlcTag, PLCDRIVERFORM MsgTransfer / ReadWrite / PlcCommLog 로그 / System>PLC Tag
- **할 수 있어야 하는 것**: ① PlcTag ST·ALARMID 시계열과 ErrTag 조회로 설비 알람의 내용과 발생~복구 구간을 확정하고, 자료 불일치(ErrTag/ErrorDescription, Comment/TagProperty)로 인한 오판을 피할 수 있다. ② Not Define 알람을 'ErrorTag 미등록 + 원래 이벤트 발생'으로 해석해 발생 ErrType·ErrEvent를 찾아내고, 원래 이벤트 처리와 별개로 매핑 규칙과 차량 담당자 확인 절차에 따라 ErrorTag(필요 시 17.x Parameter)를 보완할 수 있다. ③ PlcTag·MsgTransfer·ReadWrite·PlcCommLog를 이어 카세트 ID 불일치가 센서, DB 기록, PLC 통신 중 어디서 생겼는지 특정할 수 있다.
- **표시**: 추정해석, 사이트의존, 병기, 근거약함
- **주의**: [L3a-25] ST 1/3/2의 의미는 사례 1건 관측 기반 추정이다. 코드 대역은 부록 A 대조표대로 260103_ErrTag_L30 / ErrorDescription 두 판을 병기한다. 채점은 '사이트 ErrorTag 화면에서 확인한다'는 절차형으로 한다. TagProperty/Comment 결함은 해당 사이트 파일의 데이터이다. / [L3a-26] CPS 29/30 사례는 파일 행 수를 대조해 추론한 것이고 실제 발생은 확인되지 않았다. / [L3a-27] 검증자 fix6: PlcCommLog가 WaitConnect일 때 무엇을 재시작하는지는 자료에 없다. 미연결 판정까지만 채점하고, 재시작 대상은 현장 인터뷰 산출물이 나온 뒤 평가한다.

- **L3a-25 PlcTag 알람 구간·ErrTag 조인**
  - 내용: PlcTag 원문으로 스테이션 알람 발생~복구를 재구성한다. 예: 04:51:30.459 STATION_765_ALARMID [0]->[110], STATION_765_ST [1]->[3] → 04:55:16 STATION_763~766_ST [1]->[2] → 04:55:18 ALARMID [110]->[0], ST [3]->[2] → 04:55:52 ST [2]->[1]. 4분이 걸렸다. ST는 1=정상, 3=알람, 2=전환/대기로 읽는다. ALARMID는 System>ErrorTag(260103_ErrTag_L30.xlsx) ErrEvent로 조회한다(예: 110 → ErrType=STATIONALARM, ErrCode 8122 'OLUS 송수신 조건이상'). STATIONALARM 대역은 두 판이 다르므로(ErrTag 8105~8130 / ErrorDescription 5000~5273) 사이트 System>ErrorTag에 등록된 판으로 조회하고 두 판의 번호를 섞지 않는다. 태그는 Comment가 아니라 TagName_TagNumber_TagProperty 기준으로 판독한다(예: addr 10102 TagProperty=CSTSIZE인데 Comment가 'OLUS#3 MAIN ALARMID').
  - 할 수 있어야 하는 것: PlcTag ST·ALARMID 시계열과 ErrTag 조회로 설비 알람의 내용과 발생~복구 구간을 확정하고, 자료 불일치(ErrTag/ErrorDescription, Comment/TagProperty)로 인한 오판을 피할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 20; 260103\_ErrTag\_L30.xlsx STATIONALARM 26행 대조; ErrorDescription.xlsx ErrType 분포; 260103\_PlcTag\_L30.xlsx STATION 356행 점검
- **L3a-26 Not Define 알람 처리**
  - 내용: Window>AlarmList에 Not Define(Not Defined Error) 알람이 뜨면 ErrorTag에 등록되지 않은 Error가 실제로 발생한 것이다(사용자 매뉴얼 7.8: 미등록 Error 발생 시 'Not Defined Error' 표시). 알람명만으로는 원인을 알 수 없다. 발생 이벤트의 ErrType·ErrEvent(PlcTag Name/Value 또는 차량 에러번호)를 찾아 원래 이벤트(설비·차량 이상일 수 있음)는 따로 처리하고, ErrorTag 미등록을 보완한다. RCP 자체 알람은 초기 셋업 때 자동으로 들어가므로 미등록은 주로 제어측 신규 알람에서 생긴다(setup 가이드). 보완은 System>ErrorTag에 PlcTag:Name=ErrorTag:ErrType, PlcTag:Value=ErrorTag:ErrEvent 규칙으로 추가·수정한다. 차량 에러번호(17.2 ObstacleSensorErrorEvent, 17.5/17.6 PIOErrorEventRangeMin/Max 등)는 추측하지 않는다. 차량 담당자에게 실제 번호를 확인한 뒤 Error Tag와 Parameter에 등록한다. 등록 누락 구조 예: PlcTag CPS 30대 vs ErrTag CPSDOWN 28대.
  - 할 수 있어야 하는 것: Not Define 알람을 'ErrorTag 미등록 + 원래 이벤트 발생'으로 해석해 발생 ErrType·ErrEvent를 찾아내고, 원래 이벤트 처리와 별개로 매핑 규칙과 차량 담당자 확인 절차에 따라 ErrorTag(필요 시 17.x Parameter)를 보완할 수 있다.
  - 근거: RCP Program setup 가이드 p.34 본문 P338~339; OCS 사용자 매뉴얼\_v04\_210114.docx 7.8 ErrorTag; OCS Parameter 매뉴얼 p.89(17.2), p.90(17.5, 17.6); 260103\_ErrTag\_L30.xlsx CPSDOWN vs 260103\_PlcTag\_L30.xlsx CPS
- **L3a-27 카세트 ID PLC 경로 추적**
  - 내용: PlcTag로 카세트 이동을 추적한다. 예: 09:40:41 STATION_768_CSTID []->[TPK31082] → 09:40:43 STATION_768_EXIST [0]->[1] → 09:40:49 STATION_10768_CSTID []->[TPK31082] + STATION_768_CSTID [TPK31082]->[]. 이 순서면 768→10768 이동 완료로 본다. _CSTID는 찼는데 _EXIST=0이면 센서/DB 불일치, 값 변화가 아예 없으면 PLC 통신 두절로 판정한다. 쓰기 경로는 Order 'Write PLC CstID' → MsgTransfer '[CoreToPlcDrv] EvtNumber : … EventWriteDataRequest' → ReadWrite 'TagName : STATION_768_CSTID, PlcNum : 6, ADDRESS : 10410, … PLCREAD : OK, DBWrite : OK, PlcConnection : OK' 순으로 따라간다. NG가 난 단계로 원인 위치를 가른다: PLCREAD는 통신/주소, DBWrite는 PLC-DB 불일치, PlcConnection은 연결 끊김. PlcCommLog CurrentStep : Run이면 정상, WaitConnect에 머물면 미연결이다. 이때 U. n은 PLC 번호다.
  - 할 수 있어야 하는 것: PlcTag·MsgTransfer·ReadWrite·PlcCommLog를 이어 카세트 ID 불일치가 센서, DB 기록, PLC 통신 중 어디서 생겼는지 특정할 수 있다.
  - 근거: RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 20, 21; 260103\_PlcTag\_L30.xlsx STATION CSTID/EXIST 태그 정의

### L3a-11 SECS 메시지 판독 (HCACK/CPACK·VID·S6F11·S5F1)

- **레벨**: L3  ·  **교육 방식**: 로그실습  ·  **탭**: 프로토콜  ·  **Section / Module**: Host Interface (HSMS) / SECS Deep-dive (Extended)  ·  **범위**: Extended
- **화면·도구**: SECS-II 로그 S2F42 / S2F50 / SECS Data Items 참조표 / SECS-II 로그 S6F11 / S1F3·S1F4 / SECS-II 로그 S6F11 / 에뮬레이터 SECS-II 통신 로그 / SECS-II 로그 S5F1 / S6F11 / MsgSend 로그
- **할 수 있어야 하는 것**: ① S2F42/S2F50 응답의 HCACK와 CPACK 쌍을 읽어 MCS 명령이 거부된 원인 파라미터와 중복 지령 유형을 특정할 수 있다. ② S6F11/S1F4의 VID 값으로 반송이 어떤 사유(Host/수동/자동/PIO Timeout)로 끝났는지, 지령 주체가 MCS인지 OCS 수동인지, 차량이 Jam/Stuck/통신단절 중 어느 상태인지 판정할 수 있다. ③ S6F11 원문을 받아 CEID와 RPTID로 리포트 포맷을 결정하고 본문 필드(위치·상태·ResultCode 등)를 판독할 수 있다. ④ 한 알람의 S5F1·AlarmSet·UnitAlarmSet 3건을 짝짓고 ALCD 비트를 분해해 발생/해제와 카테고리, 진행 중 반송에 미친 영향을 판정할 수 있다.
- **표시**: 자료충돌, 근거약함, 민감정보, 사이트의존, 추정해석
- **주의**: [L3a-28] SFA SPEC 계열의 번호 체계는 RCP setup 가이드와 충돌할 수 있으므로 현장 SML로 확인한다. 48개 Data Item 전체 암기는 평가하지 않는다(C357 근거약함). / [L3a-29] S1F4 예시의 VEHICLEID·PORTID·CARRIERID는 사이트 실값이라 마스킹한다. / [L3a-30] CEID 번호대는 BASIC SPEC과 RCP setup 가이드가 충돌한다(검증자 overreach). CEID 10/11은 MESSAGE SPEC에만 있다. Line Out 후에도 S6F11이 반복되는 현상(C308)은 미해결 이슈라 '정답 없음' 케이스로만 쓴다. / [L3a-31] CEID 번호는 사이트 SML 기준으로 확인한다. MsgSend의 '3종 세트' 대응은 로그분석 매뉴얼상 추정이다.

- **L3a-28 HCACK·CPACK 거부 원인 판정**
  - 내용: S2F42/S2F50의 HCACK로 MCS 명령 거부 원인을 판정한다. 코드: 1 명령 없음, 2 현재 실행 불가, 3 파라미터 무효, 4 Confirmed(이벤트로 완료 통보), 5 이미 요청됨, 6 객체 없음, 7 Already Auto, 8/9 DEST/SOURCE 명령 한도 초과, 13 CommandID-CarrierID 불일치, 22/27 Source/Dest Unit 없음, 28 Source=Dest, 31 Carrier 없음, 41/42 Unit Unavail, 45/46 Port Cassette 유무, 47/48 Type Interlock, 55 CarrierID 이미 요청됨. HCACK=3이면 CPNAME/CPACK 쌍(1 Undefined, 2 incorrect value, 3 incorrect Format)으로 문제 파라미터를 특정한다(예: 'PRIORITY' 1, 'DESTPORT' 1). 중복 지령은 HCACK 0x05(같은 Carrier/CommandID, 원 명령 계속)와 0x08(다른 Carrier가 같은 Dest Port, 먼저 등록된 반송 수행)로 구분한다. 그 밖의 ACK 계열(ACKC5/6, DRACK, LRACK, ERACK, ONLACK/OFLACK, TIACK)은 실제 로그에 나온 코드만 참조표로 해석한다.
  - 할 수 있어야 하는 것: S2F42/S2F50 응답의 HCACK와 CPACK 쌍을 읽어 MCS 명령이 거부된 원인 파라미터와 중복 지령 유형을 특정할 수 있다.
  - 근거: 1\_SFA\_VHC\_BASIC\_SPEC\_V3.2.pdf p.19~22(5.1 SECS Data Items, No.26 HCACK); 2\_SFA\_VHC\_MESSAGE\_SPEC\_V3.4.pdf p.31~33(S2F42); 3\_SFA\_VHC\_SCENARIO\_SPEC\_V3.5.pdf p.45, p.47(9.1, 9.3)
- **L3a-29 반송·차량 VID 코드 판정**
  - 내용: 반송 종료 사유를 VID 코드로 판정한다. CommandState(VID 93)는 3 Complete, 11/12 HOST_Cancel/Abort, 21/22 MNL_Cancel/Abort, 31/32 AUTO_Cancel/Abort, 41/42 Source/Dest_PIOTimeOver이다. ResultCode(VID 64)는 0 success, 4 Duplicate, 5 Mismatch, 6 ID Read Fail, 16 Carrier Size Error, 64 Load/Unload Error by Vehicle, 20~22 복합이다. TransferState(VID 202)는 1 queued~6 waiting, IDReadStatus(VID 210)는 0 Success/1 Failure/2 Duplicate/3 Mismatch/4 NoCarrier이다. CommandID가 'MNL'+설비명 8자리+YYYYMMDDHH24MISS+순번으로 시작하면 OCS 수동 지령, 아니면 MCS 지령이다. 차량 상태는 VehicleState(72) 1 Removed~6 Depositing, OperationState(419), JamState(416) 0/1/2 Stuck, CommunicationState(413), MainteState(408)로 읽는다. S1F3 SVID 요청과 S1F4 응답(ActiveVehicles, CurrentPortStates, EnhancedCarriers)을 필드 단위로 판독한다.
  - 할 수 있어야 하는 것: S6F11/S1F4의 VID 값으로 반송이 어떤 사유(Host/수동/자동/PIO Timeout)로 끝났는지, 지령 주체가 MCS인지 OCS 수동인지, 차량이 Jam/Stuck/통신단절 중 어느 상태인지 판정할 수 있다.
  - 근거: 1\_SFA\_VHC\_BASIC\_SPEC\_V3.2.pdf p.27~28, p.31, p.33~36, p.55~58; 2\_SFA\_VHC\_MESSAGE\_SPEC\_V3.4.pdf p.10~14(S1F3, S1F4)
- **L3a-30 S6F11 CEID·RPTID 본문 판독**
  - 내용: S6F11의 CEID→RPTID 매핑으로 본문 필드 구성을 정해 판독한다. 매핑 예(MESSAGE SPEC 2.38 기준): RPTID 1 → CEID 1,2,3,10,11,51~57 / RPTID 2 → 107,109 / RPTID 3 → 101~106,108,110,111 / RPTID 9 → 254 / RPTID 11 → 251 / RPTID 13 → 503,504 / RPTID 14 → 270 / RPTID 16 → 153,154. 다만 SCENARIO SPEC(7·8장 UnitAlarmSet)과 실제 SECS-II 로그('CEID 504 … RPTID 12')는 UnitAlarm을 RPTID 12로 보고한다. RPTID 12와 13은 같은 UnitAlarm 포맷(UnitID+AlarmID+AlarmText+위치+UnitStatusCleable)이므로, 어느 번호를 쓰는지 현장 SML로 확인한 뒤 판독한다. RPTID별 포맷 예: 2=EqpName+CommandInfo+TransferCompleteInfo+ResultCode+…, 11=CommandID+CarrierID+IDReadStatus+CarrierLoc, 14=MonitoredVehicles 7필드. 실제 로그 '[17:19:39.989] RECV S6F11 … [SB=5986]'에서 CEID 270, RPTID 14, 위치 1490/103, MainteState=2(Not Maintenance)를 읽는다. Line Out 뒤 MonitoredVehicles 보고 대상이 바뀌는 현상도 분석한다.
  - 할 수 있어야 하는 것: S6F11 원문을 받아 CEID와 RPTID로 리포트 포맷을 결정하고 본문 필드(위치·상태·ResultCode 등)를 판독할 수 있다.
  - 근거: 1\_SFA\_VHC\_BASIC\_SPEC\_V3.2.pdf p.42~49(7.1~7.3 ReportID); 2\_SFA\_VHC\_MESSAGE\_SPEC\_V3.4.pdf p.40~57(2.38 S6F11); 02. RCPHMI.txt 27~29행, 32~106행(현상 8)
- **L3a-31 알람 3중 보고 대조**
  - 내용: 알람 1건이 S5F1 Alarm Report → S6F11 AlarmSet(CEID 52, RPTID 1) → S6F11 UnitAlarmSet(CEID 504, RPTID 12) 3건 세트로 나가는지 짝지어 확인한다. 해제는 S5F1 → AlarmCleared(51) → UnitAlarmCleared(503)이고, MsgSend에서는 EventAlarmSetReport + EventAlarmSet + EventUnitAlarmSet으로 나간다. 주행 중 차량에 알람이 걸리면 TransferPaused(109, RPTID 2)가, 해제되면 TransferResumed(110)가 붙는지로 Transfer 영향을 판정한다. S5F1의 ALCD는 bit8=1 발생/0 해제, bit7~1 카테고리(1 Personal safety … 9 other, 9는 MES 미보고)로 분해한다(예: ALARMCODE '128'=0x80, 발생+카테고리 0). ALID·ALTX·UNITID도 함께 읽는다.
  - 할 수 있어야 하는 것: 한 알람의 S5F1·AlarmSet·UnitAlarmSet 3건을 짝짓고 ALCD 비트를 분해해 발생/해제와 카테고리, 진행 중 반송에 미친 영향을 판정할 수 있다.
  - 근거: 3\_SFA\_VHC\_SCENARIO\_SPEC\_V3.5.pdf p.37~40(7.1~7.3); 2\_SFA\_VHC\_MESSAGE\_SPEC\_V3.4.pdf p.36~37(2.32 S5F1); RCP\_실전\_로그분석\_매뉴얼.pptx 슬라이드 16

### L3a-12 이적재 실패 케이스 (PIO Interlock·BCR NG·Empty/Double)

- **레벨**: L3  ·  **교육 방식**: 로그실습  ·  **탭**: 프로토콜  ·  **Section / Module**: Host Interface (HSMS) / SECS Deep-dive (Extended)  ·  **범위**: Extended
- **화면·도구**: SECS-II 로그 S6F11·S2F49 / TSC(OCS) Manual Transfer / Parameter>6. PIO Param 6.1~6.3 / SECS-II 로그 S6F11(151~154, 203, 251, 107) / OrderNack CstID / SECS-II 로그 S6F11·S2F41 / OCS Manual Order 생성
- **할 수 있어야 하는 것**: ① ResultCode=64와 CarrierLoc으로 적재/하역 실패를 구분하고, Once Retry → AbortLocation → Manual Handling 단계 중 현재 위치를 판정해 수동 개입 시점과 방법(MCS 재지령/OCS Manual Transfer)을 결정할 수 있다. ② CEID 조합과 IDReadStatus/ResultCode로 BCR NG 유형을 판정하고, UNKNOWN CarrierID를 분해해 유령 카세트의 발생 시점과 경위를 추적할 수 있다. ③ TransferPaused 이후 이벤트 조합으로 Empty Retrieval과 Double Storage를 구분하고, STB Double Storage에서 Manual Order 생성이 필요한 시점을 결정할 수 있다.
- **표시**: 자료충돌, 사이트의존, 민감정보
- **주의**: [L3a-32] 검증자 missing(PIO Interlock 자동 복구 체계)이다. CEID 번호는 사이트 SML로 확인한다. Once Retry는 MCS 시나리오이고 RetryCount는 OCS 파라미터라 주체가 다르다는 점을 구분해 가르친다. Manual Transfer 화면 조작 자체는 L1이다. / [L3a-33] 검증자 missing 항목이다. OrderNack 실례 'UNKNOWNSTOTA20100260803094846336444'와 형식이 일치하는지 사이트에서 확인한다. CEID 번호는 SML 기준이다. / [L3a-34] CEID 번호는 SML 기준이다. STB 구성 여부는 사이트에 따라 다르다. Manual Order 화면 조작은 L1로 분리한다.

- **L3a-32 PIO Interlock 자동 복구 추적**
  - 내용: PIO Interlock 실패의 자동 복구 체계를 로그로 추적한다. 적재 실패: VehicleAcquireStarted(202) 이후 VehicleUnassigned(210) → TransferCompleted(107) ResultCode=64, CarrierLoc='SourcePort'이면 Once Retry로 S2F49가 재지령되고 TransferInitiated(108)부터 다시 시작한다. 하역 실패: VehicleDepositStarted(206) 이후 ResultCode=64, CarrierLoc='VHC UNIT NAME'(화물이 차량에 남음)이면 Once Retry로 Previous Destination에 재지령하고, 다시 실패하면 Destination='AbortLocation' 대체 명령을 낸다. AbortLocation까지 실패하면 UnitAlarmSet(CEID 504) 'All Port Loading Fail - Manual Handling'이 뜨고 차량은 CST를 실은 채 명령 없음 상태가 되므로, 자동 복구가 끝나 사람이 개입할 경계로 판정한다. 개입은 MCS 재지령 또는 TSC(OCS) Manual Transfer로 하며, 이때 CEID 254 CommandType='EQ_TRANSFER' → 108 → 204로 진행되는지 확인한다. OCS측 재시도는 6.1/6.2 RetryCountFromOrder/ToOrder(설정값+1회 시도)이고, 6.3 DeleteOrderWithJobFail=True일 때만 유효하다.
  - 할 수 있어야 하는 것: ResultCode=64와 CarrierLoc으로 적재/하역 실패를 구분하고, Once Retry → AbortLocation → Manual Handling 단계 중 현재 위치를 판정해 수동 개입 시점과 방법(MCS 재지령/OCS Manual Transfer)을 결정할 수 있다.
  - 근거: 3\_SFA\_VHC\_SCENARIO\_SPEC\_V3.5.pdf p.41~44, p.46(8.1~8.3, 9.2); 1\_SFA\_VHC\_BASIC\_SPEC\_V3.2.pdf p.28(VID 74 CommandType); OCS Parameter 매뉴얼 p.35(6.1~6.3)
- **L3a-33 BCR NG·UNKNOWN ID 추적**
  - 내용: BCR NG 3유형을 이벤트 조합으로 가른다: Failure(IDReadStatus=1, ResultCode=6), Duplicate(2, 4), Mismatch(3, 5). 흐름은 VehicleCarrierInstalled(153) → VehicleAcquireCompleted(203) → CarrierIDRead(251) → TransferCompleted(107) → VehicleCarrierRemoved(154, 원 ID 삭제) → VehicleCarrierInstalled(153, UNKNOWN ID)이다. UNKNOWN CarrierID 형식(UNKNOWN + EQPNAME + YYMMDDhhmmss + 1Sec/100000)으로 유령 카세트의 생성 시각·위치를 역추적한다. 이후 MCS가 AbortLocation으로 반송하는지 확인한다. SCAN 결과 8케이스(Mismatch: 251+152+151 / Duplicate: Removed 2+Installed 2 / Success / 빈 포트 케이스 / Fail 가정별)를 CEID 조합으로 역추적한다. Reading Station에서는 VehicleDepositCompleted·Carrier Installed·CarrierIDRead 순서가 바뀌어도 이상이 아님을 감안한다.
  - 할 수 있어야 하는 것: CEID 조합과 IDReadStatus/ResultCode로 BCR NG 유형을 판정하고, UNKNOWN CarrierID를 분해해 유령 카세트의 발생 시점과 경위를 추적할 수 있다.
  - 근거: 3\_SFA\_VHC\_SCENARIO\_SPEC\_V3.5.pdf p.16~19(2.6 SCAN), p.52~55(13.1~13.4), p.64(17.1)
- **L3a-34 Empty Retrieval·Double Storage 판정**
  - 내용: 이적재 이상을 TransferPaused(109) 이후 이벤트로 가른다. Empty Retrieval은 AcquireStarted(202) 이후 109가 오고, S2F41 ABORT 뒤 CarrierRemoved(152) → CarrierInstalled(151, UTB의 Unknown) → 103 → 101 → 210 순으로 진행된다. Double Storage는 DepositStarted(206) 이후 109가 오고, ABORT 뒤 CarrierRemoved 없이 CarrierInstalled(151)만 올라오며 → 103 → 101 → New Order S2F49 → 108로 진행된다. STB Double Storage는 2단 복구다: ① Vehicle을 다른 STB로 보내는 To Order ② Unknown Carrier를 ID 읽기 가능한 STB로 보내는 New Order. Host가 자동 생성하지 못하면 운전자가 OperationInitiatedAction(CEID 254)으로 Manual Order를 만든다.
  - 할 수 있어야 하는 것: TransferPaused 이후 이벤트 조합으로 Empty Retrieval과 Double Storage를 구분하고, STB Double Storage에서 Manual Order 생성이 필요한 시점을 결정할 수 있다.
  - 근거: 3\_SFA\_VHC\_SCENARIO\_SPEC\_V3.5.pdf p.59~62(15.1~15.4)

### L3a-13 취소·중단 식별·Controller 복구 검증

- **레벨**: L3  ·  **교육 방식**: 로그실습  ·  **탭**: 프로토콜  ·  **Section / Module**: Host Interface (HSMS) / SECS Deep-dive (Extended)  ·  **범위**: Extended
- **화면·도구**: SECS-II 로그 S6F11(254, 101~106, 154, 153, 208, 209) / TSC Transfer Command Delete / MCP CarrierRemoved / SECS-II 로그 / SECOMDRIVER 로그 / S1F3·S1F4
- **할 수 있어야 하는 것**: ① CEID 254 선행 여부, REPLACE 값, 후속 이벤트로 취소·중단의 유형과 주체(MCS/OCS 운전자/Vehicle Removed)를 식별하고, 3중 DB 정합성이 맞는지 판정할 수 있다. ② Controller 재기동(또는 Rose Failover) 후 SECS 로그로 복구 시퀀스를 재구성하고, 다운 전 명령이 모두 다시 보고되어 운전이 재개됐는지 검증할 수 있다.
- **표시**: 자료충돌
- **주의**: [L3a-35] CEID 번호는 SML 기준이다. 토글 조작 자체는 L1이다. / [L3a-36] 검증자 missing 항목이다. Rose Failover 직후 검증 맥락은 L3-b와 교차 평가할 수 있다. CEID 번호는 SML 기준이다.

- **L3a-35 Cancel·Abort 유형·주체 식별**
  - 내용: CEID 254 OperationInitiatedAction이 앞서는지로 취소 주체를 가린다. CommandType='CANCEL' 뒤에 106 → 104 → 210이 오면 OCS 운전자의 Transfer Command Delete이고, 254 없이 진행되면 MCS 취소이다. ABORT는 REPLACE 값과 후속 이벤트로 3유형을 구분한다: Normal(REPLACE=FALSE, 103 → 101, 이후 AbortLocation 대체 명령), Global Duplicate(REPLACE=TRUE, 154 원 ID 삭제 + 153 Unknown 생성 추가), FAIL(TransferAbortfailed 102, 이전 ACTIVE substate 복귀). Vehicle Removed(209)는 254 CommandType='ABORT', CarrierLoc='VHCUnitName' → 103 → 101이 연쇄되고, MCP CarrierRemoved 토글 → 154 → VehicleInstalled(208)로 이어진다. VHC·MCS·MCP 세 곳의 CST 정보가 모두 제거됐는지로 DB 정합성을 판정한다.
  - 할 수 있어야 하는 것: CEID 254 선행 여부, REPLACE 값, 후속 이벤트로 취소·중단의 유형과 주체(MCS/OCS 운전자/Vehicle Removed)를 식별하고, 3중 DB 정합성이 맞는지 판정할 수 있다.
  - 근거: 3\_SFA\_VHC\_SCENARIO\_SPEC\_V3.5.pdf p.33~36(6.2~6.5), p.56~58(14.1~14.3)
- **L3a-36 Controller Down→Up 복구 검증**
  - 내용: Controller 다운~복구를 SECS 로그로 재구성한다. 다운: EquipmentOFFline(CEID 1) → Separate.req. 복구: Select.req/rsp → S1F13/S1F14 → S1F17/S1F18 → OnlineRemote(CEID 3) → TSCAutoInitiated(54) → TSCPaused(56) → S2F31/32(시간 동기) → S1F3/F4(현황 재수집). 다운 전에 Transferring 1건과 Command Queuing 2건이 있었다면, 재기동 후 3건이 모두 다시 보고되는지와 Transferring(111) → MCS RESUME(HCACK 0x04 또는 0x07) → TSCAutoCompleted(53)까지 진행되는지 확인해 명령이 살아남았는지 검증한다. 누락된 명령이 있으면 MCS 재지령 대상으로 판정한다.
  - 할 수 있어야 하는 것: Controller 재기동(또는 Rose Failover) 후 SECS 로그로 복구 시퀀스를 재구성하고, 다운 전 명령이 모두 다시 보고되어 운전이 재개됐는지 검증할 수 있다.
  - 근거: 3\_SFA\_VHC\_SCENARIO\_SPEC\_V3.5.pdf p.48~49(10. VHC CONTROLLER DOWN → UP)

### L3a-14 거동 파라미터 튜닝·위험 판단

- **레벨**: L3  ·  **교육 방식**: 화면실습  ·  **탭**: System  ·  **Section / Module**: Parameters / Tuning (Extended)  ·  **범위**: Extended
- **화면·도구**: System>Parameter>12. Timeout / 16. VehicleControl / 17. VehicleEvent Param / Window>CommEvent / System>Parameter>13. Traffic Param 13.15 / 10. System Param 10.19 / ErrorList / System>Parameter>5. OrderControlParam / 12. Timeout / 13. Traffic / 16. VehicleControl / OHS CheckAllocPoint
- **할 수 있어야 하는 것**: ① 안전 관련 파라미터 쌍의 의존 관계와 해제 시 위험을 설명하고, 변경 요청을 받았을 때 짝 파라미터·차량 프로토콜 지원·충돌 위험을 확인해 승인 여부를 판단할 수 있다. ② Noway Timeout 발생 시 UnuseByStationPenaltyMSec 과대 설정을 원인 후보로 특정하고, 경로 소실을 부르는 Penalty·PassPoint 변경 요청의 위험을 판단할 수 있다. ③ 블로킹·우회·정체·재가속·정위치 실패 현상에 대해 조정할 파라미터와 방향(증감)을 근거와 함께 제시하고, 하드웨어 점검으로 에스컬레이션할 경계를 판단할 수 있다.
- **표시**: 사이트의존, 추정해석, 근거약함
- **주의**: [L3a-37] 검증자 fix8의 Prohibited-Ops Gate '안전 파라미터 해제' 대응 항목이다. 에러번호와 Interlock 사용 여부는 사이트·차량별로 다르다. / [L3a-38] 검증자 fix8의 'Max Penalty' 대응 항목이다. / Max Penalty→Noway Timeout 연결은 검증자 해석. 원문은 "경로를 찾지 못함"까지만 기재. / [L3a-39] 파라미터 기본값과 권장 범위 표가 없어(data_gaps) 수치 정답은 채점하지 않고 조정 방향과 트레이드오프만 평가한다. CheckAllocPoint는 설치 메모 1줄이 근거라 근거약함이다.

- **L3a-37 안전 파라미터 쌍 해제 위험**
  - 내용: 안전 기능을 끄거나 바꾸기 전에 짝 파라미터와 위험을 판단한다. 첫째, 12.10 NoOrderMovingVehicleTimeoutSec + 16.4 TxCancelWhenLoseWay는 명령 없이 움직이는 차량을 Wrong Way Stop으로 정지시키고 Comm Event에 'Vehicle Auto-NoOrder-Moving'을 남긴다. 끄면 차량 간 충돌 위험이 있다. 둘째, 16.6 ObstacleSensorDetectDistance + 17.2 ObstacleSensorErrorEvent(전방감지 에러번호, 차량 담당자 확인)는 16.12 AutoParkingDistance와 상호 영향이 있다. 셋째, 16.5 TxReleaseInterlock('R' Command) + 17.1 InterlockStopErrorCode이다. 짝이 없으면 값을 바꿔도 효과가 없다: 6.1/6.2↔6.3, 12.7↔16.9, 13.9/13.10↔13.14, 11.2~11.5↔11.1. 8.2, 15.1, 16.5, 16.7, 16.8, 16.11, 17.1은 Vehicle Protocol 지원을 확인하기 전에는 켜지 않는다.
  - 할 수 있어야 하는 것: 안전 관련 파라미터 쌍의 의존 관계와 해제 시 위험을 설명하고, 변경 요청을 받았을 때 짝 파라미터·차량 프로토콜 지원·충돌 위험을 확인해 승인 여부를 판단할 수 있다.
  - 근거: OCS Parameter 매뉴얼 p.35, p.38, p.51~52, p.56, p.57, p.68~69, p.71, p.83, p.86~92
- **L3a-38 경로 소실 위험 값 판단**
  - 내용: 13.15 UnuseByStationPenaltyMSec는 Station Unuse Point/Segment로 가는 경로에 Penalty를 더한다. Max 수치로 넣으면 경로를 찾지 못한다(Parameter 매뉴얼 13.15). ErrorList의 Noway Timeout으로 이어질 수 있으나 원문에 직접 연결 기재는 없다. 상한 전에 경로 존재를 확인하도록 판단한다. 10.19 PassPointReleaseInterlock은 ','로 구분한 포인트만 Pass 포인트 등록/해제를 허용하는 화이트리스트다. 미등록 포인트를 변경하려 하면 '해당 포인트는 PointType을 변경할 수 없습니다.' 팝업이 뜬다. 반송/이동경로에 영향을 주므로 최소화하는 값으로 다룬다.
  - 할 수 있어야 하는 것: Noway Timeout 발생 시 UnuseByStationPenaltyMSec 과대 설정을 원인 후보로 특정하고, 경로 소실을 부르는 Penalty·PassPoint 변경 요청의 위험을 판단할 수 있다.
  - 근거: OCS Parameter 매뉴얼 p.50(10.19), p.72(13.15)
- **L3a-39 경로·점유 거동 파라미터 튜닝**
  - 내용: 현상에 맞춰 거동 파라미터를 조정한다. Traffic Penalty: 13.2~13.6, 13.8(예: 5000 → 1번경로 10000+5000=15000 vs 2번 14000 → 2번 우회), 양방향 13.7 CollisionPenalty / 13.11 ToleranceWeight / 13.12 CheckLimitCollisionWeight, 분기·합류 13.16~13.19. 점유: 5.1 MaxAllocWeight(크면 Blocking 거리·반송시간 증가), 5.2 isSoonArriveWeight. 경로 재탐색: 5.13 FindPathLimitTime(짧으면 Core 부하 증가, 0=미사용). Alloc 해제·재송신: 12.7 WaitLimitTimeoutSec + 16.9 CheckVehicleAllocPoint. 감속 중 재가속 불가: OHS CheckAllocPoint(재전송을 빠르게). 정위치 실패: 16.1 MoveCreateCountForIStatus / 16.2 / 16.3 OnPointTolerance(1=0.1cm). 계속 실패하면 소프트웨어로 덮지 않고 차량 점검을 요청한다.
  - 할 수 있어야 하는 것: 블로킹·우회·정체·재가속·정위치 실패 현상에 대해 조정할 파라미터와 방향(증감)을 근거와 함께 제시하고, 하드웨어 점검으로 에스컬레이션할 경계를 판단할 수 있다.
  - 근거: OCS Parameter 매뉴얼 p.26, p.32, p.56, p.62~75, p.85, p.87; 01. RCP 최초설치 확인사항.txt 59~60행

### L3a-15 로그 기록량·디스크 용량 설정 조정

- **레벨**: L3  ·  **교육 방식**: 화면실습  ·  **탭**: System  ·  **Section / Module**: System Setup / Database  ·  **범위**: Core  ·  **교육 일차**: 2
- **화면·도구**: System>Parameter>2. Host Param / 3. Log Param / 8. Socket Param / 11. TaskMgrParam / System > Parameter > DataBaseParam / LogParam / SystemParam(HDDWarningSpaceGB)
- **할 수 있어야 하는 것**: ① 분석 목적에 필요한 디버깅·Packet·리소스 로그를 켜고 분석 후 원복하며, 차량 대수에 맞춰 로그 기록량과 MonitoredVehicle 전송 분할을 조정할 수 있다. ② HDD 여유 용량과 SQL 사양을 근거로 백업 주기·보존기간·PlayBack 삭제량 값을 산정·변경하고 그 영향(HDD 경고)을 예측할 수 있다.
- **표시**: 사이트의존, 자료충돌
- **주의**: [L3a-40] 어떤 파라미터가 32종 로그 중 어느 것을 켜는지 대응표가 없다(data_gaps). 어떤 상황에 어떤 디버깅 로그가 필요한지 아는 부분은 L2-c이다. / [L3a-41] HDDWarningSpaceGB 예시가 Parameter 매뉴얼 50 vs CPU_RAM_HDD 점검 캡처 5로 다름. 실가동 서버 변경은 승인 절차 하에서만

- **L3a-40 분석용 로그·기록량 조정**
  - 내용: 분석할 때만 켜고 끝나면 끄는 스위치를 다룬다. 3.1 LogTrafficData(주행), 3.2 LogRecvData(Order), 3.3 LogDebuggingData(디버깅, True일 때 Vehicle MasterStop 로그 저장), 8.9 WriteCommPacket(Comm Log에 Packet 기록, 용량 증가로 미사용 시 False)이 해당한다. 리소스 로깅은 11.1 UseTaskMgrLogging=True일 때 11.2 CheckResourceIntervalSec / 11.3·11.4 CPU·MemoryWarningLevel(기록 시작 %) / 11.5 NormalResourceCheckIntervalMin으로 켠다(10.5~10.16 알람용과 구분). 규모 조정 대상은 3.6 LogMaxMsgCount / 3.7 LogMaxWriteRowCount / 3.8 LogWriteInterval, 2.4 SendMonitoredVehicleTimeoutSec / 2.5 SendMonitoredVehicleMsgCount(0=전체 일괄, 2=2대씩)이며 Vehicle 대수에 맞춘다.
  - 할 수 있어야 하는 것: 분석 목적에 필요한 디버깅·Packet·리소스 로그를 켜고 분석 후 원복하며, 차량 대수에 맞춰 로그 기록량과 MonitoredVehicle 전송 분할을 조정할 수 있다.
  - 근거: OCS Parameter 매뉴얼 p.14~15, p.18, p.20, p.41, p.51~52, p.61
- **L3a-41 디스크 용량 관련 설정 조정**
  - 내용: DataBaseParam의 1.3 DBBackupPeriod('1'=1일+23:59:59 보관)·1.4 DBBackupInterval('1'=1시간, 0=사용안함)·1.5 DeleteRowsPlayBack·1.6 DeleteRowsInterval과 Log Param 3.10, 3.12~3.16 보존기간을 '사이트 규모·SQL 사양·HDD 용량'에 맞춰 조정한다. 백업 주기를 짧게 하거나 보존기간을 늘리면 드라이브 사용량이 증가해 10.17 HDDWarningSpaceGB(0=사용안함, 예: (사이트별 확인)) 알람으로 이어지는 인과를 근거로 변경 전후를 검증한다.
  - 할 수 있어야 하는 것: HDD 여유 용량과 SQL 사양을 근거로 백업 주기·보존기간·PlayBack 삭제량 값을 산정·변경하고 그 영향(HDD 경고)을 예측할 수 있다.
  - 근거: OCS Parameter 매뉴얼 p.11~12 (1.3~1.6); OCS Parameter 매뉴얼 p.21~24 (3.10, 3.12~3.16); OCS Parameter 매뉴얼 p.49 (10.17)

## L3-b Rose 서버 이중화

### L3b-01 Rose Console 상태 판정·Group 조작

- **레벨**: L3  ·  **교육 방식**: 도구실습  ·  **탭**: 외부도구  ·  **Section / Module**: Redundancy (Rose) / Rose Operation  ·  **범위**: Core  ·  **교육 일차**: 9
- **화면·도구**: RoseMirrorHA Control Center > 호스트명 우클릭 > Login / Console 상태 화면(Server·Group·Agent·NICs) / Rose Console > Group 우클릭 > Bring In(带入) / Bring Out(带出) / Force Start(强制启动) / Delete
- **할 수 있어야 하는 것**: ① Replace IP 환경에서 Heartbeat IP로 콘솔에 로그인하고, Server/Group/Agent/NICs 4요소를 읽어 '이중화 정상/비정상'과 그 근거 요소를 제시할 수 있다. ② Group 상태(Online/Offline, 한 노드 장애)가 주어지면 Bring In / Bring Out / Force Start 중 허용되는 명령을 골라 중문 UI에서 실행하고, Delete가 운영서비스 중지를 요구한다는 점을 들어 운영 중 사용 금지를 설명할 수 있다.
- **표시**: 민감정보, 사이트의존, 근거약함, 버전차이
- **주의**: [L3b-01] 매뉴얼 예시 계정(Administrator / 평문 PW)과 IP는 배포 시 삭제·마스킹. 4요소 각각의 정상 표시(색상·문구) 기준은 매뉴얼에 스크린샷으로만 있어 현장 캡처로 판정표를 보강해야 함. 4요소 위치를 아는 것만 묻는다면 L2-c로 쪼갤 수 있음. / [L3b-02] 중문 UI는 현장 캡처(단독 실행 매뉴얼 내장 이미지) 1건에만 있음. 进入离线维护/退出离线维护·中止·链路配置·远程关机配置의 영문 매뉴얼 대응 기능은 자료에 없어 대응표를 새로 만들어야 함(검증자 data_gaps). Delete는 '존재만 알고 손대지 않는다'로 평가.

- **L3b-01 Console 접속·상태 판정**
  - 내용: Windows 시작 >> 모든 프로그램 >> RoseMirrorHA >> Control Center로 콘솔을 띄우고, 트리의 호스트명(예: RoseMirror01)을 우클릭 > Login 해서 Username/Password(사이트별 확인)로 로그인한다. Replace IP를 쓰는 환경에서는 운영서비스 Real IP가 Virtual IP로 바뀌므로 Login IP를 Heartbeat IP로 바꿔 접속하고, 운영서버 원격 접근은 Virtual IP로 한다. 접속 후 Server 상태 / Group 상태 / Agent 통신 / NICs 상태 4요소로 이중화 정상 여부를 판정한다.
  - 할 수 있어야 하는 것: Replace IP 환경에서 Heartbeat IP로 콘솔에 로그인하고, Server/Group/Agent/NICs 4요소를 읽어 '이중화 정상/비정상'과 그 근거 요소를 제시할 수 있다.
  - 근거: \_MANUAL\_RoseMirrorHA\_운영가이드\_Windows\_\_v01\_20200316\_김연수.pdf p.6~9, p.62~63
- **L3b-02 Group 기동·정지·강제기동**
  - 내용: Group 우클릭 메뉴로 Bring In(带入: 서비스 미제공 상태에서만 Resources Online), Bring Out(带出: Group Online 상태에서만 가능하며 곧 운영서비스 정지), Force Start(强制启动: 정상 Bring In 불가 + Active/Standby 중 한 노드만 운영 가능할 때만, 정상 시 메뉴 비활성)를 조작한다. Delete는 운영서비스를 중지해야만 가능하므로 운영 중에는 쓰지 않는다. 현장 중문 메뉴 순서 带入 / 带出 / 进入离线维护·退出离线维护 / 中止 / 强制启动 / 切换 / 数据 / 资源 / 修改·查看 / 链路配置 / 心跳状态 / 远程关机配置를 영문 명령에 대응시킨다.
  - 할 수 있어야 하는 것: Group 상태(Online/Offline, 한 노드 장애)가 주어지면 Bring In / Bring Out / Force Start 중 허용되는 명령을 골라 중문 UI에서 실행하고, Delete가 운영서비스 중지를 요구한다는 점을 들어 운영 중 사용 금지를 설명할 수 있다.
  - 근거: \_MANUAL\_RoseMirrorHA\_운영가이드\_Windows\_\_v01\_20200316\_김연수.pdf p.21~22, p.25~30; Server Independent Execution Manual\_240518.pptx 슬라이드 2 내장 이미지

### L3b-02 수동 절체·역절체·서비스 검증

- **레벨**: L3  ·  **교육 방식**: 도구실습  ·  **탭**: 외부도구  ·  **Section / Module**: Redundancy (Rose) / Rose Operation  ·  **범위**: Core  ·  **교육 일차**: 9
- **화면·도구**: Rose Console > Group 우클릭 > Fail Over / Take Over (현장: 切换) / VIP로 RCP UI 접속 / Report > FailOverHistory / SECS(HSMS) 로그
- **할 수 있어야 하는 것**: ① 복제 정상을 확인한 뒤 수동 절체를 실행하고, 절체 후 서비스를 확인한 다음 역절체로 원래 Active 노드에 서비스를 되돌릴 수 있다. ② 절체 직후 VIP로 RCP UI 접속 여부와 FailOverHistory 기록을 확인해 서비스가 새 Active 노드로 정상 인계됐는지 판정하고, 반송 명령 생존 검증(L3a-13)이 필요한지 결정할 수 있다.
- **표시**: 근거약함, 자료충돌, 추정해석, 사이트의존
- **주의**: [L3b-03] Fail Over와 Take Over의 차이가 매뉴얼에 구분 설명되지 않음. 운영 서버 절체는 라인 영향이 있으므로 테스트 서버 2노드 실습 또는 참관으로 대체(검증자 open_questions). / [L3b-04] C211(FailOverHistory)·C392(Controller Down→Up)는 다른 버킷 후보를 검증자 missing 지적에 따라 연결함. FailOverHistory는 v04본 10.17·MXA본 9.19 근거. C392는 VHC Controller 재기동 시나리오이며 Rose Failover에 그대로 적용된다는 것은 검증자 해석(추정). CEID 번호대는 BASIC SPEC과 RCP setup 가이드가 충돌하므로 사이트 상위 기준으로 확인.

- **L3b-03 수동 절체·역절체**
  - 내용: Online된 Group을 우클릭 > Fail Over 또는 Take Over(현장 切换)로 Active node에서 Standby node로 소유권을 넘긴다. 실행 전에 복제 정상 완료를 확인하고, 실행 후 Standby node에서 서비스가 정상인지 본다. Active-Standby 간 Performance가 다르면 Failover/Takeover를 한 번 더 실행해 서비스를 원래 Active node로 되돌린다.
  - 할 수 있어야 하는 것: 복제 정상을 확인한 뒤 수동 절체를 실행하고, 절체 후 서비스를 확인한 다음 역절체로 원래 Active 노드에 서비스를 되돌릴 수 있다.
  - 근거: \_MANUAL\_RoseMirrorHA\_운영가이드\_Windows\_\_v01\_20200316\_김연수.pdf p.23~24, p.55
- **L3b-04 Failover 후 서비스 검증**
  - 내용: Failover가 일어난 뒤 HA 점검 4번대로 VIP 주소로 RCP UI 접속이 되는지 확인한다(Web Config의 DB 접속 IP를 DB Server IP로 등록했다는 전제). 이어 OCS Report > FailOverHistory의 DATETIME / MODULE / COMMENT(서버명칭, Program 명칭, FailOver 원인, 결과 값)로 어느 Program이 언제 왜 넘어갔는지 확인한다. 진행 중이던 반송 명령이 살아남았는지는 SECS 로그의 Controller Down→Up 재접속 시퀀스로 판정하며, 그 판독은 L3a-36에서 평가한다.
  - 할 수 있어야 하는 것: 절체 직후 VIP로 RCP UI 접속 여부와 FailOverHistory 기록을 확인해 서비스가 새 Active 노드로 정상 인계됐는지 판정하고, 반송 명령 생존 검증(L3a-13)이 필요한지 결정할 수 있다.
  - 근거: 01. RCP 최초설치 확인사항.txt 44행; RCP Program setup 가이드 p.27 본문 P259; OCS 사용자 매뉴얼\_v04\_210114.pdf p76 (FailOverHistory); 3\_SFA\_VHC\_SCENARIO\_SPEC\_V3.5.pdf p.48~49 (10. VHC CONTROLLER DOWN → UP)

### L3b-03 Replication·Snapshot 관리·복구

- **레벨**: L3  ·  **교육 방식**: 도구실습  ·  **탭**: 외부도구  ·  **Section / Module**: Redundancy (Rose) / Rose Operation  ·  **범위**: Core  ·  **교육 일차**: 9
- **화면·도구**: Rose Console > Group 우클릭 > Full Mirror / Verify / Transmit / Target Write Disk / Rose Console > Group 우클릭 > Snapshot > Take Snapshot / Scheduling Snapshot / Snapshot Manage / Rose Console > Group 우클릭 > Snapshot > Recover Snapshot
- **할 수 있어야 하는 것**: ① Full Mirror·Verify를 실행하고 진행률을 읽으며, Transmit 색상(녹색/노란색)과 Target Side Pause 표시로 복제가 정상인지 일시중지인지 판정하고 Resume으로 되돌릴 수 있다. ② 작업 전 수동 스냅샷을 생성하고, 스케줄·저장 한도를 확인·변경하며, Snapshot Manage에서 DELETE만 사용하고 REVERT를 쓰지 않을 수 있다. ③ Downtime 승인을 전제로 Recover Snapshot 마법사를 끝까지 진행하면서 Recover Mode를 매뉴얼 지시대로(Compare file content 선택, Recover to specified path 해제) 설정하고, 5개 옵션 각각의 매뉴얼 정의를 말할 수 있다.
- **표시**: 사이트의존
- **주의**: [L3b-05] 매뉴얼 목차의 'Replication : Select Source'는 상세 슬라이드가 없어 제외. / [L3b-06] Interval·저장 한도는 사이트 설정값. REVERT 금지 사유는 매뉴얼에 설명이 없음. / [L3b-07] 운영 서버에서는 실습 불가. 테스트 서버에서만 실습.

- **L3b-05 Replication 조작·판독**
  - 내용: Group 우클릭으로 Full Mirror(Replication Data 전체 재복제, Start/Stop/Pause/Resume, 진행률 Mirror(43%) 형태), Verify(Active·Standby Data 정합성 확인, Start/Stop, 진행률 Verifying(45%) 형태), Transmit(Replication Area 변경분을 Standby로 전달, Pause/Resume, 정상 녹색 / 일시중지 노란색), Target Write Disk(Standby의 Replication Area Write 일시중지, Pause/Resume, Target Side Pause 상태 변화)를 조작한다.
  - 할 수 있어야 하는 것: Full Mirror·Verify를 실행하고 진행률을 읽으며, Transmit 색상(녹색/노란색)과 Target Side Pause 표시로 복제가 정상인지 일시중지인지 판정하고 Resume으로 되돌릴 수 있다.
  - 근거: \_MANUAL\_RoseMirrorHA\_운영가이드\_Windows\_\_v01\_20200316\_김연수.pdf p.32~39
- **L3b-06 Snapshot 생성·스케줄·관리**
  - 내용: Group 우클릭 > Snapshot > Take Snapshot으로 위험 작업 전 수동 스냅샷을 만들고 성공 팝업을 확인한다. Snapshot > Scheduling Snapshot에서 Snapshot Interval을 Day / Hour / Minute 단위로 지정하고(매뉴얼 예시 10분, 사이트별 확인) Snapshot Storage Setting에서 최대 저장 크기를 지정한다(Default 해당 Volume의 10%). Snapshot > Snapshot Manage에서 DELETE로 선택한 Snapshot을 삭제하되, REVERT는 매뉴얼상 '절대 사용 금지'다.
  - 할 수 있어야 하는 것: 작업 전 수동 스냅샷을 생성하고, 스케줄·저장 한도를 확인·변경하며, Snapshot Manage에서 DELETE만 사용하고 REVERT를 쓰지 않을 수 있다.
  - 근거: \_MANUAL\_RoseMirrorHA\_운영가이드\_Windows\_\_v01\_20200316\_김연수.pdf p.41~47
- **L3b-07 Recover Snapshot 복구**
  - 내용: Snapshot > Recover Snapshot은 운영서비스 중지(Downtime)가 반드시 필요하며, 진행하면 Group이 Bring Out 된다. 복구할 Node / 복구시점 / 복구 Data를 차례로 고른다. Recover Mode 화면에서는 복구 방식 3개 중 하나(Compare file property=파일 속성 비교 / Compare file content=파일 내용 비교 / Sync the whole file=전체 파일 복구)를 고르고, 체크박스 2개(Bring in after finishing recovery=복구 후 Group Bring in / Recover to specified path=복구할 위치 지정)를 정한다. 매뉴얼 지시는 'Compare file content 선택, Recover to specified path는 Uncheck'다(캡처상 Bring in after finishing recovery도 미체크). Finish를 누르면 '기존의 Data는 모두 삭제된다'는 경고가 뜨고, 이를 확인한 뒤 진행한다.
  - 할 수 있어야 하는 것: Downtime 승인을 전제로 Recover Snapshot 마법사를 끝까지 진행하면서 Recover Mode를 매뉴얼 지시대로(Compare file content 선택, Recover to specified path 해제) 설정하고, 5개 옵션 각각의 매뉴얼 정의를 말할 수 있다.
  - 근거: \_MANUAL\_RoseMirrorHA\_운영가이드\_Windows\_\_v01\_20200316\_김연수.pdf p.48~53

### L3b-04 계획 작업·Rose 전제 조건 점검 (포트·미러 경로)

- **레벨**: L3  ·  **교육 방식**: 현장점검  ·  **탭**: 서버  ·  **Section / Module**: Redundancy (Rose) / Rose Maintenance (Extended)  ·  **범위**: Extended
- **화면·도구**: Rose Console(Bring Out / Bring In / Verify / Failover) + services.msc(SQL Server 서비스) / Windows Firewall Inbound 규칙 / 보안솔루션 예외 등록 / Server Manager > NIC Teaming / SSMS > DB 우클릭 > 속성 > 파일 / Server 우클릭 > 속성 > 데이터베이스 설정 / Sp_helpfile / StandBy 서버 미러디스크
- **할 수 있어야 하는 것**: ① Windows Update와 DB Patch 작업에서 Downtime 필요 여부를 가르고, 각 절차를 순서대로 수행하며 절체·Verify를 넣어야 하는 지점을 지목할 수 있다. ② Failover 미동작 상황에서 보안솔루션·방화벽의 Rose 포트 5개와 설치 경로·프로세스 등록을 점검해 누락 항목을 찾아 시정하고, 매뉴얼 프로세스명과 현장 서비스명을 대조할 수 있다. ③ Sp_helpfile과 SSMS 속성으로 DB 파일이 미러링 경로에 있는지 판정하고, StandBy 미러디스크 접근 시험으로 이중화가 실제로 걸렸는지 판정할 수 있다.
- **표시**: 사이트의존, 자료충돌
- **주의**: [L3b-10] C289(NIC Teaming)는 다른 버킷 후보를 검증자 missing(Rose 통신 전제 설정)에 따라 연결함. 매뉴얼 프로세스명(MirrorHAService.exe 등)과 현장 services.msc 서비스명(RoseHAService/RoseMirrorService 등, C071 참조)이 달라 현장 실명으로 등록 여부를 확인해야 함. 보안 설정 성격이 있어 AUX와 겹침. / [L3b-11] 미러링 대상 볼륨·폴더 경로가 Rose 그룹에 어떻게 등록돼 있는지 보여주는 구성 문서는 없음. 이중화와 DB 경로의 관계 설명만 묻는다면 L2-b로 쪼갤 수 있음.

- **L3b-08 계획 작업(Update·Patch)**
  - 내용: Windows Update는 Downtime을 최소화하는 순서로 한다. 1) Standby node Update 2) Standby 재시작 3) 복제 정상 완료 확인 4) Group Failover/Takeover 5) Standby에서 서비스 확인 6) Active node Update·재시작 7) 복제 정상 완료 확인 8) Standby에서 운영을 계속하거나, Performance가 다르면 한 번 더 절체해 원래 Active로 되돌린다. MSSQL/Oracle Patch(Service Pack)는 Downtime이 필요하며 1) Group Bring Out 2) 양 node에 Patch 동시 실행 3) Windows Service에서 자동 시작된 SQL/Oracle Service를 관리자가 중지 4) Group Bring In·정상 확인 5) Data verify 완료 후 Failover/Takeover 6) 운영서비스 확인 순서로 진행한다.
  - 할 수 있어야 하는 것: Windows Update와 DB Patch 작업에서 Downtime 필요 여부를 가르고, 각 절차를 순서대로 수행하며 절체·Verify를 넣어야 하는 지점을 지목할 수 있다.
  - 근거: \_MANUAL\_RoseMirrorHA\_운영가이드\_Windows\_\_v01\_20200316\_김연수.pdf p.55, p.57
- **L3b-10 Rose 통신 전제 점검**
  - 내용: 절체가 안 되면 Rose 통신 전제부터 점검한다. 보안솔루션 예외와 Windows Firewall Inbound 규칙에 RoseMirrorHA 포트 TCP/UDP 7330, 3000, 3001, 3002, 7320이 열려 있는지 확인한다. 설치 경로 C:\Program Files\MirrorHA와 프로세스 MirrorHAService.exe, MirrorService.exe, MirrorMonitor.exe가 등록돼 있는지도 확인한다(Inbound port와 process 동일 설정). 매뉴얼 프로세스명과 현장 services.msc 서비스명(RoseHAService/RoseMirrorService 등)이 다르므로 현장 실명으로 대조한다. 관리자가 Rose 서비스를 중지하면 운영서비스도 같이 멈추므로, 서비스 재기동이 필요하면 엔지니어에게 요청해 진행한다. 서버 NIC Teaming 설정은 AUX-14에서 다룬다.
  - 할 수 있어야 하는 것: Failover 미동작 상황에서 보안솔루션·방화벽의 Rose 포트 5개와 설치 경로·프로세스 등록을 점검해 누락 항목을 찾아 시정하고, 매뉴얼 프로세스명과 현장 서비스명을 대조할 수 있다.
  - 근거: \_MANUAL\_RoseMirrorHA\_운영가이드\_Windows\_\_v01\_20200316\_김연수.pdf p.64; RCP Program setup 가이드 p.47 (기타 > Teaming Setting) 본문 P474~498
- **L3b-11 DB 미러링 경로 점검**
  - 내용: DB가 미러링 경로에 없으면 Failover가 정상 동작하지 않는다. SSMS > DB 우클릭 > 속성 > 파일 탭에서 DB 파일 위치를, Server 우클릭 > 속성 > 데이터베이스 설정에서 기본 경로를 보고, 쿼리 `Use \<DB_Name> Go Sp_helpfile go`로 경로를 확인한다. 설치 단계에서는 OCS 설치 기준서 2.3.1 7-1)의 '(옵션) server 이중화 구성 시 Data root directory 경로 변경'대로 미러링 경로(예: D 드라이브, 사이트별 확인)로 바꿔야 한다. HA 점검 3번대로 StandBy 서버에서 미러디스크 접근·수정이 안 되는지 확인하고, 접근이 된다면 이중화가 걸려 있지 않다고 판정한다.
  - 할 수 있어야 하는 것: Sp_helpfile과 SSMS 속성으로 DB 파일이 미러링 경로에 있는지 판정하고, StandBy 미러디스크 접근 시험으로 이중화가 실제로 걸렸는지 판정할 수 있다.
  - 근거: RCP Program setup 가이드 p.22 (3.4 SQL DB 경로 및 메모리 사용량 확인) 표10·11, 본문 P208~215; OCS 설치 기준서 p.8 (2.3.1 절차 7-1); 01. RCP 최초설치 확인사항.txt 43행

### L3b-05 장애 유형별 판정·대처

- **레벨**: L3  ·  **교육 방식**: 이론  ·  **탭**: 외부도구  ·  **Section / Module**: Redundancy (Rose) / Rose Operation  ·  **범위**: Core  ·  **교육 일차**: 9
- **화면·도구**: RoseMirrorHA Console(Server·Group·NICs 상태, Log 영역) / ncpa.cpl(Host, Heartbeat, Mirror) / Windows 서버 콘솔
- **할 수 있어야 하는 것**: 장애 노드(Active/Standby)와 장애 망(Public/Heartbeat/Mirror), OS Hang 여부가 주어지면 Failover 발생 여부와 운영 영향을 판정하고 1차 조치(강제종료·강제 재시작·Mirror 망 복구 우선)를 결정할 수 있다.
- **표시**: 근거약함
- **주의**: C094(재시작 정책)·C070(Console Log)은 다른 버킷 후보를 판정 근거로 함께 연결함. Rose 로그의 실제 경로·파일명과 Heartbeat 타임아웃 등 판정 수치는 자료에 없음(검증자 data_gaps). 노드·망별 영향을 설명만 하는 문항은 L2-b로 쪼갤 수 있음.

- **교육 내용**
  - 내용: Server 장애: Active node에서 예기치 않은 종료나 실수로 Shutdown/Restart가 나면 Standby로 Failover되고, Standby에서 나면 운영 영향이 없다. NIC 장애: Active Public 장애는 Failover, Standby Public 장애는 영향 없음, Heartbeat 장애는 어느 노드든 운영 영향 없음, Mirror 장애는 운영 영향은 없지만 복제가 막히므로 조속히 복구한다. OS Hang up: Active에서 나면 운영서비스를 강제종료해 Failover를 유도하고, Standby에서 나면 그대로 두면 이후 Failover가 불가능하므로 강제 재시작해 대기 상태로 만든다. 운영 필수 서비스(SQL/Oracle) 장애는 reset timeout 안에서 정해진 횟수만큼 재시작하고 넘으면 Failover한다(Default 3600s까지 3회). 콘솔 Log 영역에서 동작·이벤트를 조회한다.
  - 근거: \_MANUAL\_RoseMirrorHA\_운영가이드\_Windows\_\_v01\_20200316\_김연수.pdf p.10, p.59~60

### L3b-06 서버 단독 실행·이중화 복귀

- **레벨**: L3  ·  **교육 방식**: 도구실습  ·  **탭**: 서버  ·  **Section / Module**: Redundancy (Rose) / Rose Maintenance (Extended)  ·  **범위**: Extended
- **화면·도구**: Rose Console > Group(IMS) 우클릭 > 带出 / services.msc / ncpa.cpl / D:\Program\Core·MCS_IF·PLCDRIVER / services.msc / ncpa.cpl / Rose Console > Group 우클릭 > Bring In(带入) / Full Mirror / Verify
- **할 수 있어야 하는 것**: ① 단독 실행 5단계를 순서대로 수행하고, 단계를 빠뜨리거나 단계 순서를 바꿨을 때 생기는 결과(서비스 정지, DB 미기동, IP 미할당)를 말할 수 있다. 프로그램 기동은 Core를 먼저 띄웠는지만 채점한다. ② 단독 실행 상태에서 이중화로 되돌리는 역순 절차를 단계별로 제시하고, 단계마다 근거 문서가 있는지 없는지 구분하며, 복귀 후 Verify로 복제 정합성을 확인할 수 있다.
- **표시**: 사이트의존, 민감정보, 근거약함, 추정해석, 자료없음
- **주의**: [L3b-12] 노드명 AGV03/AGV04, 그룹명 IMS, NIC 이름(BMS/Heartbeat/Host/iDRAC_Don't-Use/Local01/Mirror/Spare), 캡처 IP는 사이트 값이라 역할명으로 치환하고 IP는 마스킹. 폴더명은 매뉴얼마다 McsIF·PlcDrv / MCS_IF·PLCDRIVER로 다르니 현장 경로를 확인. / [L3b-13] 원복 절차서가 어느 자료에도 없음. 골격은 검증자 제시안 — 현업 인터뷰 + 테스트 서버 검증으로 절차서를 먼저 만들어야 평가 가능.

- **L3b-12 서버 단독 실행**
  - 내용: 이중화를 믿을 수 없을 때 쓰는 최후 수단이다. 1) Rose Console에서 Group(현장 IMS, 노드 AGV03/AGV04)을 带出(Bring Out)해 리소스를 내린다. 2) Windows key + R > services.msc에서 RoseHAService, RoseMirrorService를 양 서버 모두 Stop 한다(Rose 서비스를 중지하면 운영서비스도 같이 멈추므로 임의로 하지 않고 엔지니어 요청·승인 후 진행). 3) 단독 운영 서버에서 SQL Server(MSSQLSERVER), SQL Server Agent(MSSQLSERVER)를 Start 한다(Startup Type Manual). 4) ncpa.cpl > Host, Local01 어댑터 > Internet Protocol Version 4(TCP/IPv4) > Properties에 Service IP를 수동 입력한다(값은 사이트별 확인). 5) D:\Program\Core\Core.exe를 먼저 기동하고, 이어서 D:\Program\MCS_IF\MCS_IF.exe와 D:\Program\PLCDRIVER\PlcDriver.exe를 기동한다(둘 사이 순서는 무관).
  - 할 수 있어야 하는 것: 단독 실행 5단계를 순서대로 수행하고, 단계를 빠뜨리거나 단계 순서를 바꿨을 때 생기는 결과(서비스 정지, DB 미기동, IP 미할당)를 말할 수 있다. 프로그램 기동은 Core를 먼저 띄웠는지만 채점한다.
  - 근거: Server Independent Execution Manual\_240518.pptx 슬라이드 2~11 (+내장 이미지); \_MANUAL\_RoseMirrorHA\_운영가이드\_Windows\_\_v01\_20200316\_김연수.pdf p.64 (Service 중지 주의사항)
- **L3b-13 단독 실행 후 이중화 복귀**
  - 내용: 자료에는 단독 실행으로 내려가는 절차만 있고 이중화 복귀(원복) 절차는 없다. 근거가 있는 조각은 다음과 같다. 양 서버 동시 OFFLINE 시 온라인 전환은 수동이다(HA 점검 5번). Bring In 전에는 자동 시작된 SQL Service를 관리자가 중지해야 한다(DB Patch 절차). Group Bring In은 서비스 미제공 상태에서만 가능하다. 복귀 뒤에는 Full Mirror / Verify로 정합성을 확인한다. 이 조각들을 단독 실행의 역순(OCS 프로그램 종료 → SQL 서비스 중지 → NIC 수동 IP 원복 → RoseHAService/RoseMirrorService 기동 → Group Bring In → Verify)에 맞춘 골격은 검증자가 제시한 안이며, 현업 인터뷰와 테스트 서버 검증으로 확정해야 한다.
  - 할 수 있어야 하는 것: 단독 실행 상태에서 이중화로 되돌리는 역순 절차를 단계별로 제시하고, 단계마다 근거 문서가 있는지 없는지 구분하며, 복귀 후 Verify로 복제 정합성을 확인할 수 있다.
  - 근거: 후보 없음 — 검증자 지적 (Rose 단독 실행 후 이중화 복귀 절차 부재); 01. RCP 최초설치 확인사항.txt 45행; \_MANUAL\_RoseMirrorHA\_운영가이드\_Windows\_\_v01\_20200316\_김연수.pdf p.21~22, p.32~35, p.57

## L3-c RailTool layout 업데이트

### L3c-01 차량 제원·Safety Margin 설정과 영향

- **레벨**: L3  ·  **교육 방식**: 도구실습  ·  **탭**: 외부도구  ·  **Section / Module**: Map & Traffic Control / Auto-Blocking  ·  **범위**: Core  ·  **교육 일차**: 6
- **화면·도구**: RailDesignTool > Steer Drive Vehicle(s) Configuration / Differential Drive / QUAD 설정창 (Length, Width, Rear·Front detection distance, Reference Point, Lock/Release) / RailDesignTool > Setup > Layout > [Auto-Blocking Configuration] / Drawing Attributes > Auto Blocking Configuration > General > Safety Margin
- **할 수 있어야 하는 것**: ① 제시된 제원 변경(예: Length 또는 Front detection distance 증가)이 Swept·오토블로킹 결과에 주는 영향을 설명하고, 변경 후 재계산·재검증 절차를 수행할 수 있다. ② Safety Margin 값을 변경해 오토블로킹을 재계산하고, 변경 전후의 블로킹 결과 차이를 확인할 수 있다.
- **표시**: 사이트의존
- **주의**: [L3c-01] 신규 사이트 마법사에서 값을 입력하는 단순 조작은 L2-a이고, 이 항목은 기존 사이트 제원 변경의 영향 판단만 다룬다. 예시값 600/300/10/10/300은 매뉴얼 예시라 사이트별로 확인해야 한다. / [L3c-02] 예시값 0은 매뉴얼 캡처값이라 운영값은 사이트별로 확인해야 한다. 값을 키우면 블로킹 범위가 넓어진다는 방향성은 매뉴얼에 명시되지 않았으니 실습 결과로 확인시켜라.

- **L3c-01 차량 제원 변경 영향 판단**
  - 내용: Steer Drive / Differential Drive / QUAD Vehicle(s) Configuration의 SD1·SD2 탭마다 Vehicle Name, Vehicle size Length(예 600)·Width(예 300), Rear detection distance(예 10), Front detection distance(예 10), Reference Point(예 300, 기본은 길이의 1/2, Lock/Release로 변경)를 입력한다. 값은 모두 사이트별로 확인한다. 기존 사이트에서 이 값을 바꾸면 Swept와 오토블로킹 범위가 달라지므로, 변경 사유를 확인하고 변경 후 Auto Blocking 재계산까지 수행해야 한다.
  - 할 수 있어야 하는 것: 제시된 제원 변경(예: Length 또는 Front detection distance 증가)이 Swept·오토블로킹 결과에 주는 영향을 설명하고, 변경 후 재계산·재검증 절차를 수행할 수 있다.
  - 근거: 24-02-RailDesignTool-Manual.pdf p.12~14
- **L3c-02 Safety Margin 설정**
  - 내용: Setup > Layout > [Auto-Blocking Configuration]에서 Drawing Attributes 창의 Auto Blocking Configuration 탭 > General > Safety Margin(예시 0)을 연다. 매뉴얼은 이 값을 '오토블로킹 계산 파라메터'라고 설명하며, 이 값을 바꾸면 계산되는 블로킹 범위가 달라진다. 값을 바꾼 뒤에는 Auto Blocking을 재계산하고 Segment Blocking Segment 결과를 변경 전과 대조한다.
  - 할 수 있어야 하는 것: Safety Margin 값을 변경해 오토블로킹을 재계산하고, 변경 전후의 블로킹 결과 차이를 확인할 수 있다.
  - 근거: 24-02-RailDesignTool-Manual.pdf p.29, p.7

### L3c-02 오토블로킹 생성·Swept 검증·계산로그 판독

- **레벨**: L3  ·  **교육 방식**: 도구실습  ·  **탭**: 외부도구  ·  **Section / Module**: Map & Traffic Control / Auto-Blocking  ·  **범위**: Core  ·  **교육 일차**: 6
- **화면·도구**: RailDesignTool > 사이트 우클릭 > Auto Blocking (Progress Unit, Start Auto-Blocking List Creation, Point Swept, Segment Swept, Show All, Clear, View Logs, Export, Cancel) / RailDesignTool > Auto-Blocking / Export JSON File 로그 창, View Logs > 'Segment Blocking Segment' 목록
- **할 수 있어야 하는 것**: ① Auto Blocking 창에서 Progress Unit의 의미를 말하고 값을 정해 오토블로킹 목록을 생성한 뒤, 지정된 Point/Segment의 Swept를 띄워 궤도 유형을 식별하고, 인접 궤도와의 겹침으로 블로킹 결과의 타당성을 판정할 수 있다. ② 오토블로킹 계산 로그에서 중단된 단계를 짚어내고, View Logs 결과에서 지정 세그먼트의 블로킹 대상 세그먼트를 찾아낼 수 있다.
- **표시**: 추정해석, 근거약함
- **주의**: [L3c-04] RDT 도구 로그라 OCS 운영 로그(L3-a)와 구분한다. 세그먼트 간 교차검사의 시작 문구(Vehicle Swept)와 완료 문구(Vehicle Track)가 다르게 찍히는 것은 원문 그대로다.

- **L3c-03 오토블로킹 생성·Swept 검증**
  - 내용: 사이트 네비게이션 트리에서 사이트를 우클릭해 Auto Blocking 창을 연다. Progress Unit(매뉴얼 정의: 차량 궤도의 차량 이동 단위, 예 5 mm — Export JSON File 창에도 같은 필드가 있다)을 정하고 'Start Auto-Blocking List Creation'으로 오토블로킹 정보를 생성한다. Point Swept에 포인트 아이디(예 1376)를 넣고 Enter를 치면 그 포인트 위치의 차량 궤도가 표시·숨김된다. Segment Swept에 세그먼트 아이디(예 2176)를 넣고 Enter를 치면 세그먼트를 지나며 계산 단위(Progress Unit)마다 이동한 차량 궤도가 표시·숨김된다. Show All / Clear로 전체 표시와 지우기를 한다. 필요하면 Tool > Swept > Show All Swept / Hide All Swept나 View > Drawing > [Swept]로 궤도 5종(SD Forward / Diff Forward / 2\*SD → Diff Forward / Crabwise Forward / Diff → 2\*SD Forward)을 함께 띄운다. 그 상태에서 인접 세그먼트·포인트 궤도와의 겹침을 보고 생성된 블로킹 결과가 타당한지 검증한다.
  - 할 수 있어야 하는 것: Auto Blocking 창에서 Progress Unit의 의미를 말하고 값을 정해 오토블로킹 목록을 생성한 뒤, 지정된 Point/Segment의 Swept를 띄워 궤도 유형을 식별하고, 인접 궤도와의 겹침으로 블로킹 결과의 타당성을 판정할 수 있다.
  - 근거: 24-02-RailDesignTool-Manual.pdf p.36, p.8; 24-02-RailDesignTool-Manual.pdf p.35, p.36; 24-02-RailDesignTool-Manual.pdf p.26, p.6, p.7, p.9
- **L3c-04 오토블로킹 계산로그 판독**
  - 내용: 계산 로그는 'Start Calculation .........' → 'Start Vehicle Swept Calculation / Vehicle Swept Calculation Complete' → 'Start Vehicle Swept Intersection Check for Each Point and Segment / … Complete' → 'Start Vehicle Swept Intersection Check for Each Segment / Vehicle Track Intersection Check for Each Segment Complete' → 'Calculation Complete!!!!' 순서로 찍힌다. 로그로 몇 단계까지 완료됐는지 판정하고, View Logs의 'Segment Blocking Segment' 목록에서 특정 세그먼트를 블로킹하는 세그먼트를 찾는다.
  - 할 수 있어야 하는 것: 오토블로킹 계산 로그에서 중단된 단계를 짚어내고, View Logs 결과에서 지정 세그먼트의 블로킹 대상 세그먼트를 찾아낼 수 있다.
  - 근거: 24-02-RailDesignTool-Manual.pdf p.35, p.36

### L3c-03 Export JSON·MapLoad 반영·백업

- **레벨**: L3  ·  **교육 방식**: 도구실습  ·  **탭**: 외부도구  ·  **Section / Module**: Map & Traffic Control / Map Deployment  ·  **범위**: Core  ·  **교육 일차**: 6
- **화면·도구**: RailDesignTool > 사이트 우클릭 > Export Json File / 'Export JSON File' 창 (Json File, Search, Progress Unit, Start Auto-Blocking List Creation, Export, Cancel) / OCS Layout > MapLoad (맵 파일 선택, BackupPath, UPDATE) — 다른 표기: System -> MapLoad, Core > System 탭 > MabLoad
- **할 수 있어야 하는 것**: ① 오토블로킹 계산이 완료된 맵을 Export JSON File 절차로 내보내고, 산출 파일의 경로와 생성 여부를 확인할 수 있다. ② 테스트 서버에서 Layout>MapLoad로 맵 파일과 BackupPath를 지정해 반영(UPDATE)을 수행하고, 반영 전 맵 파일 저장 날짜·파일명 확인과 반영 후 백업 폴더 생성 확인을 빠뜨리지 않으며, 복귀에 쓸 직전 맵 파일과 백업 위치를 지목할 수 있다.
- **표시**: 근거약함, 사이트의존, 추정해석
- **주의**: [L3c-05] Export한 결과물을 OCS에 넣는 것은 L3c-03(Layout>MapLoad)이다. RDT로 만든 맵도 Winlay로 만든 맵과 같은 절차로 OCS Layout 탭 MapLoad에서 반영한다(2026-10-08 사이트 확인). 경로 E:\test.json은 예시다. / [L3c-07] 메뉴는 MXA본 11장 기준 Layout>MapLoad(파일 선택·BackupPath·UPDATE). 매뉴얼 원문은 선택 파일을 MDB로 적고 RDT 산출물은 JSON(Export Json File)이므로, 현장 MapLoad 화면에서 고르는 파일 형식을 실습 전에 확인한다. 백업에서 되돌리는 롤백 절차는 어느 자료에도 없다. MapLoad는 운영 SQL DB의 맵을 바꾸는 작업이므로(setup 가이드 5.1 'DB에 MDB 파일 적용으로 현장에 맞는 MAP 등록') 실습은 테스트 서버로 제한한다.

- **L3c-05 Export JSON 산출**
  - 내용: 사이트 우클릭 > Export Json File로 'Export JSON File' 창을 연다. Json File 경로(예 E:\test.json)를 Search로 지정하고 Progress Unit을 정한 뒤 'Start Auto-Blocking List Creation' → Export 순서로 오토블로킹 정보가 포함된 단일 JSON 맵 산출물을 만든다. Export 전에는 계산 로그가 'Calculation Complete!!!!'에 도달했는지 확인한다.
  - 할 수 있어야 하는 것: 오토블로킹 계산이 완료된 맵을 Export JSON File 절차로 내보내고, 산출 파일의 경로와 생성 여부를 확인할 수 있다.
  - 근거: 24-02-RailDesignTool-Manual.pdf p.35, p.8
- **L3c-07 MapLoad 반영·백업 확보**
  - 내용: RDT로 만든 맵도 Winlay로 만든 맵과 같은 절차로 OCS Layout 탭 MapLoad에서 반영한다(2026-10-08 사이트 확인). 메뉴는 Layout > MapLoad다(MXA본 11장: 파일 선택·BackupPath·UPDATE). 다른 자료에는 Core > System 탭 > MabLoad(setup 가이드: Map 선택·백업 폴더·MDB -> SQL), System -> MapLoad(설치 기준서: MDB File Path·BackupPath·MDB->SQL)로도 적혀 있다. 맵 파일과 BackupPath(백업 폴더)를 지정한 뒤 UPDATE(MDB->SQL)로 맵을 SQL DB에 적재한다. 원문은 '저장 날짜, 파일 이름 확인(매우 중요)'만 적고 있다. 그러므로 실행 전에는 지정한 맵 파일의 저장 날짜·파일 이름이 의도한 개정판인지 확인한다. 실행 후에는 지정한 백업 폴더에 결과물이 생겼는지 확인하고, 복귀에 쓸 직전 맵 파일과 백업 위치를 기록해 둔다. 백업 폴더에 정확히 무엇이 저장되는지, 백업에서 되돌리는 롤백 절차가 무엇인지는 어느 자료에도 없다.
  - 할 수 있어야 하는 것: 테스트 서버에서 Layout>MapLoad로 맵 파일과 BackupPath를 지정해 반영(UPDATE)을 수행하고, 반영 전 맵 파일 저장 날짜·파일명 확인과 반영 후 백업 폴더 생성 확인을 빠뜨리지 않으며, 복귀에 쓸 직전 맵 파일과 백업 위치를 지목할 수 있다.
  - 근거: RCP Program setup 가이드 p.29 (Map Load) 표21; OCS 설치 기준서 p.35 (4장 절차 10); \_MANUAL\_User Manual\_V01\_MXA.docx Layout 장 (MapLad/MDB/UPDATE); RCP Program setup 가이드 p.29 표21; \_MANUAL\_User Manual\_V01\_MXA.docx Layout 장

### L3c-04 MapLoad 실패 조치·실 시스템 영향 판정

- **레벨**: L3  ·  **교육 방식**: 현장점검  ·  **탭**: 서버  ·  **Section / Module**: Map & Traffic Control / Map Deployment  ·  **범위**: Core  ·  **교육 일차**: 6
- **화면·도구**: AccessDatabaseEngine 설치본, OCS Layout > MapLoad / RailDesignTool File > Open / Save ↔ 사이트 우클릭 > Auto Blocking, Export Json File / OCS Layout > MapLoad
- **할 수 있어야 하는 것**: ① MapLoad가 실패했을 때 AccessDatabaseEngine 설치 여부·비트·Office 충돌을 점검하고, 재설치 조치를 결정·수행할 수 있다. ② 제시된 맵 작업 목록의 각 조작이 도구 내부에서 끝나는지 실 시스템에 영향을 주는지 판정하고, 실 반영 조작에 필요한 선행 조치를 제시할 수 있다.
- **표시**: 추정해석
- **주의**: [L3c-08] AccessDatabaseEngine은 MDB를 읽는 MapLoad 전제 조건이다(setup 가이드 3.5). RDT 맵도 같은 MapLoad로 반영하므로 이 점검을 적용하되, 현장에서 MapLoad에 넣는 파일이 MDB가 아니면 AccessDatabaseEngine이 관여하는지 확인한다. / [L3c-09] 이 기준은 조사자가 매뉴얼을 종합해 만든 것이다. RDT로 만든 맵도 Winlay로 만든 맵과 같은 절차로 OCS Layout 탭 MapLoad에서 반영한다(2026-10-08 사이트 확인). 반영 후 롤백 절차는 자료에 없으므로 '실 반영 전 백업·테스트 서버 선행'까지만 채점한다.

- **L3c-08 MapLoad 실패 조치**
  - 내용: AccessDatabaseEngine은 Core Map Update(MapLoad)에 필요한 프로그램이다. Microsoft Office가 설치돼 있으면 설치가 되지 않으므로 Access부터 설치해야 하고, OS 비트에 맞는 버전을 써야 한다. Microsoft Office를 제거한 뒤 Core에서 MapLoad가 안 되면 AccessDatabaseEngine을 재설치한다.
  - 할 수 있어야 하는 것: MapLoad가 실패했을 때 AccessDatabaseEngine 설치 여부·비트·Office 충돌을 점검하고, 재설치 조치를 결정·수행할 수 있다.
  - 근거: RCP Program setup 가이드 p.23 (3.5 AccessDatabaseEngine 설치) 본문 P218~223; RCP Program setup 가이드 p.29 표21 (AccessDataBaseEngine 설치 확인 필수)
- **L3c-09 실 시스템 영향 판정**
  - 내용: RDT에서 작도·Attributes 수정·Save(Revision 기록)한 결과는 사이트 폴더 안에만 머문다. Auto Blocking 계산, Safety Margin·Progress Unit 변경, Export Json File, Layout>MapLoad(UPDATE)는 실 시스템에 들어갈 데이터를 만들거나 직접 바꾼다. 수행하려는 조작이 이 체인(RDT 작도 → 오토블로킹 → JSON Export → OCS Layout>MapLoad 반영)의 어느 단계인지 짚고, 실 반영 단계라면 백업과 테스트 서버 선행 여부를 확인한다.
  - 할 수 있어야 하는 것: 제시된 맵 작업 목록의 각 조작이 도구 내부에서 끝나는지 실 시스템에 영향을 주는지 판정하고, 실 반영 조작에 필요한 선행 조치를 제시할 수 있다.
  - 근거: 24-02-RailDesignTool-Manual.pdf p.8, p.17, p.27, p.35, p.36 종합; OCS 설치 기준서 p.35

## 보조 7개 목표 밖

### AUX-01 DB 서비스·파일 증가 점검

- **레벨**: L1  ·  **교육 방식**: 화면실습  ·  **탭**: 서버  ·  **Section / Module**: System Setup / Database  ·  **범위**: Core  ·  **교육 일차**: 2
- **화면·도구**: services.msc / SSMS > SQL Server 에이전트 > 작업 활동 모니터 > 작업 활동 보기 / 탐색기 D:\SQLData, E:\SQLLog / SSMS > 개체 탐색기 > 테이블 > 속성
- **할 수 있어야 하는 것**: ① services.msc와 SSMS 작업 활동 모니터를 열어 DB/Agent 서비스 상태와 실패한 Job을 찾아 정상/비정상을 판정할 수 있다. ② SQLData/SQLLog 폴더와 SSMS 테이블 사용량을 조회해 비정상 증가 중인 DB 파일·테이블을 지목할 수 있다.
- **표시**: 사이트의존, 근거약함
- **주의**: [AUX-01] 점검 주기(일/주/월)와 체크시트 양식이 자료에 없음(검증자 fixes) — 교육 산출물로 신규 작성 필요 / [AUX-02] '비정상 증가'의 수치 기준이 자료에 없음. 테이블 사용량(C116)은 절차 설명 1줄뿐

- **AUX-01 DB·Agent 서비스 기동 점검**
  - 내용: 실행 > services.msc에서 DB Service와 Agent Service가 둘 다 '실행 중'인지 확인하고 DBMS 접속 가능 여부를 본다(접속 불가 시 OCS Program 가동·DataBase 업데이트·유지보수 불가). 이어 SSMS > SQL Server 에이전트 > 작업 활동 모니터 > 작업 활동 보기에서 각 Job의 최근 실행 결과(성공/실패)를 확인한다. Agent가 죽어 있으면 History 정리·백업이 전부 멈춘다.
  - 할 수 있어야 하는 것: services.msc와 SSMS 작업 활동 모니터를 열어 DB/Agent 서비스 상태와 실패한 Job을 찾아 정상/비정상을 판정할 수 있다.
  - 근거: DB 점검 메뉴얼\_20220607.pdf p.3; DB 점검 메뉴얼\_20220607.pdf p.7
- **AUX-02 MDF·LDF·테이블 증가 점검**
  - 내용: D드라이브 > SQLData(MDF)와 E드라이브 > SQLLog(LDF)에서 [수정한 날짜]가 바뀌는 파일을 골라 크기가 비정상적으로 증가하는지 주기 점검한다(증가 = HDD FULL 위험). SSMS > 개체 탐색기 > 테이블 속성/사용량으로 테이블별 비정상 누적을 확인한다. 드라이브 경로는 예: (사이트별 확인).
  - 할 수 있어야 하는 것: SQLData/SQLLog 폴더와 SSMS 테이블 사용량을 조회해 비정상 증가 중인 DB 파일·테이블을 지목할 수 있다.
  - 근거: DB 점검 메뉴얼\_20220607.pdf p.5; DB 점검 메뉴얼\_20220607.pdf p.6; DB 점검 메뉴얼\_20220607.pdf p.8

### AUX-02 History Job·SQL 메모리·백업 계획 점검

- **레벨**: L2  ·  **교육 방식**: 화면실습  ·  **탭**: 서버  ·  **Section / Module**: System Setup / Database  ·  **범위**: Core  ·  **교육 일차**: 2
- **화면·도구**: SSMS > History DB 테이블 / SSMS 로그 파일 뷰어 > 작업 기록 / SYSTEM > Parameter > LogParam / 작업 관리자 / SSMS > 서버 속성 > 메모리 / SSMS > 관리 > 유지 관리 계획 / System > Parameter > DataBaseParam / 탐색기 백업 폴더
- **할 수 있어야 하는 것**: ① History 테이블이 안 생기거나 안 지워질 때 Agent Job 등록·실행 → LogParam 보존기한 순으로 원인 위치를 설명하고 해당 Job을 지목할 수 있다. ② SQL Server 메모리 점유와 최대 서버 메모리 설정을 비교해 무제한(2147483647) 설정의 위험을 지적하고 사양 기준 상한 설정 필요 여부를 판정할 수 있다. ③ 유지관리 계획과 DBBackupFolder/DBBackupFolder2 설정을 읽어 백업 7종 파일 생성 여부와 2차 경로 분리 여부를 판정할 수 있다.
- **표시**: 사이트의존, 민감정보, 근거약함, 자료충돌
- **주의**: [AUX-03] 캡처의 서버명 RCP-DB01은 역할명(DB서버)으로 치환. Job 목록·보존기한 400일은 사이트별 확인. LogParam 자체 항목은 타 버킷 / [AUX-04] 상한 산정 기준값이 자료에 없음. MemoryLevel 70/80/90은 Parameter 매뉴얼 예시(80/85/90)·현장 캡처(87/92/97)와 달라 기준값으로 쓰지 말 것 / [AUX-05] 계획명·주기·보존기간은 캡처 예시

- **AUX-03 History DB·Agent Job 연쇄**
  - 내용: SSMS > 데이터베이스 History에서 dbo.AlarmHistoryByDay_YYYYMMDD / dbo.OrderHistoryByDay_YYYYMMDD / dbo.OrderHistory2ByDay_YYYYMMDD 날짜별 테이블이 매일 생성되고 저장기한(예시 400일, SYSTEM > Parameter > LogParam) 지난 테이블이 삭제되는지 확인한다. 이 생성·삭제는 SQL Agent Job(AlarmHistoryJob, CommLogHistoryJob, OrderLogHistoryJob, HsmsHistoryJob, VehicleMoveHistoryJob, DeleteOldHistoryPlayBackJob(15분 간격), CpuUsageUpdateJob, HddUsageUpdateJob, MemoryUsageUpdateJob, FullBackup.하위 계획_1 등)이 수행하므로, Agent 작업 등록이 먼저 확인되어야 History(알람/Comm Log/Transfer/Move) 잔존 데이터를 판정할 수 있다.
  - 할 수 있어야 하는 것: History 테이블이 안 생기거나 안 지워질 때 Agent Job 등록·실행 → LogParam 보존기한 순으로 원인 위치를 설명하고 해당 Job을 지목할 수 있다.
  - 근거: DB 점검 메뉴얼\_20220607.pdf p.4, p.9~11, p.14 + docx 내장 이미지
- **AUX-04 SQL 메모리 점유·상한 판정**
  - 내용: 작업 관리자에서 'SQL Server Windows NT - 64 Bit' 프로세스 메모리 점유를 보고 SSMS > Server 우클릭 > 속성 > 메모리 > '최대 서버 메모리(MB)' 값과 비교한다(점유 ≤ 최대값이 정상). 캡처 기본값 2147483647은 사실상 무제한이므로, SQL이 메모리를 전부 점유해 같은 서버의 Core/MCS_IF/PlcDriver가 영향받지 않도록 서버 사양에 맞는 상한을 설정해야 함을 설명한다. 최초설치 BASE 항목 MemoryLevel1/2/3=70/80/90은 예: (사이트별 확인).
  - 할 수 있어야 하는 것: SQL Server 메모리 점유와 최대 서버 메모리 설정을 비교해 무제한(2147483647) 설정의 위험을 지적하고 사양 기준 상한 설정 필요 여부를 판정할 수 있다.
  - 근거: DB 점검 메뉴얼\_20220607.pdf p.16 + docx 내장 이미지; RCP Program setup 가이드 p.22 표12; 01. RCP 최초설치 확인사항.txt 48~52행
- **AUX-05 DB 백업 계획·경로 확인**
  - 내용: SSMS > 관리 > 유지 관리 계획에서 계획('유지관리로그백업' 예) > 하위 계획_1에 '데이터베이스 백업 태스크'(모든 사용자 DB, 트랜잭션 로그, 디스크)와 '유지 관리 정리 태스크'(보존 기간 예: 1일)가 연결·스케줄(예: 매일 1시간 간격) 등록되어 있는지 확인한다. Parameter -> 1. DataBaseParam의 1.1 DBBackupFolder / 1.2 DBBackupFolder2가 서로 다른 경로인지, 그 아래 날짜·시간 폴더에 aspnetdb / Host / OrderList / RCP / Rundata / Winlay / WinlayUpdate .BAK 7종이 생성되는지 확인한다.
  - 할 수 있어야 하는 것: 유지관리 계획과 DBBackupFolder/DBBackupFolder2 설정을 읽어 백업 7종 파일 생성 여부와 2차 경로 분리 여부를 판정할 수 있다.
  - 근거: DB 점검 메뉴얼\_20220607.pdf p.17 + docx 내장 이미지; OCS Parameter 매뉴얼 p.10 (1.1, 1.2)

### AUX-03 설치 기준·반입 전 준비 체크리스트

- **레벨**: L1  ·  **교육 방식**: 현장점검  ·  **탭**: 서버  ·  **Section / Module**: System Setup / Server Preparation  ·  **범위**: Core  ·  **교육 일차**: 1
- **화면·도구**: OCS 설치 기준서 / 레지스트리 편집기 / 프로그램 및 기능 / 제어판 > 어댑터 설정 변경 > IPV4 속성 / CMD ipconfig /all / 신청 양식
- **할 수 있어야 하는 것**: ① 설치 기준서와 레지스트리를 보고 서버에 필수 S/W·버전이 갖춰졌는지 체크리스트로 판정하고 비인가 S/W를 지적할 수 있다. ② 서버 반입·IP·Port·Wips 신청에 필요한 확인 항목과 제출 정보를 체크리스트로 빠짐없이 준비하고 Server IP를 설정·확인할 수 있다.
- **표시**: 사이트의존, 버전차이, 자료충돌, 민감정보
- **주의**: [AUX-06] .NET 최소 버전이 v04 매뉴얼 4.7.2 vs setup 가이드 3.5 vs 최초설치 확인사항 .net8 자동설치로 갈림 / [AUX-11] 신청 양식·추가 요구 항목은 사이트 보안 정책별로 다름. 실 IP·Mac은 마스킹

- **AUX-06 설치 기준·필수 S/W 확인**
  - 내용: OCS 설치 기준서는 '인가된 S/W만 설치'를 원칙으로 각 항목에 '관련 위협' 필드를 둔 위협-대응 대조표로 읽는다. 전제조건: Windows, MS SQL2016, .NetFrameWork 4.7.2 이상(setup 가이드는 3.5 이상), AccessDatabaseEngine, XcomPro / 서버 유틸: MicrosoftEdge, 반디집, UltraEdit, ExcelViewer/OpenOffice, ssms, nettime(업데이트 간격 1시간, 로컬VIP), cport. .NET 버전은 레지스트리 편집기 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\NET Framework Setup에서 확인한다.
  - 할 수 있어야 하는 것: 설치 기준서와 레지스트리를 보고 서버에 필수 S/W·버전이 갖춰졌는지 체크리스트로 판정하고 비인가 S/W를 지적할 수 있다.
  - 근거: OCS 사용자 매뉴얼\_v04\_210114.pdf p8; OCS 설치 기준서 p.3 (1. 개요); 01. RCP 최초설치 확인사항.txt 26~38행; RCP Program setup 가이드 p.16 표4
- **AUX-11 반입 전 현장·IP·Port 신청**
  - 내용: Server Rack 반입 전: 공장 도면(PM 요청)으로 Rack 기둥 열, 무선 업체 라인 통신 구성도로 AP/HUB 위치·HUB·Switch 사용 포트, 그레이팅 타공 사이즈, 전원 8구(UPS·Server×2·Switch×2·KVM·Monitor·Fan), 랜포트 2개+스페어 2개 확인. 공장 Local IP 신청(Mac Address 필수 + 사이트별 기둥열·허브룸·Windows 버전·Update/백신 일자·랜선 번호) 후 제어판 > 네트워크 및 인터넷 > 어댑터 설정 변경 > 속성 > 인터넷 프로토콜 버전 IPV4 > 속성에서 설정하고 ipconfig /all로 확인. Port 사용 가능 여부는 현업 Mail 문의, Wips·Local IP 방화벽 해제는 양식(Mac, 설비명, IP) 제출.
  - 할 수 있어야 하는 것: 서버 반입·IP·Port·Wips 신청에 필요한 확인 항목과 제출 정보를 체크리스트로 빠짐없이 준비하고 Server IP를 설정·확인할 수 있다.
  - 근거: RCP Program setup 가이드 p.5~8 (1.1~1.5); RCP Program setup 가이드 p.11~14 (1.8~1.11)

### AUX-04 기반 S/W·MSSQL 설치

- **레벨**: L2  ·  **교육 방식**: 도구실습  ·  **탭**: 서버  ·  **Section / Module**: System Setup / Database  ·  **범위**: Core  ·  **교육 일차**: 2
- **화면·도구**: OCS 설치 기준서 2장 / IIS 관리자 / 127.0.0.1/rcpgt / CMD(관리자) / SQL Server 2016 설치 마법사
- **할 수 있어야 하는 것**: ① 기반 S/W를 순서대로 설치하고, 장애 증상(Core/MDB 로드 실패, UI 미실행, 상위 통신 실패)을 보고 미설치·오설치된 항목을 지목할 수 있다. ② MSSQL 2016을 기준서대로 설치하면서 Agent 자동 시작과 데이터 경로를 미러링 경로로 지정해야 하는 이유를 설명할 수 있다.
- **표시**: 자료충돌, 사이트의존
- **주의**: [AUX-07] Access Engine 표기가 2.1 X64 vs 2.7 'X84'로 다름. 현 사이트 맵 도구는 RailDesignTool이므로 2.7 설치는 맵 작업 PC에 필수. .Net/IIS의 RCPGT 구조 설명은 L2-b 버킷(C557 주) / [AUX-08] 미러링 경로·Sp_helpfile 확인(C245)은 Rose 버킷 항목과 연결

- **AUX-07 기반 S/W 설치와 위협 매핑**
  - 내용: 설치 기준서 2장 항목별 설치와 미설치 시 증상: 2.1 AccessDatabaseEngine_X64(미설치 → Core 실행·MDB File 불러오기 실패), 2.2 'net user administrator /active:yes'(→ 관리자 권한 실행 오류, 비정상=액세스 거부), 2.3.2 SSMS-Setup-ENU.exe(→ SQL DB 구성 실패, SSMS 18.4는 SQL 2008~2019 지원), 2.4 Windows 기능의 .Net Framework·IIS·웹관리도구 + IIS 관리자에서 RCPGT 애플리케이션 추가 후 127.0.0.1/rcpgt 접속(→ RCP UI 실행 실패), 2.7 Setup4RailDesignToolV1(선행 Accessdatabaseengine), 2.8 XComProSetup.exe → HASP Driver(→ 상위 통신 연결 실패). DB 구축 전 RCP UI 경고 문구는 정상이며 IIS 장애로 오진하지 않는다.
  - 할 수 있어야 하는 것: 기반 S/W를 순서대로 설치하고, 장애 증상(Core/MDB 로드 실패, UI 미실행, 상위 통신 실패)을 보고 미설치·오설치된 항목을 지목할 수 있다.
  - 근거: OCS 설치 기준서 p.4 (2.1, 2.2), p.9~10 (2.3.2), p.12~16 (2.4), p.19 (2.7), p.20 (2.8); RCP Program setup 가이드 p.20 표8
- **AUX-08 MSSQL Server 2016 설치**
  - 내용: Setup.exe > Installation > 'Perform a new Installation of SQL Server 2016' > Feature Selection에서 Database Engine Services만 체크 > Default Instance(추가 설치는 Named Instance) > SQL Server Agent 'Automatic' > 로그인 암호·현재 사용자 추가 > Data root directory를 미러링 경로(예: D 드라이브)로 변경 후 서비스팩(SQLServer2016-SP2 CU10-KB4524334-x64) 설치. 관련 위협: Agent 미설정 시 SQL 실행 오류, 미러링 경로가 아니면 Failover 비정상.
  - 할 수 있어야 하는 것: MSSQL 2016을 기준서대로 설치하면서 Agent 자동 시작과 데이터 경로를 미러링 경로로 지정해야 하는 이유를 설명할 수 있다.
  - 근거: RCP Program setup 가이드 p.19 표7; OCS 설치 기준서 p.5~9 (2.3.1)

### AUX-05 DB 구축·UI 배포와 오류 조치

- **레벨**: L3  ·  **교육 방식**: 도구실습  ·  **탭**: 서버  ·  **Section / Module**: System Setup / Database  ·  **범위**: Core  ·  **교육 일차**: 2
- **화면·도구**: SSMS (ALLDB_CreateDataBase / ALLDB_CreateTable / ALLDB_UpdateTableAndProcedure) / 인터넷옵션 > 보안 / CMD (mage -cc, dfshim.dll CleanOnlineAppCache)
- **할 수 있어야 하는 것**: ① DB 구축 쿼리 3단계를 직접 실행하고, 실패 시 경로 함정 제거와 개별 쿼리 실행으로 구축을 완료할 수 있다. ② UI 설치·실행 오류 메시지를 보고 4종 중 어느 것인지 판별해 해당 조치(신뢰 사이트 추가, 캐시 정리 등)를 직접 수행할 수 있다.
- **표시**: 사이트의존
- **주의**: [AUX-09] 실습은 교육용 서버에서만 / [AUX-10] MXA본 TroubleShooting 장 기준.

- **AUX-09 DB 구축 쿼리 실행·실패 대응**
  - 내용: SSMS에서 DB_Procedure\CreateDataBaseAndTable -> ALLDB_CreateDataBase(DB 파일 경로 설정, F5) → ALLDB_CreateTable → DB_PROCEDURE\ALLDB_UpdateTableAndProcedure 3단계 순서로 실행하고 각 단계 생성 여부를 확인한다. 일괄 실행 실패 시 CreateTable / UpdateTable / Update_Procedure 쿼리를 각각 개별 실행하고, 경로에 띄어쓰기·특수문자가 없게 한다. 테이블·프로시저는 사이트별로 다르므로 DBProcedure 최신 버전을 확인한다.
  - 할 수 있어야 하는 것: DB 구축 쿼리 3단계를 직접 실행하고, 실패 시 경로 함정 제거와 개별 쿼리 실행으로 구축을 완료할 수 있다.
  - 근거: RCP Program setup 가이드 p.21 표9; OCS 설치 기준서 p.26~29 (3장)
- **AUX-10 UI 설치·배포 오류 조치**
  - 내용: MXA본 TroubleShooting 4종: 'IIS 7.5 ASP Error', '신뢰할 수 없음'(도구-인터넷옵션-보안-신뢰할 수 있는 사이트-추가), '응용프로그램 배포 오류'(동일 ID 앱 기설치 → SDK Tool 보유 시 mage -cc, 미보유 시 rundll32 c:\windows\system32\dfshim.dll CleanOnlineAppCache), 'InteropServices.COMException (HRESULT 0x800736B3)'(최초 UI 잘못 설치).
  - 할 수 있어야 하는 것: UI 설치·실행 오류 메시지를 보고 4종 중 어느 것인지 판별해 해당 조치(신뢰 사이트 추가, 캐시 정리 등)를 직접 수행할 수 있다.
  - 근거: \_MANUAL\_User Manual\_V01\_MXA.docx TroubleShooting 장

### AUX-06 방화벽 해제·CMD 진단 명령

- **레벨**: L2  ·  **교육 방식**: 화면실습  ·  **탭**: 네트워크  ·  **Section / Module**: System Setup / Server Preparation  ·  **범위**: Core  ·  **교육 일차**: 1
- **화면·도구**: 제어판 > Windows Defender 방화벽 / CMD ping / CMD: ping/tracert/telnet/netstat/tcping/arp/netsh/ipconfig/nbtstat/systeminfo
- **할 수 있어야 하는 것**: ① 방화벽을 설정 절차대로 해제하고 ping 결과 문구로 통신 정상/비정상 및 ICMP 차단 상황을 판정할 수 있다. ② 현상(무응답, 포트 미개방, IP 충돌 의심)에 맞는 CMD 명령을 골라 실행하고 결과 문구(ESTABLISHED, 요청 시간 만료 등)를 읽을 수 있다.
- **표시**: 사이트의존
- **주의**: [AUX-12] 사이트 보안정책상 전면 해제 대신 포트 예외만 허용될 수 있음. Rose 포트 예외(TCP/UDP 7330·3000~3002·7320, C097)는 Rose 버킷 항목과 연결 / [AUX-15] 검증자 missing(CMD 1차 진단 세트) 반영. tcping은 외부 도구 — 사이트 보안정책상 반입 승인 필요할 수 있음

- **AUX-12 방화벽 해제와 Ping 판정**
  - 내용: 제어판 > Windows Defender 방화벽 > 설정 사용자 지정에서 각 네트워크 유형 'Windows Defender 방화벽 사용 안 함' 체크(또는 Windows 보안 -> 방화벽 및 네트워크 보호), AP·DB 서버 양쪽. CMD 'ping IP'로 판정: 정상 '응답이 있다' / 비정상 '요청 시간이 만료 되었습니다'. 통신은 되는데 Ping만 안 나가면 방화벽 ICMP를 확인한다. 설치 기준서 판단: 타 서버·노트북 Ping 정상/불가.
  - 할 수 있어야 하는 것: 방화벽을 설정 절차대로 해제하고 ping 결과 문구로 통신 정상/비정상 및 ICMP 차단 상황을 판정할 수 있다.
  - 근거: RCP Program setup 가이드 p.15 표3, p.17 표5, p.50 표42; OCS 설치 기준서 p.17 (2.5)
- **AUX-15 CMD 진단 명령 세트**
  - 내용: ping IP(도달), tracert IP(통신 장애 구간), telnet IP Port(포트 접속, 미지정 시 23), netstat -an |findstr Port(ESTABLISHED만 통신 중), tcping IP Port(Ping+Port Open 동시, windows\system32에 복사 설치), arp -a/-d, netsh(ipv4 reset, arp 정적 변경), ipconfig /all, nbtstat -A IP(IP 충돌 PC명), systeminfo(핫픽스), net user /active. 모든 명령 뒤 |findstr 문자로 필터. ComGroup/PLCUnit 등록 전 RCP↔Vehicle/PLC 통신을 이 명령으로 먼저 확인한다.
  - 할 수 있어야 하는 것: 현상(무응답, 포트 미개방, IP 충돌 의심)에 맞는 CMD 명령을 골라 실행하고 결과 문구(ESTABLISHED, 요청 시간 만료 등)를 읽을 수 있다.
  - 근거: RCP Program setup 가이드 p.30 표22·23·24; RCP Program setup 가이드 p.50~52 표42~52

### AUX-07 서버 운영 설정 (RDP·NIC Teaming·UPS)

- **레벨**: L2  ·  **교육 방식**: 현장점검  ·  **탭**: 서버  ·  **Section / Module**: System Setup / Server Preparation  ·  **범위**: Core  ·  **교육 일차**: 1
- **화면·도구**: NIC 속성 > 전원 관리 / 원격 데스크톱 설정 / 이벤트 뷰어 / UPS 관리 콘솔 / Window Server Manager > NIC Teaming
- **할 수 있어야 하는 것**: ① RDP 포트·NIC 전원관리·UPS 자동종료 설정 상태를 점검하고, 전원 이중화 여부에 따라 UPS 자동 종료 설정이 맞는지 판정할 수 있다. ② NIC Teaming을 기준 모드로 구성·확인하고, 해제 전 IP 기록 등 주의사항을 지켜 작업할 수 있다.
- **표시**: 사이트의존, 민감정보
- **주의**: [AUX-13] RDP 포트 9833은 사이트 값 — 배포본 마스킹. UPS 설정 화면 절차는 자료에 없음 / [AUX-14] setup 가이드 p.47 Teaming Setting 기준. 원문은 Rose·Failover를 언급하지 않음.

- **AUX-13 서버 운영 설정·UPS 점검**
  - 내용: 최초설치 확인사항: 원격데스크톱 포트 3389 -> 9833 변경, 네트워크 카드 > 속성 > 전원 관리의 '전원을 절약하기 위해 컴퓨터가 이 장치를 끌 수 있음' 해제(남기면 랜카드 절전으로 통신 단절), Windows 이벤트 로그 특이사항 확인, UPS 작동 확인(일정 시간 후 서버 자동 종료). 단 파워 입력 이중화 구성에서는 자동 종료가 되면 안 된다(한쪽 전원 장애로 양 서버 동시 OFFLINE 위험).
  - 할 수 있어야 하는 것: RDP 포트·NIC 전원관리·UPS 자동종료 설정 상태를 점검하고, 전원 이중화 여부에 따라 UPS 자동 종료 설정이 맞는지 판정할 수 있다.
  - 근거: 01. RCP 최초설치 확인사항.txt 6~10행
- **AUX-14 NIC Teaming 구성**
  - 내용: Window Server Manager > NIC Teaming(NIC 2개 이상) > TASKS > New Team에서 Team name·Member adapters 지정, Additional Properties: Teaming mode = Switch independent, Load balancing modes = Dynamic, Standby adapter = None(모든 랜카드 활성). Teaming 해제 시 IP 정보가 모두 사라지므로 해제 전 IP를 기록한다.
  - 할 수 있어야 하는 것: NIC Teaming을 기준 모드로 구성·확인하고, 해제 전 IP 기록 등 주의사항을 지켜 작업할 수 있다.
  - 근거: RCP Program setup 가이드 p.47 (기타 > Teaming Setting)

### AUX-08 상위·차량 없는 시뮬 환경

- **레벨**: L2  ·  **교육 방식**: 도구실습  ·  **탭**: 외부도구  ·  **Section / Module**: System Setup / Site Configuration  ·  **범위**: Core  ·  **교육 일차**: 3
- **화면·도구**: XCom Simulator / Simulation.exe / RCP UI
- **할 수 있어야 하는 것**: XCom Simulator와 Simulation.exe로 MCS·실차 없이 OCS를 기동하고 오더 1건 반송까지 재현하는 교육·검증 환경을 구성할 수 있다.
- **표시**: 사이트의존
- **주의**: cfg/sml·포트는 사이트별. 검증자 open question의 실습 환경 최소안 근거

- **교육 내용**
  - 내용: XcomPro -> Simulator 실행, MCS_IF 폴더의 시뮬 cfg·sml 복사, D:\XComLog에 VHC_SIMUL 폴더 사전 생성 → Create New Simulation File(File > New > CFG) → View -> Configuration: Host Type=Host, IP Address/TCP Port, Connection Mode=Active, Log File 경로 → Start XCom(연결 → 끊기 → 메시지 보내기). 차량 측은 Simulation.exe를 실행해 대체하고 RCP UI에서 오더 생성·반송 수행을 확인한다.
  - 근거: RCP Program setup 가이드 p.45 표39; OCS 설치 기준서 p.31~33, p.37~38 (4장 절차 3~7, 13, 15)

### AUX-09 무선·유선 네트워크 구조 (5GHz 채널·AP/Bridge·Turbo Ring)

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: 네트워크  ·  **Section / Module**: System Setup / Server Preparation  ·  **범위**: Core  ·  **교육 일차**: 1
- **화면·도구**: 네트워크 채널 설계 자료(이론) / Window > PingList / ErrTag PING 대역 / MOXA Web Console: Turbo Ring DIP Switch / Loop Protection / Relay Warning / Event Log
- **할 수 있어야 하는 것**: ① DFS/SFS 차이와 채널표를 근거로 OCS-OHT용 4채널과 E84 PIO용 165채널 분리 설계를 설명하고 DFS 채널 사용을 부적합으로 판정할 수 있다. ② PING 알람 문구(OHT / OHT Bridge / AP)를 보고 문제 위치를 차량 탑재 Bridge와 트랙사이드 AP로 1차 분리해 설명할 수 있다. ③ 유선 Ring 이중화 구조와 Ring 단절 시 신호가 남는 위치(Relay Warning, Event Log)를 설명하고 해당 화면을 지목할 수 있다.
- **표시**: 사이트의존, 추정해석, 민감정보, 병기
- **주의**: [AUX-17] 자료 제목은 '9개'이나 본문은 8개+165 조건부. 'E84 알람 다발 → 165채널 의심' 판정은 자료에 없는 추론이라 평가에서 제외. 국가별 채널 규제 차이 확인 필요 / [AUX-18] Bridge=차량측 해석은 자료 조합 추론. PING 대역은 병기(ErrTag 7001~7120 / ErrorDescription 7001~7112). AP IP는 마스킹 / [AUX-24] 현장 Ring 적용 여부는 사이트 구성도로 확인

- **AUX-17 5GHz 채널 설계 원칙**
  - 내용: DFS 채널은 레이더 감지 시 채널 전환으로 1~10초 중단, CAC 최대 60초 → OHT 로밍에 부적합, SFS(고정 채널)를 쓴다. 20MHz 26채널 중 사용 가능 UNII-1(36/40/44/48)·UNII-3(149/153/157/161) 8개, UNII-2/2Ext 52~144 16개는 'X / DFS Required'(120·124·128 Weather Radar), ISM 165는 '△ Industry, Medical' 조건부. 제안: OCS-OHT 통신에 149/153/157/161, 차량-설비 E84 PIO 통신에 165 분리 할당.
  - 할 수 있어야 하는 것: DFS/SFS 차이와 채널표를 근거로 OCS-OHT용 4채널과 E84 PIO용 165채널 분리 설계를 설명하고 DFS 채널 사용을 부적합으로 판정할 수 있다.
  - 근거: 네트워크/\_네트워크채널설명\_OCS\_250113\_v2\_kor.pptx 슬라이드 3~7
- **AUX-18 AP·Bridge 역할과 알람 분리**
  - 내용: 트랙사이드 AP(MOXA AWK-3131A-US)와 차량 탑재 Bridge(MOXA AWK-1137C-US)로 구성되며 무선 경로는 AP > Bridge > Vehicle PLC다. ErrTag PING 대역에 'OHT nnn' / 'OHT Bridge nnn' / 'AP nn'이 별도로 있어, 'OHT Bridge DisConnected'는 차량 탑재 무선 모듈, 'AP nn Disconnected'는 트랙사이드 AP 쪽으로 1차 분리한다.
  - 할 수 있어야 하는 것: PING 알람 문구(OHT / OHT Bridge / AP)를 보고 문제 위치를 차량 탑재 Bridge와 트랙사이드 AP로 1차 분리해 설명할 수 있다.
  - 근거: 네트워크/Micron 대만 AP, Bridge 추가 설정 매뉴얼.pdf 2p; RestAPI\_추가본\_SNMP\_LIST.pptx 슬라이드 3; 260103\_ErrTag\_L30.xlsx PING 대역(7001/7052/7109)
- **AUX-24 Turbo Ring·Loop Protection**
  - 내용: IKS 계열은 Turbo Ring/Turbo Chain 이중화를 제공하며 외부 4번 DIP 스위치로 Turbo Ring 활성화(기본 Turbo Ring v2 enabled), DIP ON이면 웹에서 비활성화 불가, DIP 미사용 시 콘솔로 활성화. Ring 단절 신호는 Relay Warning 'Turbo Ring Break'(MASTER 스위치만 출력)와 Event Log 'Topology changed'·'Master setting is mismatched'에 나타난다. Loop Protection은 별도 enable.
  - 할 수 있어야 하는 것: 유선 Ring 이중화 구조와 Ring 단절 시 신호가 남는 위치(Relay Warning, Event Log)를 설명하고 해당 화면을 지목할 수 있다.
  - 근거: 네트워크/moxa-iks-6524-6526-series-managed-ethernet-switch-manual-v9.5.pdf 3-15, 3-18, 3-70, 3-86

### AUX-10 네트워크 장비 접속·모니터 판독·Export

- **레벨**: L1  ·  **교육 방식**: 도구실습  ·  **탭**: 네트워크  ·  **Section / Module**: Station, Network & EQ (Extended) / Network Equipment  ·  **범위**: Extended
- **화면·도구**: MOXA Web Console / Serial Console / Maintenance > Troubleshooting / MOXA Web Console: Monitoring > System Utilization / Monitor > Monitor by Switch·Port·SFP
- **할 수 있어야 하는 것**: ① 노트북 IP를 맞춰 MOXA AP/스위치 콘솔에 접속하고 Troubleshooting Export 파일을 확보할 수 있다. ② 모델별 메뉴 경로로 포트 Count·Monitor·SFP 화면을 열어 항목·색상 의미를 읽고 점검 캡처를 남길 수 있다.
- **표시**: 사이트의존, 민감정보, 근거약함
- **주의**: [AUX-19] 계정 PW는 현장 담당자 확인으로 대체. Export 파일 해석법은 자료 없음(검증자 지적) / [AUX-22] Monitor 3종은 벤더 매뉴얼 일반론. 모델은 사이트별

- **AUX-19 MOXA 장비 접속·자료 Export**
  - 내용: AP 웹콘솔: PC Network Connections > IPv4에서 장비와 같은 대역 IP·서브넷 설정 → 브라우저에 장비 IP(Default 192.168.127.253, 현장은 장비 정보 확인) → 인증서 경고 'Advanced' → 'Continue' → admin 로그인. 스위치는 serial(115200, None, 8, 1, VT100, RJ45 to DB9-F)·Telnet·Web 3경로이며 시리얼과 Telnet은 동시 접속 불가. 장애 자료는 Maintenance > Troubleshooting > Export(약 1~2분, PC 다운로드 폴더)로 확보한다.
  - 할 수 있어야 하는 것: 노트북 IP를 맞춰 MOXA AP/스위치 콘솔에 접속하고 Troubleshooting Export 파일을 확보할 수 있다.
  - 근거: 네트워크/AP Troubleshooting export 매뉴얼\_26.02.09\_최지현.pdf 4~7p; 네트워크/moxa-iks-6524-6526-series-managed-ethernet-switch-manual-v9.5.pdf 2-2
- **AUX-22 Switch/HUB 모니터 화면 판독**
  - 내용: 포트 Tx/Rx Count: IKS-G6524A(Main Switch) Monitoring > System Utilization, EDS-P510A(HUB) Monitor > Monitor System에서 포트 선택 후 상세 Count를 캡처. Monitor by Switch/Port: Total/TX/RX/Error Packets(Uni-cast 적·Multi-cast 녹·Broad-cast 청, Packets/s), All Ports 막대(청 Uni/적 Multi/주 Broad). Monitor by SFP: Temperature(±3°C), Voltage(±0.1V), Tx/Rx power dBm(±3dB).
  - 할 수 있어야 하는 것: 모델별 메뉴 경로로 포트 Count·Monitor·SFP 화면을 열어 항목·색상 의미를 읽고 점검 캡처를 남길 수 있다.
  - 근거: 네트워크/Switch HUB Tx, Rx Count 확인 메뉴얼.pdf 3~5p; 네트워크/moxa-iks-6524-6526-series-managed-ethernet-switch-manual-v9.5.pdf 3-78~3-80

### AUX-11 AP/Bridge·스위치 설정 변경

- **레벨**: L3  ·  **교육 방식**: 도구실습  ·  **탭**: 네트워크  ·  **Section / Module**: Station, Network & EQ (Extended) / Network Equipment  ·  **범위**: Extended
- **화면·도구**: MOXA Web Console: Advanced WLAN Settings / Save Configuration / Firmware Upgrade / Cisco Switch CLI / Cisco WLC 웹
- **할 수 있어야 하는 것**: ① AP/Bridge 무선 파라미터를 기준값으로 설정·저장하고, 통신 단절 영향을 고려해 펌웨어 업그레이드 시점을 정해 수행할 수 있다. ② Cisco 스위치 VLAN·access/trunk 구성과 WLC에서 AP 채널·출력 조정을 CLI/웹으로 수행할 수 있다.
- **표시**: 사이트의존, 자료충돌, 민감정보, 버전차이
- **주의**: [AUX-20] 기준값은 Micron 사이트 지정값 / [AUX-21] 서브넷 255.255.254.0(2019 BOE) vs 255.255.252.0(Micron) 충돌 — 사이트별 확인. Cisco 구성 사이트에만 해당, MOXA 사이트와 장비 체계 다름

- **AUX-20 MOXA AP/Bridge 설정 변경**
  - 내용: Wireless LAN Setup > WLAN > Advanced WLAN Settings 필수값: AWK-3131A-US(AP) Multicast rate 6M, Inactive timeout 8, CCA Settings Auto, Maximum CCA -75, CCA Threshold 30 / AWK-1137C-US(Bridge) CCA Auto, -75, 30. Submit 후 Save Configuration에서 Save해야 유지된다. 펌웨어는 Maintenance > Firmware Upgrade > Choose File > 'Upgrade Firmware and Restart'(재부팅 약 4분 — 해당 구간 차량 통신 단절이므로 작업 시점 선정).
  - 할 수 있어야 하는 것: AP/Bridge 무선 파라미터를 기준값으로 설정·저장하고, 통신 단절 영향을 고려해 펌웨어 업그레이드 시점을 정해 수행할 수 있다.
  - 근거: 네트워크/Micron 대만 AP, Bridge 추가 설정 매뉴얼.pdf 4~6p, 8~10p
- **AUX-21 Cisco Switch/AP 설정**
  - 내용: Switch: Console(Hyperterminal) enable → conf t → int Vlan 10 → ip address (장비IP) (서브넷) → secret·line vty 0 4 + login local → sp portfast default → hostname; AP·서버 포트 switchport mode access + access VLAN 10, Switch·Controller 포트 mode trunk + trunk allowed VLAN 10; wr / wr mem 저장. AP: lwapp ap ip address / default-gateway / hostname 후 Controller 웹에서 Access Points > 802.11a/n/ac > Configure로 RF Channel·Tx Power Level 조정.
  - 할 수 있어야 하는 것: Cisco 스위치 VLAN·access/trunk 구성과 WLC에서 AP 채널·출력 조정을 CLI/웹으로 수행할 수 있다.
  - 근거: 네트워크/\_MANUAL\_ Switch\_AP 세팅 메뉴얼.pptx 슬라이드 4~5, 8~9; RestAPI\_추가본\_SNMP\_LIST.pptx 슬라이드 4

### AUX-12 스위치 로그로 원인 계층 판정

- **레벨**: L3  ·  **교육 방식**: 로그실습  ·  **탭**: 네트워크  ·  **Section / Module**: Station, Network & EQ (Extended) / Network Equipment  ·  **범위**: Extended
- **화면·도구**: MOXA Web Console: Event Log / Syslog / Monitor + OCS ErrorList·AlarmHistory
- **할 수 있어야 하는 것**: 스위치 Event Log·포트 통계와 OCS 통신 알람 시각을 대조해 장애 원인을 OCS측/네트워크 포트/물리 계층으로 특정할 수 있다.
- **표시**: 사이트의존, 근거약함
- **주의**: OCS 알람과의 대조 판정은 자료 해석(벤더 매뉴얼에 OCS 연계 근거 없음) — 실 사례 보강 필요

- **교육 내용**
  - 내용: MOXA Event Log(Bootup, Date, Time, System Startup Time, Events — Cold/Warm start, Configuration change, Power 1/2 transition, Authentication fail, Topology changed, Master setting is mismatched, Port traffic overload, dot1x Auth Fail, Port link off/on)와 Syslog(서버 최대 3대, UDP 514)의 시각을 OCS PING/PLCCOMM 알람 시각과 대조하고, Tx/Rx·Error Packets 증가, Broadcast 급증, SFP Tx/Rx power 공차 이탈을 함께 봐 원인이 OCS측인지 스위치 포트·물리 계층인지 가른다.
  - 근거: 네트워크/moxa-iks-6524-6526-series-managed-ethernet-switch-manual-v9.5.pdf 3-78~3-80, 3-86~3-87

### AUX-13 EQ 감시 체계 구조

- **레벨**: L2  ·  **교육 방식**: 이론  ·  **탭**: 프로토콜  ·  **Section / Module**: Station, Network & EQ (Extended) / EQ Monitoring  ·  **범위**: Extended
- **화면·도구**: RCPGT EQ Group / EQ Tag / Error Tag
- **할 수 있어야 하는 것**: EQ Group/EQ Tag/Error Tag 3층 구조와 장비별 감시 항목·프로토콜·정상값을 설명하고, EQ 알람을 보고 해당 EQ Tag(OID/엔드포인트)를 지목할 수 있다.
- **표시**: 근거약함, 버전차이, 사이트의존, 민감정보, 자료충돌
- **주의**: 감시 대상은 'OCS Server 1/2 + UPS + AP' 4행(장비 종류 3)으로 표기. SNMP 목록 AP 8대 vs ErrTag AP 12대·HUB 6대 불일치. 화면은 스크린샷뿐, v04에 없는 신규 기능. 장비 IP·계정 마스킹

- **교육 내용**
  - 내용: EQ Group(장비를 IP·프로토콜 SNMP/REST 단위로 묶음) → EQ Tag(EqGroupNumber, TagName, TagNumber, TagProperty, TagPollingSecond, Address(OID/URL), Value, Normal Value) → Error Tag 자동 생성(Comment·Remark만 수정 가능). 대상: OCS Server 1/2(HPE DL360 gen11 iLO — SNMP 161 FAN/POWER/DISK Normal=2·Abnormal=1, REST 443 /json/health_summary MEMORY·CPU·BATTERY OP_STATUS_OK/FAILED), UPS(Eaton 9PX — UPSOutputMode 3=OnLine/4=Bypass/5=OnBattery, BatteryChargePercent 0~100 등), AP(MOXA AWK-3131A-US — POWER 0/1, Temperature Normal Under 70 등).
  - 근거: RestAPI\_추가본\_SNMP\_LIST.pptx 슬라이드 3, 5, 13~20

### AUX-14 EQ 감시 체인 검증·알람 대응

- **레벨**: L3  ·  **교육 방식**: 도구실습  ·  **탭**: 프로토콜  ·  **Section / Module**: Station, Network & EQ (Extended) / EQ Monitoring  ·  **범위**: Extended
- **화면·도구**: MIB Browser / 브라우저(REST) / iLO·UPS·MOXA SNMP 설정 / RCPGT EQ Tag / iLO 웹 / UPS 관리 콘솔 / MOXA Web Console / CMD ping
- **할 수 있어야 하는 것**: ① 장비측 SNMP/REST 응답을 직접 검증해 미수신 원인을 장비측/OCS측으로 가르고, 허용된 방식(Normal Value 변경)으로 알람 체인을 시험할 수 있다. ② EQ 알람 종류별로 정해진 확인 순서를 수행해 장비 상태를 판정하고 에스컬레이션 여부와 대상을 결정할 수 있다.
- **표시**: 사이트의존, 민감정보, 근거약함, 버전차이
- **주의**: [AUX-26] Normal Value 변경 후 원복 절차는 자료에 없음 — 실습 시 원값 기록 필수 / [AUX-27] 에스컬레이션 연락 체계는 사이트별

- **AUX-26 EQ 감시 체인 검증**
  - 내용: EQ Tag 등록 전 4단계: ① iLO/UPS/AP에서 SNMP enable·UDP 161 개방 확인 ② MIB Browser로 OID 직접 질의 ③ REST URL(/json/health_summary)을 브라우저로 열어 JSON 응답·기대값·key 형식 확인 ④ iLO 웹에 먼저 로그인해 인증 세션 생성. 등록 후 RCPGT Local Simulation Test로 EQ Tag Normal Value를 바꿔 알람을 유발해 체인을 검증한다(EQ Tag Value 직접 갱신은 'test environments only' — 실가동 금지).
  - 할 수 있어야 하는 것: 장비측 SNMP/REST 응답을 직접 검증해 미수신 원인을 장비측/OCS측으로 가르고, 허용된 방식(Normal Value 변경)으로 알람 체인을 시험할 수 있다.
  - 근거: RestAPI\_추가본\_SNMP\_LIST.pptx 슬라이드 7~12, 21
- **AUX-27 EQ 알람 대응·에스컬레이션**
  - 내용: OCS Server FAN/DISK/POWER: iLO 접속 → 온도 센서·네트워크 포트·메모리 모듈·프로세서 4화면 확인 → 반복 시 지원팀. UPS: SNMP 알람 확인 → OCS Server LED → UPS 관리 콘솔(최근 알람 로그, 입력 전압·주파수, 출력 전압·전류, 시스템 로그) → 이상 전원 의심 시 담당팀. AP: AP IP ping → 응답 시 MOXA 웹콘솔 시스템 로그·장치 상태 → 무응답·반복 시 Troubleshooting Export 확보 후 네트워크/지원팀.
  - 할 수 있어야 하는 것: EQ 알람 종류별로 정해진 확인 순서를 수행해 장비 상태를 판정하고 에스컬레이션 여부와 대상을 결정할 수 있다.
  - 근거: RestAPI\_추가본\_SNMP\_LIST.pptx 슬라이드 22~33; 네트워크/AP Troubleshooting export 매뉴얼\_26.02.09\_최지현.pdf 7p
