from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from mysql import connector
import mysql.connector

website = Flask(__name__)


@website.route('/', methods=['GET','POST'])
def index():

    return render_template("index.html")

@website.route('/Hakkında',methods=['GET','POST'])
def hakkinda():

    return render_template("Hakkında.html")

@website.route('/iletisim',methods=['GET','POST'])
def iletisim():
    return render_template("iletişim.html")

@website.route('/Motorlar',methods=['GET','POST'])
def Motorlar():
    return render_template("Motorlar.html")

@website.route('/2.ElUrunler',methods=['GET','POST'])
def IIElUrunler():
    return render_template("2.ElUrunler.html")

@website.route('/ozelkilavuzlar',methods=['GET','POST'])
def ozelkilavuzlar():
    return render_template("ozelkilavuzlar.html")

@website.route('/turkceelkitaplari',methods=['GET','POST'])
def turkceelkitaplari():
    return render_template("turkceelkitaplari.html")   


        