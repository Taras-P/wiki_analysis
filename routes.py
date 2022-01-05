from app import app
from flask import render_template, redirect, url_for, request
import forms
import wikipedia
import wikipediaapi
from content import ArticleInfo, language_links
import json

menu = [{"name": "Find article", "url": "/search"},
		{"name": "Wiki main page", "url": "https://en.wikipedia.org/wiki/Main_Page"},
		{"name": "PASS THROUGH LANGUAGES", "url": "/full_analysis"}]

article_att = ['lang_number', 'art_summary', 'lang_list', 'back_links']

with open('E:\work\python\FlaskPet\static\css\ISO_939.json', 'r') as jsonFile:
	lang_data = json.load(jsonFile)
	jsonFile.close()


@app.route('/search', methods=['GET', 'POST'])
def search():
	form = forms.Searcher()
	return render_template('search.html', form=form, menu=menu)


@app.route('/welcome')
def welcome():
	return render_template('welcome.html', menu=menu)


@app.route('/res', methods=['GET', 'POST'])
def res():
	articles = request.form.get('article')
	wiki = wikipedia.search(articles, results=10, suggestion=False)
	print("length of world: ", wiki)
	return render_template('res.html', results=wiki, articles=articles, menu=menu)


@app.route("/res/<article>", methods=['GET', 'POST'])
def article_load(article):
	article_info = ArticleInfo()
	article_info.get_info(article)
	l = language_links(article_info.lang_links, lang_data)
	return render_template("article.html", page=article_info,
							article_att=article_att,
							menu=menu,
							language_links=l,
						   	zip=zip)


@app.route("/full_analysis", methods=['GET', 'POST'])
def full_analysis(article):
	article_info = ArticleInfo()
	article_info.get_info(article)
	data = language_links(article_info.lang_links, lang_data)
	return render_template("full_analysis.html", menu=menu)

