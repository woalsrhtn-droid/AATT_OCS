import json, copy
from collections import Counter, OrderedDict

d = json.load(open('_work/wf2_result.json', encoding='utf-8'))
items = [copy.deepcopy(i) for i in d['items']]
I = {i['id']: i for i in items}
log = []


def addf(it, fl):
    s = it.get('flags') or []
    for f in fl:
        if f not in s:
            s.append(f)
    it['flags'] = s


def note(it, txt):
    cur = it.get('flag_note') or ''
    it['flag_note'] = cur + (' / ' if cur else '') + txt


ops = []
for v in d['verifies']:
    for o in (v['result'] or {}).get('ops', []):
        ops.append((v['lens'], o))

# ---- 검증자 간 충돌 판정: 적용하지 않을 op ----
SKIP = set()
for k, (lens, o) in enumerate(ops):
    # L3a-08 <- AUX-17 병합(boundary) 미적용: dup-grounding의 L3a-08 축소 채택, AUX-17은 L3a 별도 항목
    if o['op'] == 'merge' and o['ids'][:2] == ['L3a-08', 'AUX-17']:
        SKIP.add(k)
    # L2b-02 축소 edit(dup-grounding) 미적용: boundary의 L2c-20 병합 채택
    if o['op'] == 'edit' and o['ids'] == ['L2b-02'] and lens == 'dup-grounding':
        SKIP.add(k)

# ---- edit: 같은 id에 여러 edit이면 new_content가 가장 긴 것 ----
best = {}
for k, (lens, o) in enumerate(ops):
    if k in SKIP or o['op'] != 'edit':
        continue
    for iid in o['ids']:
        cur = best.get(iid)
        if cur is None or len(o.get('new_content') or '') > len(cur[1].get('new_content') or ''):
            best[iid] = (lens, o)
for k, (lens, o) in enumerate(ops):
    if k in SKIP or o['op'] != 'edit':
        continue
    for iid in o['ids']:
        it = I[iid]
        if o.get('new_title'):
            it['title'] = o['new_title']
        if o.get('new_objective'):
            it['objective'] = o['new_objective']
        if o.get('add_flags'):
            addf(it, o['add_flags'])
for iid, (lens, o) in best.items():
    if o.get('new_content'):
        I[iid]['content'] = o['new_content']
        log.append(f'edit {iid} ({lens})')
    else:
        log.append(f'edit {iid} ({lens}, 본문 변경 없음)')

# ---- flag ----
for k, (lens, o) in enumerate(ops):
    if k in SKIP or o['op'] != 'flag':
        continue
    for iid in o['ids']:
        addf(I[iid], o.get('add_flags') or [])
    log.append(f"flag {o['ids']} {o.get('add_flags')}")

# ---- move ----
seen = set()
for k, (lens, o) in enumerate(ops):
    if k in SKIP or o['op'] != 'move':
        continue
    for iid in o['ids']:
        key = (iid, o.get('to_bucket'), o.get('to_level'))
        if key in seen:
            continue
        seen.add(key)
        it = I[iid]
        if o.get('to_bucket'):
            it['bucket'] = o['to_bucket']
        if o.get('to_level'):
            it['level'] = o['to_level']
        log.append(f"move {iid} -> {it['bucket']}/{it['level']} ({lens})")

# ---- merge ----
removed = set()
for k, (lens, o) in enumerate(ops):
    if k in SKIP or o['op'] != 'merge':
        continue
    keep, *rest = o['ids']
    K = I[keep]
    for r in rest:
        R = I[r]
        K['source_cids'] = list(OrderedDict.fromkeys((K.get('source_cids') or []) + (R.get('source_cids') or [])))
        K['sources'] = list(OrderedDict.fromkeys((K.get('sources') or []) + (R.get('sources') or [])))
        addf(K, R.get('flags') or [])
        removed.add(r)
    if o.get('new_title'):
        K['title'] = o['new_title']
    if o.get('new_content'):
        K['content'] = o['new_content']
    if o.get('new_objective'):
        K['objective'] = o['new_objective']
    if o.get('add_flags'):
        addf(K, o['add_flags'])
    log.append(f"merge {keep} <- {rest} ({lens})")

# ---- 수작업 수정 (검증자가 op로 낼 수 없었던 것) ----
I['AUX-17']['bucket'] = 'L3a'
I['AUX-17']['level'] = 'L3'
log.append('move AUX-17 -> L3a (CMD로 장애 구간 분리 = L3-a 처리 역량, L3a-08 Ping 판독과 별개)')

I['AUX-13']['level'] = 'L2'
log.append('AUX-13 L1->L2 (설치 시 기준대로 설정 = L2, 운영 중 설정 변경 = L3로 AUX 기준 통일)')

I['AUX-06']['bucket'] = 'L3a'
log.append('move AUX-06 -> L3a (Parameter 조정으로 현상 해결 = L3-a)')

it = I['L1-30']
it['flags'] = [f for f in (it.get('flags') or []) if f != '버전차이']
it['flag_note'] = 'v04 10.16·중문 10.16·MXA 9.17 모두 존재(원본 확인). SxFy 본문(CEID/RCMD) 판독은 L3-a.'

it = I['L2c-10']
it['flags'] = [f for f in (it.get('flags') or []) if f != '버전차이']
it['flag_note'] = 'XComLog 경로는 설치값. HSMSHistory는 v04·중문·MXA 모두 존재(원본 확인).'

I['L1-03']['flag_note'] = (I['L1-03'].get('flag_note') or '').replace('Help>Define(L1-49)', 'Help>Define(L1-47)')
I['L1-41']['flag_note'] = '중문통합본·MXA본에는 Window>TerminalMsg 장이 없음.'

it = I['L1-15']
it['flag_note'] = ('근거 pptx 캡처 타이틀바에 현장 서버 호스트명·IP와 차량명이 보임 — 배포 시 마스킹. '
                   'Sub Vehicle Command 구성이 판본마다 다름(v04 / MXA / 2026 현장 캡처). '
                   'Clean Mode가 할당·경로에 미치는 영향은 자료 없음. 분기진입 실패 판단 후 Forcible Entry 투입 결정은 L3-a.')
addf(it, ['버전차이'])

it = I['L3b-02']
it['content'] = it['content'].replace(
    'Delete는 운영서비스를 중지해야만 가능하고 복구가 안 되므로 쓰지 않는다.',
    'Delete는 운영서비스를 중지해야만 가능하므로 운영 중에는 쓰지 않는다.')
it['objective'] = it['objective'].replace(
    'Delete를 쓰면 안 되는 이유를 설명할 수 있다',
    'Delete가 운영서비스 중지를 요구한다는 점을 들어 운영 중 사용 금지를 설명할 수 있다')

it = I['AUX-15']
it['content'] = it['content'].replace(' Rose 이중화 통신의 전제 설정이다.', '')
it['flag_note'] = 'setup 가이드 p.47 Teaming Setting 기준. 원문은 Rose·Failover를 언급하지 않음.'

it = I['L3a-36']
it['content'] = it['content'].replace(
    'Max 수치로 넣으면 경로를 찾지 못해 Noway Timeout Error(ErrorList)가 나므로 상한 전에 경로 존재를 확인하도록 판단한다.',
    'Max 수치로 넣으면 경로를 찾지 못한다(Parameter 매뉴얼 13.15). ErrorList의 Noway Timeout으로 이어질 수 있으나 '
    '원문에 직접 연결 기재는 없다. 상한 전에 경로 존재를 확인하도록 판단한다.')
addf(it, ['추정해석'])
note(it, 'Max Penalty→Noway Timeout 연결은 검증자 해석. 원문은 "경로를 찾지 못함"까지만 기재.')

I['L2b-16']['objective'] = ('HSMS 프레임·헤더 필드와 Stream별 의미를 설명하고, 지원 S/F 목록에서 메시지 방향을 짚으며, '
                            'S9F1~F7(스펙 불일치)과 S9F9(Transaction Timer time-out)를 구분해 설명할 수 있다.')

addf(I['L2c-14'], ['근거약함'])
note(I['L2c-14'], 'JunctionParam>JunctionOccupyWaitTimeOutSec은 ErrorDescription Description에만 있고 Parameter 매뉴얼 그룹 목록에는 없음.')

I['L2a-13']['content'] += (' 선행조건: 10.19 PassPointReleaseInterlock에 등록되지 않은 Point는 Pass 등록·해제 시 '
                           '"해당 포인트는 PointType을 변경할 수 없습니다" 팝업이 뜬다.')

it = I['L1-27']
it['content'] += ' 포인트 추가 시 Vehicle 진행방향을 고려하고 Unuse Point/Segment는 경로에서 제외한다(v04 p57).'
it['flag_note'] = 'RCPHMI 현상5(Resume 시 "error unhandled eventname = cyclelistcommand")는 원인 미해결.'

I['L1-43']['menu_tab'] = '메인화면'
I['L1-43']['title'] = '메인 화면 찾기·확대·결과 확인'
for k in ['L1-01', 'L1-02', 'L1-03', 'L1-05']:
    I[k]['menu_tab'] = '메인화면'
I['L1-49']['menu_tab'] = 'MCS_IF'
I['L1-50']['menu_tab'] = 'MCS_IF'

it = I['L3b-14']
addf(it, ['자료없음'])
it['flag_note'] = ('원복 절차서가 어느 자료에도 없음. 골격은 검증자 제시안 — '
                   '현업 인터뷰 + 테스트 서버 검증으로 절차서를 먼저 만들어야 평가 가능.')

# ---- Layout 탭 L1 분리 ----
src = I['L2a-18']
new_l1 = {
    'id': 'L1-NEW-LAYOUT', 'bucket': 'L1', 'level': 'L1', 'menu_tab': 'Layout',
    'title': 'Layout Setting·Check 조작',
    'content': ('Layout > Setting에서 CoordScale / BaseVehicleScale / PointScale / PointNumberScale / SegmentThickness를 '
                '사이트에 맞게 Confirm하거나 Reset한다(화면 표시 배율이며 맵 데이터는 바뀌지 않는다). '
                'Layout > Check에서 LayoutCheck를 실행하고 Message 목록을 확인한다.'),
    'objective': 'Layout>Setting으로 화면 배율을 맞추거나 Reset하고, Layout>Check를 실행해 Message 목록을 열어 볼 수 있다.',
    'screen_or_tool': '메뉴 탭 > Layout > Setting / Check', 'teach_mode': '화면실습',
    'sources': list(src.get('sources', [])), 'source_cids': ['C219', 'C220'], 'flags': ['버전차이'],
    'flag_note': 'Layout>Check는 중문통합본에 없음. Check 경고가 실제 결함인지 판정해 고치는 것은 L2-a(Layout Run 항목).',
}
src['title'] = 'Layout Run 객체 배치·수정'
src['content'] = ('Layout > Run에서 Object·Safety·Graphic을 배치하고 LEFT/TOP/WIDTH/HEIGHT/ANGLE과 좌·우·상하 정렬, '
                  '우클릭 Select로 크기를 맞춘 뒤 APPLY / UPDATE / DELETE한다. '
                  '수정 후 Layout > Check를 다시 실행해 Message로 잘못된 설정을 찾아 고친다.')
src['objective'] = 'Layout>Run에서 UI Object를 추가·정렬·UPDATE·DELETE하고, 수정 후 Layout>Check Message로 잘못된 설정을 찾아 수정할 수 있다.'
src['source_cids'] = ['C217', 'C219']
src['flag_note'] = ('Layout>Check는 중문통합본에 없음. RCPHMI 현상7의 9992~9999번 point 경고는 정답 미확정이라 '
                    '채점하지 않고 사례집으로 보냄. Layout>MapLoad는 L3-c.')
items.append(new_l1)
log.append('split L2a-18 -> L1(Layout Setting·Check 조작) + L2a(Layout Run 배치·수정)')

items = [i for i in items if i['id'] not in removed]

# ---- 재번호 ----
TAB_ORDER = ['메인화면', 'View', 'System', 'Object', 'Transfer', 'Report', 'Statistics', 'Window', 'Layout',
             'PlayBack', 'Help', 'MCS_IF']
BUCKET_ORDER = ['L1', 'L2a', 'L2b', 'L2c', 'L3a', 'L3b', 'L3c', 'AUX']


# 다른 버킷에서 옮겨온 항목은 관련 항목 바로 뒤에 둔다
ANCHOR = {'AUX-17': 'L3a-08~', 'AUX-06': 'L3a-38~', 'L3b-12': 'L3a-09~'}


def sortkey(it):
    b = BUCKET_ORDER.index(it['bucket'])
    if it['bucket'] == 'L1':
        t = it.get('menu_tab') or ''
        return (b, TAB_ORDER.index(t) if t in TAB_ORDER else 99, it['id'])
    return (b, 0, ANCHOR.get(it['id'], it['id']))


items.sort(key=sortkey)
cnt = Counter()
idmap = {}
for it in items:
    b = it['bucket']
    cnt[b] += 1
    new = f"{b}-{cnt[b]:02d}"
    idmap[it['id']] = new
    it['old_id'] = it['id']
    it['id'] = new

json.dump({'items': items, 'idmap': idmap, 'log': log},
          open('_work/items_v0.1.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\n'.join(log))
print()
print('총', len(items), ' 버킷', dict(Counter(i['bucket'] for i in items)), ' 레벨', dict(Counter(i['level'] for i in items)))
bad = [i['id'] for i in items if i['bucket'][:2] in ('L1', 'L2', 'L3') and i['bucket'][:2] != i['level']]
print('버킷-레벨 불일치:', bad)
print('L1 탭별:', dict(Counter(i.get('menu_tab') for i in items if i['bucket'] == 'L1')))
