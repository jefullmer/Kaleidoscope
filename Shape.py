import pygame, math
from pygame.locals import *

class Shapes(object):
    
    def __init__(self, surf):
        self.surf = surf
        INFO = pygame.display.Info()
        self.sWidth = INFO.current_w
        self.sHeight = INFO.current_h
        self.selected = 0
        self.isDone = False
        
    def drawSelected(self, select, mod, color):
        off = 5
        offset = mod * off
        cx = self.sWidth / 2
        cy = self.sHeight / 2                    
        if select == 0: #square
            p1 = [cx - off - offset, cy - off - offset] #top left
            p2 = [cx + off + offset, cy - off - offset] #top right
            p3 = [cx + off + offset, cy + off + offset] #bottom right
            p4 = [cx - off - offset, cy + off + offset] #bottom left
            
            p1 = self.rotatePoint(cx, cy, p1, mod)
            p2 = self.rotatePoint(cx, cy, p2 , mod)
            p3 = self.rotatePoint(cx, cy, p3 , mod)
            p4 = self.rotatePoint(cx, cy, p4 , mod)
            
            pygame.draw.line(self.surf, color, p1, p2, 2)
            pygame.draw.line(self.surf, color, p2, p3, 2)
            pygame.draw.line(self.surf, color, p3, p4, 2)
            pygame.draw.line(self.surf, color, p4, p1, 2)
        if select == 1: #triangle
            p1 = [cx, cy - off - offset] #top
            p2 = [cx + off + offset, cy + off + offset] #bottom right
            p3 = [cx - off - offset, cy + off + offset] # bottom left
            
            p1 = self.rotatePoint(cx, cy, p1, mod)
            p2 = self.rotatePoint(cx, cy, p2 , mod)
            p3 = self.rotatePoint(cx, cy, p3 , mod) 
            
            pygame.draw.line(self.surf, color, p1, p2, 2)
            pygame.draw.line(self.surf, color, p2, p3, 2)
            pygame.draw.line(self.surf, color, p3, p1, 2)            
        if select == 2: #square no rotate
            p1 = [cx - off - offset, cy - off - offset] #top left
            p2 = [cx + off + offset, cy - off - offset] #top right
            p3 = [cx + off + offset, cy + off + offset] #bottom right
            p4 = [cx - off - offset, cy + off + offset] #bottom left            
            
            pygame.draw.line(self.surf, color, p1, p2, 2)
            pygame.draw.line(self.surf, color, p2, p3, 2)
            pygame.draw.line(self.surf, color, p3, p4, 2)
            pygame.draw.line(self.surf, color, p4, p1, 2)            
        if select == 3: #triangle no rotate
            p1 = [cx, cy - off - offset] #top
            p2 = [cx + off + offset, cy + off + offset] #bottom right
            p3 = [cx - off - offset, cy + off + offset] # bottom left            
            
            pygame.draw.line(self.surf, color, p1, p2, 2)
            pygame.draw.line(self.surf, color, p2, p3, 2)
            pygame.draw.line(self.surf, color, p3, p1, 2)              
    
    def rotatePoint(self, cx, cy, point, mod):
        s = math.sin(mod)
        c = math.cos(mod)        
        point[0] -= cx
        point[1] -= cy
        xnew = point[0] * c - point[1] * s
        ynew = point[0] * s + point[1] * c
        point[0] = xnew + cx
        point[1] = ynew + cy
        return point