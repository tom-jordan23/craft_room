#!/usr/bin/env python3
"""Render craft room floor plans as PNG images - based on actual DXF geometry."""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
import matplotlib.patheffects as pe

# Room dimensions in inches (from DXF)
ROOM_WIDTH = 360   # 30'
ROOM_HEIGHT = 240  # 20'

def setup_figure(title):
    """Create figure with room outline matching DXF."""
    fig, ax = plt.subplots(1, 1, figsize=(16, 11))

    # White background
    ax.set_facecolor('white')

    # Grid (4' = 48")
    for x in range(0, ROOM_WIDTH + 1, 48):
        ax.axvline(x, color='#e8e8e8', linewidth=0.5, zorder=0)
        if x > 0 and x < ROOM_WIDTH:
            ax.text(x, -8, f"{x//12}'", ha='center', fontsize=7, color='#999')
    for y in range(0, ROOM_HEIGHT + 1, 48):
        ax.axhline(y, color='#e8e8e8', linewidth=0.5, zorder=0)
        if y > 0 and y < ROOM_HEIGHT:
            ax.text(-8, y, f"{y//12}'", ha='right', va='center', fontsize=7, color='#999')

    # Room outline (from DXF FOOTPRINT layer)
    ax.plot([0, ROOM_WIDTH], [0, 0], 'k--', linewidth=2.5)  # South - OPEN_EDGE (dashed)
    ax.plot([ROOM_WIDTH, ROOM_WIDTH], [0, ROOM_HEIGHT], 'k-', linewidth=3)  # East
    ax.plot([ROOM_WIDTH, 0], [ROOM_HEIGHT, ROOM_HEIGHT], 'k-', linewidth=3)  # North
    ax.plot([0, 0], [ROOM_HEIGHT, 0], 'k-', linewidth=3)  # West

    ax.set_xlim(-30, ROOM_WIDTH + 50)
    ax.set_ylim(-40, ROOM_HEIGHT + 60)
    ax.set_aspect('equal')
    ax.set_xlabel('Inches', fontsize=10)
    ax.set_ylabel('Inches', fontsize=10)
    ax.set_title(title, fontsize=16, fontweight='bold', pad=15)

    # Dimension annotations
    ax.annotate('', xy=(ROOM_WIDTH, -20), xytext=(0, -20),
                arrowprops=dict(arrowstyle='<->', color='#666', lw=1.5))
    ax.text(ROOM_WIDTH/2, -28, '360" (30\'-0")', ha='center', fontsize=10, color='#444')

    ax.annotate('', xy=(-20, ROOM_HEIGHT), xytext=(-20, 0),
                arrowprops=dict(arrowstyle='<->', color='#666', lw=1.5))
    ax.text(-25, ROOM_HEIGHT/2, '240" (20\'-0")', ha='center', va='center',
            fontsize=10, color='#444', rotation=90)

    # Wall labels
    ax.text(ROOM_WIDTH/2, 10, 'OPEN EDGE (interior access)',
            ha='center', fontsize=9, color='#666', style='italic')
    ax.text(ROOM_WIDTH/2, ROOM_HEIGHT + 12, 'BACK WALL (exterior - vent access)',
            ha='center', fontsize=9, color='#666', style='italic')
    ax.text(-5, ROOM_HEIGHT/2, 'W\nE\nS\nT', ha='center', va='center', fontsize=8, color='#999')
    ax.text(ROOM_WIDTH + 8, ROOM_HEIGHT/2, 'E\nA\nS\nT', ha='center', va='center', fontsize=8, color='#999')

    return fig, ax


def render_zones():
    """Render zone allocation diagram matching DXF geometry exactly."""
    fig, ax = setup_figure('CRAFT ROOM - ZONE ALLOCATION (from DXF)')

    # Colors
    c_elec = '#2196F3'    # Blue - Electronics
    c_fab = '#FF5722'     # Deep Orange - Fabrication
    c_fume = '#F44336'    # Red - Fume
    c_storage = '#9E9E9E' # Gray - Storage
    c_table = '#FF9800'   # Orange - Assembly
    c_cab = '#795548'     # Brown - Cabinetry
    c_her = '#4CAF50'     # Green - Her Zone (proposed)

    # === FROM DXF: CABINETRY layer ===
    # Bounds: x: 0-360, y: 216-240 (24" deep strip along north wall)
    rect = Rectangle((0, 216), 360, 24, facecolor=c_cab, alpha=0.3,
                      edgecolor=c_cab, linewidth=2)
    ax.add_patch(rect)
    ax.text(180, 228, 'CABINETRY RUN (24" DEPTH)', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#5D4037')

    # Electrical outlets (8 shown in DXF at y=226-230)
    outlet_xs = [24, 72, 120, 168, 216, 264, 312]
    for ox in outlet_xs:
        ax.plot(ox, 228, 's', markersize=4, color='#FFC107', markeredgecolor='#333', markeredgewidth=0.5)
    ax.text(340, 228, '⚡', fontsize=8, ha='center', va='center')

    # === FROM DXF: BENCH layer - Electronics/Clean Bench ===
    # Lines form box: (0,156) to (60,156) to (60,216) to (0,216) to (0,156)
    # Note: DXF shows y going to 276 but that's outside room - using 216 (against cabinetry)
    rect = Rectangle((0, 156), 60, 60, facecolor=c_elec, alpha=0.3,
                      edgecolor=c_elec, linewidth=2)
    ax.add_patch(rect)
    ax.text(30, 195, 'ELECTRONICS', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(30, 182, 'CLEAN BENCH', ha='center', va='center', fontsize=8)
    ax.text(30, 165, '60"×60" (25 sq ft)', ha='center', va='center', fontsize=7, color='#666', style='italic')

    # === FROM DXF: BENCH layer - Tool/Dirty Bench ===
    # Lines form box: (330,72) to (360,72) to (360,216) to (330,216) to (330,72)
    rect = Rectangle((330, 72), 30, 144, facecolor=c_fab, alpha=0.3,
                      edgecolor=c_fab, linewidth=2)
    ax.add_patch(rect)
    ax.text(345, 150, 'TOOL', ha='center', va='center', fontsize=9, fontweight='bold', rotation=90)
    ax.text(345, 120, 'DIRTY', ha='center', va='center', fontsize=9, fontweight='bold', rotation=90)
    ax.text(345, 90, 'BENCH', ha='center', va='center', fontsize=9, fontweight='bold', rotation=90)
    ax.text(352, 144, '30"×144"', ha='center', va='center', fontsize=6, color='#666', rotation=90)

    # === FROM DXF: TABLE layer - Center Assembly Table ===
    # Lines form box: (132,96) to (228,96) to (228,144) to (132,144) to (132,96)
    rect = Rectangle((132, 96), 96, 48, facecolor=c_table, alpha=0.3,
                      edgecolor=c_table, linewidth=2)
    ax.add_patch(rect)
    ax.text(180, 125, 'CENTER ASSEMBLY TABLE', ha='center', va='center', fontsize=9, fontweight='bold')
    ax.text(180, 108, '96"×48" (8\'×4\')', ha='center', va='center', fontsize=8, color='#666')

    # === FROM DXF: STORAGE layer - Sheet Goods/Lumber Stage ===
    # Lines form box: (0,0) to (96,0) to (96,60) to (0,60) to (0,0)
    rect = Rectangle((0, 0), 96, 60, facecolor=c_storage, alpha=0.3,
                      edgecolor=c_storage, linewidth=2)
    ax.add_patch(rect)
    ax.text(48, 38, 'SHEET GOODS', ha='center', va='center', fontsize=9, fontweight='bold')
    ax.text(48, 24, 'LUMBER STAGE', ha='center', va='center', fontsize=8)
    ax.text(48, 8, '96"×60" (40 sq ft)', ha='center', va='center', fontsize=7, color='#666', style='italic')

    # === FROM DXF: VENT layer - Fume + Fiberglass Bench ===
    # Lines form box: (270,156) to (360,156) to (360,186) to (270,186) to (270,156)
    rect = Rectangle((270, 156), 90, 30, facecolor=c_fume, alpha=0.3,
                      edgecolor=c_fume, linewidth=2)
    ax.add_patch(rect)
    ax.text(315, 175, 'FUME + FIBERGLASS BENCH', ha='center', va='center', fontsize=8, fontweight='bold')
    ax.text(315, 162, '90"×30"', ha='center', va='center', fontsize=7, color='#666')

    # Vent to outside indicator (from DXF: line at x=350-370, y=230)
    ax.annotate('VENT TO\nOUTSIDE', xy=(360, 230), xytext=(370, 215),
                fontsize=7, ha='left', color=c_fume,
                arrowprops=dict(arrowstyle='->', color=c_fume, lw=1.5))
    ax.plot([350, 370], [230, 230], color=c_fume, linewidth=3)

    # === PROPOSED: Her Zone (not in original DXF) ===
    # Proposed bounds: x: 0-120, y: 60-156
    rect = Rectangle((0, 60), 120, 96, facecolor=c_her, alpha=0.15,
                      edgecolor=c_her, linewidth=2, linestyle='--')
    ax.add_patch(rect)
    ax.text(60, 115, 'HER ZONE', ha='center', va='center', fontsize=10, fontweight='bold', color=c_her)
    ax.text(60, 100, '(PROPOSED)', ha='center', va='center', fontsize=8, color=c_her, style='italic')
    ax.text(60, 85, 'Fiber/Fine Arts/Paper', ha='center', va='center', fontsize=7, color='#666')
    ax.text(60, 70, '120"×96" (80 sq ft)', ha='center', va='center', fontsize=7, color='#666', style='italic')

    # === Legend ===
    legend_y = ROOM_HEIGHT + 40
    legend_items = [
        ('Electronics (DXF)', c_elec, '-'),
        ('Fabrication (DXF)', c_fab, '-'),
        ('Fume Zone (DXF)', c_fume, '-'),
        ('Assembly (DXF)', c_table, '-'),
        ('Storage (DXF)', c_storage, '-'),
        ('Cabinetry (DXF)', c_cab, '-'),
        ('Her Zone (PROPOSED)', c_her, '--'),
    ]
    for i, (label, color, ls) in enumerate(legend_items):
        x = 10 + i * 52
        rect = Rectangle((x, legend_y), 14, 10, facecolor=color, alpha=0.3,
                         edgecolor=color, linewidth=1.5, linestyle=ls)
        ax.add_patch(rect)
        ax.text(x + 7, legend_y - 6, label, ha='center', va='top', fontsize=6, rotation=45)

    # Note about DXF geometry error
    ax.text(5, ROOM_HEIGHT + 25,
            'Note: DXF shows Electronics bench extending to y=276 (outside room). Shown here as y=156-216.',
            fontsize=7, color='#999', style='italic')

    plt.tight_layout()
    plt.savefig('/Users/tjordan/code/git/craft_room/craft_room_zones.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print('Saved: craft_room_zones.png')


def render_flow():
    """Render traffic flow diagram based on DXF geometry."""
    fig, ax = setup_figure('CRAFT ROOM - TRAFFIC FLOW (based on DXF zones)')

    # Ghost zones for reference
    ghost = '#e0e0e0'
    alpha = 0.2

    # Cabinetry
    ax.add_patch(Rectangle((0, 216), 360, 24, facecolor=ghost, alpha=alpha, edgecolor='#ccc', lw=1))
    # Electronics bench
    ax.add_patch(Rectangle((0, 156), 60, 60, facecolor=ghost, alpha=alpha, edgecolor='#ccc', lw=1))
    # Dirty bench
    ax.add_patch(Rectangle((330, 72), 30, 144, facecolor=ghost, alpha=alpha, edgecolor='#ccc', lw=1))
    # Assembly table
    ax.add_patch(Rectangle((132, 96), 96, 48, facecolor=ghost, alpha=alpha, edgecolor='#ccc', lw=1))
    # Storage
    ax.add_patch(Rectangle((0, 0), 96, 60, facecolor=ghost, alpha=alpha, edgecolor='#ccc', lw=1))
    # Fume bench
    ax.add_patch(Rectangle((270, 156), 90, 30, facecolor=ghost, alpha=alpha, edgecolor='#ccc', lw=1))
    # Her zone (proposed)
    ax.add_patch(Rectangle((0, 60), 120, 96, facecolor=ghost, alpha=0.1, edgecolor='#ccc', lw=1, ls='--'))

    # Zone labels (subtle)
    ax.text(30, 186, 'ELEC', ha='center', fontsize=8, color='#aaa')
    ax.text(345, 144, 'FAB', ha='center', fontsize=8, color='#aaa', rotation=90)
    ax.text(180, 120, 'ASSEMBLY', ha='center', fontsize=8, color='#aaa')
    ax.text(48, 30, 'STORAGE', ha='center', fontsize=8, color='#aaa')
    ax.text(315, 171, 'FUME', ha='center', fontsize=8, color='#aaa')
    ax.text(60, 108, 'HER', ha='center', fontsize=8, color='#aaa')
    ax.text(180, 228, 'CABINETRY', ha='center', fontsize=8, color='#aaa')

    # === ENTRY ===
    entry = FancyBboxPatch((140, -15), 80, 18, boxstyle="round,pad=0.02",
                            facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=2)
    ax.add_patch(entry)
    ax.text(180, -6, 'ENTRY', ha='center', va='center', fontsize=10, fontweight='bold', color='#1565C0')

    # === PRIMARY CIRCULATION (wide path along open edge) ===
    ax.add_patch(Rectangle((96, 0), 234, 36, facecolor='#2196F3', alpha=0.2,
                           edgecolor='#1976D2', linewidth=2))
    ax.text(213, 18, 'PRIMARY CIRCULATION (36"+ clear)', ha='center', va='center',
            fontsize=8, color='#1565C0', fontweight='bold')

    # === SECONDARY PATHS ===
    # West corridor (between Her Zone and Assembly)
    ax.add_patch(Rectangle((120, 36), 12, 180, facecolor='#4CAF50', alpha=0.15,
                           edgecolor='#388E3C', linewidth=1.5, linestyle='--'))
    ax.text(126, 126, 'W', ha='center', va='center', fontsize=8, color='#2E7D32', fontweight='bold')

    # East corridor (between Assembly and Fab)
    ax.add_patch(Rectangle((228, 36), 102, 60, facecolor='#4CAF50', alpha=0.15,
                           edgecolor='#388E3C', linewidth=1.5, linestyle='--'))

    # Path to fume zone
    ax.add_patch(Rectangle((228, 144), 42, 42, facecolor='#4CAF50', alpha=0.15,
                           edgecolor='#388E3C', linewidth=1.5, linestyle='--'))

    # === PERSON FLOW ARROWS ===
    arrow_kw = dict(arrowstyle='->', color='#1565C0', lw=2,
                    connectionstyle='arc3,rad=0.1')

    # Entry to branches
    ax.annotate('', xy=(180, 50), xytext=(180, 0), arrowprops=arrow_kw)

    # To Her Zone
    ax.annotate('', xy=(60, 60), xytext=(126, 50),
                arrowprops=dict(arrowstyle='->', color='#4CAF50', lw=2))
    ax.text(85, 70, 'To Her\nZone', ha='center', fontsize=7, color='#2E7D32')

    # To Electronics
    ax.annotate('', xy=(30, 156), xytext=(60, 70),
                arrowprops=dict(arrowstyle='->', color='#2196F3', lw=2))
    ax.text(35, 115, 'To\nElec', ha='center', fontsize=7, color='#1565C0')

    # To Assembly
    ax.annotate('', xy=(180, 96), xytext=(180, 50),
                arrowprops=dict(arrowstyle='->', color='#1565C0', lw=2))
    ax.text(188, 75, 'To\nAssembly', ha='left', fontsize=7, color='#1565C0')

    # To Fabrication
    ax.annotate('', xy=(330, 100), xytext=(228, 50),
                arrowprops=dict(arrowstyle='->', color='#FF5722', lw=2))
    ax.text(280, 65, 'To Fab', ha='center', fontsize=7, color='#E64A19')

    # To Fume Zone (from Fab)
    ax.annotate('', xy=(300, 156), xytext=(330, 144),
                arrowprops=dict(arrowstyle='->', color='#F44336', lw=2))
    ax.text(310, 150, 'To\nFume', ha='center', fontsize=7, color='#D32F2F')

    # === MATERIAL FLOW (dotted orange) ===
    mat_kw = dict(arrowstyle='->', color='#FF9800', lw=2.5, linestyle='dotted')

    # Materials in to storage
    ax.annotate('', xy=(48, 50), xytext=(48, -15),
                arrowprops=mat_kw)
    ax.text(35, -20, 'Materials\nIn', ha='center', fontsize=7, color='#E65100', fontweight='bold')

    # Storage to Assembly
    ax.annotate('', xy=(132, 110), xytext=(96, 55),
                arrowprops=mat_kw)

    # Assembly to Fab
    ax.annotate('', xy=(330, 120), xytext=(228, 120),
                arrowprops=mat_kw)

    # Fab to Fume
    ax.annotate('', xy=(315, 156), xytext=(340, 140),
                arrowprops=mat_kw)

    # Fume to Out
    ax.annotate('', xy=(375, 171), xytext=(330, 171),
                arrowprops=mat_kw)
    ax.text(378, 171, 'Out', ha='left', va='center', fontsize=8, color='#E65100', fontweight='bold')

    # === AIRFLOW ===
    ax.annotate('', xy=(340, 200), xytext=(60, 200),
                arrowprops=dict(arrowstyle='->', color='#9C27B0', lw=2, linestyle='dashed'))
    ax.text(200, 205, 'AIRFLOW: Clean (West) → Dirty (East) → EXHAUST',
            ha='center', fontsize=8, color='#7B1FA2', style='italic')

    # Exhaust at vent
    ax.annotate('EXHAUST', xy=(360, 230), xytext=(340, 200),
                arrowprops=dict(arrowstyle='->', color='#9C27B0', lw=2),
                fontsize=8, color='#7B1FA2', fontweight='bold')

    # === LEGEND ===
    ly = ROOM_HEIGHT + 45
    ax.add_patch(Rectangle((20, ly), 30, 8, facecolor='#2196F3', alpha=0.3, edgecolor='#1976D2', lw=2))
    ax.text(55, ly+4, 'Primary Path', va='center', fontsize=8)

    ax.add_patch(Rectangle((120, ly), 30, 8, facecolor='#4CAF50', alpha=0.2, edgecolor='#388E3C', lw=1.5, ls='--'))
    ax.text(155, ly+4, 'Secondary', va='center', fontsize=8)

    ax.annotate('', xy=(235, ly+4), xytext=(210, ly+4), arrowprops=dict(arrowstyle='->', color='#FF9800', lw=2))
    ax.text(240, ly+4, 'Material Flow', va='center', fontsize=8)

    ax.plot([300, 330], [ly+4, ly+4], color='#9C27B0', lw=2, ls='--')
    ax.text(335, ly+4, 'Airflow', va='center', fontsize=8)

    # Flow summary
    ax.text(180, -35, 'Materials enter SW (storage) → Assembly → Fab → Fume → Exit NE',
            ha='center', fontsize=8, style='italic', color='#666')

    plt.tight_layout()
    plt.savefig('/Users/tjordan/code/git/craft_room/craft_room_flow.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print('Saved: craft_room_flow.png')


if __name__ == '__main__':
    render_zones()
    render_flow()
    print('Done!')
