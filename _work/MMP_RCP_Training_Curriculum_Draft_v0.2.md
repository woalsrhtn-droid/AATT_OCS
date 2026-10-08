# MMP RCP Project Setup & Maintenance Training — Plan (Draft v0.2)

**Site:** MMP, Penang, Malaysia  
**Period:** 12 Oct – 30 Nov 2026 (Jaemin, Gun Ho on site)  
**Prepared by:** Jaemin (Trainer)  
**Date:** 9 Oct 2026  
**Status:** Draft for review. Dates, modules, marks and pass criteria are open to change.

This document covers the RCP Project Setup & Maintenance Training (19–30 Oct) only. The OHT Operation & Maintenance Training (2–30 Nov) will be planned separately by its trainers.

1. Training schedule and curriculum
2. Assessment / evaluation plan
3. Prerequisites and open items that need MMP confirmation

---

## 1. Training schedule and curriculum

| Item | Detail |
|---|---|
| Training | RCP Project Setup & Maintenance Training |
| Dates | Mon 19 Oct – Fri 30 Oct 2026: 9 training days + 1 assessment day |
| Hours | 09:00–17:00 (lecture AM, hands-on PM; adjustable to site shift pattern) |
| Trainer | Jaemin |
| Trainees | MMP CS Team (Areez, Farizal, Thines), CMO Darwin, Gun Ho |
| Scope | RCP/OCS (OHT Control System) server: installation and setup, screen operation, system structure, map editing, vehicle / host / PLC interfaces, log analysis, Rose MirrorHA, RailDesignTool layout update, periodic inspection and network |
| Base material | OCS competency item list v0.4: **91 items** (L1 23 / L2 39 / L3 29), organised in 9 Sections and 40 Modules in the same structure as the LCS Training & Competency System workbook. Each item is one assessable competency ("the trainee can …"). All 91 items are taught within the 9 days. |

### 1.1 Competency levels

| Level | Meaning |
|---|---|
| L1 | Screen familiarity: opens any OCS screen, reads fields, colours and columns, performs manual-based register / query / command / save |
| L2 | Structure and entry points: knows the Core / PlcDriver / MCS_IF structure, edits map and traffic areas on screen, knows which screen or log to open for a symptom |
| L3 | Hands-on resolution: reads logs, identifies root cause and acts, changes parameters, operates Rose MirrorHA, deploys a map update |

### 1.2 Sections and modules (curriculum structure)

Same structure as the LCS workbook: Section → Module → Category (= one competency item) → Training Item (checklist line). Marks per section add up to 100.

| # | Section | Modules (items) | Items | Level mix | Max marks |
|---|---|---|---:|---|---:|
| 1 | System Setup | Architecture (3); Installation (3); Server Settings (2); Simulation Env (1) | 9 | L1 1 / L2 7 / L3 1 | 8 |
| 2 | Screen Operation | Main & View (3); System Menu (4); Object Menu (4); Transfer & Report (3); Statistics & Window (3); PlayBack & Help (3) | 20 | L1 20 | 14 |
| 3 | Map & Traffic Control | RDT Basics (3); OCS Traffic Settings (5); Auto-Blocking (2); Map Deployment (2) | 12 | L2 8 / L3 4 | 12 |
| 4 | Vehicle Interface | OHT Protocol (2); Comm Log Analysis (2); Comm Diagnosis (1) | 5 | L2 2 / L3 3 | 8 |
| 5 | Host Interface | MCS_IF Config (1); SECS Structure (2); Host Sequence (1); Host Log Analysis (4) | 8 | L2 4 / L3 4 | 10 |
| 6 | PLC & Equipment Interface | Tag System (2); PLC Comm (1); Station & PIO Rules (1); Equipment Log Analysis (1); EQ Monitoring (2) | 7 | L2 5 / L3 2 | 8 |
| 7 | Parameters & Operation Settings | Parameter System (1); Tuning (1); Log & Disk Settings (1); DB Maintenance (2) | 5 | L1 1 / L2 2 / L3 2 | 6 |
| 8 | Alarm & Troubleshooting | Log Map & Entry Points (3); Alarm Entry Points (6); Analysis Method (1); Vehicle & Order Analysis (3); Server Analysis (1) | 14 | L2 9 / L3 5 | 20 |
| 9 | Redundancy & Network | Rose Concept (1); Rose Operation (3); Rose Maintenance (3); Network Structure (1); Network Equipment (3) | 11 | L1 1 / L2 2 / L3 8 | 14 |
| | **Total** | | **91** | | **100** |

Full item list with objectives, screens, sources and the v0.3 → v0.4 mapping: `OCS_교육항목_레벨별_리스트_v0.4.md` (Korean; English translation to follow with the slides).

### 1.3 Daily schedule (9 training days + assessment day)

| Day | Date | AM (09:00–12:00) | PM (13:00–17:00) | Items |
|---|---|---|---|---:|
| 1 | 10/19 Mon | Kick-off · System Setup: Architecture | System Setup: Installation · Server Settings · Simulation (hands-on) | 9 |
| 2 | 10/20 Tue | Screen Operation: Main & View · System Menu | Screen Operation: Object Menu (hands-on) | 11 |
| 3 | 10/21 Wed | Screen Operation: Transfer & Report · Statistics & Window · PlayBack & Help | Map & Traffic Control: OCS Traffic Settings (hands-on) | 14 |
| 4 | 10/22 Thu | Map & Traffic Control: RDT Basics · Auto-Blocking (hands-on) | Map & Traffic Control: Map Deployment (hands-on on test server) | 7 |
| 5 | 10/23 Fri | Vehicle Interface: OHT Protocol · Comm Log Analysis · Comm Diagnosis | PLC & Equipment Interface: Tag System · PLC Comm · Station & PIO · Equipment Log · EQ Monitoring | 12 |
| 6 | 10/26 Mon | Host Interface: MCS_IF Config · SECS Structure · Host Sequence · Host Log Analysis | Parameters & Operation Settings: Parameter System · Tuning · Log & Disk · DB Maintenance | 13 |
| 7 | 10/27 Tue | Alarm & Troubleshooting: Log Map & Entry Points · Alarm Entry Points | Alarm & Troubleshooting: Analysis Method (case practice) | 10 |
| 8 | 10/28 Wed | Alarm & Troubleshooting: Vehicle & Order Analysis · Server Analysis (case practice) | Redundancy & Network: Network Structure · Network Equipment | 8 |
| 9 | 10/29 Thu | Redundancy & Network: Rose Concept · Rose Operation (hands-on) | Redundancy & Network: Rose Maintenance · overall review & Q&A | 7 |
| 10 | 10/30 Fri | ASSESSMENT — written (L2 structure) + practical (L1 screen, L3 cases) | ASSESSMENT — practical cont. · scoring · individual feedback | - |

Notes

- Time budget: 9 days × 6 h = 54 h for 91 items, about 35 min per item on average. Day 3 (14 screen items) and Day 6 (13 items) are the densest; Days 4 and 9 are tool-heavy hands-on days.
- Hands-on sessions need a training server (or VM) with OCS and the simulator, RDT on two PCs and a Rose test pair. See §3.1.
- A 30-minute recap and Q&A opens each day. Day 9 PM ends with an overall review before the assessment.
- Items that cannot be fully assessed yet because no written procedure exists (§3.3) are still taught; the missing procedure part is written together with the MMP team during the session.

---

## 2. Assessment / evaluation plan

### 2.1 Principle

- One item = one assessable competency, scored by section as in the LCS workbook (marks per section, max marks per section as in §1.2).
- Training completion (checklist, per item per trainee) and assessment marks are tracked separately: Training Tracker and Checklist sheets for completion, Assessment sheet for marks.
- Result per trainee: total marks, total %, PASS / FAIL and level band. Section-wise % shows strengths and the section to re-train.

### 2.2 Format (Day 10, Fri 30 Oct)

| Part | Method | Covers |
|---|---|---|
| Written | Structure, codes, parameters, "symptom X — where do you go first?" questions | L2 items, L1 knowledge parts |
| Practical — screen | Trainee opens the screen, reads the field, explains and performs the action on the training server; trainer ticks items | L1 items |
| Practical — cases | A log set to analyse and report; a Rose operation on the test pair; a map update on the test server | L3 items |

The test paper (question bank per section) is prepared separately after this structure is agreed.

### 2.3 Pass criteria and level bands (proposal, same as LCS workbook, to be confirmed)

| Total % | Result |
|---|---|
| < 50 % | Trainee (FAIL) |
| 51–65 % | Level 1 (PASS) |
| 66–90 % | Level 2 |
| 91 % + | Level 3 |

If a level per training goal is required (e.g. L3 on log analysis, L2 on Rose), it can be computed from the item-level tags in addition to the overall band.

### 2.4 Target level by trainee (proposal, to be confirmed)

| Trainee | Target |
|---|---|
| MMP CS Team (Areez, Farizal, Thines) | Level 3 |
| CMO Darwin | Level 2 |
| Gun Ho | Level 3 |

### 2.5 Output

- Workbook in the LCS format: Config, Curriculum, Training content Checklist, Training Tracker, Assessment, Engineer Profiles, Analytics, Dashboard.
- Scorecard per trainee after Day 10; summary for management; re-training list per section for the November OJT period (trainer stays on site until end of Nov).

---

## 3. Prerequisites and open items

### 3.1 Environment requested from MMP

- A training server or VM with OCS installed, plus XCom Simulator and Simulation.exe, so trainees can start OCS and run orders without MCS or real vehicles.
- RailDesignTool installed on at least two PCs.
- Access to a Rose MirrorHA test pair, or an agreed time window on the live pair for read-only console viewing.
- Sample log sets from the MMP site (Comm, Order, SECS, PLC, Event) for the log analysis cases.
- Read-only access to the live OCS UI for the L1 screen practice.
- Training room with projector; network access for the trainer laptop.

### 3.2 Site-specific points to confirm (affect item content)

| # | Question | Items affected (v0.4) |
|---|---|---|
| A | Does the MMP MCS_IF program have a window (UI)? The user manual describes it as having no UI; the setup guide shows screens. | L1-20, L2b-01, L2b-04, L2b-10, L2c-08 |
| B | In Layout > MapLoad, is the file selected an MDB or the RDT JSON export? | L3c-03, L3c-04 |
| C | Does the MMP OCS have the System > AltTransfer screen? | L2b-15 |

### 3.3 Procedures that do not exist in writing yet

These cannot be assessed until a procedure is written. Proposed: write them during the training with the MMP team, as part of the hands-on sessions.

- Return from Rose standalone run to redundant mode (only the standalone-run direction is documented).
- Rollback after a map update (BackupPath is documented, restore is not).
- Actions after root cause is found in logs: releasing a stuck merge occupancy, restart target when PlcCommLog shows WaitConnect, sequence for clearing a stuck Order.

### 3.4 Material language

Source manuals are in Korean and Chinese. Training slides, the checklist and the assessment sheets will be prepared in English. Full manual translation is not planned for this round; the item list (91 items) will be translated.

---

## 4. Change log

| Version | Date | Change |
|---|---|---|
| v0.1 | 9 Oct 2026 | First rough draft (210 items, 10 modules, two assessments) |
| v0.2 | 9 Oct 2026 | Items merged 210 → 91; 9 Sections / 40 Modules in the LCS workbook structure; 9 training days + assessment on Day 10; section marks (100) and LCS level bands |
