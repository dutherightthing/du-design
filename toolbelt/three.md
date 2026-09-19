# three.js — 3D on the web

**What:** The standard WebGL 3D library — scenes, cameras, meshes, materials, lights, loaders, post-processing.

**Use it when:** a project genuinely benefits from 3D or GPU visuals — hero 3D objects, particle fields, shader backgrounds, product viewers, immersive scroll scenes. Not for flat UI motion (use [GSAP](gsap.md)) and not for standalone video (use [HyperFrames](hyperframes.md), which has a Three adapter).

**Weight warning:** 3D is heavy (bundle size + GPU + dev time). It must earn its place. Don't add a spinning cube for decoration. Budget performance (mobile especially) and provide a fallback.

**Consider first:** in React, **React Three Fiber** (`@react-three/fiber` + `@react-three/drei`) makes three.js far more ergonomic. Reach for it if the project is React.

**Install:**
```bash
npm i three
# React: npm i three @react-three/fiber @react-three/drei
```

**Sketch (vanilla):**
```js
import * as THREE from 'three';
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, innerWidth/innerHeight, 0.1, 100);
camera.position.z = 4;
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2)); // perf guard
renderer.setSize(innerWidth, innerHeight);
document.body.appendChild(renderer.domElement);
const mesh = new THREE.Mesh(new THREE.IcosahedronGeometry(1, 0),
  new THREE.MeshStandardMaterial({ color: 0x4f8cff, flatShading: true }));
scene.add(mesh, new THREE.DirectionalLight(0xffffff, 2), new THREE.AmbientLight(0xffffff, 0.3));
renderer.setAnimationLoop(() => { mesh.rotation.y += 0.005; renderer.render(scene, camera); });
```

Animate three.js with [GSAP](gsap.md) for controlled motion. See [`../principles/motion.md`](../principles/motion.md).
