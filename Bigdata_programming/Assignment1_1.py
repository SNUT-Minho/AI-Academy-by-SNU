#1. Worhole
def makeGrey(f) :
  p = makePicture(f)
  for x in range(0,getWidth(p)) :
    for y in range(0,getHeight(p)) :
      px = getPixel(p,x,y)
      r = getRed(px)
      g = getGreen(px)
      b = getBlue(px)
      grey = (r+g+b)/3
      color = makeColor(grey,grey,grey)
      setColor(px,color)
  return p 
  
def worhol(f) :
  p = makeGrey(f)
  halfw = getWidth(p)/2
  halfh = getHeight(p)/2
  for x in range(0,getWidth(p)) :
    for y in range(0,getHeight(p)) :
      px = getPixel(p,x,y)
      r = getRed(px)
      g = getGreen(px)
      b = getBlue(px)
      if(x<halfw and y<halfh) :
        if(r>=100 and g>=100 and b>=100) :
          setColor(px,blue)
        else : 
          setColor(px,yellow)
      elif(x<halfw and y>=halfh) :
        if(r>=100 and g>=100 and b>=100) :
          setColor(px,green)
        else : 
          setColor(px,red)        
      elif(x>=halfw and y>=halfh) :
        if(r>=100 and g>=100 and b>=100) :
          setColor(px,yellow)
        else : 
          setColor(px,blue)         
        
      else :
        if(r>=100 and g>=100 and b>=100) :
          setColor(px,red)
        else : 
          setColor(px,green)   
  show(p) 
     




