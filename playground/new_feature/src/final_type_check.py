from typing import Final

if __name__ == "__main__":
    LIVE_TITLE: Final[str] = "Last Live ! Goodbye, Forever !"
    # 再代入すると mypy に引っかかる（PyCharm上もエラー表示になる）
    # LIVE_TITLE = "FUKKATSU SHIMASHITA."
    print(LIVE_TITLE)
