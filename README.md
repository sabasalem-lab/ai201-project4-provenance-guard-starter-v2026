# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

1. A submission arrives as JSON at `POST /submit` with `text` and `creator_id`.
2. The route validates it: missing or empty text returns a 400 with an error field, logs a rejection, and never reaches a signal.
3. Valid text gets a 12-character `content_id`.
4. Signal one (`detector.model_signal`) scores how predictable the text is to GPT-2, 0–1, higher = more AI-like.
5. Signal two (`stylometry.style_signal`) scores the shape of the text — sentence-length spread, vocabulary variety, punctuation — same direction.
6. `scoring.combine_signals` averages the two into one confidence score, and `scoring.score_to_label` turns that into a guess and the sentence a reader sees.
7. The decision is written to `logs/audit.jsonl` with both signal scores, and the response returns the id, both scores, the combined score, and the label. A writer who disagrees posts the `content_id` to `POST /appeal`, which marks it `under_review` and records their reasoning next to the original decision.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to GPT-2 (perplexity, scaled to 0–1; higher = more likely AI).

**Why that might differ between human and AI writing:** A language model writes by picking likely next words, so model-written text is text a model finds easy to predict. Human writing wanders — odd word choices, abrupt turns.

**What it can't see:** Predictability is not authorship. It rewards common words in short, ordinary sentences, so it flags real people who write plainly — second-language writers, anyone writing simply on purpose. I saw this on my own writing: a genuine essay I wrote scored 0.6909. The reverse also holds: rare words surprise GPT-2, so ornate human prose scores human for the wrong reason.
### Signal two — the style signal

**What it measures:** The shape of the text, without reading it: sentence-length spread (stdev/mean of sentence word counts), type-token ratio (unique/total words), and varied-punctuation density per word. Each scaled to 0–1, flipped so higher = more AI-ish, averaged in equal thirds.

**Why that might differ between human and AI writing:** Generated prose tends toward even, mid-length sentences and a narrower vocabulary band; human writing is lumpier — a three-word sentence next to a forty-word one.

**What it can't see:** It cannot read. Anything that changes shape without changing substance moves it — typos, broken-up sentences, pasted quotations — which is cheap to do on purpose.

### The combining rule

**The rule:** A weighted average of the two signals. When they disagree, the average lands mid-range — in the unsure band — which I take as correct: two independent methods disagreeing *is* uncertainty.

**The numbers:** 0.5 × model_score + 0.5 × style_score (weights in `config.py`). Equal weights because the signals measure independent things and I had no evidence to trust one over the other.

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:** A formal literary-analysis paragraph I wrote scored 0.4048 on the model signal (rare words like "trochaic" surprise GPT-2) but 0.6321 on style (long, even academic sentences). They disagreed by 0.23; the average, 0.5185, landed it in unsure — no accusation either way, which is what I want when my two methods can't agree.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | This text looks like it was written by a person. |
| unsure | 0.35 – 0.65 | We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result. |
| high-confidence AI | 0.65 – 1.00 | This text is very likely to have been generated by AI. If you believe this result is incorrect, you can appeal it for human review. |

**Why I worded the "unsure" one this way:**
The person reading it may have written every word themselves, so it has to admit the system's limitation without implying theirs. I named the uncertainty as ours ("we could not confidently determine") and said explicitly that no action follows, so a real writer reads it as "the system can't tell" rather than "you're suspected."

---


## Sample Run

**A submission** — an essay I wrote myself:

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "In my first semester at Irvine Valley College, I flew home for a funeral and missed about a week of class. [full essay — abridged here for length]", "creator_id": "saba"}'
```

```json
{
    "confidence":  0.6161,
    "content_id":  "db70d0000efc",
    "guess":  "unsure",
    "label":  "We could not confidently determine whether this text was written by a person or generated by AI. No action will be taken based on this result.",
    "model_score":  0.6909,
    "style_score":  0.5413
}
```

**An appeal** — on that same submission:

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "db70d0000efc", "creator_id": "saba", "reasoning": "I wrote this essay myself about my own life."}'
```

```json
{
    "content_id":  "db70d0000efc",
    "message":  "Your appeal has been recorded. A person will review this decision.",
    "ok":  true,
    "status":  "under_review"
}
```

**What the log shows afterwards** — the original decision, the appeal that moved it to `under_review`, and a rejected bad input:

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
    "combined_score":  0.6161,
    "content_id":  "db70d0000efc",
    "creator_id":  "saba",
    "guess":  "unsure",
    "model_score":  0.6909,
    "status":  "decided",
    "style_score":  0.5413,
    "timestamp":  "2026-11-15T23:35:45+00:00"
}
{
    "content_id":  "db70d0000efc",
    "creator_id":  "saba",
    "event":  "appeal",
    "reasoning":  "I wrote this essay myself about my own life.",
    "status":  "under_review",
    "timestamp":  "2026-11-15T23:45:41+00:00"
}
{
    "creator_id":  "saba",
    "event":  "rejected",
    "reason":  "missing_or_empty_text",
    "status":  "rejected",
    "timestamp":  "2026-11-15T23:46:00+00:00"
}
```
---

## How I Used AI

**Moment 1**

- *What I asked for:* I drafted my five acceptance criteria and asked Claude to check only whether each could be tested by someone who couldn't ask me what I meant — not to write them.
- *What came back:* It flagged that my label-coverage criterion demanded all three labels from exactly three submissions (only satisfiable if every one landed perfectly), and that "clear validation error" named no observable.
- *What I changed:* Rewrote them to require at least ten varied submissions, and named the observable: HTTP 400 with an error field.

**Moment 2**

- *What I asked for:* When my own genuine essay scored 0.6161 — 0.034 below the AI threshold — I worked through with Claude which signal drove the near-miss.
- *What came back:* The model signal (0.6909) was the driver: plain sentences built from common words are exactly what GPT-2 predicts easily, the structural bias detector.py warns about.
- *What I changed:* I kept my 0.5/0.5 weights but wrote the near-miss into this README as evidence for why the unsure band and the appeal path carry the real safety weight, and appealed that submission as my sample appeal.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
