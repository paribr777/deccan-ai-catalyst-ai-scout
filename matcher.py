def compute_match_score(candidate, jd):
    required_skills = jd.get("Skills", [])
    candidate_skills = candidate.get("skills", [])

    skill_overlap = len(set(required_skills) & set(candidate_skills)) / max(len(required_skills), 1)

    exp_required = jd.get("Experience", 0)
    exp_candidate = candidate.get("experience", 0)
    experience_match = min(exp_candidate / max(exp_required, 1), 1)

    score = 0.5 * skill_overlap + 0.5 * experience_match

    explanation = [
        f"Resume screened with results:"
        f"Matched {len(set(required_skills) & set(candidate_skills))}/{len(required_skills)} skills",
        f"Experience: {exp_candidate} vs required {exp_required}"
    ]

    return score, explanation
