'use strict';

let httpRequest = new XMLHttpRequest();
httpRequest.open('GET', 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=0563bf5aecdb4ac0ae210bd0ee9feb68&q=Apollo 11');
httpRequest.send(null);
httpRequest.onreadystatechange = function() {
  if (httpRequest.readyState === 4 && httpRequest.status === 200) {
    let response = JSON.parse(httpRequest.response);
    displayArticles(response.response.docs);
  }
};

function displayArticles (articles) {
  let element = document.createElement('ul');
  document.body.appendChild(element);

  articles.forEach(function(article) {
    let elements = document.createElement('li');
    element.appendChild(elements);
    elements.textContent = article.headline.main + article.snippet + article.pub_date;
  });
}