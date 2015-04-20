==============
Baseball Card Inventory
==============

Anyone that still has trading cards in the hopes of someday making a bit of profit could find use in a program that manages their card inventory. Of course, simply having a list of the cards isn't quite enough; you'd also like to have a readily accessible means to assess value, condition, find certain players, etc. Building a program that can quickly and easily provide reports or calculations based on specified values 

Personas:
========

Dick
--------------

Dick has numerous baseball cards that have made it into his collection over the years and would like to maintain detailed records on each of his small treasures. He regularly has his cards appraised and occasionally sells a few and needs to track profit for each sale.

Goals
^^^^^
- Add/remove records from the main inventory.
- Allow for search of records based on specific criteria.
- Provide brief reports including counts, averages, and sums across multiple criteria.
- Maintain record of items sold and calculate total profit.

Problem Scenario:
=================

Given the numerous aspects of trading card valuation, e.g., player, card condition, year, production company, etc., which can be quite a hassle to search and inspect visually. Maintaining a spreadsheet inventory is possible but given the volume of items it would be better served with a database-like mechanism. Users would need to provide item counts, calculate sums for both appraised values as well as record the profit on a sale and records should be updated on the fly.

User Stories
============

Dick needs to have quick access to all information concerning this baseball card collection. Since he is an active card collector/trader he'll need to recall card values and conditions as well as add and remove cards from his inventory. In the case of the latter, it should be assumed that he's sold a card and will track his sales accordingly and provide a summary and total of sales. Dick will also need to generate reports based on things such as player position, card condition, number of duplicates, etc.