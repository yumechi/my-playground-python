from typing import NamedTuple
from dataclasses import dataclass


@dataclass
class Idol:
    name: str
    profile: str
    brand: str = ""

    def __post_init__(self):
        if not self.brand:
            self.brand = f"{self.name}'s original corde"


class Live(NamedTuple):
    title: str
    member: list[Idol]

    def summary(self) -> str:
        return "title: {title}\nmember: \n  - {member_name}".format(
            title=self.title,
            member_name="\n  - ".join([m.name for m in self.member]),
        )


if __name__ == "__main__":
    raara = Idol(name="raara", profile="kashikoma Idol")
    mirei = Idol(name="mirei", profile="pripri Idol", brand="CandyAlamode")
    today_live = Live(title="Bold SUMMER ADVENTURE", member=[raara, mirei])
    print(today_live.summary())
    print(raara.brand)
    print(mirei.brand)
