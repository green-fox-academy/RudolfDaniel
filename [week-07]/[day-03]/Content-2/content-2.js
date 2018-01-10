let paragraphs = document.querySelectorAll('p');

for (var i = 0; i < paragraphs.length; i++) {
  paragraphs[i].innerText = paragraphs[paragraphs.length-1].textContent; 
}

console.log(paragraphs);