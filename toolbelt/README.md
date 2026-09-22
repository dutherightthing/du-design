# Toolbelt

Index cards for code libraries. **We do not vendor these** — they're huge and go stale. Each card says what a tool is for, when to reach for it vs. an alternative, the install line, and a canonical snippet or two. The agent reads the card, then installs the real library *into the project*.

## Quick routing

| I'm making... | Reach for |
|---|---|
| A video / motion graphic | [HyperFrames](hyperframes.md) (default) · [Remotion](remotion.md) (React-native, programmatic only) |
| An animated website | [GSAP](gsap.md) + [Lenis](lenis.md) (smooth scroll) · [three.js](three.md) (3D) |
| Web UI components | [shadcn/ui](shadcn.md) (primitives) · [react-bits](react-bits.md) (animated accents) · [Aceternity UI](aceternity.md) (big animated sections) |
| Icons — UI glyphs | [Hugeicons](hugeicons.md) |
| Icons — brand/logos | [SuperTinyIcons](super-tiny-icons.md) |
| Transition/motion inspiration | [transitions.dev](transitions.md) (reference, not a dep) |

**Don't know *which* source to pull from?** That's not a toolbelt question — see [`../sources/ROUTER.md`](../sources/ROUTER.md), which maps a design need (navbar? landing hero? icons? motion taste?) to the exact source and how to retrieve it (including sites the network policy blocks).

See also the medium principles in [`../principles/`](../principles/) and the motion skill in [`../skills/README.md`](../skills/README.md).
