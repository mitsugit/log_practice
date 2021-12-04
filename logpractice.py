## ファイル出力とコンソール出力の両方のログを出力できるようにする。
## ファイル出力については、更にエラーのみの出力ファイルに分ける。

from logging import ERROR, Formatter, getLogger, StreamHandler,FileHandler,DEBUG
## ログの出力形式を設定
formatter=Formatter('[%(levelname)s] %(asctime)s - %(message)s(%(filename)s)')
logger = getLogger(__name__)

## コンソール表示用
stream_handler = StreamHandler()
## テキスト出力用
file_handler = FileHandler('log.txt')
error_handler = FileHandler('log_error.txt')

## レベルと形式の設定
stream_handler.setLevel(ERROR)
stream_handler.setFormatter(formatter)

file_handler.setLevel(DEBUG)
file_handler.setFormatter(formatter)

error_handler.setLevel(ERROR)
error_handler.setFormatter(formatter)

logger.setLevel(DEBUG)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.addHandler(error_handler)

logger.debug('ロギング 開始')

def test_func(num):
    return num + 3
try:
    test_func("ss")
except Exception as e:
    logger.exception("test_func関数にてエラー発生。エラー内容は下記のとおり。")

logger.debug('ロギング 終了')