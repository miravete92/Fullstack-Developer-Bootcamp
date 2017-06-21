var numclicks = 0;
var state = {cats:[
	{name:"Bob",clicks:0,image:"img/cat1.jpg"},
	{name:"Linda",clicks:0,image:"img/cat2.jpg"}
]};

function setupCats(){
	for(var i = 0; i<state.cats.length;i++){
		var cathtml = "<div id='cat'>"+
			"<h3 id='cat-name'>"+state.cats[i].name+"</h3>"+
			"<img src='"+state.cats[i].image+"' alt='Cat image'/>"+
			"<span id='click-count'>"+state.cats[i].clicks+"</span>"+
		"</div>";
		$('main').append(cathtml);
	}
}
function handleClicks(){
	$('#cat').click(function(e) {
	  numclicks ++;
	  console.log("click");
	  $('#click-count').text(numclicks);
	});
}
$(function(){
	console.log("ready");
	setupCats();
	handleClicks();
});