---
title: Web-Scraping Data
layout: default
nav_order: 3
---

# Web-Scraping Reddit

> 2023-02-06

An easy way to retrieve data from Reddit is through the PushShift.io API Wrapper [**PMAW**](https://github.com/mattpodolak/pmaw), [**PSAW**](https://psaw.readthedocs.io/en/latest/), or [**PRAW**](https://praw.readthedocs.io/en/stable/). Unfortunately, these wrappers do not have access to posts in certain timeframes.

As a result, files.PushShift.io is utilized due to its 100% operational status as seen [here](https://stats.uptimerobot.com/l8RZDu1gBG). Screenshot taken on Jan 17, 2023:

<p align="center">
  <img src="assets/Pushshift_status.png"
  width = "50%">
</p>

## The following scripts were used:

**1.**  [filePushshiftpull.py](https://github.com/JLS-bz/JLS-bz.github.io/blob/main/scripts/filePushshiftpull.py)
  - Automates the downloading of compressed .zst files from [files.pushshift.io](https://files.pushshift.io/reddit/submissions/). 
  - Date range: **2019-11 to 2021-02**
    -*TBA: 2019-11 to 2022-11*
  

**2.**  PushshiftDumps by Watchful1

a) [combine_folder_multiprocess.py](https://github.com/Watchful1/PushshiftDumps/blob/master/scripts/combine_folder_multiprocess.py)

Converts a folder of .zst files into decompressed .ndjson and individual subreddit specific .zst files.

b)  [to_csv.py (adapted)](https://github.com/JLS-bz/JLS-bz.github.io/blob/main/scripts/to_csv.py)

Converts and processes subreddit specific .zst files into decompressed .csv files.
  - Only information falling under the following columns are kept: subreddit, title, selftext, score, num_comments, created_utc.
  - Columns 'title' and 'selftext' are combined to create column 'post', then dropped.
  - Combines individual subreddit specific .zst files according to general topics of interest.

## List of general topics and their respective subreddits:

  - **Autism/ADHD**: adhd_anxiety, ADHD, adhdwomen, asd, autism, AutisticWithADHD, aspergers
  - **Anxiety/Depression**: SuicideWatch, depression, depression_help, Anxiety, AnxietyDepression, Anxietyhelp, socialanxiety, HealthAnxiety, anxietysuccess
  - **COVID**: COVID19positive, covidlonghaulers
   - **Dissociation**: dpdr, dpdrhelp, Dissociation, Depersonalization, derealization, DPDRecoveryStories, OSDD, anhedonia, BrainFog, Psychosis
  - **Drugs/addiction related**: leaves, zoloft, Drugs, addiction, REDDITORSINRECOVERY, opiates, Psychonaut, benzorecovery, HPPD
  - **LGBT**: lgbt, GenderDysphoria, ftm, MtF, trans, NonBinary
  - **PTSD and Personality Disorders**: CPTSD, PTSD, ptsdrecovery, NarissisticAbuse, raisedbynarcissists, BPD, BPDlovedones, BorderlinePDisorder, BPD4BPD, BPDPartners

----
