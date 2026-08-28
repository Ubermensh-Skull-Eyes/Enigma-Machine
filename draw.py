import pygame

def draw(enigma,screen,width,height,margins,gap,font,path):
   #components dimension
    w = ((width-(margins['left']+margins['right']))-gap*5)/6
    h = height-(margins["top"]+margins["bottom"])
   
   #drawing components
    y = margins["top"]
    x = margins["left"]
   
    for tables in [enigma.re,enigma.r3,enigma.r2,enigma.r1,enigma.pb,enigma.kb]:
        tables.draw(screen ,x,y,w,h,font)
        x+=w+gap
    x = margins["left"]
    for label in ["Keyboard","PlugBoard","Rotor1","Rotor2","Rotor3","Reflector"]:
        lab = font.render(label,False,'black')
        lab_box = lab.get_rect(midleft = (width-x-w,y-20))
        screen.blit(lab,lab_box)
        x+=w+gap
    # Storing x and y coordinates
    X = [width - margins["left"]-w/2]
    Y = []
    for i in range(1,5):# forward
        # print(i)
        X.append(width-margins["left"]-i*(gap+w)-w/4)
        X.append(width-margins["left"]-i*(gap+w)-w*3/4)
    X.append(margins["right"]+w*3/4)
    for i in range(0,5):# backward
        X.append(margins["right"]+i*(gap+w)+w/4)
        X.append(margins["right"]+i*(gap+w)+w*3/4)
    X.append(margins["right"]+5*(gap+w)+w*2/4)
    for i in path:
        Y.append(margins['top']+(i+1)*h/27)
    if len(Y)>0:
        Y.append(margins['top']+path[-1]*h/27)
    # print(len(path))
    # drawing paths
    print("X axis:-",X,"\n","Y axis:-",Y,"\n",f"Path is:-{path}")
    if len(Y)>1:
        for i in range(20):
            if i<10:
                colour = "#1e64ff"
            elif i>=10 and i<12:
                colour = "#a03cc8"
            else:
                colour = "#1eb450"
            pygame.draw.line(screen,colour,(X[i],Y[i]),(X[i+1],Y[i+1]),width=3)