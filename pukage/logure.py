
from loguru import logger
logger.info("hello world")
#输出不同的日志级别
logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条waring日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")
#输出到文件
logger.add("a.log", format="{time} {level} {message}", level="INFO")
#字符串格式化
logger.info("今天星期{}", "三")