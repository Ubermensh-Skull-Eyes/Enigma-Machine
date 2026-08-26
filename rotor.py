import pygame
class Rotor:
    def __init__(self,wiring,notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.notch = notch
    def forward(self,signal):
                letter = self.right[signal]
                signal = self.left.find(letter)
                return signal
        
    def backward(self,signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal
    def rotate(self , n=1,forward = True):
        if forward:
            for i in range(n):
                self.left = self.left[1:]+self.left[0]
                self.right = self.right[1:]+self.right[0]
        else:
             for i in range(n):
                self.left = self.left[25]+self.left[:25]
                self.right = self.right[25]+self.right[:25]
                
    def show(self):
         print(self.left)
         print(self.right)  
         print("")

    def rotate_to_letter(self,letter):
         n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
         self.rotate(n)

    def ring(self,n):
        # n = self.right.find(letters)
        self.rotate(n-1,False)
        n_notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(self.notch)
        self.notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(n_notch-n)%26]

    def draw(self,screen ,x,y,w,h,font):
                r = pygame.Rect(x,y,w,h)
                pygame.draw.rect(screen,'black',r,width=2,border_radius=2)
                for i in range(26):
                    letter = self.right
                    letter = font.render(letter[i],False,'black')
                    text_box = letter.get_rect(center = (x+3*w/4,y+(i+1)*h/27))
                    screen.blit(letter,text_box)
                for i in range(26):
                    letter = self.left
                    letter = font.render(letter[i],False,'black')
                    text_box = letter.get_rect(center = (x+w/4,y+(i+1)*h/27))
                    if i==0:
                        pygame.draw.rect(screen,'cyan',text_box,border_radius=5)
                    if self.left[i]==self.notch:
                         letter = font.render(self.notch,False,'white')
                         pygame.draw.rect(screen,'#333333',text_box,border_radius=5)
                    screen.blit(letter,text_box)
