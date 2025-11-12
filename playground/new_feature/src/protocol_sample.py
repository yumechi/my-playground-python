from typing import Protocol, runtime_checkable


@runtime_checkable
class Idol(Protocol):
    def gobi(self) -> str:
        ...


class Mirei(Idol):
    def gobi(self):
        return "pri"


class Gaaruru(Idol):
    def gobi(self):
        return "pri"


if __name__ == "__main__":
    mirei = Mirei()
    gaaruru = Gaaruru()
    print(f"{issubclass(mirei.__class__, Idol)=} {mirei.gobi()=}")
    print(f"{issubclass(gaaruru.__class__, Idol)=} {gaaruru.gobi()=}")
