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
const dotsLayerGroup = L.layerGroup().addTo(map);
const iconLayerGroup = L.layerGroup().addTo(map);

function selectEntry(entry) {
    const coords = entry['geometry']['coordinates'];
    const latlng = new L.LatLng(coords[1], coords[0]);
    const props = entry['properties'];
    const message = props['message'];
    const name = props['name'];

    // Update textbox content
    d3.select('#textBoxHeader').text(name);
    d3.select('#textBoxContent').text(message);

    // Redraw icon marker
    iconLayerGroup.clearLayers();
    const icon = L.icon({
        iconUrl: 'static/pinkdoticon.png',
        iconSize: [36, 36],
        iconAnchor: [18, 18],
    })
    const iconMarker = L.marker(latlng, {
        icon: icon,
        interactive: false
    });
    iconMarker.addTo(iconLayerGroup);

    // Center on icon marker
    map.panTo(latlng);
}

function redrawMarkers(entries) {
    function drawMarker(entry) {
        const coords = entry['geometry']['coordinates'];
        const latlng = new L.LatLng(coords[1], coords[0]);
        const colour = entry['properties']['colour'];
        const zoomLevel = map.getZoom();
        const marker = L.circleMarker(latlng, {
            radius: 2 + (zoomLevel - 12),
            color: colour,
            weight: 7 + (zoomLevel - 12) * 2,
            opacity: 0.2,
            fillColor: colour,
            fillOpacity: 1
        });
        marker.addTo(dotsLayerGroup);
        marker.on('click', () => selectEntry(entry));
    }

    dotsLayerGroup.clearLayers();
    entries.forEach(entry => drawMarker(entry));
}

function shuffle(entries) {
    const randomIndex = Math.floor(Math.random() * entries.length);
    const randomEntry = entries[randomIndex];
    selectEntry(randomEntry);
}

fetch('data.json').then(res => res.json()).then(data => {
    const entries = data['features'];
    redrawMarkers(entries);
    map.on('zoom', () => redrawMarkers(entries));
    document.getElementById('textBoxShuffle').addEventListener('click', () => shuffle(entries));
});
