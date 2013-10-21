jQuery(document).ready(function(jq){

  /*************************
   *  MOBILE MENU BUTTON
   * **********************/

  jq("#portaltab-sitemap").click(
    function (event) {
      // Show the menu items
      event.preventDefault();

      var MENU_HIDDEN = 'menu_hidden';
      var MENU_VISIBLE = 'menu_visible';

      if (jq('#portaltab-sitemap').hasClass(MENU_HIDDEN)) {
        // Show menu
        jq('#portal-globalnav li').show();
        jq('#portaltab-sitemap').removeClass(MENU_HIDDEN);
        jq('#portaltab-sitemap').addClass(MENU_VISIBLE);
        jq('#portaltab-sitemap a').html('Cacher le menu');
      } else {
        // Hide menu
        jq('#portal-globalnav li').hide();
        jq('#portaltab-sitemap').removeClass(MENU_VISIBLE);
        jq('#portaltab-sitemap').addClass(MENU_HIDDEN);
        jq('#portaltab-sitemap a').html('Afficher le menu');
      }

      jq('#portaltab-sitemap').show();
    }
  );

  /*************************
   *  HOME PAGE CONTENT
   * **********************/

  /* Light bow for "Mentions sur les Décrets" links
  !!! Links title must be 'Mentions sur les Décrets'
  Documentation : http://plone.org/products/plone.app.jquerytools/#overlay-helpers
  */
  jq(".section-front-page #content a[title='Mentions sur les Décrets']")
    .prepOverlay({
        subtype: 'ajax',
        filter: '#content > *',
        cssclass: 'home_decret_overlay',
        config: {expose:{color:'#00f'}}
        });;

});