import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

def main():
    # Figure & axes
    fig, ax = plt.subplots(figsize=(6, 8), facecolor="#131123")
    ax.set_facecolor("#131123")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")

    # --- Background stars ---
    rng = np.random.default_rng(31)
    num_stars = 140
    xs = rng.uniform(0, 10, num_stars)
    ys = rng.uniform(4, 10, num_stars)
    sizes = rng.uniform(5, 25, num_stars)
    ax.scatter(xs, ys, s=sizes, c="white", alpha=0.9, linewidths=0)

    # --- Ghost path (body with scalloped bottom) ---
    verts = [
        (5.0, 8.6),               # 0: top
        (4.0, 8.9), (3.2, 8.0), (3.0, 6.7),     # left curve down
        (2.9, 5.5), (3.0, 4.6), (3.2, 4.0),     # towards bottom-left
        # scallops (3 bumps)
        (3.7, 3.3), (4.3, 3.3), (4.8, 4.0),     # bump 1
        (5.3, 3.3), (5.9, 3.3), (6.4, 4.0),     # bump 2
        (6.8, 3.7), (7.1, 4.2), (7.0, 4.6),     # bump 3 end
        (6.9, 6.2), (6.7, 7.6), (5.8, 8.4),     # right curve up
        (5.4, 8.7), (5.2, 8.7), (5.0, 8.6),     # close to top
        (0.0, 0.0),                               # placeholder for CLOSEPOLY
    ]
    codes = [Path.MOVETO] + [Path.CURVE4] * (len(verts) - 2) + [Path.CLOSEPOLY]

    body_path = Path(verts, codes)

    # Soft drop shadow
    shadow_dx, shadow_dy = 0.18, -0.18
    shadow_verts = [(x + shadow_dx, y + shadow_dy) for (x, y) in verts]
    shadow_path = Path(shadow_verts, codes)
    shadow = patches.PathPatch(
        shadow_path, facecolor="black", edgecolor="none", alpha=0.18, zorder=1
    )
    ax.add_patch(shadow)

    # Ghost body
    ghost = patches.PathPatch(
        body_path, facecolor="white", edgecolor="#e6f3ff", lw=3, zorder=2, joinstyle="round"
    )
    ax.add_patch(ghost)

    # --- Face ---
    # Eyes
    eye_L = patches.Circle((4.35, 6.55), 0.18, facecolor="#161616", edgecolor="none", zorder=3)
    eye_R = patches.Circle((5.65, 6.55), 0.18, facecolor="#161616", edgecolor="none", zorder=3)
    ax.add_patch(eye_L); ax.add_patch(eye_R)

    # Eye sparkles
    spark_L = patches.Circle((4.27, 6.62), 0.05, facecolor="white", edgecolor="none", zorder=4)
    spark_R = patches.Circle((5.57, 6.62), 0.05, facecolor="white", edgecolor="none", zorder=4)
    ax.add_patch(spark_L); ax.add_patch(spark_R)

    # Cheeks
    cheek_L = patches.Circle((4.10, 6.05), 0.16, facecolor="#ffb3c1", edgecolor="none", alpha=0.8, zorder=3)
    cheek_R = patches.Circle((5.90, 6.05), 0.16, facecolor="#ffb3c1", edgecolor="none", alpha=0.8, zorder=3)
    ax.add_patch(cheek_L); ax.add_patch(cheek_R)

    # Smile (arc)
    smile = patches.Arc((5.0, 6.2), width=0.7, height=0.35, angle=0, theta1=200, theta2=340,
                        color="#1a1a1a", lw=2.5, zorder=3)
    ax.add_patch(smile)

    # --- Little arms ---
    arm_L = Path(
        [(3.6, 5.4), (3.2, 5.6), (3.0, 5.9)],
        [Path.MOVETO, Path.CURVE3, Path.CURVE3],
    )
    arm_R = Path(
        [(6.4, 5.4), (7.0, 5.6), (7.2, 5.2)],
        [Path.MOVETO, Path.CURVE3, Path.CURVE3],
    )
    ax.add_patch(patches.PathPatch(arm_L, edgecolor="#e6f3ff", facecolor="none", lw=3, zorder=3))
    ax.add_patch(patches.PathPatch(arm_R, edgecolor="#e6f3ff", facecolor="none", lw=3, zorder=3))

    # --- Pumpkin bucket ---
    pumpkin = patches.Circle((7.4, 4.7), 0.48, facecolor="#ff8c00", edgecolor="#d65a00", lw=2.5, zorder=3)
    ax.add_patch(pumpkin)

    # Bucket handle
    handle = patches.Arc((7.4, 4.9), width=0.8, height=0.6, angle=0, theta1=200, theta2=340,
                         color="#7a4b00", lw=3, zorder=4)
    ax.add_patch(handle)

    # Pumpkin face (triangles + mouth)
    tri1 = patches.Polygon([[7.25,4.85],[7.20,4.70],[7.30,4.70]], closed=True, facecolor="#1a1a1a", zorder=4)
    tri2 = patches.Polygon([[7.55,4.85],[7.50,4.70],[7.60,4.70]], closed=True, facecolor="#1a1a1a", zorder=4)
    mouth = patches.Polygon([[7.20,4.45],[7.30,4.35],[7.50,4.35],[7.60,4.45],[7.50,4.40],[7.30,4.40]],
                            closed=True, facecolor="#1a1a1a", zorder=4)
    ax.add_patch(tri1); ax.add_patch(tri2); ax.add_patch(mouth)

    # Little grab line from ghost arm to bucket
    grab = Path(
        [(6.9, 5.2), (7.05, 5.0), (7.2, 4.9)],
        [Path.MOVETO, Path.CURVE3, Path.CURVE3],
    )
    ax.add_patch(patches.PathPatch(grab, edgecolor="#e6f3ff", facecolor="none", lw=2, zorder=4))

    # Text
    ax.text(1.0, 9.0, "BOO!", color="white", fontsize=28, weight="bold", family="DejaVu Sans")

    # Candy sprinkles
    for (cx, cy) in [(2.2, 4.2), (3.0, 3.6), (8.0, 3.9), (1.3, 7.0), (8.7, 8.2)]:
        ax.add_patch(patches.Circle((cx, cy), 0.06, facecolor="#b1e5ff", edgecolor="none", alpha=0.9, zorder=2))
        ax.add_patch(patches.Circle((cx+0.12, cy+0.04), 0.06, facecolor="#ffd1dc", edgecolor="none", alpha=0.9, zorder=2))

    # Save and show
    out_path = "/mnt/data/cute_halloween_ghost.png"
    plt.savefig(out_path, dpi=220, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.show()


if __name__ == "__main__":
    main()

