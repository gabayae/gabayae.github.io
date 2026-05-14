---
layout: post
title: "The African AI landscape: opportunities and challenges"
date: 2025-04-01
description: "Reflections on building AI research capacity across Africa — from AIMS to Data Science Africa and beyond."
tags: [data-science, Africa, machine-learning]
categories: [research]
giscus_comments: true
related_posts: true
---

## What's actually happening on the continent

AI and data science activity in Africa is no longer marginal. Labs in Lagos, Nairobi, Cape Town, Kigali, and elsewhere are producing research and shipped systems at a pace that did not exist five years ago.

I've worked at institutions in **Benin**, **South Africa**, and **Rwanda**, and the change I see most directly: organizations like [AIMS](https://www.nexteinstein.org/), [Data Science Africa](https://www.datascienceafrica.org/), and [Quantum Leap Africa](https://quantumleapafrica.org/) used to be promising. Now they're producing graduates and research that hold their own against any global benchmark.

## What works

**Mathematical training.** AIMS has trained thousands of graduates across its centres (South Africa, Senegal, Ghana, Cameroon, Tanzania, Rwanda), with deep coursework in analysis, algebra, and topology. Many alumni move to PhDs and postdocs abroad; a growing share now come back, and a growing share stay in the first place.

**Problems that bite.** Healthcare, agriculture, financial inclusion, climate monitoring. The work happens close to people whose lives depend on whether the model is right or wrong, which is a different research environment than benchmark-chasing. Disease surveillance in East Africa, crop yield prediction in West Africa, mobile money fraud detection across the continent: the cost of being wrong is operational, not just a number in a results table.

**Open-source as default.** Through [Data Science Makers](https://github.com/AI-Technipreneurs), Data Science Africa, and the broader AI4Africa networks, researchers publish code, notebooks, and datasets early, and other people actually build on them. That habit isn't universal globally and it matters more than people realize — it compresses the gap between a paper and someone else's working pipeline.

## What doesn't

**Infrastructure.** Compute, connectivity, and access to GPU clusters are uneven. A researcher in Kigali can have reliable cloud access while a colleague two countries over fights intermittent connectivity. This constrains the kind of research that's locally feasible and produces real dependencies on US and EU cloud providers.

**Brain drain.** Keeping good researchers requires competitive funding, a research community worth being in, and a credible link from the work to local impact. The pull of well-funded labs in North America and Europe is real and it's not going away. I'm cautiously optimistic anyway: AIMS, QLA, and ACAS are showing that a meaningful research career on the continent is possible, not just notional.

**Data scarcity.** Representative datasets for African contexts are missing in many domains. Medical imaging skews to lighter skin tones, NLP is overwhelmingly English-and-Romance, economic datasets reflect the measurement infrastructure of wealthier countries. Building the datasets is itself a research agenda — and one with a long horizon.

## Why topology and geometry, specifically

This isn't a generic case for African researchers to do all of AI. It's specifically about topological and geometric methods, and there are four reasons.

They're data-efficient: persistent homology and TDA pull structural features out of small samples, which matters when collecting more data isn't the answer.

They sit on mathematics where the local training is unusually deep — particularly via the AIMS network. Building on what's already there is faster than importing what's missing.

They produce interpretable features: a topological signal has a geometric reading you can explain to a clinician or a regulator, which matters in healthcare and finance where black-box outputs cost trust.

They're hardware-light. A TDA pipeline runs on a workstation. The compute gap is real, but it's a smaller obstacle here than in foundation-model work.

The [WoComToQC workshop](https://wocomtoqc.github.io/), the teaching materials for [AI.Technipreneurs](https://github.com/AI-Technipreneurs), and the research at AIRINA Labs and ACAS are all pushing on this — translating the mathematical training that already exists into applied AI work.

## What I'm watching for

The interesting question isn't whether African researchers will participate in AI globally; they already do. It's whether the work coming out of the continent starts to have a distinctive shape, defined by the problems in front of it and the mathematical training behind it. My bet is yes, and I'd like the topology, geometry, and fixed-point thread to be a recognizable part of that shape.

If you're working in this space and want to compare notes, the communities linked above are where I'd start.
