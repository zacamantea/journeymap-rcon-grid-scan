import time
import os
from mcrcon import MCRcon

RCON_HOST = "SERVER_IP"
RCON_PORT = 25575
RCON_PASSWORD = "strongpassword"

PLAYERS = ["PLAYER1", "PLAYER2"]
Y = 200

STEP = 500
RADIUS = 10000
DELAY = 17

PROGRESS_FILE = "progress.txt"

def generate_spiral_points(step: int, radius: int):
    n = radius // step
    points = [(0, 0)]

    for k in range(1, n + 1):
        x = k
        z = k - 1

        z += 1
        points.append((x, z))

        for _ in range(2 * k):
            x -= 1
            points.append((x, z))

        for _ in range(2 * k):
            z -= 1
            points.append((x, z))

        for _ in range(2 * k):
            x += 1
            points.append((x, z))

        for _ in range(2 * k - 1):
            z += 1
            points.append((x, z))

    world_points = []
    for gx, gz in points:
        wx = gx * step
        wz = gz * step
        if -radius <= wx <= radius and -radius <= wz <= radius:
            world_points.append((wx, wz))

    seen = set()
    ordered = []
    for p in world_points:
        if p not in seen:
            seen.add(p)
            ordered.append(p)

    return ordered

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r") as f:
                return int(f.read().strip())
        except Exception:
            return 0
    return 0

def save_progress(index: int):
    with open(PROGRESS_FILE, "w") as f:
        f.write(str(index))

def main():
    points = generate_spiral_points(STEP, RADIUS)
    total = len(points)
    start_index = load_progress()

    if start_index < 0 or start_index > total:
        start_index = 0

    if start_index >= total:
        print(f"Already finished. Progress {total}/{total} (100.00%).")
        return

    print(f"Starting at {start_index}/{total} ({(start_index/total)*100:.2f}%).")
    print("If you changed STEP, RADIUS, or scan order, delete progress.txt once.")

    with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as rcon:
        print("Connected to RCON")

        for i in range(start_index, total):
            x, z = points[i]
            current = i + 1
            percent = (current / total) * 100

            for player in PLAYERS:
                cmd = f"tp {player} {x} {Y} {z}"
                print(f"{current}/{total} ({percent:.2f}%) -> {cmd}")
                rcon.command(cmd)

            save_progress(current)
            time.sleep(DELAY)

    print(f"Finished. Progress {total}/{total} (100.00%). Auto-stopping.")

if __name__ == "__main__":
    main()
