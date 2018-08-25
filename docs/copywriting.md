# Copywriting: headings, labels & body text

## App name / site title

ScienceWatch
ScholarWatch
KnowledgeWatch
ScienceTracker
**KnowledgeTracker**

---

## Tagline / prompt for users to enter keywords

Find articles mentioned on social media in the past 24 hours
Search for articles mentioned on social media during the last 24 hours:
Results of articles shared or mentioned on social media in the last 24 hours
Search trending articles by keyword:
**What’s trending on the subject of [keywords] in the last [timeframe]?**

----

## Paragraph / more details

_Search scholarly works mentioned across the social web: policy documents, [mainstream media](https://www.altmetric.com/about-our-data/our-sources/news/), blogs, online reference managers, post-publication peer-review forums, social media, patent citations and [other online sources](https://help.altmetric.com/support/solutions/articles/6000060968-what-outputs-and-sources-does-altmetric-track-)_

---

## Main menu / header

- [ALTMETRIC LOGO]
- [What are altmetrics?](https://www.altmetric.com/about-altmetrics/what-are-altmetrics/)
- [About these data](https://www.altmetric.com/about-our-data/)

---

## Interesting data to display

### Parameters

- score (default)
- **at_score** - sort by all-time score (badges display that score, not the timeframe-based one)
- readers
- first_seen
- pubdate

### Citation object (`results`)

The info displayed should give users context on papers that are related to the keywords searched, the work’s content and the chosen timeframe.
Every work displayed should lead to either the original paper or the Altmetric detail page.
Avoid showing too much metadata for that purpose (since Altmetric’s detail page should provide this info anyway).

- **title***
- **type**
- doi
- nlmid
- arxiv_id
- ads_id
- handles
- isbns
- tq - **maybe** (could be interesting to display a selection of quotes)
- cited_by_posts
- **journal**
- altmetric_id*
- cited_by_x_count
- **score*** (for ordering / sorting)
- history* - **maybe** (for context?)
- **url***
- authors
- editors - (only for books)
- authors_or_editors
- book_cover_url
- book
- chapters
- added_on*
- **published_on**
- subjects - **maybe**
- cohorts
- readers
- **images** - for displaying Altmetric scores
- **details_url** - for displaying Altmetric scores


---

## Footer

- Contact?
- Year?
- Another link to Altmetric.com?
- Altmetric’s detailed description:
  - Altmetrics data is provided by Altmetric.com, a research metrics company who track and collect the online conversations around millions of scholarly outputs. Altmetric continually monitors a variety of non-traditional [sources](https://www.altmetric.com/about-altmetrics/our-sources/) to provide real-time updates on new mentions and shares of individual research outputs, which are collated and presented to users via the Altmetric [details pages](https://www.altmetric.com/about-altmetrics/altmetric-details-page/) and [badge visualisations](https://www.altmetric.com/products/altmetric-badges/). Each research output that Altmetric finds attention for is also given a score; a weighted count of the online attention it has received. Further information about how the Altmetric Attention Score is calculated is available [here](https://www.altmetric.com/about-altmetrics/the-donut-and-score/).
