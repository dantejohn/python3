import requests
url = "https://stepic.org/media/attachments/course67/3.6.3/";
text = ["699991.txt"]
while text[0][0:2] != "We":
    print(url﻿ + text[0])
    r = requests.get(url﻿ + text[0])
    text = r.text.splitlines(True)

open("out.txt", "w").writelines(text)
