from tabulate import tabulate
from PIL import Image, ImageFont, ImageDraw
import sys
import csv

if len(sys.argv) < 2:
    sys.exit("Too few arguments")


def main():
    table = create_table()

    print(table)
    # generate_table_pic(table)


def create_table():

    table = []

    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
        table = tabulate(table, tablefmt="grid", headers="firstrow")
        return table

    except (FileNotFoundError):
        sys.exit("File does not exist")


# def generate_table_pic(table):
#     font = ImageFont.load_default()
#     dummy_img = Image.new("RGB", (1, 1))
#     dummy_draw = ImageDraw.Draw(dummy_img)
#     w, h = dummy_draw.textbbox((0, 0), table, font=font)[2:]

# #     img = Image.new("RGB", (w + 20, h + 20), "white")
# #     draw = ImageDraw.Draw(img)

# #     draw.text((10, 10), table, fill="black", font=font)
# #     img.save("new_timetable.png")

#     img = Image.new("RGB", (w + 1672,h + 688), "white")
#     draw = ImageDraw.Draw(img)

#     draw.text((10, 10), table, fill="black", font=font)
#     img.save("new_timetable.png")


if __name__ == "__main__":
    main()
