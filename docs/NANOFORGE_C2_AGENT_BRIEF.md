# NanoForge-C2 agent brief

Write NanoForge-C2 inside the existing FalsifyPhys repo.

## Goal

Build a CPU-first, web-native mechanosynthesis protocol planner for the CBNNT C2-on-H:Si(100) paper.

The model must not use Colab. It must run locally through the repo and open a browser-native molecular/protocol viewer.

## Source repos to inspect

- https://github.com/SakanaAI/ShinkaEvolve
- https://github.com/cusp-ai-oss/kups
- https://github.com/cusp-ai-oss/tojax
- https://github.com/TorchSim/torch-sim
- https://github.com/ACEsuit/mace
- https://github.com/facebookresearch/fairchem
- https://github.com/microsoft/mattergen
- https://github.com/microsoft/mattersim
- https://github.com/orbital-materials/orb-models
- https://github.com/materialsproject/pymatgen
- https://github.com/learningmatter-mit/NeuralForceField
- https://github.com/OpenOPC/OpenILT
- https://github.com/shelljane/lithobench
- https://github.com/ShiningSord/TorchResist

## What to implement now

Implement only the first runnable wedge:

1. paper-calibrated C2 mechanosynthesis operation grammar
2. probabilistic transition simulator
3. candidate protocol enumeration for IR-C2, 2IR-C2, IR-C2/C4, 2IR-C4
4. Monte Carlo evaluator
5. fast ranking heuristic
6. ShinkaEvolve task that mutates only fast ranking/compression code
7. web-native molecular/protocol viewer

## Interface separation

There are two UIs:

1. Molecular/protocol viewer: shows molecule/state/protocol output.
2. ShinkaEvolve code UI/results: shows mutation prompts, candidate code, and scores.

Do not mix these. Shinka output is code-search evidence, not molecular visualization.

## ShinkaEvolve command

Use the Codex headless backend:

```bash
shinka_run \
  --task-dir src/falsify/nanoforge_c2/shinka \
  --results_dir results/nanoforge_c2_headless \
  --num_generations 5 \
  --max-evaluation-jobs 1 \
  --max-proposal-jobs 1 \
  --set evo.llm_models='["headless/codex@gpt-5.5?effort=high"]' \
  --set evo.embedding_model=null \
  --set evo.patch_types='["full", "diff"]' \
  --set evo.patch_type_probs='[0.5, 0.5]'
```

## Do not do

- Do not use a generic main model provider for Shinka mutations.
- Do not claim DFT, STM, or QM/MM truth.
- Do not use MatterGen/MACE/TorchSim as the first loop.
- Do not route molecule viewing through the Shinka code UI.
- Do not mutate paper priors or immutable tests.
