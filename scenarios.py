"""
What my test runs. UNIT 8, MILESTONE 3

One scenario per criterion in criteria.md. run_eval.py runs each three times.

Criterion 3 (appeals) can't be expressed as text alone: it needs a submission
and then an appeal against the content_id that came back. That one is tested
by appeal_check.py, run three times by hand, not by this file.

Criterion 5 (score spread) compares the average combined score of the AI
scenario below against the average of criterion 1's human scenario.
"""

# Criterion 1: ten pieces of my own writing, from essays and coursework I wrote.

MY_WRITING = [
    "When I was little, my mom would sometimes hand me a game controller to calm me down when I cried. Back then, I was interested in playing. As I grew older, I became more curious about what happened behind the screen: how controllers communicated with consoles, how games responded to my actions, and how people built the technology behind them.",
    "My curiosity led me to teach myself web design through online tutorials before immigrating to the United States in 2023. This eventually led to an internship building responsive websites. Later, I built my own 2D game in Godot, coding its double-jump mechanics, animations, and collisions.",
    "At Irvine Valley College, I joined the IVC honors program and strengthened my foundations in C++ and data structures by developing a Delivery Order System using inheritance, polymorphic discounts, and custom exceptions. Through the Computer Science Club, I learned more about Python simulation, Java backend design (controllers, services, repositories, and the strategy pattern), and embedded hardware. I built an ESP32 web server that sends messages from my phone to an OLED display, and I presented on machine learning to the club.",
    "As a software engineering intern at Tangenta, I work in C to wire, configure, and test embedded hardware, and I write tests that check whether our software handles bad inputs, such as lost signals, without crashing. Before a component goes into a vehicle, I make sure it can communicate with everything around it, and then I test what happens when it can't. Tangenta connects unmanned vehicles to their operators through simulation, telemetry, and custom hardware, so a dropped signal is a real problem, not a classroom exercise. A machine that cannot hear its operator could become dangerous. My job is to find those failures in testing, long before they could happen in the real world.",
    "I further challenged myself through CodePath's AI Engineering course, dedicating over ten hours weekly to developing practical AI applications. I have built four AI systems so far: a system for finding clothes within budget limits and proposing outfits to wear, a program for answering questions based on a large number of documents, an application that flags writing that may be AI-generated and lets writers appeal if it gets it wrong. I have done all of this while supporting myself financially and working long hours, so I know how to manage a demanding schedule.",
    "In my first semester at Irvine Valley College, I flew home for my cousin's funeral and missed about a week of class. I was working more than 60 hours a week, and I was still learning English. I worked as hard as I could to catch up, but I finished with a B in C programming, the only B on my record. I felt that I had let myself down. For the first time, I wondered whether I was capable of achieving everything I had once believed I could. But beneath that doubt, I still believed my circumstances did not have to determine my future.",
    "My understanding of challenges has changed. I no longer see them as situations I must overcome perfectly. I have learned that progress sometimes means adjusting my expectations, finding another way forward, and continuing even when the results are not immediate. This semester I carry 21 units, mentor elementary school children as a College Corps fellow, tutor at IVC's Math Center, teach two students privately, build AI projects, and work at my internship. Every challenge has made me stronger, and I want to use that strength to build robots that help people, especially children.",
    "One afternoon during math center time at my College Corps placement, I noticed a second grader staring at her worksheet with tears in her eyes and her head lowered. 'All the others are fast,' she said softly. 'I'm not good at math.' I sat beside her. 'Let's do one problem together, just you and me.' We solved a multiplication problem in small steps, and when we finished, she lifted her head. 'I solved it,' she said, 'but only because you helped.' I told her, 'You did the thinking. I was just sitting with you.' She asked, 'Can we do another one?'",
    "My service continues at IVC's Math Center, where I tutor math and computer science about twenty hours a week, and at Crown Valley Academy with high school students. In all, I have helped more than one hundred students, from elementary school to college. Many arrive believing they are slow or bad at math, and my work is to help them test that belief one problem at a time. I chose this work because education changed the direction of my own life, and I want to make that door easier to open for someone else.",
    "In 'Love Among the Ruins', Browning compares the past with the present giving love more weight than material things through the persona that he creates. In this poem, Browning creates rhyme through paring long trochaic lines with short sentences often made of only three words. The persona compares what he is seeing at that particular time which is a pasture in the ruins where sheep are grazing to what used to be there; a great city led by a superior king. Browning emphasizes giving a detailed picture of the city using figurative language, which makes the poem more engaging and memorable.",
]

# Criterion 5: ten clearly AI-generated samples, written by a chatbot (Claude)
# for this test, verbatim, on varied topics.

AI_SAMPLES = [
    "Regular exercise offers many benefits for both physical and mental health. Staying active helps strengthen the heart, improve circulation, and build stronger muscles and bones. It can also increase energy levels, improve sleep quality, and support the body's ability to manage everyday activities. In addition to physical benefits, exercise can have a positive effect on mental well-being by reducing stress, improving mood, and helping people feel more focused throughout the day.",
    "Time management is an essential skill for students and professionals alike. By setting clear goals, prioritizing important tasks, and breaking larger projects into smaller steps, individuals can make steady progress without feeling overwhelmed. Using tools such as calendars, to-do lists, and reminders can help people stay organized and meet deadlines. Ultimately, effective time management leads to greater productivity, reduced stress, and a healthier balance between work and personal life.",
    "Reading regularly provides a wide range of benefits for people of all ages. It helps expand vocabulary, improve concentration, and strengthen critical thinking skills. Reading also allows individuals to explore new ideas, cultures, and perspectives without leaving their homes. In addition, many people find that reading before bed helps them relax and unwind after a busy day. Making reading a daily habit is a simple way to support lifelong learning and personal growth.",
    "Renewable energy sources such as solar, wind, and hydroelectric power play an important role in creating a more sustainable future. Unlike fossil fuels, these sources produce little to no greenhouse gas emissions, which helps reduce the impact of climate change. Advances in technology have also made renewable energy more affordable and efficient than ever before. As more communities invest in clean energy, they can enjoy cleaner air, new job opportunities, and greater energy independence.",
    "Effective communication is a key factor in building strong relationships, both personally and professionally. It involves not only expressing ideas clearly but also listening actively and showing empathy toward others. Good communicators adapt their message to their audience and remain open to feedback. By practicing these skills, individuals can resolve conflicts more easily, collaborate more effectively, and create an environment of trust and mutual respect.",
    "Healthy eating is an important part of maintaining overall well-being. A balanced diet that includes fruits, vegetables, whole grains, lean proteins, and healthy fats provides the nutrients the body needs to function properly. Limiting processed foods, added sugars, and excessive salt can help reduce the risk of chronic diseases. Planning meals ahead of time and staying hydrated are simple strategies that can make healthy eating easier to maintain over the long term.",
    "Technology has transformed the way people learn in the modern world. Online courses, educational apps, and digital resources make it possible for students to access information anytime and anywhere. Interactive tools can help learners engage with material in new ways and receive immediate feedback on their progress. While technology offers many advantages, it is also important to use it thoughtfully and maintain a healthy balance between screen time and other activities.",
    "Volunteering is a rewarding way to give back to the community while also developing valuable skills. Whether helping at a local food bank, tutoring students, or participating in environmental cleanups, volunteers make a meaningful difference in the lives of others. Volunteering can also help individuals build connections, gain new experiences, and discover a sense of purpose. Many people find that the benefits they receive are just as significant as the help they provide.",
    "Traveling offers people the opportunity to experience new cultures, cuisines, and ways of life. Exploring different places can broaden perspectives and encourage greater understanding and appreciation of diversity. Travel can also provide a welcome break from daily routines, allowing individuals to relax and recharge. Whether visiting a nearby town or a distant country, every journey has the potential to create lasting memories and inspire personal growth.",
    "Getting enough sleep is essential for good health and daily performance. During sleep, the body repairs tissues, strengthens the immune system, and consolidates memories. A lack of sleep can affect concentration, mood, and decision-making, and it may increase the risk of long-term health problems. Establishing a consistent sleep schedule, limiting screen time before bed, and creating a calm sleeping environment are effective ways to improve sleep quality.",
]

# Criterion 2: two informal texts aimed at the human band. Written by Claude for
# this test, so not counted as human writing anywhere; they only probe whether
# the high-confidence human label is reachable at all.

PROBE_TEXTS = [
    "Bus 79 -- late. Again! Forty-seven minutes on a cold bench, phone at 3%, and a pigeon eyeing my granola bar like it owed him rent. I gave up; walked. Somewhere near the laundromat (the one with the flickering 'OPEN' sign -- only the 'P' works) it started to drizzle. Fine. Whatever. Got home soaked, made tea, burnt my tongue. Classic Tuesday.",
    "Grandpa's recipe, verbatim from the stained index card: 'flour -- some; butter -- a lot; sugar -- less than you think.' No temperatures. No times. Just a smudge where the oven setting should be, and, in pencil, underlined twice: DON'T RUSH IT. Mom swears it's 350. Aunt Rosa says 325, obviously. I split the difference, burnt the edges anyway, and ate three.",
]

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": MY_WRITING,
    },
    {
        "name": "label coverage",
        "criterion": 2,
        # Ten varied inputs: four AI samples, four pieces of my writing, and two
        # informal probes aimed at the human band.
        "texts": AI_SAMPLES[:4] + MY_WRITING[:4] + PROBE_TEXTS,
    },
    {
        "name": "bad input",
        "criterion": 4,
        # Raw bodies: empty, whitespace-only, null, or missing text. Each has its
        # own creator_id so the rate limiter doesn't merge them.
        "bodies": [
            {"text": "", "creator_id": "eval_bad_01"},
            {"text": "   ", "creator_id": "eval_bad_02"},
            {"text": "\n\t ", "creator_id": "eval_bad_03"},
            {"text": None, "creator_id": "eval_bad_04"},
            {"creator_id": "eval_bad_05"},
            {"text": "", "creator_id": "eval_bad_06"},
            {"text": "      ", "creator_id": "eval_bad_07"},
            {"text": None, "creator_id": "eval_bad_08"},
            {"creator_id": "eval_bad_09"},
            {"text": "\n", "creator_id": "eval_bad_10"},
        ],
    },
    {
        "name": "score spread (AI side)",
        "criterion": 5,
        "texts": AI_SAMPLES,
    },
]


def validate() -> list[str]:
    """Complain about anything malformed, before a long run rather than during."""
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")
        texts = scenario.get("texts")
        bodies = scenario.get("bodies")
        if texts and bodies:
            problems.append(f"scenario {i} has both texts and bodies - pick one")
            continue
        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(f"scenario {i}, body {j} is not a dict")
            continue
        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue
        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(f"scenario {i}, text {j} is empty")
            elif str(text).startswith("REPLACE ME"):
                problems.append(f"scenario {i}, text {j} is still the placeholder")
    return problems