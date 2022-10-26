window.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/hello/?lang=' + lang, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
