"""v0.4 항목에 LCS 역량 체계 양식(Section / Module / Category)과 배점·일정을 붙인다."""
import json
from collections import OrderedDict, Counter

d = json.load(open('_work/items_v0.4.json', encoding='utf-8'))
I = OrderedDict((it['id'], it) for it in d['items'])

# Section: (영문명, 한글명, 배점(만점), [(Module, [v0.4 ID...])])
SECTIONS = [
    ('System Setup', '시스템 구조·설치', 8, [
        ('Architecture', ['L2b-01', 'L2b-02', 'L2b-03']),
        ('Installation', ['AUX-03', 'AUX-04', 'AUX-05']),
        ('Server Settings', ['AUX-06', 'AUX-07']),
        ('Simulation Env', ['AUX-08']),
    ]),
    ('Screen Operation', '화면 조작', 14, [
        ('Main & View', ['L1-01', 'L1-02', 'L1-03']),
        ('System Menu', ['L1-04', 'L1-05', 'L1-06', 'L1-07']),
        ('Object Menu', ['L1-08', 'L1-09', 'L1-10', 'L1-11']),
        ('Transfer & Report', ['L1-12', 'L1-13', 'L1-14']),
        ('Statistics & Window', ['L1-15', 'L1-16', 'L1-17']),
        ('PlayBack & Help', ['L1-18', 'L1-19', 'L1-20']),
    ]),
    ('Map & Traffic Control', '맵·통행 제어', 12, [
        ('RDT Basics', ['L2a-01', 'L2a-02', 'L2a-03']),
        ('OCS Traffic Settings', ['L2a-04', 'L2a-05', 'L2a-06', 'L2a-07', 'L2a-08']),
        ('Auto-Blocking', ['L3c-01', 'L3c-02']),
        ('Map Deployment', ['L3c-03', 'L3c-04']),
    ]),
    ('Vehicle Interface', '차량 통신', 8, [
        ('OHT Protocol', ['L2b-06', 'L2b-07']),
        ('Comm Log Analysis', ['L3a-01', 'L3a-02']),
        ('Comm Diagnosis', ['L3a-04']),
    ]),
    ('Host Interface', '상위(MCS) 연동', 10, [
        ('MCS_IF Config', ['L2b-04']),
        ('SECS Structure', ['L2b-08', 'L2b-09']),
        ('Host Sequence', ['L2b-10']),
        ('Host Log Analysis', ['L3a-09', 'L3a-11', 'L3a-12', 'L3a-13']),
    ]),
    ('PLC & Equipment Interface', 'PLC·설비 연동', 8, [
        ('Tag System', ['L2b-11', 'L2b-13']),
        ('PLC Comm', ['L2b-12']),
        ('Station & PIO Rules', ['L2b-15']),
        ('Equipment Log Analysis', ['L3a-10']),
        ('EQ Monitoring', ['AUX-13', 'AUX-14']),
    ]),
    ('Parameters & Operation Settings', '파라미터·운영 설정', 6, [
        ('Parameter System', ['L2b-14']),
        ('Tuning', ['L3a-14']),
        ('Log & Disk Settings', ['L3a-15']),
        ('DB Maintenance', ['AUX-01', 'AUX-02']),
    ]),
    ('Alarm & Troubleshooting', '알람·로그 분석', 20, [
        ('Log Map & Entry Points', ['L2c-01', 'L2c-02', 'L2c-03']),
        ('Alarm Entry Points', ['L2c-04', 'L2c-05', 'L2c-06', 'L2c-07', 'L2c-08', 'L2c-09']),
        ('Analysis Method', ['L3a-06']),
        ('Vehicle & Order Analysis', ['L3a-03', 'L3a-07', 'L3a-08']),
        ('Server Analysis', ['L3a-05']),
    ]),
    ('Redundancy & Network', '이중화·네트워크', 14, [
        ('Rose Concept', ['L2b-05']),
        ('Rose Operation', ['L3b-01', 'L3b-02', 'L3b-03']),
        ('Rose Maintenance', ['L3b-04', 'L3b-05', 'L3b-06']),
        ('Network Structure', ['AUX-09']),
        ('Network Equipment', ['AUX-10', 'AUX-11', 'AUX-12']),
    ]),
]

# 9일 교육 + 10일차 평가. (일차, 날짜, AM, PM, [v0.4 ID...])
SCHEDULE = [
    (1, '10/19 Mon', 'Kick-off · System Setup: Architecture', 'System Setup: Installation · Server Settings · Simulation (hands-on)',
     ['L2b-01', 'L2b-02', 'L2b-03', 'AUX-03', 'AUX-04', 'AUX-05', 'AUX-06', 'AUX-07', 'AUX-08']),
    (2, '10/20 Tue', 'Screen Operation: Main & View · System Menu', 'Screen Operation: Object Menu (hands-on)',
     ['L1-01', 'L1-02', 'L1-03', 'L1-04', 'L1-05', 'L1-06', 'L1-07', 'L1-08', 'L1-09', 'L1-10', 'L1-11']),
    (3, '10/21 Wed', 'Screen Operation: Transfer & Report · Statistics & Window · PlayBack & Help', 'Map & Traffic Control: OCS Traffic Settings (hands-on)',
     ['L1-12', 'L1-13', 'L1-14', 'L1-15', 'L1-16', 'L1-17', 'L1-18', 'L1-19', 'L1-20', 'L2a-04', 'L2a-05', 'L2a-06', 'L2a-07', 'L2a-08']),
    (4, '10/22 Thu', 'Map & Traffic Control: RDT Basics · Auto-Blocking (hands-on)', 'Map & Traffic Control: Map Deployment (hands-on on test server)',
     ['L2a-01', 'L2a-02', 'L2a-03', 'L3c-01', 'L3c-02', 'L3c-03', 'L3c-04']),
    (5, '10/23 Fri', 'Vehicle Interface: OHT Protocol · Comm Log Analysis · Comm Diagnosis', 'PLC & Equipment Interface: Tag System · PLC Comm · Station & PIO · Equipment Log · EQ Monitoring',
     ['L2b-06', 'L2b-07', 'L3a-01', 'L3a-02', 'L3a-04', 'L2b-11', 'L2b-13', 'L2b-12', 'L2b-15', 'L3a-10', 'AUX-13', 'AUX-14']),
    (6, '10/26 Mon', 'Host Interface: MCS_IF Config · SECS Structure · Host Sequence · Host Log Analysis', 'Parameters & Operation Settings: Parameter System · Tuning · Log & Disk · DB Maintenance',
     ['L2b-04', 'L2b-08', 'L2b-09', 'L2b-10', 'L3a-09', 'L3a-11', 'L3a-12', 'L3a-13', 'L2b-14', 'L3a-14', 'L3a-15', 'AUX-01', 'AUX-02']),
    (7, '10/27 Tue', 'Alarm & Troubleshooting: Log Map & Entry Points · Alarm Entry Points', 'Alarm & Troubleshooting: Analysis Method (case practice)',
     ['L2c-01', 'L2c-02', 'L2c-03', 'L2c-04', 'L2c-05', 'L2c-06', 'L2c-07', 'L2c-08', 'L2c-09', 'L3a-06']),
    (8, '10/28 Wed', 'Alarm & Troubleshooting: Vehicle & Order Analysis · Server Analysis (case practice)', 'Redundancy & Network: Network Structure · Network Equipment',
     ['L3a-03', 'L3a-07', 'L3a-08', 'L3a-05', 'AUX-09', 'AUX-10', 'AUX-11', 'AUX-12']),
    (9, '10/29 Thu', 'Redundancy & Network: Rose Concept · Rose Operation (hands-on)', 'Redundancy & Network: Rose Maintenance · overall review & Q&A',
     ['L2b-05', 'L3b-01', 'L3b-02', 'L3b-03', 'L3b-04', 'L3b-05', 'L3b-06']),
    (10, '10/30 Fri', 'ASSESSMENT — written (L2 structure) + practical (L1 screen, L3 cases)', 'ASSESSMENT — practical cont. · scoring · individual feedback', []),
]

assigned = {}
for sec_en, sec_kr, marks, mods in SECTIONS:
    for mod, ids in mods:
        for i in ids:
            assert i in I, i
            assert i not in assigned, f'dup {i}'
            assigned[i] = (sec_en, sec_kr, mod)
missing = [i for i in I if i not in assigned]
assert not missing, missing
sched = {}
for day, date, am, pm, ids in SCHEDULE:
    for i in ids:
        assert i not in sched, f'dup sched {i}'
        sched[i] = day
missing = [i for i in I if i not in sched]
assert not missing, f'not scheduled {missing}'

for it in d['items']:
    sec_en, sec_kr, mod = assigned[it['id']]
    it['section'] = sec_en
    it['section_kr'] = sec_kr
    it['module'] = mod
    it['category'] = it['title']
    it['training_item'] = it['objective']   # 체크리스트 문구. 시험지 만들 때 축약 예정
    it['day'] = sched[it['id']]

d['sections'] = [OrderedDict([('section', s), ('section_kr', k), ('max_marks', m),
                              ('modules', [OrderedDict([('module', mo), ('items', ids)]) for mo, ids in mods])])
                 for s, k, m, mods in SECTIONS]
d['schedule'] = [OrderedDict([('day', day), ('date', date), ('am', am), ('pm', pm), ('items', ids)]) for day, date, am, pm, ids in SCHEDULE]
d['level_bands'] = OrderedDict([('Trainee', '<50%'), ('Level 1', '51-65%'), ('Level 2', '66-90%'), ('Level 3', '91%+')])
d['log'].append({'version': 'v0.4', 'date': '2026-10-08', 'change': 'LCS 양식 구조(Section/Module/Category) 부여, 섹션 배점 100점, 9일 교육+1일 평가 일정 배정'})
json.dump(d, open('_work/items_v0.4.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

print('sections:', [(s, sum(len(ids) for _, ids in mods), m) for s, _, m, mods in SECTIONS], 'marks sum', sum(m for _, _, m, _ in SECTIONS))
print('per day:', [(day, len(ids)) for day, _, _, _, ids in SCHEDULE])
print('level by section:', {s: dict(Counter(I[i]['level'] for _, ids in mods for i in ids)) for s, _, _, mods in SECTIONS})
