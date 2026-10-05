"""Example usage for GEO & Citation Scorer."""
from client import GEOCitationScorer

if __name__ == "__main__":
    doc = """How does autonomous tool repair improve reliability?
Tool repair is defined as runtime schema rectification.
Key performance gains:
- 99.4% tool execution recovery rate.
- Reduces pipeline interruptions by 80%."""
    res = GEOCitationScorer.audit_geo_readiness(doc)
    print("GEO Score:", res["geo_score"])
    print("Verdict:", res["verdict"])
    for f in res["optimization_factors"]:
        print("-", f)
