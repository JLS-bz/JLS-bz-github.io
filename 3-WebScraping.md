---
title: Web-Scraping Data
layout: default
nav_order: 3
---

# Web-Scraping Reddit

A popular and easy way to retrieve data from Reddit is through the [**PushShift.io**](https://reddit-api.readthedocs.io/en/latest/) API Wrapper [**PMAW**](https://github.com/mattpodolak/pmaw), [**PSAW**](https://psaw.readthedocs.io/en/latest/), or [**PRAW**](https://praw.readthedocs.io/en/stable/). Unfortunately, many attempts at using them produced questionable results - submissions were missing within specified timeframes, as well as producing numerous duplicates of ones that were retrieved. The former has been confirmed by Elizaveta Sivak's article within the Summer Institute in Computational Social Science website, as seen [**here**](https://sicss.io/2021/materials/hse/reddit_.html). These wrappers do not have access to posts in certain timeframes.

As a result, the more manual use of files.PushShift.io itself is utilized, due to its 100% operational status as seen [here](https://stats.uptimerobot.com/l8RZDu1gBG). Screenshot taken on Jan 17, 2023:

<p align="center">
  <img src="assets/Pushshift_status.png"
  width = "50%">
</p>

Description of web-scraped data:
1. 2019-11 to 2021-02
2. 

The following scripts were used:
1. [filePushshiftpull.py](https://github.com/JLS-bz/JLS-bz.github.io/blob/main/scripts/filePushshiftpull.py): Automates the downloading of compressed .zst files from [files.pushshift.io](https://files.pushshift.io/reddit/submissions/): 

2. PushshiftDumps by Watchful1
  - [combine_folder_multiprocess.py](https://github.com/Watchful1/PushshiftDumps/blob/master/scripts/combine_folder_multiprocess.py): converts a folder of .zst files into decompressed .ndjson and subreddit specific .zst files 
      - the following subreddits were selected and grouped according to topics of interest:
          - **Autism/ADHD**: adhd_anxiety, ADHD, adhdwomen, asd, autism, AutisticWithADHD, aspergers
          - **Anxiety/Depression**: SuicideWatch, depression, depression_help, Anxiety, AnxietyDepression, Anxietyhelp, socialanxiety, HealthAnxiety, anxietysuccess
          - **COVID**: COVID19positive, covidlonghaulers
          - **Dissociation**: dpdr, dpdrhelp, Dissociation, Depersonalization, derealization, DPDRecoveryStories, OSDD, anhedonia, visualsnow, BrainFog, DID, Psychosis
          - **Drugs/addiction related**: leaves, zoloft, Drugs, addiction, REDDITORSINRECOVERY, opiates, Psychonaut, benzorecovery, HPPD
          - **LGBT**: lgbt, GenderDysphoria, ftm, MtF, trans, NonBinary
          - **PTSD and Personality Disorders**: CPTSD, PTSD, ptsdrecovery, NarissisticAbuse, raisedbynarcissists, BPD, BPDlovedones, BorderlinePDisorder, BPD4BPD, BPDPartners
  - [single_file.py (adapted)](https://github.com/JLS-bz/JLS-bz.github.io/blob/main/scripts/to_csv.py): converts and processes subreddit specific .zst files into decompressed .csv
      - only information falling under the following columns were kept: ['subreddit','title','selftext','score','num_comments','created_utc']
      - columns 'title' and 'selftext' were combined to create column 'post', then dropped


# Web-Scraping Facebook ?

asdf
----
