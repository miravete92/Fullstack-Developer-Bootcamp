
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');
	var cityStr = $('#city').val();
	var $streetStr = $('#street').val();
	
	var URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json?" + $.param({
		'api-key': "01cf633e6a954887ac288fcacf7eac14",
		'q': cityStr,
		'sort':'newest'
	});

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview
	$body.append('<img class="bgimg" src="http://maps.googleapis.com/maps/api/streetview?size=600x300&location='+
		cityStr+','+$streetStr+'">');
    
	$('#nytimes-header').text('New York Times Articles about '+cityStr);
	
	$.getJSON(URL, function(data){
		data.response.docs.forEach(function(row){
			$nytElem.append('<li id="class">'+
			'<a href="'+row.web_url+'">'+row.headline.main+'</a>'+
			'<p>'+row.lead_paragraph+'</p>'+
			'</li>');
		});
	}).error(function(errorlog){
		console.log(errorlog);
	});
	
	var wikiRequestTimeout = setTimeout(function(){
		$wikiElem.text("failed to get wikipedia resources");
	},8000);
	$.ajax( {
		url: "https://en.wikipediaaaaaaaa.org/w/api.php",
		data: "action=opensearch&search="+cityStr+"&format=json",
		dataType: 'jsonp',
		success: function(data) {
		   var articles = data[1];
		   articles.forEach(function(article){
			   $wikiElem.append("<li><a href='http://en.wikipedia.org/wiki/"+article+"'>"+article+"</a></li>")
		   });
		   clearTimeout(wikiRequestTimeout);
		}
	} );

    return false;
};

$('#form-container').submit(loadData);
