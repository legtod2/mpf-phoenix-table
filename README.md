# mpf-phoenix-table
Mission Pinball table of Williams Phoenix 

The following code consist primarily of yaml files for a Cobrapin board and OPP with Mission Pinball Framework Version .55
Two small python programs (Bonus.py to count down bonus, shutdown.py)

Version 1.0

To test.. 
Open a terminal session(1)
mpf both -X
Open a 2nd terminal seesion(2)
mpf monitor

On the playfield monitor you will see the virtual Williams table. On the bottom row you will see the Start button, coin button, shutdown (Bottom left)
On the bottom right side you will see the service buttton)

1) Start by adding coins
2) Start button and attract mode ends
3) Click one of the top 5 lane and notice score and music changes
4) Click any targets or drop targets
5) To sink ball and got to next bal click bottom middle switch (Next ball will start)
6) Repeat for ball 2 and 3
7) To see service menu items click on the service menu button (Bottom right side)
8) Use the service menu buttons to navigate on bottom right

This is the first time I have ever uploaded to github so I made a couple of mistakes.
After you unzip the contents, you will need to create directory called tests and move test_simple_game.py into that folder

Run full game unit test (This will cycle thru a full game extra ball, replay, initials for high score)

python3 -m unittest discover
