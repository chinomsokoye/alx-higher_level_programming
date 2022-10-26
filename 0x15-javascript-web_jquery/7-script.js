$(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, textStatus) {
    if (textStatus === 'success') {
      $('#character').text(data.name);
    }
  });
});
