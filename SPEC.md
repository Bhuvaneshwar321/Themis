# THEMIS - Project Specification

## Goals
- Build a polished, working, deployed portfolio project.
- Demonstrate: Proper RAG, hallucination control, evaluation, multilingual UX, security/privacy, clean engineering.
- Provide real utility to ordinary people, including low-bandwidth and first-time smartphone users.

## Non-Goals (for v1.0.0)
- Monetization or pitching.
- Acting as a lawyer or legal advice replacement.
- Automating government portals.
- User accounts, payments, or Redis.
- Voice support (stretch goal).

## Target Audience
- Ordinary Indian citizens facing common, stressful legal situations.
- Users who need plain language explanations in English, Tamil, or Hindi.

## Supported Scenarios (v1.0.0)
1. **Police Stop:** Driving-licence or vehicle seizure.
2. **FIR Refusal:** Refusal by police to register an FIR.
3. **Unpaid Wages:** Non-payment of wages by employer.
4. **Illegal Eviction:** Landlord-tenant dispute (Focus: Tamil Nadu).
5. **Cyber Fraud:** Online/financial scams.

## Success Metrics
- **Recall@5:** >= 80% on seed test queries.
- **Citation Validity:** 100% (No hallucinated citations; any answer failing this must be blocked by the verifier).
- **Refusal Accuracy:** Correctly refusing 100% of out-of-scope questions on the eval dataset.
- **Accessibility:** Lighthouse score >= 90.
- **Latency:** Acceptable p50/p95 times for streaming responses.
