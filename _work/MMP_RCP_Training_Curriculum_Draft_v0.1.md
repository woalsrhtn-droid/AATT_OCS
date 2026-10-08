# MMP RCP Project Setup & Maintenance Training — Plan (Rough First Draft v0.1)

**Site:** MMP, Penang, Malaysia  
**Period:** 12 Oct – 30 Nov 2026 (Jaemin, Gun Ho on site)  
**Prepared by:** Jaemin (Trainer)  
**Date:** 9 Oct 2026  
**Status:** Rough first draft for review. Dates, modules, and assessment criteria are open to change.

This document covers the RCP Project Setup & Maintenance Training (19–30 Oct) only. The OHT Operation & Maintenance Training (2–30 Nov) will be planned separately by its trainers.

1. Training schedule and curriculum
2. Assessment / evaluation plan
3. Prerequisites and open items that need MMP confirmation

---

## 1. Training schedule and curriculum

| Item | Detail |
|---|---|
| Training | RCP Project Setup & Maintenance Training |
| Dates | Mon 19 Oct – Fri 30 Oct 2026 (10 working days) |
| Hours | 09:00–17:00 (lecture AM, hands-on PM; adjustable to site shift pattern) |
| Trainer | Jaemin |
| Trainees | MMP CS Team (Areez, Farizal, Thines), CMO Darwin, Gun Ho |
| Scope | RCP/OCS (OHT Control System) server: installation and setup, screen operation, system structure, map editing, log analysis, Rose MirrorHA, RailDesignTool layout update, periodic inspection and network |
| Base material | OCS training item list v0.3 — 210 competency items in 3 levels across 7 goals (see §1.1). Each item is one assessable competency ("the trainee can …"). |

### 1.1 Curriculum structure

Three competency levels. Each level has a single measuring question.

| Level | Goal | Measuring question | Items |
|---|---|---|---:|
| L1 | OCS program familiarity | Can the trainee handle everything on the OCS screens? | 51 |
| L2-a | Map / traffic-area editing | Can the trainee edit the map with Layout-type functions? | 18 |
| L2-b | Program / system structure | Does the trainee understand the Core / PLC Driver / MCS_IF structure? | 32 |
| L2-c | Symptom → entry point | When a problem occurs, does the trainee know which OCS screen or log to open? | 20 |
| L3-a | Log analysis and handling | Can the trainee analyse logs and resolve the problem alone? | 41 |
| L3-b | Rose server redundancy | Can the trainee operate the Rose MirrorHA program? | 13 |
| L3-c | RailTool layout update | Can the trainee update the layout with RailDesignTool? | 8 |
| AUX | Outside the 7 goals | Periodic inspection, network equipment, installation standard, SNMP/REST | 27 |
| **Total** | | | **210** |

### 1.2 Modules

| # | Module | Content (summary) | Item range | Level |
|---|---|---|---|---|
| M1 | System overview | What RCP/OCS is; execution units (Core, PlcDriver, MCS_IF, UI, DB) and what each talks to; server and network layout; key terms (MCS, MCP, MTL, CPS, PIO …) | L2b-01, L2b-07, L1-49 | L1/L2 |
| M2 | OCS screen operation | Every menu tab: Main screen, View, System, Object, Transfer, Report, Statistics, Window, Layout, PlayBack, Help, MCS_IF | L1-01 … L1-51 | L1 |
| M3 | Project setup (installation) | Pre-delivery checklist (IP/port requests), server OS settings, NIC teaming, firewall, base software, MSSQL 2016, DB build queries, UI deployment, config files and folders, startup order and Core state, simulator environment without MCS/vehicles | AUX-06…16, L2b-03, L2b-04 | L2/L3 |
| M4 | System structure and interfaces | Vehicle communication and OHT protocol; Host HSMS/SECS-II (timeouts, SVID/CEID, state models, connection sequence, remote commands); PLC tags and equipment monitoring; error types and code ranges; Parameter groups and dispatch/driving parameters; Rose HA concept | L2b-05…32 | L2 |
| M5 | Map and traffic-area editing | OCS side: Unuse, Home, Cluster, StationWeightGroup, Point type, UserBlock/DisableBlock, Safety/CPS interlock, MTL zone, AutoPark, Layout Run. RDT side: screens, new site, open/save/revision, segment drawing, attributes | L2a-01 … L2a-18 | L2 |
| M6 | Troubleshooting entry points | Log map (4 families), CoreForm log types, log order per symptom, Report screens per question, UIHistory, NackHistory, FailOver, host and vehicle communication paths, alarm families, startup abnormality, DB exception | L2c-01 … L2c-20 | L2 |
| M7 | Log analysis and handling | (I) Comm / status / command messages, order lifecycle, merge occupancy, ping, CMD diagnostics. (II) Server resource / FailOver / exception logs, multi-log joins, Order / Host / dispatch / route / blocking / home logs. (III) Host SECS logs, PLC and equipment logs, carrier ID, PIO, BCR, cancel/abort, controller recovery. (IV) Parameter tuning and operational settings | L3a-01 … L3a-41 | L3 |
| M8 | Rose MirrorHA | Console and status, group start/stop, manual failover and failback, service verification, replication, snapshot and recovery, planned maintenance (Windows update, DB patch), failure types, communication prerequisites, DB mirror path, standalone run | L3b-01 … L3b-13 | L3 |
| M9 | RailDesignTool layout update | Vehicle spec impact, safety margin, auto-blocking and swept check, calculation log, Export JSON, MapLoad with backup, MapLoad failure handling, live-system impact judgement | L3c-01 … L3c-09 | L3 |
| M10 | Periodic inspection and network | DB and Agent service checks, MDF/LDF growth, backup plan, SQL memory, MOXA AP/Bridge, switch monitoring, Turbo Ring, 5 GHz channel design, Cisco switch/AP, EQ monitoring (SNMP/REST) | AUX-01…05, AUX-17…27 | L1–L3 |

### 1.3 Daily schedule (draft)

| Day | Date | AM (09:00–12:00) | PM (13:00–17:00) | Modules |
|---|---|---|---|---|
| 1 | Mon 19 Oct | Kick-off, training goals and assessment rules; M1 System overview | M2 Screens part 1: Main screen, View, System | M1, M2 |
| 2 | Tue 20 Oct | M2 Screens part 2: Object, Transfer, Report, Statistics | M2 Screens part 3: Window, Layout, PlayBack, Help, MCS_IF; hands-on on training server | M2 |
| 3 | Wed 21 Oct | M3 Project setup: prerequisites, OS/network settings, base SW, MSSQL | M3 DB build, UI deploy, config, startup order; hands-on: bring OCS up on the training server with the simulator | M3 |
| 4 | Thu 22 Oct | M4 Vehicle comm and OHT protocol; PLC tags; error codes | M4 Host HSMS/SECS; Parameters; Rose concept | M4 |
| 5 | Fri 23 Oct | M5 Map and traffic-area editing (OCS side, RDT basics) | **Assessment 1** — L1 practical + L2 written/oral | M5, A1 |
| 6 | Mon 26 Oct | M6 Troubleshooting entry points | M7-I Log analysis: Comm / order / ping / CMD | M6, M7 |
| 7 | Tue 27 Oct | M7-II Resource / FailOver / exception; Order, Host, dispatch, route, blocking logs | M7-III Host SECS logs; PLC and equipment logs. Case studies | M7 |
| 8 | Wed 28 Oct | M7-IV Parameter tuning and operational settings | M8 Rose MirrorHA (hands-on on test pair if available) | M7, M8 |
| 9 | Thu 29 Oct | M9 RailDesignTool layout update (hands-on on test server) | M10 Periodic inspection and network | M9, M10 |
| 10 | Fri 30 Oct | **Assessment 2** — L3 practical cases (log analysis, Rose operation, map update) + oral | Results review, individual feedback, wrap-up; OJT follow-up plan for November (trainer stays on site until end of Nov) | A2 |

Notes

- Hands-on sessions need a training server (or VM) with OCS and the simulator. See §3.1.
- Days 6–8 are the heaviest. If the group is slower than expected, M10 (Day 9 PM) can be shortened or moved to OJT in November.
- A 30-minute daily recap and Q&A is included at the start of each day.

---

## 2. Assessment / evaluation plan

### 2.1 Principle

- One item = one assessable competency. Each item states what the trainee "can do" and is scored pass / fail.
- Levels are cumulative: L2 requires L1, L3 requires L2.
- Each of the 7 goals is evaluated separately, so a trainee's result is a profile (e.g. L3 on log analysis, L2 on Rose) rather than one number.

### 2.2 Format

| Level | Method | When |
|---|---|---|
| L1 | Practical checklist on the OCS screen: the trainee opens the screen, reads the field, and explains it. Trainer ticks items. | Day 5 PM |
| L2 | Written test (structure, codes, parameters) + oral Q&A ("Symptom X — where do you go first?") | Day 5 PM; re-test on Day 10 if needed |
| L3 | Practical cases: a log set to analyse and report; a Rose operation on the test pair; a map update on the test server | Day 10 AM |

### 2.3 Pass criteria (proposal, to be confirmed)

| Level | Proposed pass line |
|---|---|
| L1 | ≥ 80 % of items passed |
| L2 | ≥ 70 % of items passed, each of L2-a / L2-b / L2-c separately |
| L3 | ≥ 70 % of items passed, each of L3-a / L3-b / L3-c separately |

### 2.4 Target level by trainee (proposal, to be confirmed)

| Trainee | Target |
|---|---|
| MMP CS Team (Areez, Farizal, Thines) | L3 on all 7 goals |
| CMO Darwin | L1 + L2 (L3 optional) |
| Gun Ho | L3 on all 7 goals |

### 2.5 Output

- Scorecard per trainee: items passed per goal, level achieved, items to re-train.
- Summary sheet for management, shared after Day 10 and again after the November OJT period.
- Items that cannot be assessed yet because no written procedure exists (see §3.3) are listed separately, not counted as fails.

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

| # | Question | Items affected |
|---|---|---|
| A | Does the MMP MCS_IF program have a window (UI)? The user manual describes it as having no UI; the setup guide shows screens. | L1-50, L1-51, L2b-01, L2b-06, L2b-20, L2c-19 |
| B | In Layout > MapLoad, is the file selected an MDB or the RDT JSON export? | L3c-07, L3c-08 |
| C | Does the MMP OCS have the System > AltTransfer screen? | L2b-31 |

### 3.3 Procedures that do not exist in writing yet

These cannot be assessed until a procedure is written. Proposed: write them during the training with the MMP team, as part of the hands-on sessions.

- Return from Rose standalone run to redundant mode (only the standalone-run direction is documented).
- Rollback after a map update (BackupPath is documented, restore is not).
- Actions after root cause is found in logs: releasing a stuck merge occupancy, restart target when PlcCommLog shows WaitConnect, sequence for clearing a stuck Order.

### 3.4 Material language

Source manuals are in Korean and Chinese. Training slides and the assessment sheets will be prepared in English. Full manual translation is not planned for this round; the item list (210 items) will be translated.

---

## 4. Change log

| Version | Date | Change |
|---|---|---|
| v0.1 | 9 Oct 2026 | First rough draft for the 9 Oct deadline |
