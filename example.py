# Import necessary classes
from easyPyGUI import Root, UIElement, Menu
import pygame

# Initialize Pygame
pygame.init()

# Create Pygame window
window = pygame.display.set_mode((800, 600))

# Create the root element
root = Root(window)

# Create a UI element
button = UIElement(x=50, y=50, width=100, height=30, parent=root, style={"text": "Click me!"})

# Create a menu
menu = Menu(x=200, y=50, width=150, height=200, parent=root, style={"background": (200, 200, 200)})

# Add elements to the menu
menu.add_children(
   UIElement(x=0, y=0, width=150, height=50, parent=menu, style={"text": "Option 1"}),
   UIElement(x=0, y=50, width=150, height=50, parent=menu, style={"text": "Option 2"}),
   UIElement(x=0, y=100, width=150, height=50, parent=menu, style={"text": "Option 3"})
)

# Main loop
running = True
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
            running = False
      # Handle events for root and its children
      root.handle_event(event)

   # Update and render root and its children
   root.update(window)
   root.render(window)

   pygame.display.flip()

pygame.quit()