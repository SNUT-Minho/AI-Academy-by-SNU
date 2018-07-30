
# coding: utf-8

# In[31]:


class Picture:
    def __init__(self, filepath):
        from PIL.Image import open
        data = open(filepath).getdata()
        self.jpgfile = list(data)
        self.mode = data.mode
        self.size = data.size

    def show(self):
        from PIL import Image
        im2 = Image.new(self.mode, self.size)
        im2.putdata(self.jpgfile)
        return im2.show()
    

class Setting:
    def setMediaPath(self,directory) :
        self.directory = directory

    def getMediaPath(self, filename):
        self.filename = self.directory + '\\' + filename
        print(self.filename)
        return self.filename 

    def makePicture(self, path) :
        picture = Picture(path)
        return picture
        

set = Setting()
set.setMediaPath(r'C:\Users\renz\Desktop\jes-5.020-windows-java-included\mediasources-4ed')
set.getMediaPath('barbara.jpg')
pic=set.makePicture(set.filename)
pic.show()
