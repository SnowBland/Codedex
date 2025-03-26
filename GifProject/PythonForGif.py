import imageio.v3 as iio

filenames = ['team-pic1.png','team-pic2.png']
images=[]

for filename in filenames:
    images.append(iio.imread(filename))

# team.gif new gif file name
# images 包含图像数据的列表
# duration 每张图片显示多长时间
# loop 循环多少次
# 方法生成新的gif文件
iio.imwrite('team.gif',images,duration = 500,loop=0)
