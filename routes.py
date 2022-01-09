from app import app
from flask import render_template, redirect, url_for, request, session, g
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
@app.route('/')
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
	link_lang = language_links(article_info.lang_links, lang_data)
	session['article'] = article_info.art_name
	return render_template("article.html", page=article_info,
							article_att=article_att,
							menu=menu,
							language_links=link_lang,
						   	zip=zip)


@app.route("/full_analysis", methods=['GET', 'POST'])
def full_analysis():
	article = session['article']
	article_info = ArticleInfo()
	article_info.get_info(article)
	lang_iterface = language_links(article_info.lang_links, lang_data)
	dict_data = {'title': [], 'full_lang': [], 'link': []}
	dict_info = {'back_links': []}
	for lang_short, lang_full, title, link in zip(lang_iterface['short_lang'], lang_iterface['full_lang'], lang_iterface['title'], lang_iterface['link']):
		article_info.language = lang_short
		article_info.get_info(title)
		dict_data['title'].append(title)
		dict_data['full_lang'].append(lang_full)
		dict_data['link'].append(link)
		dict_info['back_links'].append(article_info.back_links)

	print(dict_data)

	return render_template("full_analysis.html", dict_data=dict_data,
						   menu=menu,
						   zip=zip)

