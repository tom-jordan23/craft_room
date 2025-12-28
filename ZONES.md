# Zone Specifications

Based on geometry from `craft_room_layout_r12.dxf`. All dimensions in inches unless noted.

---

## Room Geometry

- **Footprint:** 360" x 240" (30' x 20' = 600 sq ft)
- **Open Edge:** South wall (y=0), interior access
- **Back Wall:** North (y=240), exterior access for ventilation

---

## Zone 1: Electronics / Clean Bench

**DXF Layer:** BENCH
**Location:** Southwest corner, against west wall
**Bounds:** x: 0-60, y: 156-216
**Dimensions:** 60"W x 60"D (5' x 5' = 25 sq ft)

### Activities - His

| Activity | Tools/Equipment | Power Needs | Ventilation |
|----------|-----------------|-------------|-------------|
| SDR operation | SDR receivers, spectrum analyzer | 120V, clean power, isolated ground | None (no fumes) |
| Antenna prototyping | Soldering iron, VNA, signal generator | 120V x 3-4 outlets | Local fume extraction for soldering |
| Circuit assembly | Oscilloscope, bench supply, DMM | 120V, dedicated circuit for test equipment | None |
| PCB rework | Hot air station, microscope | 120V | Local fume extraction |
| CAD/documentation | Computer, monitors | 120V | None |

### Infrastructure Requirements

- **Electrical:**
  - Minimum 2x 20A circuits (test equipment + bench tools)
  - Isolated ground for RF equipment
  - Clean power (consider line conditioner)
  - 6-8 outlets at bench height (36")
- **Lighting:**
  - High CRI (90+) task lighting for inspection
  - Dimmable for screen work
- **HVAC:**
  - Minimal - keep away from dust-generating zones
  - Local solder fume extractor with carbon filter
- **Special:**
  - Grounding bar for RF work
  - Coax feedthrough to exterior (antenna routing)
  - ESD-safe work surface and flooring

### Adjacencies
- Adjacent to Her Zone (both clean, quiet compatible)
- Distant from Fabrication (EMI isolation from motors, VFDs)
- Near cabinetry for parts storage

---

## Zone 2: Tool / Dirty Bench (Fabrication)

**DXF Layer:** BENCH
**Location:** East wall, full height
**Bounds:** x: 330-360, y: 72-216
**Dimensions:** 30"W x 144"H (2.5' x 12' = 30 sq ft bench footprint)

### Activities - His

| Activity | Tools/Equipment | Power Needs | Ventilation |
|----------|-----------------|-------------|-------------|
| Woodworking - joinery | Router, biscuit joiner, hand tools | 120V 15A per tool | Dust collection |
| Woodworking - shaping | Bandsaw (if fits), jigsaw, sanders | 120V 15A, some 20A | Dust collection |
| Wood turning | Lathe (floor-standing nearby) | 120V 20A or 240V | Heavy dust collection |
| Metalwork - grinding | Angle grinder, bench grinder | 120V 15A | Spark containment, local exhaust |
| Metalwork - welding prep | Wire brush, cutoff wheel | 120V 15A | Local exhaust |
| Light machining | Drill press, mill (if present) | 120V 20A or 240V | Coolant mist, chip management |
| Tool maintenance | Sharpening, blade changes | 120V | None |

### Infrastructure Requirements

- **Electrical:**
  - Minimum 2x 20A 120V circuits
  - 1x 240V 30A circuit (for lathe, welder, or compressor)
  - Outlets every 4' along bench
  - Consider retractable cord reels from ceiling
- **Lighting:**
  - High-output ambient (100+ fc at bench)
  - Portable task lights for detail work
  - Spark-resistant fixtures if grinding
- **HVAC:**
  - Dust collection drops (4" minimum) at each major tool
  - Trunk line to central collector or wall port
  - Local exhaust hood for grinding/welding prep
- **Special:**
  - Fire extinguisher (ABC) within reach
  - Heavy-duty bench surface (butcher block or steel top)
  - Floor mat for standing comfort

### Adjacencies
- Adjacent to Fume Zone (workflow: fabricate → finish)
- Adjacent to Assembly Table (large piece handling)
- Near back wall for dust/exhaust routing

---

## Zone 3: Fume + Fiberglass Bench

**DXF Layer:** VENT
**Location:** Northeast, against back wall
**Bounds:** x: 270-360, y: 156-186
**Dimensions:** 90"W x 30"D (7.5' x 2.5' = 18.75 sq ft)
**Vent:** Penetration at x: 350-370, y: 230 (through back wall)

### Activities - His/Shared

| Activity | Tools/Equipment | Power Needs | Ventilation |
|----------|-----------------|-------------|-------------|
| Fiberglass layup | Rollers, squeegees, mixing cups | 120V (heat gun) | **Critical** - 200+ CFM exhaust |
| Epoxy work | Mixing station, heat lamps | 120V (lamps, hot box) | Active exhaust during cure |
| Carbon fiber work | Vacuum bagging, infusion setup | 120V (vacuum pump) | Active exhaust |
| Spray finishing | HVLP gun, spray cans | 120V (compressor elsewhere) | **Critical** - explosion-proof, high CFM |
| Solvent cleaning | Parts washer, wipe-down | None | Active exhaust |
| Chemical mixing | Scale, graduated containers | 120V (scale) | Active exhaust |

### Infrastructure Requirements

- **Electrical:**
  - 1x 20A circuit, GFCI protected
  - Explosion-proof outlets if spraying solvents
  - Switch for exhaust fan at bench entry
- **Lighting:**
  - Explosion-proof if solvent spraying
  - Good color rendering for finish inspection
  - Cleanable lens covers
- **HVAC:**
  - **Dedicated exhaust fan:** 200-400 CFM minimum
  - Direct vent to exterior (back wall penetration at y=230)
  - Make-up air provision to avoid negative pressure
  - Damper for when not in use
- **Special:**
  - Chemical-resistant work surface (stainless, HDPE, or disposable covering)
  - Spill containment lip or tray
  - Fire-rated flammable storage cabinet within reach
  - Eye wash station accessible
  - No ignition sources (pilot lights, sparking tools) in zone

### Adjacencies
- Against back wall for direct exhaust
- Adjacent to Fabrication (workflow continuity)
- Downwind from all other zones (contamination control)

---

## Zone 4: Sheet Goods / Lumber Stage

**DXF Layer:** STORAGE
**Location:** Southwest corner, along open edge
**Bounds:** x: 0-96, y: 0-60
**Dimensions:** 96"W x 60"D (8' x 5' = 40 sq ft)

### Activities - Shared

| Activity | Tools/Equipment | Power Needs | Ventilation |
|----------|-----------------|-------------|-------------|
| Material receiving | Hand truck, pallet jack | None | None |
| Sheet good storage | Vertical rack, A-frame | None | None |
| Lumber storage | Horizontal rack, cantilever | None | None |
| Material breakdown | Circular saw, track saw | 120V 15A | Dust (portable collector) |
| Long stock handling | Sawhorses | None | None |

### Infrastructure Requirements

- **Electrical:**
  - 1x 20A circuit for portable tools
  - Outlet near floor level for track saw
- **Lighting:**
  - Adequate ambient (50+ fc)
  - No special requirements
- **HVAC:**
  - None dedicated
  - Keep clear of main dust collection
- **Special:**
  - Floor rated for heavy loads (sheet goods stack weight)
  - Vertical storage rack for plywood/MDF (4x8 sheets)
  - Horizontal rack for dimensional lumber
  - Clear path to open edge for delivery

### Adjacencies
- At open edge for material entry
- Near Assembly Table for breakdown workflow
- Separated from Electronics (sawdust contamination)

---

## Zone 5: Center Assembly Table

**DXF Layer:** TABLE
**Location:** Center of room
**Bounds:** x: 132-228, y: 96-144
**Dimensions:** 96"W x 48"D (8' x 4' = 32 sq ft table top)

### Activities - Shared

| Activity | Tools/Equipment | Power Needs | Ventilation |
|----------|-----------------|-------------|-------------|
| Large assembly | Clamps, squares, mallets | 120V (occasional) | None |
| Glue-ups | Clamps, cauls, glue applicators | None | Minimal (glue fumes) |
| Layout and marking | Straightedge, tape, markers | None | None |
| Fabric cutting | Rotary cutter, mat, weights | None | None |
| Upholstery work | Staple gun, foam, batting | 120V (electric stapler) | None |
| Project staging | N/A | None | None |
| Kayak frame assembly | Long clamps, forms | 120V (steam bender nearby?) | None |

### Infrastructure Requirements

- **Electrical:**
  - Overhead drop or floor box (1x 20A)
  - Retractable cord reel ideal
- **Lighting:**
  - Excellent ambient from above
  - No shadows across table surface
- **HVAC:**
  - General room air
  - Position under ceiling fan if present
- **Special:**
  - Flat, replaceable top (MDF or hardboard)
  - Sturdy base (torsion box or heavy apron)
  - Consider adjustable height or outfeed support
  - 36" clearance on all sides for circulation
  - T-track or dog holes for workholding

### Adjacencies
- Central to all zones
- Equidistant from Her Zone and Fabrication
- Clear sightlines to entry

---

## Zone 6: Cabinetry Run

**DXF Layer:** CABINETRY
**Location:** Full width along back (north) wall
**Bounds:** x: 0-360, y: 216-240
**Dimensions:** 360"W x 24"D (30' x 2' = 60 sq ft footprint)

### Configuration

| Section | X Range | Serves | Contents |
|---------|---------|--------|----------|
| West section | 0-120 | Electronics, Her Zone | Small parts bins, components, fabric/paper storage |
| Center section | 120-270 | Assembly, General | Hardware, fasteners, adhesives, finishing supplies |
| East section | 270-360 | Fabrication, Fume Zone | Power tool accessories, abrasives, safety gear, PPE |

### Infrastructure Requirements

- **Electrical:**
  - Outlet every 48" along backsplash (8 outlets shown in DXF)
  - At y=226-230 (inside cabinet zone)
  - Mix of 15A and 20A circuits
- **Lighting:**
  - Under-cabinet task lighting
  - LED strips recommended
- **HVAC:**
  - Vent penetration at x=350-370 for Fume Zone exhaust
- **Special:**
  - Base cabinets: 24"D x 36"H
  - Upper cabinets: 12"D x 30"H (bottom at 54" AFF)
  - Countertop provides secondary work surface
  - Consider pegboard or french cleat between base and upper

---

## Zone 7: Her Zone (Proposed - Not in Original DXF)

**Note:** The original DXF does not define a dedicated zone for Her activities. Based on discussion, this zone needs to be carved from available space.

**Proposed Location:** West side, between Electronics bench and Cabinetry, or repurposing part of the floor area west of Assembly Table.

**Proposed Bounds:** x: 0-120, y: 60-156 (approximate)
**Proposed Dimensions:** 120"W x 96"D (10' x 8' = 80 sq ft)

### Activities - Her

| Activity | Tools/Equipment | Power Needs | Ventilation |
|----------|-----------------|-------------|-------------|
| Sewing | Sewing machine, serger | 120V x 2-3 outlets | None |
| Quilting | Long-arm or domestic machine, cutting mat | 120V, large table space | None |
| Knitting/crochet | Yarn winder, swift | None | None |
| Embroidery | Hoop, frame, machine | 120V | None |
| Painting | Easel, palette, brushes | 120V (task light) | Minimal (oil paints may need ventilation) |
| Drawing/illustration | Drafting table, light box | 120V | None |
| Paper crafts | Die cutter (Cricut), heat press | 120V (multiple outlets) | Heat press may need ventilation |
| Upholstery | Staple gun, foam cutter, sewing | 120V | Foam cutting - local exhaust |
| Miniatures | Magnifier, airbrush, paints | 120V | Airbrush - local exhaust |

### Infrastructure Requirements

- **Electrical:**
  - 2x 20A circuits (sewing machines, heat press, die cutter draw significant power)
  - 6-8 outlets at counter height (36")
  - Consider switched outlets for machines
- **Lighting:**
  - **Critical:** High CRI (95+) for color-accurate work
  - 5000K color temperature (daylight)
  - Task lighting at each work station
  - Natural light if window available
- **HVAC:**
  - General room air (clean zone)
  - Local exhaust for airbrush work (portable or ducted)
  - Keep separated from sawdust and composite fumes
- **Special:**
  - Multiple work surfaces at different heights:
    - 30" for seated sewing
    - 36" for standing cutting/layout
  - Large cutting mat surface (minimum 36" x 48")
  - Thread/yarn/fabric storage (bins, cubbies, bolt rack)
  - Good floor (easy to clean dropped threads, pins)
  - Ironing station with heat-resistant surface

### Adjacencies
- Adjacent to Electronics (both clean, compatible noise levels)
- Away from Fabrication (dust, noise)
- Access to Assembly Table for large quilts/upholstery projects
- Near Cabinetry for supply storage

---

## Electrical Summary by Zone

| Zone | Circuits | Voltage | Special |
|------|----------|---------|---------|
| Electronics | 2x 20A | 120V | Isolated ground, clean power |
| Fabrication | 2x 20A + 1x 30A | 120V + 240V | High capacity |
| Fume Zone | 1x 20A | 120V | GFCI, explosion-proof option |
| Storage | 1x 20A | 120V | Floor-level outlet |
| Assembly Table | 1x 20A | 120V | Overhead drop or floor box |
| Cabinetry | 4x 15-20A | 120V | Every 48" |
| Her Zone | 2x 20A | 120V | High outlet count |

**Total estimate:** 12-14 circuits, 100A+ subpanel recommended

---

## HVAC Summary

| System | Zones Served | CFM | Notes |
|--------|--------------|-----|-------|
| Fume exhaust | Fume Zone | 200-400 | Direct to exterior, makeup air required |
| Dust collection | Fabrication | 400-800 | Central collector or wall port |
| Local exhaust | Electronics (solder), Her (airbrush) | 50-100 each | Carbon filter or ducted |
| General HVAC | All | Per room size | Filtration for dust, positive pressure in clean zones optional |

---

## Workflow Paths

### Material Flow
```
Delivery → Storage (breakdown) → Assembly Table (layout) → Zone bench (work) → Fume Zone (finish) → Out
```

### Clean Work Path
```
Entry → Her Zone or Electronics → Assembly Table (if needed) → Exit
```

### Dirty Work Path
```
Entry → Storage → Assembly Table → Fabrication → Fume Zone → Exit
```

### Contamination Control
- Airflow: West → East (clean to dirty)
- Her Zone and Electronics upwind of Fabrication
- Fume Zone at terminus with direct exhaust
