from dnd_dungeon_generator.types import (
    Location,
    History,
    HistoryKey,
    Monster,
    MonsterKey,
)

locations = [
    Location(id="castle", name="Castle"),
    Location(id="outpost", name="Outpost"),
    Location(id="mine", name="Mine"),
    Location(id="temple", name="Temple"),
    Location(id="cave", name="Cave"),
]


history = {
    HistoryKey(locations=("castle", "outpost")): [
        History(id="active", name="Active"),
        History(id="abandoned", name="Abandoned"),
        History(id="ruined", name="Ruined"),
    ],
    HistoryKey(locations=("mine",)): [
        History(id="active", name="Active"),
        History(id="abandoned", name="Abandoned"),
        History(id="collapsed", name="Collapsed"),
        History(id="haunted", name="Haunted"),
        History(id="infested", name="Infested"),
    ],
    HistoryKey(locations=("cave",)): [
        History(id="normal", name="Normal"),
        History(id="haunted", name="Haunted"),
        History(id="infested", name="Infested"),
    ],
    HistoryKey(locations=("temple",)): [
        History(id="cult", name="Cult"),
        History(id="abandoned", name="Abandoned"),
        History(id="ruined", name="Ruined"),
    ],
}

monsters = {
    MonsterKey(locations=("castle", "outpost"), history=("active",)): [
        Monster(id="bandit", name="Bandit"),
        Monster(id="goblin", name="Goblin"),
        Monster(id="orc", name="Orc"),
    ],
    MonsterKey(
        locations=("castle", "outpost", "mine", "temple"),
        history=("abandoned", "ruined"),
    ): [
        Monster(id="goblin", name="Goblin"),
        Monster(id="orc", name="Orc"),
        Monster(id="skeleton", name="Skeleton"),
        Monster(id="zombie", name="Zombie"),
        Monster(id="ghost", name="Ghost"),
        Monster(id="specter", name="Specter"),
    ],
    MonsterKey(
        locations=("castle", "outpost", "mine", "cave"),
        history=("infested", "collapsed"),
    ): [
        Monster(id="giant_rat", name="Giant Rat"),
        Monster(id="giant_spider", name="Giant Spider"),
    ],
    MonsterKey(locations=("mine",), history=("active",)): [
        Monster(id="miner", name="Miner"),
    ],
    MonsterKey(locations=("mine", "cave"), history=("haunted", "normal")): [
        Monster(id="ghost", name="Ghost"),
        Monster(id="specter", name="Specter"),
    ],
    MonsterKey(locations=("temple",), history=("cult",)): [
        Monster(id="cultist", name="Cultist"),
        Monster(id="goblin", name="Goblin"),
    ],
}
