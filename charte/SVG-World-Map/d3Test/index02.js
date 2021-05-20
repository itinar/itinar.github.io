var illustration;
var svg;
var svg2;
 Promise.all([
  illustration = d3.xml("http://192.168.1.151/charte/SVG-World-Map/src/world-states-provinces-stripes-test05.svg"),
])
.then(([mapleIllustration]) => {
		
  		
  		svg = d3.select(".maple-container")
  			.append("svg")
  					.attr("width",  460)
    				.attr("height",  460)
  			.node()
  				.append(mapleIllustration.documentElement)
  						
  		console.log('mapleIllustration');console.log(mapleIllustration);
  		
  		svg2 = d3.select(".maple-container")
  			.call(d3.zoom().on("zoom", function () {
     			svg2.attr("transform", d3.event.transform)
    		}))
  		console.log('svg2');console.log(svg2);
});