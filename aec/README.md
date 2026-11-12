# Demonstrate specification and RFI lookup

## Offline configuration check

From the repository root, generate a configuration without loading LangChain or calling a provider:

```bash
python3 aec/build_config.py --user-id demo-library --response-model approved-provider/approved-model --query-model approved-provider/approved-query-model
```

The `approved-provider/...` values are illustrative placeholders, not working model names. Supply currently available model identifiers approved for the intended data when configuring a real service. The original upstream defaults name older models; do not assume they remain available.

## Configure an actual pilot

Follow the retained upstream README for environment and dependency setup. Select and provision one supported vector store. Set credentials in an untracked `.env` and confirm provider/model access. Use the config generator with real approved identifiers and pass the resulting `configurable` values to both graph calls as appropriate.

The `indexer` graph in `langgraph.json` accepts `{"docs": [...]}` with the entries in `documents.json`. Invoke it using the chosen configuration. The `retrieval_graph` accepts `{"messages": [{"role": "user", "content": "Can full-area masonry cleaning start?"}]}` with the same demo namespace. Check the current LangGraph runner's invocation method for the installed version. Index each synthetic corpus only once or implement stable document IDs/upserts before repeated ingestion.

The three documents all belong to the same synthetic project. Metadata includes source/revision/section for citations. Before real use, derive identity and authorized project scope server-side, enforce access during ingestion and retrieval, and verify isolation with adversarial tests. Do not use a caller-chosen `user_id` as authorization. Untrusted documents can contain malicious instructions; prompting alone cannot guarantee resistance.

## Evaluate

Run `evaluation-cases.json` manually against the live pilot. For each answer record source accuracy, factual support, revision handling, appropriate refusal/uncertainty, latency, and actual model cost. An expected answer in this file is a rubric, not a measured result. Test access isolation independently at the application and vector-store layers.

## Handover

Document how authorized staff add a revised document, retire old revisions, rerun the evaluation set, view retrieval errors, rotate service credentials, and restore the index. Name a process owner and maintainer. Keep writes, submissions, design approval, and external sends outside this Q&A pilot.
