# CLAUDE.md — Craft Room Parametric CAD Baseline (Tom + Melissa)

## 0) Mission
Build a parametric CAD model (and supporting docs) for a home craft room that functions like a small research lab + maker studio:
- Clean-first craft/electronics zone for Melissa
- Dusty woodworking/CNC zone for Tom
- Dirty/fume zone for finishing/adhesives (NO open flame)
- Shared circulation + receiving/pack/ship workflow
- Supports full Greenland kayak construction with a long clear lane

Primary success criteria:
- Clear, repeatable material flow: receiving → breakdown → CNC → finish → pack
- Physical separation + airflow separation between clean and dusty/dirty work
- Storage that is dead-simple to maintain (containerized projects, labeled bays, enclosed cabinets)
- Parametric model that can reconfigure as constraints change (cabinet runs, station widths, aisle widths)

## 1) Absolute Decisions (Non-Negotiables)
- NO wood stove or any open-flame centerpiece in the shop (dust + solvents + fire risk).
- Dirty/Fume bump-out table is for ventilated dirty work ONLY; no hot metalwork, no open flame.
- Maintain a main workflow spine with ≥ 42 in (1067 mm) aisles where possible.
- Keep a soft dust barrier between clean and dusty zones (curtain/partition + airflow strategy).
- One-way material flow is a design constraint, not a suggestion.

## 2) Zones (Baseline Layout Intent)
### Clean Zone (Left)
Purpose: clean precision craft + digital + electronics; should feel inspiring and controllable.
Core stations:
- Melissa’s primary phenolic-topped assembly/precision bench (“Melissa’s workbench”)
- Adjacent computer/desktop station for design/pattern work/machine control
- Electronics & soldering bench (microscope, rework; fume extraction)
- 3D printing enclosure + filament storage
- Cricut / 2D CAM station
- Clean material + notion storage: flat files, roll bays, drawers, enclosed cabinetry
- Wall-mounted TV reference display
- Movable pole-based laptop stand that drops into a standard bench dog hole

### Dusty Zone (Right-Center)
Purpose: receiving, breakdown, CNC, sanding, dust collection.
Core stations:
- Sheet-goods receiving + vertical rack
- Long-stock lumber storage
- Breakdown / grid table optimized for track-saw workflow + dogs/rail registration
- CNC router bay: 4×4 machine with 4×8 tiling capability (future-proof)
- CNC tool cart + bit management
- Sanding / downdraft table
- Dust collector + filtration closet

### Dirty / Fume Zone (Right-Top / Bump-Out)
Purpose: coatings, adhesives, resins, fumes — controllable ventilation and containment.
Core stations:
- Dedicated dirty/vent table (no open flame; no hot metalwork)
- Finishing & coating area (spray/brush/wipe workflows)
- Curing/drying racks
- Adhesives/resins/paints storage (safe, enclosed)

### Shared / Circulation
- Open south-wall receiving & pack/ship bench
- Project parking (carts/pallets)
- Long-assembly / lofting clear lane for kayaks (target 20–23 ft / 6–7 m clear run)
- Maintain intuitive “reset to clean” behavior: nothing blocks aisles; parking zones are explicit.

## 3) Station List (Parametric Baseline)
Use this as the authoritative station inventory. Each station needs:
- Footprint (W×D), clearance envelope, and adjacency constraints
- Power + network needs
- Dust/fume requirements (none / dust / fume)
- Storage type (drawers / shelves / roll bay / flat file / bin)

Stations:
Clean:
- MelissaWorkBench_Phenolic
- MelissaPC_DesignStation
- ElectronicsBench_ReworkMicroscope
- PrinterBay_3DPrint_Enclosure
- Cricut_2DCAM_Station
- CleanStorage_FlatFiles
- CleanStorage_RollBays
- CleanStorage_NotionDrawers
- TV_WallMount
- LaptopStand_DogholePole

Dusty:
- Receiving_SheetGoods
- Storage_SheetVerticalRack
- Storage_LongStock
- BreakdownTable_GridDogsTrackSaw
- CNC_Bay_4x4_Tiling4x8
- CNCToolCart_BitsFixturing
- SandingTable_Downdraft
- DustCollector_Closet_Filtering

Dirty/Fume:
- DirtyVentTable_BumpOut
- FinishingArea_Coatings
- CuringRacks_Drying
- ChemStorage_AdhesivesResinsPaints

Shared:
- PackShipBench_SouthWall
- ProjectParking_Carts
- WorkflowSpine_Aisles
- KayakLane_LoftingAssembly

Infrastructure overlays:
- LeftWall_CabinetBand + CountertopBand
- TopWall_CabinetBand + CountertopBand
- SoftDustBarrier_CleanToDusty
- OneWayFlow_ReceivingToPack

## 4) CAD Output Expectations
Claude Code should produce:
- A parametric 2D plan (sketch-driven) with zones, stations, and clearance envelopes
- A parametric 3D assembly for cabinetry bands + key benches/tables
- A station inventory table exported from parameters (CSV/JSON) for BOM and planning

Modeling conventions:
- Everything dimension-driven; no “freehand” placement unless explicitly tagged TEMP.
- Prefer named parameters + constraints to direct edits.
- Stations placed via reference points anchored to walls and workflow spine.
- Use consistent coordinate system: origin at a defined corner; axes labeled.

## 5) Parametric Variables (Start Here)
Create and use parameters (units in both in/mm where useful):
Room + circulation:
- room_length, room_width
- aisle_min = 42 in (1067 mm)
- kayak_lane_length_target = 20–23 ft (6–7 m)
Cabinetry:
- base_cab_depth (e.g., 24 in / 610 mm)
- countertop_depth
- upper_cab_depth
- counter_height
- cabinet_run_left_length
- cabinet_run_top_length
Stations (examples; expand as measured/selected):
- melissa_bench_w, melissa_bench_d
- cnc_bay_w, cnc_bay_d, cnc_service_clearance
- breakdown_w, breakdown_d
- packship_w, packship_d

## 6) Constraints / Adjacencies (Rules the CAD Must Enforce)
- Clean zone must be upwind/isolated from dusty zone (partition + airflow plan).
- Sheet goods receiving adjacent to breakdown table.
- Breakdown adjacent to CNC bay.
- Finishing/dirty zone separated from clean zone; dedicated ventilation assumed.
- Pack/ship bench positioned to support one-way flow and quick “reset.”
- Kayak lane must remain clear (no permanent station encroachment).

## 7) Storage Philosophy (Design Intent)
- Favor enclosed cabinetry/drawers in clean zone to reduce dust deposition.
- Containerize projects with labeled bins; allocate explicit “project parking.”
- Provide “landing zones” at each station for tools-in-use and quick cleanup.

## 8) Known Constraints / Notes
- Concrete bump-out area (48 in × 126 in) is suitable for dirty work with ventilation, not flame/hot metalwork.
- Separate CNC station and sheet breakdown station (do not combine into one surface by default).
- Breakdown station top is phenolic with T-track + bench dogs optimized for track saw use.

## 9) What Claude Code Should Ask/Infer (Without Blocking Progress)
If dimensions are unknown, Claude should:
- Use reasonable defaults (documented), keep them as parameters, and proceed.
- Tag placeholders clearly as ASSUMED and list them in a “Missing Measurements” section.

## 10) Deliverables Checklist
- [ ] Parametric station layout (2D)
- [ ] Clearance + aisle compliance overlay
- [ ] Cabinetry band model + elevations
- [ ] Station inventory export (CSV/JSON)
- [ ] Notes: decisions, assumptions, and “do not regress” list (incl. no stove)

## 11) “Do Not Regress” List (Repeat)
- Do not propose a wood stove or any open-flame heat source in the shop.
- Do not place dusty operations in the clean zone.
- Do not reduce aisles below the minimum without explicit callout and rationale.
- Do not block the kayak lane with permanent stations.

## 12) Repo Structure Suggestion
- /cad/ (FreeCAD or preferred CAD source)
- /exports/ (DXF/SVG/PDF plan outputs)
- /data/ (station_inventory.csv, parameters.json)
- /docs/ (decisions.md, assumptions.md, BOM.md)
