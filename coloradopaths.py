import glib
def mapmaker (filename):
    f = open(filename, 'r')
    data = f.readlines()
    topo = []
    values = []
    for i in range (0 , len(data)):
        topo.append (data[i].split('   '))
    for i in range (0, len(topo)):
        values.append([])
        for j in range (1, len(topo[i])):
                        values[i].append(int(topo[i][j]))
    f.close()
    return values
def normalize (values):
    a = 255/2
    normie = []
    for i in range (0, len(values)):
        normie.append([])
        for j in range (1, len(values[i])):
            top = max(values[i])
            bottom = min(values[i])
            a = 255/top
            value = values[i][j]
            value = (255*(value-bottom))/(top-bottom)
            normie[i].append(value)
    return normie
def main ():
    import glib
    glib.open_window(800, 600)
    colorado = normalize(mapmaker("Colorado_480x480.txt"))
    im = glib.create_image (len(colorado),len(colorado[0]))
    model = glib.get_pixels (im)
    length = im.size[0]
    height = im.size[1]
    for x in range ( 0 , length):
        for y in range (0 , height):
            point = int(colorado[x][y])
            color = model.getpixel(x,y)
            model.setpixel(x, y, (point,point,point))   
    glib.show_image(im, 400,300)
    glib.update()
main()
