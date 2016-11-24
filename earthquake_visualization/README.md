

## Earthquakes around the world visualization

In this visualization we plot all the significant earthquakes around the world since the year 1900s. We wanted the visualization user to have freedom as to how to explore the data. We provide a map and a scatter plot below which allows the user to scroll to the dates and places she/he might be interested in.


### About the data
obtained from the Significance Earthquake database collected by the National Centers for Environmental Information and available [here](https://www.ngdc.noaa.gov/metaview/page?xml=NOAA/NESDIS/NGDC/MGG/Hazards/iso/xml/G012153.xml&view=getDataView&header=none). You can check [here](https://github.com/jlcoto/Udacity/tree/master/earthquake_project) the codebook as well as the exploratory analysis we conducted.


## Design
Our purpose was to give the final user as much freedom as what the story he wants to build. The user can play with several features in our visualization. There two most relevant are geographic and time span: we use a library called leaflet allowing the user to pan/zoom to different parts of the world map to check the incidence of earthquakes. Additionally, we included a brush at the bottom which allows the user to select the period he might be interested in. We also used some animation, though we tried to keep it at a minimum. We did not want to meddle too much in the users' experience.

## Feedback

I asked three friends to evaluate the visualization. I also posted the visualization in the forums but, unfortunately, I did not get feedback. 

The feedback that I got was as follows. In my first visualization, I only have plotted the brush and the scatterplot. Someone correctly suggested that I should explore the geographic implications of earthquakes and use the lat/lon data to my advantage. I decided, correspondingly that I could include a map to my visualization.

Once I had done that, one friend notice that while the scatterplot was fairly interactive with the brush, the points of the map did not get updated with the selection in the brush. He suggested me to find a way for these two plots to tell the same story. I needed to find a way to connect these two plots. In the end, I found out the way of making the updates also work for the map.

The final tester was happy about the interaction but said that labels were lacking, making it difficult for the user to really engage with the data. He recommended me to appropriately label each point and to generate a legend for the map. He also notice that my axis were not labeled. 

You can see how the first plot in index_1, then I included sequentially the changes in index_final.

### First attempt

![first](https://cloud.githubusercontent.com/assets/7328852/20595247/7b6f9ae2-b239-11e6-8f29-69d1e9d0d666.png) 
![second](https://cloud.githubusercontent.com/assets/7328852/20595586/bb1240a4-b23a-11e6-8537-292b18a19149.png)

## Resources

1. Michael Bostock on how to combine leaflet and d3.js (https://bost.ocks.org/mike/leaflet/).
2. D3.js documentation (https://github.com/d3/d3/wiki).
3. Leaflet documentation and tutorials. (http://leafletjs.com/reference.html)
4. Example on how to plot circles in leaflet with d3.js (http://bl.ocks.org/d3noob/9267535).
5. Short tutorial on leaflet and d3.js (https://chriszetter.com/blog/2014/06/15/building-a-voronoi-map-with-d3-and-leaflet/).
