from time import sleep
def progress(percent=0, width=50):
    left = width * percent // 100
    right = width - left

    tags = "#" * left
    spaces = " " * right
    percents = f"{percent:.0f}%"

    print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)
# Example run
for i in range(101):
    progress(i)
    sleep(0.05)
