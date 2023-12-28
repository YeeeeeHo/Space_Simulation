// Create the scene and set the scene size.
var scene = new THREE.Scene();
var WIDTH = window.innerWidth,
    HEIGHT = window.innerHeight;

// Create a renderer and add it to the DOM.
var renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(WIDTH, HEIGHT);
document.body.appendChild(renderer.domElement);

// Create a camera, zoom it out from the model a bit, and add it to the scene.
var camera = new THREE.PerspectiveCamera(45, WIDTH / HEIGHT, 0.1, 20000);
camera.position.set(0, 6, 0);
scene.add(camera);

// Create a light, set its position, and add it to the scene.
var light = new THREE.PointLight(0xffffff);
light.position.set(-100, 200, 100);
scene.add(light);

// Add a white PointLight to the scene.
var pointLight = new THREE.PointLight(0xFFFFFF);
pointLight.position.set(200, 100, 200);
scene.add(pointLight);

// Create a sphere (planet) and add it to the scene.
var sphereGeometry = new THREE.SphereGeometry(1, 20, 20);
var sphereMaterial = new THREE.MeshLambertMaterial({ color: 0xCC0000 });
var sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
sphere.position.set(1, 1, 0);
scene.add(sphere);

// Add OrbitControls so that we can pan around with the mouse.
controls = new THREE.OrbitControls(camera, renderer.domElement);

// Renders the scene and updates the render as needed.
function animate() {
    requestAnimationFrame(animate);

    // Rotate the sphere
    sphere.rotation.x += 0.01;
    sphere.rotation.y += 0.01;
    sphere.rotation.z += 0.01;

    // Render the scene
    renderer.render(scene, camera);
    controls.update();
}

animate();
