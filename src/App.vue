<template>
  <v-app>
    <!-- <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Kanye West</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar> -->

    <v-content>
      <BarCodes/>
    </v-content>
  </v-app>
</template>

<script>
// import ScatterPlot from './components/ScatterPlot'
import BarCodes from './components/BarCodes'

export default {
  name: 'App',
  components: {
    BarCodes
  },
  data () {
    return {
      //
    }
  }
}
</script>
