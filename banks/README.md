# IUK Tier Banks

Built from `benchmark/pools/IUK_pool_T*.json`. Run `scripts/build_tier_banks.py` to regenerate.

## Tier counts

| Tier | Label | Count | Default weight | Pass gate |
|------|-------|-------|----------------|-----------|
| T1 | Technician | 201 | 1.0× | ≥80% |
| T2 | Engineer | 515 | 2.0× | ≥75% |
| T3 | Specialist/PhD | 425 | 3.5× | ≥65% |
| T4 | Expert+ | 406 | 5.0× | ≥60% adv · safety 100% |
| T5 | AI Ceiling | 0 | 7.0× | TBD |
| **Total** | | **1547** | | |

## Source breakdown per tier

### T1 Technician — 201Q
- `IUK_upgrade_IUK_T1_technician_560_upgrade`: 200Q
- `IUK_mastery_textualized_IUK_MASTERY_INST200_x1_mastery_v01_textualized`: 1Q

### T2 Engineer — 515Q
- `IUK_upgrade_IUK_T2_engineer_560_upgrade`: 200Q
- `IUK_v3_IUK_v3_T2_applied`: 198Q
- `IUK_v3_IUK_v3_T1_foundational`: 100Q
- `IUK_mastery_textualized_IUK_MASTERY_INST200_x1_mastery_v01_textualized`: 8Q
- `IUK_mastery_textualized_IUK_MASTERY_INST251_x2_mastery_textualized`: 5Q
- `IUK_mastery_textualized_IUK_MASTERY_INST200_x1_mastery_v02_textualized`: 2Q
- `IUK_mastery_textualized_IUK_MASTERY_INST241_x2_mastery_latest_textualized`: 2Q

### T3 Specialist/PhD — 425Q
- `IUK_v3_IUK_v3_T3_diagnostic`: 296Q
- `IUK_upgrade_IUK_T3_specialist_560_upgrade`: 125Q
- `IUK_mastery_textualized_IUK_MASTERY_INST200_x1_mastery_v01_textualized`: 3Q
- `IUK_mastery_textualized_IUK_MASTERY_INST251_x2_mastery_textualized`: 1Q

### T4 Expert+ — 406Q
- `IUK_v3_IUK_v3_T4_adversarial`: 241Q
- `IUK_v3_IUK_v3.1_T5_safety-critical_enhanced`: 130Q
- `IUK_upgrade_IUK_T4_expert_plus_560_upgrade`: 35Q

### T5 AI Ceiling — 0Q
_(empty — see bank file)_
