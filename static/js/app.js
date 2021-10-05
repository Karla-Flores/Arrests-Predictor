




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
        
        
        // console.log(data)
        console.log(data['result'])
        console.log(data['prob'])
    
    })
});

