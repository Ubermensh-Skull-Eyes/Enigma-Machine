from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
import string

k = Keyboard()
p = Plugboard(["AX","GM","OY"])
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ","Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE","W")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO","E")
reflex = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD","T")
enigma = Enigma(k,p,I,II,III,reflex)
enigma.set_rings((1,1,1))
enigma.set_key("KIA")

message = input("Enter a message to Encode:- ")
ciphered_text = ""
for i in message.upper():
    if i in string.punctuation or i.isspace():
        ciphered_text+=i
        continue
    ciphered_text += enigma.encipher(i)
print(ciphered_text)