import random
import urllib.request

def dwnl_image(url):
    name= random.randrange(1,1000)
    fullname = str(name)+".jpg"
    urllib.request.urlretrieve(url,fullname)

dwnl_image("https://assets.myntassets.com/h_640,q_90,w_480/v1/assets/images/1794347/2017/3/8/11488968495808-MANGO-Women-Dresses-8881488968495695-1.jpg")
