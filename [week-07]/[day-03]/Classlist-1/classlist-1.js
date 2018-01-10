'use strict';

let third_p = document.querySelectorAll('p');
if (third_p[2].classList.contains('red-dot')) {
  alert("OMG DOTS!");
}

if (third_p[3].innerText === 'dolphin') {
  third_p[0].textContent = 'pear';
}

if (third_p[0].classList.contains('apple')) {
  third_p[2].textContent = 'dog';
}

third_p[0].classList.add('red');

third_p[1].style.borderRadius = '10%';