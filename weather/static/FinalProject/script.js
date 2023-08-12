document.addEventListener('DOMContentLoaded', function() {

  document.querySelector('#info-2').addEventListener('click', () => load_info());
  document.querySelector('#weather-2').addEventListener('click', () => load_weather());
  document.querySelector('#password-2').addEventListener('click', () => load_password());

  load_info();
});

function load_info() {

  document.querySelector('#info').style.display = 'block';
  document.querySelector('#weather').style.display = 'none';
  document.querySelector('#password').style.display = 'none';

}

function load_weather() {

  document.querySelector('#weather').style.display = 'block';
  document.querySelector('#info').style.display = 'none';
  document.querySelector('#password').style.display = 'none';

}

function load_password() {

  document.querySelector('#password').style.display = 'block';
  document.querySelector('#info').style.display = 'none';
  document.querySelector('#weather').style.display = 'none';


}

