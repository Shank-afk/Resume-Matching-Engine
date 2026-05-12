import math
import re

# ============================================================
# SKILL_ALIASES — Exact as provided
# ============================================================
SKILL_ALIASES = {
    # Languages
    "python": "python", "pyhton": "python", "java": "java",
    "javascript": "javascript", "javascrpit": "javascript", "js": "javascript",
    "typescript": "typescript", "typescrpit": "typescript",
    "c++": "cpp", "cpp": "cpp", "r": "r", "kotlin": "kotlin",

    # ML / Data
    "machinelearning": "machine_learning", "machine learning": "machine_learning",
    "ml": "machine_learning", "sklearn": "machine_learning",
    "deeplearning": "deep_learning", "deep learning": "deep_learning",
    "deep-learning": "deep_learning",
    "tensorflow": "tensorflow", "pytorch": "pytorch", "keras": "keras",
    "nlp": "nlp", "bert": "bert", "xgboost": "xgboost",
    "feature engineering": "feature_engineering",
    "statistics": "statistics", "stats": "statistics",
    "regression": "regression", "clustering": "clustering",
    "data-viz": "data_visualization", "data visualization": "data_visualization",
    "data viz": "data_visualization", "matplotlib": "data_visualization",
    "tableau": "data_visualization", "power-bi": "data_visualization",
    "power bi": "data_visualization", "powerbi": "data_visualization",
    "pandas": "pandas", "numpy": "numpy",

    # Web — Frontend
    "react": "react", "reacts": "react", "reactjs": "react",
    "vue": "vue", "vue.js": "vue", "vuejs": "vue",
    "redux": "redux", "tailwind": "tailwind",
    "html/css": "html_css", "html css": "html_css",
    "html": "html_css", "css": "html_css",
    "jest": "jest", "graphql": "graphql",

    # Web — Backend
    "node.js": "nodejs", "nodejs": "nodejs", "node js": "nodejs",
    "flask": "flask",
    "spring boot": "spring_boot", "springboot": "spring_boot",
    "rest api": "rest_api", "rest": "rest_api", "restapi": "rest_api",
    "microservices": "microservices",

    # Databases
    "sql": "sql", "mysql": "mysql", "mysq": "mysql",
    "postgresql": "postgresql", "postgres": "postgresql",
    "mongodb": "mongodb", "redis": "redis",

    # DevOps / Cloud
    "docker": "docker",
    "kubernetes": "kubernetes", "kubernates": "kubernetes", "k8s": "kubernetes",
    "ci/cd": "ci_cd", "cicd": "ci_cd", "ci cd": "ci_cd",
    "aws": "aws",

    # Mobile
    "android": "android", "firebase": "firebase",

    # CS Fundamentals
    "algorithms": "algorithms", "algoritms": "algorithms",
    "data structure": "data_structures", "data structures": "data_structures",
    "competitive programming": "competitive_programming",

    # Design
    "ui/ux": "ui_ux", "ui ux": "ui_ux", "figma": "figma",
}

# ============================================================
# RAW RESUME DATA
# ============================================================
RESUMES = [
    {"id": "01", "name": "Arjun Sharma",    "raw": "Pyhton, MachineLearning, SQL, pandas, numpy, Deep-learning"},
    {"id": "02", "name": "Priya Nair",      "raw": "JavaScrpit, Reacts, Node.JS, MongoDb, REST api, HTML/CSS"},
    {"id": "03", "name": "Rahul Gupta",     "raw": "Java, Spring Boot, MySql, Microservices, Docker, kubernates"},
    {"id": "04", "name": "Sneha Patel",     "raw": "Python, TensorFlow, Keras, NLP, BERT, data-viz, matplotlib"},
    {"id": "05", "name": "Vikram Singh",    "raw": "C++, Algoritms, Data Structure, competitive programming, python"},
    {"id": "06", "name": "Ananya Krishnan", "raw": "javascript, vue.js, python, flask, PostgreSQL, AWS, CI/CD"},
    {"id": "07", "name": "Karan Mehta",     "raw": "Python, Sklearn, XGboost, feature engineering, SQL, tableau"},
    {"id": "08", "name": "Deepika Rao",     "raw": "Java, Android, Kotlin, Firebase, REST, UI/UX, figma"},
    {"id": "09", "name": "Aditya Kumar",    "raw": "Reactjs, TypeScrpit, GraphQL, redux, tailwind, nodejs, jest"},
    {"id": "10", "name": "Meera Iyer",      "raw": "python, R, statistics, ML, regression, clustering, Power-BI"},
]

# ============================================================
# JOB DESCRIPTIONS
# ============================================================
JDS = [
    {
        "id": "JD-1", "company": "Kakao (ML Engineer)",
        "required": "Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, SQL, Data Visualization",
        "preferred": "NLP, BERT, Feature Engineering, Statistics"
    },
    {
        "id": "JD-2", "company": "Naver (Backend Engineer)",
        "required": "Java, Spring Boot, MySQL, PostgreSQL, Microservices, Docker, Kubernetes",
        "preferred": "REST API, CI/CD, Redis"
    },
    {
        "id": "JD-3", "company": "Line (Frontend Engineer)",
        "required": "JavaScript, React, Vue, TypeScript, REST API, HTML/CSS",
        "preferred": "Node.js, GraphQL, Redux, Jest, AWS"
    },
]

# ============================================================
# STEP 1: NORMALIZE SKILLS
# ============================================================
def normalize_skills(raw_string):
    """
    1. Split on commas
    2. Lowercase each token
    3. Match multi-word phrases FIRST, then single tokens
    4. Apply SKILL_ALIASES
    5. Discard tokens not in alias map
    """
    # Split on commas and strip whitespace
    tokens = [t.strip().lower() for t in raw_string.split(",")]

    # Sort alias keys by length DESC so multi-word phrases match first
    sorted_aliases = sorted(SKILL_ALIASES.keys(), key=lambda x: len(x), reverse=True)

    canonical_skills = []
    for token in tokens:
        matched = False
        for alias_key in sorted_aliases:
            if token == alias_key:
                canonical_skills.append(SKILL_ALIASES[alias_key])
                matched = True
                break
        # If no match found, token is discarded (not in alias map)
    return canonical_skills

def deduplicate(skills_list):
    """Remove duplicates while preserving first-occurrence order."""
    seen = set()
    result = []
    for s in skills_list:
        if s not in seen:
            seen.add(s)
            result.append(s)
    return result

# ============================================================
# STEP 2: PROCESS ALL RESUMES
# ============================================================
print("=" * 60)
print("STEP 1 & 2: NORMALIZED + DEDUPLICATED SKILLS PER RESUME")
print("=" * 60)

for resume in RESUMES:
    normalized = normalize_skills(resume["raw"])
    deduped    = deduplicate(normalized)
    resume["skills"] = deduped
    print(f"\n[{resume['id']}] {resume['name']}")
    print(f"  Raw   : {resume['raw']}")
    print(f"  Skills: {deduped}  (N={len(deduped)})")

# ============================================================
# STEP 3: BUILD SHARED VOCABULARY (sorted alphabetically)
# ============================================================
all_skills = set()
for resume in RESUMES:
    all_skills.update(resume["skills"])

VOCAB = sorted(all_skills)

print("\n" + "=" * 60)
print("STEP 3: SHARED VOCABULARY (alphabetical)")
print("=" * 60)
for i, skill in enumerate(VOCAB):
    print(f"  [{i:02d}] {skill}")
print(f"\n  Total vocab size: {len(VOCAB)}")

# ============================================================
# STEP 4: COMPUTE TF-IDF VECTORS FOR RESUMES
# ============================================================

# --- Document Frequency ---
df = {skill: 0 for skill in VOCAB}
for resume in RESUMES:
    for skill in resume["skills"]:
        df[skill] += 1

print("\n" + "=" * 60)
print("STEP 4a: DOCUMENT FREQUENCY (df) PER SKILL")
print("=" * 60)
for skill in VOCAB:
    print(f"  {skill:<30} df={df[skill]}")

# --- IDF ---
idf = {}
for skill in VOCAB:
    idf[skill] = math.log(10 / df[skill])   # ln(10 / df), no smoothing

print("\n" + "=" * 60)
print("STEP 4b: IDF VALUES")
print("=" * 60)
for skill in VOCAB:
    print(f"  {skill:<30} IDF={idf[skill]:.6f}")

# --- TF-IDF ---
print("\n" + "=" * 60)
print("STEP 4c: TF-IDF VECTORS")
print("=" * 60)

for resume in RESUMES:
    N = len(resume["skills"])           # total unique skills after dedup
    tfidf_vec = []
    for skill in VOCAB:
        if skill in resume["skills"]:
            tf    = 1 / N               # TF = 1/N after deduplication
            score = tf * idf[skill]
        else:
            score = 0.0
        tfidf_vec.append(score)
    resume["tfidf"] = tfidf_vec

    # Print non-zero entries only for readability
    print(f"\n[{resume['id']}] {resume['name']}  (N={N})")
    for i, skill in enumerate(VOCAB):
        if tfidf_vec[i] > 0:
            tf_val = 1 / N
            print(f"  {skill:<30} TF={tf_val:.6f}  IDF={idf[skill]:.6f}  TF-IDF={tfidf_vec[i]:.6f}")

# ============================================================
# STEP 5: BUILD JD BINARY VECTORS
# ============================================================
def build_jd_vector(jd):
    """
    Combine required + preferred skills, normalize, deduplicate,
    then build a binary vector over VOCAB.
    """
    combined_raw = jd["required"] + ", " + jd["preferred"]
    normalized   = normalize_skills(combined_raw)
    deduped      = deduplicate(normalized)
    jd["skills"] = deduped

    binary_vec = []
    for skill in VOCAB:
        binary_vec.append(1 if skill in deduped else 0)
    jd["vector"] = binary_vec
    return binary_vec

print("\n" + "=" * 60)
print("STEP 5: JD BINARY VECTORS")
print("=" * 60)

for jd in JDS:
    build_jd_vector(jd)
    print(f"\n{jd['id']} — {jd['company']}")
    print(f"  Normalized skills: {jd['skills']}")
    active = [VOCAB[i] for i, v in enumerate(jd["vector"]) if v == 1]
    print(f"  Active vocab dims: {active}")

# ============================================================
# STEP 6: COSINE SIMILARITY & RANKING
# ============================================================
def cosine_similarity(vec_a, vec_b):
    """
    Cosine(A, B) = (A · B) / (|A| × |B|)
    A = TF-IDF resume vector
    B = binary JD vector
    """
    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a ** 2 for a in vec_a))
    norm_b = math.sqrt(sum(b ** 2 for b in vec_b))

    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)

print("\n" + "=" * 60)
print("STEP 6: COSINE SIMILARITY SCORES")
print("=" * 60)

for jd in JDS:
    print(f"\n{jd['id']} — {jd['company']}")
    scores = []
    for resume in RESUMES:
        sim = cosine_similarity(resume["tfidf"], jd["vector"])
        scores.append((resume["name"], sim))
        print(f"  {resume['name']:<20} score={sim:.6f}")

    # Sort: descending score, then alphabetical name on tie
    scores.sort(key=lambda x: (-round(x[1], 10), x[0]))
    jd["ranking"] = scores

# ============================================================
# FINAL OUTPUT
# ============================================================
print("\n" + "=" * 60)
print("FINAL RESULTS — TOP 3 CANDIDATES PER JD")
print("=" * 60)

for jd in JDS:
    top3 = jd["ranking"][:3]
    result_str = ", ".join(f"{name}({score:.2f})" for name, score in top3)
    print(f"\n{jd['id']} — {jd['company']}")
    print(f"  {result_str}")