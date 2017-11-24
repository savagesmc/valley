import os

def getSongs(root):
   r, l1, l2 = os.walk(root)
   return r[1]

def getFilenames(files, filt):
   return [f  for f in files if filt in f ]

def getPages(path):
   f = os.listdir(path)
   return getFilenames(f, 'jpg')

def getMp3Files(path):
   f = os.listdir(path)
   return getFilenames(f, 'mp3')
