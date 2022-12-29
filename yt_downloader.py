from pytube import YouTube
from pytube.cli import on_progress
from os.path import isfile, isdir
from os import mkdir

def Download():
  print('\n-----------------------------------------------------------\n')
  url = input('Video URL: ')
  print('\n-----------------------------------------------------------\n')
  yt_object = YouTube(url=url, on_progress_callback=on_progress)
  streams = yt_object.streams

  # Show all the possibility of quality and the video itag to download
  for stream in streams:
    print(stream)

  print('\n-----------------------------------------------------------\n')
  itag = int(input('ITAG: '))
  print('\n-----------------------------------------------------------\n')
  data = streams.get_by_itag(itag=itag)
  size = data.filesize_mb
  default_filename = data.default_filename

  try:
    # Verify if the 'downloads' directory exists
    # and create that directory if is not
    if not isdir('./downloads'):
      mkdir('downloads')

    # Verify if the file already exists and make message if it is
    if isfile('./downloads/' + data.default_filename):
      print('File already exists.')
    else:
      filename = input('Enter file [' + data.default_filename + ']: ')

      # Give the default filename if the user input is empty
      if filename == '':
        filename = default_filename
        
      print('Downloading "' + filename + '"...\n')
      data.download(filename=str('./downloads/' + filename))
      print('\n\nFile name : ' + filename)
      print('File size: ' + str(size) + 'Mb')

  except:
    print('Download Failed.')