# Upstream: alchaincyf/huashu-design

- Source: https://github.com/alchaincyf/huashu-design  (License: MIT, see LICENSE)
- Vendored: `SKILL.md` + all `references/*.md` (design knowledge).
- Left upstream (~60MB, grab if you need the render/export pipeline): `assets/` (iOS frames, animation engine, slide system), `demos/` (GIF/MP4/HTML examples), `scripts/` (video render, PPTX export), `package.json`.
- Note: some references point at those assets/scripts. The design guidance stands alone; for actual PPTX/MP4 export tooling, clone upstream: `git clone --depth 1 https://github.com/alchaincyf/huashu-design`.
- **Trimmed 2026-09-26:** the 17 video/animation references (animation, camera, GSAP, SFX/audio, voiceover, launch film, video export, HyperFrames backend) were removed; they crowded out `../motion-design/` and `../emil/` in search and duplicated the `hyperframes` skill. Any remaining mention of them in `SKILL.md` refers to upstream. For video, use `hyperframes` + `../motion-design/` + `../emil/`.
