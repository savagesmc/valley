import os

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

def getGroup(path):
   f = os.listdir(path)
   group = "General Songs"
   fname = getFilenames(f, 'group.txt')
   if fname:
      groupFile = path + '/' + fname[0]
      with open(groupFile, 'r') as myfile:
         group = myfile.read()
         if 'expired' in group:
            group="expired"
   return group

def getSongs(root):
   result = {}
   for root, dirs, files in os.walk(root):
      # print("debug: {} {} {}".format(root, dirs, files))
      for dir_ in dirs:
         group_ = getGroup(root+'/'+dir_)
         if group_ in result.keys():
            result[group_].append(dir_)
         elif group_ != 'expired':
            result[group_] = [dir_]
   return result

