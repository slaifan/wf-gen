(function($) {

  $(document).ready(function() {

    if (EdGel.cookieSettings.allowed('performance')) { 
 
      setTimeout(function () {
      var a = document.createElement("script");
      var b = document.getElementsByTagName("script")[0];
      a.src = document.location.protocol + "//script.crazyegg.com/pages/scripts/0007/0800.js?" + Math.floor(new Date().getTime() / 3600000);
      a.async = true;
      a.type = "text/javascript";
      b.parentNode.insertBefore(a, b)
    }, 1);
 
    }
  });
 
})(jQuery);;
