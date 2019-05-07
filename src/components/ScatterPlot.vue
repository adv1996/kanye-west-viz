<template>
  <div>
    <svg id="scatterPlot"/>
    <v-container>
      <v-btn
        v-for="album in albums"
        :key="album"
        :color="album === albumSelected ? selected : notSelected"
        v-on:click="changeAlbum(album)"
      >
        {{album}}
      </v-btn>
      <br>
      <h3>X Axis</h3>
      <v-btn
        v-for="label in labels"
        :key="label.name"
        v-on:click="changeXAxis(label)"
        :color="label.name === xAxisLabel ? selected : notSelected"
      >
        {{label.name}}
      </v-btn>
      <h3>Y Axis</h3>
      <v-btn
        v-for="label in labels"
        :key="label.name + width"
        v-on:click="changeYAxis(label)"
        :color="label.name === yAxisLabel ? selected : notSelected"
      >
        {{label.name}}
      </v-btn>
    </v-container>
  </div>
</template>

<script>
  import _ from 'lodash';
  import * as d3 from 'd3';
  import KanyeData from '../data/kanye_west.json';

  export default {
    data() {
      return {
        albumData: [],
        albums: [],
        width: 800,
        height: 500,
        margin: {top: 20, right: 20, bottom: 50, left: 120},
        xScale: null,
        yScale: null,
        selected: 'green',
        notSelected: 'white',
        albumSelected: '',
        labels: [
          {
            name: 'danceability',
            min: 0,
            max: 1,
          },
          {
            name: 'energy',
            min: 0,
            max: 1,
          },
          {
            name: 'loudness',
            min: -60,
            max: 0,
          },
          {
            name: 'speechiness',
            min: 0,
            max: 1,
          },
          {
            name: 'acousticness',
            min: 0,
            max: 1,
          },
          {
            name: 'instrumentalness',
            min: 0,
            max: 1,
          },
          {
            name: 'liveness',
            min: 0,
            max: 1,
          },
          {
            name: 'tempo',
            min: 0,
            max: 250,
          }
        ],
        xAxisLabel: 'danceability',
        yAxisLabel: 'energy',
      }
    },
    created() {
      this.setUpData()
    },
    mounted() {
      this.initChart()
    },
    methods: {
      changeAlbum(album) {
        this.albumSelected = album
        let a = this.albumData[album]
        let miniDataList = _.map(a, (d) => {
          return {
            name: d.name,
            energy: parseFloat(d['energy']),
            danceability: parseFloat(d['danceability']),
            loudness: parseFloat(d['loudness']),
            speechiness: parseFloat(d['speechiness']),
            acousticness: parseFloat(d['acousticness']),
            instrumentalness: parseFloat(d['instrumentalness']),
            liveness: parseFloat(d['liveness']),
            tempo: parseFloat(d['tempo'])
          }
        })
        let songs = d3.select('.albums').selectAll('circle')
          .data(miniDataList)
        
        songs.exit().remove()
        songs.enter().append('circle')
          .merge(songs)
            .transition()
            .duration(1000)
            .attr('cx', (d) => this.xScale(d[this.xAxisLabel]))
            .attr('cy', (d) => this.yScale(d[this.yAxisLabel]))
            .attr('fill', 'orange')
            .attr('class', 'albumSongs')
            .attr('r', 5)
      },
      initChart() {
        this.albums = Object.keys(this.albumData)
        // Albums: KIDS SEE GHOST, YE, The Life of Pablo, Yeezus, Kanye West Presents Good Music Cruel Summer, My Beautiful Dark Twisted Fantasy, 808s & Heartbreak, Graduation, Late Registration, The College Dropout
        this.albumSelected = 'The College Dropout'
        let album = this.albumData[this.albumSelected]
        let svg = d3.select('#scatterPlot')
          .attr('height', this.height + this.margin.top + this.margin.bottom)
          .attr('width', this.width + this.margin.left + this.margin.right)
        
        // set up default label values
        let xAxisLabel = this.xAxisLabel
        let yAxisLabel = this.yAxisLabel
        let miniDataList = _.map(album, (d) => {
          return {
            name: d.name,
            energy: parseFloat(d['energy']),
            danceability: parseFloat(d['danceability']),
            loudness: parseFloat(d['loudness']),
            speechiness: parseFloat(d['speechiness']),
            acousticness: parseFloat(d['acousticness']),
            instrumentalness: parseFloat(d['instrumentalness']),
            liveness: parseFloat(d['liveness']),
            tempo: parseFloat(d['tempo'])
          }
        })
        //margin controls
        const g = svg.append('g')
          .attr("transform", "translate(" + this.margin.left + "," + this.margin.top + ")")
        // xScale danceability
        this.xScale = d3.scaleLinear()
          .domain([0, 1])
          .range([0, this.width - this.margin.right - this.margin.left])
        
        this.yScale = d3.scaleLinear()
          .domain([0, 1])
          .range([this.height - this.margin.top - this.margin.bottom, 0])
        
        g.append('g')
          .attr('class', 'albums')
          .selectAll('songs')
          .data(miniDataList)
          .enter().append('circle')
          .attr('class', 'albumSongs')
          .attr('cx', (d) => this.xScale(d.danceability))
          .attr('cy', (d) => this.yScale(d.energy))
          .attr('fill', 'orange')
          .attr('r', 5)
          .on('mouseover', (d) => {
            console.log(d.name)
          })
        
        let h = this.height - this.margin.top - this.margin.bottom
        g.append("g")
          .attr('class', 'xAxisLine')
          .attr("transform", "translate(0," + h + ")")
          .call(d3.axisBottom(this.xScale));

        g.append("g")
          .attr('class', 'yAxisLine')
          .call(d3.axisLeft(this.yScale));

        g.append("text")
          .attr('class', 'yaxislabel')
          .attr("y", this.height / 2 - this.margin.top)
          .attr("x", -this.margin.left / 2)
          .attr("dy", "1em")
          .style("text-anchor", "middle")
          .text(yAxisLabel);
        
        g.append("text")
          .attr('class', 'xaxislabel')
          .attr("transform","translate(" + (this.width/2) + " ," + (this.height) + ")")
          .style("text-anchor", "middle")
          .text(xAxisLabel);
      },
      setUpData() {
        this.albumData = _.groupBy(KanyeData, 'album')
      },
      changeXAxis(label) {
        d3.select('.xaxislabel')
          .text(label.name)
        
        this.xScale.domain([label.min, label.max])

        d3.select('.xAxisLine')
          .call(d3.axisBottom(this.xScale))
        d3.selectAll('.albumSongs')
          .transition()
          .duration(1000)
          .attr('cx', (d) => {
            return this.xScale(d[label.name])
          })
        
        this.xAxisLabel = label.name
      },
      changeYAxis(label) {
        d3.select('.yaxislabel')
          .text(label.name)
        this.yScale.domain([label.min, label.max])

        d3.select('.yAxisLine')
          .call(d3.axisLeft(this.yScale));
        d3.selectAll('.albumSongs')
          .transition()
          .duration(1000)
          .attr('cy', (d) => {
            return this.yScale(d[label.name])
          })
        
        this.yAxisLabel = label.name
      }
    }
  }
  // need to make sure songs are getitng updating, deleted, and added correctly
  // be able to change the x axis and y axis labels
</script>

<style lang="scss" scoped>

</style>