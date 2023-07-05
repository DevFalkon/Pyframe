# Pyframe
 
## _How to create a new Pyframe project_

> ### Creating a new project directory
```
mkdir <project_name>
cd <project_name>
```

> ### Adding a python virtual environment
```
python -m venv env
```

> ### Adding Pyframe to the project

> Using git
```
git clone https://github.com/DevFalkon/Pyframe/
```

> Or manually place the Pyframe folder into the project folder

> ### Example Code

```
import Pyframe
import pygame as pg


app = Pyframe.GuiWindow()
screen = app.screen
FPS = 100
clock = pg.time.Clock()

while 1:
    app.win_update()

    for event in pg.event.get():
        pass

    # FPS = 100
    clock.tick(FPS)
```
