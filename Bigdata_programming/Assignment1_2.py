#2. Couple
def pinkBg(p):
  for x in range(0,getWidth(p)):
    for y in range(0,getHeight(p)):
      px = getPixel(p,x,y)
      r = getRed(px)
      g =getGreen(px)  
      if(r>=100 and g>=100):
        setColor(px,pink)
  return p
  
def mirror(source,target,sx,sy,ex,ey):
  sourceX = 0
  for x in range(sx,ex) :
    for y in range(sy,ey) :
      targetPixel = getPixel(target,x,y)
      sourcePixel = getPixel(source,ex-sourceX,y)
      setColor(targetPixel, getColor(sourcePixel))
    sourceX = sourceX +1
def couple(f) :
  source = makePicture(f)
  target = makePicture(f)
  mirror(source,target,312,77,417,478)
  mirror(source,target,417,95,515,474)
  pinkBg(target)
  show(target)