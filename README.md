# Maze-generation
Maze generation using different [maze algorithms](https://en.wikipedia.org/wiki/Maze_generation_algorithm). Additionally, a simple recursive backtracking pathfinder was also implemented. 
Thus far it's only working with mazes that was genereted with recursive backtracking. The start point is always at the upper left corner and the end point is at the lower right corner.

Pygame was used to visualize the maze generation and the pathfinding process.

### List of maze algorithms progression
- [x] Recursive backtracking 
- [x] Prims 
- [x] Hunt and kill
- [x] Kruskal 
- [x] Binary tree 
- [x] Growing tree

### How to run
Download the packages in the requirements file:


    pip install -r requirements.txt


To start the screen run the following command:


    py main.py


When the screen appears with a 2D grid, press either button to start the maze generation. To generate a new maze simply
click either buttons again when the current generation has finished. The different buttons represent the different algorithms.


### Commands
You can also use commands to start the generation or exit the screen. Additionally there's a pathfinder


| Command | Description |
| ------- | ----------- |
| `p` | Run Prims algorithm |
| `r` | Run Recursive backtracking |
| `h` | Run Hunt and kill |
| `b` | Run Binary tree |
| `g` | Run Growing tree |
| `k` | Run Kruskal |
| `s` | Run recursive backtracking pathfinder (thus far only works if maze was generated with r) |
| `esc` | Exit |


### Recursive backtracking
![Maze generation visualization RB](assets/RB%20maze%20generation.gif)

### Prims 
![Maze generation visualization Prims](assets/prims%20%20generation.gif)

### Hunt and kill
![Maze generation visualization hunt and kill](assets/hak%20generation.gif)

### Binary tree
![Maze generation visualization binary tree](assets/BT%20generation.gif)

### Growing tree
![Maze generation visualization growing tree](assets/GT%20generation.gif)

### Kruskal
![Maze generation visualization kruskal](assets/kruskal%20generation.gif)

### Recursive backtracking pathfinder
![Maze pathfinder visualization RB](assets/RB%20pathfinder.gif)