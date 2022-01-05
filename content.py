import wikipedia
from wikipediaapi import Wikipedia



class ArticleInfo(Wikipedia):
    art_name = None
    lang_number = 0
    art_summary = ''
    lang_list = []
    back_links = 0  #Returns all pages linking to the current page.
    full_url = None
    lang_links = None

    def get_info(self, article):
        self.art_name = article
        page = self.page(article)
        lang_links = page.langlinks
        self.lang_number = len(lang_links)
        self.lang_list = lang_links.keys()
        self.art_summary = page.summary
        self.back_links = len(page.backlinks)
        self.full_url = page.fullurl
        self.lang_links = page.langlinks


def language_links(lang_links, lang_dada):
    data = {'short_lang': [], 'full_lang': [], 'title': [], 'link': []}
    for l in sorted(lang_links.keys()):
        current = lang_links[l]
        data['short_lang'].append(current.language)
        data['title'].append(current.title)
        try:
            data['full_lang'].append(lang_dada[current.language]['native'][0])
        except:
            data['full_lang'].append('Not Recognized')
        data['link'].append(current.fullurl)
    return data
