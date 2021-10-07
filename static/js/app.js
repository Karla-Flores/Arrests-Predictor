




d3.select("#model_result").on("click", function(){
    let crime = d3.select("#crime_dropdown").property('value')
    let location = d3.select("#location_dropdown").property('value')
    let season = d3.select("#season_dropdown").property('value')
    let hour = d3.select("#hour_dropdown").property('value')
    let lat = d3.select("#lat_dropdown").property('value')
    let lon = d3.select("#lon_dropdown").property('value')
    let domestic = d3.select("#dom_dropdown").property('value')
    console.log(`127.0.0.1:5000/results/${crime}/${location}/${season}/${hour}/${lat}/${lon}/${domestic}`)
    d3.json(`/results/${crime}/${location}/${season}/${hour}/${lat}/${lon}/${domestic}`)

    .then(function(data){
        
        var arrest_prob = (data.prob[0][1]*100).toFixed()
        document.getElementById('arrest_prob').innerHTML = arrest_prob+" %"
        // console.log(data)()
        console.log(data.result)
        console.log(`probability of arrest is ${(data.prob[0][1]*100).toFixed(2)} %`)
        
    
    })
});

// const street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
// });

const myMap = L.map("map", {
    center: [
        15.6, -28.7
    ],
    zoom: 3
});

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);


// setTimeout(function() {map.invalidateSize()},1000)

// function initMap() {
//     const myLatlng = { lat: 25.34512195709302, lng: -89.8890446170271 };
//     const map = new google.maps.Map(document.getElementById('map'), {
//         zoom: 3,
//         center: myLatlng,
//         streetViewControl: false,
//         mapTypeId: 'terrain',
//         fullscreenControl: false,
//         mapTypeControl: false,
//     });
//     // Configure the click listener.
//     map.addListener('click', (mapsMouseEvent) => {
//         $('#lat').val(mapsMouseEvent.latLng.lat);
//         $('#lon').val(mapsMouseEvent.latLng.lng);
//     });
// }
