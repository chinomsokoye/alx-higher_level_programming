$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
    if (textStatus === 'success') {
      const films = data.results;
      for (const i in films) {
        $('#list_movies').append('<li>' + films[i].title + '</li>');
      }
    }
  });
});
