d3.xml("http://192.168.1.151/charte/SVG-World-Map/src/world-states.svg").then(data => {
		d3.select(".maple-container").node().append(data.documentElement)
		var svg = d3.select('#Earth').call(d3.zoom().on("zoom", function(){
			svg.attr("transform", d3.event.transform)
		}));		
	});

  		
 