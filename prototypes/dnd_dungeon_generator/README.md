# D&D Dungeon Generator

Randomly generate a dungeon.

Taking inspiration from these projects:

- https://donjon.bin.sh/d20/dungeon/
- https://watabou.itch.io/one-page-dungeon

but I am wanting to make dungeons that feel more "real". If that's at all
possible. I'm sure those guys are much smarter than I am.

## Scope

For this prototype we'll scope it down to a "standard" dungeon with one of the
following themes:

1. **Bandit** - a dungeon full of bandits or humanoids.
2. **Haunted** - a haunted dungeon (e.g. zombies, ghoul).
3. **Inhabited** - a dungeon that's been occupied by a beast (e.g. wolves).

## Design

I'm thinking of making this a half-procedural, half-AI. That sounds weird and
buzzwordy but I'll explain it.

I want to have some base algorithm that generates the dungeon. Then, this
generated dungeon will then be passed into an LLM that helps to "polish" the
procedure and give it more of a complete feel to the dungeon.

It would be doubly-cool if we could use an LLM to create the options/procedures
in the algorithm! e.g. someone can explain a location and then an LLM will
condense that into a prompt.

For the MVP, I am thinking we can focus on the **procedural generation**. The
LLM piece can come later. Basically the random "seed" that an LLM will use to
help polish the output.

I am thinking the procedure will randomly pick from a list of options:

1. **Location** - is it an old dwarven mine? A hidden cultist temple? A cave?
2. **History** - is it recently left? Old, abandoned dungeon?
3. **Monster** - what monster will inhabit the dungeon?
4. **Layout** - how will the dungeon be laid out? Will it be established, or a
   new dungeon?

Of course there is a lot more we can do but let's limit the scope there!
