# Dungeon Generator

Generates random dungeons.

Scope is being kept pretty lean. We're not going to "render" the dungeon. I'm 
just going to print the final layout

## How Does It Work?

For the first version, let's just make the dungeons random. Our algorithm can be
summarised as:

1. Specify the dimensions (e.g. NxM cells).
2. (Randomly) Determine the number of rooms and the dimensions of the room.
3. Attempt to place the rooms on the map, one at a time, ensuring valid placement.
   If you find an room unplaceable, then restart the algorithm.
4. Generate corridors to connect the rooms.
5. Print to screen.
