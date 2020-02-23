from removebg import RemoveBg
import os
from PIL import Image

rmbg = RemoveBg("RKxxxxxxx","error.log")   #输入获取得API
path = '%s/photoss'%os.getcwd()   #图片放到同级文件夹photos中
for pic in os.listdir(path):
    rmbg.remove_background_from_img_file("%s\%s"%(path,pic))

rmbg = RemoveBg("RKxxxxx","error.log")   #输入获取得API
rmbg.remove_background_from_img_file(r"C:\Jupyter\baby.n.png")