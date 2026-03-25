const image = document.querySelector(".image-container");
const position = { x: 0, y: 0 };
const screenSizes = {
  get width() {
    return window.innerWidth;
  },
  get height() {
    return window.innerHeight;
  },
};
const speed = { x: 3, y: 4 };
let hueRotation = 0;

function rotateHue(image) {
  const minHueRotation = 120;
  const maxHueRotation = 240;
  hueRotation =
    Math.floor(
      Math.random() * (maxHueRotation - minHueRotation) + minHueRotation,
    ) % 360;
  image.style.filter = `hue-rotate(${hueRotation}deg)`;
}

function processAxisMovement(axisData) {
  let { position, speed, imageLength, screenLength } = axisData;
  let hasCollision = false;
  if (position + speed < 0 || position + imageLength + speed >= screenLength) {
    hasCollision = true;
    position = speed > 0 ? screenLength - imageLength : 0;
    speed *= -1;
  } else {
    position += speed;
  }
  return {
    position,
    speed,
    hasCollision,
  };
}

function render() {
  const xShift = processAxisMovement({
    position: position.x,
    speed: speed.x,
    imageLength: image.clientWidth,
    screenLength: screenSizes.width,
  });
  speed.x = xShift.speed;
  position.x = xShift.position;

  const yShift = processAxisMovement({
    position: position.y,
    speed: speed.y,
    imageLength: image.clientHeight,
    screenLength: screenSizes.height,
  });
  speed.y = yShift.speed;
  position.y = yShift.position;

  if (xShift.hasCollision || yShift.hasCollision) {
    rotateHue(image);
  }

  image.style.left = `${position.x}px`;
  image.style.top = `${position.y}px`;
  requestAnimationFrame(render);
}

render();
