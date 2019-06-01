<template>
  <div>
    <svg :id="name"/>
  </div>
</template>

<script>
  import _ from 'lodash';
  import * as d3 from 'd3';

  export default {
    props: ['name', 'data'],
    data() {
      return {
        height: null,
        width: null,
        margin: {top: 20, right: 20, bottom: 20, left: 25},
      }
    },
    mounted () {
      this.setDimensions();
      this.initGraph();
    },
    methods: {
      setDimensions() {
        this.width = this.$el.offsetWidth
        this.height = 400
      },
      initGraph() {
        const svg = d3.select('#' + this.name)
          .attr('height', this.height)
          .attr('width', this.width)
        
        const g = svg.append('g')
          .attr("transform", "translate(" + this.margin.left + "," + this.margin.top + ")")
        
        let xScale = d3.scaleLinear()
          .domain([0, 1])
          .range([0, this.width - this.margin.right - this.margin.left])

        let yScale = d3.scaleLinear()
          .domain([0, 1])
          .range([this.height - this.margin.top - this.margin.bottom, 0])

        g.append('g')
          .attr('class', 'albums')
          .selectAll('songs')
          .data(this.data)
          .enter().append('circle')
          .attr('class', 'albumSongs')
          .attr('cx', (d) => {
            return xScale(parseFloat(d.danceability))
          })
          .attr('cy', (d) => {
            return yScale(parseFloat(d.energy))
          })
          .attr('fill', 'orange')
          .attr('r', 5)
        
        let h = this.height - this.margin.top - this.margin.bottom
        g.append("g")
          .attr('class', 'xAxisLine')
          .attr("transform", "translate(0," + h + ")")
          .call(d3.axisBottom(xScale));

        g.append("g")
          .attr('class', 'yAxisLine')
          .call(d3.axisLeft(yScale));
        
        // album name
        g.append('text')
          .attr('x', this.margin.left)
          .attr('y', 0)
          .text(this.data[0].album)
        
        // x axis
        g.append('text')
          .attr('x', 0)
          .attr('y', this.height / 2)
          .text('Danceability')
        
        // y axis
        g.append('text')
          .attr('x', this.width / 2)
          .attr('y', this.height - 50)
          .text('Energy')
      }
    },
  }
</script>

<style lang="scss" scoped>

</style>