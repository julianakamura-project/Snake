# 🐍 Classic Snake Game — Python OOP Project

A classic **Snake game** developed in Python using the `turtle` module as part of my studies in **Object-Oriented Programming (OOP)**.

In addition to practicing OOP concepts, this project introduces **file handling**, allowing the game to save and retrieve high scores between sessions.

---

## 🎯 About the Project

The goal of this project is to recreate the classic Snake game while applying Object-Oriented Programming concepts to structure the game into separate classes and objects.

The project also introduces persistent data storage through file handling. The player's high score is saved to a file and loaded when the game starts, allowing the score to remain available after closing the program.

This project is part of my ongoing Python and OOP studies.

---

## 🎮 Gameplay

The player controls a snake that moves continuously around the game board.

The objective is to:

1. Move the snake around the board.
2. Eat food to increase its length.
3. Earn points for each food item collected.
4. Avoid colliding with the walls.
5. Avoid colliding with the snake's own body.
6. Achieve the highest score possible.

The high score is saved to a file so that it can be preserved between game sessions.

---

## 🧠 Concepts Practiced

This project provides an opportunity to practice:

### Object-Oriented Programming

- Classes and Objects
- Constructors (`__init__`)
- Instance Attributes
- Instance Methods
- Object Interaction
- Encapsulation
- Modular Programming
- Separation of Responsibilities

### Python

- Lists
- Loops
- Conditional Statements
- Functions
- Modules
- Tuples
- Event Handling
- Collision Detection

### File Handling

- Opening files
- Reading from files
- Writing to files
- File modes
- Managing persistent data
- Handling stored high scores

---

## 💾 High Score System

Unlike a score that only exists while the game is running, this project stores the high score in a file.

The basic flow is:

```text
                 Game starts
                     │
                     ▼
             Read high score
                from file
                     │
                     ▼
              Start the game
                     │
                     ▼
              Player earns
                  points
                     │
                     ▼
          Is current score higher
             than high score?
                /       \
              Yes        No
               │          │
               ▼          │
          Update high     │
             score        │
               │          │
               └────┬─────┘
                    ▼
             Write high score
                 to file
```

This allows the high score to persist even after the program is closed.

For example:

```text
First session:
Score: 15
High Score: 15

Game closed

Second session:
Score: 0
High Score: 15
```

If the player later achieves a score of `20`, the stored high score will be updated.

---

## 🏗️ Planned Classes

The game will be divided into several classes, each responsible for a specific part of the application.

### 🐍 Snake

Responsible for:

- Creating the snake
- Managing the snake's body segments
- Moving the snake
- Changing direction
- Detecting the snake's head position
- Resetting the snake after a collision

### 🍎 Food

Responsible for:

- Creating the food
- Placing food at random positions
- Moving the food to a new position

### 🧮 Scoreboard

Responsible for:

- Displaying the current score
- Displaying the high score
- Updating the score
- Comparing the current score with the high score
- Reading the stored high score
- Saving a new high score

### 🎮 Game

The main game logic will coordinate the different objects and handle:

- Game state
- Collision detection
- Game-over conditions
- User input
- Game updates

The final class structure may change as the project develops.

---

## 🗂️ Project Structure

The project is expected to follow a structure similar to:

```text
Snake-Game/
│
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
├── data.txt
│
└── README.md
```

The `data.txt` file is used to store the persistent high score.

The structure may change as the project evolves.

---

## 🛠️ Technologies

- **Python**
- **Object-Oriented Programming**
- **Turtle Graphics**
- **File Handling**
- **PyCharm**
- **Git**
- **GitHub**

---

## 🎮 Controls

| Key | Action |
|---|---|
| `↑` | Move Up |
| `↓` | Move Down |
| `←` | Move Left |
| `→` | Move Right |

The snake cannot immediately reverse direction into itself.

For example:

```text
Moving Right → cannot immediately move Left
Moving Up    → cannot immediately move Down
```

---

## 📈 Development Progress

- [x] Set up the game window
- [x] Create the snake
- [x] Create the snake's segments
- [x] Implement snake movement
- [x] Implement directional controls
- [x] Create the food
- [x] Detect food collisions
- [x] Increase snake length
- [x] Create the scoreboard
- [x] Implement the current score
- [x] Implement wall collision
- [x] Implement self-collision
- [x] Implement game-over conditions
- [x] Create the high score file
- [x] Read the high score from the file
- [x] Write new high scores to the file

---

## 🧩 OOP Architecture

The game is designed around several objects that interact with one another:

```text
                         ┌──────────────┐
                         │     Game     │
                         └──────┬───────┘
                                │
                 ┌──────────────┼──────────────┐
                 │              │              │
                 ▼              ▼              ▼
           ┌──────────┐    ┌─────────┐   ┌────────────┐
           │  Snake   │    │  Food   │   │ Scoreboard │
           └──────────┘    └─────────┘   └──────┬─────┘
                                                │
                                                ▼
                                         ┌────────────┐
                                         │ High Score │
                                         │    File    │
                                         └────────────┘
```

Each class has a specific responsibility while working together to create the complete game.

---

## 💡 File Handling

One of the main learning objectives of this project is understanding how Python can interact with external files.

The game uses a file to persist the player's high score.

### Reading

When the game starts, the program reads the previously stored high score.

```python
with open("data.txt", mode="r") as file:
    self.highscore = int(file.read())
```

### Writing

When the player achieves a new high score, the program updates the file.

```python
with open("data.txt", mode="w") as file:
    file.write(f"{self.highscore}")
```

These examples demonstrate the basic principles of reading and writing persistent data in Python.

---

## 📚 Learning Objectives

Through this project, I aim to improve my understanding of:

- Designing classes for different game components
- Making objects interact with one another
- Separating responsibilities between classes
- Managing object state
- Working with lists of objects
- Handling user input
- Detecting collisions
- Organizing a multi-file Python project
- Reading data from files
- Writing data to files
- Persisting information between program executions
- Combining OOP with file handling

---

## 📖 Part of My OOP Studies

This project is part of my ongoing study of **Object-Oriented Programming with Python**.

It builds upon concepts practiced in previous projects while introducing **file handling and persistent data**.

The goal is not only to create a playable game, but also to practice designing a program using classes and objects while learning how applications can store and retrieve information outside of their runtime.

---

## 👩‍💻 Author

**Julia Nakamura**

This project is part of my programming studies and GitHub portfolio.

---

## 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.
