---
title: "Recover Before You Build"
date: 2026-07-01
summary: "The cheapest engineering is often the code you already have — how to tell recover from complete from build."
generated_by: spark-inference (ollama/mistral, local, zero-token) · revised
---

# Recover Before You Build: Making Informed Decisions on Reuse and Development

As a software engineer, I've often found myself at a crossroads, weighing the options between reusing existing code and building something new. This article aims to shed light on when it makes sense to recover (reconnect or complete) pre-existing functionality versus building from scratch.

## The Importance of Recovery Over Building

In many cases, the most cost-effective engineering solution is utilizing the code that you already have. Instead of embarking on a new build, consider whether the required capability can be:

1. **Recovered**: If a module has been disconnected but still functions correctly, it's often more efficient to reconnect it rather than building a new one from scratch. For instance, in a recent project, we discovered an abandoned API integration that was no longer being used due to a team change. By reconnecting the integration, we saved significant time and resources compared to building a new one.
2. **Completed**: If a feature is almost functional but lacks some finishing touches or minor adjustments, it might be more practical to complete it rather than starting from scratch. I've encountered situations where developers have built 80% of a feature only to abandon it due to shifting priorities. In these cases, completing the existing work can save both time and effort in the long run.

## When is Recovery a False Economy?

While recovery can offer significant benefits, there are instances when it may not be the best choice. For example:

1. **Obsolete Technology**: If the pre-existing code relies on outdated technologies or libraries that are no longer supported or maintained, it may cause long-term issues and maintenance headaches. In such cases, building a new solution using modern tools might be a better approach, even though more effort is required upfront.
2. **Inefficient Design**: Sometimes, the pre-existing code may have been designed poorly, leading to unnecessary complexity, duplicated functionality, or poor performance. If the cost of refactoring the existing code outweighs the benefits, it might be wiser to build a new solution from scratch.
3. **Maintainability and Scalability**: If the pre-existing code lacks maintainability or scalability, it could hinder future development and make it challenging to meet evolving business needs. In such cases, building a new solution that incorporates best practices for maintenance and scaling may be the better choice.

## Differentiating Between "Almost Works" and "Looks Like It Works"

Determining whether a pre-existing feature "almost works" or merely "looks like it works" can be challenging. Here are some strategies to help you make an informed decision:

1. **Code Review**: Thoroughly review the existing code to identify any potential issues, inconsistencies, or inefficiencies that could indicate the feature is not as functional as it seems.
2. **Unit Testing**: Write unit tests for the pre-existing functionality to confirm its behavior and identify any edge cases or errors that may have been missed during initial development.
3. **Performance Benchmarking**: Compare the performance of the existing code with a potential new implementation to determine if the old code is significantly slower or less efficient.
4. **Collaboration**: Involve other team members, such as tech leads or more experienced developers, to provide additional insights and help evaluate the quality and viability of the pre-existing functionality.
5. **Pilot Deployment**: If possible, deploy the pre-existing feature in a controlled environment (e.g., a test cluster) to confirm its functionality under real-world conditions and identify any unforeseen issues.

In conclusion, understanding when to recover or build is crucial for making cost-effective engineering decisions. By considering concrete examples, evaluating the trade-offs, and employing strategies like code reviews, unit testing, performance benchmarking, collaboration, and pilot deployment, you can make informed choices that maximize your team's efficiency and productivity.
