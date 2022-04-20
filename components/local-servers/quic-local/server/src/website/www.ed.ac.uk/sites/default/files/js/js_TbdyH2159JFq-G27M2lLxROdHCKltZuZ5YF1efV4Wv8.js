/**
 * Add Google Tag Manager with a container ID dependent on cookie settings.
 */

(function () {
  'use strict';

  if (window.uoe_gdpr.default_id) {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      'gtm.start': new Date().getTime(),
      event: 'gtm.js'
    });

    if (typeof EdGel !== 'undefined' && EdGel.cookieSettings) {
      EdGel.cookieSettings.subscribe(function () {
        var container = window.uoe_gdpr.default_id;
        var overrides = window.uoe_gdpr.overrides;
        var allowed = EdGel.cookieSettings.allowedList();

        if (allowed && overrides.hasOwnProperty(allowed)) {
          container = overrides[allowed];
        }

        var f = document.getElementsByTagName('script')[0];
        var j = document.createElement('script');
        j.async = true;
        j.src = 'https://www.googletagmanager.com/gtm.js?id=' + container;
        f.parentNode.insertBefore(j, f);
      });
    }
    else {
      var f = document.getElementsByTagName('script')[0];
      var j = document.createElement('script');
      j.async = true;
      j.src = 'https://www.googletagmanager.com/gtm.js?id=' + window.uoe_gdpr.default_id;
      f.parentNode.insertBefore(j, f);
    }
  }

})();
;
(function($) {

Drupal.behaviors.webform_steps = {};
Drupal.behaviors.webform_steps.attach = function(context, settings) {

$('.webform-client-form', context).each(function() {
  var $form = $(this);
  var $steps = $form.find('.webform-progressbar .webform-progressbar-page');
  $form.find('.webform-steps-buttons .step-button').each(function(i) {
    var $button = $(this);
    if ($button.is(':enabled')) {
      $($steps[i]).click(function(event) {
        $button.click();
      }).addClass('clickable').css('cursor', 'pointer');
    }
  });
});

}
})(jQuery);
;
