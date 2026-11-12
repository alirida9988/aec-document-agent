"""Print a LangGraph configuration; no packages, credentials, or API calls needed."""
import argparse
import importlib.util
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--user-id', required=True, help='Demo namespace; never trust a browser-supplied identity in production')
parser.add_argument('--response-model', required=True, help='Approved provider/model identifier')
parser.add_argument('--query-model', required=True, help='Approved provider/model identifier')
parser.add_argument('--retriever', choices=['elastic', 'elastic-local', 'pinecone', 'mongodb'], default='elastic')
args = parser.parse_args()
if not args.user_id.strip() or any('/' not in model or not all(model.split('/', 1)) for model in [args.response_model, args.query_model]):
    parser.error('A nonempty namespace and provider/model identifiers are required')
path = Path(__file__).resolve().parents[1] / 'src/retrieval_graph/prompts.py'
spec = importlib.util.spec_from_file_location('aec_prompts', path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
print(json.dumps({'configurable': {
    'user_id': args.user_id,
    'response_model': args.response_model,
    'query_model': args.query_model,
    'retriever_provider': args.retriever,
    'response_system_prompt': module.RESPONSE_SYSTEM_PROMPT,
    'query_system_prompt': module.QUERY_SYSTEM_PROMPT,
}}, indent=2))
