import Barionix, random

def get_gif(arg):
    url = "http://giphy.com/search/%s" %arg
    res = Barionix.getIn(url, "src", None)
    gifs = []
    for i in res:
        if ".giphy." in i:
            gifs.append(i)
        else:
            pass
    result = random.choice(gifs)
    return result
