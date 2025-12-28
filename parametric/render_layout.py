#!/usr/bin/env python3
"""
Parametric 2D floor plan renderer for Craft Room.
Reads dimensions from data/parameters.json and generates layout visualization.
"""

import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent
PARAMS_FILE = SCRIPT_DIR / "data" / "parameters.json"
OUTPUT_DIR = SCRIPT_DIR / "exports"


def load_parameters():
    """Load parameters from JSON file."""
    with open(PARAMS_FILE, 'r') as f:
        return json.load(f)


def setup_figure(params, title):
    """Create figure with room outline from parameters."""
    room = params['room']
    bump = params.get('bump_out', {})

    room_w = room['room_width']
    room_d = room['room_depth']

    # Figure size proportional to room
    fig_w = 14
    fig_h = fig_w * (room_d / room_w) * 0.7
    fig, ax = plt.subplots(1, 1, figsize=(fig_w, fig_h))

    ax.set_facecolor('white')

    # Grid (4' = 48")
    for x in range(0, room_w + 1, 48):
        ax.axvline(x, color='#e8e8e8', linewidth=0.5, zorder=0)
        if 0 < x < room_w:
            ax.text(x, -12, f"{x//12}'", ha='center', fontsize=7, color='#999')
    for y in range(0, room_d + 1, 48):
        ax.axhline(y, color='#e8e8e8', linewidth=0.5, zorder=0)
        if 0 < y < room_d:
            ax.text(-12, y, f"{y//12}'", ha='right', va='center', fontsize=7, color='#999')

    # Main room outline
    ax.plot([0, room_w], [0, 0], 'k--', linewidth=2.5)  # South - OPEN (dashed)
    ax.plot([room_w, room_w], [0, room_d], 'k-', linewidth=3)  # East
    ax.plot([room_w, 0], [room_d, room_d], 'k-', linewidth=3)  # North
    ax.plot([0, 0], [room_d, 0], 'k-', linewidth=3)  # West

    # Bump-out outline (if enabled)
    if bump.get('enabled'):
        bx0 = bump['x_start']
        bx1 = bump['x_end']
        by0 = bump['y_start']
        by1 = bump['y_end']
        # Draw bump-out extension
        ax.plot([bx0, bx1], [by0, by0], 'k-', linewidth=3)  # Bottom of bump
        ax.plot([bx1, bx1], [by0, by1], 'k-', linewidth=3)  # Right side
        ax.plot([bx1, bx0], [by1, by1], 'k-', linewidth=3)  # Top
        # Opening into main room (remove wall segment)
        ax.plot([bx0, bx0], [by0, by1], 'k--', linewidth=1, alpha=0.3)  # Opening

    # Axis setup
    x_max = max(room_w, bump.get('x_end', room_w)) + 60
    ax.set_xlim(-40, x_max)
    ax.set_ylim(-50, room_d + 70)
    ax.set_aspect('equal')
    ax.set_xlabel('Inches', fontsize=10)
    ax.set_ylabel('Inches', fontsize=10)
    ax.set_title(title, fontsize=14, fontweight='bold', pad=15)

    # Dimension annotations
    ax.annotate('', xy=(room_w, -25), xytext=(0, -25),
                arrowprops=dict(arrowstyle='<->', color='#666', lw=1.5))
    ax.text(room_w/2, -35, f'{room_w}" ({room["room_width_ft"]}\'-0")',
            ha='center', fontsize=10, color='#444')

    ax.annotate('', xy=(-25, room_d), xytext=(-25, 0),
                arrowprops=dict(arrowstyle='<->', color='#666', lw=1.5))
    ax.text(-30, room_d/2, f'{room_d}" ({room["room_depth_ft"]}\'-0")',
            ha='center', va='center', fontsize=10, color='#444', rotation=90)

    # Wall labels
    ax.text(room_w/2, 15, 'OPEN EDGE (south - entry)',
            ha='center', fontsize=9, color='#666', style='italic')
    ax.text(room_w/2, room_d + 15, 'BACK WALL (north - exterior)',
            ha='center', fontsize=9, color='#666', style='italic')

    return fig, ax


def render_zones(params):
    """Render zone allocation diagram from parameters."""
    fig, ax = setup_figure(params, 'CRAFT ROOM - ZONE LAYOUT (15\' x 30\' + 4\' Bump-Out)')

    zones = params['zones']
    bump = params.get('bump_out', {})

    # Zone colors
    colors = {
        'clean': '#4CAF50',       # Green
        'dusty': '#FF9800',       # Orange
        'dirty_fume': '#F44336',  # Red
        'shared': '#9E9E9E',      # Gray
        'infrastructure': '#795548',  # Brown
    }

    # Draw each zone
    for zone_id, zone in zones.items():
        x = zone['x_start']
        y = zone['y_start']
        w = zone['width']
        d = zone['depth']
        cat = zone.get('category', 'shared')
        color = colors.get(cat, '#999999')

        # Special handling for bump-out zone
        alpha = 0.35 if zone.get('in_bump_out') else 0.25

        rect = Rectangle((x, y), w, d,
                         facecolor=color, alpha=alpha,
                         edgecolor=color, linewidth=2)
        ax.add_patch(rect)

        # Zone label
        cx, cy = x + w/2, y + d/2
        name = zone['name']

        # Adjust text for narrow/tall zones
        fontsize = 8 if w < 50 or d < 50 else 9

        if w < 40:  # Vertical text for narrow zones
            ax.text(cx, cy, name, ha='center', va='center',
                   fontsize=fontsize, fontweight='bold', rotation=90)
        else:
            # Split long names
            if len(name) > 20:
                parts = name.split(' ', 2)
                ax.text(cx, cy + 8, ' '.join(parts[:2]), ha='center', va='center',
                       fontsize=fontsize, fontweight='bold')
                if len(parts) > 2:
                    ax.text(cx, cy - 8, parts[2], ha='center', va='center',
                           fontsize=fontsize-1)
            else:
                ax.text(cx, cy, name, ha='center', va='center',
                       fontsize=fontsize, fontweight='bold')

        # Area label
        area = zone.get('area_sqft', 0)
        if area and d > 30:
            ax.text(cx, y + 12, f'{area} sq ft', ha='center', va='center',
                   fontsize=7, color='#666', style='italic')

    # Draw soft dust barrier
    barrier = params.get('infrastructure', {}).get('soft_dust_barrier', {})
    if barrier:
        bx = barrier.get('x', 84)
        by0 = barrier.get('y_start', 72)
        by1 = barrier.get('y_end', 300)
        ax.plot([bx, bx], [by0, by1], color='#9C27B0', linewidth=2,
               linestyle=':', alpha=0.7)
        ax.text(bx, (by0+by1)/2, 'DUST\nBARRIER', ha='center', va='center',
               fontsize=7, color='#7B1FA2', rotation=90, alpha=0.8)

    # Bump-out label
    if bump.get('enabled'):
        bx = (bump['x_start'] + bump['x_end']) / 2
        by = bump['y_end'] + 8
        ax.text(bx, by, f"4' × 4' BUMP-OUT", ha='center', fontsize=8,
               color='#666', style='italic')

    # Legend
    legend_y = params['room']['room_depth'] + 45
    legend_items = [
        ('Clean Zone', colors['clean']),
        ('Dusty Zone', colors['dusty']),
        ('Fume Zone', colors['dirty_fume']),
        ('Shared', colors['shared']),
        ('Infrastructure', colors['infrastructure']),
    ]
    for i, (label, color) in enumerate(legend_items):
        x = 10 + i * 38
        rect = Rectangle((x, legend_y), 12, 8, facecolor=color, alpha=0.3,
                         edgecolor=color, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + 6, legend_y - 8, label, ha='center', va='top',
               fontsize=6, rotation=45)

    # Total area
    total_sqft = params['bump_out'].get('total_room_sqft',
                 params['room'].get('main_area_sqft', 0))
    ax.text(params['room']['room_width'] - 10, legend_y + 4,
           f'Total: {total_sqft} sq ft', ha='right', fontsize=9,
           fontweight='bold', color='#333')

    return fig, ax


def render_stations(params):
    """Render station placement diagram."""
    fig, ax = setup_figure(params, 'CRAFT ROOM - STATION LAYOUT (15\' x 30\')')

    zones = params['zones']
    stations = params['stations']

    # Draw zones as ghost background
    for zone_id, zone in zones.items():
        rect = Rectangle((zone['x_start'], zone['y_start']),
                         zone['width'], zone['depth'],
                         facecolor='#f5f5f5', alpha=0.5,
                         edgecolor='#ddd', linewidth=1)
        ax.add_patch(rect)

    # Station placements (calculated positions within zones)
    # These are example placements - would be refined based on actual layout
    station_positions = {
        # Clean zone stations (against west wall, stacked north-south)
        'melissa_workbench_phenolic': {'x': 6, 'y': 240, 'zone': 'zone_clean'},
        'melissa_pc_station': {'x': 6, 'y': 180, 'zone': 'zone_clean'},
        'electronics_bench': {'x': 6, 'y': 130, 'zone': 'zone_clean'},
        'printer_bay_3d': {'x': 42, 'y': 270, 'zone': 'zone_clean'},
        'cricut_station': {'x': 42, 'y': 240, 'zone': 'zone_clean'},

        # Dusty zone stations
        'breakdown_table': {'x': 108, 'y': 90, 'zone': 'zone_dusty'},
        'cnc_bay': {'x': 108, 'y': 160, 'zone': 'zone_dusty'},
        'sanding_table_downdraft': {'x': 138, 'y': 230, 'zone': 'zone_dusty'},

        # Receiving zone
        'vertical_sheet_rack': {'x': 12, 'y': 6, 'zone': 'zone_receiving'},
        'lumber_rack': {'x': 6, 'y': 48, 'zone': 'zone_receiving'},

        # Pack/ship
        'pack_ship_bench': {'x': 120, 'y': 6, 'zone': 'zone_packship'},

        # Fume zone (bump-out)
        'dirty_vent_table': {'x': 183, 'y': 267, 'zone': 'zone_fume'},
    }

    # Draw stations
    for station_id, pos in station_positions.items():
        if station_id not in stations:
            continue

        s = stations[station_id]
        x, y = pos['x'], pos['y']
        w = s.get('width', s.get('machine_width', 30))
        d = s.get('depth', s.get('machine_depth', 24))

        # Station rectangle
        rect = Rectangle((x, y), w, d,
                         facecolor='#E3F2FD', alpha=0.8,
                         edgecolor='#1976D2', linewidth=1.5)
        ax.add_patch(rect)

        # Label
        label = station_id.replace('_', '\n').replace('phenolic', '').replace('station', '')
        ax.text(x + w/2, y + d/2, label, ha='center', va='center',
               fontsize=5, color='#0D47A1')

    # Draw kayak lane indicator
    circ = params['circulation']
    kayak_len = circ.get('kayak_lane_length_available', 264)
    ax.add_patch(Rectangle((72, 72), 24, kayak_len,
                           facecolor='#E8F5E9', alpha=0.3,
                           edgecolor='#4CAF50', linewidth=2, linestyle='--'))
    ax.text(84, 72 + kayak_len/2, f'KAYAK LANE\n{kayak_len//12}\' CLEAR',
           ha='center', va='center', fontsize=8, color='#2E7D32', rotation=90)

    # Cabinetry runs
    cab = params['cabinetry']
    back_cab = cab['cabinet_run_back_wall']
    ax.add_patch(Rectangle((back_cab['x_start'], back_cab['y_start']),
                           back_cab['length'], back_cab['depth'],
                           facecolor='#795548', alpha=0.3,
                           edgecolor='#5D4037', linewidth=2))
    ax.text(back_cab['length']/2, back_cab['y_start'] + 12,
           'CABINETRY (15\')', ha='center', fontsize=8, color='#4E342E')

    return fig, ax


def render_flow(params):
    """Render traffic and material flow diagram."""
    fig, ax = setup_figure(params, 'CRAFT ROOM - WORKFLOW + AIRFLOW')

    zones = params['zones']
    room = params['room']

    # Ghost zones
    for zone_id, zone in zones.items():
        rect = Rectangle((zone['x_start'], zone['y_start']),
                         zone['width'], zone['depth'],
                         facecolor='#f0f0f0', alpha=0.3,
                         edgecolor='#ccc', linewidth=1)
        ax.add_patch(rect)
        # Zone label
        cx = zone['x_start'] + zone['width']/2
        cy = zone['y_start'] + zone['depth']/2
        short_name = zone['name'].split()[0]
        ax.text(cx, cy, short_name, ha='center', va='center',
               fontsize=8, color='#aaa')

    # Entry indicator
    entry_x = room['room_width'] / 2
    entry = FancyBboxPatch((entry_x - 30, -20), 60, 18,
                           boxstyle="round,pad=0.02",
                           facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=2)
    ax.add_patch(entry)
    ax.text(entry_x, -11, 'ENTRY', ha='center', va='center',
           fontsize=10, fontweight='bold', color='#1565C0')

    # Material flow arrows (orange, one-way)
    flow_color = '#FF9800'
    arrow_kw = dict(arrowstyle='->', color=flow_color, lw=2.5)

    # 1. Entry to Receiving
    ax.annotate('', xy=(42, 36), xytext=(60, 0),
                arrowprops=arrow_kw)

    # 2. Receiving to Breakdown
    ax.annotate('', xy=(120, 100), xytext=(60, 50),
                arrowprops=arrow_kw)

    # 3. Breakdown to CNC
    ax.annotate('', xy=(130, 180), xytext=(130, 140),
                arrowprops=arrow_kw)

    # 4. CNC to Fume Zone (via bump-out)
    ax.annotate('', xy=(200, 285), xytext=(155, 210),
                arrowprops=arrow_kw)

    # 5. Fume to Pack/Ship (finished goods)
    ax.annotate('', xy=(150, 24), xytext=(200, 270),
                arrowprops=dict(arrowstyle='->', color=flow_color, lw=2.5,
                               connectionstyle='arc3,rad=-0.3'))

    # Flow labels
    ax.text(30, 60, '1. RECEIVE', fontsize=7, color='#E65100', fontweight='bold')
    ax.text(95, 85, '2. BREAKDOWN', fontsize=7, color='#E65100', fontweight='bold')
    ax.text(145, 160, '3. CNC', fontsize=7, color='#E65100', fontweight='bold')
    ax.text(175, 250, '4. FINISH', fontsize=7, color='#E65100', fontweight='bold')
    ax.text(155, 40, '5. SHIP', fontsize=7, color='#E65100', fontweight='bold')

    # Airflow (west to east, purple dashed)
    air_y = 200
    ax.annotate('', xy=(175, air_y), xytext=(10, air_y),
                arrowprops=dict(arrowstyle='->', color='#9C27B0', lw=2, linestyle='dashed'))
    ax.text(90, air_y + 12, 'AIRFLOW: Clean (W) → Dirty (E) → EXHAUST',
           ha='center', fontsize=8, color='#7B1FA2', style='italic')

    # Exhaust at bump-out
    bump = params['bump_out']
    if bump.get('enabled'):
        ex = bump['x_end']
        ey = (bump['y_start'] + bump['y_end']) / 2
        ax.annotate('EXHAUST', xy=(ex + 5, ey), xytext=(ex - 20, ey),
                   arrowprops=dict(arrowstyle='->', color='#9C27B0', lw=2),
                   fontsize=8, color='#7B1FA2', fontweight='bold')

    # Legend
    ly = room['room_depth'] + 50
    ax.plot([20, 50], [ly, ly], color=flow_color, lw=2.5)
    ax.text(55, ly, 'Material Flow (one-way)', va='center', fontsize=8)

    ax.plot([120, 150], [ly, ly], color='#9C27B0', lw=2, linestyle='--')
    ax.text(155, ly, 'Airflow', va='center', fontsize=8)

    return fig, ax


def main():
    """Generate all layout visualizations."""
    # Ensure output directory exists
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Load parameters
    params = load_parameters()
    print(f"Loaded parameters: {params['room']['room_width_ft']}' x {params['room']['room_depth_ft']}'")

    # Render zone layout
    fig, ax = render_zones(params)
    zone_file = OUTPUT_DIR / "layout_zones.png"
    plt.savefig(zone_file, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {zone_file}")

    # Render station layout
    fig, ax = render_stations(params)
    station_file = OUTPUT_DIR / "layout_stations.png"
    plt.savefig(station_file, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {station_file}")

    # Render flow diagram
    fig, ax = render_flow(params)
    flow_file = OUTPUT_DIR / "layout_flow.png"
    plt.savefig(flow_file, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {flow_file}")

    print("Done!")


if __name__ == '__main__':
    main()
