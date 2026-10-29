# ROSHANA — Complete Master Project Context
**Purpose:** Source-of-truth context for AI research, competitive benchmarking, product strategy, and UX/UI design.

> This document consolidates the supplied Roshana product brief into a standalone English reference. It preserves source-stated requirements and distinguishes them from open decisions and research recommendations. It is not a completed competitive benchmark or a final technical specification.

## Evidence labels
- **[SOURCE FACT]** Explicitly stated in the supplied brief.
- **[INFERENCE]** A reasoned interpretation, not confirmed as a product decision.
- **[OPEN QUESTION]** A decision or detail that remains unresolved.
- **[MISSING SOURCE]** A referenced file or attachment that was not supplied.
- **[EXTERNAL RESEARCH REQUIRED]** A topic requiring evidence from external sources.

## Instructions for AI systems using this file
1. Treat the source-stated product facts and constraints as the baseline for all analysis.
2. Do not silently invent features, rules, metrics, personas, technical architecture, or business decisions.
3. Keep Roshana requirements separate from competitor features, general UX conventions, and your own recommendations.
4. When researching competitors, cite reliable evidence and record the product, source URL, access date, observed behavior, relevant user flow, and implications for Roshana.
5. Map findings to Roshana’s user needs, pages, flows, and MVP priorities. Do not recommend a feature solely because a competitor has it.
6. Preserve unresolved questions as open questions until the product owner approves them.
7. The referenced attachment listing 17 IXL question types is missing. Do not guess its contents or present a reconstructed list as the original attachment.
8. The source mentions 13 main pages, but the priority table's page counts may not reconcile cleanly. Verify the inventory rather than forcing totals to match.
9. Use the source brief as product context, not as proof that competitor claims or external assumptions are true.

---

## Detailed Product Brief (Consolidated Source Content)

**Document title:** Product Definition and Design Brief — Roshana  
**Subtitle:** A structured guide to the product, pages, interactions, and priorities  
**Source basis:** User-provided Persian DOCX, cross-checked against the accompanying PDF  
**Translation note:** This is an organized English translation of the source brief, not an independent product specification. Unresolved decisions remain explicitly unresolved.

## 1. Product Overview and Value Proposition

### 1.1 What is Roshana?
Roshana is a web-based learning platform for practicing and strengthening school skills. A student can practice a skill assigned by a teacher, recommended by the system, or independently selected from the skill library. After each answer, the student receives instructional feedback, reviews progress, and decides what to practice next. Teachers can find existing platform content, assign skills to a class or selected students, generate quizzes from the platform question bank, follow a teaching plan, and use analytics to support learning.

Reference products such as IXL help clarify the product category, but Roshana’s interaction model, brand, visual components, and experience must be designed independently around real user needs.

### 1.2 Problems to solve
- Students may not know what to practice, where to start, or how to learn the correct method after an incorrect answer.
- Students need immediate feedback, understandable progress indicators, and an experience that does not leave them confused.
- Teachers should not have to switch between disconnected tools to find skills, assign work, track due dates, and review each student’s status.
- Performance reports should go beyond displaying numbers and lead to a concrete instructional action, such as assigning follow-up practice.

### 1.3 Value proposition by primary user

| Student | Teacher |
|---|---|
| Find an appropriate skill quickly. | Find existing skills by subject, grade, topic, and class needs. |
| Practice varied questions and understand answers. | Create skill assignments and quizzes based on platform questions. |
| See progress, SmartScore, and achievements. | Review class progress, individual performance, and skills needing attention. |
| Continue practicing without losing the path. | Move directly from a report to a next action, such as assigning a skill. |

### 1.4 Core value loops
- **Student:** Sign in → see an assignment or recommendation → choose a skill → answer practice questions → receive feedback → review progress → continue or choose the next skill.
- **Teacher:** Review class status → select a skill or identify a learning gap → assign practice or generate a quiz → review results → decide on the next instructional support.

## 2. Users, Needs, and Contexts

### 2.1 Student
**Primary goal:** Know what to practice now, understand answers, see progress, and remain motivated to continue.

**Typical contexts:** Completing work with a due date; optional after-school practice; resuming an earlier session; using a system recommendation; viewing badges; spending virtual coins on items.

**UX needs:** Make the primary action obvious; use age-appropriate plain language; focus on one question at a time; provide non-punitive feedback; show whether progress has been saved; minimize friction when resuming practice.

### 2.2 Teacher
**Primary goal:** Create assignments quickly, track student activity, and make instructional decisions about areas of difficulty.

**Typical contexts:** Preparing a lesson; selecting a skill; assigning work to a class or selected students; creating a quiz; tracking due dates; reviewing reports; planning the next session.

**UX needs:** Support multiple classes; provide useful filters and multi-select; make recipients and due dates explicit; preview before publishing; allow a direct path from analytics to action.

## 3. MVP Scope, Confirmed Rules, and Priorities

### 3.1 Confirmed product decisions
- Users do not choose their role at sign-in. The system identifies the role after authentication.
- After sign-in, users land on the landing page for their role—not a generic dashboard or role-selection screen.
- The product is planned to be bilingual. The stated target audience is children aged **9–15**.
- The MVP focuses on mathematics. The brief estimates approximately **300 skills per grade**. Language and science are planned for later product development.
- Students receive a username and password from their school. A mechanism will allow students to enter a class code to join a class.
- Diagnostic assessment is **out of scope for the MVP**.
- Students may start a teacher-assigned, system-recommended, or self-selected skill.
- Teachers cannot author new questions or edit existing questions.
- Teachers can generate quizzes from existing platform questions by setting parameters.
- The skill-selection page and question-answering page are separate experiences: **Skill Library** and **Practice Session**.
- The MVP is a responsive web application, not a native Android or iOS application.

### 3.2 Source gap
The source numbering jumps from section **3.1** to **3.3**. No section 3.2 was present in either supplied file. Its content must not be inferred or invented.

### 3.3 Page priorities
The brief says all 13 main pages are within the expected scope; priority determines the order of design, testing, and delivery.

| Priority | Student pages | Teacher pages |
|---|---|---|
| **P0 — Core** | Sign in; Student Landing Page; Skill Library; Question page; Question Feedback page | Sign in; Teacher Landing Page; Skill Library; Class Management / Student List; Assignments; Performance Analytics |
| **P1 — MVP completion** | Recommendations; Performance Analytics (dashboard) | Quiz Generator; Timetable and Teaching Plan |
| **P2 — Motivation** | Honor Roll; Rewards Store | — |

## 4. Learning Content Model and Information Architecture

### 4.1 Learning content hierarchy
The conceptual content model is hierarchical. Users select a subject and grade, then navigate from topic to skill. In the skill library, topics may appear as expandable sections with their related skills nested underneath.

**Reference hierarchy:** Subject → Grade → Topic → Skill → Question.

The grade provides context for filtering and content organization. The conceptual model may also include subtopics. The design must support multiple skills under each subtopic without making navigation excessively long or complicated.

**Illustrative example:** Mathematics, Grade 4 → “Operations and Computation” → “Divide with remainders.” This example clarifies information structure only.

### 4.2 Student navigation model
- **Landing Page:** Quick access to assignments, resume practice, and recommendations.
- **Skill Library:** Search and browse skills independently.
- **Recommendations:** Skills recommended with a reason, topic grouping, and a start action.
- **Performance Analytics:** Individual results and progress.
- **Honor Roll and Rewards Store:** Achievements and coin-based personalization.
- **Practice Session:** Focused question-answering space with a safe exit.

### 4.3 Teacher navigation model
- **Landing Page:** Daily overview, classes, due dates, and urgent actions.
- **Skill Library:** Browse, preview, and select skills for assignments or quizzes.
- **Assignments:** Create, publish, and track skill assignments.
- **Quiz Generator:** Configure and generate a quiz from the question bank.
- **Timetable and Teaching Plan:** Review sessions, topics, and teaching plans.
- **Performance Analytics:** Class/student reports, learning gaps, and next actions.
- **Class Management and Student List:** Required support for selecting assignment recipients.

## 5. Student Page Requirements

For each page, the source defines its goal, required information, key interactions, states/scenarios, and design guidance. This is a basis for wireframes and effort estimation—not a final pixel-level specification.

### 5.1 Student Landing Page
**Goal:** Immediately after sign-in, the student should understand the top priority and start practicing with one clear action.

**Must show:**
- Assigned skills, teacher name, due date, and status.
- Overdue assignments and assignments nearing their due dates.
- A way to resume unfinished practice.
- Recommended skills and the reason for each recommendation.
- Daily/weekly goal summary.
- Recent progress, activity streak, coin balance, and latest badge.

**Key interactions:** Start or resume an assignment; open the Skill Library; view all recommendations; open Performance Analytics, Honor Roll, and Rewards Store.

**States/scenarios:** No assignments; multiple concurrent assignments; overdue assignment; no new recommendations; first visit; loading failure.

**Design guidance:** Give the most important assignment or nearest due date priority. Motivational content must not obscure the primary learning action.

### 5.2 Skill Library
**Goal:** Help students independently find and choose a skill through an understandable path.

**Must show:** Subject and grade selectors; relevant topics and subtopics; skills within each section; not started / in progress / completed status; existing SmartScore; assigned or recommended labels; and skill level or short description when available.

**Key interactions:** Change subject or grade; expand topics/subtopics; search or filter; start or resume a skill.

**States/scenarios:** No results for a filter; large content volume; long skill names; grade change; inaccessible content.

**Design guidance:** Keep the sequence Subject → Grade → Topic → Skill clear, and always show users where they are.

### 5.3 Recommendations
**Goal:** Help students understand which skill is appropriate for the next learning step and why.

**Must show:** Recommended skills; a short reason for each; grouping by topic or recommendation reason; prior progress; and a start/resume action.

**Key interactions:** Read the recommendation reason; go directly to practice; filter or browse recommendations by topic.

**States/scenarios:** Insufficient data; duplicate recommendation; already-completed skill; recommendation for inaccessible content.

**Design guidance:** Avoid vague labels such as “AI recommends” without a specific, understandable reason grounded in available data.

### 5.4 Student Analytics
**Goal:** Turn practice results into a simple, motivating picture of the student’s learning path.

**Must show:** Started and completed skills; progress by subject and topic; SmartScore trends when valid data exists; question count, answer accuracy, and practice time; recent activity; and goal progress.

**Key interactions:** Change time range or subject; open the related skill from a report; view topic details.

**States/scenarios:** New student; limited data; performance decline; comparison across periods; partial data access.

**Design guidance:** Reports must not feel judgmental. Charts should be readable and understandable, and should answer “What can I do next?”

### 5.5 Practice Session
**Goal:** Present one question at a time, capture the answer, provide instructional feedback, and continue practice.

**Must show:** Skill and topic name; question number; SmartScore; elapsed time; question text and media; input controls appropriate to the question type; submit action; and safe exit.

**Key interactions:** Submit an answer; see correct/incorrect feedback; read the correct answer and solution method; continue to the next question; exit and resume; view skill completion.

**States/scenarios:** Unanswered question; incomplete answer; submission in progress; correct answer; incorrect answer; network error/offline; recovery; completion.

**Design guidance:** Different question formats and feedback states should be independent components with consistent behavior. Score and time must not distract from the question.

### 5.6 Honor Roll
**Goal:** Show genuine achievements and progress worth celebrating.

**Must show:** Earned medals, badges, and certificates; achievement date; locked achievements and unlock criteria; progress toward the next badge.

**Key interactions:** View achievement details; view/download a certificate if approved; go to related practice.

**States/scenarios:** No achievements yet; unclear criteria; certificate unavailable.

**Design guidance:** Keep the experience encouraging rather than competitive. Avoid public rankings that create pressure for students.

### 5.7 Rewards Store
**Goal:** Spend earned virtual coins on avatars and personalization items.

**Must show:** Coin balance; items and prices; avatar/item preview; purchased / available / equipped states; owned items.

**Key interactions:** Preview an item; confirm purchase; select/equip a purchased item; return to practice.

**States/scenarios:** Insufficient coins; duplicate purchase; coin transaction error; balance changed; item already equipped; empty store.

**Design guidance:** In the MVP, purchases use in-product virtual coins, not real money. Clearly explain purchase confirmation and coin deduction.

## 6. Teacher Page Requirements

### 6.1 Teacher Landing Page
**Goal:** Provide an action-oriented overview of what the teacher should review or do today.

**Must show:** Classes and today’s schedule; active, upcoming, and overdue assignments; recent student results/activity; skills or students needing attention; class progress summary; quick actions for assigning skills, creating quizzes, and opening reports.

**Key interactions:** Select active class; open assignments; create an assignment or quiz; open analytics and timetable.

**States/scenarios:** No classes; multiple classes; many assignments; repeated alerts; first visit.

**Design guidance:** Make the active class and time range explicit on all cards. Do not hide actionable information beneath decorative charts.

### 6.2 Teacher Skill Library
**Goal:** Review and assess existing skills for teaching, assignments, and quizzes.

**Must show:** Subject, grade, topic, and subtopic selectors; skill list; learning objective, level, and sample content; sample platform questions; class performance for a skill when valid data exists.

**Key interactions:** Search/filter; open preview; select one or multiple skills; add selected skills to an assignment, quiz, or teaching plan.

**States/scenarios:** No skills available; no sample question; multiple selection; filter changes; content outside the relevant grade.

**Design guidance:** Multi-select and a clear summary of selected skills are required. Do not design controls for teachers to create or edit questions.

### 6.3 Assignments
**Goal:** Select existing skills, specify recipients and due dates, and track class assignments.

**Must show:** Active, scheduled, completed, and overdue assignments; class and recipients; skills and due date; each student’s status; a calendar or due-date view.

**Key interactions:** Create assignment; select class or students; choose one or more skills; set due date and short instructions; review and publish; track/edit/cancel according to approved rules.

**States/scenarios:** No recipient selected; invalid date; duplicate assignment; cancellation after a student has started; publishing failure.

**Design guidance:** Before publishing, clearly summarize “which skills, for whom, and by when.” Policies for changes after students start must be defined.

### 6.4 Quiz Generator
**Goal:** Generate a quiz from existing platform questions using teacher-defined settings.

**Must show:** Class/student selection; subject/grade/topic/skill; approved parameters such as question count, level, and time; generated-question preview; publishing settings and result visibility if approved.

**Key interactions:** Enter parameters; generate quiz; preview and regenerate; review and publish.

**States/scenarios:** Insufficient question bank; impossible parameter combination; generation in progress; published quiz; publishing failure.

**Design guidance:** Teachers do not create or edit questions. If there are too few questions, offer clear options such as reducing the count or changing filters.

### 6.5 Timetable and Teaching Plan
**Goal:** Help teachers view scheduled sessions and organize the sequence of teaching and learning activities.

**Must show:** Day/week and, if needed, month views; classes and lesson times; planned topic/skill; lesson status; assignment and quiz due dates with clear visual distinctions.

**Key interactions:** View/edit the teaching plan where permitted; select a topic or skill; mark a lesson complete; create an assignment or quiz from a plan item.

**States/scenarios:** Schedule conflicts; empty schedule; class change; cancelled session; invalid date.

**Design guidance:** Scheduled classes, teaching-plan items, assignments, and quizzes are different event types, but should link to one another.

### 6.6 Teacher Analytics
**Goal:** Identify students or skills needing attention and turn data into instructional action.

**Must show:** Class summary; assignment and quiz status; performance by subject/topic/skill; individual student reports; SmartScore, accuracy, or time when valid data is available; students and skills needing support.

**Key interactions:** Select class, student, subject, and time range; open skill details; compare progress over time; select and assign remedial practice.

**States/scenarios:** Insufficient data; new class; skill with no answers; empty chart; unauthorized data access.

**Design guidance:** Every metric needs an understandable definition. Avoid labels such as “weak” without an explainable basis; make the path from report to action short.

**Additional role note:** The source says parent and school-administrator pages resemble the other roles, with different analytics indicators. It does not provide complete page specifications or separate user flows for these roles.

## 7. Twenty Core User Flows

### 7.1 Ten student flows

1. **Sign in and reach landing page**  
   Goal: The student signs in and sees the appropriate page without choosing a role.  
   Path: Sign in → account validation → Student Landing Page.  
   Branches: Failed sign-in; password recovery; initial loading.

2. **Start a teacher assignment**  
   Goal: Find a due-dated assignment and start the relevant skill.  
   Path: Landing Page → assignment card → skill view → Practice Session.  
   Branches: Overdue assignment; completed assignment; multiple assignments with different due dates.

3. **Resume unfinished practice**  
   Goal: Resume from the last saved state.  
   Path: Landing Page → Resume practice → restore question/score → next answer.  
   Branches: Unsaved progress; inconsistent state; network interruption.

4. **Choose a skill independently**  
   Goal: Browse topics and subtopics and choose a skill by subject and grade.  
   Path: Skill Library → subject/grade → topic/subtopic → skill → start.  
   Branches: Empty filter results; crowded topic; skill in progress.

5. **Use a system recommendation**  
   Goal: Understand the recommendation reason and enter practice.  
   Path: Landing Page/Recommendations → reason → choose skill → practice.

6. **Answer a question and receive feedback**  
   Goal: Answer and learn from correct/incorrect feedback.  
   Path: Show question → enter/select answer → submit → evaluate → feedback → continue.  
   Branches: Empty answer; incorrect answer; duplicate submission or delayed API response.

7. **Exit and return to practice**  
   Goal: Leave without losing a confirmed answer and resume later.  
   Path: Practice Session → exit → preserve state → return → resume.  
   Branches: Disconnection; save in progress; exit during submission.

8. **Review progress and choose the next step**  
   Goal: Understand progress and identify suitable next practice.  
   Path: Landing Page → Analytics → filter by subject/topic → next skill.  
   Branches: No history; sparse chart data; declining performance.

9. **View achievements**  
   Goal: See badges/certificates and their earning criteria.  
   Path: Landing Page → Honor Roll → achievement/certificate details.  
   Branches: No badges yet; locked badge; certificate unavailable.

10. **Spend coins and equip an avatar item**  
    Goal: Purchase a virtual item with a clear understanding of balance and outcome.  
    Path: Landing Page → Store → preview → confirm purchase → equip.  
    Branches: Insufficient coins; duplicate purchase; transaction error.

### 7.2 Ten teacher flows

1. **Sign in and reach landing page**  
   Goal: See classes and urgent actions after sign-in.  
   Path: Sign in → role identification → Teacher Landing Page.  
   Branches: No class; failed sign-in; data error.

2. **Select/create a class and manage the roster**  
   Goal: Select an active class and manage its student list.  
   Path: Landing Page → Classes → select/create class → student list.  
   Branches: Empty class; invalid invitation; duplicate member. The joining mechanism needs approval.

3. **Browse and preview a skill**  
   Goal: Evaluate a ready-made skill before using it.  
   Path: Teacher Skill Library → subject/grade/topic → select skill → preview.  
   Branches: No sample question; empty filter results.

4. **Assign skills to a class**  
   Goal: Assign multiple skills to the entire class with a due date.  
   Path: Library/Assignments → skills → class → due date → review → publish.  
   Branches: Missing recipient or skill; due-date conflict; publishing failure.

5. **Create targeted work for selected students**  
   Goal: Create a targeted assignment based on a specific learning need.  
   Path: Analytics → select students → skill → due date → publish.  
   Branches: Preserve selection; student no longer belongs to the class.

6. **Manage assignments and due dates**  
   Goal: Review active and overdue work and make permitted changes.  
   Path: Assignments → filter by class/status → details → allowed action.  
   Branches: Student has started; cancellation or due-date extension; concurrent change.

7. **Generate and publish a quiz**  
   Goal: Build a quiz from the platform bank using defined parameters.  
   Path: Quiz Generator → skills/settings → generate → preview → publish.  
   Branches: Insufficient questions; generation failure; regenerate; result-display rules.

8. **Plan a teaching session**  
   Goal: Connect topics and skills to the teaching schedule.  
   Path: Timetable → session → teaching plan → choose skill → save.  
   Branches: Date change; empty schedule; time conflict.

9. **Identify a class learning gap**  
   Goal: Identify a skill needing attention from a report.  
   Path: Analytics → class → topic/skill → inspect pattern → take action.  
   Branches: Insufficient data; metric definition; non-judgmental presentation.

10. **Review an individual student and provide support**  
    Goal: Review one student’s report and assign appropriate practice.  
    Path: Analytics → student → skill reports → next assignment.  
    Branches: Data privacy; no student activity; preserve selection context.

## 8. Product Rules and Required Behaviors

### 8.1 Sign-in, roles, and permissions
- A shared sign-in form or approved sign-in flow should route users to the correct landing page after identification.
- Role switching is not part of the sign-in screen. Whether one account can hold multiple roles is undefined.
- Students can see only their own reports and assets. Teachers can see only authorized class/student reports.
- Expired sessions, invalid access, inactive accounts, and password recovery need clear and secure experiences.

### 8.2 Practice and feedback lifecycle

| Stage | Expected behavior |
|---|---|
| Before answering | Show skill name, question number, SmartScore, and time; keep focus on the question. |
| Answer entry | Use controls appropriate to the question type; identify incomplete/invalid answers before submission. |
| Submitting | Prevent duplicate submissions and clearly show that the answer is being checked. |
| Correct answer | Brief positive feedback, correct answer, updated score, and a Continue action. |
| Incorrect answer | Show the correct answer, explanation, and solution method without blame; allow continuation. |
| Exit/recovery | Clearly show save status; label progress as saved only after confirmation. |
| Completion | Summarize progress and, if available, rewards; provide the next action and a way back to the originating context. |

### 8.3 Question formats and form design
Each question type needs its own input pattern, error handling, feedback display, and accessible behavior. The exact number and names of MVP formats must be confirmed against the final answer-type specification. Examples in the source:
- **Multiple choice:** Select one option; show the correct option and an explanation.
- **Short or numeric answer:** Validate text/number input, explain expected format, and handle equivalent answer forms.
- **Matching:** Connect/select pairs and provide a keyboard-accessible alternative to drag-and-drop.

The source refers to an attachment containing **17 IXL question types**, but that attachment was not included in the supplied files.

### 8.4 Assignment rules
- An assignment can contain one or more skills and target either a whole class or selected students.
- Before publishing, review must make skills, recipients, due date, and instructions explicit.
- Editing, extending, cancelling, and reassigning an assignment after a student starts are still subject to approval.
- Assignment statuses must use consistent definitions in teacher and student experiences.

### 8.5 Quiz generator rules
- Teachers select permitted parameters; the system selects questions from its existing bank.
- Quiz preview and a way to return and adjust parameters are required.
- If there are not enough questions, explain the limitation in plain language.
- Final parameters still require approval: question count, difficulty/level, time, retries, question order, and when results are shown.
- The student experience for “taking a quiz” must be defined: a separate Practice Session mode or a separate page.

### 8.6 Recommendations, analytics, and gamification
- Recommendations will be generated without an initial diagnostic assessment, based on practice history, assignments, and relationships between skills.
- Each recommendation must include a clear, understandable reason. If data is insufficient, recommendations should not be forced.

## 9. Shared States, UX Writing, and Non-functional Needs

### 9.1 Required shared states

| State | Design expectation | Roshana example |
|---|---|---|
| Loading | Show progress or skeleton UI; prevent duplicate actions. | Loading class report |
| Empty | Explain why no content is present and suggest an action. | No assignments have been recorded yet |
| Error | Explain the issue and recovery action; clarify what data was retained. | Assignment was not published; try again |
| Offline | Show connection and actual save status. | Connection lost; answer not confirmed |
| Success | Give brief confirmation and a relevant next action. | Assignment published; view list |
| Confirmation | Explain consequences before a consequential action. | Confirm coin purchase / publish quiz |
| Permission | Deny access without exposing another user’s data. | You do not have access to this class report |
| Conflict | Prevent silent overwrite or hidden changes. | Another user changed the assignment due date |

### 9.2 Content and UX writing rules
- **Student language:** Short, precise, respectful, and encouraging. Example: “Your answer is correct. Ready for the next question?”
- **Incorrect-answer feedback:** Instructional and non-judgmental. Example: “That answer isn’t correct; let’s look at the solution method together.”
- **Teacher language:** Operational and data-based. Example: “Five students have not yet completed practice for this skill.”
- **Error messages:** State what happened, what was saved, and what the user can do next.
- Use consistent meanings for **Start**, **Continue**, **Completed**, **Assigned**, and **Recommended** across the product.

## 10. Unified Product Glossary

| Term | Meaning in Roshana |
|---|---|
| **Skill Library** | Place to browse subjects, grades, topics, subtopics, and choose a skill. |
| **Practice Session** | Environment for answering questions with score and feedback. |
| **Assignment** | One or more skills published by a teacher for a student or class. |
| **Quiz** | A set of questions selected from the existing bank using teacher-defined parameters. |
| **SmartScore** | A skill-performance/progress metric; its formula and precise meaning still require approval. |
| **Recommendation** | A system-suggested skill accompanied by an understandable reason. |

## Source-Control Notes and Open Questions

The following are not resolved by the supplied brief and must not be silently filled in:

1. **Missing section 3.2:** Numbering jumps from 3.1 to 3.3 in both supplied files.
2. **Missing question-type attachment:** The brief references 17 IXL question formats, but the attachment is absent.
3. **SmartScore:** Formula, meaning, thresholds, and display rules are not defined.
4. **Roles:** Parent and school-administrator analytics are mentioned, but detailed pages, permissions, and user flows are not specified. Multi-role accounts are also unresolved.
5. **Class joining:** A student class-code mechanism is mentioned, but the full join/invitation rules are not defined.
6. **Assignment changes:** Rules for editing, extending, cancelling, or reassigning after practice starts need approval.
7. **Quiz parameters:** Question count, level, time, retries, ordering, result visibility, and the student quiz interface need final decisions.
8. **MVP question formats:** The exact supported formats and validation rules need confirmation.
9. **Age range:** The source states ages 9–15. Any broader audience must be confirmed separately rather than assumed.
10. **Bilingual implementation:** The brief says bilingual, but does not define the full localization rules for Persian/English, RTL/LTR, numerals, dates, or calendar systems.
11. **Analytics:** Metric definitions, thresholds, and rules for identifying learning gaps need explicit definitions.
12. **Scheduling:** Calendar conventions, lesson editing permissions, and conflict-handling policies need clarification.
13. **Authentication:** Password reset, inactive-account handling, expired sessions, and role-permission details require specification.

## Evidence and interpretation policy
- **Source-stated:** Explicitly described in the supplied brief.
- **Needs approval / open:** Explicitly identified as undecided or requiring approval.
- **Not provided:** Not specified in the supplied files.
- Do not treat competitor conventions or general UX practice as Roshana requirements unless separately researched and clearly labeled.


---

## 11. Additional Consolidated Product Context

### 11.1 Product and user summary
- **Product:** Roshana is a responsive web learning platform for practicing and strengthening school skills.
- **Primary users:** Students aged 9–15 and teachers.
- **MVP subject:** Mathematics, with approximately 300 skills estimated per grade. Language and science are planned for later development.
- **Student skill entry points:** Teacher-assigned, system-recommended, or independently selected from the Skill Library.
- **Teacher capabilities:** Browse existing skills, assign one or more skills to a class or selected students, generate quizzes from the existing question bank, and use analytics to inform instructional action.
- **Explicit MVP exclusions:** Initial diagnostic assessment and native Android/iOS applications.
- **Question-authoring constraint:** Teachers cannot create new questions or edit existing questions.
- **Practice structure:** Skill Library and Practice Session are distinct experiences.

### 11.2 Content hierarchy
The source describes the content hierarchy as:

**Subject → Grade → Topic → Subtopic → Skill → Question**

The English source also presents a shorter version without Subtopic. Preserve Subtopic as part of the more detailed model, while noting that the source expresses the hierarchy in both forms. Confirm the canonical content model with the product owner before implementing the information architecture.

### 11.3 Student experience requirements
The student experience should make the next action obvious, use plain age-appropriate language, focus attention on one question at a time, provide non-punitive instructional feedback, show confirmed save status, and make it easy to resume practice. Progress and analytics should be motivating rather than judgmental. Public rankings that create harmful pressure are explicitly discouraged.

### 11.4 Teacher experience requirements
The teacher experience should support multiple classes, useful filters and multi-selection, explicit recipient and due-date summaries, preview before publishing, and a short path from analytics to assigning follow-up practice. Metrics must have clear definitions and should not label students as “weak” without an explainable basis.

### 11.5 Parent and school-administrator roles
The source briefly mentions parent and school-administrator views with different analytics indicators. It does **not** provide complete page specifications, permissions, or dedicated user flows for these roles. Treat their existence as source-stated, but their detailed experiences as unresolved.

---

## 12. Consolidated Open Questions and Missing Inputs

These questions must remain open unless the product owner or a verified source resolves them:

| ID | Topic | What is known | What remains unresolved |
|---|---|---|---|
| OQ-01 | Bilingual experience | The product is intended to be bilingual. | Second language, language switching, RTL/LTR behavior, numeral/date formats, and calendar conventions. |
| OQ-02 | Multiple roles per account | Roles are identified after authentication; users do not choose a role at sign-in. | Whether one account can hold multiple roles and how role switching would work. |
| OQ-03 | Joining a class | Students are expected to have school-provided credentials and a class-code mechanism is mentioned. | Full join/invitation flow, teacher approval, invalid/expired codes, and duplicate membership behavior. |
| OQ-04 | SmartScore | It is the principal skill-level progress/performance indicator. | Formula, meaning, thresholds, increase/decrease rules, and display behavior. |
| OQ-05 | Assignment changes | Assignments can contain one or more skills and target a class or selected students. | Editing, extending, cancelling, and reassigning after a student has started. |
| OQ-06 | Quiz parameters | Teachers configure a quiz generated from existing questions. | Final supported parameters, including count, difficulty, time, retries, ordering, and result visibility. |
| OQ-07 | Student quiz experience | A quiz can be generated and published by a teacher. | Whether students use a separate quiz page or a distinct mode of Practice Session. |
| OQ-08 | Question formats | Multiple choice, short/numeric answer, and matching are examples in the supplied English brief. | The authoritative list of MVP formats and validation rules. |
| MS-01 | Missing 17-type IXL attachment | The source references an attachment with 17 IXL question types. | The actual attachment and its exact list are not present in the supplied files. |
| OQ-09 | Achievements | Honor Roll may display medals, badges, and certificates. | Award criteria, unlock rules, and certificate download policy. |
| OQ-10 | Privacy and permissions | Students see their own data; teachers see authorized class/student data. | Detailed privacy policy, access boundaries, and parent/admin permissions. |
| OQ-11 | Analytics definitions | Student and teacher analytics are required. | Metric definitions, thresholds, and rules for identifying learning gaps. |
| OQ-12 | Scheduling | Timetable and teaching-plan functionality is listed. | Editing permissions, calendar conventions, and conflict handling. |
| OQ-13 | Authentication edge cases | School-provided credentials are described. | Password recovery, inactive accounts, expired sessions, and account recovery details. |
| OQ-14 | Page inventory | The brief refers to 13 main pages and provides P0/P1/P2 priorities. | Reconciliation of the stated total with the pages listed in the priority table and detailed page sections. |
| MS-02 | Missing source section | Numbering jumps from section 3.1 to 3.3 in the supplied brief. | Whether a section 3.2 existed in another version or was intentionally omitted. |

---

## 13. Competitive Benchmarking Protocol

This section describes how a research model should use this context. It does not contain completed benchmark findings.

### 13.1 Benchmark objectives
Research products that can provide evidence about:
- Skill discovery and learning-content navigation.
- Student landing pages, assignments, and resuming practice.
- Question interaction patterns and instructional feedback.
- Recommendations and explanation of recommendation reasons.
- Student progress analytics and teacher analytics.
- Class management, assignments, and quiz generation.
- Motivation systems, achievements, and virtual rewards.
- Responsive web experiences and bilingual/localized educational UX.

IXL is a relevant reference product mentioned in the source brief, but the benchmark should not be limited to IXL. Select additional competitors or adjacent products based on functional relevance and explain the selection criteria.

### 13.2 Required research method
For each competitor:
1. Identify the product, target audience, platform, geography/language, and relevant user roles.
2. Use official product pages, help documentation, product demos, and other reliable sources first. Use reviews or community reports as supplementary evidence, not as the sole basis for factual claims.
3. Record each finding with a source URL and access date.
4. Separate directly observed behavior from claims made by the vendor and from researcher interpretation.
5. Map each observation to a Roshana page, user flow, requirement, and priority.
6. Record unavailable or unverified information as unknown; do not infer functionality from screenshots alone.
7. Include screenshots or visual references only when legitimately accessible and useful, and document which interaction or state they demonstrate.
8. Do not reproduce competitor UI wholesale. Extract patterns and trade-offs, then evaluate suitability for Roshana’s audience and constraints.

### 13.3 Suggested comparison matrix
Use one row per observed feature or flow, with these columns:

| Field | Description |
|---|---|
| Competitor | Product name and relevant plan/version if known |
| Capability / flow | The behavior being studied |
| User role | Student, teacher, parent, administrator, or other |
| Evidence | Concise factual observation |
| Source | Direct URL and access date |
| Evidence quality | Official documentation, direct observation, secondary source, or unverified |
| Roshana mapping | Relevant page, flow, or requirement |
| UX benefit | User problem addressed |
| Trade-off / risk | Complexity, distraction, privacy, accessibility, or implementation cost |
| Roshana applicability | Applicable, possibly applicable, not applicable, or needs validation |
| Priority | P0, P1, P2, or not yet prioritized |
| Recommendation | Adopt, adapt, test, or reject—with rationale |

### 13.4 Benchmark deliverables
The research output should include:
- Competitor selection rationale.
- A feature and user-flow comparison matrix.
- Evidence-backed patterns and meaningful differences.
- Screenshots or annotated references where useful.
- Strengths, weaknesses, and trade-offs—not just feature checklists.
- Opportunities and gaps relevant to Roshana’s confirmed MVP.
- Recommendations separated into **must-have for MVP**, **consider for later**, and **do not recommend without validation**.
- A list of unresolved Roshana product decisions that block a reliable comparison.
- Citations for all external factual claims.

### 13.5 Research safeguards
- Never describe a feature as present in Roshana merely because a competitor has it.
- Do not treat competitor practices as automatically best practice.
- Do not make unsupported claims about children’s behavior, learning outcomes, or accessibility.
- For accessibility, investigate relevant standards and practical keyboard/screen-reader behavior for educational interactions. Mark external research as external research.
- Evaluate motivational systems against the source’s explicit constraint against harmful public ranking.
- Respect student privacy and age-appropriate design.
- Distinguish verified evidence, assumptions, and recommendations throughout the report.

---

## 14. Compact AI Context

Use this short context when a tool has a limited prompt budget:

> You are researching product and UX/UI benchmarks for Roshana, a responsive bilingual web learning platform for students aged 9–15 and teachers. The MVP focuses on mathematics, with approximately 300 skills per grade. Students can practice teacher-assigned, system-recommended, or self-selected skills; they receive instructional feedback and track progress. Teachers browse existing content, assign skills to classes or selected students, generate quizzes from the existing question bank, and review analytics. Teachers cannot author or edit questions. The Skill Library and Practice Session are separate experiences. Initial diagnostic assessment and native mobile apps are outside the MVP. The source lists P0/P1/P2 pages and 20 core user flows. SmartScore rules, quiz parameters, class-joining details, some role permissions, localization rules, and assignment-change policies remain unresolved. The source references a missing attachment containing 17 IXL question types; do not guess its contents. Separate source facts, external evidence, inference, and recommendations. Cite external findings and map them to Roshana requirements and MVP priorities.

---

## 15. Source and Quality-Control Notes

### Supplied source files
- `rowshana_design_brief_farsi.docx`
- `rowshana_design_brief_farsi.pdf`
- `roshana_design_brief_en(1).md` — an organized English translation of the supplied brief.

The Persian master and the English translation should be treated as versions of the same underlying product brief, not as independent evidence that a requirement is correct. The English file states that it was cross-checked against the Persian DOCX and PDF. The available materials do not include the referenced 17-type question attachment.

### Quality-control cautions
- The source says there are 13 main pages, but page totals should be checked against the page-priority table and detailed page descriptions.
- The source numbering skips section 3.2.
- The content hierarchy appears in both a shorter form (Subject → Grade → Topic → Skill → Question) and a more detailed form including Subtopic. Confirm the canonical model.
- Parent and school-administrator roles are mentioned, but their detailed experiences are not specified.
- SmartScore is named but its formula is not defined.
- The exact MVP question formats are not confirmed by the missing attachment.

**This file is the master context for beginning research. It is not a substitute for the missing attachment, product-owner decisions, or a completed evidence-based competitive benchmark.**
