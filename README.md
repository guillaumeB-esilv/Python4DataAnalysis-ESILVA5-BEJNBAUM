# Python4DataAnalysis-ESILVA5-BEJNBAUM
Final project for "Python for Data Analysis" ESILV course. Developed by Ariane HUCKEL-ANTOINE (CORE IBO1) and Guillaume BOULEY (CORE IBO2)

## About the dataset 
### Link
https://archive.ics.uci.edu/ml/datasets/Facebook+Comment+Volume+Dataset


The dataset contains features extracted from facebook posts. Our is to predict how many comments Facebook posts will receive.

### Features Description :
#### 1
Page Popularity/likes;
Decimal Encoding;
Page feature;
Defines the popularity or support for the source of the document.
#### 2
Page Checkins;
Decimal Encoding;
Page feature;
Describes how many individuals so far visited this place. This feature is only associated with the places eg:some institution, place, theater etc.
#### 3
Page talking about;
Decimal Encoding;
Page feature;
Defines the daily interest of individuals towards source of the document/ Post. The people who actually come back to the page, after liking the page. This include activities such as comments, likes to a post, shares, etc by visitors to the page.
#### 4
Page Category;
Value Encoding;
Page feature;
Defines the category of the source of the document eg: place, institution, brand etc.
#### 5 - 29
Derived;
Decimal Encoding;
Derived feature;
These features are aggregated by page, by calculating min, max, average, median and standard deviation of essential features.
#### 30
CC1;
Decimal Encoding;
Essential feature;
The total number of comments before selected base date/time.

#### 31
CC2;
Decimal Encoding;
Essential feature;
The number of comments in last 24 hours, relative to base date/time.;

#### 32
CC3;
Decimal Encoding;
Essential feature;
The number of comments in last 48 to last 24 hours relative to base date/time.

#### 33
CC4;
Decimal Encoding;
Essential feature;
The number of comments in the first 24 hours after the publication of post but before base date/time.

#### 34
CC5;
Decimal Encoding;
Essential feature;
The difference between CC2 and CC3.

#### 35
Base time;
Decimal(0-71) Encoding;
Other feature;
Selected time in order to simulate the scenario.

#### 36
Post length;
Decimal Encoding;
Other feature;
Character count in the post.

#### 37
Post Share Count;
ï¿¼ï¿¼Decimal Encoding;
Other feature;
This features counts the no of shares of the post, that how many peoples had shared this post on to their timeline.

#### 38
Post Promotion Status;
Binary Encoding;
Other feature;
To reach more people with posts in News Feed, individual promote their post and this features tells that whether the post is promoted(1) or not(0).

#### 39
H Local;
Decimal(0-23) Encoding;
Other feature;
This describes the H hrs, for which we have the target variable/ comments received.

#### 40-46
Post published weekday;
Binary Encoding;
Weekdays feature;
This represents the day(Sunday...Saturday) on which the post was published.

#### 47-53
Base DateTime weekday;
Binary Encoding;
Weekdays feature;
This represents the day(Sunday...Saturday) on selected base Date/Time.

#### 54
Target Variable;
Decimal;
Target;
The no of comments in next H hrs(H is given in Feature no 39).

## Objectives :
As we said the goal is to predict the amount of comment a Facebok post will received based on 53 features on the pages, the post and other related factors.

## Data processing 
First we look at the correlation between the features. Then we did some data cleaning : labelize features, transform binaries features, convert feature 4 integers to string.

## Data visualization
The goal is to learn what influence the number of comments on posts. So, we look at the Page Features if we have some interesting things to discover

## Data modelisation
We performed differents machine learning models and we compared them in in order to determinate the most optimised one.
