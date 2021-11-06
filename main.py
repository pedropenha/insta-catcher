import os
import instaloader
from instaloader import Profile
import json

L = instaloader.Instaloader()
profile = Profile.from_username(L.context, username="username to get the images")
hashtag1 = "#marcenariasobmedida" #hashtag to search in user profile 
hashtag2 = 'marcenariasobmedida' #duplicate of the above hashtag for processing in the code

lista = []
flag = 0

#check if the dados.json file already exists
if os.path.exists('dados.json'):
    with open("dados.json", encoding='utf8') as f:
        linha = json.loads(f.read())
        for val in profile.get_posts():
            if hashtag2 in val.caption_hashtags:
                for linhas in linha.get("Insta"):
                    if val.shortcode == linhas.get("shortcode"):
                        flag = 1
                        break
                if flag == 0:
                    L.download_post(val)
                    lista.append(dict(shortcode=val.shortcode))
                else:
                    flag = 0

    dict_salvar = json.dumps(lista, indent=4, sort_keys=False)
    try:
        file = open("dados.json", "a")
        file.write(dict_salvar)
        file.close()
    except Exception as erro:
        print("O erro é: {}".format(erro))
else:
    for val in profile.get_posts():
        if hashtag2 in val.caption_hashtags:
            L.download_post(val, target=profile.username)
            lista.append(dict(shortcode=val.shortcode))

    dict_salvar = {"Insta": lista}
    dict_salvar = json.dumps(dict_salvar, indent=4, sort_keys=False)
    try:
        file = open("dados.json", "w")
        file.write(dict_salvar)
        file.close()
    except Exception as erro:
        print("O erro é: {}".format(erro))