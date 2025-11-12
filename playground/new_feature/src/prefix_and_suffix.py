def remove_prefix_from_list(l1: list[str]) -> list[str]:
    return [s.removeprefix("pri_") for s in l1]


def remove_suffix_from_list(l1: list[str]) -> list[str]:
    return [s.removesuffix("_peko") for s in l1]


if __name__ == "__main__":
    print(
        remove_prefix_from_list(
            [
                "pri_pri_puri~",
                "pri_para",
                "yaru_pri_yo",
            ]
        )
    )

    print(
        remove_suffix_from_list(
            [
                "kon_peko",
                "peko_peko_peko_peko",
                "ahahahahaha_pekora_ha_kouun_usagi_tte_wake!",
            ]
        )
    )
