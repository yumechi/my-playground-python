def replace_string(s1: str) -> str:
    return "".replace("", s1, 2)


if __name__ == "__main__":
    print(replace_string(""))
    # Python 3.8 returns "", but 3.9 return "a~"
    print(replace_string("a~"))
