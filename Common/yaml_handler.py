import yaml

from Common.dir_path import config_yaml_path, chrome_driver_path


class YamlHandler():

    def __init__(self, file):
        self.file = file

    def get_yaml_data(self):
        """读取数据"""
        with open(self.file, 'r', encoding='utf-8') as f:
            yaml_data = yaml.load(f.read(), Loader=yaml.FullLoader)
        return yaml_data

    def write_yaml_data(self, result):
        """写入数据"""
        # 写入数据使用a+ a+:可读可写且不会覆盖数据
        with open(self.file, 'a+', encoding='utf-8') as f:
            # 如果写入的数据有中文 需要加上 allow_unicode=True
            yaml.dump(data=result, stream=f, allow_unicode=True)


if __name__ == '__main__':
    desired_caps = YamlHandler(config_yaml_path).get_yaml_data()
    desired_caps['chromedriverExecutable'] = chrome_driver_path
    print(desired_caps)
