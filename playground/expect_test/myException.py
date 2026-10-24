# ruff: noqa: LOG015, G201  (ログ出力の書き方を試すサンプル)
import logging


# Exceptionを継承すれば簡単に自作の例外が作れる
# Customizeはよくしらないけど。。。。
# Exceptionにあるものを調べればいいかも？
class YumechiException(Exception):
    pass


def run():
    try:
        raise YumechiException
    except Exception:
        logging.error("自作の例外", exc_info=True)


if __name__ == "__main__":
    run()
