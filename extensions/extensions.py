def main():
    media = input("File name: ").lower()
    media = media.strip()
    if media.endswith(".gif"):
        print("image/gif")
    elif media.endswith(".jpg"):
        print("image/jpeg")
    elif media.endswith(".png"):
        print("image/png")
    elif media.endswith(".jpeg"):
        print("image/jpeg")
    elif media.endswith(".pdf"):
        print("application/pdf")
    elif media.endswith(".txt"):
        print("text/plain")
    elif media.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()
