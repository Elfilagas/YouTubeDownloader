from pytube import YouTube


def download():
    link = input("Input YouTube link: ")
    yt = YouTube(link)
    res = yt.streams.get_highest_resolution()
    print(f"Downloading...")
    res.download('./YouTubeVideos/')
    print(f"Title: {yt.title}, has downloaded.")


def main():
    download()


if __name__ == '__main__':
    main()
