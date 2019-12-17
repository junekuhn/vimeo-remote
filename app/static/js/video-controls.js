AFRAME.registerComponent('video-controls', {
  init: function() {
    this.video = document.querySelector(this.el.getAttribute('src'));
    
    this.video.preload = 'auto';
    
    var myVideo = this.video;
    
    this.video.addEventListener('canplaythrough', function() {
      console.log('canplaythrough');
    });
    
    this.video.addEventListener('loadeddata', function() {
      console.log('loadeddata');
      
    }); 
    
    this.video.addEventListener('progress', function() {
      console.log('progress');
      
    });
      
  }
//    
//    tick: function() {
//        var quat = document.getElementById('camera').object3D.getWorldQuaternion(new THREE.Quaternion());
//        var oil = new THREE.Euler();
//        oil = oil.setFromQuaternion(quat, 'YZX');
//        
//        console.log(oil);
//        //this one seems to work
//    }
});

AFRAME.registerComponent('playing',{
  init: function() {
    this.video = document.querySelector(this.el.getAttribute('src'));
    this.video.play();
  }
})





// AFRAME.registerComponent('preloading', {
//   init: function() {
//     //control for what type of element
//     this.video = document.querySelector(this.el.getAttribute('src'))

//     this.video.load()
//     this.video.play()
//     // if ( this.video.readyState === 4 ) { this.video.play() }
//   },
  
//   tick: function() {
//   // console.log(this.video.readyState)
  
// }
// });