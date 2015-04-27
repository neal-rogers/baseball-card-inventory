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

-------------------
Acceptance Stories:
-------------------

+++++++++++
Scenario 1:
+++++++++++

At each start of the program, a prompt for type of transaction is displayed: 'Update' to add/remove records, 'Search' to begin a search, and 'Reports' to output a brief report summarizing recent changes to inventory and total profit. Selecting 'Update' and then responding to another prompt to 'Add' a new card starts a series of additional prompts, asking player name, position, card year, etc. and then finally adds the new card to the inventory file.

+++++++++++
Scenario 2:
+++++++++++

When a card is sold, it must be removed from the current inventory and added to the list of sold cards. At prompt, selecting 'Update' then 'Sold', then prompt to search for card by player name. If duplicate names (cards) are found, a list of duplicates are returned for the user to select. Once the selection has been made, the entry is removed from the current inventory and added to the sold list.

+++++++++++
Scenario 3:
+++++++++++

Running a report starts with selection of the 'Reports' option from startup prompts. Next, responding to a 'Search by?' with 'Team', 'Position', ' 'Sold', etc., will output a list of cards which can be refined to print all or the last 6 records. I default option will be to print unless user responds to a 'Summary' prompt. In the case of sold cards, all items sold along with the total profit from all sales will be displayed.

+++++++++++
Scenario 4:
+++++++++++

Searching can be run by 'Team', 'Position', etc., after selecting 'Search' to startup prompt. The default output will be to display all records matching the search term. If multiple terms are entered, the search will be refined accordingly, i.e., entering 'Cardinals' and 'pitcher' or 'p' will limit output to Cardinals pitchers cards within inventory.