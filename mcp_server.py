"""MCP server for GEO & Citation Scorer."""
import sys
import json
from client import GEOCitationScorer

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "audit_geo_citation",
                "description": "Audits copy for Generative Engine Optimization and AI citation likelihood",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string"}
                    },
                    "required": ["text"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "audit_geo_citation":
            text = params.get("arguments", {}).get("text", "")
            res = GEOCitationScorer.audit_geo_readiness(text)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
