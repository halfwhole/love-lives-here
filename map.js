// Set up the map
const map = L.map('map').setView([1.35, 103.82], 12);

L.tileLayer('http://a.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png', {
    attribution: '',
    minZoom: 11,
    maxZoom: 18
}).addTo(map);

// Initialize SVG layer and group
L.svg().addTo(map);

// Select SVG layer and group from map
const svg = d3.select('#map').select('svg');
const g = svg.select('g');
const layerGroup = L.layerGroup().addTo(map);

function update(entries) {
    function updateEntry(entry) {
        const coords = entry['geometry']['coordinates'];
        const latlng = new L.LatLng(coords[1], coords[0]);

        const props = entry['properties'];
        const colour = props['colour'];
        const message = props['message'];
        const name = props['name'];

        const zoomLevel = map.getZoom();

        L.circleMarker(latlng, {
            radius: 2 + (zoomLevel - 12) * 0.5,
            color: colour,
            weight: 7 + (zoomLevel - 12),
            opacity: 0.2,
            fillColor: colour,
            fillOpacity: 1
        }).addTo(layerGroup).on('click', () => clickHandler(message, name, coords));
    }

    function clickHandler(message, name, coords) {
        // TODO
        console.log(message);
        console.log(name);
        console.log(coords);
        d3.select('#bottomText').text('hi');
    }

    layerGroup.clearLayers();
    entries.forEach(entry => updateEntry(entry));
}


fetch('data.json').then(res => res.json()).then(data => {
    const entries = data['features'].slice(0, 10000);
    map.on('zoom', () => update(entries));
    update(entries);

        // const layerPoints = points.map(pt => map.latLngToLayerPoint(pt));
        // svg.selectAll('g').remove();
        // const svgPoints = svg.selectAll('g')
        //     .data(layerPoints)
        //     .enter()
        //     .append('g')
        //     .append('circle')
        //     .attr('transform', (pt) => 'translate(' + pt.x + ',' + pt.y + ')')
        //     .attr('fill', 'pink')
        //     .attr('r', 2);

    // function addPopupContent(feature, layer) {
    //     layer.bindPopup("<h3>" + feature.properties.name + "</h3>" +
    //                     "<p>" + feature.properties.message + "</p>");
    // }

    // function pointToLayer(feature, latlng) {
    //     return L.marker([latlng['lat'], latlng['lng']]);
    // }
});
