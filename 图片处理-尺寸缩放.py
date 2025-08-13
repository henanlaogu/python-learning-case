from PIL import Image

# 打开图片，这里假设图片在当前目录下，根据实际情况修改文件名
image = Image.open("original.png")

# 获取原始图片的宽度和高度
width, height = image.size

# 计算缩放后的尺寸
new_width = width // 2
new_height = height // 2

# 进行缩放操作
resized_image = image.resize((new_width, new_height))

# 保存处理后的图片，可指定新的文件名和格式
resized_image.save("resized.png")

print("图片处理并保存成功！")