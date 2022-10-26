window.addEventListener('DOMContentLoaded', function () {
  $('#language_code').keypress(function (event) {
    const keyCode = event.which;
    if (keyCode === 13) {
      const lang = $('#language_code').val();
      $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
        $('#hello').text(data.hello);
      });
    }
  });
  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
