from pytube import YouTube


url_video = input('Ingrese la URL del video a Descargar: ')
destino = input('Ingrese el destino donde desea descargar el archivo: ')

yt = YouTube(url_video)
name_video = yt.title
print('Se descargará el Archivo:', name_video)
videos = yt.streams.all()

video = list(enumerate(videos))
for i in video:
  print(i)

dn_opcion = int(input('Ingrese el Número correspondiente al formato para Descargar: '))
dn_video = videos[dn_opcion]
try:
  dn_video.download(destino)
  print(f'Se ha descargado su video en {destino}')
except:
  print('Ha ocurrido un error')