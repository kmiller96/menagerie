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

## UPDATE: Lessons Learnt

As much as I want to continue with this, I already feel like it's pretty 
convoluted 😅 it's hard figuring out good design AND the language at the same
time. I'll have a go at this again at some point in the future.

However, it did teach me about how to implement traits for Rust. Traits have 
been really confusing to me up to this point; I'm so glad that I learnt them!
I actually really like the design pattern and now I understand it I'm sure I'll
want to use them everywhere.
