import os

def getSongs(root):
   result = []
   for root, dirs, files in os.walk(root):
      for dir in dirs:
         result.append(dir)
   return result

def getFilenames(files, filt):
   return [f  for f in files if filt in f ]

def getPages(path):
   f = os.listdir(path)
   return getFilenames(f, 'jpg')

def getMp3Files(path):
   f = os.listdir(path)
   return getFilenames(f, 'mp3')

def getMp4Files(path):
   f = os.listdir(path)
   return getFilenames(f, 'mp4')
