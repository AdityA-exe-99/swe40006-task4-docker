import os
import datetime

# these paths are inside the container. the actual files live on the host
# and get mapped in here with "docker run -v", which is what proves the
# volume mount / persistent storage requirement for Task 4.4.
SCORES_FILE = "/data/scores.txt"
REPORT_FILE = "/data/report.txt"


def read_scores(path):
    scores = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # each line in scores.txt is just "PlayerName score", e.g. "Aditya 87"
            parts = line.split()
            name = parts[0]
            score = int(parts[1])
            scores.append((name, score))
    return scores


def main():
    print("=== GameDev Toolkit: Score Log Analyzer ===")

    if not os.path.exists(SCORES_FILE):
        print(f"ERROR: {SCORES_FILE} not found. Did you mount the data folder with -v?")
        return

    scores = read_scores(SCORES_FILE)

    if not scores:
        print("No scores found in the log file.")
        return

    values = [s for _, s in scores]
    games_played = len(values)
    high_score = max(values)
    high_scorer = [name for name, s in scores if s == high_score][0]
    average = sum(values) / games_played

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    summary = (
        f"--- Report generated {timestamp} ---\n"
        f"Games played:  {games_played}\n"
        f"High score:    {high_score} (by {high_scorer})\n"
        f"Average score: {average:.2f}\n"
        f"\n"
    )

    print(summary)

    # append (not overwrite) so re-running the container keeps a running
    # history in report.txt, this is what proves the data persists on the
    # host even after the container is removed
    with open(REPORT_FILE, "a") as f:
        f.write(summary)

    print(f"Report appended to {REPORT_FILE} on the mounted volume.")


if __name__ == "__main__":
    main()
