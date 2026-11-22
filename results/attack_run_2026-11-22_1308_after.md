# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-22 13:08
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `f57de53be8bd` | unsure | 0.377 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `09d28d6b5ca5` | unsure | 0.469 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `dca0c3036462` | unsure | 0.569 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `05edf2755a13` | unsure | 0.592 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `8f8cb8540573` | human | 0.344 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `ba67052c3815` | unsure | 0.477 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `43f83b21f220` | unsure | 0.538 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `02e5267ab22c` | unsure | 0.397 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `1a9e4149c886` | unsure | 0.584 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `3dfd86048d9d` | ai | 0.854 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `3d884257878c` | unsure | 0.585 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `7129c7ff589f` | ai | 0.694 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `4e3f01924af2` | ai | 0.714 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `08e4b9b349e7` | ai | 0.697 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `c9facf90cea1` | ai | 0.729 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `8ac48be8cffd` | ai | 0.701 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `e5bb4b6e91a7` | ai | 0.693 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `ad320f784ff2` | unsure | 0.404 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `a2626493cf62` | unsure | 0.438 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `4051e2001863` | human | 0.282 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `0aae84283d16` | unsure | 0.544 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `66637fd31d1b` | unsure | 0.480 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `55eade0b6957` | unsure | 0.450 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `00dd4594d8cc` | unsure | 0.558 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 200 | `1fe201c8522d` | ai | 0.953 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4d70c4207055` | human | 0.348 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7920ef6acbc9` | human | 0.348 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `de938715c9b5` | human | 0.348 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `aa54a7f7da82` | human | 0.348 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ef70a92270eb` | human | 0.348 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "f57de53be8bd",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.377,
  "model_score": 0.1635,
  "style_score": 0.5905,
  "label": "We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "09d28d6b5ca5",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4687,
  "model_score": 0.5943,
  "style_score": 0.3431,
  "label": "We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "dca0c3036462",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.56935,
  "model_score": 0.6662,
  "style_score": 0.4725,
  "label": "We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "05edf2755a13",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5918000000000001,
  "model_score": 0.6114,
  "style_score": 0.5722,
  "label": "We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "8f8cb8540573",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.34445000000000003,
  "model_score": 0.3212,
  "style_score": 0.3677,
  "label": "This text looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "ba67052c3815",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.47655000000000003,
  "model_score": 0.5727,
  "style_score": 0.3804,
  "label": "We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "43f83b21f220",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.53825,
  "model_score": 0.5862,
  "style_score": 0.4903,
  "label": "We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "02e5267ab22c",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.39699999999999996,
  "model_score": 0.2452,
  "style_score": 0.5488,
  "label": "We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "1a9e4149c886",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.58355,
  "model_score": 0.7042,
  "style_score": 0.4629,
  "label": "We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "3dfd86048d9d",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8541,
  "model_score": 0.9792,
  "style_score": 0.729,
  "label": "This text is very likely to have been generated by AI. If you believe this result is incorrect, you can appeal it for human review.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "3d884257878c",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.58455,
  "model_score": 0.6175,
  "style_score": 0.5516,
  "label": "We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "7129c7ff589f",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.69355,
  "model_score": 0.7387,
  "style_score": 0.6484,
  "label": "This text is very likely to have been generated by AI. If you believe this result is incorrect, you can appeal it for human review.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "4e3f01924af2",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7137,
  "model_score": 0.8051,
  "style_score": 0.6223,
  "label": "This text is very likely to have been generated by AI. If you believe this result is incorrect, you can appeal it for human review.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "08e4b9b349e7",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6971,
  "model_score": 0.8329,
  "style_score": 0.5613,
  "label": "This text is very likely to have been generated by AI. If you believe this result is incorrect, you can appeal it for human review.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "c9facf90cea1",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.72905,
  "model_score": 0.8005,
  "style_score": 0.6576,
  "label": "This text is very likely to have been generated by AI. If you believe this result is incorrect, you can appeal it for human review.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "8ac48be8cffd",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7014499999999999,
  "model_score": 0.8814,
  "style_score": 0.5215,
  "label": "This text is very likely to have been generated by AI. If you believe this result is incorrect, you can appeal it for human review.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "e5bb4b6e91a7",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.6934,
  "model_score": 0.8816,
  "style_score": 0.5052,
  "label": "This text is very likely to have been generated by AI. If you believe this result is incorrect, you can appeal it for human review.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "ad320f784ff2",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.40425,
  "model_score": 0.3223,
  "style_score": 0.4862,
  "label": "We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "a2626493cf62",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.43765,
  "model_score": 0.4625,
  "style_score": 0.4128,
  "label": "We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "4051e2001863",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.28245,
  "model_score": 0.2044,
  "style_score": 0.3605,
  "label": "This text looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "0aae84283d16",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5438500000000001,
  "model_score": 0.5943,
  "style_score": 0.4934,
  "label": "We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "66637fd31d1b",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4799,
  "model_score": 0.4998,
  "style_score": 0.46,
  "label": "We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "55eade0b6957",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4496,
  "model_score": 0.6401,
  "style_score": 0.2591,
  "label": "We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "00dd4594d8cc",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5585,
  "model_score": 0.5583,
  "style_score": 0.5587,
  "label": "We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "1fe201c8522d",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9532,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "This text is very likely to have been generated by AI. If you believe this result is incorrect, you can appeal it for human review.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "4d70c4207055",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.34769999999999995,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "7920ef6acbc9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.34769999999999995,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "de938715c9b5",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.34769999999999995,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "aa54a7f7da82",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.34769999999999995,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "ef70a92270eb",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.34769999999999995,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
