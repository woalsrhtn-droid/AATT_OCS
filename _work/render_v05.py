import json, os
from collections import Counter, OrderedDict
import openpyxl

d = json.load(open('_work/items_v0.5.json', encoding='utf-8'))
items = d['items']
I = {it['id']: it for it in items}
V = 'v0.5'
LIST = f'OCS_교육항목_레벨별_리스트_{V}.md'
DETAIL = f'OCS_교육항목_상세_{V}.md'
SHOW = OrderedDict([('자료없음', '자료없음'), ('자료충돌', '충돌'), ('병기', '병기'), ('버전차이', '버전'),
                    ('근거약함', '근거약'), ('추정해석', '추정')])


def esc(s):
    return (s or '').replace('<', '\\<').replace('*', '\\*')


def cell(s):
    return esc(s).replace('|', '\\|').replace('\n', ' ').strip()


def tags(it):
    return ' '.join(f'`{SHOW[f]}`' for f in SHOW if f in (it.get('flags') or []))


def has_old(it, *olds):
    return any(o in it['merged_from'] for o in olds)


def ids_old(*olds):
    out = []
    for it in items:
        if has_old(it, *olds) and it['id'] not in out:
            out.append(it['id'])
    return ', '.join(out)


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
TAB_ORDER = ['메인화면', 'View', 'System', 'Object', 'Transfer', 'Report', 'Statistics', 'Window', 'Layout', 'PlayBack', 'Help', 'MCS_IF']
byb = OrderedDict((k, [i for i in items if i['bucket'] == k]) for k in B)
lv = Counter(i['level'] for i in items)
aux_lv = Counter(i['level'] for i in byb['AUX'])
fl = Counter(f for i in items for f in (i.get('flags') or []))
n_old = sum(len(i['merged_from']) for i in items)

L = [f'# OCS 교육 항목 — 레벨별 리스트 {V}', '',
     f'> 통합본 (2026-10-08). v0.3의 {n_old}항목을 비슷한 것끼리 묶어 **{len(items)}항목**으로 줄였습니다. 교육 기간 10일 중 9일에 전부 가르치고 10일차에 평가하는 구조에 맞춘 것입니다. 통합 전 항목의 전문은 상세 문서와 `_work/items_v0.5.json`의 `parts`에 그대로 남아 있어, 되돌리거나 다시 쪼갤 수 있습니다.',
     f'> 항목별 교육 내용 전문과 근거 문서·페이지는 [{DETAIL}]({DETAIL})에 있습니다. LCS 역량 체계 양식(Section / Module / Category)과 배점·일정은 아래 "역량 체계 구조"에 있습니다.', '',
     '## 요약', '', '| 레벨 | 목표 | 측정 질문 | v0.3 | v0.4 |', '|---|---|---|---:|---:|']
for k, (code, name, q) in B.items():
    n = len(byb[k]); o = sum(len(i['merged_from']) for i in byb[k])
    n_s = f"{n} (L1 {aux_lv['L1']} · L2 {aux_lv['L2']} · L3 {aux_lv['L3']})" if k == 'AUX' else str(n)
    L.append(f'| {code} | {name} | {q} | {o} | {n_s} |')
L.append(f"| **합계** | | | **{n_old}** | **{len(items)}** (L1 {lv['L1']} · L2 {lv['L2']} · L3 {lv['L3']}) |")
L += ['', '통합 원칙: 같은 화면·같은 도구·같은 종류의 판독을 하나로 묶고, 묶인 항목의 "할 수 있어야 하는 것"은 ①②③으로 나란히 둡니다. 내용은 하나도 빼지 않았습니다. 레벨이 다른 항목끼리는 묶지 않았습니다.', '',
      '### 표시', '', '| 표시 | 의미 | 항목 수 |', '|---|---|---:|']
desc = {'자료없음': '근거 자료가 없음 — 절차서를 새로 만들어야 평가 가능', '자료충돌': '두 자료가 서로 다른 값·순서·화면 유무를 제시', '병기': '에러코드 대역을 ErrTag_L30 / ErrorDescription 두 판으로 병기 (부록 A)',
        '버전차이': '사용자 매뉴얼 판본 외의 버전 차이 — Rose 서비스명, 프로토콜 개정, 로그 형식, .NET, 장비 구성 등',
        '근거약함': '자료가 스크린샷뿐이거나 초안 수준', '추정해석': '원자료가 "추정"으로 표기했거나 1개 사이트 표본 기반'}
for f, s in SHOW.items():
    L.append(f'| `{s}` | {desc[f]} | {fl[f]} |')
L += [f"\n표에는 생략했지만 `사이트의존`(IP·임계값 등 사이트별 값) {fl['사이트의존']}건, `민감정보`(호스트명·IP·계정 — 타 사이트 배포 시 마스킹) {fl['민감정보']}건이 붙어 있습니다.", '']

# ---------------- 역량 체계 구조 ----------------
L += ['## 역량 체계 구조 (LCS 양식 기준)', '',
      'LCS_Training_Competency_System 파일과 같은 구조입니다. Section 9개 → Module → Category(=항목) → Training Item(체크리스트 문구). 배점은 9일차 지식 테스트의 섹션별 만점(합계 100)이며 셋업에 30점을 두었습니다. Extended 항목은 배점 0입니다. 10일차 실기 100점은 별도 배점표(아래)로 매깁니다.', '',
      '| # | Section | 한글 | Module (항목 수) | Core | Ext | 레벨 구성 | 배점 |', '|---|---|---|---|---:|---:|---|---:|']
for n, s in enumerate(d['sections'], 1):
    ids = [i for m in s['modules'] for i in m['items']]
    lvc = Counter(I[i]['level'] for i in ids)
    mods = ' · '.join(f"{m['module']} ({len(m['items'])})" for m in s['modules'])
    nc = sum(1 for i in ids if I[i]['scope'] == 'Core'); ne = len(ids) - nc
    L.append(f"| {n} | {s['section']} | {s['section_kr']} | {mods} | {nc} | {ne} | " + ' '.join(f"{k} {lvc[k]}" for k in ('L1', 'L2', 'L3') if lvc[k]) + f" | {s['max_marks']} |")
L.append(f"| | **합계** | | | **{sum(1 for i in items if i['scope']=='Core')}** | **{sum(1 for i in items if i['scope']=='Extended')}** | | **{sum(s['max_marks'] for s in d['sections'])}** |")
L += ['', '### 10일차 실기 배점 (회사 제안서 구조)', '', '| 실기 과제 | 배점 | 증빙 | 필수 요건 |', '|---|---:|---|---|']
for t in d['practical_tasks']:
    L.append(f"| {t[0]} | {t[1]} | {t[2]} | {t[3]} |")
L += ['', '합격 규칙(제안): ' + ' · '.join(f'{k} = {v}' for k, v in d['pass_rule'].items()), '']
L += ['### 10일 일정 (회사 제안서 양식: 09–12 설명·시연 / 13–15 실습 / 15–16 복습·테스트)', '', '| 일차 | 날짜 | 모듈 | 설명·시연 | 실습 | 복습·테스트 | 산출물 | 항목 |', '|---|---|---|---|---|---|---|---|']
for s in d['schedule']:
    L.append(f"| {s['day']} | {s['date']} | {cell(s['module'])} | {cell(s['explain'])} | {cell(s['hands_on'])} | {cell(s['review'])} | {cell(s['deliverable'])} | {', '.join(s['items']) or '-'} |")
nc = sum(1 for i in items if i['scope'] == 'Core')
L += ['', f"교육 9일 × 6시간 = 54시간을 Core {nc}항목에 쓰면 항목당 평균 약 {54*60//nc}분입니다. 1~3일차가 셋업(서버·DB·설치·사이트 구성)이고, 6일차(맵 12항목)와 8일차(알람·진입점 12항목)가 가장 빡빡합니다.", '']

# ---------------- 결정·확인 사항 ----------------
L += ['## 확정된 결정 (2026-10-08)', '', '| # | 질문 | 결정 | 반영 내용 |', '|---|---|---|---|',
      "| 1 | 기준 매뉴얼 | **사용자 매뉴얼 3판 모두** (v04 / 중문통합 / MXA — 사실상 동일) | 판본 차이 표시를 지움. 사용자 매뉴얼에 없는 화면(MCS_IF, AltTransfer)은 아래 A·C로 확인 |",
      "| 2 | 맵 도구 | **RailDesignTool** | LayOut Designer 절차는 뺐거나 삭제(v0.3 L3c-06) |",
      f"| 3 | 에러코드 기준 | **두 판 병기** (`260103_ErrTag_L30.xlsx` / `ErrorDescription.xlsx`) | 대역 충돌 항목은 `병기`로 표시. 대조표는 부록 A |",
      f"| 4 | 프로그램 기동 순서 | **Core만 먼저**, PlcDriver·MCS_IF 순서는 무관 | {ids_old('L2b-04', 'L3b-12')} 본문·채점 기준 수정 |",
      f"| 5 | RDT 맵의 OCS 반영 | **Winlay 맵과 같은 절차로 OCS Layout>MapLoad** | {ids_old('L3c-05', 'L3c-07', 'L3c-08', 'L3c-09')}의 `자료없음` 해제. 반영 체인은 RDT 작도 → 오토블로킹 → JSON Export → Layout>MapLoad |",
      f"| 6 | RDT 맵 검증 기능 | **없음** | v0.3 L3c-06 삭제 — 부록 B. OCS 화면 Layout>Check는 {ids_old('L1-44')}·{ids_old('L2a-18')}에 유지 |",
      '', '## 새로 확인이 필요한 것', '', '| # | 질문 | 왜 생겼나 | 걸린 항목 |', '|---|---|---|---|',
      f"| A | 현장 MCS_IF에 화면(창)이 있습니까? | MCS_IF 화면은 사용자 매뉴얼에 없고 setup 가이드·설치 기준서에만 있음. MXA본은 MCS_IF를 '사용자 Interface가 없고, 내부적으로 구동'으로 적음 | {ids_old('L1-50', 'L1-51', 'L2b-01', 'L2b-06', 'L2b-20', 'L2c-19')} |",
      f"| B | MapLoad에서 고르는 파일은 MDB입니까, RDT JSON입니까? | 매뉴얼 원문은 MDB 선택으로 적고 RDT 산출물은 JSON. 실습 전에 확인하면 되고 항목 구성에는 영향 없음 | {ids_old('L3c-07', 'L3c-08')} |",
      f"| C | 현장에 System>AltTransfer 화면이 있습니까? | 사용자 매뉴얼 3판에는 화면 장이 없고 setup 가이드 5.10에만 있음 | {ids_old('L2b-31')} |",
      '', '### 자료가 없어서 지금은 평가할 수 없는 것', '',
      f"- **Rose 단독 실행 후 이중화 복귀** ({ids_old('L3b-13')} 중 ②) — 내려가는 절차만 있고 원복 절차가 어느 자료에도 없음",
      f"- **맵 반영 후 롤백** ({ids_old('L3c-07', 'L3c-09')}) — 항목은 평가하되 롤백 부분만 제외",
      f"- **로그로 원인 특정 이후의 조치 일부** ({ids_old('L3a-06', 'L3a-15', 'L3a-27')}) — 합류부 점유 고착 해제, PlcCommLog WaitConnect 때 재시작 대상, 멈춘 Order 해소 순서",
      '', '---', '']


def table(rows, cols):
    out = ['| ' + ' | '.join(c[0] for c in cols) + ' |', '|' + '|'.join('---' for _ in cols) + '|']
    for r in rows:
        out.append('| ' + ' | '.join(cell(c[1](r)) if c[0] != '주의' else c[1](r) for c in cols) + ' |')
    return out


old = lambda i: ', '.join(i['merged_from'])
secmod = lambda i: f"{i['section']} / {i['module']}"
scope = lambda i: ('Core D' + str(i['day'])) if i['scope'] == 'Core' else 'Ext'
COLS_L1 = [('ID', lambda i: i['id']), ('항목', lambda i: i['title']), ('할 수 있어야 하는 것', lambda i: i['objective']), ('Section / Module', secmod), ('범위', scope), ('v0.3 ID', old), ('주의', tags)]
COLS = [('ID', lambda i: i['id']), ('항목', lambda i: i['title']), ('할 수 있어야 하는 것', lambda i: i['objective']), ('화면·도구', lambda i: i['screen_or_tool']), ('Section / Module', secmod), ('범위', scope), ('v0.3 ID', old), ('주의', tags)]
COLS_AUX = [('ID', lambda i: i['id']), ('레벨', lambda i: i['level']), ('항목', lambda i: i['title']), ('할 수 있어야 하는 것', lambda i: i['objective']), ('Section / Module', secmod), ('범위', scope), ('v0.3 ID', old), ('주의', tags)]

code, name, q = B['L1']
L += [f'## L1 — {name} ({len(byb["L1"])}항목)', '', f'**{q}** — 화면을 메뉴 경로로 열고, 필드·컬럼·색상 의미를 알고, 매뉴얼 절차대로 등록·조회·지령·저장을 수행한다.', '']
tabs = OrderedDict((t, [i for i in byb['L1'] if i.get('menu_tab') == t]) for t in TAB_ORDER if any(i.get('menu_tab') == t for i in byb['L1']))
L += ['| 탭 | ' + ' | '.join(tabs) + ' |', '|---|' + '|'.join('---:' for _ in tabs) + '|', '| 항목 수 | ' + ' | '.join(str(len(v)) for v in tabs.values()) + ' |', '']
for t, rows in tabs.items():
    label = {'메인화면': '메인 화면 (메뉴 밖 공통 영역)', 'MCS_IF': 'MCS_IF 프로그램 화면 (OCS 메뉴 밖)', 'View': 'View·화면 표시 설정'}.get(t, f'{t} 탭')
    L += [f'### {label}', '']
    if t == 'MCS_IF':
        L += ["> 현장 MCS_IF 화면 유무 확인 필요 — 위 '새로 확인이 필요한 것' A. 확인 전까지 `충돌`로 둡니다.", '']
    L += table(rows, COLS_L1) + ['']
for lvl, keys, desc_l in [('L2', ['L2a', 'L2b', 'L2c'], '구조를 알고 어디를 찾아가야 하는지 아는가. 맵·통행영역은 화면 기능으로 수정하되, 거동을 규정하는 Parameter 값은 바꾸지 않는다.'),
                          ('L3', ['L3a', 'L3b', 'L3c'], '직접 처리할 수 있는가. 로그 판독·원인 특정·조치, 설정값 변경, Rose 조작, 맵 실 반영 전부.')]:
    L += ['---', '', f'## {lvl} ({sum(len(byb[k]) for k in keys)}항목)', '', desc_l, '']
    for k in keys:
        code, name, q = B[k]
        L += [f'### {code} {name} ({len(byb[k])}항목)', '', f'**{q}**', ''] + table(byb[k], COLS) + ['']
L += ['---', '', f'## 보조 — 7개 목표 밖 ({len(byb["AUX"])}항목)', '', '정기점검·네트워크 장비·설치 기준·SNMP/REST. 설치할 때 기준대로 하는 것은 L2, 운영 중 설정을 바꾸는 것은 L3로 매겼습니다.', '']
L += table(sorted(byb['AUX'], key=lambda i: (i['level'], i['id'])), COLS_AUX) + ['']


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


A = bands('Manual/260103_ErrTag_L30.xlsx'); Bd = bands('Manual/ErrorDescription.xlsx')
order = sorted(list(A) + [t for t in Bd if t not in A], key=lambda t: min((A.get(t) or Bd.get(t))))
rng = lambda cs: f"{min(cs)}~{max(cs)} ({len(cs)})" if cs else '없음'
L += ['---', '', '## 부록 A — 에러코드 대역 대조표 (두 판 병기)', '',
      f"`260103_ErrTag_L30.xlsx` {sum(len(v) for v in A.values()):,}행 / `ErrorDescription.xlsx` {sum(len(v) for v in Bd.values()):,}행에서 ErrType별 ErrCode 최소~최대(행 수)를 뽑았습니다. 교재에서는 두 값을 나란히 적고, 실제 판정은 사이트 System>ErrorTag 화면에 등록된 값으로 하게 합니다.", '',
      '| ErrType | 260103_ErrTag_L30 | ErrorDescription | 차이 |', '|---|---|---|---|']
for t in order:
    a, b = A.get(t), Bd.get(t)
    same = a and b and (min(a), max(a), len(a)) == (min(b), max(b), len(b))
    diff = '같음' if same else ('ErrTag에만 있음' if not b else ('ErrorDescription에만 있음' if not a else '**다름**'))
    L.append(f"| {t} | {rng(a)} | {rng(b)} | {diff} |")
L += ['', '## 부록 B — 삭제한 항목', '', '| v0.3 ID | 항목 | 할 수 있어야 하는 것 (삭제 전) | 삭제 이유 |', '|---|---|---|---|']
for x in d.get('deleted', []):
    L.append(f"| {x['id']} | {cell(x['title'])} | {cell(x['objective'])} | {cell(x['deleted_reason'])} |")
L += ['', '## 부록 C — v0.3 → v0.4 ID 대응표', '', '| v0.4 ID | 항목 | v0.3 ID |', '|---|---|---|']
for it in items:
    L.append(f"| {it['id']} | {cell(it['title'])} | {', '.join(it['merged_from'])} |")
L.append('')
open(LIST, 'w', encoding='utf-8').write('\n'.join(L))

# ---------------- 상세 ----------------
D = [f'# OCS 교육 항목 — 상세 {V}', '',
     f'> [{LIST}]({LIST})의 항목별 교육 내용 전문, 근거 문서, 주의사항입니다. 통합된 항목은 통합 전 항목(v0.3 ID)별로 교육 내용을 그대로 나눠 실었습니다. 범위 Core는 10일 교육·평가 대상, Extended는 자료로만 넘기는 항목입니다. 기준 매뉴얼은 사용자 매뉴얼 3판(v04 / 중문통합 / MXA), 맵 도구는 RailDesignTool입니다.', '']
for k, (code, name, q) in B.items():
    D += [f'## {code} {name}', '']
    for it in byb[k]:
        D += [f"### {it['id']} {esc(it['title'])}", '',
              f"- **레벨**: {it['level']}  ·  **교육 방식**: {it.get('teach_mode') or '-'}" + (f"  ·  **탭**: {it['menu_tab']}" if it.get('menu_tab') else '') + f"  ·  **Section / Module**: {it['section']} / {it['module']}  ·  **범위**: {it['scope']}" + (f"  ·  **교육 일차**: {it['day']}" if it['day'] else ''),
              f"- **화면·도구**: {esc(it['screen_or_tool'])}",
              f"- **할 수 있어야 하는 것**: {esc(it['objective'])}"]
        if it.get('flags'):
            D.append(f"- **표시**: {', '.join(it['flags'])}")
        if it.get('flag_note'):
            D.append(f"- **주의**: {esc(it['flag_note'])}")
        D.append('')
        for p in it['parts']:
            head = f"**{p['old_id']} {esc(p['title'])}**" if len(it['parts']) > 1 else '**교육 내용**'
            D += [f"- {head}", f"  - 내용: {esc(p['content'])}"]
            if len(it['parts']) > 1:
                D.append(f"  - 할 수 있어야 하는 것: {esc(p['objective'])}")
            D.append(f"  - 근거: {esc('; '.join(p.get('sources') or [])).replace('_', chr(92) + '_') or '-'}")
        D.append('')
open(DETAIL, 'w', encoding='utf-8').write('\n'.join(D))
for f in (LIST, DETAIL):
    print(f, os.path.getsize(f), 'bytes', sum(1 for _ in open(f, encoding='utf-8')), 'lines')
