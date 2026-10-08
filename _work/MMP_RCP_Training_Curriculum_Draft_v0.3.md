# MMP RCP Project Setup & Maintenance Training — Plan (Draft v0.3)

**Site:** MMP, Penang, Malaysia · **Dates:** 19–30 Oct 2026 · **Trainer:** Park Jae Min · **Date:** 9 Oct 2026  
**Attachment:** `RCP_Training_Plan_19-30_Oct_2026_Trainer_v0.5.xlsx` (Management Overview · Daily Training Plan · Assessment Tracker · Curriculum Items). This note summarises the workbook.

## 1. What changed from the company proposal

The company proposal (RCP_Training_Plan_19-30_Oct_2026.xlsx) gave the frame: 10 weekdays, 09:00–16:00, one module per day with explain / hands-on / review, Week-1 checkpoint on Day 5, knowledge test on Day 9, individual practical on Day 10. The trainer version keeps that frame and fills in the RCP-specific sequence:

- Days 1–3 are setup: server preparation, MSSQL and DB build / backup / restore, RCP application install, UI on IIS, simulator, and site configuration (vehicle, tag, PLC registration).
- Days 4–5 are OCS screen operation (user manual), Day 6 map (OCS traffic settings, RailDesignTool, MapLoad), Day 7 HSMS, Day 8 simulation and troubleshooting entry points, Day 9 Rose MirrorHA + knowledge test, Day 10 practical.
- Gun Ho is added to the participants as in the request e-mail.
- Content outside the user manuals (deep log analysis, SECS deep-dive, Rose maintenance, network equipment, EQ monitoring) is marked **Extended**: handed over as reference, not taught or assessed in this round. November follow-up on site.

## 2. Curriculum scope

| # | Section | Modules (items) | Core | Extended | Knowledge marks |
|---|---|---|---:|---:|---:|
| 1 | System Setup | Architecture (3); Server Preparation (4); Database (5); Site Configuration (5) | 17 | 0 | 30 |
| 2 | Screen Operation | Main & View (3); System Menu (1); Object Menu (4); Transfer & Report (3); Statistics & Window (3); PlayBack & Help (2) | 16 | 0 | 15 |
| 3 | Map & Traffic Control | RDT Basics (3); OCS Traffic Settings (5); Auto-Blocking (2); Map Deployment (2) | 12 | 0 | 15 |
| 4 | Parameters | Parameter System (2); Tuning (Extended) (1) | 2 | 1 | 5 |
| 5 | Host Interface (HSMS) | MCS_IF Config (2); HSMS Structure & Sequence (2); SECS Deep-dive (Extended) (5) | 4 | 5 | 10 |
| 6 | Vehicle Interface | OHT Protocol (1); Comm Log Basics (2); Protocol Deep-dive (Extended) (2) | 3 | 2 | 5 |
| 7 | Alarm & Troubleshooting | Alarm System (1); Log Map & Entry Points (3); Symptom Entry Points (6); Log Analysis (Extended) (6) | 10 | 6 | 15 |
| 8 | Redundancy (Rose) | Rose Concept (1); Rose Operation (4); Rose Maintenance (Extended) (2) | 5 | 2 | 5 |
| 9 | Station, Network & EQ (Extended) | Station & PIO Rules (1); Network Equipment (3); EQ Monitoring (2) | 0 | 6 | 0 |
| | **Total** | | **69** | **22** | **100** |

## 3. Daily plan (details in the workbook)

| Day | Date | Module | Core items |
|---|---|---|---:|
| 1 | 2026-10-19 | Architecture & server preparation | 7 |
| 2 | 2026-10-20 | Database setup & maintenance | 5 |
| 3 | 2026-10-21 | Application installation & site configuration | 5 |
| 4 | 2026-10-22 | OCS screen operation (1) & parameters | 10 |
| 5 | 2026-10-23 | OCS screen operation (2) & Week-1 checkpoint | 8 |
| 6 | 2026-10-26 | Map create, change & update | 12 |
| 7 | 2026-10-27 | HSMS: RCP ↔ MCS | 5 |
| 8 | 2026-10-28 | Simulation, alarms & troubleshooting entry points | 12 |
| 9 | 2026-10-29 | Rose MirrorHA & knowledge test | 5 |
| 10 | 2026-10-30 | Individual practical & handover | - |

## 4. Assessment

- **Week-1 checkpoint (Day 5):** each trainee walks through server → DB → application → site setup and the main screens.
- **Knowledge test (Day 9):** written, marks by section as in §2, 100 in total.
- **Individual practical (Day 10):** 100 points.

| Practical task | Points | Critical requirement |
|---|---:|---|
| Server + application + IIS setup | 20 | Explain setup and identify service/config dependencies |
| Database build + backup/restore | 20 | Backup before change; restore successfully |
| Site configuration (vehicle, tag, PLC) + screens | 15 | Tag mapping correct; CHECK TAG clean |
| Map change + rollback | 15 | Verify connectivity and demonstrate rollback |
| HSMS communication | 10 | Explain communication checks and reconnect |
| Fault diagnosis + recovery | 15 | Name the first screen/log, recover safely |
| Handover + teach-back | 5 | Explain what changed and show evidence |

Proposed pass: attendance ≥ 9/10 days, Week-1 checkpoint passed, knowledge ≥ 70, practical ≥ 80, all critical checks passed (backup before change, rollback, recovery), trainer sign-off. Level band on knowledge score (Trainee < 50, L1 51–65, L2 66–90, L3 91+) as in the LCS workbook; to be confirmed.

## 5. Requests to MMP before 19 Oct

- Lab server / VM with network access, MSSQL 2016 media, Office / AccessDatabaseEngine, two PCs for RailDesignTool.
- Rose MirrorHA test pair, or a read-only window on the live pair for Day 9.
- Sample logs from the site for Day 8 (IP / host names masked).
- Site confirmations: A) MCS_IF has a UI window? B) MapLoad file is MDB or RDT JSON? C) System > AltTransfer screen exists?
- Trainees released 09:00–16:00 for all 10 days.

## 6. Change log

| Version | Change |
|---|---|
| v0.1 | First draft: 210 items, 10 modules, two assessments |
| v0.2 | Items merged 210 → 91, 9 sections in the LCS workbook structure, 9 + 1 days |
| v0.3 | Setup-heavy rebalance after the company proposal: Core 69 / Extended 22, company day structure and assessment (Day 5 / 9 / 10), workbook attachment |
