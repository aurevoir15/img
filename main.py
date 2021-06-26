from PIL import Image
import os



for file in os.listdir('orig'):  # . 就是現在位置的意思
    if file.endswith('.jpg'): # endswith 檢查字串是否有在
        image_file = Image.open(os.path.join('orig', file)) #open colour image
        image_file = image_file.convert('L') # convert image to black and white
        image_file.save(os.path.join('result', file[:-4] + '_grey.png'))  #[:-4]把.jpg刪掉