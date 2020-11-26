import requests
import bs4
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detik-populer')
def detik_populer():
    url = 'https://www.detik.com/terpopuler?tag_from=framebar'
    content = requests.get(url)
    # print(content.text)
    html = bs4.BeautifulSoup(content.text, "html.parser")
    # print(html)
    populer_area = html.find(attrs={'class': 'grid-row list-content'})
    titles = populer_area.find_all(attrs={'class': 'media__title'})
    images = populer_area.find_all(attrs={'class': 'media__image'})

    return render_template('index.html',images=images)


if __name__ == '__main__':
    app.run(debug=True)