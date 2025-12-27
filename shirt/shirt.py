from PIL import ImageOps, Image
import sys
import os


if len(sys.argv) < 3:
    sys.exit("Too few arguments")

if os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
    sys.exit("Extensions do not match")

# for infile in sys.argv[1:]:
#     if os.path.splitext(infile)[1] not in [[".jpg", ".jpeg", ".png"]]:
#         sys.exit("File type not supported")

if os.path.splitext(sys.argv[1])[1] not in [".jpg", ".jpeg", ".png"] and os.path.splitext(sys.argv[2])[1] not in [".jpg", ".jpeg", ".png"]:
    sys.exit("File type not supported")


def main():
    # try:
    file = Image.open("shirt.png")
    size = file.size
    # except FileNotFoundError:
    #     sys.exit()

    shirt = Image.open(sys.argv[1])
    # Resizing
    shirt = ImageOps.fit(shirt, size)
    shirt.paste(file, file)
    shirt.save(sys.argv[2])

    file.close
    shirt.close


if __name__ == "__main__":
    main()
