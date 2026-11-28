# Lean verification

In any pseudometric space, if the endpoints approach each other, the local arc has the stated unbounded distortion witnesses, and the complementary arc contains a fixed point separated from the limiting endpoint, Lean proves that no uniform two-arc bounded-turning constant exists. The construction of the common curve and the quasiconformality criterion remain in the paper.

The checked declaration is `TurningObstruction.no_uniform_turning`. [Source](Turning.lean) · [Pinned CI](../.github/workflows/lean.yml)

```sh
cd formalization
lake env lean -DwarningAsError=true Turning.lean
```

CI compares the compiler output with the committed axiom report.
