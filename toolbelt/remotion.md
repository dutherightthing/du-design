# Remotion — programmatic video in React

**What:** Make videos in React/TypeScript — compose frames as components, render to MP4. High ceiling for data-driven or highly custom, parametric video.

**Use it when:** the project is **already a React/TS codebase** *and* needs programmatic generation (e.g. hundreds of personalized variants, tightly data-bound charts-as-video, reusing existing React components in a video).

**Do NOT default to it.** For Jerry's projects, HyperFrames is the default — it's lower friction and already known. Remotion means more code to write and maintain. Only choose it when the React/programmatic advantage is real and specific; otherwise use [HyperFrames](hyperframes.md).

**Install (per project):**
```bash
npm create video@latest
```

**Sketch:**
```tsx
import {useCurrentFrame, interpolate, AbsoluteFill} from 'remotion';

export const Title = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 20], [0, 1], {extrapolateRight: 'clamp'});
  return <AbsoluteFill style={{opacity, justifyContent: 'center', alignItems: 'center'}}>
    <h1>Hello</h1>
  </AbsoluteFill>;
};
```

**Motion quality** still comes from [`../principles/motion.md`](../principles/motion.md) + the motion-design skill, not from Remotion itself.
