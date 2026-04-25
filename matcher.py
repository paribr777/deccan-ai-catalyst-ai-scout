def compute_match_score(candidate, jd):
    required_skills = set([s.lower() for s in jd.get("Skills", [])])
    candidate_skills = set([s.lower() for s in candidate.get("skills", [])])

    matched_skills = required_skills & candidate_skills
    missing_skills = required_skills - candidate_skills

    skill_overlap = len(matched_skills) / max(len(required_skills), 1)

    exp_required = jd.get("Experience", 0)
    exp_candidate = candidate.get("experience", 0)
    experience_match = min(exp_candidate / max(exp_required, 1), 1)

    score = 0.7 * skill_overlap + 0.3 * experience_match

    explanation = {
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "skill_overlap": round(skill_overlap, 2),
        "experience_match": round(experience_match, 2)
    }

    return score, explanation, len(matched_skills)
