# Resume Matching Engine

Built for the Redrob AI Campus Hackathon. Parses and normalizes 
noisy resume skill data from 10 candidates, computes TF-IDF vectors, 
and ranks them against 3 job descriptions from Korean tech companies 
(Kakao, Naver, Line) using cosine similarity.

## How it works
- Normalizes misspelled/noisy skills via a canonical alias map
- Builds a shared vocabulary across all resumes
- Computes TF-IDF (no external libraries — pure Python)
- Builds binary vectors for each JD
- Outputs Top 3 matching candidates per role

## Stack
Python 3 · Standard Library only · No numpy/pandas/sklearn