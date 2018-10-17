# ! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
import datetime

def index(request):
    main()
    return render(request, r"C:\Users\Alena\Documents\test_project\new_try\schedule\templates\schedule\index.html", {})


subjects = (
    "Планирование развития сервисов и услуг связи на базе инфокоммуникационных технологий",
    "ОСНОВЫ ПОСТРОЕНИЯ ИНФОКОММУНИКАЦИОННЫХ СИСТЕМ И СЕТЕЙ (ЛЕК)",
    "АДМИНИСТРИРОВАНИЕ OC UNIX (лек)",
    "МУЛЬТИМЕДИЙНЫЕ ТЕХНОЛОГИИ",
    "ОБЛАЧНЫЕ ТЕХНОЛОГИИ И УСЛУГИ",
    "МЕТРОЛОГИЯ И ТРЕБОВАНИЯ СТАНДАРТИЗАЦИИ В ИНФОКОММУНИКАЦИОННЫХ СИСТЕМАХ",
    "АДМИНИСТРИРОВАНИЕ СЕТЕЙ WINDOWS",
    "СОЗДАНИЕ КЛИЕНТ-СЕРВЕРНЫХ ПРИЛОЖЕНИЙ ",
    "СОЗДАНИЕ ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ ИНФОКОММУНИКАЦИОННЫХ СИСТЕМ",
)

file_index = r"C:\Users\Alena\Documents\test_project\new_try\schedule\templates\schedule\index.html"

def main():
    file_temp = r"C:\Users\Alena\Documents\test_project\new_try\schedule\templates\schedule\temp.txt"
    import sys
    reload(sys)
    import locale
    # sys.setdefaultencoding('utf8')
    import datetime
    logfile = open(file_index, 'w+')
    logfile.close()

    logfile = open("index.html", 'w+')
    logfile.close()

    generate_page()



def save_to_file(message, file_custom=None):
    if file_custom:
        file_local = file_custom
    else:
        file_local = file_index

    logfile = open(file_local, 'a')
    logfile.write(message)
    logfile.close()

    """
    try:
        logfile = open(file_local, 'a')
        logfile.write(message)
        logfile.close()
    except:
        print "The logger has error with filewriting" """


def get_array():
    odd_week = [
        [
            {"time": "",
             "class": "Отдых. Хорошей идеей будет сходить на физру <p>Ссыль на  <a href='https://isu.ifmo.ru/pls/apex/f?p=2153:15:103802598991767'>расписание</a> секций. </p>",
             "place": "",
             "teacher": "",
             "homework": None}
        ],
        [
            {"time": "",
             "class": "Отдых. Хорошей идеей будет сходить на физру <p>Ссыль на  <a href='https://isu.ifmo.ru/pls/apex/f?p=2153:15:103802598991767'>расписание</a> секций. </p>",
             "place": "",
             "teacher": "",
             "homework": None}
        ],
        [
            {"time": datetime.time(hour=13, minute=30),
             "class": "Планирование развития сервисов и услуг связи на базе инфокоммуникационных технологий (Лаб)",
             "place": "424 АУД. Биржевая линия, д.14, лит.А",
             "teacher": "Гуревич Евгений Львович",
             "homework": "Написали две контрольные, у меня есть фотки моего варианта, потом выложу"},
            {"time": datetime.time(hour=15, minute=20),
             "class": "Планирование развития сервисов и услуг связи на базе инфокоммуникационных технологий (лек)",
             "place": "424 АУД. Биржевая линия, д.14, лит.А",
             "teacher": "Гуревич Евгений Львович",
             "homework": None},
            {"time": datetime.time(hour=17, minute=00),
             "class": "ОСНОВЫ ПОСТРОЕНИЯ ИНФОКОММУНИКАЦИОННЫХ СИСТЕМ И СЕТЕЙ (ЛЕК)",
             "place": "353 АУД. Биржевая линия, д.14, лит.А",
             "teacher": "Дубаков Анатолий Алексеевич",
             "homework": "Изучить теорию на его сайте <a href='aad.tpu.ru/4955'>aad.tpu.ru/4955 </a>, пройти на стороннем сайте лекции, написать реферат по ним (просто переведя на русский со скринами) и приложить к рефератам "
                         " ответы на вопросы в тех же модулях. Написать реферат и определиться с темой диплома и научруком. "},
            {"time": datetime.time(hour=18, minute=40),
             "class": "ОСНОВЫ ПОСТРОЕНИЯ ИНФОКОММУНИКАЦИОННЫХ СИСТЕМ И СЕТЕЙ (Прак)",
             "place": "353 АУД. Биржевая линия, д.14, лит.А",
             "teacher": "Дубаков Анатолий Алексеевич",
             "homework": None},
        ],
        [
            {"time": datetime.time(hour=10, minute=00),
             "class": "АДМИНИСТРИРОВАНИЕ OC UNIX (лек)",
             "place": "101 АУД. ул.Гастелло, д.12, лит.А",
             "teacher": "Ананченко Игорь Викторович",
             "homework": "Сдали две лабы<br>"
                "При сдаче очень следит за оформлением, задает вопросы при сдаче<br>"
                "Есть смысл чаще к нему ходить, чтобы знал в лицо<br>"
                "Прошли тест на  <a href='fx-fx.ru'>fx-fx.ru</a> по моделям OSI<br>"
                "<a href='https://www.intuit.ru/studies/courses/1/1/lecture/22'>Тут</a>есть все ответы, но  у всех максимум 7 из 10"},
            {"time": datetime.time(hour=11, minute=40),
             "class": "АДМИНИСТРИРОВАНИЕ OC UNIX (ЛАБ)",
             "place": "101 АУД. ул.Гастелло, д.12, лит.А",
             "teacher": "Ананченко Игорь Викторович",
             "homework": None},
            {"time": datetime.time(hour=13, minute=30),
             "class": "АДМИНИСТРИРОВАНИЕ СЕТЕЙ WINDOWS (ЛАБ)",
             "place": "101 АУД. ул.Гастелло, д.12, лит.А",
             "teacher": "Ананченко Игорь Викторович",
             "homework": "Первая лаба: надо поставить windows server (родительский и три разностных), сбросить уникальные id с помощью sysprep, контроллеры доменов должны быть DC1.familiya.local (фамилия своя, аналогично для систем 2 и 3)"
                "<br>Лабы по винде есть <a href='https://yadi.sk/i/zMCLp4YhgSGy4Q'>тут</a>"},
        ],
        [
            {"time": "",
             "class": "Отдых. Хорошей идеей будет сходить на физру <p>Ссыль на  <a href='https://isu.ifmo.ru/pls/apex/f?p=2153:15:103802598991767'>расписание</a> секций. </p>",
             "place": "",
             "teacher": "",
             "homework": None}
        ],
        [
            {"time": datetime.time(hour=15, minute=20),
             "class": "Облачные технологии и услуги (Лаб) : 2, 6, 10, 14 недели",
             "place": "304 АУД. ул.Гастелло, д.12, лит.А",
             "teacher": "Буркова Мария Леонидовна",
             "homework": "Дохренища лаб, но сдавать легко"},
            {"time": datetime.time(hour=17, minute=00),
             "class": "Облачные технологии и услуги (Лаб) : 2, 6, 10, 14 недели",
             "place": "304 АУД. ул.Гастелло, д.12, лит.А",
             "teacher": "Буркова Мария Леонидовна",
             "homework": None},
        ],
    ]
    even_week = [
        [
            {"time": datetime.time(hour=15, minute=20),
             "class": "МУЛЬТИМЕДИЙНЫЕ ТЕХНОЛОГИИ (лек)",
             "place": "405-1 АУД. Кронверкский пр., д.49, лит.А",
             "teacher": "Андреев Артем Станиславович",
             "homework": None},
            {"time": datetime.time(hour=17, minute=00),
             "class": "МУЛЬТИМЕДИЙНЫЕ ТЕХНОЛОГИИ (ЛАБ)",
             "place": "405-1 АУД. Кронверкский пр., д.49, лит.А",
             "teacher": "Андреев Артем Станиславович",
             "homework": None},
            {"time": datetime.time(hour=18, minute=40),
             "class": "Облачные технологии и услуги (Лек) : 3, 7, 11, 15 нед.",
             "place": "403 АУД. Кронверкский пр., д.49, лит.А",
             "teacher": "Осипов Никита Алексеевич",
             "homework": None},
            {"time": datetime.time(hour=20, minute=20),
             "class": "Облачные технологии и услуги (Лек) : 3, 7, 11, 15 нед.",
             "place": "403 АУД. Кронверкский пр., д.49, лит.А",
             "teacher": "Осипов Никита Алексеевич",
             "homework": None},
        ],
        [
            {"time": "",
             "class": "Отдых. Хорошей идеей будет сходить на физру <p>Ссыль на  <a href='https://isu.ifmo.ru/pls/apex/f?p=2153:15:103802598991767'>расписание</a> секций. </p>",
             "place": "",
             "teacher": "",
             "homework": None}
        ],
        [
            {"time": "",
             "class": "Отдых. Хорошей идеей будет сходить на физру <p>Ссыль на  <a href='https://isu.ifmo.ru/pls/apex/f?p=2153:15:103802598991767'>расписание</a> секций. </p>",
             "place": "",
             "teacher": "",
             "homework": None}
        ],
        [
            {"time": datetime.time(hour=10, minute=00),
             "class": "Метрология и требования стандартизации в инфокоммуникационных системах (Лек)",
             "place": "428 АУД. пер. Гривцова, д.14-16, лит.А",
             "teacher": "Полякова Елена Валериевна",
             "homework": None},
            {"time": datetime.time(hour=11, minute=40),
             "class": "Метрология и требования стандартизации в инфокоммуникационных системах (Лаб)",
             "place": "428 АУД. пер. Гривцова, д.14-16, лит.А",
             "teacher": "Полякова Елена Валериевна",
             "homework": None},
            {"time": datetime.time(hour=15, minute=20),
             "class": "СОЗДАНИЕ КЛИЕНТ-СЕРВЕРНЫХ ПРИЛОЖЕНИЙ (ПРАК)",
             "place": "304 АУД. ул.Гастелло, д.12, лит.А",
             "teacher": "Иванов Сергей Евгеньевич",
             "homework": "Несложные лабы по базам и программированию, варианты заданий <a href='https://vk.com/doc10284375_476894994?hash=42b4a5efd9754ee42c&dl=4be65eb6d9f58c9f1b'>тут</a>, сами задания где-то в архиве"},
            {"time": datetime.time(hour=17, minute=00),
             "class": "СОЗДАНИЕ КЛИЕНТ-СЕРВЕРНЫХ ПРИЛОЖЕНИЙ  (ЛЕК)",
             "place": "304 АУД. ул.Гастелло, д.12, лит.А",
             "teacher": "Иванов Сергей Евгеньевич",
             "homework": None},
        ],
        [
            {"time": "",
             "class": "Отдых. Хорошей идеей будет сходить на физру <p>Ссыль на  <a href='https://isu.ifmo.ru/pls/apex/f?p=2153:15:103802598991767'>расписание</a> секций. </p>",
             "place": "",
             "teacher": "",
             "homework": None}
        ],
        [
            {"time": datetime.time(hour=13, minute=30),
             "class": "СОЗДАНИЕ ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ ИНФОКОММУНИКАЦИОННЫХ СИСТЕМ (ЛАБ)",
             "place": "101 АУД. ул.Гастелло, д.12, лит.А",
             "teacher": "Осипов Никита Алексеевич",
             "homework": None},
            {"time": datetime.time(hour=15, minute=20),
             "class": "Создание программного обеспечения инфокоммуникационных систем (Лек) : 3, 7, 11, 15 нед.",
             "place": "101 АУД. ул.Гастелло, д.12, лит.А",
             "teacher": "Осипов Никита Алексеевич",
             "homework": None},
            {"time": datetime.time(hour=17, minute=00),
             "class": "Создание программного обеспечения инфокоммуникационных систем (Лек) : 3, 7, 11, 15 нед.",
             "place": "101 АУД. ул.Гастелло, д.12, лит.А",
             "teacher": "Осипов Никита Алексеевич",
             "homework": None},
        ],
    ]
    today = datetime.datetime.today() + datetime.timedelta(days=1)
    today = today.date()
    first_day = datetime.date(year=2018, month=9, day=1)
    delta = today - first_day
    number_of_weeks = delta.days / 7
    if number_of_weeks % 2 == 0:
        print "today is odd week"
        array = [
            {
                "week": "odd",
                "days": odd_week
            },
            {
                "week": "even",
                "days": even_week
            }
        ]
    else:
        print "today is even week"
        array = [
            {
                "week": "even",
                "days": even_week
            },
            {
                "week": "odd",
                "days": odd_week
            }
        ]

    from models import Class
    for i in Class.objects.all():

        title = i.title
        title = str(title.encode('CP866'))
        homework = i.homework
        homework = str(homework.encode('CP866'))
        flag = True
        for line in array:
            for day in line["days"]:
                for sub in day:
                    subject = str(sub["class"].encode('CP866'))
                    if subject in title or title in subject:
                        if flag:
                            sub["homework"] = homework
                            flag = False

    return array




def generate_page():
    array = get_array()
    flag = True
    css = ".zero{ border-collapse: collapse; border: 15px solid gray; width: 100%; } TD, TH { padding: 3px; /* Поля вокруг содержимого таблицы */ border: 1px solid black; /* Параметры рамки */ } TH { background: #b0e0e6; /* Цвет фона */ } body { background-image: url(bg_352383.png); } ::selection {background: #981181; color:#fff;} ::-moz-selection {background: #981181; color:#fff;} ::-webkit-selection {background:#981181; color:#fff;} .one{ width: 30%; height: 100%; } .two { width: 100%; height: 100%; border: grey; } .three { height: 100px; text-align: center; } .actual{ border: 5px solid #981181; width: 100%; height: 100%; } td.one:hover { background-color: rgba(199, 199, 199, 0.3); } p{ color: gray; margin: 5px; } .news { background-color: lightcoral; border-radius: 15px; padding: 5px; } .news ol li { margin: 10px; } .homework { background-color: #d6f9d9; border: 1px solid black; /* Рамка вокруг таблицы */ } .homework tr td { padding: 5px; /* Поля вокруг содержимого ячейки */ } .odd { background-color: #a6f9d9; } .session { background-color: #fff6bc; border: 1px solid black; /* Рамка вокруг таблицы */ } .session tr td { padding: 5px; /* Поля вокруг содержимого ячейки */ } .odd2 { background-color: #fffde1; }"
    load_css = "<link href='style.css' rel='stylesheet'>"
    js = "<script>window.onload = function(){progres();var now = new Date();var elem = document.getElementById(now.getDate()+1);if (now.getHours()> 18) {elem.className = elem.className.replace('two', 'actual') }else { var elem = document.getElementById(now.getDate()); elem.className = elem.className.replace('two', 'actual')  }}</script>"

    save_to_file(
        "<!DOCTYPE html> <html> <head> <meta charset='UTF-8'></head> <body> <table class='zero'><tr><th></th><th>Понедельник</th><th>Вторник</th><th>Среда</th><th>Четверг</th><th>Пятница</th><th>Суббота</th></tr>")
    last_day = None
    today = datetime.datetime.today() # + datetime.timedelta(days=1)
    for line in array:
        string, last_day = get_line_with_dates(last_day)
        save_to_file(string)
        save_to_file("<tr><td>" + odd_or_even_week(line["week"]) + "</td>")
        days = line["days"]
        for day_number, day in enumerate(days):
            save_to_file("<td class='one'>")
            if day_number == today.weekday() and flag:
                # print day_number, "should be ", 3, today.weekday(),
                save_to_file("<table class='actual'>")
                flag = False
            else:
                save_to_file("<table class='two'>")
            # print len(day), "*"
            for sub in day:
                if str(sub["time"]) != "":
                    # print sub["time"], type(sub["time"])
                    other_info = "<p>{0} <br>{1} </p>".format(sub["place"], sub["teacher"])
                    if sub["homework"] is not None and sub["homework"] != "":
                        save_to_file(
                            "<tr>" + "<td>" + str(sub["time"]) + "</td><td>" + sub["class"] + other_info +
                            "<p style='color:red'>" + sub["homework"] + "</p>" + "</td></tr>")
                    else:
                        save_to_file("<tr>" + "<td>" + str(sub["time"]) + "</td><td>" + sub["class"] + other_info +
                                     "</td></tr>")

                else:
                    save_to_file("<tr><td>" + sub["class"] + "</td></tr>")
            save_to_file("</table>")
            save_to_file("</td>")
        save_to_file("</tr>")

    save_to_file("</table></body></html>")
    save_to_file("<style>"+css+"</style>")



""""""






ddd = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def odd_or_even_week(week):
    if week == "odd":
        return "Четная неделя"
    else:
        return "Нечетная неделя"

# сделать функцию добавления домашки
def add_homework(text, subject, week):
    array = get_array()
    if text != "":
        for line in array:
            # print line["week"], week, line["week"] == week
            if line["week"] == week:
                for day in line["days"]:
                    for sub in day:
                        # print  sub["class"], subject, sub["class"] == subject
                        if sub["class"] == subject:
                            sub["homework"] = text
                            logfile = open(file_index, 'w')
                            logfile.close()
                            generate_page()

def get_line_with_dates(last_day=None):

    import datetime
    if last_day:
        today = last_day + datetime.timedelta(days=2)
    else:
        if datetime.datetime.today().weekday() == 6:
            today = datetime.datetime.today() + datetime.timedelta(days=6)
        else:
            today = datetime.datetime.today()
    temp = today
    while temp.weekday() != 0:
        temp -= datetime.timedelta(days=1)

    monday = temp
    string = "<tr><td></td>"
    temp = datetime.datetime.today().date() # + datetime.timedelta(days=1)
    # print "today", temp
    for x in range(6):
        # print "monday ", monday.date(), monday.date() == temp
        if monday.date() == temp:
            string += "<td  style='text-align: center; border: 5px solid #981181;'>" + monday.strftime(
                "%B %d") + "</td>"
        else:
            string += "<td  style='text-align: center;'>" + monday.strftime("%B %d") + "</td>"
        monday += datetime.timedelta(days=1)

    string += "</tr>"
    return string, monday


import time

# time.sleep(5)

# add_homework("TERTSTSTS ", "Метрология и требования стандартизации в инфокоммуникационных системах (Лаб)", "odd")

