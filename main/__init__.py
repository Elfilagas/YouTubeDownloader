from pytube import YouTube
from sys import argv


def download():
    link = input("Input YouTube link: ")
    yt = YouTube(link)

    print(f"Title: {yt.title}")
    print(f"Title: {yt.views}")


def main():
    download()


if __name__ == '__main__':
    main()
