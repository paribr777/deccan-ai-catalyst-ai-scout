import streamlit as st
from parser import parser
from matcher import compute_match_score
from outreach import simulate_outreach
from scoring import score_interest
from loader import load_candidates

st.title("Catalyst AI Scouting Agent")
jd_text = st.text_area("Paste Job Description")

if st.button("Run Agent"):
    st.subheader("Parsing JD...")
    jd = parse_jd(jd_text)
    st.json(jd)

    candidates = load_candidates()

    results = []
    st.subheader("Matching Candidates...")

    for c in candidates:
        match_score, explanation = compute_match_score(c, jd)

        response = simulate_outreach(c)
        interest_score = score_interest(response)

        final_score = 0.7 * match_score + 0.3 * interest_score

        results.append({
            "name": c["name"],
            "match_score": round(match_score, 2),
            "interest_score": round(interest_score, 2),
            "final_score": round(final_score, 2),
            "explanation": explanation,
            "response": response
        })

    results = sorted(results, key=lambda x: x["final_score"], reverse=True)
    st.subheader("Shortlisted Candidates")

    for r in results:
        with st.expander(f"{r['name']} — Score: {r['final_score']}"):
            st.write("Match Score:", r["match_score"])
            st.write("Interest Score:", r["interest_score"])
            st.write("Explanation:", r["explanation"])
            st.write("Simulated Response:", r["response"])
