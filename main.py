import os

LINE = "My lidar keeps flagging you as an obstacle, so tonight I'm overriding collision avoidance."


def main():
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    if out == "/output/entry.txt":
        os.makedirs("/output", exist_ok=True)
    elif os.path.dirname(out):
        os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
