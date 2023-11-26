import pygame
from pygame.constants import *

def isPercentageOrDecimal(value):
    if type(value) == float:
        return "decimal"
    elif type(value) == str:
        return "percentage"
    elif value >= 1:
        return "integer"
    else:
        return "invalid"
    
""" def decimal(self, number, parameter, isPercentage=False):
    if isPercentage == True:
        decimal = int(number.split("%")[0]) / 100
    else:
        decimal = number
        
    if parameter == "width":
        return self.parent.width * (decimal)
    elif parameter == "height":
        return self.parent.height * (decimal)
    elif parameter == "x":
        return self.parent.x * (decimal)
    elif parameter == "y":
        return self.parent.y * (decimal) """
    
class Root:
    def __init__(self, window, x=0, y=0, width=1920, height=1080):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window
        self.children = []
        
    def update(self, window):
        self.window = window
        self.width = self.window.get_width()
        self.height = self.window.get_height()
        for child in self.children:
            child.update()

    def render(self, surf):
        for child in self.children:
            child.render(surf)

    def add_children(self, *args):
        for element in args:
            element.parent = self
            self.children.append(element)

class UIElement:
    def __init__(self, x, y, width, height, parent, style={}, hoverStyle={}, activeStyle={}, action=None):
        self.local_x = x
        self.local_y = y
        self.width = width
        self.height = height
        self.children = []
        self.defaultStyle = style
        self.hoverStyle = hoverStyle
        self.activeStyle = activeStyle
        self.action = action
        self.hover = False
        self.active = False
        self.offset = {"x": 0, "y": 0, "width": 0, "height": 0}
        self.image = style.get("image", None)
        self.text = style.get("text", "")
        self.font = style.get("font", None)
        self.fontSize = style.get("font_size", 12)
        self.colour = style.get("colour", (0, 0, 0))
        self.background = style.get("background", (255, 255, 255))
        self.opacity = style.get("opacity", 255)
        parent.add_children(self)
        self.parent = parent
    
    @property
    def x(self):
        return self.local_x + + self.offset["x"] + (self.parent.x if self.parent else 0)
    
    @property
    def y(self):
        return self.local_y + + self.offset["y"] + (self.parent.y if self.parent else 0)

    @property
    def pos(self):
        return (self.x, self.y)

    @property
    def size(self):
        return (self.width, self.height)

    def render(self, surf):
        # Creates the text
        font = pygame.font.Font(None, self.fontSize)
        textSurface = font.render(self.text, True, self.colour)

        # Creates a surface
        uiElement = pygame.Surface(self.size)
        uiElement.fill(self.background)
        uiElement.blit(textSurface, (self.width // 2 - (textSurface.get_width() // 2), self.height // 2 - (textSurface.get_height() // 2)))
        uiElement.set_alpha(self.opacity)
        surf.blit(uiElement, self.pos)

    def follow(self, entity):
        self.local_x = entity[0] - (self.width // 2)
        self.local_y = entity[1] - (self.height // 2)

    def set_pos(self, x, y):
        self.local_x = x - (self.width // 2)
        self.local_y = y - (self.height // 2)
        
    def add_children(self, *args):
        for element in args:
            element.parent = self
            self.children.append(element)
            
    def change_style(self, event):
        if event == "hover":
            style = self.hoverStyle
        elif event == "active":
            style = self.activeStyle
        elif event == "default":
            style = self.defaultStyle
            
        self.image = style.get("image", self.image)
        self.text = style.get("text", self.text)
        self.font = style.get("font", self.font)
        self.fontSize = style.get("font_size", self.fontSize)
        self.colour = style.get("colour", self.colour)
        self.background = style.get("background", self.background)
        self.opacity = style.get("opacity", self.opacity)
            
    def handle_event(self, event):
        if self.action != None:
            if self.hover == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.active = True
                    self.change_style("active")
                if event.type == pygame.MOUSEBUTTONUP:
                    self.action()
                    self.active = False
            
                if event.type == pygame.JOYBUTTONDOWN:
                    self.active = True
                    self.change_style("active")
                if event.type == pygame.JOYBUTTONUP:
                    self.action()
                    self.active = False
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    
    def update(self):
        if self.action != None:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
                if self.active != True:
                    self.hover = True
                    self.change_style("hover")
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                self.hover = False
                
            if self.active != True and self.hover != True:
                self.change_style("default")
            
            
class Menu(UIElement):
    def __init__(self, x, y, width, height, parent=None, style={}):
        super().__init__(x, y, width, height, parent, style)
        self.children = []
        self.currentIndex = 0

    def render(self, surf):
        super().render(surf)
        for element in self.children:
            element.render(surf)
            
    def update(self):
        super().update()
        for element in self.children:
            element.update()

    def handle_event(self, event):  
        for element in self.children:
            element.handle_event(event)
        