$(() =>
  $.get(`https://fourtonfish.com/hellosalut/?lang=${$('html').attr('lang')}`,
    (data) => $('div#hello').html(data.hello)));
