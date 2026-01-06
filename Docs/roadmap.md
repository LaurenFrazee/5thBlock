
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

* [ ] Create Flask application factory (`create_app`)
* [ ] Configure environment-based settings
* [ ] Initialize SQLAlchemy instance
* [ ] Create base project layout
* [ ] Add `.env.example` and config loading
* [ ] Verify app boots successfully

**Deliverable:**
Minimal Flask app that runs with no features enabled.

---

## Phase 2 — Core User Models & Authentication

**Goal:** Rebuild authentication cleanly with clear role separation.

* [ ] Define base User model
* [ ] Implement Teacher, Student, Parent models
* [ ] Password hashing & verification
* [ ] Auth blueprint (login / logout / signup)
* [ ] Session management
* [ ] Role-based access control helpers

**Deliverable:**
Users can authenticate and land on role-appropriate dashboards.

---

## Phase 3 — Teacher Experience (Course Management)

**Goal:** Restore teacher control over learning content.

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
