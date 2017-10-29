from flask import Flask, request, render_template, make_response, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required
import requests
import json
import csv



app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret key!'

class StudentForms(FlaskForm):
    sign = StringField('Please Enter the name of Student')
    submit = SubmitField('Submit')


@app.route('/')
def mainpage():
    main_response = make_response('<p> Site is Using Cookies. '
                                  '<h1>Welcome to School Management</h1>'
                                  '<a href = "/addinformation" > Add new student </a> </br>'
                                  '<a href = "/viewallstudents" > View All Students </a> </br>'
                                  '<a href = "/showmyimage" > Look at all the school supplies they need! </a> </br>')
    main_response.set_cookie('secret', 'noSecret')
    return main_response


@app.route('/addinformation')
def ursignform():
	simpleForm = StudentForms()
	return render_template("addStudent.html", form=simpleForm)


@app.route('/addinformation', methods=['POST'])
def add_students():
    form = StudentForms(request.form)
    sign = form.sign.data

    with open("studentsinformation.csv","a") as csvfile:
        writer=csv.writer(csvfile, delimiter=',')
        writer.writerow([sign])

    return "You have added "+ sign;


@app.route('/viewallstudents')
def view_students():
    response=""
    # processed_text = text.upper()
    with open("studentsinformation.csv","r") as csvfile:
        reader=csv.reader(csvfile, delimiter=',')
        for rows in reader:
            response+="<p>"+rows[0]+"</p>"

    return response

@app.route('/showmyimage')
def insert_image():
	return render_template ("addimage.html")

@app.errorhandler(404)
def notfoundPage(e):
	return render_template("notFound.html")

@app.errorhandler(405)
def incorrectPage(e):
	return render_template("incorrectpage.html")


if __name__ == '__main__':
    app.run()