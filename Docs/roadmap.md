
---

# ✅ FifthBlock Roadmap 

## Purpose

**FifthBlock** is a ground-up rebuild of the original *FifthBlock (v1)* repository.
The goal is to preserve the **same feature set** while dramatically improving:

* Code organization
* Documentation
* Maintainability
* Portfolio quality

This version emphasizes **clean architecture, phased development, and traceable decisions**.

---

## Phase 0 — Rebuild Preparation (Completed)

* [x] Create new repository for v2
* [x] Establish documentation-first workflow
* [x] Add project overview and tech stack
* [x] Separate v2 from legacy v1 codebase

---

## Phase 1 — Application Foundation

**Goal:** Establish a stable, production-quality Flask foundation.

* [x] Create Flask application factory (`create_app`)
* [x] Configure environment-based settings
* [x] Initialize SQLAlchemy instance
* [x] Create base project layout
* [x] Add `.env.example` and config loading
* [x] Verify app boots successfully

**Deliverable:**
Minimal Flask app that runs with no features enabled.

---

## Phase 2 — Core User Models & Authentication

**Goal:** Rebuild authentication cleanly with clear role separation.

<<<<<<< Updated upstream
* [x] Auth blueprint scaffolded
* [x] Login / logout flow
* [x] Session management
* [x] Centralized auth helpers
* [x] Role-based access decorators
* [x] Role-based access control helpers
* [x] Unauthorized access redirects

=======
* [x] Define base User model
* [x] Implement Teacher, Student, Parent models
* [x] Password hashing & verification
* [x] Auth blueprint (login / logout / signup)
* [x] Session management
* [x] Role-based access control helpers
>>>>>>> Stashed changes

**Deliverable:**
Authentication works and access control is enforced consistently across roles
---

## Phase 3 — Teacher Experience (Course Management)

**Goal:** Restore teRebuild the data layer cleanly using v1 as a reference.

* [ ] Course model
* [ ] Module model
* [ ] Quiz model
* [ ] CRUD routes for courses and modules
* [ ] Teacher dashboard UI
* [ ] Course publishing logic

**Deliverable:**
Teachers can create and manage courses and content.

---

## Phase 4 — Student Experience

**Goal:** Enable students to interact with assigned coursework.

* [ ] Student dashboard
* [ ] Course enrollment logic
* [ ] View assigned courses and modules
* [ ] Quiz-taking interface
* [ ] Submission handling

**Deliverable:**
Students can view coursework and take quizzes.

---

## Phase 5 — Quiz Engine & Grading

**Goal:** Implement reliable assessment and grading logic.

* [ ] Question and Answer models
* [ ] QuizAttempt model
* [ ] StudentResponse model
* [ ] Automatic scoring
* [ ] Grade persistence
* [ ] Teacher quiz review view

**Deliverable:**
Completed quizzes are graded and stored correctly.

---

## Phase 6 — Communication System

**Goal:** Rebuild messaging from v1 in a cleaner, documented form.

* [ ] Message model
* [ ] Inbox / sent views
* [ ] Student ↔ Teacher messaging
* [ ] Context-aware messages (course-related)

**Deliverable:**
Users can communicate within the platform.

---

## Phase 7 — Reporting & Analytics

**Goal:** Provide meaningful feedback on student progress.

* [ ] Student performance reports
* [ ] Quiz attempt history
* [ ] Simple analytics visuals
* [ ] Teacher insights dashboard

**Deliverable:**
Clear progress tracking for students and teachers.

---

## Phase 8 — UI Polish & UX Improvements

**Goal:** Improve clarity, accessibility, and responsiveness.

* [ ] Consistent layout templates
* [ ] Mobile-friendly student views
* [ ] Flash messages & validation
* [ ] Error handling pages

**Deliverable:**
App feels cohesive and usable.

---

## Phase 9 — Production Readiness

**Goal:** Prepare v2 for real deployment.

* [ ] PostgreSQL compatibility
* [ ] Database migrations
* [ ] Gunicorn config
* [ ] Deployment documentation
* [ ] Final README updates

**Deliverable:**
Deployment-ready LMS with professional documentation.
