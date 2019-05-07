<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Kanye West</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>

    <v-content>
      <ScatterPlot/>
    </v-content>
  </v-app>
</template>

<script>
import ScatterPlot from './components/ScatterPlot'

export default {
  name: 'App',
  components: {
    ScatterPlot
  },
  data () {
    return {
      //
    }
  }
}
</script>
