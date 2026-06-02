resume = input("Enter Resume Skills (comma separated): ").lower()
job_description = input("Enter Job Skills (comma separated): ").lower()

resume_skills = {skill.strip() for skill in resume.split(",")}
job_skills = {skill.strip() for skill in job_description.split(",")}

matched_skills = resume_skills.intersection(job_skills)
missing_skills = job_skills - resume_skills

match_percentage = (len(matched_skills) / len(job_skills)) * 100

print("\n===== Resume Analysis Report =====")
print("Match Percentage:", round(match_percentage, 2), "%")

print("\nMatched Skills:")
for skill in matched_skills:
    print("-", skill)

print("\nMissing Skills:")
for skill in missing_skills:
    print("-", skill)