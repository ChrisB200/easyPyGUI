# easyPyGUI

**easyPyGUI** is a simple Python library for creating graphical user interfaces (GUIs) using the Pygame library.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).
2. Install the Pygame library:

   ```bash
   pip install pygame

3. Clone **easyPyGUI** from GitHub
   ```bash
   git clone https://github.com/ChrisB200/easyPyGUI.git

## Usage

To use **easyPyGUI** in your project, import the necessary classes:

   ```python
   from easyPyGUI import Root, UIElement, Menu
   ```

## Examples

Here's a basic example of how to create a simple GUI using easyPyGUI

   ```python
   # Import necessary classes
   from easyPyGUI import Root, UIElement, Menu

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
   ```
   
## Contibuting

If you'd like to contribute to **easyPyGUI**, feel free to submit a pull request or open an issue. Your contributions are welcome!

## License

Feel free to customize the examples, add more sections, or provide additional information based on the features and details of your easyPyGUI library.
