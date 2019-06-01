<template>
    <div id="container"></div>
</template>

<script>
import * as Three from 'three'
import * as d3 from 'd3';
import KanyeData from '../data/kanye_west.json';
import _ from 'lodash';

export default {
  name: 'ThreeTest',
  data() {
    return {
      camera: null,
      scene: null,
      renderer: null,
      mesh: null,
      objects: [],
    }
  },
  methods: {
    init() {
        let container = document.getElementById('container');
        this.camera = new Three.PerspectiveCamera(75, container.clientWidth/container.clientHeight, .1, 1000);
        this.camera.position.z = 1000;
        this.camera.position.x = 300
        this.camera.position.y = 300
        this.scene = new Three.Scene();
        // this.scene.background = new Three.Color(0xf0f0f0)
        let light = new Three.AmbientLight( 0x0f0f0f ); // soft white light
        this.scene.add( light );

        let lamp = new Three.SpotLight(0xffffff, 1.5)
        lamp.position.set(0, 500, 2000)

        this.scene.add(lamp)

        let geometry = new Three.SphereGeometry(10, 10, 10)

        let data = _.groupBy(KanyeData, 'album')
        console.log(Object.keys(data))
        let subData = KanyeData
      
        let xScale = d3.scaleBand()
          .domain(Object.keys(data))
          .range([0, 750])

        let yScale = d3.scaleLinear()
          .domain([0, 1])
          .range([700, 0])

        let zScale = d3.scaleLinear()
          .domain([0, 1])
          .range([700, 0])

        for (let i = 0; i < subData.length; i++) {
          let color = this.getAlbumColor(subData[i].album)
          let object = new Three.Mesh(geometry, new Three.MeshLambertMaterial({ color: color}))
          
          object.position.x = xScale(subData[i].album)
          object.position.y = yScale(subData[i].energy)
          object.position.z = zScale(subData[i].speechiness)

          object.castShadow = true;
          object.receiveShadow = true;
          
          this.scene.add(object);
          this.objects.push(object);
        }
        var axesHelper = new Three.AxesHelper( 1000 );
        this.scene.add( axesHelper );
        // material = new Three.LineBasicMaterial( { color: 0x0000ff } );
        // geometry = new Three.Geometry();
        // geometry.vertices.push(new Three.Vector3( 0, 0, 0) );
        // geometry.vertices.push(new Three.Vector3( 1,0,0) );
        // geometry.vertices.push(new Three.Vector3( 0,1,0) );
        // geometry.vertices.push(new Three.Vector3( 0,0,1) );
        // let line = new Three.Line( geometry, material );
        // this.scene.add( line );
        this.renderer = new Three.WebGLRenderer({antialias: true});
        this.renderer.setSize(container.clientWidth, container.clientHeight);
        container.appendChild(this.renderer.domElement);
        this.renderer.render(this.scene, this.camera);

    },
    animate() {
        requestAnimationFrame(this.animate);
        this.mesh.rotation.x += 0.01;
        this.mesh.rotation.y += 0.02;
        this.renderer.render(this.scene, this.camera);
    },
    getAlbumColor(album) {
      if (!album) {
        console.log(album)
      }
      let colorList = [
        '#a6cee3',
        '#1f78b4',
        '#b2df8a',
        '#33a02c',
        '#fb9a99',
        '#e31a1c',
        '#fdbf6f',
        '#ff7f00',
        '#cab2d6',
        '#6a3d9a'
      ]
      if (album === 'KIDS SEE GHOSTS') {
        return colorList[0]
      } else if (album === 'ye') {
        return colorList[1]
      } else if (album === 'The Life Of Pablo') {
        return colorList[2]
      } else if (album === 'Yeezus') {
        return colorList[3]
      } else if (album === 'Kanye West Presents Good Music Cruel Summer') {
        return colorList[4]
      } else if (album === 'My Beautiful Dark Twisted Fantasy') {
        return colorList[5]
      } else if (album === '808s & Heartbreak') {
        return colorList[6]
      } else if (album === 'Graduation') {
        return colorList[7]
      } else if (album === 'Late Registration') {
        return colorList[8]
      } else if (album === 'The College Dropout') {
        return colorList[9]
      }
    }
  },
  mounted() {
      this.init();
      // this.animate();
  }
}
</script>

<style>
#container {
  height: 100%
}
</style>

