// Set up the map
const map = L.map('map').setView([1.35, 103.82], 12);

L.tileLayer('http://a.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
    attribution: '',
    maxZoom: 17,
}).addTo(map);

// Initialize SVG layer and group
L.svg().addTo(map);

// Select SVG layer and group from map
const svg = d3.select('#map').select('svg');
const g = svg.select('g');

fetch('data.json').then(res => res.json()).then(data => {
    L.geoJSON(data, {
        onEachFeature: addPopupContent,
        pointToLayer: pointToLayer
    }).addTo(map);

    function addPopupContent(feature, layer) {
        layer.bindPopup("<h3>" + feature.properties.name + "</h3>" +
                        "<p>" + feature.properties.message + "</p>");
    }

    function pointToLayer(feature, latlng) {
        return L.marker([latlng['lat'], latlng['lng']]);
    }
});
