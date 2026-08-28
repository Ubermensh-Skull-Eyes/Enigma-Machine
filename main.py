import pygame
from sys import exit
from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw
import string

pygame.init()
Width = 1400
Height = 800
Margins = {"top":200,"bottom":50,"right":100,"left":100}
Gap = 100
SCREEN = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Enigma Simulation")
text = pygame.font.SysFont("TimesNewRoman",size=25,bold=True)
text1 = pygame.font.SysFont("FreeMono",size=25,bold=True)
INPUT = ""
OUTPUT = ""
PATH = []

k = Keyboard()
p = Plugboard(["AX","GM","OY"])
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ","Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE","E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO","V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB","Z")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK","J")
VI = Rotor("JPGVOUMFYQBENHZRDKASXLICTW","G")
VII = Rotor("NZJHGRCXMYSWBOUFAIVLPEKQDT","Y")
VIII = Rotor("FKQHTLXOCBJSPDZRAMEWNIUYGV","U")
reflex = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD","N")
enigma = Enigma(k,p,I,II,III,reflex)
enigma.set_notch((1,1,1))
enigma.set_key("AAA")
animating = True

"""message = input("Enter a message to Encode:- ")
ciphered_text = ""
for i in message.upper():
    if i in string.punctuation or i.isspace():
        ciphered_text+=i
        continue
    ciphered_text += enigma.encipher(i)
print(ciphered_text)"""
while animating:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            key = event.unicode
            if key in "abcdefghijklmnopqrstuvwxyz" or "abcdefghijklmnopqrstuvwxyz".upper() and not key.isspace() and key not in string.punctuation:
                letter = key.upper()
                INPUT+=letter
                PATH,cipher = enigma.encipher(letter)
                print(PATH)
                OUTPUT+=cipher
                print(len(PATH))
            elif key in string.punctuation or key.isspace():
                INPUT+= key
                OUTPUT+= key
    SCREEN.fill('white')
    draw(enigma,SCREEN,Width,Height,Margins,Gap,text,PATH)
    inp = text1.render(INPUT,False,'red')
    inp_box = inp.get_rect(center = (Width/2,Margins["top"]/6))
    SCREEN.blit(inp,inp_box)

    out = text1.render(OUTPUT,False,'blue')
    out_box = out.get_rect(center = (Width/2,3*Margins["top"]/6))
    SCREEN.blit(out,out_box)
    pygame.display.update()