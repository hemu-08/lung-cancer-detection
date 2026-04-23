import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

def random_date(start_year=2018, end_year=2024):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

def generate_patient(is_cancer):
    if is_cancer:
        return {
            "visit_date": random_date(),
            "SMOKING":         random.choices([0,1,2,3], weights=[50,20,15,15])[0],
            "YELLOW_FINGERS":  random.choices([0,1], weights=[30,70])[0],
            "ANXIETY":         random.choices([0,1], weights=[25,75])[0],
            "PEER_PRESSURE":   random.choices([0,1], weights=[40,60])[0],
            "CHRONIC_DISEASE": random.choices([0,1], weights=[30,70])[0],
            "FATIGUE":         random.choices([0,1], weights=[20,80])[0],
            "ALLERGY":         random.choices([0,1], weights=[35,65])[0],
            "WHEEZING":        random.choices([0,1], weights=[25,75])[0],
            "LUNG_CANCER":     "YES"
        }
    else:
        return {
            "visit_date": random_date(),
            "SMOKING":         random.choices([0,1,2,3], weights=[70,15,10,5])[0],
            "YELLOW_FINGERS":  random.choices([0,1], weights=[80,20])[0],
            "ANXIETY":         random.choices([0,1], weights=[65,35])[0],
            "PEER_PRESSURE":   random.choices([0,1], weights=[60,40])[0],
            "CHRONIC_DISEASE": random.choices([0,1], weights=[70,30])[0],
            "FATIGUE":         random.choices([0,1], weights=[60,40])[0],
            "ALLERGY":         random.choices([0,1], weights=[55,45])[0],
            "WHEEZING":        random.choices([0,1], weights=[75,25])[0],
            "LUNG_CANCER":     "NO"
        }

data = []

for _ in range(1500):
    data.append(generate_patient(is_cancer=True))

for _ in range(1500):
    data.append(generate_patient(is_cancer=False))

df = pd.DataFrame(data)
df = df.sample(frac=1).reset_index(drop=True)
df.to_csv("lung_cancer_dataset.csv", index=False)

print(f"Dataset generated: {len(df)} rows")
print(df['LUNG_CANCER'].value_counts())