from ascii_magic import AsciiArt, Back
from PIL import ImageEnhance

# output = AsciiArt.from_image("test_image.jpg")
# output.to_terminal()

#1st one
# output.image = ImageEnhance.Brightness(output.image).enhance(0.8)
# output.to_terminal(columns=100,back=Back.BLUE)


#2nd one
# lion_output = AsciiArt.from_image('lion.jpg')
# lion_output.to_html_file('lion3.html',columns=200,width_ratio=2.0)


#3rd one
# mana_output = AsciiArt.from_image('test2.jpg')
# mana_output.image = ImageEnhance.Brightness(mana_output.image).enhance(1.2)
# mana_output.to_html_file('test2_three.html',columns=400,width_ratio=2.3)


#4th one
grp = AsciiArt.from_image('test4.jpg')
grp.image = ImageEnhance.Brightness(grp.image).enhance(1.25)
grp.image = ImageEnhance.Sharpness(grp.image).enhance(1.3)
grp.image = ImageEnhance.Color(grp.image).enhance(1.15)
grp.to_html_file('test4_one.html',columns=400,width_ratio=2)
