import os

def getSongs(root):
   print("getSongs: {}".format(root))
   r, l1, l2= os.walk(root)
   return r[1]

def getFilenames(files, filt):
   result = []
   for f in files:
      if filt in f:
         result.append(f)
   return result

def getPages(path):
   f = os.listdir(path)
   print("getPages: {} : {}".format(path, f))
   return getFilenames(f, 'jpg')

def getMp3Files(path):
   f = os.listdir(path)
   print("getMp3Files: {} : {}".format(path, f))
   return getFilenames(f, 'mp3')
