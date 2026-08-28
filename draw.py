import pygame

def draw(enigma,screen,w,h,margins,gap,font):
   y = margins["top"]
   x = margins["left"]
   w = ((w-(margins['left']+margins['right']))-gap*5)/6
   h = h-(margins["top"]+margins["bottom"])
   for tables in [enigma.re,enigma.r3,enigma.r2,enigma.r1,enigma.pb,enigma.kb]:
      tables.draw(screen ,x,y,w,h,font)
      x+=w+gap