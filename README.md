# Mini Platformer

A simple 2D platformer game built with Python and Pygame.  
Control a blue rectangle, jump across platforms, avoid moving red enemies, and reach the last platform in each level to progress. After completing all levels, the game gracefully exits with a music fade-out.

---

## Features

- Multiple levels with increasing difficulty  
- Moving red enemy obstacles that patrol a random platform per level  
- Background music that plays during gameplay and fades out at the end  
- Jump sound effect when you jump  
- Automatic respawn at level start if you fall or collide with an enemy  
- Clean exit running `exit.py` after all levels completed  

---

## Installation (Mac Only)

### Prerequisites

- Python 3.8 or higher  
- [Pygame](https://www.pygame.org/)

### Setup

1. **Check Python version**

```bash
python3 --version
```
**Make sure you have pygame installed**
```bash
pip3 install pygame
```

# Add your media files

Place your background music and jump sound effect files at the following locations, or update the file paths in main.py accordingly:

Background music:
/Users/some-user/Downloads/Evening Light.mp3

Jump sound effect:
/Users/some-user/Downloads/Jump Sound Effect.mp3

# Running the Game
Run the game with:
```bash
python3 main.py
```
This opens a 1200×600 window with scaled graphics.

# Controls
Move Left: Left Arrow key

Move Right: Right Arrow key

Jump: Up Arrow key

# Gameplay
Reach the last platform on the current level, then move to its right edge to advance to the next level.

Avoid red enemies. Colliding with one respawns you at the level start.

Falling off platforms and touching the ground beyond the first platform also causes a respawn.

After completing the final level, the background music fades out and the game exits cleanly.


