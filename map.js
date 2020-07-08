// Set up the map
const map = L.map('map').setView([1.35, 103.82], 12);

L.tileLayer('http://a.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png', {
    attribution: '',
    maxZoom: 17,
}).addTo(map);

// Initialize SVG layer and group
L.svg().addTo(map);

// Select SVG layer and group from map
const svg = d3.select('#map').select('svg');
const g = svg.select('g');

fetch('data.json').then(res => res.json()).then(data => {
    // L.geoJSON(data, {
    //     onEachFeature: addPopupContent,
    //     pointToLayer: pointToLayer
    // }).addTo(map);

    // Get points in latitude/longitude format
    const points = data['features']
          .map(ft => ft['geometry']['coordinates'])
          .map(pt => new L.LatLng(pt[1], pt[0]));

    for (point of points) {
        L.circleMarker(point, {
            radius: 2,
            color: 'pink',
            weight: 7,
            opacity: 0.5,
            fillColor: 'pink',
            fillOpacity: 1
        }).addTo(map).bindPopup('marker')
    }

    // TODO: filter points

    // function update() {
    //     const layerPoints = points.map(pt => map.latLngToLayerPoint(pt));
    //     svg.selectAll('g').remove();
    //     const svgPoints = svg.selectAll('g')
    //         .data(layerPoints)
    //         .enter()
    //         .append('g')
    //         .append('circle')
    //         .attr('transform', (pt) => 'translate(' + pt.x + ',' + pt.y + ')')
    //         .attr('fill', 'pink')
    //         .attr('r', 2);
    // }

    // map.on('viewreset moveend', update);
    // update();

    // function addPopupContent(feature, layer) {
    //     layer.bindPopup("<h3>" + feature.properties.name + "</h3>" +
    //                     "<p>" + feature.properties.message + "</p>");
    // }

    // function pointToLayer(feature, latlng) {
    //     return L.marker([latlng['lat'], latlng['lng']]);
    // }
});
