Promise.all([
  d3.xml("http://192.168.1.151/charte/SVG-World-Map/src/world-states-provinces-stripes-test05.svg")
]).then(([mapleIllustration, oakIllustration]) => {
  d3.select(".maple-container").nodes().forEach(n => {
    n.append(mapleIllustration.documentElement.cloneNode(true))
  });

});