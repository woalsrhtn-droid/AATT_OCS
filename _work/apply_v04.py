"""v0.3 → v0.4: 비슷한 항목 통합. 9일 교육 + 1일 평가에 맞춰 항목 수를 줄인다.
내용은 버리지 않고 parts(통합 전 항목 전문)로 보존한다."""
import json, re
from collections import Counter, OrderedDict

d = json.load(open('_work/items_v0.3.json', encoding='utf-8'))
I = OrderedDict((it['id'], it) for it in d['items'])

# (통합 후 제목, [v0.3 ID...]) — 버킷 순서대로
GROUPS = [
    # L1
    ('L1', '메인 화면 구성·연결 램프·객체 색·찾기', ['L1-01', 'L1-02', 'L1-03', 'L1-05']),
    ('L1', '로그인 ID 등록·권한', ['L1-04']),
    ('L1', '화면 표시·배치·문구 설정 (View·Layout Setting/Check·DockSetting·Graphic)', ['L1-06', 'L1-44', 'L1-42', 'L1-26']),
    ('L1', 'System 자원·Status·Color 조회', ['L1-07', 'L1-08']),
    ('L1', '차량 등록 체인 (CommGroup→Vehicle→Station→OrderGroup)', ['L1-09', 'L1-10', 'L1-11']),
    ('L1', 'ErrorTag 등록·Tag Excel 일괄 편집', ['L1-12', 'L1-13']),
    ('L1', 'Parameter 진입·UI 표시값', ['L1-14']),
    ('L1', 'Object>Vehicle 조작 (Line In/Out·Prevent·Sub Command·Clean·Set/Etc·IO)', ['L1-15', 'L1-16', 'L1-17']),
    ('L1', 'Object>Station 속성·Mode·Port 확인', ['L1-18', 'L1-19']),
    ('L1', 'Object>Point·CPS·MTL 상태 판독', ['L1-20', 'L1-21', 'L1-22']),
    ('L1', 'Object>PLC·Ping Unit·Tag Group 등록·확인', ['L1-23', 'L1-24', 'L1-25']),
    ('L1', 'Transfer 수동 지령·CycleMove', ['L1-27', 'L1-28']),
    ('L1', 'Report 반송·운영 이력 조회 (Transfer·공통 이력·Blocking·CommErr)', ['L1-29', 'L1-32', 'L1-33']),
    ('L1', 'ErrorHistory·HSMSHistory 조회·Comment', ['L1-30', 'L1-31']),
    ('L1', 'Statistics 조회·Excel 저장 (Vehicle·Transfer·Error·Quality)', ['L1-34', 'L1-35', 'L1-36', 'L1-37']),
    ('L1', 'OrderList 판독·개입·NACK 처리', ['L1-38', 'L1-39']),
    ('L1', '실시간 창 판독 (AlarmList·ErrorList·PingList·CommEvent)', ['L1-40', 'L1-41', 'L1-43']),
    ('L1', 'PlayBack 재현·Export', ['L1-45', 'L1-46']),
    ('L1', 'Help Version·Define·주요 용어', ['L1-47', 'L1-48', 'L1-49']),
    ('L1', 'MCS_IF Cfg/SML 등록·상위 연결 확인', ['L1-50', 'L1-51']),
    # L2-a
    ('L2a', 'RDT 기본 조작 (실행·사이트 생성·열기·저장·개정)', ['L2a-01', 'L2a-02', 'L2a-03']),
    ('L2a', 'RDT 작도·편집·방향 확인', ['L2a-04', 'L2a-05', 'L2a-07']),
    ('L2a', 'RDT 속성 설정 (Point·Segment·Drawing)', ['L2a-06', 'L2a-08']),
    ('L2a', 'System>Unuse·Home 설정', ['L2a-09', 'L2a-10']),
    ('L2a', 'System 통행 제어 영역 (Cluster·StationWeightGroup·AutoParkArea)', ['L2a-11', 'L2a-12', 'L2a-17']),
    ('L2a', 'Object>Point Type·UserBlock/DisableBlock 설정', ['L2a-13', 'L2a-14']),
    ('L2a', 'Safety·CPS Interlock·MTL 유지보수 존 설정', ['L2a-15', 'L2a-16']),
    ('L2a', 'Layout Run 객체 배치·수정', ['L2a-18']),
    # L2-b
    ('L2b', 'OCS 실행 단위·서버·네트워크 구성', ['L2b-01', 'L2b-07']),
    ('L2b', 'Config·IIS·폴더 구성과 기동 실패 1차 확인', ['L2b-02', 'L2b-03']),
    ('L2b', '기동 순서와 Core 상태 전이', ['L2b-04']),
    ('L2b', 'MCS_IF 구성 (cfg 경로·HSMS IP·XCom CfgSml·HostNetworkName)', ['L2b-05', 'L2b-06']),
    ('L2b', 'Rose 이중화 구조·FailOver 요청·자원 경고 체계', ['L2b-08', 'L2b-09', 'L2b-10']),
    ('L2b', '차량 통신 구조·OHT 전문 (CMD·STATUS)', ['L2b-11', 'L2b-12', 'L2b-13']),
    ('L2b', '차량 지령 규칙·부가 장치 시나리오 (JCR·MTU·RFID·SCAN)', ['L2b-14', 'L2b-15']),
    ('L2b', 'HSMS·SECS-II 구조·타임아웃', ['L2b-16', 'L2b-17']),
    ('L2b', 'SECS 데이터 체계·SEMI 상태 모델', ['L2b-18', 'L2b-19']),
    ('L2b', '상위 접속·원격명령·이벤트 시퀀스', ['L2b-20', 'L2b-21', 'L2b-22']),
    ('L2b', 'Tag 등록·매핑·PlcTag 체계', ['L2b-23', 'L2b-24']),
    ('L2b', 'PLC 통신 구성·설비 태그 구조', ['L2b-25', 'L2b-26']),
    ('L2b', '알람 분류 체계 (ErrType·ErrCode·ErrEvent)', ['L2b-27', 'L2b-28']),
    ('L2b', 'Parameter 체계·배차/주행 거동 Parameter', ['L2b-29', 'L2b-30']),
    ('L2b', '반송 경로·Station·PIO·Host 연동 규칙', ['L2b-31', 'L2b-32']),
    # L2-c
    ('L2c', 'OCS 로그 지도 (4갈래·CoreForm·MCSIF/PLC/Secom)', ['L2c-01', 'L2c-02', 'L2c-03']),
    ('L2c', '증상별 로그 진입 순서·LogParam 로그 위치', ['L2c-04', 'L2c-05']),
    ('L2c', 'Report 이력 질문 매핑·UIHistory 변경자 추적', ['L2c-06', 'L2c-07']),
    ('L2c', '상위 명령 거부·상위 통신 이력 진입점', ['L2c-08', 'L2c-10']),
    ('L2c', '서버 리소스·FailOver·DB Exception 진입점', ['L2c-09', 'L2c-16', 'L2c-20']),
    ('L2c', '차량 통신 이상 진입 경로 (CommError·No Response·UVP)', ['L2c-11', 'L2c-12']),
    ('L2c', '타임아웃 알람 대응 파라미터·진입처', ['L2c-13', 'L2c-14']),
    ('L2c', '명령 후 무동작·기동 이상 진입점', ['L2c-15', 'L2c-19']),
    ('L2c', '설비·PLC 알람 진입점·원인 설명 찾기', ['L2c-17', 'L2c-18']),
    # L3-a
    ('L3a', 'Comm 로그 판독·오더 생애주기 재구성', ['L3a-01', 'L3a-02']),
    ('L3a', 'OHT 전문(HEX) 판독·프로토콜 불일치 판정', ['L3a-03', 'L3a-04', 'L3a-05']),
    ('L3a', '합류부 점유 고착·홈 재배치 판독', ['L3a-06', 'L3a-20']),
    ('L3a', '통신 지연·단절 구간 특정 (CommT·Ping·CMD)', ['L3a-07', 'L3a-08', 'L3a-09']),
    ('L3a', '서버 자원·FailOver 트리거·예외 로그 판정', ['L3a-10', 'L3a-11', 'L3a-12']),
    ('L3a', '다중 로그 재구성·근본원인 분리 (분석 방법)', ['L3a-13', 'L3a-14']),
    ('L3a', 'Order·Host 거부·배차/인계 로그 추적', ['L3a-15', 'L3a-16', 'L3a-17']),
    ('L3a', '정체 레일·블로킹·혼잡도 분석', ['L3a-18', 'L3a-19', 'L3a-21']),
    ('L3a', '상위 통신 로그 체인·S9/타임아웃 판정', ['L3a-22', 'L3a-23', 'L3a-24']),
    ('L3a', '설비 알람·PLC 로그 추적 (PlcTag·Not Define·카세트 ID)', ['L3a-25', 'L3a-26', 'L3a-27']),
    ('L3a', 'SECS 메시지 판독 (HCACK/CPACK·VID·S6F11·S5F1)', ['L3a-28', 'L3a-29', 'L3a-30', 'L3a-31']),
    ('L3a', '이적재 실패 케이스 (PIO Interlock·BCR NG·Empty/Double)', ['L3a-32', 'L3a-33', 'L3a-34']),
    ('L3a', '취소·중단 식별·Controller 복구 검증', ['L3a-35', 'L3a-36']),
    ('L3a', '거동 파라미터 튜닝·위험 판단', ['L3a-37', 'L3a-38', 'L3a-39']),
    ('L3a', '로그 기록량·디스크 용량 설정 조정', ['L3a-40', 'L3a-41']),
    # L3-b
    ('L3b', 'Rose Console 상태 판정·Group 조작', ['L3b-01', 'L3b-02']),
    ('L3b', '수동 절체·역절체·서비스 검증', ['L3b-03', 'L3b-04']),
    ('L3b', 'Replication·Snapshot 관리·복구', ['L3b-05', 'L3b-06', 'L3b-07']),
    ('L3b', '계획 작업·Rose 전제 조건 점검 (포트·미러 경로)', ['L3b-08', 'L3b-10', 'L3b-11']),
    ('L3b', '장애 유형별 판정·대처', ['L3b-09']),
    ('L3b', '서버 단독 실행·이중화 복귀', ['L3b-12', 'L3b-13']),
    # L3-c
    ('L3c', '차량 제원·Safety Margin 설정과 영향', ['L3c-01', 'L3c-02']),
    ('L3c', '오토블로킹 생성·Swept 검증·계산로그 판독', ['L3c-03', 'L3c-04']),
    ('L3c', 'Export JSON·MapLoad 반영·백업', ['L3c-05', 'L3c-07']),
    ('L3c', 'MapLoad 실패 조치·실 시스템 영향 판정', ['L3c-08', 'L3c-09']),
    # AUX
    ('AUX', 'DB 서비스·파일 증가 점검', ['AUX-01', 'AUX-02']),
    ('AUX', 'History Job·SQL 메모리·백업 계획 점검', ['AUX-03', 'AUX-04', 'AUX-05']),
    ('AUX', '설치 기준·반입 전 준비 체크리스트', ['AUX-06', 'AUX-11']),
    ('AUX', '기반 S/W·MSSQL 설치', ['AUX-07', 'AUX-08']),
    ('AUX', 'DB 구축·UI 배포와 오류 조치', ['AUX-09', 'AUX-10']),
    ('AUX', '방화벽 해제·CMD 진단 명령', ['AUX-12', 'AUX-15']),
    ('AUX', '서버 운영 설정 (RDP·NIC Teaming·UPS)', ['AUX-13', 'AUX-14']),
    ('AUX', '상위·차량 없는 시뮬 환경', ['AUX-16']),
    ('AUX', '무선·유선 네트워크 구조 (5GHz 채널·AP/Bridge·Turbo Ring)', ['AUX-17', 'AUX-18', 'AUX-24']),
    ('AUX', '네트워크 장비 접속·모니터 판독·Export', ['AUX-19', 'AUX-22']),
    ('AUX', 'AP/Bridge·스위치 설정 변경', ['AUX-20', 'AUX-21']),
    ('AUX', '스위치 로그로 원인 계층 판정', ['AUX-23']),
    ('AUX', 'EQ 감시 체계 구조', ['AUX-25']),
    ('AUX', 'EQ 감시 체인 검증·알람 대응', ['AUX-26', 'AUX-27']),
]

used = [i for _, _, ids in GROUPS for i in ids]
assert len(used) == len(set(used)), 'duplicate'
missing = [i for i in I if i not in used]
assert not missing, f'missing {missing}'

PREFIX = {'L1': 'L1', 'L2a': 'L2a', 'L2b': 'L2b', 'L2c': 'L2c', 'L3a': 'L3a', 'L3b': 'L3b', 'L3c': 'L3c', 'AUX': 'AUX'}
CIRC = '①②③④⑤'
counters = Counter()
new_items, idmap = [], {}
for bucket, title, ids in GROUPS:
    counters[bucket] += 1
    for i in ids:
        idmap[i] = f"{PREFIX[bucket]}-{counters[bucket]:02d}"
pat = re.compile(r'\b(L1|L2a|L2b|L2c|L3a|L3b|L3c|AUX)-(\d{2})\b')
def remap(txt):
    return pat.sub(lambda m: idmap.get(m.group(0), m.group(0)), txt) if txt else txt
for s0 in I.values():
    for f in ('content', 'objective', 'flag_note'):
        s0[f] = remap(s0[f])
counters = Counter()
for bucket, title, ids in GROUPS:
    srcs = [I[i] for i in ids]
    assert all(s['bucket'] == bucket for s in srcs), (title, [s['bucket'] for s in srcs])
    levels = {s['level'] for s in srcs}
    assert len(levels) == 1, (title, levels)
    counters[bucket] += 1
    nid = f"{PREFIX[bucket]}-{counters[bucket]:02d}"
    if len(srcs) == 1:
        s = srcs[0]
        objective = s['objective']
    else:
        objective = ' '.join(f"{CIRC[k]} {s['objective']}" for k, s in enumerate(srcs))
    def uniq(xs):
        out = []
        for x in xs:
            if x and x not in out:
                out.append(x)
        return out
    flags = uniq(f for s in srcs for f in (s.get('flags') or []))
    notes = [f"[{s['id']}] {s['flag_note']}" if len(srcs) > 1 else s['flag_note'] for s in srcs if s.get('flag_note')]
    it = OrderedDict([
        ('id', nid), ('title', title if len(srcs) > 1 else srcs[0]['title']),
        ('objective', objective),
        ('screen_or_tool', ' / '.join(uniq(s['screen_or_tool'] for s in srcs))),
        ('level', srcs[0]['level']), ('bucket', bucket),
        ('menu_tab', srcs[0]['menu_tab']),
        ('teach_mode', Counter(s['teach_mode'] for s in srcs).most_common(1)[0][0]),
        ('sources', uniq(x for s in srcs for x in (s.get('sources') or []))),
        ('source_cids', uniq(x for s in srcs for x in (s.get('source_cids') or []))),
        ('flags', flags), ('flag_note', ' / '.join(notes) or None),
        ('merged_from', ids),
        ('parts', [OrderedDict([('old_id', s['id']), ('title', s['title']), ('content', s['content']),
                                ('objective', s['objective']), ('screen_or_tool', s['screen_or_tool']),
                                ('sources', s.get('sources') or []), ('flag_note', s.get('flag_note'))]) for s in srcs]),
    ])
    new_items.append(it)

out = OrderedDict([
    ('version', 'v0.4'),
    ('items', new_items),
    ('idmap_v03_to_v04', idmap),
    ('deleted', d.get('deleted', [])),
    ('log', d.get('log', []) + [{'version': 'v0.4', 'date': '2026-10-08',
                                 'change': f"비슷한 항목 통합: 210 → {len(new_items)}. 9일 교육 + 1일 평가 구조에 맞춤. 통합 전 전문은 parts에 보존"}]),
])
json.dump(out, open('_work/items_v0.4.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('v0.4 items:', len(new_items), dict(counters))
print('levels:', Counter(i['level'] for i in new_items))
print('merged groups >=4:', [(i['id'], len(i['merged_from'])) for i in new_items if len(i['merged_from']) >= 4])
