import pygame
class Plugboard:

    def __init__(self,pairs):
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            pos_A = self.left.find(pair[0])
            pos_B = self.left.find(pair[1])
            self.left = self.left[:pos_A]+self.left[pos_B]+self.left[pos_A+1:pos_B]+self.left[pos_A]+self.left[pos_B+1:]
            # self.right = self.right[:pos_B]+self.right[pos_A]+self.right[pos_B+1:]+self.right[pos_B]+self.right[pos_A+1:]
    def forward(self,signal):
            letter = self.right[signal]
            signal = self.left.find(letter)
            return signal
    
    def backward(self,signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal
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
                screen.blit(letter,text_box)
