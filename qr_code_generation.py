import qrcode
name = "www.youtube.com"
img = qrcode.make(name)
type(img)  # qrcode.image.pil.PilImage
img.save("youtube.png")

