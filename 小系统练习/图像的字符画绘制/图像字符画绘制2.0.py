#DrawCharImage.py
from PIL import Image
ascil_char = list('''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. ''')#生成字符画所需的字符集
def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    #gray = int(0.299 * r + 0.587 * g + 0.114 * b)
    unit = 256 / len (ascil_char)
    return ascil_char[int(gray//unit)]
def main():
    im = Image.open('QQ图片20210516165933.jpg')
    WIDTH, HEIGHT = 1000, 600
    im = im.resize((WIDTH, HEIGHT))
    txt =' '
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    fo = open('pic_char.txt', 'w')
    fo.write(txt)
    fo.close()
main()
