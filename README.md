# Artificial Intelligence Requirement Engineering
AI-powered web system to bridge the gap between unstructured client requirements and structured software artifacts.


# Project Plan

## Step 1 : Goal Formulation

- Why am I making this project?
  I am making this project for simplify the Software development process by defining best RE model and automating the process.

- Who is this project for?
  This project main target is the startup software companies, and the employees
  1. PM
  2. QA
  3. BA
  4. Devs

- What is gonna make it valuable?
  obviously its,
  - Reduce **Time** duration of the development.
  - Reduce the **Cost** because of the clear idea at initial stage.
  - Reduce complexity because we have the actual **Scope** of the project.

## Step 2 : User Stories (What User able to do or interact with this system)

### Stakeholder Type-01: Company Clients

- As a Client I want to chat with company any time ,give my requirenement and check the progess so I can satisfy and understand shedule my own things

### Stakeholder Type-02: Company Employers

**These are the raw user stories not from actual experts I have to collect them maually by collectin data or by researching**

- As Project Manager I want to eveluate the Cost, Time and Scope of the project
- As QA I want to write test case and evaluate quality of the software product
- As a BA I want to collect requirenment without any complexity in the requirenment
- As a Developer I want build software without any repeaition and make thing worse

## Step 3 : Defining project Data model (What are the data here we are going to store?)

- requirements
  - requirement_id PK (the token)
  - json_requirement complete structured requirement JSON
  - source 'chatbot' | 'audio'
  - submitted_at timestamp

- ba_outputs
  - output_id PK
  - requirement_id FK → requirements
  - user_stories JSON
  - functional_label 'Functional' | 'Non-Functional'
  - generated_at timestamp

- pm_output,

- dev_output

## Step 4 : Minimum Viable Product (MVP)

#### V01

- input : raw text as requirenment
- process : classify text into different relevent term words
- Model : basic superwise models for analyse quality of requirenment
- output : User Stories

## Step 5 : Basic WireFrame

- Basic HTML & CSS front end takes input
- flask back end process things
- Again output send back to front end

## Step 6 : Final version

- Visit proposal
