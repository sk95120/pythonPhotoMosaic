#https://www.shiyanlou.com/courses/1041
$ sudo apt-get update
$ sudo pip install --upgrade pip # ���� pip
$ sudo pip install Pillow numpy # ʹ�� pip ��װ Pillow �� numpy

$ wget http://labfile.oss.aliyuncs.com/courses/1041/test-data.zip
$ unzip test-data.zip

def getImages(imageDir):
  """
  ����һ��Ŀ¼�����ظ�Ŀ¼�µ�ͼ�񣬲����б����ʽ����
  """
  files = os.listdir(imageDir)
  images = []
  for file in files:
    filePath = os.path.abspath(os.path.join(imageDir, file))
    try:
      # ��ʽ�����Ա�����ԴΣ��
      fp = open(filePath, "rb")
      im = Image.open(fp)
      images.append(im)
      # ǿ�ƴ��ļ��м���ͼ������
      im.load() 
      # �ر��ļ�
      fp.close() 
    except:
      # skip
      print("Invalid image: %s" % (filePath,))
  return images

def getAverageRGB(image):
  """
  ���㲢���ظ��� Image ���� (r,g,b) ��ʽ����ɫƽ��ֵ
  """
  # ��ͼ��ת���� numpy �е����� (��ά����)
  im = np.array(image)
  # ��ȡ���, �߶�, ���
  w,h,d = im.shape
  # ����ƽ��ֵ
  return tuple(np.average(im.reshape(w*h, d), axis=0))

def getAverageRGB(image):
  """
  ���㲢���ظ��� Image ���� (r,g,b) ��ʽ����ɫƽ��ֵ
  """
  # ��ͼ��ת���� numpy �е����� (��ά����)
  im = np.array(image)
  # ��ȡ���, �߶�, ���
  w,h,d = im.shape
  # ����ƽ��ֵ
  return tuple(np.average(im.reshape(w*h, d), axis=0))

def createImageGrid(images, dims):
  """
  ���������С��С��ͼ���б�, ������ͼ����ɵ�����
  """
  m, n = dims

  # ������
  assert m*n == len(images)

  # ��ȡͼ����, �߶ȵ����ֵ
  # ע��: ������ÿ��С��ͼ��Ĵ�С������ͬ��
  width = max([img.size[0] for img in images])
  height = max([img.size[1] for img in images])

  # �������ͼ��
  grid_img = Image.new('RGB', (n*width, m*height))

  # ճ��ͼ��
  for index in range(len(images)):
    row = int(index/n)
    col = index - n*row
    grid_img.paste(images[index], (col*width, row*height))

  return grid_img

def createImageGrid(images, dims):
  """
  ���������С��С��ͼ���б�, ������ͼ����ɵ�����
  """
  m, n = dims

  # ������
  assert m*n == len(images)

  # ��ȡͼ����, �߶ȵ����ֵ
  # ע��: ������ÿ��С��ͼ��Ĵ�С������ͬ��
  width = max([img.size[0] for img in images])
  height = max([img.size[1] for img in images])

  # �������ͼ��
  grid_img = Image.new('RGB', (n*width, m*height))

  # ճ��ͼ��
  for index in range(len(images)):
    row = int(index/n)
    col = index - n*row
    grid_img.paste(images[index], (col*width, row*height))

  return grid_img

def createImageGrid(images, dims):
  """
  ���������С��С��ͼ���б�, ������ͼ����ɵ�����
  """
  m, n = dims

  # ������
  assert m*n == len(images)

  # ��ȡͼ����, �߶ȵ����ֵ
  # ע��: ������ÿ��С��ͼ��Ĵ�С������ͬ��
  width = max([img.size[0] for img in images])
  height = max([img.size[1] for img in images])

  # �������ͼ��
  grid_img = Image.new('RGB', (n*width, m*height))

  # ճ��ͼ��
  for index in range(len(images)):
    row = int(index/n)
    col = index - n*row
    grid_img.paste(images[index], (col*width, row*height))

  return grid_img

def createImageGrid(images, dims):
  """
  ���������С��С��ͼ���б�, ������ͼ����ɵ�����
  """
  m, n = dims

  # ������
  assert m*n == len(images)

  # ��ȡͼ����, �߶ȵ����ֵ
  # ע��: ������ÿ��С��ͼ��Ĵ�С������ͬ��
  width = max([img.size[0] for img in images])
  height = max([img.size[1] for img in images])

  # �������ͼ��
  grid_img = Image.new('RGB', (n*width, m*height))

  # ճ��ͼ��
  for index in range(len(images)):
    row = int(index/n)
    col = index - n*row
    grid_img.paste(images[index], (col*width, row*height))

  return grid_img

#all-code behand above

def createImageGrid(images, dims):
  """
  ���������С��С��ͼ���б�, ������ͼ����ɵ�����
  """
  m, n = dims

  # ������
  assert m*n == len(images)

  # ��ȡͼ����, �߶ȵ����ֵ
  # ע��: ������ÿ��С��ͼ��Ĵ�С������ͬ��
  width = max([img.size[0] for img in images])
  height = max([img.size[1] for img in images])

  # �������ͼ��
  grid_img = Image.new('RGB', (n*width, m*height))

  # ճ��ͼ��
  for index in range(len(images)):
    row = int(index/n)
    col = index - n*row
    grid_img.paste(images[index], (col*width, row*height))

  return grid_img

#test-data ����
def createImageGrid(images, dims):
  """
  ���������С��С��ͼ���б�, ������ͼ����ɵ�����
  """
  m, n = dims

  # ������
  assert m*n == len(images)

  # ��ȡͼ����, �߶ȵ����ֵ
  # ע��: ������ÿ��С��ͼ��Ĵ�С������ͬ��
  width = max([img.size[0] for img in images])
  height = max([img.size[1] for img in images])

  # �������ͼ��
  grid_img = Image.new('RGB', (n*width, m*height))

  # ճ��ͼ��
  for index in range(len(images)):
    row = int(index/n)
    col = index - n*row
    grid_img.paste(images[index], (col*width, row*height))

  return grid_img

$ wget http://labfile.oss.aliyuncs.com/courses/1041/photomosaic.py