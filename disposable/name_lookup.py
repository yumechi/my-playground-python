import argparse


def get_settings() -> argparse.Namespace:
    """
    Preprocess for arguments

    :return: argparse.Namespace
    """
    parser = argparse.ArgumentParser(description="対象ファイル")
    parser.add_argument("-f", "--file", required=True)

    return parser.parse_args()


def run(args: argparse.Namespace) -> None:
    """
    distinct script, ignore staff.
    Name include half or full space, so they are replaced and remap distinct name.

    input format
    ```
    name	kind
    name	kind
    name	kind
    ```
    :param args:
    :return:
    """
    filename = args.file
    with open(filename, "r") as f:
        lines = f.readlines()
    name_map = {}
    for line in lines:
        name, kind = line.split("\t")
        # ignore staff
        if "staff" in kind.lower():
            continue
        no_spaced_name = name.strip().replace(" ", "").replace("　", "")
        name_map[no_spaced_name] = name.strip()
    names = sorted(name_map.values())
    print("\n".join(names))


if __name__ == "__main__":
    run(get_settings())
