Mini Platformer
A simple 2D platformer game built with Python and Pygame.
You control a blue rectangle, jumping across platforms and avoiding moving red enemies. Reach the final platform of each level to progress. After completing all levels, the game gracefully exits with a music fade-out.

Features
Multiple levels with increasing difficulty

Moving red enemy obstacles that patrol a random platform per level

Background music that plays during gameplay and fades out at the end

Jump sound effect when you jump

Automatic restart to the level start if you fall

Clean exit – after finishing all levels, it runs exit.py

Installation (Mac only for now)
1. Install Python
You need Python 3.8 or higher.
Check if you have it:

bash
Copy
Edit
python3 --version
If not, download Python from the official website.

2. Install Pygame
bash
Copy
Edit
pip3 install pygame
3. Add Your Music & Sound Files
Background music:
Place your background music file at:

swift
Copy
Edit
/Users/some-user/Downloads/Evening Light.mp3
Jump sound:
Place your jump sound effect file at:

swift
Copy
Edit
/Users/noah-zipor/Downloads/Jump Sound Effect.mp3
(Or update the paths in the code to match your system.)

How to Run
Run the game with:

bash
Copy
Edit
python3 main.py
The game will open a 1200×600 window with scaled graphics.

How to Play
Move Left: Left Arrow key

Move Right: Right Arrow key

Jump: Up Arrow key

Gameplay Rules
Reach the last platform of the level, then move to the right edge to advance to the next level.

Avoid red enemies—if they touch you, you respawn at the level start.

If you fall off the platforms and touch the ground beyond the first platform, you respawn.

After the final level, the background music fades out and the game ends.

