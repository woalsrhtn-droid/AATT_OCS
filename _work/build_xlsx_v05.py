"""회사 제안서(RCP_Training_Plan_19-30_Oct_2026.xlsx) 양식으로 재민 트레이너 버전 엑셀을 새로 만든다. 원본은 건드리지 않는다."""
import json, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

d = json.load(open('_work/items_v0.5.json', encoding='utf-8'))
items = d['items']; I = {i['id']: i for i in items}
F = 'Arial'
H1 = Font(name=F, size=14, bold=True, color='FFFFFF'); H2 = Font(name=F, size=11, bold=True, color='FFFFFF')
B = Font(name=F, size=10, bold=True); N = Font(name=F, size=10); SM = Font(name=F, size=9, italic=True, color='555555')
NAVY = PatternFill('solid', fgColor='1F3864'); BLUE = PatternFill('solid', fgColor='2F5597'); GREY = PatternFill('solid', fgColor='D9E1F2')
YEL = PatternFill('solid', fgColor='FFF2CC'); EXT = PatternFill('solid', fgColor='EDEDED')
thin = Side(style='thin', color='BFBFBF'); BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical='top'); CENTER = Alignment(horizontal='center', vertical='center', wrap_text=True)
TRAINEES = ['Thines', 'Areez', 'Farizal', 'Darwin', 'Gun Ho']


def style_range(ws, rng, font=N, fill=None, align=WRAP, border=BOX):
    for row in ws[rng]:
        for c in row:
            c.font = font; c.alignment = align
            if fill: c.fill = fill
            if border: c.border = border


def header(ws, row, labels, widths=None, fill=BLUE):
    for j, lab in enumerate(labels, 1):
        c = ws.cell(row=row, column=j, value=lab); c.font = H2; c.fill = fill; c.alignment = CENTER; c.border = BOX
    if widths:
        for j, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(j)].width = w


def title(ws, text, sub, ncols):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    c = ws.cell(row=1, column=1, value=text); c.font = H1; c.fill = NAVY; c.alignment = Alignment(vertical='center')
    ws.row_dimensions[1].height = 24
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncols)
    c = ws.cell(row=2, column=1, value=sub); c.font = SM
    ws.freeze_panes = 'A4'


wb = Workbook()
# ---------------- 1. Management Overview ----------------
ws = wb.active; ws.title = 'Management Overview'
title(ws, 'RCP Project Setup & Maintenance Training — Proposal (Trainer version)', 'Prepared by Park Jae Min, 9 Oct 2026. Based on the company proposal RCP_Training_Plan_19-30_Oct_2026 with the technical sequence and content filled in by the trainer. Yellow cells are to be confirmed / filled in.', 6)
rows = [('Training period', '19–30 October 2026 (10 weekdays: 9 training days + Day 10 practical)'),
        ('Location', 'MMP, Penang, Malaysia'), ('Trainer', 'Park Jae Min'),
        ('Participants', 'Thines, Areez, Farizal, Darwin (MMP) + Gun Ho (AATT)'), ('Coordinator', 'Darwin'),
        ('Purpose', 'Build MMP capability to set up, maintain and troubleshoot RCP (OCS): server, database, application, site configuration, map, HSMS, alarms and Rose redundancy.'),
        ('Daily timetable', '09:00–12:00 explain & demonstrate · 13:00–15:00 hands-on · 15:00–16:00 review / test (MYT)'),
        ('Training hours', '=SUM(\'Daily Training Plan\'!K5:K14)'),
        ('Curriculum basis', f"OCS competency item list v0.5: {len(items)} items in 9 sections. Core {sum(1 for i in items if i['scope']=='Core')} items taught and assessed in the 10 days; Extended {sum(1 for i in items if i['scope']=='Extended')} items (deep log analysis, SECS deep-dive, Rose maintenance, network equipment, EQ monitoring) handed over as reference for November follow-up. See sheet 'Curriculum Items'."),
        ('Assessment', 'Week-1 checkpoint (Day 5) · Knowledge test (Day 9, by section, 100) · Individual practical (Day 10, 100) · critical checks · trainer sign-off. See sheet \'Assessment Tracker\'.')]
r = 4
for k, v in rows:
    ws.cell(row=r, column=1, value=k).font = B; ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)
    c = ws.cell(row=r, column=2, value=v); c.font = N; c.alignment = WRAP
    ws.row_dimensions[r].height = 30 if len(str(v)) > 90 else 18; r += 1
r += 1
header(ws, r, ['Before training', 'Owner', 'Due', 'Requirement / deliverable', 'Status', 'Notes'], [24, 44, 14, 46, 12, 30]); r += 1
pre = [('Confirm scope, dates and trainees', 'Darwin + Park Jae Min', datetime.date(2026, 10, 9), 'Agree this proposal; confirm Gun Ho attendance and 09:00–16:00 availability', 'Pending', ''),
       ('Prepare lab server / VM', 'Darwin', datetime.date(2026, 10, 16), 'Windows server VM with network access; MSSQL 2016 media; Office/AccessDatabaseEngine; two PCs for RailDesignTool', 'Pending', 'Isolated test network'),
       ('Prepare RCP materials', 'Park Jae Min', datetime.date(2026, 10, 16), 'RCP installer and version, base software list, sample DB/map, tag Excel, manuals, XCom Simulator and Simulation.exe', 'Pending', 'Confirm site RCP version'),
       ('Prepare Rose test pair', 'Darwin + Park Jae Min', datetime.date(2026, 10, 16), 'Rose MirrorHA test pair or read-only window on the live pair for Day 9', 'Pending', ''),
       ('Site confirmations', 'Darwin', datetime.date(2026, 10, 16), 'A) MCS_IF has a UI window?  B) MapLoad file: MDB or RDT JSON?  C) System>AltTransfer screen exists?', 'Pending', 'Affects items L1-20, L2b-04, L3c-03/04, L2b-15'),
       ('Sample logs from site', 'Darwin', datetime.date(2026, 10, 16), 'Comm, Order, HSMS/XCom, PLC, Event log samples for Day 8', 'Pending', 'Mask IP / host names'),
       ('Release trainees', 'MMP manager', datetime.date(2026, 10, 16), 'Protect 6 hours/day and arrange operational cover', 'Pending', 'All attend common modules')]
for row in pre:
    for j, v in enumerate(row, 1):
        c = ws.cell(row=r, column=j, value=v); c.font = N; c.alignment = WRAP; c.border = BOX
        if j == 3: c.number_format = 'yyyy-mm-dd'
        if j in (5, 6): c.fill = YEL
    ws.row_dimensions[r].height = 32; r += 1
r += 1
ws.cell(row=r, column=1, value='Planning assumptions').font = B; r += 1
for t in ['This is the trainer\'s proposal. Content follows the OCS user manuals, installation standard, setup guide, Parameter manual, RailDesignTool manual and Rose operation guide.',
          'Proposed pass: Week-1 checkpoint passed; knowledge ≥ 70/100; practical ≥ 80/100; all critical checks (backup before change, rollback, recovery) passed; trainer sign-off.',
          'All changes are made on the lab server only. Map and DB changes include backup, validation and rollback steps.',
          'November: supervised follow-up on site for gaps and for the Extended items (trainer stays until end of November).']:
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=6); c = ws.cell(row=r, column=1, value=t); c.font = N; c.alignment = WRAP; ws.row_dimensions[r].height = 28; r += 1

# ---------------- 2. Daily Training Plan ----------------
ws = wb.create_sheet('Daily Training Plan')
title(ws, 'RCP — Two-week Daily Training Plan (Trainer version)', 'Trainer: Park Jae Min · All sessions: Thines, Areez, Farizal, Darwin, Gun Ho · Times: MYT · Item IDs refer to sheet \'Curriculum Items\'', 13)
header(ws, 4, ['Day', 'Date', 'Module', '09:00–12:00  Explain & demonstrate', '13:00–15:00  Hands-on practice', '15:00–16:00  Review / test', 'Daily deliverable', 'Items', 'Item IDs', 'Hours', 'Hours', 'Status', 'Actual notes'],
       [5, 11, 26, 44, 44, 34, 26, 6, 30, 1, 6, 10, 24])
ws.column_dimensions['J'].hidden = True
r = 5
for s in d['schedule']:
    vals = [s['day'], datetime.date.fromisoformat(s['date']), s['module'], s['explain'], s['hands_on'], s['review'], s['deliverable'], len(s['items']), ', '.join(s['items']) or '-', None, 6, 'Planned', '']
    for j, v in enumerate(vals, 1):
        c = ws.cell(row=r, column=j, value=v); c.font = N; c.alignment = WRAP if j >= 3 else CENTER; c.border = BOX
        if j == 2: c.number_format = 'yyyy-mm-dd'
        if j in (12, 13): c.fill = YEL
    ws.row_dimensions[r].height = 120; r += 1
ws.cell(row=r, column=1, value='Practice rotation: Thines + Areez / Farizal + Darwin (+ Gun Ho rotating). Each pair rotates operator and reviewer. Day 10: four to five 45-minute individual practical slots in the morning; afternoon for retest and handover.').font = SM
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=13); ws.row_dimensions[r].height = 28

# ---------------- 3. Assessment Tracker ----------------
ws = wb.create_sheet('Assessment Tracker')
title(ws, 'RCP — Individual Assessment Tracker', 'Enter results after testing in the yellow cells. Knowledge and practical scores are 0–100. Result and Level are calculated.', 11)
header(ws, 4, ['Trainee', 'Attendance (days)', 'Week-1 checkpoint', 'Knowledge score', 'Practical score', 'Critical checks', 'Trainer sign-off', 'Result', 'Level (knowledge band)', 'Gap / follow-up action', 'Retest date'],
       [14, 12, 14, 12, 12, 13, 13, 10, 16, 36, 12])
r = 5
for t in TRAINEES:
    ws.cell(row=r, column=1, value=t).font = N
    for j in range(2, 12):
        c = ws.cell(row=r, column=j); c.border = BOX; c.font = N; c.alignment = CENTER
        if j in (2, 3, 4, 5, 6, 7, 10, 11): c.fill = YEL
    for j, v in ((3, 'Pending'), (6, 'Pending'), (7, 'Pending')):
        ws.cell(row=r, column=j, value=v)
    ws.cell(row=r, column=8, value=f'=IF(OR(D{r}="",E{r}=""),"Pending",IF(AND(B{r}>=9,C{r}="Pass",D{r}>=70,E{r}>=80,F{r}="Pass",G{r}="Signed"),"PASS","FAIL"))')
    ws.cell(row=r, column=9, value=f'=IF(D{r}="","Not assessed",IF(D{r}>=91,"Level 3",IF(D{r}>=66,"Level 2",IF(D{r}>=51,"Level 1","Trainee"))))')
    ws.cell(row=r, column=11).number_format = 'yyyy-mm-dd'
    ws.cell(row=r, column=1).border = BOX; r += 1
ws.cell(row=r, column=1, value='Example (delete):').font = SM
ex = ['Example', 10, 'Pass', 78, 85, 'Pass', 'Signed', None, None, 'Rose failback to re-check in Nov', datetime.date(2026, 11, 12)]
for j, v in enumerate(ex, 1):
    if v is not None: c = ws.cell(row=r, column=j, value=v); c.font = SM; c.border = BOX
ws.cell(row=r, column=8, value=f'=IF(OR(D{r}="",E{r}=""),"Pending",IF(AND(B{r}>=9,C{r}="Pass",D{r}>=70,E{r}>=80,F{r}="Pass",G{r}="Signed"),"PASS","FAIL"))').font = SM
ws.cell(row=r, column=9, value=f'=IF(D{r}="","Not assessed",IF(D{r}>=91,"Level 3",IF(D{r}>=66,"Level 2",IF(D{r}>=51,"Level 1","Trainee"))))').font = SM
ws.cell(row=r, column=11).number_format = 'yyyy-mm-dd'
r += 2
ws.cell(row=r, column=1, value='KNOWLEDGE TEST (Day 9) — marks by section').font = B; r += 1
header(ws, r, ['Section', 'Core items', 'Max marks', 'Thines', 'Areez', 'Farizal', 'Darwin', 'Gun Ho', '', '', '']); r += 1
k0 = r
for s in d['sections']:
    ids = [i for m in s['modules'] for i in m['items']]
    vals = [s['section'], sum(1 for i in ids if I[i]['scope'] == 'Core'), s['max_marks']]
    for j, v in enumerate(vals, 1):
        c = ws.cell(row=r, column=j, value=v); c.font = N; c.border = BOX
    for j in range(4, 9):
        c = ws.cell(row=r, column=j); c.border = BOX; c.fill = YEL if s['max_marks'] else EXT
    r += 1
ws.cell(row=r, column=1, value='Total').font = B
for j in range(2, 9):
    col = get_column_letter(j); c = ws.cell(row=r, column=j, value=f'=SUM({col}{k0}:{col}{r-1})'); c.font = B; c.border = BOX
ws.cell(row=r + 1, column=1, value='Knowledge score (0–100) = Total marks; copy into column D above. Extended sections carry 0 marks in this round.').font = SM
r += 3
ws.cell(row=r, column=1, value='PRACTICAL TEST (Day 10) — tasks and points').font = B; r += 1
header(ws, r, ['Practical task', 'Max points', 'Evidence', 'Critical requirement', 'Thines', 'Areez', 'Farizal', 'Darwin', 'Gun Ho', '', '']); r += 1
p0 = r
for t in d['practical_tasks']:
    for j, v in enumerate(t, 1):
        c = ws.cell(row=r, column=j, value=v); c.font = N; c.border = BOX; c.alignment = WRAP
    for j in range(5, 10):
        c = ws.cell(row=r, column=j); c.border = BOX; c.fill = YEL
    ws.row_dimensions[r].height = 30; r += 1
ws.cell(row=r, column=1, value='Total practical points').font = B
for j in range(2, 10):
    if j in (3, 4): continue
    col = get_column_letter(j); c = ws.cell(row=r, column=j, value=f'=SUM({col}{p0}:{col}{r-1})'); c.font = B; c.border = BOX
r += 2
ws.cell(row=r, column=1, value='PROPOSED COMPLETION RULE').font = B; r += 1
for k, v in d['pass_rule'].items():
    ws.cell(row=r, column=1, value=k.replace('_', ' ').capitalize()).font = N; ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6); ws.cell(row=r, column=2, value=v).font = N; r += 1
ws.column_dimensions['C'].width = 30; ws.column_dimensions['D'].width = 34

# ---------------- 4. Curriculum Items ----------------
ws = wb.create_sheet('Curriculum Items')
title(ws, 'OCS Competency Items v0.5 — curriculum reference', f"{len(items)} items. Scope Core = taught and assessed 19–30 Oct; Extended = handed over as reference, November follow-up. Objectives are in Korean (source language); English translation follows with the slides.", 10)
header(ws, 4, ['ID', 'Section', 'Module', 'Category (item)', 'Objective — the trainee can …', 'Skill Level', 'Scope', 'Day', 'Screen / tool', 'v0.3 IDs'], [9, 24, 24, 34, 70, 9, 9, 6, 36, 22])
r = 5
for s in d['sections']:
    for m in s['modules']:
        for i in m['items']:
            it = I[i]
            vals = [it['id'], s['section'], m['module'], it['title'], it['objective'], it['level'], it['scope'], it['day'] or '', it['screen_or_tool'], ', '.join(it['merged_from'])]
            for j, v in enumerate(vals, 1):
                c = ws.cell(row=r, column=j, value=v); c.font = N; c.border = BOX; c.alignment = WRAP if j in (4, 5, 9) else CENTER
                if it['scope'] == 'Extended': c.fill = EXT
            ws.row_dimensions[r].height = 60; r += 1
ws.auto_filter.ref = f'A4:J{r-1}'
r += 1
ws.cell(row=r, column=1, value='Legend').font = B; r += 1
for k, v in [('Core / Extended', 'Core items are taught Day 1–9 and assessed Day 9–10. Extended items (grey) are outside this round.'),
             ('Skill Level', 'L1 screen familiarity · L2 structure and entry points · L3 hands-on resolution'),
             ('Day', 'Training day in sheet Daily Training Plan'),
             ('Counts', f"Core: =COUNTIF(G5:G{4+len(items)},\"Core\") → see cell B{r+4}")]:
    ws.cell(row=r, column=1, value=k).font = N; ws.cell(row=r, column=2, value=v).font = N; r += 1
ws.cell(row=r, column=1, value='Core items').font = B; ws.cell(row=r, column=2, value=f'=COUNTIF(G5:G{4+len(items)},"Core")').font = B
ws.cell(row=r + 1, column=1, value='Extended items').font = B; ws.cell(row=r + 1, column=2, value=f'=COUNTIF(G5:G{4+len(items)},"Extended")').font = B

out = 'Training_Plan/RCP_Training_Plan_19-30_Oct_2026_Trainer_v0.5.xlsx'
wb.save(out); print('saved', out)
