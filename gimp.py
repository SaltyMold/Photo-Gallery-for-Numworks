import math



def couleur_proche(couleur, palette):
    """Retourne l'index de la couleur la plus proche dans la palette."""
    return min(range(len(palette)), key=lambda i: math.sqrt(sum((couleur[j] - palette[i][j])**2 for j in range(3))))



def nw():
    lett = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"  
    palette_fixe = [
    	[63, 67, 40], [95, 113, 50], [148, 173, 57], [194, 214, 79], [239, 243, 124],
    	[227, 230, 172], [165, 198, 124], [115, 154, 112], [77, 102, 89], [52, 63, 65],
    	[40, 46, 59], [26, 31, 46], [30, 49, 75], [47, 76, 108], [61, 128, 163],
    	[99, 196, 204], [154, 229, 213], [229, 239, 239], [186, 201, 205], [141, 153, 164],
    	[105, 111, 128], [65, 68, 83], [184, 161, 194], [126, 101, 155], [92, 58, 111],
    	[57, 39, 94], [47, 25, 62], [78, 26, 73], [123, 35, 76], [178, 54, 87],
    	[209, 105, 116], [237, 170, 163], [238, 203, 144], [225, 168, 69], [197, 120, 53],
    	[141, 72, 48], [228, 114, 89], [195, 60, 64], [141, 54, 73], [92, 43, 52],
    	[60, 37, 43], [104, 64, 57], [130, 86, 70], [183, 120, 98], [125, 89, 93],
    	[83, 59, 65], [63, 51, 59], [43, 34, 42], [109, 78, 75], [134, 112, 102],
    	[180, 157, 126], [196, 198, 184]]
    img = gimp.image_list()[0]
    pdb.gimp_image_scale(img, 320, 240)
    drw = pdb.gimp_image_active_drawable(img)
    im, c, prec = "", 0, None
    for i in range(320 * 240):
        x, y = i % 320, i // 320
        v = list(pdb.gimp_image_pick_color(img, drw, x, y, 1, 0, 0))[:-1]
        index_couleur = couleur_proche(v, palette_fixe)
        if i == 0: prec = index_couleur
        if prec != index_couleur and i > 0:
            im += lett[prec] + (str(c) if c > 1 else "")
            c, prec = 1, index_couleur
        else: c += 1
    print("\"" + im + "\"")



nw()
