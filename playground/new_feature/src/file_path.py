if __name__ == "__main__":
    import os

    current_file_path: str = f"{os.getcwd()}/src/file_path.py"
    print(__file__)
    print(current_file_path)
    assert __file__ == current_file_path
