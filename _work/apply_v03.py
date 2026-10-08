"""v0.2 -> v0.3: 2026-10-08 사이트 확인 반영.

1. 기준 매뉴얼 = 사용자 매뉴얼 3판(v04 / 중문통합 / MXA) 모두 -> 'MXA외' 표시 해제
   사용자 매뉴얼에 있는 화면은 현장에 있다고 본다(Cluster, Vehicle IO Tag, AltTransfer, TerminalMsg, Statistics)
2. RDT로 만든 맵은 Winlay 맵과 같은 절차로 OCS Layout 탭(MapLoad)에서 반영 -> L3-c '자료없음' 해소
3. RDT에는 맵 검증 기능이 없음 -> L3c-06(LayOut Designer Check Layout·Solid Detect) 삭제
"""
import json

d = json.load(open('_work/items_v0.2.json', encoding='utf-8'))
items = d['items']
I = {it['id']: it for it in items}
SITE = '2026-10-08 사이트 확인'


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


# ---------------------------------------------------------------- 1. 사용자 매뉴얼 3판 모두 기준
for it in items:
    flags(it['id'], remove=['MXA외'])

note('L1-17', 'System>Vehicle IO Tag는 v04본 근거. Home Point 필드는 RCPHMI 메모의 \'필요한 듯\'·save 불가 기록뿐이라 평가 문항에서 제외하고 위치 인지만. IO 비트로 차량 이상을 판정하는 것은 L3-a.')
note('L1-34', 'Statistics는 v04본 근거(MXA본에는 상세 장이 없음). L1-35~37도 같음.')
sub('L1-35', 'flag_note', 'MXA본 Statistics 장 없음(v04 근거).', 'v04본 근거.')
sub('L1-36', 'flag_note', 'MXA본 Statistics 장 없음(v04 근거).', 'v04본 근거.')
note('L1-37', 'v04본 근거.')
note('L1-42', 'TerminalMsg는 v04본, Docking Setting은 MXA본 10.6 근거.')
sub('L2a-11', 'flag_note', 'MXA본 6장에 System>Cluster 장이 없음(v04 근거). ', 'v04본·중문통합본 근거. ')
sub('L2b-13', 'flag_note', 'IO Tag 부분은 MXA본에 장이 없음(v04 근거).', 'IO Tag 부분은 v04본 근거.')
sub('L2b-30', 'flag_note', 'Cluster EntranceLimit 부분은 MXA본에 장이 없음(v04 근거). 나머지 Parameter는 MXA본 6.10에 있음.',
    'Cluster EntranceLimit 부분은 v04본 근거, 나머지 Parameter는 MXA본 6.10 근거.')
note('L2b-31', 'System>AltTransfer는 v04본 근거. 경유지 반송이 있는 사이트에만 해당.')

# MCS_IF 프로그램 화면: 사용자 매뉴얼에 없고 setup 가이드·설치 기준서에만 있음 → 확인 질문으로 남김
MCSIF = (' MCS_IF 프로그램 화면은 사용자 매뉴얼 3판에 없고 setup 가이드·설치 기준서에만 있다. MXA본은 MCS_IF를 \'UI 없이 내부 구동\'으로 적고 있어(2.2) '
         '현장 MCS_IF 화면 유무를 확인해야 한다.')
for iid in ['L1-50', 'L1-51']:
    sub(iid, 'flag_note', ' MXA본에는 MCS_IF 탭 장이 없음(v04/setup 가이드 근거).', MCSIF)
    flags(iid, add=['자료충돌'])

# ---------------------------------------------------------------- 2. RDT 맵 → OCS Layout>MapLoad
ROUTE = f'RDT로 만든 맵도 Winlay로 만든 맵과 같은 절차로 OCS Layout 탭 MapLoad에서 반영한다({SITE}).'

flags('L3c-05', remove=['자료없음'])
note('L3c-05', f'Export한 결과물을 OCS에 넣는 것은 L3c-07(Layout>MapLoad)이다. {ROUTE} 경로 E:\\test.json은 예시다.')

sub('L3c-07', 'content', '반영 메뉴 경로는 자료마다 다르게 표기된다', f'{ROUTE} 반영 메뉴 경로는 자료마다 다르게 표기된다')
flags('L3c-07', remove=['자료없음'])
note('L3c-07', '메뉴는 MXA본 11장 기준 Layout>MapLoad(파일 선택·BackupPath·UPDATE). 매뉴얼 원문은 선택 파일을 MDB로 적고 RDT 산출물은 JSON(Export Json File)이므로, '
               '현장 MapLoad 화면에서 고르는 파일 형식을 실습 전에 확인한다. 백업에서 되돌리는 롤백 절차는 어느 자료에도 없다. 실패하면 전 라인에 영향을 주므로 실습은 테스트 서버로 제한한다.')

flags('L3c-08', remove=['자료없음'])
note('L3c-08', 'AccessDatabaseEngine은 MDB를 읽는 MapLoad 전제 조건이다(setup 가이드 3.5). RDT 맵도 같은 MapLoad로 반영하므로 이 점검을 적용하되, '
               '현장에서 MapLoad에 넣는 파일이 MDB가 아니면 AccessDatabaseEngine이 관여하는지 확인한다.')

sub('L3c-09', 'content', '(RDT 작도 → 오토블로킹 → JSON Export → OCS 반영)', '(RDT 작도 → 오토블로킹 → JSON Export → OCS Layout>MapLoad 반영)')
flags('L3c-09', remove=['자료없음'])
note('L3c-09', f'이 기준은 조사자가 매뉴얼을 종합해 만든 것이다. {ROUTE} 반영 후 롤백 절차는 자료에 없으므로 \'실 반영 전 백업·테스트 서버 선행\'까지만 채점한다.')

# ---------------------------------------------------------------- 3. L3c-06 삭제
deleted = [it for it in items if it['id'] == 'L3c-06']
d['items'] = [it for it in items if it['id'] != 'L3c-06']
d.setdefault('deleted', []).extend(
    {**it, 'deleted_reason': f'RailDesignTool에는 맵 검증 기능(Check Layout·Solid Detect)이 없음({SITE}). LayOut Designer 기준 절차라 현 사이트 도구에 해당 없음. '
                             'OCS 화면 Layout>Check는 L1-44·L2a-18에 그대로 있음.', 'deleted_in': '0.3'} for it in deleted)

d['log'].append({'v': '0.3', 'date': '2026-10-08', 'decisions': {
    '기준 매뉴얼': '사용자 매뉴얼 3판(v04/중문통합/MXA) 모두. 사용자 매뉴얼에 있는 화면은 현장에 있다고 봄',
    'RDT 맵 반영': 'Winlay 맵과 동일하게 OCS Layout>MapLoad', 'RDT 맵 검증': '없음 → L3c-06 삭제'}})

json.dump(d, open('_work/items_v0.3.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ---------------------------------------------------------------- 점검
import re
from collections import Counter
print(Counter(f for it in d['items'] for f in it.get('flags') or []))
print('항목 수', len(d['items']), '삭제', [x['id'] for x in d['deleted']])
txt = lambda it: ' '.join(str(it.get(f) or '') for f in ('content', 'objective', 'flag_note', 'screen_or_tool'))
print('L3c-06 참조 남음:', [it['id'] for it in d['items'] if 'L3c-06' in txt(it)])
print('MXA 부재 문구 남음:', [it['id'] for it in d['items'] if re.search(r'MXA본(?:에는|에)?[^.]{0,25}(?:장이 )?없', txt(it)) and it['id'] not in ('L1-34',)])
print('자료없음 남음:', [it['id'] for it in d['items'] if '자료없음' in (it.get('flags') or [])])
print('미확정 표현 남음:', [it['id'] for it in d['items'] if re.search(r'어느 자료에도 없다\.?$|경로[^.]*자료에 없', it.get('flag_note') or '') and it['bucket'] == 'L3c'])
