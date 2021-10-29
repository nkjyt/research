from PIL import Image
from PIL import ImageDraw
import csv

def fullPageRect():
    source = "TBan_A30_EJ01_001_20200126210258.csv"
    csv_file = open(source, "r", encoding="ms932", errors="", newline="")
    f = csv.reader(csv_file,  delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    data = []
    img = Image.open('00001.png')
    draw = ImageDraw.Draw(img)
    rectcolor = (255,0,0)
    linewidth = 4

    for row in f:
        if row[2] == '1' and row[5] == '1':
            print(row[15])
            data.append([int(row[i]) for i in range(6,10)])
            data = [int(row[i]) for i in range(6,10)]
            print(data)
            draw.rectangle([(data[0], data[1]), (data[2], data[3])], outline=rectcolor, width = linewidth)

    img.save("output.png")


source = "TBan_A30_EJ01_001_20200126210258.csv"
csv_file = open(source, "r", encoding="ms932", errors="", newline="")
f = csv.reader(csv_file,  delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

data = []
img = Image.open('10005.png')
draw = ImageDraw.Draw(img)
rectcolor = (255,0,0)
linewidth = 4

for row in f:
    if row[2] == '1' and row[5] == '1':
        print(row[15])
        data.append([int(row[i]) for i in range(6,10)])
        data = [int(row[i]) for i in range(6,10)]
        print(data)
        draw.rectangle([(data[0], data[1]), (data[2], data[3])], outline=rectcolor, width = linewidth)

img.save("output_half.png")
