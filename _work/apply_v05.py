"""v0.4 → v0.5: 셋업 비중 확대. 사용자 매뉴얼 밖의 어려운 항목은 '확장(Extended)'으로 빼고 10일 안에서는 가르치지 않는다.
회사 제안서(RCP_Training_Plan_19-30_Oct_2026.xlsx) 양식: 하루 6시간(09-12 / 13-15 실습 / 15-16 복습), 5일차 체크포인트, 9일차 지식 테스트, 10일차 실기."""
import json
from collections import OrderedDict, Counter

d = json.load(open('_work/items_v0.4.json', encoding='utf-8'))
I = OrderedDict((it['id'], it) for it in d['items'])

# Section: (영문, 한글, 배점, [(Module, [ID...])])  — 확장 항목도 자연스러운 섹션에 둔다
SECTIONS = [
    ('System Setup', '시스템 구조·설치', 30, [
        ('Architecture', ['L2b-01', 'L2b-02', 'L2b-03']),
        ('Server Preparation', ['AUX-03', 'AUX-06', 'AUX-07', 'AUX-09']),
        ('Database', ['AUX-04', 'AUX-05', 'AUX-01', 'AUX-02', 'L3a-15']),
        ('Site Configuration', ['AUX-08', 'L1-05', 'L1-06', 'L2b-11', 'L2b-12']),
    ]),
    ('Screen Operation', '화면 조작', 15, [
        ('Main & View', ['L1-01', 'L1-02', 'L1-03']),
        ('System Menu', ['L1-04']),
        ('Object Menu', ['L1-08', 'L1-09', 'L1-10', 'L1-11']),
        ('Transfer & Report', ['L1-12', 'L1-13', 'L1-14']),
        ('Statistics & Window', ['L1-15', 'L1-16', 'L1-17']),
        ('PlayBack & Help', ['L1-18', 'L1-19']),
    ]),
    ('Map & Traffic Control', '맵·통행 제어', 15, [
        ('RDT Basics', ['L2a-01', 'L2a-02', 'L2a-03']),
        ('OCS Traffic Settings', ['L2a-04', 'L2a-05', 'L2a-06', 'L2a-07', 'L2a-08']),
        ('Auto-Blocking', ['L3c-01', 'L3c-02']),
        ('Map Deployment', ['L3c-03', 'L3c-04']),
    ]),
    ('Parameters', '파라미터', 5, [
        ('Parameter System', ['L1-07', 'L2b-14']),
        ('Tuning (Extended)', ['L3a-14']),
    ]),
    ('Host Interface (HSMS)', '상위(MCS) 연동', 10, [
        ('MCS_IF Config', ['L2b-04', 'L1-20']),
        ('HSMS Structure & Sequence', ['L2b-08', 'L2b-10']),
        ('SECS Deep-dive (Extended)', ['L2b-09', 'L3a-09', 'L3a-11', 'L3a-12', 'L3a-13']),
    ]),
    ('Vehicle Interface', '차량 통신', 5, [
        ('OHT Protocol', ['L2b-06']),
        ('Comm Log Basics', ['L3a-01', 'L3a-04']),
        ('Protocol Deep-dive (Extended)', ['L2b-07', 'L3a-02']),
    ]),
    ('Alarm & Troubleshooting', '알람·트러블슈팅', 15, [
        ('Alarm System', ['L2b-13']),
        ('Log Map & Entry Points', ['L2c-01', 'L2c-02', 'L2c-03']),
        ('Symptom Entry Points', ['L2c-04', 'L2c-05', 'L2c-06', 'L2c-07', 'L2c-08', 'L2c-09']),
        ('Log Analysis (Extended)', ['L3a-06', 'L3a-03', 'L3a-07', 'L3a-08', 'L3a-05', 'L3a-10']),
    ]),
    ('Redundancy (Rose)', 'Rose 이중화', 5, [
        ('Rose Concept', ['L2b-05']),
        ('Rose Operation', ['L3b-01', 'L3b-02', 'L3b-03', 'L3b-05']),
        ('Rose Maintenance (Extended)', ['L3b-04', 'L3b-06']),
    ]),
    ('Station, Network & EQ (Extended)', 'Station·네트워크·EQ (확장)', 0, [
        ('Station & PIO Rules', ['L2b-15']),
        ('Network Equipment', ['AUX-10', 'AUX-11', 'AUX-12']),
        ('EQ Monitoring', ['AUX-13', 'AUX-14']),
    ]),
]
EXTENDED = {'L3a-14', 'L2b-09', 'L3a-09', 'L3a-11', 'L3a-12', 'L3a-13', 'L2b-07', 'L3a-02',
            'L3a-06', 'L3a-03', 'L3a-07', 'L3a-08', 'L3a-05', 'L3a-10', 'L3b-04', 'L3b-06',
            'L2b-15', 'AUX-10', 'AUX-11', 'AUX-12', 'AUX-13', 'AUX-14'}

# 회사 양식: Day | Date | Module | 09:00–12:00 Explain & demonstrate | 13:00–15:00 Hands-on | 15:00–16:00 Review/test | Daily deliverable
SCHEDULE = [
    (1, '2026-10-19', 'Architecture & server preparation',
     'RCP/OCS components (Core, PlcDriver, MCS_IF, UI, DB) and what each talks to; server and network layout; config files and folders; startup order and Core state; installation standard, pre-delivery checklist',
     'Check the lab server against the installation standard: required software, firewall, NIC teaming, RDP, UPS; CMD diagnostics (ping, netstat); draw the component flow',
     'Each trainee explains the component flow and startup order and shows the server checklist',
     'Architecture sketch + server readiness checklist',
     ['L2b-01', 'L2b-02', 'L2b-03', 'AUX-03', 'AUX-06', 'AUX-07', 'AUX-09']),
    (2, '2026-10-20', 'Database setup & maintenance',
     'MSSQL 2016 installation per standard (Agent auto-start, data path on mirror disk); DB build queries; backup plan and folders; History tables and Agent jobs; SQL memory cap; log retention and disk settings',
     'Install MSSQL, run the 3-step DB build, fix a seeded path fault; set backup folders; check services, MDF/LDF growth and Agent jobs; restore from backup',
     'Each trainee restores the training DB from backup and explains the backup/retention settings',
     'DB setup guide + backup/restore evidence',
     ['AUX-04', 'AUX-05', 'AUX-01', 'AUX-02', 'L3a-15']),
    (3, '2026-10-21', 'Application installation & site configuration',
     'Base software and RCP install order; UI deployment on IIS and the 4 typical UI errors; simulator environment (XCom Simulator, Simulation.exe); registering a site: CommGroup → Vehicle → Station → OrderGroup; Tag 3-step registration and PlcTag file; PLC connection fields',
     'Each trainee installs RCP on the lab server from a clean baseline, brings Core up, deploys the UI, registers one vehicle and one PLC unit, loads tags from Excel and runs one order in the simulator',
     'Start RCP from clean baseline; identify a seeded configuration fault (DB IP / config / tag mapping)',
     'Application + site setup checklist',
     ['AUX-08', 'L1-05', 'L1-06', 'L2b-11', 'L2b-12']),
    (4, '2026-10-22', 'OCS screen operation (1) & parameters',
     'Main screen, status lamps, object colours, search; login and rights; View / Layout Setting / DockSetting; System menu: SystemInfo, Status, Color; Parameter menu structure and dispatch/driving parameters (read only)',
     'Object menu hands-on: Vehicle Line In/Out, Prevent, Sub Command, Clean; Station mode; Point/CPS/MTL status; PLC, Ping unit and Tag group registration',
     'Screen drill: trainer names a field or action, trainee finds it and explains it',
     'Screen checklist part 1',
     ['L1-01', 'L1-02', 'L1-03', 'L1-04', 'L1-07', 'L2b-14', 'L1-08', 'L1-09', 'L1-10', 'L1-11']),
    (5, '2026-10-23', 'OCS screen operation (2) & Week-1 checkpoint',
     'Transfer commands and CycleMove; Report histories; ErrorHistory / HSMSHistory; Statistics; OrderList and NACK; AlarmList, ErrorList, PingList, CommEvent; PlayBack; Help Version / Define',
     'Manual transfer and CycleMove on the simulator; look up histories and statistics; PlayBack export',
     'Week-1 checkpoint: each trainee walks through server → DB → application → site setup and the main screens',
     'Screen checklist part 2 + Week-1 checkpoint record',
     ['L1-12', 'L1-13', 'L1-14', 'L1-15', 'L1-16', 'L1-17', 'L1-18', 'L1-19']),
    (6, '2026-10-26', 'Map create, change & update',
     'Map structure; OCS-side traffic settings: Unuse, Home, Cluster, StationWeightGroup, AutoPark, Point type, UserBlock, Safety/CPS/MTL zones, Layout Run; RailDesignTool basics; vehicle spec and Safety Margin; auto-blocking',
     'Edit traffic settings on the lab OCS; in RDT open the site map, draw a segment, run auto-blocking, export JSON; MapLoad on the lab server with BackupPath',
     'Each trainee applies a map change on the lab server and explains the rollback path and live-system impact',
     'Validated map + change/rollback record',
     ['L2a-01', 'L2a-02', 'L2a-03', 'L2a-04', 'L2a-05', 'L2a-06', 'L2a-07', 'L2a-08', 'L3c-01', 'L3c-02', 'L3c-03', 'L3c-04']),
    (7, '2026-10-27', 'HSMS: RCP ↔ MCS',
     'MCS_IF configuration: cfg path, HSMS IP, XCom CfgSml, HostNetworkName; HSMS/SECS-II frame and timeouts T3–T8; connection sequence (S1F13/F17, S2F41, S2F49) and transfer events; where host communication problems show up (NackHistory, HSMSHistory, XCom log)',
     'Connect the lab OCS to the XCom simulator; register cfg/sml, bring the link to MCMD remote; send S2F49 and trace the order; recover from a seeded disconnect',
     'Each trainee explains a captured exchange and restores the seeded communication failure',
     'Communication checklist + annotated HSMS log',
     ['L2b-04', 'L1-20', 'L2b-08', 'L2b-10', 'L2c-04']),
    (8, '2026-10-28', 'Simulation, alarms & troubleshooting entry points',
     'Vehicle communication structure and OHT message basics; alarm classification (ErrType / ErrCode / ErrEvent); OCS log map (file log / DB history / UI / XCom); symptom → first screen or log for vehicle, order, server, startup, PLC problems',
     'Rotate fault stations on the simulator: startup failure, DB connection, vehicle no-response, order timeout, PLC comm alarm; read Comm log and CommErrHistory; isolate a communication break with ping / CMD',
     'Each trainee diagnoses two seeded faults, names the first screen/log and the recovery',
     'Fault isolation guide + incident records',
     ['L2b-06', 'L2b-13', 'L2c-01', 'L2c-02', 'L2c-03', 'L2c-05', 'L2c-06', 'L2c-07', 'L2c-08', 'L2c-09', 'L3a-01', 'L3a-04']),
    (9, '2026-10-29', 'Rose MirrorHA & knowledge test',
     'Rose resources, groups, virtual IP and FailOver triggers; console status reading; Bring In / Bring Out; manual failover and failback; service verification; failure types and first actions',
     'On the Rose test pair: read status, manual failover and failback, verify RCP UI via VIP and FailOverHistory',
     'Knowledge test (written): setup, DB, screens, map, HSMS, alarms, Rose. Record scores and gaps',
     'Knowledge scores + Rose checklist',
     ['L2b-05', 'L3b-01', 'L3b-02', 'L3b-03', 'L3b-05']),
    (10, '2026-10-30', 'Individual practical & handover',
     'Independent integrated practical: verify setup, edit map, register a vehicle/tag, run a simulation order, resolve a seeded fault and recover; trainer review and feedback',
     'Four individual practical slots (45 min each) in the morning; afternoon: targeted retest, handover of setup guide, map change checklist and fault guide',
     'Trainer records practical score, critical checks and sign-off; assign November follow-up (extended items)',
     'Individual results + handover pack + action list',
     []),
]

assigned, sched = {}, {}
for s_en, s_kr, marks, mods in SECTIONS:
    for mod, ids in mods:
        for i in ids:
            assert i in I and i not in assigned, i
            assigned[i] = (s_en, s_kr, mod)
missing = [i for i in I if i not in assigned]; assert not missing, missing
for day, date, mod, ex, ho, rv, dl, ids in SCHEDULE:
    for i in ids:
        assert i not in sched and i not in EXTENDED, i
        sched[i] = day
core = [i for i in I if i not in EXTENDED]
missing = [i for i in core if i not in sched]; assert not missing, f'not scheduled {missing}'

for it in d['items']:
    s_en, s_kr, mod = assigned[it['id']]
    it['section'], it['section_kr'], it['module'] = s_en, s_kr, mod
    it['category'] = it['title']
    it['training_item'] = it['objective']
    it['scope'] = 'Extended' if it['id'] in EXTENDED else 'Core'
    it['day'] = sched.get(it['id'])

d['version'] = 'v0.5'
d['sections'] = [OrderedDict([('section', s), ('section_kr', k), ('max_marks', m),
                              ('modules', [OrderedDict([('module', mo), ('items', ids)]) for mo, ids in mods])]) for s, k, m, mods in SECTIONS]
d['schedule'] = [OrderedDict([('day', day), ('date', date), ('module', mod), ('explain', ex), ('hands_on', ho), ('review', rv), ('deliverable', dl), ('items', ids)])
                 for day, date, mod, ex, ho, rv, dl, ids in SCHEDULE]
d['practical_tasks'] = [  # 10일차 실기 배점 (회사 제안서 구조)
    ('Server + application + IIS setup', 20, 'Working startup and UI URL from a test client', 'Explain setup and identify service/config dependencies'),
    ('Database build + backup/restore', 20, 'DB built, backup taken, restore verified', 'Backup before change; restore successfully'),
    ('Site configuration (vehicle, tag, PLC) + screens', 15, 'Vehicle runs one order in the simulator; screens explained', 'Tag mapping correct; CHECK TAG clean'),
    ('Map change + rollback', 15, 'Validated map applied with BackupPath', 'Verify connectivity and demonstrate rollback'),
    ('HSMS communication', 10, 'Link to simulator up; S2F49 order traced', 'Explain communication checks and reconnect'),
    ('Fault diagnosis + recovery', 15, 'Root cause evidence for a seeded fault', 'Name the first screen/log, recover safely'),
    ('Handover + teach-back', 5, 'Clear runbook and escalation record', 'Explain what changed and show evidence'),
]
d['pass_rule'] = OrderedDict([('attendance', 'at least 9 of 10 days'), ('week1_checkpoint', 'passed (Day 5)'),
                              ('knowledge', '>= 70 / 100 (Day 9)'), ('practical', '>= 80 / 100 (Day 10)'),
                              ('critical_checks', 'all passed: backup before change, rollback, recovery'),
                              ('signoff', 'trainer sign-off after reviewing evidence and catch-up work')])
d['log'].append({'version': 'v0.5', 'date': '2026-10-08', 'change': f"셋업 비중 확대. Core {len(core)} / Extended {len(EXTENDED)}. 회사 제안서 양식(일별 설명·실습·복습·산출물, 5일차 체크포인트, 9일차 지식 테스트, 10일차 실기)에 맞춤"})
json.dump(d, open('_work/items_v0.5.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('core', len(core), 'extended', len(EXTENDED))
print('per day', [(day, len(ids)) for day, *_ , ids in SCHEDULE])
for s, k, m, mods in SECTIONS:
    ids = [i for _, x in mods for i in x]
    print(f"{s:36s} core {sum(1 for i in ids if i not in EXTENDED):2d} ext {sum(1 for i in ids if i in EXTENDED):2d} marks {m}")
print('marks', sum(m for *_, m, _ in [(s, k, m, mods) for s, k, m, mods in SECTIONS]), 'practical', sum(t[1] for t in d['practical_tasks']))
