<template>
  <v-container fluid grid-list-md>
    <v-layout row wrap>
      <v-flex v-for="album in Object.keys(albums).length" :key="`album${album - 1}`" xs3>
        <v-card height="400">
          <Plot :name="`album${album - 1}`" :data="albums[Object.keys(albums)[album - 1]]"/>
        </v-card>
      </v-flex>44
    </v-layout>
  </v-container>
</template>

<script>
  import _ from 'lodash';
  import * as d3 from 'd3';
  import KanyeData from '../data/kanye_west.json';
  import Plot from './Plot'

  export default {
    components: {
      Plot,
    },
    data() {
      return {
        albums: []
      }
    },
    mounted () {
      this.initData();
    },
    methods: {
      initData() {
        this.albums = _.groupBy(KanyeData, 'album')
      }
    },
  }
</script>

<style lang="scss" scoped>

</style>