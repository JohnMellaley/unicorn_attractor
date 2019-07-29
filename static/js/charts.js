d3.queue()
    .defer(d3.json, 'getdata')
    .await(makeGraphs);
    
function makeGraphs(graphData){
    var dataSet = graphData;
    alert("I am in js charts");
    alert("test", dataSet);
   // var ndx = crossfilter(dataSet); 
    
    // Bar chart based on likes per recipe
  //  var vote_dim = ndx.dimension(dc.pluck('name'));
  //  var total_likes_per_recipe = vote_dim.group().reduceSum(dc.pluck('vote'));
    
  //  dc.barChart('#chart_user_likes2')
  //          .width(600)
 //           .height(400)
  //          .margins({top: 10, right: 50, bottom: 70, left: 50})
  //          .useViewBoxResizing(true) 
  //          .dimension(dish_dim)
  //          .group(total_likes_per_recipe)
  //          .transitionDuration(500)
  //          .x(d3.scale.ordinal())
  //          .xUnits(dc.units.ordinal)
  //          .xAxisLabel("Recipes")
  //          .yAxis().ticks(4);
   
} 