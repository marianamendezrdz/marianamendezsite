
/* pushpin for TopNav */
$('.pushpin-demo-nav').each(function() {
    var $this = $(this);
    var $target = $('#pushpinthis' + $(this).attr('data-target'));
    $this.pushpin({
      top: $target.offset().top,
      bottom: $target.offset().top + $target.outerHeight() - $this.height()
    });
  });
  /* initialization */
  document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.pushpin');
  var instances = M.Pushpin.init(elems, options);
});
  /* --------------------------------------------------------------------------- */
