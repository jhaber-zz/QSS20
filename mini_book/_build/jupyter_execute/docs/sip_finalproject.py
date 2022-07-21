(finalproject_sip)=

# Final Project: Social Impact Practicum

For our final course project, we are going to be applying the data science skills you learn in the course to an important matter of public policy: how well are U.S. employers' protecting the health and safety of temporary guestworkers?

With support from the [Dartmouth Center for Social Impact](https://students.dartmouth.edu/social-impact/), our final project will be a [Social Impact Practicum](https://students.dartmouth.edu/social-impact/programs-initiatives/students/social-impact-practicums-sips), or a chance for you to use your data science skills to help a real-world organization.


## Project overview

Data science project involving nationwide data that TRLA has scraped and collected on H-2A and H-2B job postings to help farmworker advocates monitor postings and conduct worker outreach. The project will involve: (1) scraping and linkages with other external data sources, such as Department of Labor (DOL) Wage and Hour Division and Occupational Safety and Health Act (OSHA) agency enforcement records of employers who have violated workers’ rights, (2) a report summarizing key trends, and (3) potentially building an interactive visualization tool of those trends to supplement the searchable database.

## Your project partner

Your project partner is the Analytics and Research division of the Texas RioGrande Legal Aid Association. TRLA’s mission is to provide “free civil legal services to residents in 68 Southwest Texas counties” and the organization “represents migrant and seasonal farm workers throughout the state and in six other southern states.” Data and analytics work within the organization informs programmatic decision-making, outreach strategy, and public legal education. This project will include enforcement information for Texas, Arkansas, Alabama, Mississippi, Louisiana, Kentucky, and Tennessee (the 7 states in which TRLA represents farmworkers).

- The website is: [https://www.trla.org/](https://www.trla.org/)
- Your liaison is Elizabeth Shackney, the Director of Analytics and Research at TRLA

```{image} ../images/trla.png
:alt: TRLA logo
:class: bg-primary mb-1
:width: 200px
:align: center
```

## Social impact practicum context

The U.S. Department of Labor (DOL) administers the H-2A visa program, which issued over 200,000 visas in FY2019 and allows agricultural employers to hire foreign guest workers on temporary visas. Employers need to certify that they are facing a shortage of U.S. workers and that they are upholding health and safety conditions. The H-2B visa program has similar aims for seasonal, non-agricultural employers, but is capped at 66,000 visas annually, limiting its scope relative to H-2A.

While the programs provide important employment opportunities for low-wage workers, especially in places with aging rural workforces, visa workers can be especially vulnerable to violations of their legal rights.  While each employer signs a contract with DOL promising to abide by worker protection laws, investigations show that employees still face systematic abuses, such as wage theft, unsafe conditions in employer-provided housing sites, unsafe transportation and workplace conditions, and other issues. While federal and state agencies (in some states) conduct inspections of select employment and housing sites, cuts to enforcement budgets have weakened oversight mechanisms. 

Investigative journalists have vividly shown the human toll of these violations and the weakness of federal and state oversight mechanisms. For instance, an agricultural employer had over two dozen federal citations for vehicle safety issues in a yearlong period but still remained in operation when a bus that was transporting workers back to the border crashed and killed six workers, injuring seven. Rather than being banned after the fatal crash, the employer was authorized to hire almost 300 additional guest workers the next season.  This example highlights how federal oversight mechanisms are necessary but not sufficient since violations are tracked but employers are rarely terminated from the program (debarred by DOL).

These examples highlight that in many jurisdictions, there are different pools of employers:

1. H-2 employers with no investigations and no violations: this may reflect weak enforcement capacity rather than a true lack of issues to investigate; we will explore whether we can use external data sources to identify “false negative” employers.
2. H-2 employers where investigations were conducted but no violations were found: looking at variation across time and space can help us understand a pool of employers where some issue triggered an investigation but there were difficulties substantiating to find violations.
3. H-2 employers where investigations were conducted and violation(s) were found: this can help us understand different “hit rates” of investigations in finding evidence for violations.
4. H-2 employers where violation(s) were found but those violations were not uncovered as part of an investigation: we will investigate whether employers are ever found to be in violation of program rules through processes other than an investigation.

Compiling enforcement data, especially across various agencies (where reporting is currently de-centralized), and over time (as, for example, cross-listed by employer) would greatly increase the ability of three sets of stakeholders---legal advocates; state agencies; federal agencies---to improve conditions by analyzing trends across these different pools.

Within this context, TRLA, responding to requests from farmworker advocates across the country, has created the most comprehensive and up-to-date database to date of recent H-2A and H-2B job postings, creating a searchable database for migrant farmworker advocates to track job postings and plan outreach: https://trla.shinyapps.io/H2Data/. The database is comprised of a mix of (1) data scraped from individual state websites, and (2) quarterly DOL data releases. The present project will build upon that initial work through linkages between the data and (1) enforcement data and (2) contextual data on the areas surrounding the job sites. 

### Primary project

**Tracking job activity by high-violation and/or temporarily-debarred employers**: DOL enforcement data shows which employers face sanctions without a program ban or with temporary program bans. What is the frequency with which employers continue to post jobs after they have been sanctioned? How rapidly do temporarily-banned employers return to posting after their ban expires? Can we use external sources to mitigate problems of small employers changing their names to evade detection? This project would build on an initial analysis of enforcement actions by the Economic Policy Institute (EPI), which summarized broad trends in DOL Wage and Hour Division (WHD) Compliance Action data.  For instance, in a section of the report investigating “bad apple” employers---defined as single employers with either a large number of violations or a high share of violations within a particular industry category---the report highlights employers with high counts of violations.  Our linkages to the posting data can help us investigate important follow-up questions, like: what does posting activity look like for employers with high counts of violations versus employers with none? Are jobs at the former set of employers filled less quickly, which one might expect if information about high-violation employers is broadly accessible and transparent to recruiters or visa seekers, or are they filled as quickly as similar jobs at no-violation employers? 


### Backup project

**Identifying Mismatches between Employer Certification of Workforce Shortages and Externally-verified Shortages**: The visas are meant to fill workforce gaps in the surrounding regions, but some allege that employers turn to the program less due to verified workforce shortages and more due to financial incentives in terms of lower wage rates, avoiding unemployment taxes, and to obtain a more vulnerable workforce by employing foreign-nationals (especially H-2A workers who are legally prohibited from choosing to work anywhere else in the U.S.). Can we use American Community Survey (ACS) and other public datasets to understand the U.S. worker poverty level data, current unemployment data for various locales, and agricultural industry wage rate data to see whether employers’ statements that there is a labor shortage, and depressed wages, in their area is true?



## Organizational context

TRLA is the second-largest civil legal aid organization in the U.S. It offers free civil legal services to residents in 68 Southwest Texas counties ([https://www.trla.org/offices](https://www.trla.org/offices)). The farmworker law practice within their broader labor and employment practice group represents farmworkers with employment problems not only in the Texas but also in six other states through a Tennessee branch office (Kentucky, Alabama, Mississippi, Louisiana, Georgia, Tennessee): [https://www.trla.org/labor-employment](https://www.trla.org/labor-employment). TRLA is an especially compelling partner for the H-2 guestworker project because the states within its jurisdiction have high concentrations of farmworkers. 

In addition to that practice area, which is the area most connected with the SIP project, they also provide free legal services to low-income people facing issues like eviction, bankruptcies and foreclosures, divorces and custody arrangements, consumer fraud, wills and estates, accessing public benefits, and litigating for civil and environmental rights. 



## Logistics

As described in the main section of the syllabus, you'll be split into assigned groups to work on sub-components of the project. We'll be working from the following common repo that you'll be added to, and have push/commit privileges for, when you're set up on GitHub: [https://github.com/rebeccajohnson88/qss20_s21_proj](https://github.com/rebeccajohnson88/qss20_s21_proj)