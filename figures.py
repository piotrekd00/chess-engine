from dataclasses import dataclass, field


@dataclass
class Queen:
    id: int
    pos_x: int
    pos_y: int
    symbol: str = field(default='Q', repr=False)


@dataclass
class Pawn:
    pos_x: int
    pos_y: int
    symbol: str = field(default='P', repr=False)
