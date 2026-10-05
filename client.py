"""Generative Engine Optimization (GEO) & Citation Scorer.
100% Python Standard Library.
"""

class GEOCitationScorer:
    """Analyzes text content for AI citation visibility, structured statements, and statistical credibility."""
    
    @staticmethod
    def audit_geo_readiness(text: str) -> dict:
        score = 0
        factors = []
        
        has_stats = any(char.isdigit() for char in text) and any(kw in text for kw in ["%", "percent", "$", "increased", "latency", "benchmark"])
        if has_stats:
            score += 35
            factors.append("Includes concrete benchmarks/statistics (+35)")
            
        if any(kw in text.lower() for kw in ["is defined as", "refers to", "specifically", "architecture consists of"]):
            score += 25
            factors.append("Contains direct conceptual definition statements (+25)")
            
        if "\n-" in text or "\n*" in text or any(f"\n{i}." in text for i in range(1, 10)):
            score += 25
            factors.append("Structured hierarchically with bullet points (+25)")
            
        if "?" in text:
            score += 15
            factors.append("Matches natural-language conversational queries (+15)")
            
        score = min(score, 100)
        verdict = "High AI Citation Probability" if score >= 75 else ("Moderate Probability" if score >= 50 else "Low Citation Readiness")
        
        return {
            "geo_score": score,
            "verdict": verdict,
            "optimization_factors": factors,
            "recommendation": "Ready for indexing in Perplexity/ChatGPT/Genspark knowledge graphs." if score >= 75 else "Add explicit quantitative claims and definitions."
        }
