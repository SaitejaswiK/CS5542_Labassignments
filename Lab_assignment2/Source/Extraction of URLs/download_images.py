import urllib.request
import os
from PIL import Image

words_list = ["food"]
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'


def downloadImages():
    for index in words_list:
        newpath = 'Dataset/food'
        i=0
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        print(index)
        with open('Extracted_urls.txt') as openfile:
            for line in openfile:
                if str(line).startswith('"') and str(line).endswith('"'):
                    print("enter")
                    line = line[1:-1]
                i = i + 1
                full_path = newpath+'/'+str(i) + '.jpg'
                headers = {'User-Agent': user_agent, }
                try:
                    request = urllib.request.Request(line, None, headers)
                    response = urllib.request.urlopen(request)
                    # install PIL package to convert the response into a PIL Image object to further save it
                    image = Image.open(response)
                    image.save(full_path)
                except Exception as ex:
                    print(line, ex)


if __name__ == '__main__':
    downloadImages()
