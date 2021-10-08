import logging


class LogHandler(logging.Logger):

    def __init__(self,
                 name="root",
                 level="DEBUG",
                 file=None,
                 fmt=('%(asctime)s:%(filename)s:%(lineno)d:%(name)s:%(levelname)s:%(message)s')):
        super().__init__(name)

        # 设置级别
        self.setLevel(level)
        #设置格式
        fmt = logging.Formatter(fmt)

        if file:
            file_handler = logging.FileHandler(filename=file)
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
        else:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(level)
            stream_handler.setFormatter(fmt)
            self.addHandler(stream_handler)

if __name__ == '__main__':
    logger=LogHandler(file='test.log')
    logger.debug('hello')
