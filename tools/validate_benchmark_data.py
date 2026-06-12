#!/usr/bin/env python3
"""Validate the public IUK benchmark data files."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_KEYS = {
    "iuk_id",
    "question",
    "answer",
    "required_elements",
    "reference",
    "review_status",
}


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"{path} is not valid JSON: {exc}") from exc


def validate_pools() -> None:
    for path in sorted((ROOT / "pools").glob("*.json")):
        data = load_json(path)
        questions = data.get("questions")
        assert isinstance(questions, list), f"{path}: questions must be a list"
        assert data.get("total_questions") == len(questions), (
            f"{path}: total_questions={data.get('total_questions')} but found {len(questions)}"
        )
        ids = [item.get("iuk_id") for item in questions]
        assert len(ids) == len(set(ids)), f"{path}: duplicate iuk_id values"
        for index, question in enumerate(questions):
            missing = QUESTION_KEYS - set(question)
            assert not missing, f"{path}: question {index} missing keys {sorted(missing)}"


def validate_results() -> None:
    result_dir = ROOT / "results" / "v1.3"
    leaderboard = load_json(result_dir / "benchmark_v1.3.json")
    for table_name in ("t1_leaderboard", "t2_leaderboard", "t3_leaderboard"):
        for row in leaderboard.get(table_name, []):
            result_file = row.get("result_file")
            if result_file:
                assert (result_dir / result_file).exists(), f"{table_name}: missing {result_file}"

    for path in sorted(result_dir.glob("*.json")):
        data = load_json(path)
        if path.name == "benchmark_v1.3.json":
            continue
        summary = data.get("summary", {})
        questions = data.get("questions", [])
        assert summary.get("total_questions") == len(questions), (
            f"{path}: summary total_questions={summary.get('total_questions')} but found {len(questions)}"
        )
        assert summary.get("answered", len(questions)) <= len(questions), f"{path}: answered exceeds question count"
        assert 0 <= summary.get("score_pct", 0) <= 100, f"{path}: score_pct out of range"


def main() -> None:
    validate_pools()
    validate_results()
    print("benchmark data ok")


if __name__ == "__main__":
    main()
