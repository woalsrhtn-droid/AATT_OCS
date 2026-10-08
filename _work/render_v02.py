import json, re, os
from collections import Counter, OrderedDict
import openpyxl

d = json.load(open('_work/items_v0.2.json', encoding='utf-8'))
items = d['items']
I = {it['id']: it for it in items}
V = 'v0.2'
LIST = f'OCS_교육항목_레벨별_리스트_{V}.md'
DETAIL = f'OCS_교육항목_상세_{V}.md'

# ---------------- 렌더링 ----------------
SHOW = OrderedDict([('자료없음', '자료없음'), ('MXA외', 'MXA외'), ('자료충돌', '충돌'), ('병기', '병기'), ('버전차이', '버전'),
                    ('근거약함', '근거약'), ('추정해석', '추정')])


def cell(s):
    return (s or '').replace('|', '\\|').replace('\n', ' ').strip()


def tags(it):
    return ' '.join(f'`{SHOW[f]}`' for f in SHOW if f in (it.get('flags') or []))


B = OrderedDict([
    ('L1', ('L1', 'OCS 프로그램 숙지', 'OCS 레이아웃(화면)에 있는 내용을 다 다룰 수 있는가')),
    ('L2a', ('L2-a', '맵·통행영역 수정', 'Layout 같은 기능으로 맵을 수정할 수 있는가')),
    ('L2b', ('L2-b', '프로그램·시스템 구조', 'Core / PLC Driver / MCS_IF 등 구조를 아는가')),
    ('L2c', ('L2-c', '현상별 진입 경로', '문제가 생겼을 때 OCS 화면 어디를 찾아가야 하는지 아는가')),
    ('L3a', ('L3-a', '로그 분석·처리', '직접 로그를 분석하고 문제를 처리할 수 있는가')),
    ('L3b', ('L3-b', 'Rose 서버 이중화', 'Rose 이중화 프로그램을 다룰 수 있는가')),
    ('L3c', ('L3-c', 'RailTool layout 업데이트', 'RailTool로 layout을 업데이트할 수 있는가')),
    ('AUX', ('보조', '7개 목표 밖', '정기점검·네트워크 장비·설치 기준·SNMP/REST')),
])
TAB_ORDER = ['메인화면', 'View', 'System', 'Object', 'Transfer', 'Report', 'Statistics', 'Window', 'Layout',
             'PlayBack', 'Help', 'MCS_IF']

byb = OrderedDict((k, [i for i in items if i['bucket'] == k]) for k in B)
lv = Counter(i['level'] for i in items)
aux_lv = Counter(i['level'] for i in byb['AUX'])
fl = Counter(f for i in items for f in (i.get('flags') or []))

L = []
L.append(f'# OCS 교육 항목 — 레벨별 리스트 {V}')
L.append('')
L.append('> 검토용 초안 (2026-10-08). v0.1에서 미결이던 4건(기준 매뉴얼·맵 도구·에러코드·기동 순서)을 반영했습니다. 항목 수는 그대로이고, 레벨 배정과 범위가 확정되면 Section / Module 분류와 배점으로 넘어갑니다.')
L.append(f'> 항목별 교육 내용 전문과 근거 문서·페이지는 [{DETAIL}]({DETAIL})에 있습니다.')
L.append('')
L.append('## 요약')
L.append('')
L.append('| 레벨 | 목표 | 측정 질문 | 항목 수 |')
L.append('|---|---|---|---:|')
for k, (code, name, q) in B.items():
    n = len(byb[k])
    if k == 'AUX':
        n_s = f"{n} (L1 {aux_lv['L1']} · L2 {aux_lv['L2']} · L3 {aux_lv['L3']})"
    else:
        n_s = str(n)
    L.append(f'| {code} | {name} | {q} | {n_s} |')
L.append(f"| **합계** | | | **{len(items)}** (L1 {lv['L1']} · L2 {lv['L2']} · L3 {lv['L3']}) |")
L.append('')
L.append(f"LCS 체계가 105항목이었으니 약 2배입니다. Manual 폴더 8개 문서군에서 나온 후보 578개를 중복 통합한 결과이고, "
         f"이 단계에서는 일부러 줄이지 않았습니다. 빼거나 합칠 항목을 지정해 주시면 반영하겠습니다.")
L.append('')
L.append('### 표시')
L.append('')
L.append('| 표시 | 의미 | 항목 수 |')
L.append('|---|---|---:|')
desc = {'자료없음': '근거 자료가 없음 — 절차서를 새로 만들어야 평가 가능', 'MXA외': '기준판(MXA본)에 장이 없음 — v04 등 다른 판 근거. 현장 화면에 있으면 유지, 없으면 삭제',
        '자료충돌': '두 자료가 서로 다른 값·순서를 제시', '병기': '에러코드 대역을 ErrTag_L30 / ErrorDescription 두 판으로 병기 (부록 A)',
        '버전차이': 'OCS 매뉴얼 판본 외의 버전 차이 — Rose 서비스명, 프로토콜 개정, 로그 형식, .NET, 장비 구성 등',
        '근거약함': '자료가 스크린샷뿐이거나 초안 수준', '추정해석': '원자료가 "추정"으로 표기했거나 1개 사이트 표본 기반'}
for f, s in SHOW.items():
    L.append(f'| `{s}` | {desc[f]} | {fl[f]} |')
L.append(f"\n표에는 생략했지만 `사이트의존`(IP·임계값 등 사이트별 값) {fl['사이트의존']}건, "
         f"`민감정보`(호스트명·IP·계정 — 타 사이트 배포 시 마스킹) {fl['민감정보']}건이 붙어 있습니다.")
L.append('')

# 확정된 결정
L.append('## 확정된 결정 (2026-10-08)')
L.append('')
L.append('| # | 질문 | 결정 | 반영 내용 |')
L.append('|---|---|---|---|')


def ids_with(pred):
    return ', '.join(i['id'] for i in items if pred(i))


L.append(f"| 1 | 기준 매뉴얼 | **MXA본** (`_MANUAL_User Manual_V01_MXA.docx`) | MXA본에 있는 기능은 `버전` 표시를 지우고 주의 문구를 MXA본 장 번호 기준으로 고침. MXA본에 장이 없는 기능 {fl['MXA외']}건은 `MXA외`로 표시해 남김 |")
L.append(f"| 2 | 맵 도구 | **RailDesignTool** | `도구` 표시 전부 해제. LayOut Designer 절차(L2a-04 일부, L3c-06)는 뺐거나 삭제 후보로 돌림 |")
L.append(f"| 3 | 에러코드 기준 | **두 판 병기** (`260103_ErrTag_L30.xlsx` / `ErrorDescription.xlsx`) | 대역 충돌만 걸려 있던 {fl['병기']}건은 `충돌` → `병기`. 대조표는 부록 A |")
L.append(f"| 4 | 프로그램 기동 순서 | **Core만 먼저**, PlcDriver·MCS_IF 순서는 무관 | {ids_with(lambda i: i['id'] in ('L2b-04', 'L3b-12'))} 본문·채점 기준 수정, `충돌` 해제 |")
L.append('')
L.append('## 새로 확인이 필요한 것')
L.append('')
L.append('| # | 질문 | 왜 생겼나 | 걸린 항목 |')
L.append('|---|---|---|---|')
L.append(f"| A | RDT에서 만든 맵을 OCS에 어떻게 넣습니까? | RDT 매뉴얼은 Export/Import **JSON**만 있고, MXA본 Layout>MapLoad는 '**Winlay로 작성한 MDB**를 불러온다'고만 적혀 있음. 두 도구를 잇는 절차(변환 도구·메뉴·재기동·양 노드 반영)가 어느 자료에도 없음 | {ids_with(lambda i: i['id'] in ('L3c-05', 'L3c-07', 'L3c-08', 'L3c-09'))} |")
L.append(f"| B | MXA본에 없는 화면 {fl['MXA외']}건을 현장 OCS에서 쓸 수 있습니까? | Statistics 탭 전체, System>Cluster, Vehicle IO Tag, AltTransfer, Window>TerminalMsg, MCS_IF 탭 화면이 MXA본에 장이 없음. 현장 화면에 있으면 유지하고 없으면 삭제 | {ids_with(lambda i: 'MXA외' in (i.get('flags') or []))} |")
L.append(f"| C | RDT에도 맵 검증(Check Layout·Solid Detect에 해당하는 기능)이 있습니까? | 해당 절차는 LayOut Designer 기준(setup 가이드 표20)이고 RDT 매뉴얼에는 없음. 없으면 L3c-06 삭제 | L3c-06 |")
L.append('')
L.append('### 자료가 없어서 지금은 평가할 수 없는 것')
L.append('')
L.append('항목은 세워 두었지만 근거 문서가 없어 정답을 정할 수 없습니다. 교육 전에 절차서를 새로 써야 합니다.')
L.append('')
L.append(f"- **Rose 단독 실행 후 이중화 복귀** ({ids_with(lambda i: i['old_id'] == 'L3b-14')}) — 내려가는 절차만 있고 원복 절차가 어느 자료에도 없음")
L.append(f"- **RailDesignTool JSON → OCS 반영 절차와 반영 후 롤백** (L3-c) — 위 A. JSON Export까지만 근거가 있음")
L.append(f"- **로그로 원인 특정 이후의 조치 일부** (L3-a) — 합류부 점유 고착 해제, PlcCommLog WaitConnect 때 재시작 대상, 멈춘 Order 해소 순서")
L.append('')
L.append('### v0.1에서 제가 판단해서 바꾼 것 (유지)')
L.append('')
L.append(f"- **Layout 탭의 L1이 0개**였습니다. 정의상 \"맵을 바꾸지 않는 화면 조작 = L1\"이므로 Layout>Setting(화면 배율)과 Layout>Check 실행을 "
         f"L1({ids_with(lambda i: i['old_id'] == 'L1-NEW-LAYOUT')})로 떼어내고, Layout>Run 배치·수정은 L2-a({ids_with(lambda i: i['old_id'] == 'L2a-18')})에 남겼습니다.")
L.append(f"- **AUX 레벨 기준 통일**: 설치할 때 기준대로 설정하는 것은 L2, 운영 중 설정을 바꾸는 것은 L3로 맞췄습니다.")
L.append('')
L.append('---')
L.append('')


def table(rows, cols):
    out = ['| ' + ' | '.join(c[0] for c in cols) + ' |', '|' + '|'.join('---' for _ in cols) + '|']
    for r in rows:
        out.append('| ' + ' | '.join(cell(c[1](r)) if c[0] != '주의' else c[1](r) for c in cols) + ' |')
    return out


COLS_L1 = [('ID', lambda i: i['id']), ('항목', lambda i: i['title']), ('할 수 있어야 하는 것', lambda i: i['objective']), ('주의', tags)]
COLS = [('ID', lambda i: i['id']), ('항목', lambda i: i['title']), ('할 수 있어야 하는 것', lambda i: i['objective']),
        ('화면·도구', lambda i: i['screen_or_tool']), ('주의', tags)]
COLS_AUX = [('ID', lambda i: i['id']), ('레벨', lambda i: i['level']), ('항목', lambda i: i['title']),
            ('할 수 있어야 하는 것', lambda i: i['objective']), ('주의', tags)]

# L1
code, name, q = B['L1']
L.append(f'## L1 — {name} ({len(byb["L1"])}항목)')
L.append('')
L.append(f'**{q}** — 화면을 메뉴 경로로 열고, 필드·컬럼·색상 의미를 알고, 매뉴얼 절차대로 등록·조회·지령·저장을 수행한다.')
L.append('')
tabs = OrderedDict()
for t in TAB_ORDER:
    rows = [i for i in byb['L1'] if i.get('menu_tab') == t]
    if rows:
        tabs[t] = rows
L.append('| 탭 | ' + ' | '.join(tabs) + ' |')
L.append('|---|' + '|'.join('---:' for _ in tabs) + '|')
L.append('| 항목 수 | ' + ' | '.join(str(len(v)) for v in tabs.values()) + ' |')
L.append('')
for t, rows in tabs.items():
    label = {'메인화면': '메인 화면 (메뉴 밖 공통 영역)', 'MCS_IF': 'MCS_IF 프로그램 화면 (OCS 메뉴 밖)'}.get(t, f'{t} 탭')
    L.append(f'### {label}')
    L.append('')
    L += table(rows, COLS_L1)
    L.append('')

# L2, L3
for lvl, keys, desc_l in [('L2', ['L2a', 'L2b', 'L2c'], '구조를 알고 어디를 찾아가야 하는지 아는가. 맵·통행영역은 화면 기능으로 수정하되, 거동을 규정하는 Parameter 값은 바꾸지 않는다.'),
                          ('L3', ['L3a', 'L3b', 'L3c'], '직접 처리할 수 있는가. 로그 판독·원인 특정·조치, 설정값 변경, Rose 조작, 맵 실 반영 전부.')]:
    tot = sum(len(byb[k]) for k in keys)
    L.append('---')
    L.append('')
    L.append(f'## {lvl} ({tot}항목)')
    L.append('')
    L.append(desc_l)
    L.append('')
    for k in keys:
        code, name, q = B[k]
        L.append(f'### {code} {name} ({len(byb[k])}항목)')
        L.append('')
        L.append(f'**{q}**')
        L.append('')
        L += table(byb[k], COLS)
        L.append('')

L.append('---')
L.append('')
code, name, q = B['AUX']
L.append(f'## 보조 — {name} ({len(byb["AUX"])}항목)')
L.append('')
L.append(f'{q}. 발주자 7개 목표 어디에도 딱 맞지 않지만 현장 운영에 필요한 것들입니다. 설치할 때 기준대로 하는 것은 L2, 운영 중 설정을 바꾸는 것은 L3로 매겼습니다.')
L.append('')
L += table(sorted(byb['AUX'], key=lambda i: (i['level'], i['id'])), COLS_AUX)
L.append('')



def bands(f):
    ws = openpyxl.load_workbook(f, read_only=True, data_only=True).worksheets[0]
    rows = list(ws.iter_rows(values_only=True))
    h = next(i for i, r in enumerate(rows) if r and 'ErrCode' in [str(c).strip() if c else '' for c in r])
    hdr = [str(c).strip() if c else '' for c in rows[h]]
    ci, ti = hdr.index('ErrCode'), hdr.index('ErrType')
    g = OrderedDict()
    for r in rows[h + 1:]:
        try:
            c = int(r[ci])
        except (TypeError, ValueError):
            continue
        g.setdefault(r[ti], []).append(c)
    return g


A = bands('Manual/260103_ErrTag_L30.xlsx')
Bd = bands('Manual/ErrorDescription.xlsx')
order = list(A) + [t for t in Bd if t not in A]
order.sort(key=lambda t: min((A.get(t) or Bd.get(t))))


def rng(cs):
    return f"{min(cs)}~{max(cs)} ({len(cs)})" if cs else '없음'


L.append('---')
L.append('')
L.append('## 부록 A — 에러코드 대역 대조표 (두 판 병기)')
L.append('')
L.append(f"`260103_ErrTag_L30.xlsx` {sum(len(v) for v in A.values()):,}행 / `ErrorDescription.xlsx` {sum(len(v) for v in Bd.values()):,}행에서 ErrType별 ErrCode 최소~최대(행 수)를 뽑았습니다. "
         "교재에서는 두 값을 나란히 적고, 실제 판정은 사이트 System>ErrorTag 화면에 등록된 값으로 하게 합니다.")
L.append('')
L.append('| ErrType | 260103_ErrTag_L30 | ErrorDescription | 차이 |')
L.append('|---|---|---|---|')
for t in order:
    a, b = A.get(t), Bd.get(t)
    same = a and b and (min(a), max(a), len(a)) == (min(b), max(b), len(b))
    diff = '같음' if same else ('ErrTag에만 있음' if not b else ('ErrorDescription에만 있음' if not a else '**다름**'))
    L.append(f"| {t} | {rng(a)} | {rng(b)} | {diff} |")
L.append('')
L.append('ErrorDescription에만 `Description`(원인 설명) 컬럼이 있습니다. ErrTag에만 있는 코드(SYSTEMALARM, SAFETY, PING·PLCCOMM·SYSTEM의 늘어난 번호)는 설명이 없습니다.')
L.append('')

open(LIST, 'w', encoding='utf-8').write('\n'.join(L))

# ---------------- 상세 ----------------
D = [f'# OCS 교육 항목 — 상세 {V}', '',
     f'> [{LIST}]({LIST})의 항목별 교육 내용 전문, 근거 문서, 주의사항입니다. 기준 매뉴얼은 MXA본, 맵 도구는 RailDesignTool입니다.', '']
for k, (code, name, q) in B.items():
    D.append(f'## {code} {name}')
    D.append('')
    for it in byb[k]:
        D.append(f"### {it['id']} {it['title']}")
        D.append('')
        D.append(f"- **레벨**: {it['level']}  ·  **교육 방식**: {it.get('teach_mode') or '-'}" + (f"  ·  **탭**: {it['menu_tab']}" if it.get('menu_tab') else ''))
        D.append(f"- **화면·도구**: {it['screen_or_tool']}")
        D.append(f"- **교육 내용**: {it['content']}")
        D.append(f"- **할 수 있어야 하는 것**: {it['objective']}")
        D.append(f"- **근거**: {'; '.join(it.get('sources') or []) or '-'}")
        if it.get('flags'):
            D.append(f"- **표시**: {', '.join(it['flags'])}")
        if it.get('flag_note'):
            D.append(f"- **주의**: {it['flag_note']}")
        D.append('')
open(DETAIL, 'w', encoding='utf-8').write('\n'.join(D))

for f in (LIST, DETAIL):
    print(f, os.path.getsize(f), 'bytes', sum(1 for _ in open(f, encoding='utf-8')), 'lines')
print('버킷', {k: len(v) for k, v in byb.items()}, '레벨', dict(lv))
