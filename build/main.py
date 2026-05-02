"""
MIMIC-IV cohort analysis — exercises all archetype groups (admissions, patient, diagnoses).
Produces deterministic summary statistics suitable for benchmark repeatability.
"""

from collections import Counter

from generated.models import create_dataset


def main():
    dataset = create_dataset()
    print(f"Loaded {len(dataset)} records")

    gender_counts = Counter()
    admission_types = Counter()
    icd_codes = Counter()
    age_buckets = Counter()
    icd_versions = Counter()

    age_values = []

    for record in dataset:
        gender = record.patient.gender or "UNKNOWN"
        gender_counts[gender] += 1

        try:
            age = int(record.patient.age) if record.patient.age is not None else None
        except (TypeError, ValueError):
            age = None
        if age is not None:
            age_values.append(age)
            bucket = (age // 10) * 10
            age_buckets[f"{bucket}-{bucket + 9}"] += 1

        atype = record.admissions.type or "UNKNOWN"
        admission_types[atype] += 1

        icd = record.diagnoses.icd_code or "UNKNOWN"
        icd_codes[icd] += 1

        ver = record.diagnoses.icd_version or "UNKNOWN"
        icd_versions[str(ver)] += 1

    print("\n=== Gender distribution ===")
    for g, n in gender_counts.most_common():
        print(f"  {g}: {n}")

    print("\n=== Age summary ===")
    if age_values:
        print(f"  n={len(age_values)} mean={sum(age_values) / len(age_values):.1f} "
              f"min={min(age_values)} max={max(age_values)}")
        print("  Age buckets:")
        for bucket, n in sorted(age_buckets.items()):
            print(f"    {bucket}: {n}")
    else:
        print("  (no age values)")

    print("\n=== Admission types (top 10) ===")
    for atype, n in admission_types.most_common(10):
        print(f"  {atype}: {n}")

    print("\n=== ICD versions ===")
    for v, n in icd_versions.most_common():
        print(f"  v{v}: {n}")

    print("\n=== Top 20 ICD codes ===")
    for code, n in icd_codes.most_common(20):
        print(f"  {code}: {n}")

    return {
        "n_records": len(dataset),
        "n_genders": len(gender_counts),
        "n_admission_types": len(admission_types),
        "n_unique_icd_codes": len(icd_codes),
        "mean_age": (sum(age_values) / len(age_values)) if age_values else None,
    }


if __name__ == "__main__":
    result = main()
    print("\n=== Result summary ===")
    for k, v in result.items():
        print(f"  {k}: {v}")
