let content_of_text = document.querySelector('h1');
alert(content_of_text.textContent);

let content_of_paragraph = document.getElementsByTagName('p')[o];
console.log(content_of_paragraph.textContent);

let content_of_second = document.querySelector('.other');
alert(content_of_second.textContent);

content_of_text.innerText = 'New content';
console.log(content_of_text);

content_of_second.innerText = content_of_text.textContent;
console.log(content_of_second);