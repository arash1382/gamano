# -*- coding: utf-8 -*-
"""English content for the benchmark edition."""

ACCESS = "2025-10-31"

CRITERIA = [
    ("discovery", "Content discovery & skill architecture", 0.15,
     "Speed of finding the right skill through subject > grade > topic > skill",
     "Core of Roshana's skill library page and the 'I don't know what to practise' problem"),
    ("practice", "Practice environment & answering", 0.18,
     "Question focus, answer entry, on-screen keypad, time handling",
     "The most important moment in the product; 18% because every learning session passes through it"),
    ("feedback", "Quality of instructional feedback", 0.17,
     "Right/wrong feedback, worked solution, learning from mistakes",
     "Brief's pain point: after a wrong answer the student never learns the correct method"),
    ("progress", "Progress display & motivation", 0.12,
     "Mastery indicators (SmartScore/mastery), streaks, badges, rewards",
     "Brief's P2 requirement (honour hall, reward shop) and keeping motivation alive"),
    ("dashboard", "Student dashboard", 0.10,
     "Start page: assignment, resume, recommendation, daily goal",
     "First screen after login; brief explicitly asks for one clear primary action"),
    ("teacher", "Teacher tools & teacher dashboard", 0.15,
     "Class management, assignment, quiz builder, reporting and next action",
     "Half of Roshana's 13 MVP pages belong to teachers; without them the product is incomplete"),
    ("visual", "Visual system & illustration", 0.07,
     "Colour, typography, cards, icons, characters, visual coherence",
     "Roshana wants an independent brand and must know how much illustration it needs"),
    ("mobile", "Mobile experience & responsiveness", 0.06,
     "Quality at narrow widths, mobile navigation, touch targets, legibility",
     "The MVP is a responsive web app and a large share of teenage usage is mobile"),
]

PRODUCTS = [
    dict(key="ixl", name="IXL", vendor="IXL Learning", country="USA", lang="English",
         audience="K-12 (4-18)", model="School / family subscription",
         roles="Student, teacher, parent, admin", tint="#0E6B4F",
         one="Skill-based practice with SmartScore and a standards-aligned content library",
         score=[9, 9, 8, 8, 8, 10, 7, 8]),
    dict(key="khan", name="Khan Academy", vendor="Khan Academy", country="USA", lang="English + translations",
         audience="K-12 and university", model="Free (non-profit)",
         roles="Student, teacher, parent", tint="#14BF96",
         one="Mastery-based learning with video, practice and a progress dashboard",
         score=[9, 8, 9, 7, 8, 8, 8, 9]),
    dict(key="math", name="Mathletics", vendor="3P Learning", country="Australia / UK", lang="English",
         audience="5-18", model="School subscription",
         roles="Student, teacher, parent", tint="#F58220",
         one="Maths as sport: live class challenges plus curriculum activities",
         score=[8, 8, 7, 9, 8, 8, 7, 7]),
    dict(key="prodigy", name="Prodigy Math", vendor="Prodigy Education", country="Canada", lang="English",
         audience="Grades 1-8", model="Free + membership",
         roles="Student, teacher, parent", tint="#8B5CF6",
         one="An RPG wrapper that hides maths practice inside a battle",
         score=[7, 9, 6, 9, 7, 6, 9, 7]),
    dict(key="quizizz", name="Quizizz / Wayground", vendor="Quizizz Inc.", country="USA / India", lang="English",
         audience="K-12 and university", model="Freemium",
         roles="Teacher, student", tint="#7C3AED",
         one="Live and self-paced interactive quizzes with teacher- and AI-authored content",
         score=[6, 8, 6, 7, 6, 7, 8, 9]),
    dict(key="mihan", name="MihanMaktab", vendor="MihanMaktab", country="Iran", lang="Persian",
         audience="Grades 4-10", model="Annual subscription",
         roles="Student, tutor", tint="#1E4FB4",
         one="Interactive slides and worked-solution videos for maths, downloadable offline",
         score=[7, 7, 6, 5, 5, 4, 6, 6]),
    dict(key="gama", name="Gama.ir", vendor="Gama", country="Iran", lang="Persian",
         audience="Grades 1-12", model="Credits / subscription",
         roles="Student, teacher, school", tint="#2E9E5B",
         one="A teacher-made content marketplace: past papers, online tests, Q&A",
         score=[8, 5, 4, 4, 5, 6, 5, 6]),
    dict(key="porsan", name="Porsan", vendor="Padres group", country="Iran", lang="Persian",
         audience="Grades 4-12", model="Free + subscription",
         roles="Student, answerer", tint="#2D6CDF",
         one="A homework Q&A network: ask a question, get an answer from peers",
         score=[5, 4, 5, 3, 5, 2, 7, 8]),
]

ADJACENT = [
    ("Duolingo", "Reference for motivation mechanics (path, streak, short sessions) - not a maths product"),
    ("Khan Academy Kids", "Reference for the 6-8 age group (almost no text, character-led)"),
]

WEIGHTED = {
    "ixl": 8.56, "khan": 8.26, "math": 7.82, "prodigy": 7.42,
    "quizizz": 6.95, "mihan": 5.81, "gama": 5.37, "porsan": 4.45,
}
RANK = {"ixl": 1, "khan": 2, "math": 3, "prodigy": 4, "quizizz": 5, "mihan": 6, "gama": 7, "porsan": 8}

PERSONAS = [
    dict(key="p1", name="Primary student", age="6-11", grades="Primary", color="#E4572E",
         need="Know 'what do I do now?' and start without reading a wall of text.",
         priorities=["One large, obvious start button", "Immediate, visual, non-blaming feedback",
                     "Visible progress (badge / reward / streak)", "Little text, more icons and pictures",
                     "A safe exit and an easy way back into the same exercise"],
         frustrates=["Multi-level menus and jargon", "Long instruction paragraphs",
                     "Negative scoring and a judgemental tone", "Losing the path after a dropped connection"]),
    dict(key="p2", name="Lower-secondary student", age="12-15", grades="Lower secondary", color="#1B8A83",
         need="In little time, find the weak skill and understand why the answer was wrong.",
         priorities=["Search and filter by textbook chapter", "Step-by-step solution after a wrong answer",
                     "Progress trend over several weeks", "A sense of agency: own choice, not only homework",
                     "A smooth mobile experience"],
         frustrates=["Cannot find the textbook topic", "'Wrong' with no explanation",
                     "Repeating easy questions", "A childish look for their age"]),
    dict(key="p3", name="Upper-secondary student", age="16-18", grades="Upper secondary", color="#6C4BB6",
         need="Targeted exam practice with the least possible friction.",
         priorities=["Focus on topic and difficulty level", "A precise performance report with weak spots",
                     "Save time: resume exactly where they stopped", "An adult, serious look - no heavy gamification",
                     "Keyboard and maths typing support"],
         frustrates=["Childish animation and characters", "Opaque scoring",
                     "No report they can rely on", "Complicated login or recovery"]),
    dict(key="p4", name="Teacher", age="25-50", grades="All three stages", color="#D9A03C",
         need="Assign the right work in minutes and move from report to action.",
         priorities=["Find a skill by grade / topic filter", "Assign to a class or a student, with a due date",
                     "Preview before publishing", "Class report showing the weakest skill",
                     "Go straight from the report to a remedial assignment"],
         frustrates=["Re-entering data for every assignment", "Numeric reports with no suggested action",
                     "No quiz builder on top of the existing question bank", "Managing several classes at once"]),
]

PERSONA_FIT = {
    "ixl": [9, 9, 10, 10], "khan": [8, 9, 9, 8], "math": [8, 8, 6, 8],
    "prodigy": [10, 6, 3, 6], "quizizz": [8, 8, 7, 8], "mihan": [6, 8, 5, 4],
    "gama": [3, 7, 8, 6], "porsan": [2, 8, 9, 2], "duolingo": [10, 7, 5, 2],
}

FINDINGS = [
    ("1", "IXL owns the gold standard for structure and feedback - not for visual language.",
     "Its skill library, SmartScore and step-by-step feedback are the strongest combination on the market. "
     "But its visual language and menu depth cannot be copied for a 9-15 year old Iranian student.",
     "8.56", "IXL weighted score"),
    ("2", "The practice loop is the weakest link in every Iranian product.",
     "MihanMaktab, Gama and Porsan sell content or answers instead of a practice session. None of them "
     "closes the loop question > feedback > worked solution > next question.",
     "4.45", "Porsan weighted score"),
    ("3", "Motivation must stay light, not become the product.",
     "Prodigy scores 10/10 for primary and 3/10 for upper secondary. Roshana needs one visual shell with "
     "three density modes - not three products.",
     "3 / 10", "Prodigy fit, upper secondary"),
    ("4", "A teacher report without a next action is a dead end.",
     "Most tools stop at a number. IXL is the only one that walks from the class list to a remedial "
     "assignment; that loop must be P0 for Roshana.",
     "10 / 10", "IXL teacher tooling"),
    ("5", "Roshana's opening: a short, Persian, decision-first path.",
     "Dashboard + simple skill library + Persian feedback with worked solutions + action-oriented teacher "
     "report does not exist as one integrated product in the Iranian market.",
     "0", "Iranian products with this combination"),
]

LANDSCAPE = [
    ("Global, mastery-first", ["IXL", "Khan Academy"], "Deep skill trees, standards mapping, strong reporting; heavy text, English-first."),
    ("Global, engagement-first", ["Mathletics", "Prodigy", "Quizizz"], "Competition, game worlds and live quizzes buy attention; feedback is thin."),
    ("Iranian, content-first", ["Gama.ir", "MihanMaktab"], "Large Persian libraries and textbook alignment; no adaptive practice loop."),
    ("Iranian, social-first", ["Porsan"], "Low friction questions and answers; unverified answers, no learning signal."),
]

PROFILES_EXTRA = {
    "ixl": "Deepest skill coverage; SmartScore is the most legible mastery number in the market.",
    "khan": "Best free, calm experience and the best mobile maths keypad; assignment path is buried.",
    "math": "Clear split between must-do (To Do), exploration and play; seven topic colours weaken hierarchy.",
    "prodigy": "Highest engagement for ages 7-11; the game hides the curriculum and locks content behind paywalls.",
    "quizizz": "Best single-question frame in the market; almost no instructional feedback.",
    "mihan": "Closest to the Iranian textbook; linear slides with no comprehension check.",
    "gama": "Largest Persian question bank; every path ends in a file download, not in practice.",
    "porsan": "Lowest friction to ask a question; answers are unverified and there is no practice at all.",
}


# ------------------------------------------------------------------ visual systems
COLOUR_NOTE = {
    "ixl": "Deep green for mastery, one coral accent for actions. Calm but text-heavy areas stay white.",
    "khan": "Near-black type on white with a single blue; the calmest and most legible system in the set.",
    "math": "Purple base with orange action colour; seven topic colours compete with the action colour.",
    "prodigy": "Dark violet world with warm orange rewards; colour carries narrative, not hierarchy.",
    "quizizz": "Purple stage with high-contrast answer cards; colour signals state during a live quiz.",
    "mihan": "Institutional blue with green accents; reads as a school portal rather than a learning app.",
    "gama": "Marketing green with red alerts; the only palette where the CTA competes with advertising.",
    "porsan": "Bright social blue; friendly, but indistinguishable from any social feed.",
}

LAYOUT_MODELS = [
    ("Library-first (IXL, Gama)",
     "A persistent tree on the left, content on the right. Scales to thousands of skills, but every new "
     "topic costs a level of depth."),
    ("Session-first (Quizizz, Khan exercise)",
     "One task fills the screen; navigation collapses to back and next. Best focus, worst for finding a "
     "specific skill."),
    ("Task-first (Mathletics, Khan home)",
     "The home screen is a list of duties with counters. Best for returning users with homework."),
]

PRACTICE_ANATOMY = [
    ("Question number", "Pinned top-left; tells the student how much is left."),
    ("Progress rail", "Session length, not mastery - a short-term commitment."),
    ("Question", "Largest type on screen; one question only."),
    ("Answer cards", "Full width, at least 44 px tall, shape plus colour for state."),
    ("Timer", "Optional; Roshana hides it by default for ages 6-11."),
    ("Next action", "Appears after feedback, in the same place every time."),
]

DASHBOARD_MODELS = [
    ("IXL - assignment-first",
     "Three panels: from my teacher, recent, recommendations. Personal greeting with an avatar and a "
     "'how am I doing' strip of three numbers.",
     "Copy: three panels, not ten; counters on duties; a greeting instead of a wall of statistics.",
     "Fix: homework hidden inside a tab; no 'resume where I stopped' action; a score without an explanation."),
    ("Khan - course-first",
     "My courses is the anchor; the assignment tab is visually quieter. Calm and readable, but a student "
     "with only homework has to hunt.",
     "Copy: one primary action per card; whitespace does the hierarchy work.",
     "Fix: assignments behind a tab; no pending-work counter."),
]
