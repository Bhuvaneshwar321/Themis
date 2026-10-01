---
name: eval-runner
description: Runs the evaluation dataset to measure retrieval and generation quality.
---
# Skill: Evaluation Runner

## Purpose
Measures the system's performance on recall, citation validity, and refusal accuracy to guarantee safety and correctness.

## Steps
1. **Prepare Dataset:** Ensure `eval/dataset.jsonl` has 60-100 items covering all scenarios, languages, and 10+ out-of-scope/must_refuse items.
2. **Run Evals:** Execute the eval script to test the retrieval pipeline and full generation pipeline.
3. **Generate Report:** Output metrics to a markdown/JSON report.

## Inputs
- `eval/dataset.jsonl` (schema: id, lang, scenario, question, expected_sections[], must_refuse, notes).

## Outputs
- `eval/report.md` (and JSON) containing:
  - recall@k
  - citation validity (must be 100%)
  - refusal accuracy
  - per-language breakdown
  - latency p50/p95

## Checks
- Citation validity is strictly 100%.
- Real numbers are populated in the README metrics table.
