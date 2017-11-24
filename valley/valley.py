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
   result = getFilenames(f, 'jpg')
   print("getPages: {} : {}".format(path, f, result))
   return result

def getMp3Files(path):
   f = os.listdir(path)
   result = getFilenames(f, 'mp3')
   print("getMp3Files: {} : {} : {}".format(path, f, result))
   return result
