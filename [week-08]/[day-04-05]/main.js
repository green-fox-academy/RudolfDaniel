'use strict';

let httpRequest = new XMLHttpRequest();
httpRequest.open('GET', 'https://time-radish.glitch.me/posts');
httpRequest.send(null);
httpRequest.onreadystatechange = function() {
  if (httpRequest.readyState === 4 && httpRequest.status === 200) {
    let response = JSON.parse(httpRequest.response);
    console.log(response);
    response.posts.forEach(function (element) {
      createComment(element)
    });
  }
};

function createComment(element) {
  let comment = document.createElement('div');
  comment.classList.add('comment');
  document.querySelector('.commentbox').appendChild(comment);

  let voter = document.createElement('div');
  voter.classList.add('voter');
  comment.appendChild(voter);

  let upvote = document.createElement('img');
  upvote.classList.add('upvote');
  upvote.src = 'upvote.png';
  voter.appendChild(upvote);
  
  let counter = document.createElement('p');
  counter.classList.add('counter');
  counter.textContent = element.score;
  voter.appendChild(counter);

  let downvote = document.createElement('img');
  downvote.classList.add('downvote');
  downvote.src = 'downvote.png';
  voter.appendChild(downvote);

  let commenttext = document.createElement('div');
  commenttext.classList.add('commenttext');
  comment.appendChild(commenttext);

  let clear = document.createElement('div');
  clear.classList.add('clearfix');
  comment.appendChild(clear);

  let title = document.createElement('h3');
  commenttext.appendChild(title);
  title.textContent = element.title;

  let submitter = document.createElement('p');
  submitter.classList.add('submitter');
  submitter.textContent = 'submitted by ' + element.owner + ' ' + element.timestamp + ' minutes ago';
  commenttext.appendChild(submitter);
}