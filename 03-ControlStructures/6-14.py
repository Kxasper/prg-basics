#chyba git
facebook = True
twitter = False
instagram = True
social_account=0

if facebook:
    social_account+=1
if twitter:
    social_account+=1
if instagram:
    social_account+=1

if social_account>=2:
    print("You are a good influencer!")
else:
    print("Too low count a accounts")