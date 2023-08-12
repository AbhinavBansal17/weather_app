document.addEventListener('DOMContentLoaded', function() {

  document.querySelector('#country').addEventListener('click', () => load_countries());
  document.querySelector('#state').addEventListener('click', () => load_states());
  document.querySelector('#city').addEventListener('click', () => load_cities());

  load_cities();
});


function load_countries() {

  document.querySelector('#countries').style.display = 'block';
  document.querySelector('#states').style.display = 'none';
  document.querySelector('#cities').style.display = 'none';


}

function load_states() {

  document.querySelector('#states').style.display = 'block';
  document.querySelector('#countries').style.display = 'none';
  document.querySelector('#cities').style.display = 'none';


}


function load_cities() {

  document.querySelector('#cities').style.display = 'block';
  document.querySelector('#states').style.display = 'none';
  document.querySelector('#countries').style.display = 'none';


}