var numclicks = 0;
var state = {cats:[
	{name:"Bob",clicks:0,image:"img/cat1.jpg"},
	{name:"Linda",clicks:0,image:"img/cat2.jpg"},
	{name:"Snowball",clicks:0,image:"img/cat3.jpeg"},
	{name:"Turquesa",clicks:0,image:"img/cat4.jpg"},
	{name:"Jeremy",clicks:0,image:"img/cat5.jpg"}
]};

function setupCats(){
	for(var i = 0; i<state.cats.length;i++){
		var cathtml = "<div class='cat'>"+
			"<div class='cat-head'><h3 class='cat-name'>"+state.cats[i].name+"</h3></div>"+
			"<img src='"+state.cats[i].image+"' alt='Cat image'/>"+
			"<span class='click-count'>"+state.cats[i].clicks+"</span>"+
		"</div>";
		$('main').append(cathtml);
	}
}
function handleClicks(){
	$('.cat').click(function(e) {
	  var catname = $(this).find(".cat-name").text();
	  var cat = state.cats.find(function(cat){
	  	return cat.name == this;
	  }, catname);
	  console.log(cat);
	  cat.clicks++;
	  $(this).find(".click-count").text(cat.clicks+"");
	});
}
$(function(){
	console.log("ready");
	setupCats();
	handleClicks();
});