console.log('\'Allo \'Allo!');

endpoint = "http://localhost:5000/"

$( document ).ready(function() { 
$.getJSON(endpoint + "person", function(data) { 
  console.log(data);
  //$( "p" ).text( "The DOM is now loaded and can be manipulated." );
  $( "p" ).text( data.name );
});
});
