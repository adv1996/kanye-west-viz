<template>
  <v-app>
    <!-- <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Kanye West</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar> -->

    <v-content>
      <Albums/>
    </v-content>
  </v-app>
</template>

<script>
import ScatterPlot from './components/ScatterPlot';
import Albums from './components/Albums';
// import BarCodes from './components/BarCodes'
import Graph from './components/Graph';

export default {
  name: 'App',
  components: {
    ScatterPlot,
    Albums,
    Graph,
  },
  data () {
    return {
      //
    }
  }
}
</script>
