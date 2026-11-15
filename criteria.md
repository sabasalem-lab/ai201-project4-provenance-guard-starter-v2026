# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
# Acceptance criteria — Provenance Guard

## 1. False positives
**Criterion:** When testing 10 pieces of text that I wrote or collected myself and know to be human-written, no more than 1 may be classified as high-confidence AI-generated.

**Why this target:** False positives can incorrectly identify genuine human writing as AI-generated. I chose a maximum of 1 out of 10 because the system should minimize incorrect accusations. I consider this target acceptable because users can appeal a classification and request a review.

## 2. Label coverage
**Criterion:** Across a test set of at least 10 varied text submissions, the system must produce all three available classifications at least once: AI-generated, human-written, and uncertain.

**Why this target:** A useful detection system must support all three classifications rather than assigning every submission to only one or two categories. The uncertain category is important when the system cannot confidently distinguish between human and AI writing.

## 3. Appeal path
**Criterion:** In 10 out of 10 valid appeal attempts, the system must change the corresponding submission status to `under_review` and create a corresponding record in the appeal log, verifiable through `GET /log`.

**Why this target:** Users should have a reliable way to challenge a classification. Recording every appeal makes the review process traceable and prevents requests from being lost.

## 4. Bad input handling
**Criterion:** In 10 out of 10 tests involving empty text or a missing text field, the system must return an HTTP 400 response containing an error field, without crashing or producing an AI-detection classification.

**Why this target:** Users may accidentally submit incomplete information. The system should handle these situations predictably instead of crashing or producing misleading classifications.

## 5. Score spread
**Criterion:** The average combined confidence score for 10 clearly AI-generated text samples produced by a chatbot must be at least 30 percentage points higher than the average combined confidence score for 10 clearly human-written samples that I wrote or collected myself.

**Why this target:** The system should demonstrate a measurable difference between clearly AI-generated and clearly human-written text. I chose a 30-percentage-point difference as a measurable target for evaluating whether the combined confidence score distinguishes between the two groups.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
