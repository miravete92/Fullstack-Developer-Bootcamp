var ViewModel = function() {
	var self = this;
	this.showSidebar = ko.observable(0);

	this.toogleSidebar = function(){		
		console.log("click");
		self.showSidebar(self.showSidebar()?0:1);
	}
}
ko.applyBindings(new ViewModel());

var map;
function initMap() { 
	map = new google.maps.Map(document.getElementById('map'),{
		center: {lat: 41.6669036,lng: -0.8846575},
		zoom: 13
	});
}