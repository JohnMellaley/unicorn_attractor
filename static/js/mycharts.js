d3.queue()
    .defer(d3.json, "../getdata_bug")
    .defer(d3.json, "../getdata_feature")
    .defer(d3.json, "../getdata_bug_user" )
    .defer(d3.json, "../getdata_feature_user" )
    .defer(d3.json, "../bug_feature_count" )
    .await(makeGraphs);
    
   
function makeGraphs(error, graphData, graphData2, graphData3, graphData4, graphData5){
    var ndx = crossfilter(graphData); 
    var vote_dim = ndx.dimension(dc.pluck('name'));
    var votes_per_bug = vote_dim.group().reduceSum(dc.pluck('vote'));
    dc.barChart('#chart_user_likes')
             .width(600)
             .height(400)
             .margins({top: 10, right: 50, bottom: 70, left: 50})
             .useViewBoxResizing(true) 
             .dimension(vote_dim)
             .group(votes_per_bug)
             .transitionDuration(500)
             .x(d3.scale.ordinal())
             .xUnits(dc.units.ordinal)
             .xAxisLabel("Bug Name")
             .yAxis().ticks(4);
    
    var ndx = crossfilter(graphData2); 
    var feature_dim = ndx.dimension(dc.pluck('feature_name'));
    var votes_per_feature = feature_dim.group().reduceSum(dc.pluck('feature_vote'));
    
    dc.barChart('#chart_user_likes2')
             .width(600)
             .height(400)
             .margins({top: 10, right: 50, bottom: 70, left: 50})
             .useViewBoxResizing(true) 
             .dimension(feature_dim)
             .group(votes_per_feature)
             .transitionDuration(500)
             .x(d3.scale.ordinal())
             .xUnits(dc.units.ordinal)
             .xAxisLabel("Feature Name")
             .yAxis().ticks(4);        
    
    var ndx = crossfilter(graphData3); 
    var user_bug_dim = ndx.dimension(dc.pluck('author'));
    var count_user_bug_dim = user_bug_dim.group().reduceCount(dc.pluck('name'));
    
    dc.barChart('#chart_user_bug')
             .width(600)
             .height(400)
             .margins({top: 10, right: 50, bottom: 70, left: 50})
             .useViewBoxResizing(true) 
             .dimension(user_bug_dim)
             .group(count_user_bug_dim)
             .transitionDuration(500)
             .x(d3.scale.ordinal())
             .xUnits(dc.units.ordinal)
             .xAxisLabel("User Name")
             .yAxis().ticks(4);  
             
    var ndx = crossfilter(graphData4); 
    var user_feature_dim = ndx.dimension(dc.pluck('author'));
    var count_user_feature_dim = user_feature_dim.group().reduceCount(dc.pluck('name'));
    
    dc.barChart('#chart_user_feature')
             .width(600)
             .height(400)
             .margins({top: 10, right: 50, bottom: 70, left: 50})
             .useViewBoxResizing(true) 
             .dimension(user_feature_dim)
             .group(count_user_feature_dim)
             .transitionDuration(500)
             .x(d3.scale.ordinal())
             .xUnits(dc.units.ordinal)
             .xAxisLabel("User Name")
             .yAxis().ticks(4);
             
    var ndx = crossfilter(graphData5); 
    var bug_feature_dim = ndx.dimension(dc.pluck('name'));
    var count_bug_feature_dim = bug_feature_dim.group().reduceSum(dc.pluck('count'));
    dc.pieChart('#pie_bug_feature')
                .height(400)
                .radius(300)
                .transitionDuration(1500)
                .dimension(bug_feature_dim)
                .group(count_bug_feature_dim);
                
    dc.renderAll()
   
} 