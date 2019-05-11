<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout row wrap>
      <v-flex v-for="album in albums" :key="`6${album.name}`" xs12>
        <v-card>
          <div v-if="album.name === 'The College Dropout'" class="title-kw">
            <p class="title pt-2 pl-3">Average Color of a Second in a Kanye West Music Video</p>
          </div>
          <v-layout row wrap>
            <v-flex xs3>
              <p class="title font-weight-black pl-5">{{album.song}}</p>
              <p class="title font-weight-light pl-5">{{album.name}}</p>
              <p class="caption font-weight-light pl-5">{{album.date}}</p>
            </v-flex>
            <v-flex xs4>
              <v-img :src="album.img" height="100" width="400"/>
            </v-flex>
            <v-flex xs2>
              <v-img :src="album.thumbnail" height="100" width="100"/>
            </v-flex>
          </v-layout>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    data() {
      return {
        albums: [
          {
            name: 'The College Dropout',
            img: require('../assets/Kanye_BarCodes/jesuswalks.jpg'),
            song: 'Jesus Walks',
            thumbnail: 'https://img.youtube.com/vi/MYF7H_fpc-g/sddefault.jpg',
            date: '02/10/2004'
          },
          {
            name: 'Late Registration',
            img: require('../assets/Kanye_BarCodes/golddigger.jpg'),
            song: 'Gold Digger',
            thumbnail: 'https://img.youtube.com/vi/6vwNcNOTVzY/sddefault.jpg',
            date: '08/30/2005',
          },
          {
            name: 'Graduation',
            img: require('../assets/Kanye_BarCodes/stronger.jpg'),
            song: 'Stronger',
            thumbnail: 'https://img.youtube.com/vi/PsO6ZnUZI0g/sddefault.jpg',
            date: '09/11/2007',
          },
          {
            name: '808s & Heartbreak',
            img: require('../assets/Kanye_BarCodes/heartless.jpg'),
            song: 'Heartless',
            thumbnail: 'https://img.youtube.com/vi/Co0tTeuUVhU/sddefault.jpg',
            date: '11/24/2008',
          },
          {
            name: 'My Beautiful Dark Twisted Fantasy',
            img: require('../assets/Kanye_BarCodes/runaway.jpg'),
            song: 'Runaway',
            thumbnail: 'https://img.youtube.com/vi/Bm5iA4Zupek/sddefault.jpg',
            date: '11/22/2010',
          },
          {
            name: 'Watch the Throne',
            img: require('../assets/Kanye_BarCodes/otis.jpg'),
            song: 'Otis',
            thumbnail: 'https://img.youtube.com/vi/BoEKWtgJQAU/sddefault.jpg',
            date: '08/08/2011',
          },
          {
            name: 'Cruel Summer',
            img: require('../assets/Kanye_BarCodes/mercy.jpg'),
            song: 'Mercy',
            thumbnail: 'https://img.youtube.com/vi/7Dqgr0wNyPo/sddefault.jpg',
            date: '09/14/2012',
          },
          {
            name: 'Yeezus',
            img: require('../assets/Kanye_BarCodes/bound2.jpg'),
            song: 'Bound 2',
            thumbnail: 'https://img.youtube.com/vi/BBAtAM7vtgc/sddefault.jpg',
            date: '06/18/2013',
          },
          {
            name: 'The Life of Pablo',
            img: require('../assets/Kanye_BarCodes/fade.jpg'),
            song: 'Fade',
            thumbnail: 'https://img.youtube.com/vi/IxGvm6btP1A/sddefault.jpg',
            date: '02/14/2016',
          }
        ]
      }
    },
  }
</script>

<style>
  .barCode {
    margin-top: 10px
  }
  .title-kw {
    margin-left: 200px
  }
</style>


