import pygame


def _s(name, filetype="wav"):
    return pygame.mixer.Sound("Sounds/" + name + "." + filetype)


snd_fire = _s("fire")
snd_bangL = _s("bangLarge")
snd_bangM = _s("bangMedium")
snd_bangS = _s("bangSmall")
snd_extra = _s("extra")
snd_saucerB = _s("saucerBig")
snd_saucerS = _s("saucerSmall")
