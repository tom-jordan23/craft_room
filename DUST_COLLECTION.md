# Dust Collection System Recommendation

For the 600 sq ft craft room with woodworking, metalwork, and composite fabrication.

---

## Recommended System: Laguna P|Flux 1 + iVAC Pro Automation

### Why This Combination

1. **Right-sized for the shop** - 900 CFM actual (1314 nominal) handles your tool mix without being overkill
2. **HEPA filtration** - Critical for composite dust and fine wood particles
3. **Runs on 120V** - No electrical upgrade needed for Phase 1
4. **Cyclone pre-separation** - Less filter maintenance, longer filter life
5. **Expandable** - Can add ducting and automation incrementally

---

## Primary Unit: Laguna P|Flux 1

| Spec | Value |
|------|-------|
| Motor | 1.5 HP, 120V/240V, 18.8A |
| CFM (actual) | 900 |
| CFM (nominal) | 1,314 |
| Static Pressure | 10.1" WC |
| Inlet | 6" (includes 2×4" splitter) |
| Drum | 32 gallon |
| Filter | HEPA (99.97% @ 0.3 micron) |
| Auto-clean | Yes, 10-minute intervals |
| Footprint | Mobile on casters |
| Weight | 232 lbs |

**Price:** ~$3,499 ([Woodcraft](https://www.woodcraft.com/products/laguna-p-flux-1-5-hp-cyclone-hepa-dust-collector), [Rockler](https://www.rockler.com/laguna-pfluxi-15hp-hepa-cyclone-dust-collector), [Acme Tools](https://www.acmetools.com/laguna-tools-pflux1-dust-collector-15hp-110-220v-60hz-mdcpf15110/195444072703.html))

### Why P|Flux 1 Over Alternatives

| Option | CFM | Price | Pros | Cons |
|--------|-----|-------|------|------|
| **Laguna P\|Flux 1** | 900 | $3,499 | HEPA, auto-clean, 120V, mobile | Moderate CFM for big ducted runs |
| Oneida Supercell | 465 | $2,500-4,000 | Extreme static pressure (97.8" WC), great for long/restrictive runs | Lower CFM, loud (high-pitched), 230V |
| JET DC1100VX | 1,100 | $800-1,000 | Affordable, good CFM | Bag filter (not HEPA), no cyclone |
| Laguna P\|Flux 3 | 1,850 | $5,500+ | Higher CFM for full ducted system | 240V required, overkill for this shop |

**The P|Flux 1 is the sweet spot** - HEPA cyclone with enough CFM for a small ducted system or direct-connect, runs on 120V, and mobile for Phase 1 flexibility.

---

## Automation: iVAC Pro System

Automatic tool-triggered dust collection - turn on a tool, the collector starts and the blast gate opens.

### Components Needed

| Component | Qty | Unit Price | Total | Purpose |
|-----------|-----|------------|-------|---------|
| [iVAC Pro Switch HP](https://shop.ivacswitch.com/collections/ivac-control-modules) | 1 | $187 | $187 | Controls collector on/off |
| [iVAC Pro 4" Plastic Blast Gate](https://shop.ivacswitch.com/products/ivac-pro-4-pro-plastic-blast-gate) | 5 | $140 | $700 | Auto gates at each tool |
| [iVAC Tool Sensor (Candlestick)](https://shop.ivacswitch.com/) | 5 | $40 | $200 | Detects tool power-on |
| Power Adaptor (12Vac) | 1 | $17 | $17 | Powers blast gates |

**Automation subtotal:** ~$1,100 for 5 tools

### How It Works

1. Tool powers on → sensor detects current draw
2. Sensor sends wireless signal to iVAC Pro Switch
3. Switch turns on dust collector
4. Same signal opens the blast gate at that tool
5. Tool powers off → gate closes → collector runs delay then shuts off

**Key feature:** System ensures at least one gate is always open when collector runs (prevents motor damage). Supports up to 8 blast gates per network.

---

## Ducting Layout

Based on [Oneida's duct sizing guide](https://www.oneida-air.com/blog/how-to-select-the-correct-duct-diameter) and [Bill Pentz's research](https://billpentz.com/woodworking/cyclone/ducting.php):

### Recommended Configuration

```
                         BACK WALL (collector location)
    ┌──────────────────────────────────────────────────────────────┐
    │                                                              │
    │  ════════════════ 6" TRUNK LINE ═══════════════════════════  │
    │       │              │              │              │         │
    │      4"             4"             4"             4"         │
    │       │              │              │              │         │
    │   [ELEC]    [ASSEMBLY DROP]   [FUME BENCH]   [FAB BENCH]    │
    │                                                              │
    │                                                              │
    │                                                              │
    │         ┌──────────┐                                        │
    │         │ ASSEMBLY │←── 4" floor sweep or drop              │
    │         │  TABLE   │                                        │
    │         └──────────┘                                        │
    │                                                              │
    │   [STORAGE]←── 4" drop for track saw / breakdown            │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘
                         OPEN EDGE
```

### Ducting Specs

| Component | Size | Material | Notes |
|-----------|------|----------|-------|
| Main trunk | 6" | Spiral steel or PVC | Along back wall above cabinetry |
| Tool drops | 4" | Spiral steel | Short as possible, <6' ideal |
| Flex hose | 4" | Anti-static | At tool connection only, minimize length |
| Fittings | -- | Long-sweep elbows, WYEs | No sharp 90s, no TEEs |

### Why 6" Trunk + 4" Drops

- 4" duct maxes out at ~400 CFM regardless of collector size ([source](https://sawmillcreek.org/threads/6-vs-4-dust-collection-duct.78081/))
- 6" trunk preserves airflow; 4" drops work for individual tools
- Most tool ports are 4" (table saw, planer, jointer) - match the port
- Keeps velocity above 3,500 FPM to prevent settling

### Tool Connection Points

| Zone | Tool | Port Size | Blast Gate | Priority |
|------|------|-----------|------------|----------|
| Fabrication | Table saw (below + above) | 2×4" | Yes | High |
| Fabrication | Planer | 4" | Yes | High |
| Fabrication | Jointer | 4" | Yes | Medium |
| Fabrication | Bandsaw | 4" | Yes | Medium |
| Fabrication | Sander (stationary) | 4" | Yes | Medium |
| Fume Zone | Downdraft table | 4" | Yes | Low (use for sanding) |
| Assembly | Floor sweep | 4" | Manual | Low |
| Storage | Track saw area | 4" | Manual | Low |

---

## Phased Implementation

### Phase 1: Mobile Direct-Connect (~$3,500)

Buy the P|Flux 1, use it mobile with the included 2×4" splitter. Move flex hose between tools manually.

- **What you get:** Immediate dust collection for any tool
- **Downside:** Manual hose swapping

### Phase 2: Basic Ducting (~$500-800)

Install 6" trunk along back wall with 4" drops to 3-4 primary tools. Manual blast gates.

- **What you get:** Fixed connections to main tools, less hose wrestling
- **Materials:** ~100' of 6" spiral, fittings, 4" drops, manual blast gates

### Phase 3: Automation (~$1,100+)

Add iVAC Pro system - auto blast gates and tool-triggered activation.

- **What you get:** Hands-free operation, no forgotten blast gates
- **ROI:** Convenience + consistent dust capture

---

## Budget Summary

| Phase | Components | Cost |
|-------|------------|------|
| **Phase 1** | Laguna P\|Flux 1 | $3,500 |
| **Phase 2** | 6" ducting, fittings, manual gates | $500-800 |
| **Phase 3** | iVAC Pro (5 gates + controller) | $1,100 |
| **Total** | Complete automated system | **~$5,100-5,400** |

---

## Installation Notes

### Electrical
- P|Flux 1 draws 18.8A on 120V - needs dedicated 20A circuit
- iVAC components are low-voltage (12V) - no additional circuits
- Locate collector near the 240V circuit if you upgrade later

### Placement
- Collector against back wall, near vent penetration (share exhaust routing)
- Trunk line above cabinetry (y=240+), drops come down to bench height
- Keep collector accessible for drum emptying (32 gal fills up)

### Grounding
- Ground all metal ducting - static buildup is real
- Use anti-static flex hose
- [iVAC Grounding Kit](https://shop.ivacswitch.com/) available ($35)

### Filter Maintenance
- HEPA filter lasts ~2,000 hours with auto-clean
- Empty drum when LED indicator or audio alarm triggers
- Cyclone pre-separation means most debris hits drum, not filter

---

## Sources

- [Laguna P|Flux 1 - Laguna Tools](https://lagunatools.com/classic/dust-collectors/p-flux-1/)
- [Laguna P|Flux 1 - Woodcraft](https://www.woodcraft.com/products/laguna-p-flux-1-5-hp-cyclone-hepa-dust-collector)
- [Laguna P|Flux 1 - Rockler](https://www.rockler.com/laguna-pfluxi-15hp-hepa-cyclone-dust-collector)
- [iVAC Pro Blast Gates](https://www.ivacswitch.com/ivac-pro-blast-gate/)
- [iVAC Pro Shop](https://shop.ivacswitch.com/)
- [Oneida Supercell Review - Fine Woodworking](https://www.finewoodworking.com/2020/06/11/tool-review-oniedas-super-cell-dust-collector)
- [Oneida Supercell - LumberJocks](https://www.lumberjocks.com/threads/oneida-supercell-dust-collector-review.352456/)
- [Duct Sizing - Oneida Air Systems](https://www.oneida-air.com/blog/how-to-select-the-correct-duct-diameter)
- [Ducting Research - Bill Pentz](https://billpentz.com/woodworking/cyclone/ducting.php)
- [4" vs 6" Duct - LumberJocks](https://www.lumberjocks.com/threads/6-dust-collection-vs-4.340481/)
- [Dust Collectors for Small Shops - Family Handyman](https://www.familyhandyman.com/list/best-dust-collector/)
- [Dust Collection Guide - Stumpy Nubs](https://www.stumpynubs.com/shop-vlog/dust-collection-explained)
