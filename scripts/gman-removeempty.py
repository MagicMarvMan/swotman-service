import os

with open("download.txt", "r") as readfile:
    with open("final.txt", "w") as donefile:
        donefile.write(os.linesep.join([s for s in readfile.read().splitlines() if s]))
        print("Done.")