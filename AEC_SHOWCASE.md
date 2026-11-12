# AEC Document Agent

Attributed fork of [langchain-ai/retrieval-agent-template](https://github.com/langchain-ai/retrieval-agent-template), MIT licensed. Upstream built the indexing/retrieval graphs and integrations. Original license and upstream documentation are retained.

## My additions

- Adapted the actual default response/search prompts in `src/retrieval_graph/prompts.py` for AEC evidence, revision conflicts, missing facts, and draft-only behavior.
- Added a synthetic historic-library corpus with a specification revision conflict, an open RFI, and a meeting action.
- Added five manual evaluation cases and a credential-free configuration generator.
- Added a setup, access-control, evaluation, and handover guide in [aec/README.md](aec/README.md).

This is a customized agent starter. Live retrieval and LLM accuracy have not been tested. Prompt instructions are not security enforcement. The upstream graph's `user_id` filter is not a complete authenticated project-access model. All examples use synthetic data and generic project labels.

[Portfolio overview](https://github.com/alirida9988/aec-automation-showcase)
