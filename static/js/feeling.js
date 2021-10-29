// By Roni Kaufman

let kMax; // maximal value for the parameter "k" of the blobs
let step = 0.01; // difference in time between two consecutive blobs
let n = 100; // total number of blobs
let radius = 0; // radius of the base circle
let inter = 0.05; // difference of base radii of two consecutive blobs
let maxNoise = 500; // maximal value for the parameter "noisiness" for the blobs



//let noiseProg = (x) => (x);

function windowResized(){
  resizeCanvas(windowWidth, windowHeight);
  canvasSetup();
}

function setup() {
  let canvas = createCanvas(windowWidth, windowHeight);
  colorMode(RGB, 255);
	angleMode(DEGREES);
  noFill();
	//noLoop();
	kMax = random(0.6, 1.0);
	noStroke();
  canvas.position(0,0);
  canvas.style('z-index', '-1');
}

function draw() {
  background(255, 255, 255);
  let t = frameCount/100;
  for (let i = n; i > 0; i--) {
		let alpha = 255 - (i / n)*255;
		fill(208, 255, 60, alpha);
		let size = radius + i * inter;
		let k = kMax * sqrt(i/n);
		let noisiness = maxNoise * (i / n);
    blob(size, width/2, height/2, k, t - i * step, noisiness);
  }
}

// Creates and draws a blob
// size is the radius (before noise) of the base circle
// (xCenter, yCenter) is the position of the center of the blob
// k is the tightness of the blob (0 = perfect circle, higher = more spiky)
// t is the time
// noisiness is the magnitude of the noise (i.e. how far it streches out)
function blob(size, xCenter, yCenter, k, t, noisiness) {
  beginShape();
	let angleStep = 360 / 10;
  for (let theta = 0; theta <= 360 + 2 * angleStep; theta += angleStep) {
    let r1, r2;
		/*
    if (theta < PI / 2) {
      r1 = cos(theta);
      r2 = 1;
    } else if (theta < PI) {
      r1 = 0;
      r2 = sin(theta);
    } else if (theta < 3 * PI / 2) {
      r1 = sin(theta);
      r2 = 0;
    } else {
      r1 = 1;
      r2 = cos(theta);
    }
		*/
		r1 = cos(theta)+1;
		r2 = sin(theta)+1; // +1 because it has to be positive for the function noise
    let r = size + noise(k * r1,  k * r2, t) * noisiness;
    let x = xCenter + r * cos(theta);
    let y = yCenter + r * sin(theta);
    curveVertex(x, y);
  }
  endShape();
}