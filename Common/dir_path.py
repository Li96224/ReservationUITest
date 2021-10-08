import os
import time


#获取当前时间
ytd_time=time.strftime('%y-%m-%d')


#项目顶层目录
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]


#chromedriver路径
chrome_driver_path = os.path.join(project_path, "chromedriver.exe")

#日志路径
log_path=os.path.join(project_path,'Outputs','log','test_log.log')

#截图文件路径
screenshot_path=os.path.join(project_path,"Outputs","img")


#config.yaml 路径
config_yaml_path=os.path.join(project_path,"Config","config.yaml")
# print(config_yaml_path)


if __name__ == '__main__':
    print(log_path)