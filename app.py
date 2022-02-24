from pytube import YouTube

url = input('Ingrese la URL del video a Descargar: ')
video = YouTube(url)
# Esto listara todos los formatos de descarga disponible para el vídeo
videos = video.streams.all()