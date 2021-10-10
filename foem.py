from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import urllib.request
import re

# Парсинг с помощью библиотеки BeautifulSoup4
def BS4():
    url = "https://lenta.ru/rubrics/russia/2019/12/01/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    allNews = []
    News_news = []
    News = []
    D = ''
    allNews = soup.find('h3', class_="card-title")
    News_news = soup.find('span', class_="g-date")
    News = soup.find('div', class_="span4")
    New = soup.findAll('section', class_="b-longgrid-column")
    for i in New:
        D += str(i) + " "
    D = D.replace('<section class="b-longgrid-column"><div class="item news b-tabloid__topic_news">', '')
    D = D.replace('<div class="info g-date item__info"><span class="g-date item__date"><span class="time">', '')
    D = D.replace('</span><span class="item__mdash">', '')
    D = D.replace('</span>', '')
    D = D.replace('</div><a class="titles" href="/news/2019/12/01/drugs/"><h3 class="card-title">', '\n')
    D = D.replace('</h3></a></div><div class="item news b-tabloid__topic_news">', '\n')
    D = D.replace('</div><a class="titles" href="/news/2019/12/01/reason/"><h3 class="card-title">', '\n')
    D = D.replace('</div><a class="titles" href="/news/2019/12/01/ikra/"><h3 class="card-title">', '\n')
    D = D.replace('</div><a class="titles" href="/news/2019/12/01/budet/"><h3 class="card-title">', '\n')
    D = D.replace('</div><a class="titles" href="/news/2019/12/01/paris/"><h3 class="card-title">', '\n')
    D = D.replace('</div><a class="titles" href="/news/2019/12/01/no_help/"><h3 class="card-title">', '\n')
    D = D.replace('</div><a class="titles" href="/news/2019/12/01/mvd/"><h3 class="card-title">', '\n')
    D = D.replace('</div><a class="titles" href="/news/2019/12/01/ryazan/"><h3 class="card-title">', '\n')
    D = D.replace('</div><a class="titles" href="/news/2019/12/01/38/"><h3 class="card-title">', '\n')
    D = D.replace('<h3 class="card-title">', '')
    D = D.replace('</div><a class="titles" ', '\n')
    D = D.replace('href="/news/2019/12/01/google_it/">', '')
    D = D.replace('</h3></a></div></section> ', '\n')
    D = D.replace('href="/news/2019/12/01/hiv/">', '')
    D = D.replace('href="/news/2019/12/01/20/">', '')
    D = D.replace('href="/news/2019/12/01/sekt/">', '')
    D = D.replace('href="/news/2019/12/01/medvedev/">', '')
    D = D.replace('href="/news/2019/12/01/lifetime/">', '')
    D = D.replace('href="/news/2019/12/01/avaria/">', '')
    D = D.replace('href="/news/2019/12/01/steklomoi/">', '')
    D = D.replace('href="/news/2019/12/01/shok/">', '')
    D = D.replace('href="/news/2019/12/01/polpred/">', '')
    D = D.replace('href="/news/2019/12/01/gorbyy/">', '')
    D = D.replace('href="/news/2019/12/01/video/">', '')
    D = D.replace('</h3></a></div><div class="item article"><div class="info g-date item__info">', '\n')
    D = D.replace('<a class="rubric item__rubric" href="/rubrics/russia/">', '')
    D = D.replace('</a><span class="g-date item__date"><span class="time">', ' ')
    D = D.replace('</div><a class="js-dh picture b-badge" href="/brief/2019/12/01/avtobus/">', '\n')
    D = D.replace('<img alt="" class="g-picture" height="200" src="https://icdn.lenta.ru/images/2019/12/01/15/20191201152035912/top7_8b52bf663747eb1f272d19145576b8b8.png" style="max-width: 300px; width: 300px; height: 200px;" width="300"/>','')
    D = D.replace('<svg class="b-badge__icon"><use xlink:href="#ui-badge-brief"></use></svg></a><a class="titles" href="/brief/2019/12/01/avtobus/">','')
    D = D.replace('</h3><span class="rightcol"> ', '\n')
    D = D.replace('</a></div><div class="item news b-tabloid__topic_news">', '\n')
    D = D.replace('href="/news/2019/12/01/wounded/">', '')
    D = D.replace('href="/news/2019/12/01/19/">', '')
    D = D.replace('href="/news/2019/12/01/why/">', '')
    D = D.replace('href="/news/2019/12/01/leader/">', '')
    D = D.replace('href="/news/2019/12/01/spasenie/">', '')
    return D

# Парсинг с помощью регулярных выражений

def Regex():
    a = ""
    b = ""
    c = ""
    c1 = ""
    c2 = ""
    c3 = ""
    c4 = ""
    c5 = ""
    course_pattern = r'[а-яёА-ЯЁ]{3}\s*[а-яёА-ЯЁ]{8}\s*важных.*?препарата.*в.*?России.*?приравняли.*?к.*?наркотикам'
    course_pattern2 = r'1\s*декабря\s*2019'
    course_pattern1 = r'[0-0]{2}[:][0-9]{2}'
    course_pattern3 = r'[1-1]{2}[:][4-6]{2}'
    course_pattern4 = r'Названа\sпричина\sпадения\sавтобуса\sс&nbsp;моста\sв&nbsp;Забайкалье'
    course_pattern5 = r'[а-яёА-ЯЁ]{7}\s*[а-яёА-ЯЁ]{7}\s*падения.*?автобуса.*с.*?моста.*?в.*?Забайкалье'
    course_pattern6 = r'[1-2]{2}[:][4-5]{2}'
    course_pattern7 = r'[а-яёА-ЯЁ]{6}\s[а-яёА-ЯЁ]{4}\sупотребления\sкрасной\sикры'
    with urllib.request.urlopen('https://lenta.ru/rubrics/russia/2019/12/01/') as responce:
        html = responce.read().decode("utf-8")
        first_pos = re.findall(course_pattern, html)
        two_pos = re.findall(course_pattern1, html)
        tree_pos = re.findall(course_pattern2, html)
        qwe_pos = re.findall(course_pattern3, html)
        ewq_pos = re.findall(course_pattern4, html)
        qwe1_pos = re.findall(course_pattern6, html)
        ewq1_pos = re.findall(course_pattern7, html)

    string = first_pos
    string1 = two_pos
    string2 = tree_pos

    for i in string:
        a += str(i) + " "

    for j in string1:
        b += str(j) + " "

    for q in string2:
        c += str(q) + " "
    for e in qwe_pos:
        c2 += str(e) + " "
    for p in ewq_pos:
        c3 += str(p) + " "
    for q1 in qwe1_pos:
        c4 += str(q1) + " "
    for q2 in ewq1_pos:
        c5 += str(q2) + " "

    c1 = re.search(course_pattern2, c)
    print(b + " —  " + c1.group())
    print(a.replace('&nbsp;', ' '))
    print(c2 + " —  " + c1.group())
    print(c3.replace('&nbsp;', ' '))
    print(c4 + " —  " + c1.group())
    print(c5)
    return b + " —  " + c1.group() + '\n' + a.replace('&nbsp;', ' ') + '\n' + c2 + " —  " + c1.group() + '\n' + c3.replace('&nbsp;', ' ') + '\n' + c4 + " —  " + c1.group() + '\n' + c5


class create_label:
    def __init__(self, text, f, txtVar):
        self.lbl = Label(root, textvariable=txtVar)
        self.lbl["text"] = text
        self.lbl["bg"] = f
        self.lbl["font"] = "Arial 9"
        self.lbl.place(x=0, y=0)
        self.lbl["justify"] = LEFT


def calc(event):
    lblVar1.set("")
    lblVar.set(BS4())
    messagebox.showinfo("Внимание", "Парсинг выполнен с помощью библиотеки BeautifulSoup4 ")


def calc1(event):
    lblVar.set("")
    lblVar1.set(Regex())
    messagebox.showinfo("Внимание", "Парсинг выполнен с помощью регулярных выражений")


def clear(event):
    lblVar.set("")
    lblVar1.set("")


if __name__ == "__main__":
    root = Tk()
    root.geometry('500x1000')
    root.title('Парсинг 4КТ')
    root.resizable(False, False)
    but = Button(root, text='BS4', width=10, height=3, font='arial 14', bg='red')
    but.bind("<Button-1>", calc)
    but.place(x=30, y=850, width=120, height=50)
    but1 = Button(root, text='Regex', width=10, height=3, font='arial 14', bg='red')
    but1.bind("<Button-1>", calc1)
    but1.place(x=350, y=850, width=120, height=50)
    but2 = Button(root, text='Clear', width=10, height=3, font='arial 14', bg='black', fg='white')
    but2.bind("<Button-1>", clear)
    but2.place(x=190, y=920, width=120, height=50)
    lblVar = StringVar()
    lblVar1 = StringVar()
    lbl = create_label('Text:', None, lblVar)
    lbl = create_label('Text:', None, lblVar1)

    root.mainloop()
