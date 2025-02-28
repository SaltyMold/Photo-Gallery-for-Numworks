def nw():
    lett="ABCDEFGHIJKLMNOP"
    img=gimp.image_list()[0]
    pdb.gimp_image_scale(img, 320, 240)
    drw = pdb.gimp_image_active_drawable(img)
    if not(pdb.gimp_drawable_is_indexed(drw)):
      pdb.gimp_convert_indexed(img, 0, 0, 16, 0, 1, 0)
    im=""
    pal=[]
    c=0
    for i in range(320*240):
      v=list(pdb.gimp_image_pick_color(img,drw,i%320,i//320,1,0,0))[:-1]
      if v not in pal: pal.append(v)
      cour = pal.index(v)  
      if i==0 : prec = cour      
      if prec != cour and i>0:
        im+=lett[prec]
        if c>1: im+=str(c)
        c=1
        prec = cour
      else:
        c+=1
    print "pal="+str(pal)    
    print "im=\""+im+"\""
nw()