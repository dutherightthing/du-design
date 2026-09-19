# Motion & animation principles

Jerry's center of gravity. **Quality comes from these principles, not the engine.** GSAP, HyperFrames, and Remotion can all produce beautiful or amateur results — the direction decides which. For deep motion direction, load the **motion-design** skill (LottieFiles) via [`../skills/README.md`](../skills/README.md); this file is the fast reference.

## Motion has meaning
Every movement should have a *reason*: guide the eye, show a relationship, give feedback, set a mood. "Everything animates in" with no intent is the #1 motion slop. If a move doesn't serve the story or the user, cut it.

## Timing & easing
- **Ease almost everything.** Linear motion feels robotic. Use ease-out for things entering (fast in, settle), ease-in for things leaving, ease-in-out for moves between states.
- **Fast, not sluggish.** UI micro-interactions: ~150–300ms. Scene/element entrances in video: ~300–600ms. Anything over ~800ms had better be a deliberate, hero moment.
- **Stagger** groups of elements (~40–100ms apart) so they read as a sequence, not a blob.

## Choreography
- One thing leads; others follow. Establish a clear order of attention per moment — don't move everything at once.
- Motion should feel like it has weight and follow-through (Disney's 12 principles, adapted): anticipation before a big move, overshoot/settle on arrival, secondary motion for life.
- Match cut frequency to energy: fast cuts = energetic; long holds = calm. (Ties directly to the Calm↔Energetic intake slider.)

## Restraint (the Restrained↔Showy slider)
- **Restrained:** simple fades/slides, few moving parts, lots of hold time. Reads as elegant and confident.
- **Showy:** particles, 3D, camera moves, staggered chains. Reads as premium/hype but dates faster and is easy to overdo.
- Pick one motion idea and commit. Mixing five effect styles looks chaotic.

## Video-specific
- Cut on the beat if there's music; motion and audio should feel locked.
- Establish, then move: let a frame *land* before animating out of it. Give the viewer time to read.
- Text on screen must be readable long enough to read at a comfortable pace — then leave.
- Consistent motion language: if elements slide from the left early on, don't switch to spins later without reason.

## Web/UI-specific
- Micro-interactions confirm actions (button press, toggle, success) — quick and subtle.
- Scroll-driven motion (Lenis + GSAP ScrollTrigger) should reveal and pace content, not fight the user's scroll. Never hijack scroll speed to the point of disorientation.
- Respect `prefers-reduced-motion` — provide a calm fallback.

## Engine routing (see toolbelt cards)
- **Video / motion graphics →** [HyperFrames](../toolbelt/hyperframes.md) (default). [Remotion](../toolbelt/remotion.md) only if the project is already React + needs programmatic/data-driven video.
- **Interactive web animation →** [GSAP](../toolbelt/gsap.md) (+ [Lenis](../toolbelt/lenis.md) for smooth scroll), [three.js](../toolbelt/three.md) for 3D.
- **Lightweight shipped animations →** Lottie (JSON) for app/web micro-animations.

## Anti-slop for motion
- Everything fades/slides in for no reason, all at once.
- Linear easing; bounces on everything; wildly different speeds.
- Text that flies off before it can be read.
- Effects stacked because they're available, not because they serve the piece.
