import pywhatkit as pw

txt="""asdfg hjkl zxcv bnmbnm qwer tyuio opiuyt werdsaq ertyu dfghjk cvbnm aswqzx cvdfer bngh tyuyhh sdesq. sdddftyure sdewqasd frt ghyt vbnfgh nmh hjyui."""

pw.text_to_handwriting(txt,"convert text to handwriting.png",[255,0,0])
print("END")
