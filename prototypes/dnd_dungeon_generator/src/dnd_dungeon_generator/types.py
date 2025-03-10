from dataclasses import dataclass


@dataclass(frozen=True)
class Location:
    id: str
    name: str


@dataclass(frozen=True)
class HistoryKey:
    locations: list[str]


@dataclass(frozen=True)
class History:
    id: str
    name: str


@dataclass(frozen=True)
class MonsterKey:
    locations: list[str]
    history: list[str]


@dataclass(frozen=True)
class Monster:
    id: str
    name: str
