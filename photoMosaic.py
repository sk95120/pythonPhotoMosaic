#https://www.shiyanlou.com/courses/1041
$ sudo apt-get update
$ sudo pip install --upgrade pip # 更新 pip
$ sudo pip install Pillow numpy # 使用 pip 安装 Pillow 和 numpy

$ wget http://labfile.oss.aliyuncs.com/courses/1041/test-data.zip
$ unzip test-data.zip

def getImages(imageDir):
  """
  给定一个目录，加载该目录下的图像，并以列表的形式返回
  """
  files = os.listdir(imageDir)
  images = []
  for file in files:
    filePath = os.path.abspath(os.path.join(imageDir, file))
    try:
      # 显式加载以避免资源危机
      fp = open(filePath, "rb")
      im = Image.open(fp)
      images.append(im)
      # 强制从文件中加载图像数据
      im.load() 
      # 关闭文件
      fp.close() 
    except:
      # skip
      print("Invalid image: %s" % (filePath,))
  return images

def getAverageRGB(image):
  """
  计算并返回给定 Image 对象 (r,g,b) 形式的颜色平均值
  """
  # 将图像转换成 numpy 中的数组 (三维数组)
  im = np.array(image)
  # 获取宽度, 高度, 深度
  w,h,d = im.shape
  # 计算平均值
  return tuple(np.average(im.reshape(w*h, d), axis=0))

def getAverageRGB(image):
  """
  计算并返回给定 Image 对象 (r,g,b) 形式的颜色平均值
  """
  # 将图像转换成 numpy 中的数组 (三维数组)
  im = np.array(image)
  # 获取宽度, 高度, 深度
  w,h,d = im.shape
  # 计算平均值
  return tuple(np.average(im.reshape(w*h, d), axis=0))

def createImageGrid(images, dims):
  """
  给定网格大小和小块图像列表, 创建由图像组成的网格
  """
  m, n = dims

  # 检查参数
  assert m*n == len(images)

  # 获取图像宽度, 高度的最大值
  # 注意: 并不是每个小块图像的大小都是相同的
  width = max([img.size[0] for img in images])
  height = max([img.size[1] for img in images])

  # 创建输出图像
  grid_img = Image.new('RGB', (n*width, m*height))

  # 粘贴图像
  for index in range(len(images)):
    row = int(index/n)
    col = index - n*row
    grid_img.paste(images[index], (col*width, row*height))

  return grid_img

def createImageGrid(images, dims):
  """
  给定网格大小和小块图像列表, 创建由图像组成的网格
  """
  m, n = dims

  # 检查参数
  assert m*n == len(images)

  # 获取图像宽度, 高度的最大值
  # 注意: 并不是每个小块图像的大小都是相同的
  width = max([img.size[0] for img in images])
  height = max([img.size[1] for img in images])

  # 创建输出图像
  grid_img = Image.new('RGB', (n*width, m*height))

  # 粘贴图像
  for index in range(len(images)):
    row = int(index/n)
    col = index - n*row
    grid_img.paste(images[index], (col*width, row*height))

  return grid_img

def createImageGrid(images, dims):
  """
  给定网格大小和小块图像列表, 创建由图像组成的网格
  """
  m, n = dims

  # 检查参数
  assert m*n == len(images)

  # 获取图像宽度, 高度的最大值
  # 注意: 并不是每个小块图像的大小都是相同的
  width = max([img.size[0] for img in images])
  height = max([img.size[1] for img in images])

  # 创建输出图像
  grid_img = Image.new('RGB', (n*width, m*height))

  # 粘贴图像
  for index in range(len(images)):
    row = int(index/n)
    col = index - n*row
    grid_img.paste(images[index], (col*width, row*height))

  return grid_img

def createImageGrid(images, dims):
  """
  给定网格大小和小块图像列表, 创建由图像组成的网格
  """
  m, n = dims

  # 检查参数
  assert m*n == len(images)

  # 获取图像宽度, 高度的最大值
  # 注意: 并不是每个小块图像的大小都是相同的
  width = max([img.size[0] for img in images])
  height = max([img.size[1] for img in images])

  # 创建输出图像
  grid_img = Image.new('RGB', (n*width, m*height))

  # 粘贴图像
  for index in range(len(images)):
    row = int(index/n)
    col = index - n*row
    grid_img.paste(images[index], (col*width, row*height))

  return grid_img

#all-code behand above

def createImageGrid(images, dims):
  """
  给定网格大小和小块图像列表, 创建由图像组成的网格
  """
  m, n = dims

  # 检查参数
  assert m*n == len(images)

  # 获取图像宽度, 高度的最大值
  # 注意: 并不是每个小块图像的大小都是相同的
  width = max([img.size[0] for img in images])
  height = max([img.size[1] for img in images])

  # 创建输出图像
  grid_img = Image.new('RGB', (n*width, m*height))

  # 粘贴图像
  for index in range(len(images)):
    row = int(index/n)
    col = index - n*row
    grid_img.paste(images[index], (col*width, row*height))

  return grid_img

#test-data 运行
def createImageGrid(images, dims):
  """
  给定网格大小和小块图像列表, 创建由图像组成的网格
  """
  m, n = dims

  # 检查参数
  assert m*n == len(images)

  # 获取图像宽度, 高度的最大值
  # 注意: 并不是每个小块图像的大小都是相同的
  width = max([img.size[0] for img in images])
  height = max([img.size[1] for img in images])

  # 创建输出图像
  grid_img = Image.new('RGB', (n*width, m*height))

  # 粘贴图像
  for index in range(len(images)):
    row = int(index/n)
    col = index - n*row
    grid_img.paste(images[index], (col*width, row*height))

  return grid_img

$ wget http://labfile.oss.aliyuncs.com/courses/1041/photomosaic.py