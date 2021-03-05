import pytube
url = 'https://www.youtube.com/watch?v=1OlHj9422Dc&list=LL&index=39'#insert link here

youtube = pytube.YouTube(url)
video = youtube.streams.first()
PATH_TO_DL = '/Users/username/yt_downloads'
video.download(PATH_TO_DL)
print('done')