from PIL import Image

image = Image.open("./data/example.png")

binary_string = ""
for pixel in image.getdata():
    thing = "".join(format(val, '08b') for val in pixel[:3])
    print(len(thing))
    binary_string += "".join(format(val, '08b') for val in pixel[:3])

width, height = image.size

mode = image.mode

print("Image size:", width, "x", height)
print("Image mode:", mode)

print("Binary string (first 100 characters):", binary_string[:100])

print(len(binary_string), 35 * 34, len(binary_string) // 24)
