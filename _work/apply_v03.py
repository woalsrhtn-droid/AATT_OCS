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

# ---------------------------------------------------------------- 검증 반영 (원문 충실도 / 결정 위반 sweep / 렌더 정합성)
# AltTransfer: 사용자 매뉴얼에는 화면 장이 없다(v04·MXA는 HandleAltTransferOrder 파라미터뿐) → MCS_IF와 같은 확인 질문
note('L2b-31', 'System>AltTransfer 화면은 사용자 매뉴얼 3판에 없고 setup 가이드 5.10(AltTransfer 등록 및 확인)에만 있다. v04본·MXA본에는 OrderControlParam의 '
               'HandleAltTransferOrder(AltPort Order Handling) 파라미터만 있다. 현장 화면 유무 확인 필요. 경유지 반송이 있는 사이트에만 해당.')
flags('L2b-31', add=['자료충돌'])
# 출처 오기: EntranceLimit·Info/Setting 구분은 RCP_Parameter_Manual에만 있다
note('L2b-30', 'Cluster 화면은 v04본·중문통합본 근거, EntranceLimit 필드 설명은 RCP_Parameter_Manual_v0.0.1 Cluster(Info) 근거(사용자 매뉴얼 3판의 Cluster Info에는 EntranceLimit 없음). '
               '나머지 Parameter 설명은 OCS Parameter 매뉴얼 근거. PushWeight·UseBothWay 등의 값을 조정해 현상을 해결하는 일은 L3-a. PushWeight 미동작 건은 RCPHMI에 미해결로 남아 있다.')
sub('L2a-11', 'flag_note', 'v04본·중문통합본 근거. ',
    'System>Cluster 화면·Point/Dest Point 조작·Simulation 경고는 v04본·중문통합본 7.2 근거. Info/Setting 구분, EntranceLimit, MaxVehicleCount=1 예시는 RCP_Parameter_Manual_v0.0.1 Cluster 근거(사용자 매뉴얼 Cluster Info에는 EntranceLimit 없음). ')
# MCS_IF 화면: 원문 인용을 정확히, 같은 화면에 기대는 항목 모두 표시
MCSIF2 = (' MCS_IF 프로그램 화면은 사용자 매뉴얼 3판에 없고 setup 가이드·설치 기준서에만 있다. MXA본 2.2(프로그램 구성도)는 "RCP GT를 제외한 프로그램들은 사용자 Interface가 없고, '
          '내부적으로 구동되고 있는 프로그램"이라 적고 있어(MCS_IF 포함) 현장 MCS_IF 화면 유무를 확인해야 한다.')
for iid in ['L1-50', 'L1-51']:
    sub(iid, 'flag_note', MCSIF, MCSIF2)
for iid in ['L2b-06', 'L2b-20', 'L2c-19']:
    I[iid]['flag_note'] = (I[iid].get('flag_note') or '') + MCSIF2
    flags(iid, add=['자료충돌'])
sub('L2b-01', 'content', 'RCP GT를 뺀 나머지는 UI 없이 내부 구동되므로 거동은 로그·Help>Version·SystemInfo로 간접 확인한다.',
    'MXA본 2.2는 RCP GT 외 프로그램을 "사용자 Interface가 없고, 내부적으로 구동"되는 프로그램으로 적으며, 그 거동은 로그·Help>Version·SystemInfo로 간접 확인한다.')
I['L2b-01']['flag_note'] += ' MCS_IF는 setup 가이드·설치 기준서에 자체 화면이 나와 MXA본 서술과 다르다 — 현장 MCS_IF 화면 유무 확인 필요(L1-50·L1-51과 같음).'
# 맵 반영: 화면·도구 칸과 본문을 Layout>MapLoad로 통일, 파일 형식은 미결
sub('L3c-07', 'content', '반영 메뉴 경로는 자료마다 다르게 표기된다(Layout > MapLoad: MDB 선택·BackupPath·MDB → UPDATE / Core > System 탭 > MabLoad: Map 선택·백업 폴더·MDB -> SQL / System -> MapLoad: MDB File Path·BackupPath·(MDB->SQL)). 어느 경로든 MDB 파일과 BackupPath(백업 폴더)를 지정한 뒤 MDB->SQL(UPDATE)로 맵을 SQL DB에 적재한다.',
    '메뉴는 Layout > MapLoad다(MXA본 11장: 파일 선택·BackupPath·UPDATE). 다른 자료에는 Core > System 탭 > MabLoad(setup 가이드: Map 선택·백업 폴더·MDB -> SQL), '
    'System -> MapLoad(설치 기준서: MDB File Path·BackupPath·MDB->SQL)로도 적혀 있다. 맵 파일과 BackupPath(백업 폴더)를 지정한 뒤 UPDATE(MDB->SQL)로 맵을 SQL DB에 적재한다.')
sub('L3c-07', 'content', '지정한 MDB의 저장 날짜·파일 이름', '지정한 맵 파일의 저장 날짜·파일 이름')
sub('L3c-07', 'content', '복귀에 쓸 직전 MDB와 백업 위치', '복귀에 쓸 직전 맵 파일과 백업 위치')
I['L3c-07']['objective'] = ('테스트 서버에서 Layout>MapLoad로 맵 파일과 BackupPath를 지정해 반영(UPDATE)을 수행하고, 반영 전 맵 파일 저장 날짜·파일명 확인과 반영 후 백업 폴더 생성 확인을 '
                            '빠뜨리지 않으며, 복귀에 쓸 직전 맵 파일과 백업 위치를 지목할 수 있다.')
I['L3c-07']['screen_or_tool'] = 'OCS Layout > MapLoad (맵 파일 선택, BackupPath, UPDATE) — 다른 표기: System -> MapLoad, Core > System 탭 > MabLoad'
sub('L3c-07', 'flag_note', '실패하면 전 라인에 영향을 주므로 실습은 테스트 서버로 제한한다.',
    'MapLoad는 운영 SQL DB의 맵을 바꾸는 작업이므로(setup 가이드 5.1 \'DB에 MDB 파일 적용으로 현장에 맞는 MAP 등록\') 실습은 테스트 서버로 제한한다.')
I['L3c-08']['screen_or_tool'] = 'AccessDatabaseEngine 설치본, OCS Layout > MapLoad'
sub('L3c-09', 'screen_or_tool', 'OCS System -> MapLoad', 'OCS Layout > MapLoad')
sub('L3c-09', 'content', 'MapLoad(MDB->SQL)는', 'Layout>MapLoad(UPDATE)는')
sub('L2a-04', 'screen_or_tool', ' / LayOut Designer', '')
# v0.2(MXA본 단일 기준)의 잔재
sub('L1-16', 'flag_note', 'Sub Vehicle Command 구성은 MXA본 7.3.2 기준으로 가르치고',
    'Sub Vehicle Command 구성은 사용자 매뉴얼(v04본 8.3 아이콘표, MXA본 7.3.2·중문통합본 같은 설명) 기준으로 가르치고')
sub('L1-32', 'content', 'v04 p76, 중문통합본 없음', 'v04 p76·MXA본 9.19')
sub('L3a-11', 'flag_note', 'FailOverHistory는 중문통합본에 없음.', 'FailOverHistory는 v04본 10.17·MXA본 9.19 근거.')
sub('L3b-04', 'flag_note', 'FailOverHistory는 중문통합본에 없음.', 'FailOverHistory는 v04본 10.17·MXA본 9.19 근거.')
sub('L1-14', 'content', 'Parameter(MXA본 15그룹)는', 'Parameter(사용자 매뉴얼 기준 16그룹 — MXA본 6.10의 15그룹에 v04본 DBInterfaceParam)는')
note('L1-14', 'v04본은 DBInterfaceParam 포함 16그룹, MXA본 6.10은 15그룹. 현장 화면의 그룹 수로 대조한다.')
sub('L2b-29', 'content', 'BlockingParam / DatabaseParam / HostParam / LogParam', 'BlockingParam / DatabaseParam / DBInterfaceParam / HostParam / LogParam')
sub('L2b-29', 'content', '15그룹이다(MXA본 6.10 기준). v04본은 DBInterfaceParam을 더해 16그룹, Parameter 매뉴얼은',
    '16그룹이다(v04본 기준, MXA본 6.10은 DBInterfaceParam 없이 15그룹). Parameter 매뉴얼은')
sub('L2b-29', 'flag_note', '그룹 목록은 MXA본 15그룹 기준.', '그룹 목록은 사용자 매뉴얼 기준 16그룹(MXA본 6.10의 15그룹 + v04본 DBInterfaceParam). 현장 화면의 그룹 수로 대조한다.')
# 번호 재매김 후 갱신되지 않은 교차참조
sub('L3b-04', 'content', '그 판독은 L3a-34에서 평가한다', '그 판독은 L3a-36에서 평가한다')
sub('L2a-16', 'content', '배출 가능 상태 5조건 판정은 L1-21에서 다룬다', '배출 가능 상태 5조건 판정은 L1-22에서 다룬다')
sub('L3b-10', 'content', 'NIC Teaming 설정은 AUX-15에서 다룬다', 'NIC Teaming 설정은 AUX-14에서 다룬다')

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
