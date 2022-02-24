from pytube import YouTube

url = input('Ingrese la URL del video a Descargar: ')
video = YouTube(url)
# Esto transmitirá todos los formatos de descarga disponible para el vídeo
try:
  videos = video.streams.all()
  # Esto enumera los formatos disponibles del video
  formatos = list(enumerate(videos))
  for i in formatos:
    print(i)
    # Esto imprimir'a los formatos de descarga disponibles

  dn_opcion = int(input('Ingrese el número correspondiente a la calidad del video para descargar: '))
  dn_video = videos[dn_opcion]
  dn_video.download('C:/Users/USER/Downloads')
  print('Descarga exitosa!')
except:
  print('Ha ocurrido un error')