var client_id = '5RUHSDHDQZKQZ3OCCAD4Y0IHFTVQDRCCXUWB4PXWKZRJIV0D';
var client_secret = 'NTKYK3KVQDMGPI1E3LHYSAZ3AL1JGENV513SLMKB0LDC3WTD';
var position = {lat: 41.6669036,lng: -0.8846575};

var Place = function(data, map){
	var self = this;
	this.name = ko.observable(data.name);
	this.location = ko.observable({lat: data.location.lat,lng: data.location.lng});
	this.marker = new google.maps.Marker({
		position: self.location(),
		map: map,
		title: self.name()
	});
}
var ViewModel = function() {
	var self = this;
	this.showSidebar = ko.observable(0);
	this.query = ko.observable("restaurante");
	this.placeList = ko.observableArray([]);

	this.toogleSidebar = function(){		
		console.log("click");
		self.showSidebar(self.showSidebar()?0:1);
	}
	this.findPlaces = function(){
		var url = 'https://api.foursquare.com/v2/venues/search?v=20161016&ll='+position.lat+'%2C%20'+position.lng+'&query='+self.query()+'&intent=checkin&client_id='+client_id+'&client_secret='+client_secret;
		$.getJSON(url, function(data) { 
			if(data.meta.code==200){
				self.placeList.removeAll();
				data.response.venues.forEach(function(locationItem){
					self.placeList.push(new Place(locationItem, map));
				});
			}
		    
		});
	}
}
ko.applyBindings(new ViewModel());

var map;
function initMap() { 
	map = new google.maps.Map(document.getElementById('map'),{
		center: position,
		zoom: 15
	});
}