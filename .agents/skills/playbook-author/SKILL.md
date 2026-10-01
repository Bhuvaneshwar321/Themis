---
name: playbook-author
description: Drafts and verifies human-in-the-loop playbooks for specific legal scenarios.
---
# Skill: Playbook Authoring

## Purpose
Creates structured YAML playbooks that provide immediate, verified "first steps" for the 5 core scenarios.

## Steps
1. **Draft YAML:** Create a playbook in `data/playbooks/<id>.yaml` for the scenario.
2. **Populate Fields:** Fill out triggers, immediate steps, rights, limits, and help links (referenced from `helplines.yaml`).
3. **Cite Sources:** Ensure every claim in `rights` or `immediate_steps` maps to an ingested chunk ID.
4. **Human Verification:** The playbook MUST be verified by a human (and ideally a legal-aid volunteer) against official texts. 
5. **Update Status:** Change `verification.status` from `draft` to `self_verified` or `reviewed`.

## Inputs
- Legal chunks and official source text.
- `helplines.yaml` for verified contact numbers.

## Outputs
- `data/playbooks/<id>.yaml` adhering to the playbook schema.

## Checks
- Every citation resolves to a real chunk ID.
- Status is never `draft` in production.
- Helplines are verified.
