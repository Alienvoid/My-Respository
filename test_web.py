from urllib import request
import re
def getHTML(url):
    return request.urlopen(url).read().decode('utf-8')#this function is used to open a web page and return the HTML document data of the page in form of String .
start_page=1
end_page=2
pic_tags='hiten'
for num in range(start_page,end_page+1):
    pic_url_ord_list=re.findall(r'<a class="thumb" href="/post/show/(.*?)">',getHTML('https://yande.re/post?page='+str(num)+'&tags=%s'%pic_tags))#this sentence returns a list consisting of the source of picture
    pic_url_list=[]
    for i in pic_url_ord_list:
        last_num=i[0:6]
        print('Collecting '+'https://yande.re/post/show/'+last_num)
        pic_url='https://yande.re/post/show/'+last_num
        pic_url_list.append(pic_url)
    print('Start to initialize and download pictures, please wait.')
    src_list=[]
    for n in pic_url_list:
        print('Collecting imagine source from '+n)
        src_list.append(re.findall(r'<img.*src="(.*?)"', getHTML(n))[1])
    print('Imagine sources have been collected. Start to download the pictures of page %s'%str(num))
    x=1
    for pic in src_list:
        print('downloading '+pic)
        request.urlretrieve(pic,'pic\\%d\\%d.jpg'%(num,x))
        x+=1