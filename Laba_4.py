from flask import Flask, render_template, request
from json import dumps as jsonstring

app = Flask(__name__)

class Student(object):
    def __init__(self, id, fio, average_mark, image):
        self.id = id
        self.fio = fio
        self.average_mark = average_mark
        self.image = image


    def __str__(self, id, fio, average_mark, image):
        return("Имя:",fio,
               "ID:",id,
               "Средний бал:",average_mark,
               "Фотография:",image)

class Group(object):
    def __init__(self, id, number, students):
          self.id = id
          self.number = number
          self.students = students

    def __str__(self, id, number):
        return("ID:",id,
               "Номер группы:",number)

st1 = Student(1,"Зинитулен Г.О",5.0,"oGVnnPC5RaU.jpg")
st2 = Student(2,"Сафулин К.Ф",3.0,"person1941267519.jpg")
st3 = Student(3,"Татарский Т.Т",4.0,"w2QcTRfLzy8.jpg")


sts = [st1,st2,st3]

gr_sm = Group("1","СМ10_61Б",sts)

@app.route("/")
def hello_world():
    return render_template('index.html',group = gr_sm)

@app.route("/new_st")
def adding():
    id = request.args.get('id')
    fio = request.args.get('fio')
    average_mark = request.args.get('average_mark')
    new_st = Student(id,fio,average_mark,"w2QcTRfLzy8.jpg")
    gr_sm.students.append(new_st)
    return "Добавил"
