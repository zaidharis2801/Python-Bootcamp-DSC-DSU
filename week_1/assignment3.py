import time
song ='''Najaane kab se
Umeedain kuch baqi hain
Mujhe phir bhi teri yaad
Kyun ati hai?
Najaane kab se

Durr jitna bhi tum mujhse
Paas tere main
Ab toh aadat si hai mujhko aise jeene main
Zindagi se koi shikva bhi nahi hai
Ab toh zinda hun main iss neele asmaan main
This line is here for a bit of fun
if you see this just reply "hello penguin" anywhere or say
the words in the friday class

Chaahat aisi hai yeh teri
Barhti jaye
Aahat aise hai yeh teri mujhko sataye

Yaadain gehri hain itni
Dil doob jaye
Aur aankhon main yeh ghum num ban jaye

Ab toh aadat si hai mujhko aise jeene main

Yeh jo raatain hain
Yeh jo baatain hain
Sabhi raatain hain
Bhula do unhain
Mitta do unhain

Ab toh aadat si hai mujhko'''
song_list=song.splitlines()

for i in song_list:
    time.sleep(0.5)
    print(i)