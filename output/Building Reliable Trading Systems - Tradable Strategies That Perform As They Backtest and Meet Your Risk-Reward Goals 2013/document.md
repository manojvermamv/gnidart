## BUILDING RELIABLE TRADING SYSTEMS

Founded in 1807, John Wiley &amp; Sons is the oldest independent publishing company in the United States. With offices in North America, Europe, Australia, and Asia, Wiley is globally committed to developing and marketing print and electronic products and services for our customers' professional and personal knowledge and understanding.

The Wiley Trading series features books by traders who have survived the market's ever-changing temperament and have prospered-some by reinventing systems, others by getting back to basics. Whether a novice trader, professional, or somewhere in-between, these books will provide the advice and strategies needed to prosper today and well into the future.

For a list of available titles, visit our web site at www.WileyFinance.com.

## BUILDING RELIABLE TRADING SYSTEMS

Tradable Strategies That Perform as They Backtest and Meet Your Risk-Reward Goals

## Keith Fitschen

WILEY

Cover Design: John Wiley &amp; Sons, Inc. Cover Illustration: © Equinox Imagery/Alamy

Copyright © 2013 by Keith Fitschen. All rights reserved.

Published by John  Wiley &amp; Sons, Inc., Hoboken, New Jersey. Published simultaneously in Canada.

No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form or by any means, electronic, mechanical, photocopying, recording, scanning, or otherwise, except as permitted under Section 107 or 108 of the 1976 United States Copyright Act, without either the prior written permission of the Publisher, or authorization through payment of the appropriate per-copy fee to the Copyright Clearance Center, Inc., 222 Rosewood Drive, Danvers, MA 01923, (978) 750-8400, fax (978) 646-8600, or on the Web at www.copyright.com. Requests to the Publisher for permission should be addressed to the Permissions Department, John  Wiley &amp; Sons, Inc., 111 River Street, Hoboken, NJ 07030, (201) 748-6011, fax (201) 748-6008, or online at www.wiley.com/go/permissions.

Limit of Liability/Disclaimer of  Warranty:  While the publisher and author have used their best efforts in preparing this book, they make no representations or warranties with respect to the accuracy or completeness of the contents of this book and specifically disclaim any implied warranties of merchantability or fitness for a particular purpose. No warranty may be created or extended by sales representatives or written sales materials.  The advice and strategies contained herein may not be suitable for your situation.  Y ou should consult with a professional where appropriate. Neither the publisher nor author shall be liable for any loss of profit or any other commercial damages, including but not limited to special, incidental, consequential, or other damages.

For general information on our other products and services or for technical support, please contact our Customer Care Department within the United States at (800) 762-2974, outside the United States at (317) 572-3993 or fax (317) 572-4002.

Wiley publishes in a variety of print and electronic formats and by print-on-demand. Some material included with standard print versions of this book may not be included in e-books or in print-ondemand. If this book refers to media such as a CD or DVD that is not included in the version you purchased, you may download this material at booksupport.wiley.com. For more information about Wiley products, visit www.wiley.com.

## Library of Congress Cataloging-in-Publication Data:

ISBN 978-1-118-52874-7 (Hardcover); ISBN 978-1-118-63561-2 (ebk); ISBN 978-1-118-63581-0 (ebk); ISBN 978-1-118-67277-8 (ebk)

Printed in the United States of America

10   9   8   7   6   5   4   3   2   1

## CONTENTS

|            | Preface                                                                     |   vii |
|------------|-----------------------------------------------------------------------------|-------|
| CHAPTER 1  | What Is a 'Tradeable Strategy?'                                             |     1 |
| CHAPTER 2  | Developing a Strategy So it Trades Like it Back-Tests                       |     7 |
| CHAPTER 3  | Find the Path of Least Resistance in the Market You Want to Trade           |    31 |
| CHAPTER 4  | Trading System Elements: Entries                                            |    45 |
| CHAPTER 5  | Trading System Elements: Exits                                              |    65 |
| CHAPTER 6  | Trading System Elements: Filters                                            |    89 |
| CHAPTER 7  | Why You Should Include Money Management Feedback in Your System Development |   107 |
| CHAPTER 8  | Bar-Scoring: A New Trading Approach                                         |   119 |
| CHAPTER 9  | Avoid Being Swayed by the 'Well-Chosen Example'                             |   133 |
| CHAPTER 10 | Trading Lore                                                                |   153 |
| CHAPTER 11 | Introduction to Money Management                                            |   175 |
| CHAPTER 12 | Traditional Money Management Techniques for Small Accounts: Commodities     |   191 |

| CHAPTER 13   | Traditional Money Management Techniques for Small Accounts: Stock Strategy   |   215 |
|--------------|------------------------------------------------------------------------------|-------|
| CHAPTER 14   | Traditional Money Management Techniques for Large Accounts: Commodities      |   221 |
| CHAPTER 15   | Traditional Money Management Techniques for Large Accounts: Stocks           |   233 |
| CHAPTER 16   | Trading the Stock and Commodity Strategies Together                          |   241 |
| APPENDIX A   | Understanding the Formulas                                                   |   245 |
| APPENDIX B   | Understanding Futures                                                        |   251 |
| APPENDIX C   | Understanding Continuous Contracts                                           |   265 |
| APPENDIX D   | More Curve-Fitting Examples                                                  |   273 |

Index

277

T his book shows you how to build a tradeable strategy. A tradeable strategy is one that fits your own risk/reward goals, and one that trades in real-time as well as it performs in the development back-test. It is not easy to develop a tradeable strategy because there are serious pitfalls. Most of us are greedy and want to trade something that has a large return. We rationalize that we can accept a lot of risk in the form of draw-down to achieve the large return, but in reality few traders can trade through a 20 percent draw-down before abandoning the strategy. T o help you form realistic risk/ reward goals, the first chapter shows the real-time performance of the best traders in the world over a recent five-year period. Based on that chapter, I urge you to write down the system characteristics that would be tradeable for you. Address risk first in the form of max draw-down, average annual max draw-down, and longest time between equity highs. So the first pitfall is greed. It manifests itself in every strategy development step.  You will be inclined to accept a system rule that increases profitability, even though it increases risk at a higher rate. But an even greater pitfall is the danger of curve-fitting.

Curve-fitting occurs when you develop a strategy with too few trades in the development sample. Curve-fit systems impact the second characteristic of a tradeable system: Curve-fit systems don't trade in real-time as well as they back-test. It is unfortunate that the system development packages you can buy are almost universally tied to the one-chart paradigm; you place many bars of data from a single tradeable on a chart and develop a strategy to trade that instrument. Even if your developed strategy yields hundreds of trades, it probably isn't enough to be anything other than heavily curve-fit. Chapter 2 covers curve-fitting extensively and shows how you can generate enough trades to minimize curve-fitting. It uses examples and statistics, and details an easy-to-perform process that you can use to determine the degree of curve-fitting in your development work. Most strategies fail or underperform because they are overly curve-fit. If you want to succeed, you need to fully understand how to minimize curve-fitting.

Most of the remainder of the book is spent developing two tradeable systems: one a short-term scalping system for stocks, and the other a mid-term trend-following strategy for commodities. As these systems are developed, entries, exits, and trading filters are detailed. By the end of the development process, both are 'tradeable' as is, but how to tailor them to a range of risk/reward profiles is covered in, five chapters on money management. I make a differentiation between small-account traders  and  large-account  traders.  Small-account  traders  are  always  a handful  of  adverse  trades  away  from  a  margin  call. They  cannot  take advantage of sizing techniques that optimize equity growth because the risk of more than a one-lot might be 10 or even 20 percent of their account size. Using small-account trading techniques, money management rules  for  both  the  stock  and  commodity  systems  are  detailed  in  two chapters. Similarly, the systems are adapted for the large-account trader in two chapters. Lastly, both systems are combined. Table P .1 illustrates the range of tradeable solutions available.

TABLE P .1

## Tradeable Solutions with Combined Trading of the Stock and Commodity Strategies

|   Average Annual Return (percent) |   Average Annual Max Draw-Down (percent) |   Max Draw-Down (percent) |
|-----------------------------------|------------------------------------------|---------------------------|
|                              23.4 |                                      5.6 |                       8.7 |
|                              25.9 |                                      6.1 |                       9.6 |
|                              28.6 |                                      6.7 |                      10.4 |
|                              31.2 |                                      7.2 |                      11.3 |
|                              33.9 |                                      7.8 |                      12.1 |
|                              36.6 |                                      8.3 |                      13.0 |

There is material in the book that I've never seen elsewhere. Most notably, bar-scoring is detailed in Chapter 8. It is an exciting new way to characterize the profit potential of each bar with user-defined criteria.

Lastly, Chapter 9 and Chapter 10 are devoted to an analysis of some of the trading claims commonly made in the literature, and to trading maxims that may or may not have a basis.

The  TradeStation Easy Language code and daily signals for the systems developed in this book are available on a companion web site. See the instructions at the back of the book for more information.

## What Is a Tradeable Strategy?

T he purpose of this book is to show the reader how to develop a tradeable strategy. But before the how-to part, you need to realistically understand what a tradeable strategy must encompass. I say realistically because some traders envision a tradeable strategy as one that never loses a trade, never has a losing day, and at least doubles your money each year. It's nice to have lofty goals, but you'll never find a strategy that meets those criteria. T o show the art of the possible, the first part of this chapter will present documented performance from some of the best traders over the last five years. Then we'll look at metrics that best characterize a trading strategy's performance. Lastly, a set of questions will be presented to help you define  what  would  constitute  a  tradeable  strategy  according  to  your risk-taking tolerance.

## ■ Realistic Return/Risk Expectations

Table 1.1 shows Barclay's top 20 Commodity Trading Advisors (CTAs) for the five-year period of July 1, 2005, through June 30, 2010. It was compiled by Barclay's from the 290 CTAs that submit performance information to them.

1

Table 1.1 raises a number of interesting points:

- ■ Across all 20 funds, the average annual yearly performance of 27.98 percent is only about 3.5 percent higher than the average of the max draw-downs.
- ■ Out of the 20 funds, 17 had an entire one-year period without any gain.
- ■ The best 12-month period heavily skewed the average five-year return performance numbers. If you compound a starting amount by 27.98 percent per year (the average annual return across the 20 entities) for five years,

TABLE 1.1 Top 20 CTA Performance for 7/1/2005 to 6/30/2010

| Advisor                    |   5-Yr. Comp. Annual Return (%) |   Largest Draw- Down (%) |   Percent Winning Months |   Best 12 Month Period (%) |   Worst 12 Month Period (%) |
|----------------------------|---------------------------------|--------------------------|--------------------------|----------------------------|-----------------------------|
| Vegasoul Capital           |                           44.54 |                     6.88 |                     80.0 |                        112 |                           1 |
| Management                 |                                 |                          |                          |                            |                             |
| Quantitative Invest. Mgmt. |                           37.01 |                    29.49 |                    68.33 |                        126 |                         -22 |
| Pere Trading Group         |                           36.44 |                    60.72 |                    61.66 |                        570 |                         -50 |
| DiTomasso Group            |                           33.73 |                    26.13 |                    68.33 |                         76 |                         -26 |
| Commodity Future Services  |                           32.04 |                    27.84 |                    61.66 |                        135 |                         -22 |
| Two Sigma                  |                           31.56 |                    18.17 |                    66.66 |                         75 |                           0 |
| 24FX Management Ltd.       |                           29.41 |                    19.28 |                     80.0 |                         55 |                           2 |
| Scully Capital Mgmt.       |                           28.44 |                    21.26 |                    58.33 |                         79 |                          -6 |
| Dighton                    |                           27.41 |                    44.32 |                    61.66 |                        226 |                         -44 |
| Belvedere Advisors         |                           27.35 |                    14.55 |                    66.66 |                         86 |                           7 |
| Financial Comm. Inv.       |                           26.99 |                    34.63 |                    76.66 |                        112 |                         -23 |
| Red Oak Comm. Advisors     |                           25.03 |                    21.91 |                    68.33 |                         86 |                          -7 |
| Altis GFP Master Fund      |                           24.45 |                    22.73 |                    56.66 |                         70 |                          -8 |
| Heyden & Steindl           |                           23.69 |                    17.76 |                    51.66 |                         82 |                          -8 |
| Aisling Analytics          |                           23.13 |                    26.05 |                     65.0 |                         66 |                         -20 |
| Tactical Invest. Mgmt.     |                           22.64 |                    22.23 |                    51.66 |                         52 |                         -16 |
| Quicksilver Trading Inc.   |                           22.04 |                    24.58 |                    63.33 |                         73 |                         -20 |
| Blenheim Capital Mgmt.     |                           21.53 |                    25.63 |                    63.33 |                         84 |                         -22 |
| Paskewitz Asset Mgmt.      |                           21.05 |                    12.18 |                    68.33 |                         64 |                          -7 |
| MIGFX Inc.                 |                           21.02 |                    12.86 |                    63.33 |                         67 |                         -11 |
| Average                    |                           27.98 |                    24.46 |                    65.08 |                      125.3 |                       -15.1 |

the ending equity is about 243 percent higher than the starting amount. The average best 12-month average return of 125.3 percent is over half that amount.

- ■ In general, the funds with the higher fi  ve-year return took more risk, as refl  ected by the draw-down numbers.  This can be seen by plotting the average return and max draw-down points on a graph and fi  tting a regression line to the return and draw-down points. Figure   1.1 shows the graph.

FIGURE  1.1 Return versus Risk for the  T op 20 CTAs

<!-- image -->

These  performance  numbers  probably  introduce  a  reality  shock  into those looking to develop their own tradeable strategy. Real trading involves these tenets:

- ■ You are not going to make 100 percent each year. The number-one CTA in  the  list  averaged  44.54  percent  for  5  years,  but  even  then  it  had  a 12-month period that netted only 1 percent.
- ■ If  you shoot for a relatively high return, you will have a relatively high draw-down at some point. If you shoot for a relatively lower return, you should be able to see relatively less draw-down.
- ■ If you are fortunate enough to have a period of exceptional returns, remember that those gains may have to carry your performance for years.
- ■ You will go extended periods of time without any gains.

4

## ■ Metrics to Use in Gauging Tradeable System Performance

Based on the performance of some of the best money managers in the world, there are a minimum of three areas that need to be addressed in defining a suitable tradeable system:

1.  Some measure of normal return and normal draw-down. These are the  risk/reward  benchmarks  you'll  be  experiencing  most  of  the time.
2.  The  worst-case  risk  benchmark. This  is  the  worst  draw-down  you'll have  to  trade  through  over  an  extended  period  of  time-maybe  the worst case in the last 5 or 10 years.
3.  The longest flat time. This is the longest time you'll go before hitting a new equity high.

Looking at worst-case risk first, we've seen that the best managers in the world normally average just a little more than their five-year biggest drawdown. A goal of a tradeable system is one that averages more per year than its largest draw-down. This book will show that, in general, return can be increased or decreased through leverage. As you increase or decrease the return, your draw-down will also go up or down. It makes sense then to define the max draw-down you are willing to accept and use leverage to bring the system performance down to a point where the max draw-down is less than your acceptable threshold.

It's  my  experience that it's  hard  to  design  a  system  with  minimal 'flat time' as a design metric.  You do the best you can through the development process and when you've got something that meets your risk-reward goals, you see what the other metrics look like. If flat time, or some other characteristic, is way over what you're willing to trade through, the best way to fix the problem is to introduce another type of strategy that is lowly correlated to the one with the issue.

## ■ Know Yourself

It's easy to start the design process and say, 'I want something that has a max draw-down of 20 percent, and for that risk I'll accept an average return of 25 percent.'   The problem starts when you've developed such a strategy and start to trade. Suppose you go three months and are down 10 percent. I don't care who you are, you'll start to have doubts:

- ■ Is the strategy curve-fit in some way?
- ■ Has the market changed?
- ■ Volatility seems too high (too low). Is that the problem?

If you've set your max draw-down too high, by the time you recover, or get to 20 percent, you'll be a wreck. This is where it becomes important to know yourself. If you're new to trading and never experienced a 20-percent draw-down, shoot for less-probably much less. I've talked to thousands of traders, and most say, 'I can weather a 20 percent draw-down if the return is X percent,' but in reality few can go that far. Don't look at draw-down as a function of return. Y ou've got to get through the draw-downs to realize the return, so set your max draw-down at a level you know you can trade through.

## ■ Conclusion

The best money managers in the world average less than 30 percent a year, and experience a max draw-down every five years that is only a few percent less than their average return. Unfortunately , statistics on average annual max draw-down aren't easy to find, but that is an important number because that' s what you need to trade through every year to achieve your return. Our goals then for developing a tradeable system must include these two performance objectives:

1.  Average annual return is greater than max draw-down over at least a five-year period.
2.  Average annual return needs to be a multiple of the average annual max draw-down.

The third required performance objective is defined by the trader: What is the max draw-down you will tolerate? Pick a realistic number.

This  book  will  show  you  how  to  develop  strategies  that  meet  these objectives.  In  fact,  when  we're  done,  there  will  be  fully  defined  stock and commodity strategies that you can trade as-is if you wish. Before we develop these systems, there's really another part to tradeability and that is, your strategy must trade in real time like it does on your developmental data. The next chapter will discuss how to develop your strategy so it trades like it back-tests.

## Developing a Strategy So It Trades Like It Back-Tests

D eveloping a tradeable strategy involves two steps. The first is to define the risk/reward balance the trader can live with, and the second is to develop a strategy that meets those guidelines and trades in real time like it back-tests. Most of the rest of this book will address how to develop strategies that meet your trading objectives.  This chapter addresses something much more important: the pitfalls a developer will run into in developing a strategy that will trade like it backtests. There are many 'how to develop' ways; this book only shows mine, but there is only one way to make sure your developed strategy trades in real time like it backtests.  That one way involves minimizing curve-fitting in your development and making trading assumptions in your development that work as realistically as possible. Far and away, the biggest pitfall is curve-fitting. This chapter uses statistics to help clarify the concept, but don't skip over it because of the math.  These are important concepts, and if you don't understand them you will continually develop systems that fail in real-time trading and you will never understand why.

## ■ Curve-Fitting

When you're developing a trading strategy, you test trading ideas against historical data to see if the idea is profitable. If you had an infinite amount of historical data, you could be sure that an idea that proves profitable on the historical data would be just as profitable in the future. But we never have an infinite amount of data; we only have a few decades worth of data in the best case. With that small subset of the 'infinite data pool,' we can't be sure a backtested profitable idea will continue to be profitable in the future. This development problem is often exacerbated by a practice called curvefitting. Curve-fitting can be defined in the following way: either the overuse of trading rules, parameters, filters, stops, and so forth when developing a trading strategy on a relatively large body of data, or the proper use of rules, filters, and so on on a relatively small body of data.

A curve-fitting example will be given for each of these cases. For the case where a relatively large body of data was used, here's a true story. I knew a trader in the late '90s that developed an S&amp;P 500 futures trading system using 45-minute bars. He had S&amp;P 45-minute bar data spanning the 19841998 time frame. During most of that time, the S&amp;P 500 futures opened at 9:30 EST and closed at 16:15 EST , so there were nine 45-minute bars each day for the 15 years. That's a total of about 34,000 bars of historical data. With all that data, he developed a trading system that made less than 90 trades in the 15 years.  That's a trade every other month. But those 90 trades were spectacular. There were only a few losers, and the average trade was over $2,000. He figured he could double a starting amount of $10,000 each year with the strategy. I saw him a few years later and asked how his system was working out. He scratched his head and said he couldn't figure out what went wrong. The system 'stopped working' as soon as he started trading it. I believe that what really happened is that he used so many rules, filters, and so forth on the relatively large amount of data that he isolated 90 short periods of time that were highly profitable.

## Curve-Fitting Using Good Development Practices on a Small Amount of Data

Curve-fitting on a relatively small body of data can be illustrated by looking at the Swiss franc during the 1980s. That time-frame was picked because the Swiss franc trended beautifully in the 1980s. Let's use a moving average to determine the trend. If today's n-day average is higher than yesterday's, the trend is up so you buy one contract.  You hold that position until today's n-day average is less than yesterday's.  When that happens, you exit your long position and go short. It's called a reversal system.  You always have a position and that position alternates from long to short to long.  The breakout in Table 2.1 shows the results when the n-day average is varied from 10 days to 100 days in 10-day increments.

TABLE 2.1 Swiss Franc Moving Average System 1/1/1980-12/31/1989: Varying the n-Day Average

|   Number of Days |   Winning Trades |   Losing Trades |   Profit ($) |   Profit-per-Trade ($) |
|------------------|------------------|-----------------|--------------|------------------------|
|               10 |              116 |             184 |       31,625 |                    105 |
|               20 |               77 |             127 |       64,200 |                    315 |
|               30 |               59 |              99 |       50,763 |                    321 |
|               40 |               49 |              63 |       61,037 |                    545 |
|               50 |               37 |              43 |       72,072 |                    900 |
|               60 |               25 |              59 |       45,187 |                    538 |
|               70 |               36 |              54 |       56,275 |                    625 |
|               80 |               25 |              53 |       55,500 |                    712 |
|               90 |               22 |              40 |       63,475 |                  1,023 |
|              100 |               25 |              39 |       62,925 |                    983 |

This table illustrates how well the Swiss franc trended in the 80s.  There is substantial profit at each moving average point. Let's select the 50-day moving average point and try to improve results by adding an n-day look-back filter.  One of the tenets of trend trading is to only trade in the direction of the long-term trend. An n-day look-back filter is a way to do that. You look back n days and if the close today is higher than that close, the trend is up and you only take long trades. In looking back n-days, if today's close is less than the n-day look-back close, you only take short trades. When we add that logic to our 50-day reversal system, the results in Table 2.2 are for look-backs ranging from 60 days to 150 days.

Let's select the 110-day look-back filter as a good addition to the system, and now look to add some risk control. Let's use a 'catastrophic stop loss' to get us out of trades that move 'too far' into loss. When we enter a long or short position, the catastrophic stop is placed X dollars away from the entry. If that stop is hit, we don't reenter in the same direction until an entry in the other direction is signaled. There are two ways to implement this stop. First you can enter the stop as a 'good until canceled' stop loss.

<!-- image -->

## Swiss Franc Moving Average System 1/1/1980-12/31/1989 with n-Day Look-Back Trend Filter

|   Number of Days |   Winning Trades |   Losing Trades |   Profit ($) |   Profit-per-Trade ($) |
|------------------|------------------|-----------------|--------------|------------------------|
|               60 |               28 |              36 |       66,924 |                  1,046 |
|               70 |               31 |              37 |       70,987 |                  1,060 |
|               80 |               34 |              33 |       75,737 |                  1,130 |
|               90 |               33 |              33 |       78,349 |                  1,187 |
|              100 |               31 |              32 |       75,849 |                  1,204 |
|              110 |               31 |              31 |       79,187 |                  1,276 |
|              120 |               31 |              31 |       77,287 |                  1,247 |
|              130 |               29 |              32 |       74,487 |                  1,221 |
|              140 |               31 |              31 |       77,412 |                  1,249 |
|              150 |               30 |              29 |       74,200 |                  1,258 |

In that case, the stop is always in the market (just when the market's open; nothing trades 24/7).  The second way is to not place the stop into the market, but instead wait until there is a close adverse to the stop and exit at the next open. In that case you can have losses well in excess of your stop loss, but there are two benefits. One benefit is that the stop is not active during periods  of  illiquidity;  almost  every  commodity  has  bid/ask  spreads  that increase overnight, sometimes dramatically, and with an active stop there's a chance of a horrendous fill.  The other benefit is that many times an active stop would be hit during the day, but the market reverses from that point to close inside the stop. In that case your trade is still alive to turn profitable. The second stop method is used to generate the results in Table 2.3.

TABLE 2.3 Swiss Franc 50-Day Moving Average System 1/1/1980-12/31/1989 with 110-Day Look-Back Filter and Catastrophic Stop

|   Catastrophic Stop ($) |   Winning Trades |   Losing Trades |   Profit ($) |   Profit-per-Trade ($) |
|-------------------------|------------------|-----------------|--------------|------------------------|
|                     250 |               20 |              40 |       32,588 |                    526 |
|                     500 |               23 |              40 |       38,324 |                    608 |
|                     750 |               31 |              33 |       84,887 |                  1,326 |
|                   1,000 |               30 |              34 |       82,775 |                  1,293 |
|                   1,250 |               30 |              34 |       80,512 |                  1,258 |
|                   1,500 |               30 |              35 |       79,662 |                  1,226 |
|                   1,750 |               30 |              35 |       77,162 |                  1,187 |
|                   2,000 |               31 |              34 |       75,425 |                  1,160 |

It  shows the results when we vary the stop loss from $250 to $2,000 in $250 increments.

Obviously, the best stop value to use is $750.

The following points can be made about this system:

- ■ If the draw-downs are reasonable, this would be an excellent system to trade. The average return per year is about $8,500 and the margin required was generally about $3,000 per contract. I would be very happy to trade a system that netted these results.
- ■ This system is pure and simple: one entry rule, one filter, and one piece of risk control logic. I doubt anyone would claim it's got too many variables or that it's over-optimized.
- ■ A $750 stop is relatively small, so even if you're stopped out two or three times in a row, it's not a huge dent to your account.
- ■ The fact that there are more losing trades than winners doesn't concern me. Most longer-term trend-following systems only average between 30 and 45 percent winning trades.
- ■ The profit-per-trade of $1,326 is very comforting because slippage and commission won't be a significant percent of profit.

You know this is supposed to be an example of curve-fitting, so what happened? Table 2.4 shows the results of trading this system on the Swiss franc from 1990 through 2010.

| TABLE 2.4      | Swiss Franc 50-Day Moving Average System 1/1/1990-12/31/2010 with 110-Day Look-Back Filter and $750 Catastrophic Stop   | Swiss Franc 50-Day Moving Average System 1/1/1990-12/31/2010 with 110-Day Look-Back Filter and $750 Catastrophic Stop   | Swiss Franc 50-Day Moving Average System 1/1/1990-12/31/2010 with 110-Day Look-Back Filter and $750 Catastrophic Stop   |
|----------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Winning Trades | Losing Trades                                                                                                           | Profit ($)                                                                                                              | Profit-per-Trade ($)                                                                                                    |
| 77             | 154                                                                                                                     | 30,638                                                                                                                  | 133                                                                                                                     |

The system that averaged $8,500 per year in the 1980s averaged only about $1,500 a year in the following 21 years. The system was obviously tuned up for the 10 years of great trend-following performance by the Swiss franc in the 1980s. In the years that followed, the franc was less 'trendy.'   We curve-fit to a relatively small amount of data, even though we didn't weigh the system down with a lot of rules, filters, and so on.

## Curve-Fitting Is Proportional to the Number of Trades in the Development Sample

If you compare the two curve-fi  tting examples, there's one similarity: They both had a relatively small number of trades in the development sample. Let's  postulate  that  curve-fi  tting  is  proportional  to  the  number  of  trades in the development sample. We know that if we had an infi  nite number of trades, we'd have the entire universe of trades and there could be no curvefi  tting . The  question is: How many trades are 'close enough' to represent the infi  nite sample? An experiment we can use to get an insight into that question  is  to  take  a  commodity  and  generate  a  large  number  of  trades, then sample from the large number and see how many trades need to be in the smaller sample to generate a small diff  erence from the 'infi  nite' sample statistics. If the hypothesis is correct, we should see the diff  erence in results between the 'infi  nite' sample and our smaller sample sizes get smaller and smaller  as  the  number  of  trades  in  the  sample  size  increases.  Figure    2.1 shows the thought.

FIGURE  2.1 Increasing Sample Size Reduces the Diff  erence in Results from the Infi  nite Sample

<!-- image -->

The only issue with that methodology is generating 'diff  erence in results.' Fortunately statisticians have solved this problem for us.  Their methodology is called standard error.  Y ou compute the mean value of the infi  nite sample (the  average  profi  t-per-trade),  and  then  randomly  pick  n-trade  samples  a number of times. If you compute the average of each of these samples, and then compute the standard deviation of the averages, you have the standard error. Hopefully, an example will clarify things.

Suppose you have an infi  nite number of trades generated by a strategy, and that the average profi  t-per-trade across the infi  nite sample was $100. You decide to randomly pull a number of 10-trade samples and see how closely the results match the infi  nite distribution. Figure   2.2 represents the results of randomly selecting fi  ve 10-trade samples.

FIGURE  2.2 Randomly Picking Five 10-Trade Samples from the Infi  nite Distribution of  Trades

<!-- image -->

The average profi  t-per-trade for each sample is:

Sample 1 mean: 97.94

Sample 2 mean: 104.6

Sample 3 mean: 100.17

Sample 4 mean: 101.43

Sample 5 mean: 98.89

The standard deviation across those fi  ve average profi  t-per-trade values is 2.59; that's also the standard error. Now for what it means. One standard deviation above and below the infi  nite sample mean of 100 will statistically include 68.3 percent of the sample means. So 0.683 multiplied by 5 sample means is a value of 4.098 cases.  That number of the sample means should be inside the 97.41 to 102.59 range (mean of 100 minus 1 standard deviation of 2.59 equals 97.41, and mean of 100 plus 2.59 equals 102.59). In our case, four of the sample means were inside the range, and one (104.6) was outside. If we extended this case to draw hundreds of 10-trade samples:

- ■ 68.3 percent of the sample means would fall in the range of 100 minus 1 standard deviation to 100 plus 1 standard deviation.
- ■ 95.4 percent of the sample means would fall in the range of 100 minus 2 standard deviations to 100 plus 2 standard deviations.
- ■ 99.7 percent of the sample means would fall in the range of 100 minus 3 standard deviations to 100 plus 3 standard deviations.

As a trader, this means that if you developed a strategy that had an average profit-per-trade of $100 and a standard error of $2.59, you could be 68.3 percent confident that the true profit-per-trade of the strategy was between $97.41 and $102.59. And you could be 99.7 percent confident that the true profit-per-trade was between $92.23 and $107.77. (My statistics professor would kill me for stating it that way, but dropping all the statistics caveats, that's basically what it means.)

That's how standard error works, but in the real world, you don't get test results. What do you do then? Well, there's a way to get an estimate of the standard error of the mean using just that one sample. Compute the standard deviation of the trades in your back-test and divide by the square

hundreds of n-trade samples.  You only get one sample, and that's your backroot of the sample size. Here are the results for our five samples of 10 trades:

Sample 1: mean = 97.94, standard deviation = 10.26, standard error = (10.26/√10) = 3.25

Sample  2:  mean  =  104.6,  standard  deviation  =  9.28,  standard  error = 2.94

Sample 3: mean = 100.17, standard deviation = 11.19, standard error = 3.54

Sample 4: mean = 101.43, standard deviation = 11.34, standard error = 3.59

Sample 5: mean = 98.89, standard deviation = 7.97, standard error = 2.52

The standard error should be 2.59, as we saw when we used all five of the samples. So the standard error results using just one sample don't match up exactly, but each one is close.

Before we leave hypothetical examples and move to trades, one other concept needs to be explored: the variance of the infinite sample. In the previous example, our five 10-trade samples lined up pretty well with our infinite trade mean of 100. The distance of each sample from the mean of 100 wasn't very far.  The reason they did is because a standard deviation of 10 was chosen for the infinite sample when the thousands of trades that formed the infinite trade distribution were generated. Using a standard deviation  of  10  means  that  68.3  of  the  randomly  generated  trades  will range from 90 to 110 (100 minus 1 standard deviation to 100 plus 1 standard deviation); 95.4 percent of the randomly generated trades will range from 80 to 120 (100 minus 2 standard deviations to 100 plus 2 standard deviations);  and  99.7  percent  of  the  trades  will  range  from  70  to  130 (100 minus 3 standard deviations to 100 plus 3 standard deviations). Real trade distributions are never this tight. Losers might be hundreds or even thousands of dollars, while winners can range the same distance, or more, to the plus side. Instead of the three-standard-deviation range of $60 we had with our example, real trade distributions can have ranges of many thousands of dollars. The bottom line is that the bigger the standard deviation (or variance) of the underlying distribution, the bigger the standard  error. The  following  example  parallels  the  previous  example,  but instead  of  a  standard  deviation  of  10  for  the  infinite  sample,  we'll  use a value of 500. That gives us a three-standard-deviation range of 3,000; 99.7 percent of the trades will be between -$1,500 and +$1,500 from the average profit-per-trade, or trade mean. Here are the results of pulling five 10-trade samples from the 'infinite trade pool' whose statistics are a trade mean of $100 and a trade standard deviation of $500.

```
Sample 1: mean = $263.29, standard error = $165.81 Sample 2: mean = -$31.05, standard error = $151.96 Sample 3: mean = -$71.57, standard error = $95.18 Sample 4: mean = $198.69, standard error = $148.14 Sample 5: mean = $275.74, standard error = $195.65 Average mean = $127.02
```

Based on the average mean of $127.02, this set of samples turned out more positive than the $100 infinite sample mean. The results show the expanded standard error when the infinite distribution has a relatively large variance; instead of a standard error of 2.59 when the standard deviation has 10, the standard error now ranges from $95.18 to $195.65 using a standard deviation of $500.

Again, what this means to the trader is that if his or her back-test yielded 10 trades that averaged a profit of $275.74 with a standard error of $195.65 (Sample 5), he or she could be 68.3 percent confident that the true average profit-per-trade of the strategy was between $80.09 and $471.39. Maybe you would be willing to roll the dice with those odds and trade the strategy, but  consider  this: Y ou  could  just  as  easily  have  yielded  Sample  2  in  your back-test.  In  that  case  your  68.3  percent  chance  sample  mean  would  lie between -$183.01 and $120.91. Not attractive at all.

This example can be used to highlight another problem we're all subject to. Think of each of the five samples as a separate back-test, maybe with one parameter value changed slightly per run.  We're likely to think we're on the right track with and Samples 1 and 5, and on the wrong track with Samples 2 and 3, but the results come from the same distribution. We just can't make a judgment on a small sample with a relatively large standard deviation.

## Testing the Hypothesis that Curve-Fitting Is Proportional to the Number of   Trades in the Sample Using Real Trade Data

After that detour, let's get back to our hypothesis testing with real trade data. Gold was selected because I have daily data going back to 1975. T o generate a lot of trades, a 20-day moving average reversal system was used. It goes long when the average of the last 20 closes is higher than yesterday's average, and closes the long position and goes short when today's average of the last 20 closes is less than yesterday's. The following are some the backtest result statistics:

Winning trades: 233

Losing trades: 450

Total profit: $22,400

Average trade: $32.80

Largest winning trade: $16,230

Largest losing trade: $5,150

Standard deviation of the trades: $1,884

For this analysis, it's not important whether this is a tradeable strategy or not. All we want to know is how many trades we need in a sample to approximate the entire population's results. For the analysis, the profit or loss value for each of the 683 gold trades was placed in a file. Then for  each  sample  size  the  appropriate  number  of  trades  was  randomly selected and the mean of that sample computed. This was done 10,000 times for each sample size. The standard deviation of the 10,000 sample means was used to compute the standard error for that sample size. To summarize for a sample size of 90 trades: 10,000 times 90 trades were randomly selected from the gold trade file containing the 683 trades; the average of the 90 trades for each of the 10,000 sets of trades was computed; the standard deviation of the 10,000 mean values was computed; and then the standard error was computed by dividing the standard error by the square root of 90. The answer for that computation was about $200. Figure   2.3 shows the standard error versus the number of trades randomly selected for each sample. Sample size was limited to 300 because there were only 683 trades in our trade file.

FIGURE  2.3 Standard Error versus Sample Size for Gold Trades

<!-- image -->

The standard error was computed by generating 10,000 samples of each sample size, then computing the average value per sample, and then computing the standard deviation of the 10,000 averages. Sample sizes were varied from 10 trades per sample to 300 trades per sample in 10-trade increments. Figure   2.3 shows that as the number of trades in each sample increases, the standard error decreases. This is in line with our hypothesis. At 300 trades per sample, the standard error is about $100. That's still a rather large difference from the true distribution; the one standard deviation range for that case is the mean trade of $32.80 minus $100, or -$67.20, to $32.80 plus $100, or $132.80. Clearly a bigger sample size is needed to accurately defi  ne the underlying infi  nite sample, but we're pretty much at the limit of the sample size we can use with 683 gold trades standing in as our 'infi  nite sample.'

To get a bigger infi  nite sample, Commodity Systems Inc. (CSI) continuous contract data on 37 domestic commodities was used going back as far as CSI had data for them. Across those data, the 20-day reversal system had the following back-test trade statistics:

Winning trades: 7,875

Losing trades: 17,107

T otal profi  t: $845,713

Average trade: $33.85

Largest winning trade: $99,641.20

Largest losing trade: $12,800

Standard deviation of the trades: $2,316

Figure   2.4 shows the standard error as a function of trade sample size when sample size is incremented from 20 trades to 1,000 trades in steps of 20 trades.

FIGURE  2.4 Standard Error versus Sample Size for a Large Group of Commodity  Trades

<!-- image -->

Figure   2.4 shows that even when the sample size is 1,000 trades, the standard error is still relatively large-about $75.

For a trader there is a practical lesson that can be learned from the foregoing discussion.  The larger the variance of your back-test results, the bigger your sample size needs to be to have confi  dence that the results are a true indication of how the strategy will trade in the future. In the fi  rst example, the standard deviation of the trade sample was 10. That yielded a standard error of about 2.5 when we pulled 10 samples from the distribution.  When the  standard  deviation  of  the  trade  sample  was  increased  to  500  and  10 samples were used, the standard error jumped to a range of about 95 to 195. And from the last graph (Figure 2.4), we see that the standard error is about 500 when the standard deviation of the trades grew to 2,316. There's good news and bad news about these facts for both shorter-term and longer-term traders:

- ■ Shorter-term strategies will have smaller average profits (bad news) but smaller  average  losses  (good  news). The  standard  deviation  across  all trades will be relatively smaller, so the standard error will be relatively smaller  and  fewer  samples  will  be  needed  to  minimize  curve-fitting (good news).
- ■ Longer-term strategies will have larger average profits (good news) but larger average losses (bad news). The standard deviation across all trades will be relatively larger, so the standard error will be relatively larger and more samples will be needed to minimize curve-fitting (bad news).

## ■ Testing for Curve-Fitting

The statistics are over. The point of the previous section was that for most trading  systems  (I  won't  say  all,  but  I'm  thinking  all)  you  need  many hundreds to thousands of trades in your back-test to minimize the effects of curve-fitting and gain the confidence that real trading will match the parameters of your back-test. I don't expect someone to statistically test his model to see if it's curve-fit. I have a relatively easy and robust way for you to convince yourself whether a system you develop is minimally curve-fit, or not. It's called 'Build, Rebuild, and Compare,' or BRAC.  The method involves using all the historical data for the instrument(s) you intend to trade in your development sample. As you build the strategy, keep track of the steps you took and the selection logic you used, and if you wind up developing a strategy that performs well, you've completed the 'Build' part. Next, cut some data off the end of your historical data. If you were using 20 years of daily-bar data, you might cut the last year off. Then with the smaller historical database 'Rebuild' your strategy using the same steps and decision criteria you used the first time.  The last step is to input all the historical data into the 'Rebuilt' strategy and 'Compare' the performance over the period of the withheld data with the performance of the first strategy over the same period. If the performance is similar, you can have pretty good confidence that your strategy will hold up in real trading.

## BRAC Example

Let's use the data for the 37 domestic commodities we used in the previous curve-fitting discussion and build a moving average system just like we did for the Swiss franc curve-fitting example earlier in this chapter. In that example, we used the following steps and used the accompanying selection logic:

- ■ Vary the number of days for the moving average from 10 to 120 in 10-day increments. Select the number of days that yields the largest profit.
- ■ Vary the number of days for the look-back filter from the moving average value plus 10 days to 200 in 10-day increments. Select the look-back value with the largest profit.
- ■ Vary  the  catastrophic  stop  value  from  $250  to  $2,000  in  $250  increments. Select the stop value that yields the largest profit.

When those three steps and the associated decision logic are implemented, we get the results shown in Table 2.5 from the start of the CSI data for each of the 37 commodities until the end of 2010.

TABLE 2.5

## Moving Average System across 37 Commodities: Number of Days for the Moving Average

| Number of Days   |   Winning Trades |   Losing Trades |   Profit ($) |   Profit-per-Trade ($) |
|------------------|------------------|-----------------|--------------|------------------------|
| 10               |           11,614 |          24,153 |     -884,394 |                    -25 |
| 20               |            7,875 |          17,107 |      845,713 |                     33 |
| 30               |            6,318 |          13,976 |    1,084,360 |                     53 |
| 40               |            5,266 |          12,153 |    1,377,589 |                     79 |
| 50               |            4,734 |          10,822 |    1,433,893 |                     92 |
| 60               |            4,208 |          10,060 |    1,579,068 |                    110 |
| 70               |            4,021 |           9,020 |    2,005,335 |                    153 |
| 80               |            3,585 |           8,201 |    2,252,218 |                    191 |
| 90               |            3,287 |           7,569 |    2,403,499 |                    221 |
| 100*             |            3,158 |           7,067 |    2,591,263 |                    253 |
| 110              |            2,923 |           6,810 |    2,253,408 |                    231 |
| 120              |            2,820 |           6,441 |    1,863,185 |                    201 |

* = value selected based on criteria The highest profit across the runs is when the number of days for the average is 100. That is the value selected. Table 2.6 shows the results when we add a trend look-back filter so that only trades in the direction of the longer-term trend are taken.

TABLE 2.6

Moving Average System across 37 Commodities: Add an N-Day

Look-Back Filter

| Number of Days   |   Winning Trades |   Losing Trades |   Profit ($) |   Profit-per-Trade ($) |
|------------------|------------------|-----------------|--------------|------------------------|
| 110              |            2,316 |           4,887 |    2,646,091 |                    372 |
| 120              |            2,202 |           4,665 |    2,506,464 |                    365 |
| 130              |            2,141 |           4,536 |    2,402,654 |                    359 |
| 140              |            2,113 |           4,428 |    2,493,393 |                    381 |
| 150              |            2,123 |           4,363 |    2,499,807 |                    385 |
| 160              |            2,101 |           4,264 |    2,519,704 |                    395 |
| 170              |            2,078 |           4,171 |    2,495,891 |                    399 |
| 180              |            2,043 |           4,129 |    2,538,957 |                    411 |
| 190              |            2,038 |           4,102 |    2,612,408 |                    425 |
| 200*             |            2,055 |           3,996 |    2,681,790 |                    443 |

The largest profit is seen with a look-back filter of 200 days, so that will be the value we select. Now let's add a catastrophic stop. Table 2.7 shows the results.

TABLE 2.7 Moving Average System across 37 Commodities: Add a Catastrophic Stop

| Catastrophic Stop ($)   |   Winning Trades |   Losing Trades |   Profit ($) |   Profit-per-Trade ($) |
|-------------------------|------------------|-----------------|--------------|------------------------|
| 250                     |            2,362 |           8,682 |    2,140,902 |                    193 |
| 500                     |            2,260 |           6,474 |    2,298,666 |                    263 |
| 750                     |            2,196 |           5,516 |    2,390,608 |                    309 |
| 1,000                   |            2,160 |           4,982 |    2,482,679 |                    347 |
| 1,250                   |            2,141 |           4,705 |    2,538,943 |                    370 |
| 1,500                   |            2,127 |           4,540 |    2,524,710 |                    378 |
| 1,750                   |            2,116 |           4,411 |    2,542,710 |                    389 |
| 2,000*                  |            2,103 |           4,326 |    2,555,125 |                    397 |

A $2,000 catastrophic stop yielded the most profit, so that value will be selected.

The system developed across all the data had 2,103 winning trades, had 4,326 losing trades, and netted $2,555,125 across its lifetime. For the last year  of  performance  (1/1/2010  to  12/31/2010),  the  system  had  these profitability benchmarks:

Winning trades:

101

Losing trades:

205

Profit:

$333,407

Now let's go back and rebuild the strategy using the same steps and logic, but with the last year of data withheld from the back-test. T ables 2.8 through 2.10 show the parameter values selected at each step based on the selection criteria.

TABLE 2.8

## Moving Average System across 37 Commodities: Number of Days for Moving Average

| Number of Days   |   Winning Trades |   Losing Trades |   Profit ($) |   Profit-per-Trade ($) |
|------------------|------------------|-----------------|--------------|------------------------|
| 100*             |            2,982 |           6,707 |    2,250,087 |                    232 |

TABLE 2.9

## Moving Average System across 37 Commodities: Add a Look-Back Trend Filter

| Number of Days   |   Winning Trades |   Losing Trades |   Profit ($) |   Profit-per-Trade ($) |
|------------------|------------------|-----------------|--------------|------------------------|
| 200*             |            1,957 |           3,832 |    2,361,508 |                    407 |

## TABLE 2.10

## Moving Average System across 37 Commodities: Add a Catastrophic Stop

| Catastrophic Stop ($)   |   Winning Trades |   Losing Trades |   Profit ($) |   Profit-per-Trade ($) |
|-------------------------|------------------|-----------------|--------------|------------------------|
| 2,000*                  |            2,002 |           4,121 |    2,221,718 |                    362 |

It may surprise you that the parameter values at each step turned out to be the same as those using the entire data sample. I'm not surprised, because if  you develop strategies with thousands of trades, the best parameter set doesn't flop around from year to year. When I developed a system I market called Aberration on a basket of 35 commodities, the best parameter value was 80 days of data. Over 25 years later that's still the best parameter value and now I use a basket of 57 worldwide commodities. So in this BRAC test, the  one  year  of  data  withheld  from  the  second  development  yielded  the same results as our initial results when it is included back in the back-test. In  the  succeeding chapters we'll be developing more strategies. We'll do a  BRAC test on some and in cases we'll see an element of curve-fitting. But remember: There's always a certain element of curve-fitting because we don't have an infinite data set and we're developing a solution based on historical data.  The key is to minimize curve-fitting as much as possible.

## BRAC versus Out-of-Sample Testing

It's funny how some things somehow get elevated to cult status as the be-all and end-all solution to a given problem. In the trading world, I consistently run across three things that I would put in that category:

1.  Monte Carlo analysis will tell you how much your strategy will really make, and what the worst draw-down will really be.
2.  A divergence signal is a very powerful entry technique.
3.  The only trustworthy measure of a good system is out-of-sample testing.

I  present my thoughts and analysis on Monte Carlo analysis and divergence elsewhere in this book, but this is an appropriate time to talk about out-of-sample testing. One of the questions asked most at seminars I present is: How much out-of-sample testing do you do before you trade a system? I don't do any. If a developed system passes the BRAC test and it fits with the  other  systems  I'm  trading,  I'll  trade  it. The  main  problem  with  outof-sample testing is there is no performance reference for the out-of-sample results.  Suppose  you  develop  a  system  on  all  the  available  data  and  your out-of-sample test is 'watch how it trades for the next year.'   Your 20-year back-test, which includes thousands of trades, averages $20,000 per year with an average draw-down of $10,000 a year and a max draw-down of $20,000. When you watch it for a year out of sample, you lose $5,000 and have a $15,000 draw-down along the way. Is this a failed out-of-sample test? I think it depends. Suppose the last five years of trading looked like this:

| Year         | Return   | Max Draw-Down   |
|--------------|----------|-----------------|
| 5 years ago: | $30,000  | $5,000          |
| 4 years ago: | -$5,000  | $15,000         |
| 3 years ago: | $40,000  | $5,000          |
| 2 years ago: | $15,000  | $15,000         |
| 1 year ago:  | $20,000  | $10,000         |
| Average      | $20,000  | $10,000         |

If your out-of-sample year had been four years ago, the $5,000 loss and $15,000 draw-down would have been the 'right' answer, but based on this test most people would discard the strategy.

If your out-of-sample methodology is to develop the strategy on 19 out of  20  years  and  then  see  how  it  does  when  you  add  back  in  the  missing year, you are missing critical data. A shortfall of data is a huge development problem. If we had infinite data, this chapter wouldn't exist.  Why make the problem even worse by withholding it?

The BRAC methodology solves both of these problems by giving you a performance reference for data not included in the development sample, and by letting you use all available data for your development sample at the same time.

## Last  Word on Curve-Fitting

I think there's a conspiracy out there that leads traders into the curve-fitting trap. The conspiracy is perpetrated by companies that sell development software. Almost every package has the 'chart paradigm' where you put one, or more, charts in a window and develop a strategy on the data for the one symbol on that chart.  That leads to developing a solution on one set of data that is probably too small. Further, the point-and-click ease with which you can add trading rules, stops, and filters, and then optimize all of them, leads the trader to think 'this is how it's supposed to be done.' I say it's a conspiracy because the software companies know there's a curve-fitting problem with that methodology, but it's so easy for a potential customer to 'find the holy grail' in a two-week trial with this paradigm that a sale of the software is almost assured.

A better solution is to offer packages that allow the user to develop across a basket of symbols at the same time, but it's hard work to find a tradeable solution in that manner, and the spectacular trade charts you see in the ads won't look nearly as good.

## ■ Other Impediments to a Valid Back-Test

If you develop a strategy and it fails in real-time trading, I'd guess there's a 90 percent probability that you curve-fit the strategy to the data. But there are other possible reasons:

- ■ Assuming every point in a bar was a trade point.
- ■ Dual orders within a bar.

- ■ Realistically accounting for transaction costs.
- ■ Limit order mania.

The relatively good thing about these impediments is that their severity  lessens  as  your  profit-per-trade  goal  goes  up.  If  you  develop  on  daily bars and try to make $500, or more, per trade, one, or more, of these issues might dampen your return, but they probably won't kill the strategy. If you're looking to scalp $50 profits two or three times a day, any one of these things could kill the system and make it a net loser.

## Assuming Every Point in a Bar Was a Trade Point

If you use daily bars and a stock has an open, high, low , and close for the day of 101, 101, 99, and 99, your back-testing platform will probably assume that there were 200 trading points that day: one at each cent of the range from 101 down to 99. In reality, the stock could have opened at 101 gapped down to 100.5 and then traded down in 1-cent increments to the closing price of 99. If your strategy had a short entry at 100.95 on a stop, your software will probably give you that price, but in reality, you'd have been filled at 100.5, or less. If you're a longer-term trader, the $0.45 won't kill you, but if you're trying to make $0.10 a trade, that $0.45 is four and a half trades of profit.  The solution to this back-testing impediment is to go ahead and develop on daily bars, but if you find something you like, do a comparison of a portion of your daily-bar results with the results using the same strategy on finer resolution bars: five-minute bars, one-minute bars, tick data (tick data is a plot of every trade point, not a bar that contains summary information for all trades in a given time-frame), and so forth.

## Dual Orders within a Bar

Many strategies  actually  have  one  or  more  orders  valid  for  a  single  bar. Examples are:

- ■ Breakout systems where you place a buy stop and a sell stop before the market opens and let the market decide your position based on the first breakout.
- ■ Counter-trend, or trading range systems where you put a sell limit above the current price, and a buy limit below current price and hope that price moves up or down to your entry price then moves back the other way

- and you're taken out of the trade with a profit when the other limit order acts as a profit-target.
- ■ Contingent orders where you put in an entry order and a contingent order for stop protection should the entry execute.

The problem with these types of orders is that there's no way to know which order gets hit first if the bar range encompasses both orders. In the second example in this list, it doesn't matter, because both trades will always be winners, but in the other two it does. Again, the way to get around this back-testing issue is to go to finer resolution data to find out which order really got hit first.

## Realistically Accounting for Transaction Costs

Transaction costs include slippage and commission. (Actually, taxes on profits should probably be included, but no one talks about that.) When I released my first commercial trading system in 1993, I included transaction costs of $75 per contract for every 60 trading days the trade lasted. The 60-day addition was to account for rollover costs from one contract to the next. Back then a typical broker would charge you about $25 round-turn per futures contact, and the pit would find a way to take another $50 away from you no matter what your order was or when you placed it (remember the dreaded words, 'fast market conditions'). We've come a long way from then. Brokers are much more competitive (you can trade a futures contract from $2 to $5 a round-turn, and $25,000 worth of stock for about $5 to $10, in-and-out), and the electronic markets have reduced bid/ask spreads to 1 to a few ticks, except at night. So the impact of transaction costs on a trade is much less than it used to be. But if you're looking to make relatively small profits on a strategy, realistic transaction costs need to be factored in.

The following are the development slippage numbers I use in my backtesting; you can use the actual commission numbers of your own broker.

## Stocks

I only trade stocks that have an average liquidity of $20,000,000 over the last five trading days. I define liquidity as closing price multiplied by volume. I almost never use stop orders intra-day for liquidity considerations. I use the following types of orders and expect slippage to average the figure noted:

Market-on-open orders: A penalty of $0.015 from the print open; that's 1.5 cents.

- Market-on-close orders: A penalty of $0.0025 from the print close; that's 1/4 of a penny.

Limit orders: See the 'Limit Order Mania' section that follows.

There is something you should be aware of if your account size is relatively small. An odd lot is now classified as an order for less than 100 shares. If  you're doing market-on-open orders for an odd lot, your slippage will average  much  more  than  an  opening  order  for  a  round  lot  (larger  than 100 shares). That's because odd-lot orders aren't included in the opening pair-offs the exchanges do and only get filled with other matching odd-lot orders. Slippage on these can be so large, I avoid doing them.

## Commodities

I'll trade even the more illiquid commodities if the profit-per-trade for the strategy is relatively high, but I expect more slippage with them.

- Market and stop orders during the day: $25
- Market and stop exit orders during the night session: I wait until the day session when the spreads are better to get out.

## Foreign Exchange (FX)

I'm  not  a  big  FX  trader,  but  when  I  do;  my  orders  are  generally  limit orders because I consider FX easiest to trade in a counter-trend manner. If you have a FX broker, not a market-maker, and you're trading pairs that involve the six major currencies, three to four pips round-turn is a good number.

## Limit Order Mania

At  some  point,  I'm  sure  nearly  every  trader  sees  a  potential 'golden goose' in limit orders. On the surface, they eliminate all concerns about slippage  because  you  get  your  price,  or  better.  But  the  reality  is  that slippage occurs in a different way with limit orders: missed entries. I used to trade a stock system that put out 20 to 30 buy limit orders each day. I only wanted 10 entries, so when 10 fills occurred, my software would cancel the rest. The system made money, but never as good as my back-tests. What was happening was that I missed some of the best fills, but always got filled on the ones that traded down to my price, and kept going down from there. In other words, I missed some big winners, but always seemed to get the losers.

If price goes down to your buy limit price, you only get filled for sure if there is sufficient liquidity on the other side of the order to take out all the buy orders at that price. Otherwise you miss getting filled at all, or get only a partial fill. Many will argue that in the very liquid markets like the S&amp;P and FX currencies there is plenty of liquidity at all price points. That's just not so. Even trading one contract, or one $100,000 FX unit, price can trade at your limit order and you may not get filled, but your back-test software will assume you did. I've sat at my screen many times with hundreds of bids sitting at my limit buy order price, saying, 'Come on, give it to me,' and it  doesn't happen. So the problem for strategies that use limit orders for entry, or as a profit-target exit, is that you will miss some of the fills that just hit your price, and your results will always be a little worse than your back-test. If your profit-per-trade is relatively large, you will probably just cal trades. But if your profit-per-trade is relatively small, this problem could

see a performance drop-off in your real-time trades versus your hypothetibe a deal-breaker.

For systems that use limit orders to scalp small profits, the drop-off in real fills from hypothetical back-test fills can be so great that a money machine turns into a money pit. Here's a real example. I implemented the following logic in 'auto-trading' software on the emini S&amp;P with a five-minute chart after a back-test showed fantastic results:

Entry Orders

Limit buy point = Close - 0.75 points

Limit sell point = Close + 0.75 points

Stop after Entry

Stop = $75 from entry price (1.5 emini S&amp;P points)

Limit Order Profit Targets

Sell to cover limit = Close + 0.75 points

Buy to cover limit = Close - 0.75 points

During the one-month period of March 12, 2011, to April 12, 2011, the strategy had these back-test statistics:

Wining trades: 928

Losing trades: 330

Total profit: $21,525

Profit-per-trade: $15.90

Max draw-down: $1,262.50

The hypothetical equity curve was just about a straight line from the bottom left to the top right of the chart, while in real trading, just about all of the losing trades would occur, but you'd only get about half the winners. The only one who would marvel at the strategy would be your broker, as he collects over 600 round-turn commissions a month.

## ■ Conclusion

After  you  develop  a  tradeable  strategy,  you  want  it  to  trade  in  real-time like it back-tested. This chapter illustrated the most probable reasons for a performance drop-off. By far, the likeliest reason is curve-fitting in the development process. As you develop, I urge you to ask yourself the following question: Can I be curve-fitting in any way by doing this step?

Appendix D has some examples of curve-fitting that might surprise you. I  urge  you  to  look  them  over. The  safest  way  to  ensure  a  low  degree  of curve-fitting is to do a BRAC test after you find a strategy you're interested in trading.

## Find the Path of Least Resistance in the Market  You Want to Trade

T his chapter explores the trading characteristics of three market classes: stocks, commodities, and foreign exchange (FX) currency pairs. Each of these classes is traded worldwide, and each has tremendous liquidity for ease of trading. Many traders assume that every market should be traded the same way, but, for whatever reason, market classes do behave differently. Moreover, within a market class the individual instruments behave differently in different time frames (monthly, weekly, daily, intra-day bars). This chapter  will  illustrate  these  differences  and  show  a  general  approach  for determining the characteristics of a trading class.

Finding  the  tendencies  of  a  market  class  is  a  shortcut  to  finding  good trading approaches for that class. If a market tends to trend in a certain time frame, trend-following techniques like moving averages, breakouts, trendlines,  and  so  forth  are  a  good  place  to  start  the  development  process.  If a market tends to counter-trend behavior, overbought/oversold oscillators like RSI, stochastic, or momentum might be good starting points.

## ■ Markets Are Different: Daily Bars

To illustrate that market classes can move in fundamentally different ways, we'll use an easy-to-understand process on daily stock and commodity data. After the data is presented, you'll probably agree that stocks move primarily  in  a  counter-trend  manner  (weak  stocks  outperform  strong  stocks  to the upside), while commodities tend to trend (strong commodities tend to continue upward, while weak commodities tend to continue downward). The process uses the following steps:

- Step 1: Determine baseline buy-and-hold performance. At the start of each month, every member of the two classes will be invested in. For stocks, the equity existing at the end of the month will be divided by the number of stocks in the class and the number of shares representing that dollar value will be bought. At the end of the month, those shares in each stock are sold at the end-of-month prevailing price. For commodities, one contract of each commodity will be bought at the price on the open of the first trading day of the month.  Those contracts will be cashed out at the closing price at the end of the month. For stocks, we'll use a baseline of 1,714 highly liquid stocks from the year 2000 through the end of 2011. The baseline performance metric for stocks will be percent profit-per-trade for the month. For commodities, we'll use a basket of 56 worldwide commodities over the same years, and the performance metric will be dollar return for the one-lot trade.
- Step 2: Determine the performance of a trend-following strategy on strong stocks and commodities.  This step duplicates the buy-and-hold methodology and metrics except the stocks and commodities that are bought at the first of each month are those whose closing price at the end of the month is one standard deviation above the average of the last 20 closes.  The standard deviation measure is the standard deviation of the last 20 closes.
- Step  3:  Determine  the  performance  of  a  counter-trend  buy  strategy  on weak stocks and commodities.  This step uses the same methodology and metrics as the trend-following strategy on strong stocks, except the instruments that are bought are those whose closing price is one standard deviation of price below the average of the last 20 closes.

## Results of the  Three-Step Process for Stocks

Table 3.1 shows the results of the three-step process on stocks. All transactions are broken out by year. The average profit-per-year is the average return across the 12 months of the year. The average profit-per-trade numbers at the end of the table show the average profit across all transactions.

## Results of Different Stock Buying Strategies Results Shown in

TABLE 3.1 Average Percentage Profit-per-Month

| Year                |   Buy-and-Hold |   Trend-Following: Buy Strong Stocks |   Counter-Trend: Buy Weak Stocks |
|---------------------|----------------|--------------------------------------|----------------------------------|
| 2000                |           1.78 |                                 0.41 |                             1.96 |
| 2001                |           0.41 |                                -1.46 |                             4.11 |
| 2002                |          -1.26 |                                -1.11 |                            -0.82 |
| 2003                |           2.95 |                                 2.56 |                             3.85 |
| 2004                |           1.54 |                                 0.95 |                             2.33 |
| 2005                |           1.01 |                                 1.19 |                             0.65 |
| 2006                |           1.35 |                                 1.08 |                             1.43 |
| 2007                |           0.99 |                                 1.68 |                             0.81 |
| 2008                |          -3.57 |                                -4.81 |                            -3.79 |
| 2009                |           3.38 |                                 1.55 |                             3.63 |
| 2010                |           1.08 |                                -0.62 |                             1.37 |
| 2011                |           0.03 |                                -1.11 |                             1.79 |
| Average Profit-per- |                |                                      |                                  |
| Trade (Percent)     |           0.71 |                                 0.16 |                             1.56 |

The  results  in T able  3.1  show  that  the  average  profit-per-trade  for  the buy-and-hold strategy across the basket of 1,714 stocks is 0.71 percent per month. If  you  adopt  the  trend-following  strategy  of  buying  strong  stocks, you  will  only  make  0.16  percent  per  trade,  which  underperforms  buyand-hold by about 70 percent per month. But if you adopt a counter-trend strategy  of  buying  weak  stocks  at  the  start  of  each  month,  you  will  make 1.56 percent per trade, which outperforms buy-and-hold by over 100 percent per month. Clearly, the easiest approach to take when working with daily-bar stock data and an intermediate time frame, like a month, is to buy weakness.

You  will  note  that  this  basket  of  stocks  outperformed  the  general market over the same time frame. This is due to survivorship basis. The 1,714 stocks were the most liquid stocks at the end of 2011 when the analysis  was  conducted. Through  the  years  other  stocks  would  have made the  list,  but  they  are  no  longer  trading,  many  because  of  poor performance. Their contribution would have brought the returns in line with the actual market performance. Still, this is not considered a major flaw in the study. The same market data was presented to each of the three strategies.

## Results of the  Three-Step Process for Commodities

Table  3.2  shows  the  results  of  the  three-step  process  on  the  basket  of 56 commodities. All transactions are broken out by year.  The average profitper-year is the sum of each transactions profit for each month in dollars divided by the total number of long transactions for the year.

TABLE 3.2

## Results of Different Commodity Buying Strategies: Results Shown in Average Dollar Profit-per-Monthly-Transaction

| Year        | Buy-and-Hold   | Trend-Following: Buy Strong Commodities   | Counter-Trend: Buy Weak Commodities   |
|-------------|----------------|-------------------------------------------|---------------------------------------|
| 2000        | 8              | -109                                      | -205                                  |
| 2001        | -305           | -625                                      | -903                                  |
| 2002        | 41             | -9                                        | 196                                   |
| 2003        | 429            | 434                                       | 473                                   |
| 2004        | 68             | 299                                       | 834                                   |
| 2005        | 169            | 193                                       | 419                                   |
| 2006        | 353            | 940                                       | 45                                    |
| 2007        | 629            | 1,085                                     | -668                                  |
| 2008        | -377           | 130                                       | -1,550                                |
| 2009        | 439            | 524                                       | 731                                   |
| 2010        | 345            | 381                                       | 833                                   |
| 2011        | -642           | -1,113                                    | 1,270                                 |
| Average per |                |                                           |                                       |
| Trade       | $66            | $158                                      | $23                                   |

The results in  Table 3.2 show that the average buy-and-hold profit-pertrade across the basket of 56 commodities is $66. If you adopt a trendfollowing  strategy  of  buying  strong  commodities,  you  will  outperform buy-and-hold by $92 per transaction, almost 140 percent. If you adopt a counter-trend strategy of buying weak commodities at the start of each month, you will underperform buy-and-hold by about $43 per transaction. Clearly, the easiest approach to take when working with daily-bar commodities is to be a trend-follower: buy strong commodities and sell weak commodities.

When I first ran this analysis, I was surprised that the counter-trend strategy of buying weak commodities actually made the small profit of $23 per trade. I had expected to see the approach lose, on average, per trade. I reran the counter-trend strategy across all the commodity data from 1980 to the end of 2011. That run had each trade losing $45 per trade on average. I'm guessing that the disparity is due to the rise of asset class funds in the last decade.  These funds are buy-only in one or more asset classes like the metals or energies.  T o them, weakness in a commodity in their asset class looks like a buying opportunity. As you develop commodity systems you'll find that the long-side trades usually make two or three times as much as the shortside trades. Part of the reason is evident in Table 3.2. Any time you make a buy trade, you have a $66 per month profit built in to the trade (the average profit across all buy-and-hold-for-a-month trades).

The $66 per trade average of the buy-and-hold trades is not just an anomaly of the 2000-2011 time frame. Using the same 56 commodities, I looked back  to  the  year  1980,  and  the  buy-and-hold  for  that  entire  period  was $50 per trade. Clearly the path of least resistance in the commodity world is up.

## Results of the  Three-Step Process for FX Pairs

The preceding analysis is relatively easy to perform on any asset class or time frame. In FX trading, there are seven major currencies: the U.S. dollar, the euro currency (before 1999, the deutsche mark), the Swiss franc, the British pound, the Japanese yen, the Australian dollar, and the Canadian dollar. Each currency can be traded against every currency, so there are 21 major pairs. When trading FX pairs, a 'one lot' of 100,000 units of the currency was used and the results of each trade converted to dollars.  The previous analysis was conducted on the daily-bar data of these FX pairs going back to the start of the year 2000.  The results are shown in  Table 3.3.

TABLE 3.3

## Results of Different FX Pairs Buying Strategies: Results Shown in Average Dollar Profit-per-Monthly-Transaction

| Year              | Buy-and-Hold   | Buy Strong FX Pairs   | Buy Weak FX Pairs   | Counter-Trend Approach   |
|-------------------|----------------|-----------------------|---------------------|--------------------------|
| 2000              | -109           | 506                   | -743                | -572                     |
| 2001              | 249            | 304                   | 640                 | 290                      |
| 2002              | 283            | -578                  | 894                 | 750                      |
| 2003              | 170            | -111                  | 867                 | 626                      |
| 2004              | 143            | -67                   | 10                  | 129                      |
| 2005              | -142           | -233                  | -47                 | 45                       |
| 2006              | 670            | 63                    | 1,125               | 484                      |
| 2007              | -34            | 215                   | -477                | -300                     |
| 2008              | -1,348         | 1,356                 | -1,745              | -1,628                   |
| 2009              | 140            | -1,040                | 986                 | 1,005                    |
| 2010              | -746           | -2,332                | -22                 | 1,237                    |
| 2011              | -199           | -1,022                | 160                 | 685                      |
| Average per Trade | -$87           | -$101                 | $178                | $137                     |

The results in  Table 3.3 show that the average buy-and-hold performance per trade across the basket of 21 FX pairs is a loss of $87 per month. If you adopt a trend-following strategy of buying strong pairs, you will underperform buy-and-hold by $14 per transaction. If you adopt a counter-trend strategy of buying weak FX pairs at the start of each month, you will outperform buy-and-hold by $265 per transaction. Since FX pairs are traded without any penalty both long and short, the counter-trend approach of buying weak FX pairs and selling strong pairs is the path of least resistance. The results of implementing this counter-trend approach are shown in the last column of the table. The average profit-per-trade traded in this manner is $137; that's $224 more than the baseline buy-and-hold.

## FX Pairs Are Generally Considered Great  Trenders

These results may be surprising to some traders. It is commonly held that the currencies are great trending instruments. This belief may be due to the tendency of the commodity currencies to trend.  The popularity of speculative FX trading is relatively new , while the trading of currency commodities dates back to the 1970s; six currency commodities have traded since then. They correspond to the major currencies versus the U.S. dollar. Table 3.4 compares buy-and-hold on the six major FX pairs against the dollar versus their

<!-- image -->

Comparison of Six U.S. Dollar-based FX Pairs versus Corresponding

Commodities: Results Shown in Average Dollar Profit-per-Monthly-

Transaction counterpart commodity currencies.  The last two columns compare the results of trading a trend-following methodology on both the FX pairs and the commodity currencies.

| Year                      |   Buy-and-Hold FX Dollar-Based Pairs |   Buy-and-Hold Dollar- Based Commodities |   Trend-Follow-Trade U.S. Dollar FX Pairs | Trend-Follow-Trade U.S. Dollar Commodities   |
|---------------------------|--------------------------------------|------------------------------------------|-------------------------------------------|----------------------------------------------|
| 2000                      |                                  172 |                                     -777 |                                       634 | 783                                          |
| 2001                      |                                  266 |                                     -518 |                                       550 | 428                                          |
| 2002                      |                                  170 |                                      844 |                                        -9 | -106                                         |
| 2003                      |                                   71 |                                    1,355 |                                     1,150 | 582                                          |
| 2004                      |                                  367 |                                      567 |                                        10 | -119                                         |
| 2005                      |                                 -290 |                                     -984 |                                      -107 | 160                                          |
| 2006                      |                                  474 |                                      416 |                                    -1,052 | -536                                         |
| 2007                      |                                  233 |                                      639 |                                     1,150 | 890                                          |
| 2008                      |                                 -875 |                                     -573 |                                     2,117 | 1,989                                        |
| 2009                      |                                  111 |                                      760 |                                    -1,153 | - 416                                        |
| 2010                      |                                 -344 |                                      521 |                                      -951 | -1,237                                       |
| 2011                      |                                 -142 |                                      208 |                                      -996 | -921                                         |
| Average Profit- per-Trade |                                   22 |                                      214 |                                       210 | 208                                          |

Table 3.4 raises two questions:

- ■ Why is buy-and-hold so different between the FX pairs and their corresponding  commodity  currencies? The  FX  dollar-based  pairs  average $22 per transaction, while the corresponding commodities make almost 10 times as much at $214 per transaction.
- ■ When trading FX pairs, why is trend-following profitable with the six major currencies against the dollar, when trend-following across all 21 major currency pairs is a net loser?

Regarding the first  question,  two  possibilities  leap  to  mind.  First,  the disparity might just be a time-frame issue. Maybe over the long haul the difference isn't so pronounced. Another strong possibility is the 'time to carry' pricing of commodities.

More perplexing is the second issue: the trend-following nature of the dollar-based FX pairs, and the counter-trend-following nature of the rest of the pairs on daily-bar data. Table 3.5 shows the results of implementing our trend-following approach on each of the seven types of currency pairs.

| TABLE 3.5                 | Trend-Following on FX Pairs: Results Shown in Average Dollar Profit- per-Monthly-Transaction   | Trend-Following on FX Pairs: Results Shown in Average Dollar Profit- per-Monthly-Transaction   | Trend-Following on FX Pairs: Results Shown in Average Dollar Profit- per-Monthly-Transaction   | Trend-Following on FX Pairs: Results Shown in Average Dollar Profit- per-Monthly-Transaction   | Trend-Following on FX Pairs: Results Shown in Average Dollar Profit- per-Monthly-Transaction   | Trend-Following on FX Pairs: Results Shown in Average Dollar Profit- per-Monthly-Transaction   | Trend-Following on FX Pairs: Results Shown in Average Dollar Profit- per-Monthly-Transaction   |
|---------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Year                      | U.S. Dollar Pairs                                                                              | Australian Dollar Pairs                                                                        | British Pound Pairs                                                                            | Canadian Dollar Pairs                                                                          | Euro Currency Pairs                                                                            | Japanese Yen Pairs                                                                             | Swiss Franc Pairs                                                                              |
| 2000                      | 634                                                                                            | 432                                                                                            | 1,075                                                                                          | 762                                                                                            | 606                                                                                            | 980                                                                                            | 357                                                                                            |
| 2001                      | 550                                                                                            | 599                                                                                            | -1,476                                                                                         | -820                                                                                           | 591                                                                                            | 1                                                                                              | -899                                                                                           |
| 2002                      | -9                                                                                             | -817                                                                                           | -739                                                                                           | -1,254                                                                                         | -985                                                                                           | 85                                                                                             | -510                                                                                           |
| 2003                      | 1,150                                                                                          | -689                                                                                           | -1,071                                                                                         | -910                                                                                           | -756                                                                                           | -510                                                                                           | -973                                                                                           |
| 2004                      | 10                                                                                             | 78                                                                                             | -211                                                                                           | 637                                                                                            | 223                                                                                            | -1,351                                                                                         | 126                                                                                            |
| 2005                      | -107                                                                                           | -473                                                                                           | 436                                                                                            | -142                                                                                           | -213                                                                                           | 679                                                                                            | -327                                                                                           |
| 2006                      | -1,052                                                                                         | -512                                                                                           | -184                                                                                           | -98                                                                                            | -421                                                                                           | -520                                                                                           | -430                                                                                           |
| 2007                      | 1,150                                                                                          | 319                                                                                            | -85                                                                                            | 517                                                                                            | 376                                                                                            | 916                                                                                            | 438                                                                                            |
| 2008                      | 2,117                                                                                          | 3,145                                                                                          | -935                                                                                           | 618                                                                                            | 1,621                                                                                          | 4,588                                                                                          | 1,367                                                                                          |
| 2009                      | -1,153                                                                                         | 192                                                                                            | -1,584                                                                                         | -2,023                                                                                         | -77                                                                                            | -891                                                                                           | -965                                                                                           |
| 2010                      | -951                                                                                           | -1,202                                                                                         | -1,015                                                                                         | -927                                                                                           | -357                                                                                           | -1,548                                                                                         | -1,689                                                                                         |
| 2011                      | -996                                                                                           | -1,010                                                                                         | -381                                                                                           | -570                                                                                           | -736                                                                                           | -1,327                                                                                         | 46                                                                                             |
| Average Profit- per-Trade | 210                                                                                            | 3                                                                                              | -405                                                                                           | -375                                                                                           | 22                                                                                             | -87                                                                                            | -352                                                                                           |

You'll note that if a similar table were presented to represent the results of counter-trend-following on FX pairs, the numbers would be exactly the same, but with the leading sign reversed: A positive $100 would be a shown as negative $100 for that year.

The dollar-based pairs are strongly suited to trend-following, while the pound, Canadian dollar, and Swiss franc are strongly suited to countertrend-following  trading  (the  negative  results  in  the  table  would  be  reversed to positive if the logic was a counter-trend entry instead of a trendfollowing  entry).  Something  that  begs  to  be  looked  at  is  combinations of trend-following currencies with other trend-following currencies, and counter-trend-following  currencies  with  other  counter-trend-following currencies. Based on the information in Table 3.5, these are the pairs in each group:

- ■ Trend-following pairs: dollar and Australian dollar, and dollar and euro currency.
- ■ Counter-trend-following pairs: pound and Canadian dollar, pound and yen, pound and Swiss franc, Canadian dollar and yen, and Canadian dollar and Swiss franc.

Table 3.6 shows the annual performance:

## Trading FX Pairs with the Same Trend Tendencies: Results Shown in

TABLE 3.6 Average Dollar Profit-per-Monthly-Transaction

| Year                | Trend-Following Pairs with Trend-Following Strategy   | Counter-Trend-Following Pairs with Counter-Trend- Following Strategy   |
|---------------------|-------------------------------------------------------|------------------------------------------------------------------------|
| 2000                | 838                                                   | -1,424                                                                 |
| 2001                | -1,360                                                | 1,647                                                                  |
| 2002                | -402                                                  | 388                                                                    |
| 2003                | 2,022                                                 | 2,905                                                                  |
| 2004                | 445                                                   | 202                                                                    |
| 2005                | -415                                                  | -472                                                                   |
| 2006                | -370                                                  | 142                                                                    |
| 2007                | 1,062                                                 | -161                                                                   |
| 2008                | 4,780                                                 | 612                                                                    |
| 2009                | -430                                                  | 1,846                                                                  |
| 2010                | -1,380                                                | 1,926                                                                  |
| 2011                | -1,280                                                | 314                                                                    |
| Average Profit-per- |                                                       |                                                                        |
| Trade               | $675                                                  | $629                                                                   |

Table 3.6 clearly shows the benefit of trading each instrument with its trading tendency. Further breaking out the numbers, there were 84 winning months of trades and 69 losing months of trades for the trend-following pairs, for a total profit of $103,421. For the counter-trend-following pairs, there were 192 winning months of trades, 166 losing months, and a total profit of $225,376. Additionally,  Table 3.6 shows that a losing year for one set of instruments is usually a winning year for the other. In other words, when markets are choppy and trends don't persist, the counter-trend instruments tend to do well, and when the markets are too 'trendy' for the counter-trend instruments, the trend-following ones do well.  There's only one year (2005) where both sets of instruments had a losing year.

Before  we  leave  the  FX  pairs  tendency  analysis,  let's  look  at  the pairs  that  have  one  strong  trend-following  member  and  one  strong counter-trend-following member. (The Australian dollar only averaged $3 per transaction and the euro only $22 for the trend-following strategy, so they are not strongly trend-following or strongly counter-trend and  will  be  left  out.) Those  pairs  are:  dollar  and  pound,  dollar  and Canadian dollar, dollar and yen, and dollar and Swiss franc. The results are shown in Table 3.7.

<!-- image -->

Trading Pairs with the Different Trend-Following Tendencies with a Trend-Following Strategy: Results Shown in Average Dollar Profitper-Monthly-Transaction

| Year                     | Profit   |
|--------------------------|----------|
| 2000                     | 478      |
| 2001                     | 432      |
| 2002                     | -273     |
| 2003                     | 698      |
| 2004                     | -167     |
| 2005                     | -48      |
| 2006                     | -905     |
| 2007                     | 1,204    |
| 2008                     | 130      |
| 2009                     | -1,131   |
| 2010                     | -786     |
| Average                  | -950     |
| Average Profit-per-Trade | -$12     |

Using daily bars, when you mate a strong trend-following tendency currency with a strong counter-trend-following tendency currency, the result is a stalemate:  The resultant instrument doesn't consistently trend or consistently move in a counter-trend-following manner.

## Summary of Daily-Bar Tendencies

To summarize what's been presented so far in this chapter, I believe stocks are primarily counter-trend-following tendency instruments on daily data; commodities are primarily trend-following instruments on daily data; and overall,  FX  pairs  are  primarily  counter-trend-following  tendency  instruments, but with FX, there are pairs with weak to strong trend-following tendencies.

## ■ Markets Are Different: Intra-Day Bars

I recommend some form of 'tendency analysis' be conducted on every instrument you wish to trade in the time frame you wish to trade it. If you want to trade five-minute bars,  it  pays  to  know  whether  the  instrument tends to trend or not. T o  illustrate,  we'll  use  hourly  bar  data  for  stocks, commodities, and the FX pairs. For stocks we'll use the 100 stocks in the Nasdaq 100 from 2000 through the end of 2010. For commodities, we'll use all the electronically traded U.S. commodities from 2000 through the end of 2010. And for the 21 FX pairs, we'll use hourly data from 2002 through the end of 2010.

## Trading Stocks on Intra-Day Bars

The trend-following criteria for stocks will be to go long on the next bar on all hours following a close one standard deviation above the 10-bar average of the hourly closes. Exit will be done on the close of the next day.  Table 3.8 shows the results.

Again, the stock database had an upward bias as the buy-and-hold average daily return of 0.07 percent per day per stock shows. But the buy-and-hold return was almost doubled using the trend-following approach on the hourly data.  This is in clear contrast to the daily-bar analysis  on  stocks,  which  rewarded  a  counter-trend-following  approach. This shows that instruments that have a trending tendency on one time frame don't necessarily have the same trending tendency in other time frames.

<!-- image -->

Trading Stocks with Trend-Following and Counter-Trend-Following Strategies, One-Day Return: Results Shown in Average Percent Profitper-Transaction

| Year    |   Baseline: Buy Each Open and Sell at Close |   Buying Stocks with a Close One Standard Deviation above the 10-Hour Average, Sell at Next Close |
|---------|---------------------------------------------|---------------------------------------------------------------------------------------------------|
| 2000    |                                        0.07 |                                                                                              0.40 |
| 2001    |                                        0.10 |                                                                                              0.25 |
| 2002    |                                       -0.05 |                                                                                              0.18 |
| 2003    |                                        0.26 |                                                                                              0.30 |
| 2004    |                                        0.13 |                                                                                              0.14 |
| 2005    |                                        0.04 |                                                                                              0.08 |
| 2006    |                                        0.04 |                                                                                              0.01 |
| 2007    |                                        0.05 |                                                                                              0.10 |
| 2008    |                                       -0.17 |                                                                                             -0.12 |
| 2009    |                                        0.23 |                                                                                              0.10 |
| 2010    |                                        0.09 |                                                                                             -0.05 |
| Average |                                        0.07 |                                                                                              0.12 |

## Trading Commodities on Intra-Day Bars

For commodities, 25 highly liquid electronic-contract commodities were used for the analysis. Buy and hold was determined by buying each day at the close and closing out the trade at next day's close. The commodities were also traded with a trend-following approach: If the close was one standard deviation or more above the average of the last 10 hourly closes, the commodity was bought; if the close was one standard deviation or less below the average of the last 10 hourly closes, the commodity was sold. The trades were closed out on the close of the next day. Table 3.9 shows the results.

Again the commodities show a sharp upward bias, as evidenced by the buy-and-hold average profit-per-day, per-commodity of $21.26. The trendfollowing approach exceeded buy-and-hold by over 40 percent, $30.05 per trade  versus  $21.26  for  buy-and-hold.  In  the  case  of  commodities,  both daily bars and hourly bars have a tendency to trend.

<!-- image -->

## Trading Commodities with Trend-Following Strategy, One-Day Return: Results Shown in Average Percent Profit-per-Transaction.

| Year    |   Baseline: Buy Each Open and Sell at Close |   Buying Commodities with a Close One Standard Deviation above the 10-Day Average, Sell Commodities with a Close One Standard Deviation below the 10-Day Average, Exit at Close |
|---------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2000    |                                       44.64 |                                                                                                                                                                           95.06 |
| 2001    |                                        1.14 |                                                                                                                                                                           10.54 |
| 2002    |                                       28.14 |                                                                                                                                                                            7.25 |
| 2003    |                                       64.41 |                                                                                                                                                                          -23.05 |
| 2004    |                                       25.03 |                                                                                                                                                                          -71.14 |
| 2005    |                                        7.60 |                                                                                                                                                                           -4.66 |
| 2006    |                                       58.26 |                                                                                                                                                                           96.78 |
| 2007    |                                       44.02 |                                                                                                                                                                           29.34 |
| 2008    |                                      -80.68 |                                                                                                                                                                           47.78 |
| 2009    |                                       58.36 |                                                                                                                                                                           56.87 |
| 2010    |                                       29.46 |                                                                                                                                                                           50.55 |
| Average |                                       21.26 |                                                                                                                                                                           30.05 |

## Trading FX Pairs on Intra-Day Bars

The FX analysis on hourly bars was conducted in the same manner as that for the commodities. The results are shown in  Table 3.10.

TABLE 3.10

## Trading FX Pairs with Trend-Following Strategy, One-Day Return: Results Shown in Dollar Profit-per-Transaction

| Year    |   Baseline: Buy on Open Each Day, Sell at Close |   Buying FX Pairs with a Close One Standard Deviation above the 10-Day Average, Selling FX Pairs with a Close One Standard Deviation below the 10-Day Average |
|---------|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2002    |                                            5.25 |                                                                                                                                                       -100.85 |
| 2003    |                                            4.96 |                                                                                                                                                         66.00 |
| 2004    |                                            5.45 |                                                                                                                                                        37.423 |
| 2005    |                                           -2.70 |                                                                                                                                                        -21.02 |
| 2006    |                                           33.31 |                                                                                                                                                         50.95 |
| 2007    |                                           -2.13 |                                                                                                                                                         -1.21 |
| 2008    |                                          -74.33 |                                                                                                                                                         30.55 |
| 2009    |                                            5.59 |                                                                                                                                                         24.00 |
| 2010    |                                          -35.39 |                                                                                                                                                        -79.75 |
| Average |                                          -11.64 |                                                                                                                                                          9.17 |

The FX pairs had a tendency to fall over this time frame as the baseline loss of $11.64 per pair per day shows. The trend-following approach beats the baseline by over $20 a trade, a $9.17 per-trade profit for the trend-following approach versus an $11.64 per-trade loss for the baseline. As was the case with stocks, the tendency of FX pairs differs on daily-bar data and hourly data.

## ■ Why the Difference in Trending Tendencies between Classes of Instruments?

I hope this chapter's analysis has convinced you that classes of instruments have different trending tendencies. An obvious question is:  Why? In the case of daily-bar stocks, I believe they are primarily counter-trend instruments because they are emotionally driven rather than value driven.  The emotions of fear and greed cause a herd reaction to movement. When stocks are rallying sharply, greed causes investors to jump in so they don't miss the move. As more and more jump in, the valuations increase beyond fair value until inevitably there are no more buyers and prices head down. At that point, fear sets in. Profits quickly turn to losses, and the investor sells at any cost to just get out. When there are no more sellers, valuations are below fair value and an up-cycle starts. Though I can't prove those statements, I offer the following evidence:

When you buy stock you are given a piece of paper, the stock certificate, not a hard asset like a gold bar or bushel of grain, which forms the basis of value for commodities. As the dot-com bubble proved, nobody really knows what a company is worth. Accounting games put out the story the company wants to tell, which clouds transparency. Without a clear marker of worth, traders/investors are at a loss to knowing whether a stock is a good buy or not.

Through the stock market bubble and subsequent crash, from 1997 to 2003, the stock market as measured by the S&amp;P 500 futures contract had a daily range exceeding 1 percent of closing price 83.6 percent of the time. During the same time frame, our basket of 56 commodities (less the stock index futures) had a daily range exceeding 1 percent of price or more only 53.6 percent of the time. The commodity currencies had a daily range of 1 percent of price or more only 26 percent of the days during the same time frame. I can think of no fundamental reason why any stock market should move 1 percent of its value four out of every five days. I conclude that it must be trader emotions moving the market up and down.

## ■ Conclusion

Different asset classes trade differently, and within the same asset class, trading characteristics can differ by time frame. It pays to perform a little analysis on what you want to trade, and in the time frame you want to trade it, before you start development. This chapter has illustrated an easy process you can use to find out the path of least resistance, which will give you a head-start in the development process.

## Trading System Elements: Entries

T he development of a trading strategy is an iterative process, but the start  of  the  process  is  always  the  entry  idea.  If  you  are  trading  an asset  class,  or  even  a  single  instrument  like  a  stock  index,  you  need  to have some idea how that class or instrument trades, and then test your ideas on how to enter the market at the appropriate time. The entry idea might be as simple as 'I'll trend-follow by going long after two up closes, or short after two down closes,' or as complex as 'I'll wait until I have a one-third retracement in the third wave of an Elliott wave cycle and incrementally buy in a position at any further Fibonacci retracement level.' For many, the entry idea comes from the study of charts; recurring up or down moves seem to happen after a certain chart setup. Some entry ideas are stimulated by the technical analysis literature. For others, like me, test ideas just pop up when I'm grocery shopping or mowing the lawn. However you do it, if you find a good entry idea, the rest of the development process is pretty straightforward.

This chapter is the first of three that will detail the process of building  a  strategy.  Chapter  5  explores  trade  exits,  and  Chapter  6  looks  at trading filters that are used, primarily in conjunction with the entry, to screen  in  good  trading  setups  or  screen  out  bad  setups. Through  these three chapters, we will build a stock and commodity strategy to illustrate the process.  There will be other examples where warranted. As the system is built, a simple money management metric will be computed from the equity  curve  that  shows  the  worth  of  the  latest  development  step. The process illustrated in these three chapters is how I develop systems.  You'll go through the process many times before you find something truly tradeable.  But  even  in  the  failures  you'll  learn  something  about  the  market you're trying to trade. Many times it's the failure that causes the breakthrough. If some step makes things much worse, doing the reverse might just be the right thing to do.

Because of its topic's importance, this chapter will start with a process that allows a developer to determine how good his entry idea is. I call it determining the entry power of a setup. Using the methodology, we'll quantify a number of popular entry techniques.

## ■ Entry: The Most Important System Element

Many will disagree with the statement that the entry is the most important system element. If they're trend-followers, they say anyone can spot a trend and jump onboard, but it's when you get out that makes the difference. Sure, when you get out is important, but the entry determines how soon and how quickly you accrue profit on a trade. If you've got a good entry, you can get out randomly and make a profit, on average, but you can't exit randomly and make a profit without a good entry, no matter how good your exit is. The entry is your edge, just like the house's edge in Vegas. On average, it makes your trade immediately profitable; the rest of the system just determines when the edge has run out and it's time to exit.

Good entries have a power and persistence that are proportional to the number of bars used for the setup logic. Bars are information. One tells you little, but the more you have the better idea you should have of what's next. If your entry uses 10 bars of information, it will have a forecasting power that builds profits to a certain level before succeeding bars either continue the direction, or not. If your entry uses 20 bars of information, your profit push should be higher and last longer than the 10-bar entry. Similarly, with 50 bars of information, you get a bigger profit push and longer persistence. Figure 4.1 illustrates the thought.

Does that mean more bars make a better signal? No. Your 10-bar entry might generate enough trades in the time the 50-bar signal generated one to be a better trading solution. It does mean that you can compare entry signals on a common basis: the number of bars used to determine the entry. Just take all the trades issued by each entry and accumulate the profit/loss on succeeding days.

FIGURE  4.1 Push and Persistence Is Proportional to Number of Bars

<!-- image -->

The following two entry examples illustrate entry power for the commodity class of tradeables:

- Trend-Following Entry 1: Buy when the close of the bar is above the n-day moving average. Exit the long position and go short when the close of the bar is below the n-day moving average.
- Trend-Following  Entry  2:  Buy  when  the  shorter-length  n-day  moving average closes above the longer n1-day moving average. Sell when the shorter-length n-day moving average closes below the n1-day moving average.

The trend-following Entry 1 rules summarize the first basic system that just about every trend-follower tests. It is a complete, standalone system because the exit of the first signal is the entry for the second. It is  always in the market and needs no other rules. The trend-following Entry 2 rules are a more sophisticated trend-following strategy using moving  averages.  In  the  first  strategy,  there  are  always  a  number  of whipsaw entries caused when no true trend is unfolding in the marketplace. The second entry system attempts to eliminate a number of these whipsaws by having both averages confirm the trend. Using our entry power methodology, Figures   4.2 and   4.3 summarize the entry power of the two entries.

FIGURE  4.2 Entry Power for Trend-Following Entry 1 on 56 Commodities

<!-- image -->

Figure   4.2 shows that the 10-day moving average is an in ineff  ective entry. The profi  ts from the day of entry out to 150 days later hug the $0 profi  t line. A 20-day average reaches a maximum profi  t point of about $50 per trade. The 40-day average almost reaches $80 of profi  t per trade, and the 80-day average hits about $110 per trade after about 90 days.

There is an interesting anomaly on the graphs: For each line, the entry  doesn't  finally  become  profitable  until  a  number  of  days  after  the entry. The  10-day  entry  doesn't  go  positive  until  20  days  after  entry; the 20-day entry doesn't go, and stay, positive until 10 days after entry; the  40-day  entry  doesn't  go  positive  until  7  days  after  entry;  and  the 80-day entry doesn't go, and stay, positive until 9 days after entry. If I was going to use one of these entries, I'd try to take advantage of this information. I'd look at delaying entry until the appropriate profitable day based on the historic averages, or look at entering at a better price with a limit order some measure away from the entry price of the open following the close.

This anomaly points out what you are likely to see with a number of common entries: Profi  t doesn't start to accrue until some number of days after the signal.  What I believe is happening in those cases is that the popularity of the entry causes an abnormal number of traders to enter on those signals. Even though the entry may ultimately be valid, there might not be enough liquidity to support the abnormal number of entries and price staggers back under the load. Eventually the market liquidity catches up with the demand, and some days later the position moves into profi  t. If you're using a popular entry, it pays to look at ways to take advantage of the price pullback.

Figure   4.3 shows the entry power of the dual moving average system.

FIGURE  4.3 Entry Power for Trend-Following Entry 2 on 56 Commodities

<!-- image -->

Figure   4.3 shows that the 5-day and 10-day two-average entry system is not worth trading, as the profi  t stays near $0 for the entire 150-day postentry period. The 10-day and 20-day two-average entry system has a profi  t peak of about $125. The 20-day and 40-day two-average entry system has a profi  t peak of about $175, and the 40-day and 80-day two-average entry system has a profi  t peak of about $400. Clearly this entry is more eff  ective than the single moving average system in Entry 1. There is one caveat, however: The single moving average system had many more entries than the second system (about 1.5 times as many).

## ■ Comparison of Common Trend-Following Entry Techniques on Daily-Bar Commodity Data

The graphs in this section use 10, 20, 40, and 80 bars of information with popular entry techniques on our basket of 56 commodities.

## Relative Strength Index (RSI)

This indicator was introduced by J.  Welles  Wilder Jr. in his classic book, New Concepts in  T echnical  T rading Systems. The algorithm determines the ratio of up closes to down closes over a specifi  ed number of bars.  The output is normalized to a value between 0 and 100.  When used as trend-following methods, values higher than 50 are bullish, while values lower than 50 are bearish. In this analysis, the trend-following buy signal was a value of 53 or higher, and the trend-following sell signal was an RSI value of 47 or lower. Figure   4.4 shows the results.

FIGURE  4.4 Entry Power for RSI

<!-- image -->

There are good separation and persistence for all the entries in Figure   4.4  . It looks like they all have an intermediate peak near 40 days after entry .  Though the graph is intended to visually present the power of the entry, it also shows the spot where you hit diminishing returns. After 40 bars, I' d look to tighten up the stop considerably expecting a profi  t pullback.

## Stochastic

This indicator is attributed to George Lane. Like the RSI indicator, the stochastic number is normalized to values between 0 and 100. The number shows the location of the current close relative to the high/low range of the number of bars used in the analysis.  The stochastic number can be smoothed by averaging the last three values. Figure   4.5 shows the smoothed values. For this analysis, the trend-following buy signal occurs when the stochastic value is close above 51 or greater, and the sell signal occurs when the stochastic value penetrates below 49.

FIGURE  4.5 Entry Power for Stochastic

<!-- image -->

The lines in Figure   4.5 are more jagged than those in the RSI profi  t run-up. I've never found a good use for stochastics, though in fairness to the algorithm, it is generally used as a two-value indicator: slow and fast stochastic.

## Rate of Change (ROC)

Rate of change (ROC) is an indicator that measures the velocity of price change. Typically, today's closing price is divided by the closing price some number of bars ago and then multiplied by 100 to yield the measurement. When the value is above 100, velocity is up; below 100, and velocity is down. Figure   4.6 shows the power of this entry signal when long trades are taken at an ROC of 102 or greater and short trades are taken at 98 or below.

There  is  good  separation  on  the  lines  in  Figure    4.6  until  about 50 days, when things start to become muddled. The intermediate peaks though 50 days are less than the corresponding ones on the RSI chart (Figure   4.4  ).

FIGURE  4.6 Entry Power for ROC

<!-- image -->

## Standard Deviation Breakouts

Breakout entries are those where price penetrates an upper or lower bound. One such boundary is some number of standard deviations away from the average price over some number of bars. Usually, the standard deviation is computed across the closing prices of the bars. Figure   4.7 uses 10, 20, 40, and 80 daily bars, and computes the breakout point as two standard deviation measures away from the average.

FIGURE  4.7 Entry Power for Standard Deviation Breakouts

<!-- image -->

Like the RSI graphs in Figure   4.4  , the lines in Figure   4.7 have the properties you want to see: clear separation and more power in the longer-term entries. A diff  erence between this set of lines and those in the RSI graphs is the defi  nite turn-down in profi  t some number of days after entry in the standard deviation graphs.

## Donchian Entry

The  Donchian  entry  was  advocated  by  Richard  Donchian  in  the  1960s for stock trading. Later, it was the baseline entry for Richard Dennis and William Eckhardt's Turtle system. It is a breakout system with the upper penetration point being the highest high, or close, of the last n bars. The lower penetration point is the lowest low , or close, of the last n bars.  This is a very popular entry because of its notoriety and the fact that it works well in almost all time frames. Because of its popularity, almost every entry will have huge entry volume and corresponding slippage, or price pullback, for a few days. For our entry, we'll go long when price closes above the n-bar Donchian high and short when price closes below the n-day Donchian low where n is the number of bars used to determine the Donchian highs and lows. Figure   4.8 shows Donchian entry power performance.

The set of lines in Figure   4.8 corresponds very closely to the standard deviation graph of Figure   4.7  . It is my experience that those are the best two well-known entries.

FIGURE  4.8 Entry Power for the Donchian Entry

<!-- image -->

## Summary of Trend-Following Entry Power for Commodities

Using the entry power results on the handful of trend-following entry techniques presented here is a good starting point for system development. If you're interested in a comprehensive set of entries to test for yourself, I highly  recommend The  Ultimate Trading  Advantage by  John  Hill,  George Pruitt, and Lundy Hill. John and George run 'Futures Truth,' which rates the real-time performance of developer-submitted trading systems.  They've seen it all.

Though each entry uses the same number of bars, the graphs are not strictly  an  apples-to-apples comparison because the number of entry signals created by each technique varies.  Tables 4.1 through 4.4 show the peak profit point, and the number of entries each entry generated over the 10-, 20-, 40-, and 80-bar periods, respectively. The third column is formed by multiplying the peak profit point by the number of entries. That number represents the total profit that would be available across all the entries if they were held to the number of days corresponding to the peak profit point.  The last  two  columns show an alternate metric; the maximum profit-per-day is found by dividing each point on the graphs by the number of days since entry. It is a measure of the velocity of profit accumulation.

| TABLE 4.1           | Comparison of Commodity Entry Techniques: 10 Daily Bars of Data   | Comparison of Commodity Entry Techniques: 10 Daily Bars of Data   | Comparison of Commodity Entry Techniques: 10 Daily Bars of Data   | Comparison of Commodity Entry Techniques: 10 Daily Bars of Data   | Comparison of Commodity Entry Techniques: 10 Daily Bars of Data   |
|---------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Entry Technique     | Highest Average $ Profit Point                                    | Number of Entries                                                 | Total $ the Entry Generates                                       | Maximum Profit-per-Day                                            | Number of Days since Entry for Max Profit                         |
| Moving Average      | 13.97                                                             | 65,532                                                            | 915,636                                                           | 0.18                                                              | 20                                                                |
| Dual Moving Average | 26.38                                                             | 41,239                                                            | 1,088,046                                                         | 0.30                                                              | 41                                                                |
| RSI                 | 154.44                                                            | 43,284                                                            | 6,684,917                                                         | 1.77                                                              | 82                                                                |
| Stochastic          | 63.49                                                             | 36,374                                                            | 2,309,317                                                         | 1.54                                                              | 19                                                                |
| Rate of Change      | 271.73                                                            | 33,124                                                            | 9,000,828                                                         | 2.88                                                              | 13                                                                |
| Standard Deviation  | 241.26                                                            | 19,840                                                            | 4,786,757                                                         | 4.30                                                              | 20                                                                |
| Donchian            | 373.88                                                            | 42,538                                                            | 15,904,280                                                        | 6.33                                                              | 19                                                                |

Using 10 bars of information, the Donchian entry is far and away the best. It's highest average profit point ranks first; its number of entries is third; and the total number of dollars the entry generates at that point is almost double the next-nearest entry. Additionally, the maximum profit generated per day is  about  50  percent  higher  than  the  next-closest  technique,  the  standard deviation entry.

| TABLE 4.2           | Comparison of Commodity Entry Techniques: 20 Daily Bars of Data   | Comparison of Commodity Entry Techniques: 20 Daily Bars of Data   | Comparison of Commodity Entry Techniques: 20 Daily Bars of Data   | Comparison of Commodity Entry Techniques: 20 Daily Bars of Data   | Comparison of Commodity Entry Techniques: 20 Daily Bars of Data   |
|---------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Entry Technique     | Highest Average $ Profit Point                                    | Number of Entries                                                 | Total $ the Entry Generates                                       | Maximum Profit-per-Day                                            | Number of Days                                                    |
| Moving Average      | 48.85                                                             | 43,237                                                            | 2,112,438                                                         | 1.53                                                              | 20                                                                |
| Dual Moving Average | 127.48                                                            | 20,062                                                            | 2,557,473                                                         | 6.52                                                              | 12                                                                |
| RSI                 | 300.87                                                            | 31,155                                                            | 9,373,667                                                         | 6.57                                                              | 15                                                                |
| Stochastic          | 113.12                                                            | 24,131                                                            | 2,729,890                                                         | 4.08                                                              | 12                                                                |
| Rate of Change      | 266.23                                                            | 28,087                                                            | 7,477,637                                                         | 5.48                                                              | 15                                                                |
| Standard Deviation  | 554.89                                                            | 21,795                                                            | 12,093,802                                                        | 10.73                                                             | 15                                                                |
| Donchian            | 559.47                                                            | 31,353                                                            | 17,541,213                                                        | 8.96                                                              | 15                                                                |

Using 20 bars of information, the Donchian and standard deviation entries are the best. They are almost identical in the highest dollar point. And while the Donchian entry generates more total dollars, the standard deviation entry has a higher maximum profit-per-day.

| TABLE 4.3           | Comparison of Commodity Entry Techniques: 40 Daily Bars of Data   | Comparison of Commodity Entry Techniques: 40 Daily Bars of Data   | Comparison of Commodity Entry Techniques: 40 Daily Bars of Data   | Comparison of Commodity Entry Techniques: 40 Daily Bars of Data   | Comparison of Commodity Entry Techniques: 40 Daily Bars of Data   |
|---------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Entry Technique     | Highest Average $ Profit Point                                    | Number of Entries                                                 | Total $ the Entry Generates                                       | Maximum Profit-per-Day                                            | Number of Days                                                    |
| Moving Average      | 79.09                                                             | 29,108                                                            | 2,302,212                                                         | 2.24                                                              | 14                                                                |
| Dual Moving Average | 182.40                                                            | 10,015                                                            | 1,826,697                                                         | 3.63                                                              | 11                                                                |
| RSI                 | 566.05                                                            | 21,080                                                            | 11,932,386                                                        | 7.65                                                              | 13                                                                |
| Stochastic          | 165.24                                                            | 16,418                                                            | 2,712,996                                                         | 4.32                                                              | 12                                                                |
| Rate of Change      | 394.66                                                            | 21,492                                                            | 8,482,083                                                         | 7.29                                                              | 12                                                                |
| Standard Deviation  | 717.96                                                            | 18,071                                                            | 12,974,274                                                        | 15.60                                                             | 16                                                                |
| Donchian            | 766.99                                                            | 22,699                                                            | 17,409,918                                                        | 12.37                                                             | 16                                                                |

Using 40 bars, the Donchian and standard deviation entries are again the best, but the RSI entry is just behind them.

| TABLE 4.4          | Comparison of Commodity Entry Techniques: 80 Daily Bars of Data   | Comparison of Commodity Entry Techniques: 80 Daily Bars of Data   | Comparison of Commodity Entry Techniques: 80 Daily Bars of Data   | Comparison of Commodity Entry Techniques: 80 Daily Bars of Data   | Comparison of Commodity Entry Techniques: 80 Daily Bars of Data   |
|--------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Entry Technique    | Highest Average $ Profit Point                                    | Number of Entries                                                 | Total $ the Entry Generates                                       | Maximum Profit-per-Day                                            | Number of Days                                                    |
| Moving Average     | 110.55                                                            | 20,111                                                            | 2,223,364                                                         | 1.71                                                              | 41                                                                |
| Dual Moving        | 402.18                                                            | 5,019                                                             | 2,018,565                                                         | 8.13                                                              | 19                                                                |
| RSI                | 858.48                                                            | 13,533                                                            | 11,617,857                                                        | 14.98                                                             | 20                                                                |
| Stochastic         | 194.63                                                            | 11,151                                                            | 2,170,272                                                         | 3.62                                                              | 13                                                                |
| Rate of Change     | 392.19                                                            | 15,699                                                            | 6,157,026                                                         | 7.91                                                              | 20                                                                |
| Standard           | 888.23                                                            | 13,178                                                            | 11,705,133                                                        | 20.01                                                             | 16                                                                |
| Deviation Donchian | 973.30                                                            | 16,184                                                            | 15,751,880                                                        | 18.31                                                             | 16                                                                |

Lastly, with 80 bars, the Donchian, standard deviation, and RSI entries look to be first, second, and third.

The bottom line is that these entries are tested, and used, by many, many traders. A signal in a popular entry technique will lead to a flood of orders, which increases slippage. If you can find something that competes in performance with the Donchian, standard deviation, or RSI entries in any time frame, you have a trading nugget. Build a tradeable system around it, and you've got something you can use for years.

Next we'll look at entries on daily-bar stock market data.

## ■ Comparison of Common Counter-Trend Entry Techniques on Daily-Bar Stock Data

In this section, we'll look at the same entry techniques we explored for commodities,  but  with  two  differences.  First,  we'll  only  look  to  trade stocks from the long side, and second, since stocks act in a counter-trend manner on daily bars, we will buy when the entry technique shows weakness. Though we'll only look to trade from the long side, we'll watch for shorting opportunities by remembering that if the long trades show a big loss, doing the reverse and shorting those signals will lead to a profit on the short trade. We will use 10, 20, 40, and 80 daily bars, as we did with the commodity trend-following  entries.  Instead  of  the  dollars-per-contract metric we used for commodities, this section will use a metric of percent profi  t-per-trade. In the last chapter, we saw that due to survivorship bias our  basket  of  1,716  stocks  has  a  slight  up  bias.  For  our  entry  analysis, we'll remove the bias in each trade by taking out the small average upward movement each day.

## Counter-Trend-Following Stock Entry with a Single Moving Average

The counter-trend entry with a single moving average is to buy when the close crosses below the moving average. Figure   4.9 shows the average percent gained across all trades from the entry day until 150 days later.

FIGURE  4.9 Entry Power for the Single Moving Average

<!-- image -->

Figure   4.9 shows that stocks behave much diff  erently than commodities. With the commodities, performance generally adhered to the rule that the more bars of information, the better the performance in terms of strength of return and persistence of the profi  t growth. This stock graph shows the diffi culty  of  trading  stocks  in  the  longer  term. The  highest  profi  t  on  the chart is at about 0.4 percent and 95 days. Since there are about 250 trading days a year, there are a bit more than two and a half 95-day cycles. A profi  t of 0.4 percent every 95 days annualizes to about 1 percent-defi  nitely not worth trading. Maybe this is just a poor setup for stocks. Let's look at the dual moving average system.

## Counter-Trend-Following Stock Entry with Two Moving Averages

The counter-trend entry with a two moving average is to buy when the shorter-length moving average crosses below the longer-term moving average. Figure   4.10 shows the average percent gained across all trades from the entry day until 150 days later.

FIGURE  4.10 Entry Power for Two Moving Averages

<!-- image -->

There is defi  nitely better separation with the dual moving average system. The most interesting points look to be 1.06 percent profi  t point that the 20/40 day entry has after 50 days of trading, and the 0.49 percent profi  t that the 40/80 day solution has at 33 days. Still, annualizing those returns only yields 5.3 percent for the 20/40 solution and 3.7 percent for the 40/80 entry.

## Counter-Trend-Following Stock Entry with RSI

The counter-trend entry with RSI is to buy when the RSI value falls below a threshold. For this analysis the threshold was 47. Figure   4.11 shows the average percent gained across all trades from the entry day until 150 days later.

Figure   4.11 shows the 80-day entry heading up to a gain of 0.19 percent at three days and then straight down to a loss of 1.06 percent at 41 days.

FIGURE  4.11 Entry Power for RSI

<!-- image -->

Assuming you entered short on day four, that would yield a short trade gain of 1.25 in 37 days, or an annualized yield of 8.4 percent-not tradeable on its own, but anytime you fi  nd something that makes money on the short side in stocks it's worth taking note.  Those types of trades can be used as a hedge to your long-side-only trading.

The only other thing of note in Figure   4.11 is the 0.19 percent gain on the long side for the 80-day entry. That annualizes to 16.7 percent, but of course slippage and commission will take their toll on such a small gain.

## Counter-Trend-Following Stock Entry with Stochastics

The  counter-trend  entry  with  stochastics  is  to  buy  when  the  three-day smoothed stochastic value crosses below a certain threshold. The threshold used in this analysis was 49. Figure   4.12 shows the average percent gained across all trades from the entry day until 150 days later.

Figure   4.12 looks more like the commodity graphs we saw in the previous section than the stock graphs we've seen so far. In particular, they separate after time and the longer term signals don't fall well below the zero line. But a diff  erence from the commodity charts is that the best longer-term results aren't the longer-term signals; they are the short-term signals. In any event, the peaks occur too far after the signal to yield anything that might annualize to a decent return.

FIGURE  4.12 Entry Power for Stochastics

<!-- image -->

## Counter-Trend-Following Stock Entry with Rate of Change

The counter-trend entry using rate of change is to buy when the rate of change value crosses below a certain threshold. The threshold value used in this analysis was 100. Figure   4.13 shows the average percent gained across all trades from the entry day until 150 days later.

There appears to be nothing of interest in Figure   4.13  .

FIGURE  4.13 Entry Power for Rate of Change

<!-- image -->

## Counter-Trend-Following Stock Entry with a Standard Deviation

The  counter-trend  entry  with  standard  deviation  is  to  buy  when  the  close crosses below the average minus two standard deviations of price. Figure   4.14 shows the average percent gained across all trades from the entry day until 150 days later.

FIGURE  4.14 Entry Power for Standard Deviation Entry

<!-- image -->

As we saw with the RSI 80-day entry signals in Figure   4.11  , the 80-day entry with standard deviation leads to short trades  that  accrue  more than 1 percent of profi  t many days after the signal, but they are not tradeable on  their  own.  On  the  long  side,  the  10-day  entry  hits  0.35  percent  of profi  t after nine days.  That annualizes to about 9.7 percent a trade-still not exciting.

## Counter-Trend-Following Stock Entry with a Donchian Entry

The counter-trend entry using the Donchian technique is to buy when the close crosses below the low close of the last n bars. Figure   4.15 shows the average percent gained across all trades from the entry day until 150 days later.

FIGURE  4.15 Entry Power for the Donchian Entry

<!-- image -->

Finally  there's  something  that  may  be  worthwhile.  Within  the  fi  rst 10 days after  entry  all  four  signals  jump  to  a  profi  t,  then  pull  back. The following is a breakout by signal of the most interesting points and their annualized return:

## ■ 10-day signal:

- ■ 0.29 percent profi  t after fi  ve days is a 14.5 percent annualized return.
- ■ 0.34 percent profi  t after six days is a 14.2 percent annualized return.
- ■ 0.37 percent profi  t after nine days is a 10.3 percent annualized return.

## ■ 20-day signal:

- ■ 0.27 percent profi  t after six days is an 11.2 percent annualized return.
- ■ 40-day signal:
- ■ 0.24 percent profi  t after fi  ve days is a 12.0 percent annualized return.

## ■ 80-day signal:

- ■ 0.28 percent profi  t after three days is a 23.3 percent annualized return.
- ■ 0.39 percent profi  t after fi  ve days is a 19.5 percent annualized return.

From this breakout, it appears that the 10-day and 80-day are the best candidates.

## Counter-Trend-Following Stock-Entry Note

Obviously the preceding analysis was not exhaustive. With an entry candidate, more work should be done before system development starts with that entry. For instance, the RSI, ROC, stochastic, and standard deviation entries are made at levels below normal; these would be varied. And because of the value of finding even moderately performing short signals, more work should be done on those entries that could potentially yield them. Lastly, remember that the graphs had a positive survivorship bias that was removed. In the later years that bias was much less because the stock basket is much closer to the 100 percent real basket that traded at the time. I'd go back and check performance for the last few years for interesting signals without the bias removal to see how good the signal really is.

## Counter-Trend-Following Stock Entry Observations

There are clear differences between the commodity and stock graphs:

- ■ The commodity graphs have a clear separation of the n-day length lines and they vary right from the start, where the stock 10-, 20-, and 40-day lines have very little spread. The 80-day stock lines head straight down from the start.
- ■ The commodity graphs have a relatively higher average profit-per-trade as the number of bars increases from 10 to 80. The stock graphs generally have their worst average percent profit using 80 days of data. In most cases the best results use 10 bars.

## ■ Conclusion

In this chapter we explored the entry power of well-known entry setups. The methodology was to use a large basket of a tradeable and generate entry signals using the setup with a spectrum of look-back bars of information. After the entry signal, the profit was accrued across all signals out to some number of days and the results graphed. From the graphs, significant peak points can be seen and the annualized return computed.  Thus entry power is represented graphically, and by annualized return.

For  commodities,  the  RSI,  standard  deviation,  and  Donchian  entries looked most interesting. For stocks, the Donchian entry was far and away the best. But a cautionary note: The analysis was not exhaustive, only illustrative. If you have an entry idea, this is the type of analysis you should do to find out if it's worthwhile and in what time frames it works best. In the next two chapters we will build a commodity and stock system on the Donchian entry.

## Trading System Elements: Exits

T he optimum time to exit a trade is at the peak profit point of the trade. Finding that point is easier said than done, and I've never seen anybody actually try to build a measure of whether today's the peak profit day or not. In reality, most developers exit trades in one of four ways: through a reversal signal, through a stop loss, through a time-based exit, or through a profit stop. Examples of each will be shown in this chapter using a stock strategy and a commodity strategy.

For this analysis, we'll use the stocks that comprised the Nasdaq 100 at the end of 2011 with daily-bar data going back to 2000, if they traded that long. On the commodity side, we'll use a basket of 56 commodities with data from 1980 to the end of 2011. Back-adjusted stock and commodity contacts will be used, and, unless otherwise noted, transaction costs (slippage and commission) will not be included.

The baseline entry signal for both stocks and commodities will be the Donchian entry described in Chapter 4. In keeping with the trending tendencies of the two classes of trading instruments, we will use a countertrend Donchian entry for stocks and a trend-following Donchian entry for commodities. For stocks, we'll initiate a $5,000 position at each long or short signal, and for commodities we'll buy or sell one contract.

## ■ Reversal Exit Signals (Stock Example)

A reversal signal exit occurs in an always-in-the-market system like the moving average system we tested in Chapter 4. The exit for the current position is also the entry for the reverse position. Sometimes starting the system development process with an entry idea and using a reversal system to find  the  best  parameter  set  for  the  long  and  short  entry,  while alternately reversing from long to short and back to long again, leads to a good strategy.

The trending tendency analysis in Chapter 4 indicated that a countertrend Donchian entry is a good candidate for a stock trading system entry. The entry/exit rules for the stock reversal system are:

- Exit the short position and go long on the next open when there is a close below the n -day look-back lowest close.
- Exit the long position and go short on the next open when there is a close above the n -day look-back highest close.

Using the 100-stock basket, the look-back period for the entry was varied from 10 to 80 days, in steps of 10, to get a feel for where the best trading point might lie. Both long and short trades were taken. Table 5.1 shows the results for each look-back length.

TABLE 5.1 Stock Trade Stats by Look-back in Days

|   Look-Back in Days |   Winning Trades |   Losing Trades |   Total Profit ($) |   Profit-per-Trade ($) |
|---------------------|------------------|-----------------|--------------------|------------------------|
|                  10 |           11,603 |           6,410 |            245,422 |                     13 |
|                  20 |            5,806 |           3,232 |             95,625 |                     10 |
|                  30 |            3,832 |           2,126 |            -67,307 |                    -12 |

By the time a 30-day look-back was hit, it was evident that the only way to trade this entry was short-term, so longer look-backs weren't tested. This  behavior  matches  my  development  experience:  It's  hard to  find  good  longer-term  trading  solutions  for  stocks  using  technical analysis.

Here's a further breakout of the run with a 10-day look-back:

Long winning trades:

6,248

Long losing trades:

2,779

Long total profit:

$629,586

Long profit-per-trade:

$69

Short winning trades:

5,355

Short losing trades:

3,631

Short total profit:

-$384,147

Short profit-per-trade:

-$43

It's  obvious  that  the  short  side  is  what's  holding  this  strategy  back. On average, every short trade is a $43 loser. Some may wonder how the  short  side  can  have  a  winning  percentage  of  60  percent  and  lose money. This  is  a  good  example  of  how  counter-trend  trading  usually works. You're  trying  to  buy  when  oversold,  and  cover  and  reverse  to short  when  overbought. The  range  between  oversold  and  overbought depends on how many days of data your setup uses. We're using 10 days, so the distance between oversold and overbought is relatively small.  That means small profits when you're right. But a stock can stay oversold all the way down to zero, or remain overbought all the way to the moon. That means large losses when you're wrong. In this case, the short-side average winner was $258 while the average loser was $498.  The fact that the short side performs so poorly again lines up with my development experience: It's very hard to find stock strategies that perform well on the short side.

Based on the results, let's make the strategy a long-only strategy. We'll still use the Donchian entry point for the short side, but instead of using it to close the long and enter short, the logic will be to just close out the long  trade  and  wait  for  a  new  long  setup. We  know  that  the  long-only strategy makes $69 per trade using the 10-day entry. Is 10 days the best short-term entry? Table 5.2 shows summary data when the look-back period  is  varied  from  20  days  down  to  two  days  in  two-day  increments. This table introduces a gain-to-pain metric that we'll use from here on out. The metric is a ratio formed by dividing the average annual return (the gain) by the average annual max draw-down (the pain you have to experience to get your gain). The average annual max draw-down figure is found by finding the x largest draw-downs over the trading period and averaging the results.  The x value is the number of years spanning the trading period. In our case, the time period is 2000 through the end of 2011. That's 12 years. The total profit is divided by 12 to form the numerator of  the  ratio,  and  the  12  largest  draw-downs  are  found  and  averaged  to form the denominator, even if more than one of the largest draw-downs occurred in the same year.

TABLE 5.2

## Long-Only Stock Trade Stats by Look-Back in Days

|   Look-Back in Days |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Max Draw-Down ($) |   Max Draw-Down ($) |   Gain-to-Pain Ratio |
|---------------------|---------------------------------|-----------------------------|------------------------------------|---------------------|----------------------|
|                  20 |                             119 |                      49,240 |                             70,436 |             182,652 |                 0.70 |
|                  18 |                             108 |                      49,390 |                             69,243 |             190,157 |                 0.71 |
|                  16 |                              97 |                      49,713 |                             71,821 |             188,504 |                 0.69 |
|                  14 |                              83 |                      48,330 |                             69,024 |             194,907 |                 0.70 |
|                  12 |                              72 |                      48,481 |                             68,617 |             199,515 |                 0.71 |
|                  10 |                              69 |                      57,099 |                             66,316 |             199,714 |                 0.86 |
|                   8 |                              62 |                      63,953 |                             69,288 |             188,764 |                 0.92 |
|                   6 |                              48 |                      65,219 |                             69,664 |             184,404 |                 0.94 |
|                   4 |                              34 |                      66,779 |                             67,491 |             148,018 |                 0.99 |
|                   2 |                              24 |                      79,553 |                             64,319 |             102,895 |                 1.24 |

In general, as the look-back is decreased from 20 days down to two, these are the trends:

- ■ Profit-per-trade decreases.
- ■ Annual return increases.
- ■ Average max draw-down decreases.
- ■ Max draw-down decreases.
- ■ Gain-to-pain increases.

Those are all good tendencies, except for the profit-per-trade trend. If using a look-back of two looks like the solution we should pick, you might have fallen into the trap this sort of analysis can set.

The problems are the average profit-per-trade and the realities of transaction costs: The average profit-per-trade is so low that transaction costs will substantially eat into them. If you use a low commission broker like Interactive Brokers, your round-turn commission for the average $5,000 position will probably be about $4, so your $24 a trade is down to $20 right off the bat. The market orders that are filled on the open for both entry and exit add to that toll. I believe the slippage you'll get on those orders will average about $0.015 per share. If the average price of a share across all entries and exits is $20, the 3 cents of slippage for the market orders is 0.15 percent. The $20 per trade we're making on each $5,000 position is 0.40 percent a trade. Subtracting the slippage percent from 0.40 percent, we wind up making 0.25 percent per trade, which is $12.50 per trade on our $5,000 positions after transaction costs. Our $24 per trade number has been halved.

My selection from  Table 5.2 would be the 8-day look-back. Even with the $4 commission and $0.03 of slippage for the two market orders, the $62 per trade is only reduced to about $50.50 per trade.  That's more than 1 percent of our $5,000 bet-size.  We should net about that number in real trading.

## ■ Exit Stops (Stock Example)

An exit stop can be a catastrophic stop, or a trailing stop. I've found that a trailing stop is usually only effective on longer-term systems as a way to signal that the trend is definitely over. I do use a catastrophic stop in almost all the commodity systems I've traded. It is the 'uncle' point of the trade. For intra-day commodity or FX systems, it might be $500 away from the entry point. For longer-term systems, it might be thousands of dollars away from the entry. If that point is hit, admit that the entry was bad, exit, and wait for a new setup.

Using the eight-bar look-back Donchian entry, long-only strategy as a baseline, let's look at a range of catastrophic stop levels.  The stop is triggered when closing price brings the position to a loss greater than the dollar stop level selected. If the close is below the stop price, exit is done on the next open. Table 5.3 shows results for a range of catastrophic dollar-stop levels.

TABLE 5.3 Long-Only Stock Trade Results versus Catastrophic Stop Level, Next Day Exit

| Catastrophic Dollar-Stop Value   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to-Pain Ratio |
|----------------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|----------------------|
| None*                            |                              62 |                      63,953 |                         69,288 |              188,764 |                 0.92 |
| $3,000                           |                              61 |                      63,243 |                         69,070 |              187,978 |                 0.92 |
| $2,500                           |                              60 |                      62,027 |                         70,061 |              187,633 |                 0.89 |
| $2,000                           |                              59 |                      60,375 |                         67,423 |              187,189 |                 0.90 |
| $1,500                           |                              58 |                      59,707 |                         64,775 |              182,585 |                 0.92 |
| $1,000                           |                              54 |                      55,748 |                         58,924 |              169,126 |                 0.95 |
| $750                             |                              51 |                      52,263 |                         54,627 |              144,297 |                 0.96 |
| $500                             |                              45 |                      46,276 |                         46,464 |              119,152 |                 1.00 |

* Baseline

The stop triggered on the close for execution on the open did improve results for stop levels of $1,000 and below , but the cost of implementing one of those stops is a fairly large drop-off in profit-per-trade. Of note is the fact that a $3,000 stop changed the statistics of the trading solution from the baseline, meaning that some trades hit that stop trigger.  Y ou need about 50 of the $62 winners to recapture a $3,000 loss.  Again this shows the tendency of counter-trend trading: Losses can be quite large. Let's look at exiting on the close instead of the next open if the stop is triggered on the close.  T able 5.4 shows the results.

TABLE 5.4 Long-Only Stock Trade Results versus Catastrophic Stop Level, Exit on Close

| Catastrophic Dollar-Stop Value   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to-Pain Ratio |
|----------------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|----------------------|
| None*                            |                              62 |                      63,953 |                         69,288 |              188,764 |                 0.92 |
| $3,000                           |                              61 |                      63,231 |                         70,184 |              188,022 |                 0.90 |
| $2,500                           |                              60 |                      61,894 |                         69,748 |              187,610 |                 0.89 |
| $2,000                           |                              59 |                      60,286 |                         67,426 |              187,255 |                 0.89 |
| $1,500                           |                              57 |                      59,157 |                         64,913 |              183,493 |                 0.91 |
| $1,000                           |                              53 |                      54,957 |                         59,182 |              167,747 |                 0.93 |
| $750                             |                              50 |                      51,764 |                         54,404 |              142,423 |                 0.95 |
| $500                             |                              43 |                      44,503 |                         46,612 |              120,626 |                 0.95 |

* Baseline

Again, the catastrophic stop triggered on the close and exited on the close only  helps  the  trading  solution  for  stop  levels  of  $1,000  and  below  and, again, at a significant penalty in profit-per-trade from the baseline. It's not surprising that the exit on the following open somewhat outperforms the exit on the close of the day that the stop is hit. When a stop is triggered, it has to have been a down day for that stock. As stocks trade in a countertrend manner, you'd expect a bounce on the next open.

Lastly, let's look at exiting with the catastrophic stop intra-day. Table 5.5 shows the results.

TABLE 5.5 Long-Only Stock Trade Results versus Catastrophic Stop Level, Exit Intra-Day

|                                | Intra-Day                     | Intra-Day                 | Intra-Day                    | Intra-Day          | Intra-Day          |
|--------------------------------|-------------------------------|---------------------------|------------------------------|--------------------|--------------------|
| Catastrophic Dollar-Stop Value | Average Profit- per-Trade ($) | Average Annual Return ($) | Average Annual Draw-Down ($) | Max Draw- Down ($) | Gain-to-Pain Ratio |
| None*                          | 62                            | 63,953                    | 69,288                       | 188,764            | 0.92               |
| $3,000                         | 60                            | 62,149                    | 70,814                       | 190,977            | 0.88               |
| $2,500                         | 59                            | 60,989                    | 68,066                       | 186,422            | 0.90               |
| $2,000                         | 58                            | 59,475                    | 64,866                       | 186,367            | 0.92               |
| $1,500                         | 55                            | 57,143                    | 63,539                       | 184,880            | 0.90               |
| $1,000                         | 51                            | 52,283                    | 56,591                       | 153,767            | 0.92               |
| $750                           | 46                            | 47,209                    | 49,064                       | 137,194            | 0.96               |
| $500                           | 37                            | 38,556                    | 44,939                       | 99,243             | 0.86               |

* Baseline

In this case, the gain-to-pain metric does exceed the baseline value for stop values of $1,500, $1,000, and $750. But in comparing the three of uses of the catastrophic stop, it's clear that the exit on the next open is the best way to go.

I went through all three versions of the catastrophic stop for a reason. I think these tables illustrate the following points:

- ■ A stop loss doesn't increase your profit-per-trade. Many think that a stop eliminates a large portion of the loss of the big losers and that should lead to an overall greater profit. They do cap the loss on the big losers, but a lot of trades that would have been winners or small losers will hit the stop, get taken out of play, and then any rebound from the stop point won't be seen. The net result isn't an increase in profit-per-trade. In fact, usually profit-per-trade goes down. Don't think this means that I don't advocate stops. When they help improve the trading solution I use them. In fact, I've never traded a futures strategy without some sort of stop. On the other hand, I've never traded a stock strategy with a catastrophic stop. Now, if a stock strategy risked all the account equity on each trade like some do when trading exchange-traded  funds  (ETFs)  like  the  Powershares QQQ (QQQ), then some sort of catastrophic stop would probably  be  warranted.  But  when  you're  trading  a  basket  of  stocks  with  a short-term scalping strategy such as this one, the risk to the portfolio from each trade is just not that great. Still, it always pays to look at them early in the development.
- ■ A stop loss doesn't increase your total profit. Hand-in-hand with the profit-pertrade conclusion is the fact that it is rare that a catastrophic stop increases overall strategy profitability. Again, this doesn't mean they shouldn't be used. If the tradeoff between decreasing risk and decreasing profitability is worth it, the stop should be used.
- ■ A catastrophic stop is a risk-avoidance measure. As you look at the three tables (5.3-5.5) you'll  see  that  the  average  max  draw-down  and  max  drawdown numbers decrease with smaller and smaller catastrophic stops.  This is the purpose of stops: risk control.
- ■ An in-the-market stop is not necessarily the best form of risk control. I rarely use in-the-market stops-not because I'm against them, but because the results of my development analysis show that the best risk/ reward solution usually lies with a stop executed at either the close or the next open.  This doesn't even take into account the argument about 'stop hunting,' which many traders consider a huge problem with in-the-market stops.  Those traders believe strong hands move the

market to pick off resting stops for their own purposes. I don't know if that's true or not, but I do know that if you have a resting stop in the overnight session of a commodity market, strange things can happen.

Regarding trailing stops, I made some runs on this strategy using variations  of  trailing  stops  and  didn't  find  anything  that  improved  the  trading solution. Later in this chapter, we'll be developing a commodity strategy. Trailing stops will be detailed then. For now , let's leave our baseline stock strategy without a catastrophic stop.

## ■ Time-Based Exits (Stock Example)

A time-of-day stop can be used by a day trader to exit at or near the market close, by an intermediate-term trader who doesn't want to hold over the weekend, or by a trader who thinks his setup has had enough time to work and wants to put the money to work on another trade. The last case is very interesting because the power of the entry graphs in Chapter 4 show us that an x -bar entry setup starts to lose steam at a certain point.  That would be an excellent time to exit the trade if it's survived to that point.

Let's take our baseline Donchian stock strategy and look at exiting a trade after a certain number of days. Runs were made exiting on the close of the x th day and at the open after the x th day.  The open exit on the following day was slightly better.  Table 5.6 reflects that exit.

TABLE 5.6 Exit after x T rading Days

| Exit on Next Open after x Days x Value   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to-Pain Ratio |
|------------------------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|----------------------|
| None*                                    |                              62 |                      63,953 |                         69,288 |              188,764 |                 0.92 |
| 20                                       |                              60 |                      65,598 |                         68,719 |              186,823 |                 0.95 |
| 15                                       |                              54 |                      62,736 |                         68,058 |              179,481 |                 0.92 |
| 10                                       |                              49 |                      62,155 |                         68,199 |              169,470 |                 0.91 |
| 8**                                      |                              47 |                      65,676 |                         61,596 |              137,433 |                 1.07 |
| 6                                        |                              41 |                      60,289 |                         62,186 |              161,139 |                 0.97 |
| 4                                        |                              34 |                      55,372 |                         55,918 |              124,762 |                 0.99 |

* Baseline

** New baseline

The eight-day exit looks the best from the gain-to-pain ratio perspective. Its average annual return is larger than its average max draw-down and the max draw-down over $50,000 less than the baseline, but it comes at a cost of giving up $15 a trade from the baseline. I think the draw-down improvements are worth the loss of profit-per-trade, so that exit will become the new baseline.

## ■ Profit Stops (Stock Example)

The profit stop is an exit strategy that is always worth looking at. It violates the rule to let your profits run, but it gets you out of the trade at an equity high to that point. In that regard, it eliminates open trade equity retracement, which is a form of draw-down. Even if the average profit-per-trade is reduced by using a profit target, it may still be worthwhile to incorporate one because of reduced draw-down. Table 5.7 shows the results of incorporating a profit stop into the baseline. The profit stop is triggered if the dollar level is exceeded intra-day so a sell limit order is used for the exit. It is placed at the entry in points plus the stop value in dollars divided by $5,000.

TABLE 5.7 Profit Targets Results on Stock Strategy

| Profit Stop Value   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to-Pain Ratio |
|---------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|----------------------|
| None*               |                              47 |                      65,676 |                         61,596 |              137,433 |                 1.07 |
| $1,000              |                              47 |                      64,241 |                         57,507 |              133,303 |                 1.12 |
| $800                |                              48 |                      65,451 |                         56,080 |              125,095 |                 1.17 |
| $600                |                              48 |                      65,752 |                         54,808 |              114,273 |                 1.20 |
| $400                |                              49 |                      68,190 |                         51,339 |              106,628 |                 1.33 |
| $300**              |                              50 |                      70,877 |                         50,693 |               92,510 |                 1.40 |
| $200                |                              46 |                      68,207 |                         46,817 |               81,262 |                 1.46 |
| $100                |                              39 |                      64,714 |                         38,916 |               74,525 |                 1.66 |

* Baseline

** New Baseline

As you can see, the profit stop really improves the strategy without any tradeoffs; the profit-per-trade actually goes up until a profit target of $300 is hit. If you're wondering how total profit can go up, it's because of increased trading opportunities.  When we exit with a profit target, we are exiting before eight trading days have elapsed (the time stop in the last section). This gives opportunities for new trades in that symbol, which obviously occur.

Profit  targets  are  effective  exits  with  scalping  strategies  like  this  for  a couple of reasons. First, you're buying oversold and looking to exit at overbought, but the distance between oversold and oversold isn't that great.  The profit target allows you to get any kind of bounce with the exit limit order.

Additionally, when you're scalping, slippage is also a major issue. Any stop or market order that you can replace with a limit order will reduce slippage.

There are other forms of profi  t-taking, as we will see next when we start the development of our commodity system. Before we start the commodity strategy, Figure   5.1 shows an equity curve of the stock system to this point.

FIGURE  5.1 Equity Curve of Stock Strategy

<!-- image -->

We've all seen better-looking equity curves, but there's really only one disaster point, and that's the bloodbath in 2008. But even then, the strategy managed to eke out a profi  t for the year.

Table   5.8 shows a breakout of return and draw-down by year.

|   Year |   Yearly Profit ($) |   Annual Max Draw-Down ($) |
|--------|---------------------|----------------------------|
|   2000 |              45,107 |                     37,404 |
|   2001 |              63,310 |                     86,213 |
|   2002 |              31,798 |                     57,830 |
|   2003 |             129,933 |                     18,715 |
|   2004 |              61,593 |                     24,871 |
|   2005 |              37,968 |                     17,558 |
|   2006 |              64,461 |                     24,155 |
|   2007 |              49,914 |                     22,007 |
|   2008 |              16,144 |                     92,510 |
|   2009 |             147,870 |                     32,435 |
|   2010 |              59,441 |                     31,037 |
|   2011 |              49,806 |                     79,048 |

A nice stat here is that there are no losing years. If you traded this strategy with $500,000, you'd average about 14 percent return-per-year, experience about 10 percent max draw-down each year, and have a max draw-down of about 19 percent once in the 12-year period. Not quite our trading objectives, but we're getting there.

## ■ Reversal Exit Signals (Commodity Example)

We've selected a trend-following Donchian entry as our baseline entry for the commodity system. The following are the trend-following entry rules:

- Long entry: If flat or short, and trading exceeds the highest close of the previous x days, then exit the short position and go long. Entry is on a stop order.
- Short entry: If flat or long, and trading goes below the lowest close of the previous x days, then exit the long position and go short. Entry is on a stop order.

Table 5.9 shows the results of reversal trading using a number of lookback periods. Again, we're using a 56-commodity basket with data from 1980 until the end of 2011, and no transaction costs have been included.

| TABLE 5.9         | Reversal Trading Commodities with Various Donchian Look-Backs   | Reversal Trading Commodities with Various Donchian Look-Backs   | Reversal Trading Commodities with Various Donchian Look-Backs   | Reversal Trading Commodities with Various Donchian Look-Backs   | Reversal Trading Commodities with Various Donchian Look-Backs   |
|-------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|
| Look-Back in Days | Average Profit- per-Trade ($)                                   | Average Annual Return ($)                                       | Average Annual Draw-Down ($)                                    | Max Draw- Down ($)                                              | Gain-to- Pain Ratio                                             |
| 10                | 149                                                             | 135,933                                                         | 137,314                                                         | 440,869                                                         | 0.99                                                            |
| 20*               | 387                                                             | 169,384                                                         | 150,574                                                         | 455,456                                                         | 1.12                                                            |
| 30                | 525                                                             | 150,091                                                         | 150,410                                                         | 511,032                                                         | 1.00                                                            |
| 40                | 676                                                             | 141,309                                                         | 138,431                                                         | 431,614                                                         | 1.02                                                            |
| 50                | 826                                                             | 136,619                                                         | 148,487                                                         | 438,396                                                         | 0.92                                                            |

* Baseline

The following trends continued for look-backs greater than 50, but total profit and gain-to-pain continued to fall off, so they're not shown.

- ■ Profit-per-trade increasing.
- ■ Average annual return decreasing.
- ■ Average max draw-down increasing.
- ■ Max draw-down increasing.
- ■ Gain-to-pain ratio decreasing.

A look-back of 20 days will form our entry baseline for the commodity strategy. Other pertinent information from that run was:

| Long wining trades: 2,716           | Short wining trades: 2,451           |
|-------------------------------------|--------------------------------------|
| Long losing trades: 3,982           | Short losing trades: 4,218           |
| Long total profit: $3,719,788       | Short total profit: $1,463,458       |
| Long average profit per trade: $555 | Short average profit per trade: $219 |

These statistics are pretty representative of mid- to longer-term trendfollowing strategies:

- ■ Winning percentage of trades is  less  than  50  percent.  In  this  case  it's about 39 percent.
- ■ Profit-per-trade increases with the number of bars used for the setup.
- ■ Long-side trades have much better statistics than short-side trades.
- ■ Profit-per-trade is so large that transaction costs will cause only a small performance drop-off.

What the statistics  don't  show  is  the  biggest  wart  of  trend-following: open-equity give-back. Trend-followers cut losses and let the profits run. The problem is figuring out when the run is over. I had a trend-following palladium trade in 1999 that grew to an open equity profit of over $30,000 a  contract.  I  got  only  about  $20,000  out  of  the  trade.  I  gave  back  about $10,000 of open equity profit. Anything you can do in your development to keep as much of the peak equity of the move is a good thing to do for two reasons: First, you'll realize more profit, but second, and more importantly, you'll reduce draw-down due to the give-back.

Let's see if catastrophic stops, time-based stops, and profit-target stops can reign in the huge draw-downs and make this strategy tradeable.

## ■ Exit Stops (Commodity Example)

In this section we'll take a more detailed look at exit stops with the commodity  reversal  baseline.  In  addition  to  dollar-based  catastrophic  stops, some volatility-based stops will be examined.

## Catastrophic Stops

For  our  stock  example,  we  only  looked  at  a  catastrophic  stop  that  was dollar-based:  a  stop  some  number  of  dollars  away  from  the  entry. With scalping systems you can't get too fancy, because you're only playing with a  margin of a couple of hundred dollars. When you develop longer-term trend-following systems, it pays to thoroughly look at a number of different candidates. That's because some trades will net many thousands of dollars. Cutting a few of those off prematurely with a haphazard stop can make a big bottom-line performance difference. In this section we'll look at three different catastrophic stops.

The first catastrophic stop we'll test is a dollar stop; for long trades a fixed stop will be placed x dollars below the entry, and for short trades, it will be placed above the entry price.  When the stop level is penetrated on a close, exit will be done on the next open.  Table 5.10 shows the results.

TABLE 5.10 Catastrophic Dollar Stop on Commodity System

| Dollar Stop Amount ($)   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to-Pain Ratio |
|--------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|----------------------|
| None*                    |                             387 |                     169,384 |                        150,574 |              455,456 |                 1.12 |
| 1,000                    |                             319 |                     158,186 |                        146,784 |              452,520 |                 1.08 |
| 1,500                    |                             341 |                     159,267 |                        148,279 |              415,709 |                 1.07 |
| 2,000                    |                             359 |                     162,909 |                        147,398 |              445,036 |                 1.11 |
| 2,500                    |                             366 |                     163,807 |                        149,811 |              441,384 |                 1.09 |
| 3,000                    |                             370 |                     164,493 |                        145,589 |              466,114 |                 1.13 |
| 5,000                    |                             379 |                     166,694 |                        147,235 |              465,759 |                 1.13 |

* Baseline

Table  5.10  illustrates  the  major  challenge  in  developing  good  mid-  to longer-term trend-following strategies: It's difficult to control the risk (in terms of draw-down and individual trade risk). Even with a stop $5,000 away from the entry point, draw-down is not curtailed.  You just can't trade a  $10,000 to $20,000 account using stops that large. If the first trade is stopped out, your account will be down 25 to 50 percent. Moreover, the $5,000 stop is really only effective for the more volatile commodities. The following  is  a  breakout  by  commodity  group  showing  the  percentage  of the trades that hit the $5,000 stop.

Grains:

0

U.S. financials:

0

Meats:

0

Foreign financials:

&lt;1

Softs:

&lt;1

Foreign stock:

5.0

Metals:

1.8

U.S. stock:

&lt;1

Energies:

&lt;1

Currencies:

&lt;1

The breakout shows that only the metals and foreign stock indices are affected by the $5,000. For the rest of the groups, it really doesn't provide much protection.

The deficiencies of the dollar-based stop cause us to look at tailoring the stop to some measure of the recent volatility of the commodity .  This has two advantages. First, every commodity goes through periods ranging from near-dormant to near-ballistic; a stop should adjust to this difference. Second, some commodities  are  more volatile than others even when they are near-dormant and the other is near-ballistic, the DAX futures index and oats are examples. Why not have a catastrophic stop that adjusts to the current volatility of the commodity?

There are two commonly used volatility measures: average daily range, or true range, and the standard deviation of closing price over some period. Sometimes, the entry setup also provides a measure of the recent volatility. That is the case with the Donchian entry. The distance between the n -day look-back's high and low triggers really pinpoints the relative movement of the commodity over the last n days.  W e'll now look at all three.

Table 5.11 shows the reversal baseline, and the reversal baseline with a catastrophic  stop  variation  based  on  the  Donchian  entry. The  variation  is called midpoint, and it is the average of the long Donchian entry point and the short Donchian entry point on the day of trade entry.

| TABLE 5.11             | TABLE 5.11                    | Donchian Midpoint Catastrophic Stop on Commodities   | Donchian Midpoint Catastrophic Stop on Commodities   | Donchian Midpoint Catastrophic Stop on Commodities   | Donchian Midpoint Catastrophic Stop on Commodities   |
|------------------------|-------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
| Catastrophic Stop Type | Average Profit- per-Trade ($) | Average Annual Return ($)                            | Average Annual Draw-Down ($)                         | Max Draw- Down ($)                                   | Gain-to-Pain Ratio                                   |
| None*                  | 387                           | 169,384                                              | 150,574                                              | 455,456                                              | 1.12                                                 |
| Midpoint               | 315                           | 158,666                                              | 157,305                                              | 521,900                                              | 1.01                                                 |

* Baseline

The midpoint stop is too tight. It chokes off a lot of profitable trades early, resulting in a $70 drop-off in profit-per-trade, and it doesn't help the draw-down situation.

TABLE 5.12 Standard Deviation Catastrophic Stop on Commodities

| Number of Multiples of the 20-Day Standard Deviation   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to- Pain Ratio |
|--------------------------------------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|-----------------------|
| None*                                                  |                             387 |                     169,384 |                        150,574 |              455,456 |                  1.12 |
| 1                                                      |                             271 |                     156,305 |                        148,665 |              467,125 |                  1.05 |
| 2                                                      |                             335 |                     159,638 |                        148,821 |              484,715 |                  1.07 |
| 3                                                      |                             378 |                     167,553 |                        147,173 |              474,203 |                  1.14 |
| 4                                                      |                             387 |                     169,535 |                        149,713 |              455,456 |                  1.13 |

* Baseline

Table 5.12 shows results when a standard deviation catastrophic stop is used. Since the Donchian entry points are found over the last 20 bars, we'll use the last 20 closes to compute the standard deviation.

Table 5.12 shows that with a stop placed three standard deviations away from our entry, the gain-to-pain ratio is increased to 1.14 from the baseline of 1.12. Let's see if the average range stop can improve on that.

Table 5.13 shows results when an average range catastrophic stop is used. The  average  range  is  found  over  the  20  days  immediately  preceding  the signal. Again, the Donchian entry points are found from those same bars of information.

TABLE 5.13 Average Range Catastrophic Stop

| Number of Multiples of the 20-Day Average Range for Catastrophic Stop   |   Average Profit-per- Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to- Pain Ratio |
|-------------------------------------------------------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|-----------------------|
| None*                                                                   |                             387 |                     169,384 |                        150,574 |              455,456 |                  1.12 |
| 1                                                                       |                             255 |                     147,835 |                        150,939 |              470,649 |                  0.98 |
| 2                                                                       |                             322 |                     156,642 |                        151,509 |              453,018 |                  1.03 |
| 3                                                                       |                             358 |                     164,545 |                        150,680 |              445,154 |                  1.09 |
| 4                                                                       |                             370 |                     166,975 |                        151,974 |              460,784 |                  1.10 |
| 5                                                                       |                             379 |                     169,470 |                        151,231 |              464,934 |                  1.12 |
| 6                                                                       |                             380 |                     169,563 |                        150,999 |              469,309 |                  1.12 |

* Baseline

The best the average range stop could do was tie the baseline gain-to-pain ratio of 1.12.

The best catastrophic stop was the three-standard-deviation stop. It seems like that might be very large when converted to dollars, so another run was made to find the average dollar value of the stop. It was $1,910. That's still large, especially for smaller accounts, but for now let's keep it as the new baseline  and  move forward in the development. We can come back to it later, if needed.

## Trailing Stops

The trick to a good trailing stop on a mid- to longer-term trend-following strategy is to ratchet up the acceleration of the stop as the trade starts to go parabolic. Figure 5.2 shows the thought.

FIGURE  5.2 Ideal  Trailing Stop

<!-- image -->

Fixed moving averages don't react fast enough as the trade starts to accelerate in profi  t so your open equity give-back is large. In this section we'll look at three sets of logic that try to mimic the ideal trailing stop. The fi  rst has been around in the open literature since 1978.

J.  W elles  Wilder Jr., in his groundbreaking book, New Concepts in  T echnical Trading  Systems, introduced  a  number  of  innovative  concepts  like  relative strength  index  (RSI)  and  average  directional  movement  index  (ADX). Often overlooked is his Parabolic Time/Price System. Though he used it as a reversal system, I think it's best used as a trailing stop. If a long trade is initiated, an initial stop is placed, and every day thereafter that stop moves up at an ever-increasing rate, whether the position is advancing in profi  t or not. The ever-increasing rate is a function of the acceleration factor. In Wilder's book, an acceleration factor of 0.02 was used, and that number was increased by 0.02 every time the trade had a profi  table day. But the number really depends on the type of trading you're doing.  With short-term systems the factor will be relatively large, and as the holding period goes longer, the acceleration factor needs to decrease.

The acceleration factor is used to tighten the stop by adding an ever-increasing increment to the existing stop. The increment is computed by multiplying the existing acceleration factor by the diff  erence of the existing stop and the high-water point of the trade. An example will clear things up. Suppose you go long and your initial stop is three standard deviations below your entry price (as we're doing with our catastrophic commodity stop). If your entry price is 100 and your initial stop is 85, the trade might start to play out as in  T able   5.14  .

TABLE 5.14

Parabolic Stop Example

As profit accrues, you can see the stop tightens at an ever-increasing rate. Table 5.15 shows results with the parabolic stop applied over our baseline for a variety of acceleration values.

|   Days After Close |   Entry |   High Water Mark |   Profit |   Stop Factor |   Acceleration |
|--------------------|---------|-------------------|----------|---------------|----------------|
|                  0 |     100 |               100 |        0 |         85.00 |           0.02 |
|                  1 |     102 |               102 |        2 |         85.34 |           0.04 |
|                  2 |     101 |               102 |        1 |         86.01 |           0.04 |
|                  3 |     105 |               105 |        5 |         86.77 |           0.06 |

TABLE 5.15 Parabolic Trailing Stop on Commodities

| Acceleration Factor   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to-Pain Ratio |
|-----------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|----------------------|
| None*                 |                             378 |                     167,553 |                        147,173 |              474,203 |                 1.14 |
| 0.02                  |                             227 |                     132,452 |                        154,229 |              474,115 |                 0.86 |
| 0.01                  |                             271 |                     144,487 |                        147,698 |              449,898 |                 0.98 |
| 0.05                  |                             308 |                     151,603 |                        148,257 |              480,639 |                 1.02 |
| 0.002                 |                             354 |                     164,100 |                        149,982 |              468,108 |                 1.09 |
| 0.00175               |                             361 |                     166,740 |                        148,238 |              469,931 |                 1.12 |
| 0.00150               |                             371 |                     170,325 |                        158,456 |              468,223 |                 1.07 |

* Baseline

The published acceleration factor of 0.02 is much too fast for this strategy. It  cuts  off  over  $150 of profit-per-trade and doesn't help the draw-down stats. Let's try a different trailing stop strategy.

A trailing stop I developed, and used in one of my commercially sold trading systems, accelerated the stop by going to shorter-length moving average trailing stops at certain profit increments.  You want to start with a  moving  average  that's  far  enough  away  from  the  entry  price  so  you don't prematurely take out a trade and then, when appreciable profit accrues, move to a shorter-length moving average.  The appreciable profit can  be  any  metric,  but  I  used  standard  deviation.  Since  we're  using 20 bars of data for entry, I'll use the standard deviation of the closes on the day of entry as the target. When there is a close above entry price plus the standard deviation level, the trailing stop moves to a shorterlength moving average.

Table 5.16 shows the results for a number of moving average combinations. I didn't exhaustively test, but just wanted to demonstrate that trailing stops can be effective.

TABLE 5.16 Trailing Stop Based on Moving Averages

| Moving Average Lengths   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to- Pain Ratio |
|--------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|-----------------------|
| None*                    |                             378 |                     167,553 |                        147,173 |              474,203 |                  1.14 |
| 40/35/30/25/20           |                             317 |                     158,158 |                        152,682 |              396,945 |                  1.04 |
| 45/40/35/30/25           |                             330 |                     164,180 |                        152,642 |              392,218 |                  1.08 |
| 50/45/40/35/30           |                             331 |                     165,338 |                        180,787 |              387,336 |                  1.10 |
| 60/50/40/30/20           |                             312 |                     162,045 |                        142,253 |              379,952 |                  1.14 |
| 80/70/60/50/40           |                             321 |                     171,296 |                        148,723 |              371,356 |                  1.15 |

* Baseline

These results show that this approach to an accelerating stop can improve results. Though the gain-to-pain is only marginally improved to 1.15 in the bottom-row case, the max draw-down is significantly reduced in every case. Let's not take the bottom row as the new baseline. It gives up a lot of profitper-trade for the draw-down reduction.  We can come back and incorporate it if the rest of the development doesn't solve the draw-down problem.

## ■ Time-Based Exits (Commodity Example)

In our stock system development this chapter, we saw a big improvement in baseline performance when we capped the trade length at eight days. Let's see if the same exit logic will work for the commodity system. Table 5.17 shows results when we exit a position after a certain holding period in days.

TABLE 5.17 Time-Based Exit in Commodities

| Exit on Close after x Days: x Value   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to-Pain Ratio |
|---------------------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|----------------------|
| None*                                 |                             378 |                     167,553 |                        147,173 |              474,203 |                 1.14 |
| 30                                    |                             272 |                     156,543 |                        157,424 |              480,732 |                 0.99 |
| 40                                    |                             308 |                     162,459 |                        145,085 |              451,963 |                 1.12 |
| 50                                    |                             340 |                     169,530 |                        153,469 |              482,254 |                 1.10 |
| 60                                    |                             350 |                     168,619 |                        148,425 |              466,228 |                 1.14 |
| 70                                    |                             363 |                     172,015 |                        161,613 |              472,137 |                 1.06 |
| 80                                    |                             371 |                     173,386 |                        150,178 |              470,228 |                 1.15 |

* Baseline

There is a marginal increase in gain-to-pain when the number of days for exit is 80, but that solution hardly impacts the draw-down problem. This is pretty typical of mid- to longer-term trend-following.  There just isn't a time constraint on how long a trend will last. We need to find something that greatly curtails the risk side of this strategy, or it won't be tradeable.

## ■ Profit Stops (Commodity Example)

Maybe a profit target of some sort will cut back risk.  We know that a profittarget exit occurs at the peak profit point of the trade up to that point, so there won't be any open equity give-back on those trades. Maybe that will be enough to limit draw-down, especially the $470,000 max draw-down that makes this strategy a non-starter.

First we'll try a dollar-based profit stop. If there is a close that puts the trade in profit by x dollars, we'll exit the trade on the next open.  Table 5.18 shows the results when the dollar-based profit target is varied from $4,000 to $15,000.

TABLE 5.18 Dollar-Based Profit Stop on Commodities

| Dollar-Based Profit Target Amount ($)   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to-Pain Ratio |
|-----------------------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|----------------------|
| None*                                   |                             378 |                     167,553 |                        147,173 |              474,203 |                 1.14 |
| 4,000                                   |                             369 |                     169,363 |                        161,136 |              498,180 |                 1.05 |
| 6,000                                   |                             375 |                     170,820 |                        156,766 |              504,604 |                 1.09 |
| 8,000                                   |                             374 |                     170,395 |                        157,890 |              506,325 |                 1.08 |
| 10,000                                  |                             377 |                     171,334 |                        150,880 |              481,065 |                 1.14 |
| 15,000                                  |                             379 |                     172,238 |                        152,661 |              469,953 |                 1.13 |

* Baseline

The dollar-based profit target didn't help. In fact, the max draw-downs got worse.

Let's  try  a  volatility-based  profit  target. W e  saw  that  a  volatility-based catastrophic stop worked for the commodity system because the risk was tailored to the recent volatility of the commodity; maybe a volatility-based profit  stop  will  work as well. A volatility-based profit stop that I've used successfully in the past counts the number of standard deviation moves of profit a trade makes. When the count hits the exit number, exit is done on the next open. Since we're using 20 days of data for the Donchian entry, let's use the last 20 days' close to compute the standard deviation. When a long trade is signaled, the first target is the entry point plus the one standard deviation value on that day. If that value is surpassed, a second target is formed by adding the standard deviation value on the day the target is passed to the close for that day. After x targets are hit, the trade is exited. Note that we're adjusting the size of each target by the prevailing standard deviation on the day of the adjustment, not with the standard deviation value that existed on the day the trade was entered. Normally, as a successful trade progresses, the volatility increases as the trade approaches and then goes parabolic. The increased volatility is accounted for in our profi  t target adjustments.

Table   5.19 shows the results as the number of the count is varied.

TABLE 5.19

Profit Targets Based on Standard Deviation Counts

| Deviation Profit Target   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to- Pain Ratio |
|---------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|-----------------------|
| None*                     |                             378 |                     167,553 |                        147,173 |              474,203 |                  1.14 |
| 6                         |                             326 |                     167,127 |                        148,114 |              472,945 |                  1.13 |
| 7                         |                             346 |                     170,137 |                        155,089 |              468,454 |                  1.10 |
| 8                         |                             357 |                     170,890 |                        146,913 |              473,515 |                  1.16 |
| 9                         |                             368 |                     173,072 |                        149,169 |              470,345 |                  1.16 |
| 10                        |                             371 |                     172,556 |                        149,242 |              470,040 |                  1.16 |

* Baseline

Table   5.19 shows that we only get a marginal increase in the gain-to-pain metric with standard deviation counts of 8 through 10. And again, the max draw-down is not curtailed.

I tried a few more profi  t-stop mechanizations, but nothing took a signifi  cant bite out of draw-down. Maybe the fi  lters we test in the next chapter can do the trick.

Figure   5.3 shows the baseline strategy equity curve at this point.

<!-- image -->

FIGURE  5.3 Equity Curve for Commodity System

The equity curve looks pretty good until 2009, when things get ugly. Table 5.20 shows the yearly returns and draw-downs.

| TABLE 5.20   | Annual Return and Max Draw-Down for Commodity Strategy   | Annual Return and Max Draw-Down for Commodity Strategy   |
|--------------|----------------------------------------------------------|----------------------------------------------------------|
| Year         | Yearly Profit ($)                                        | Annual Max Draw-Down ($)                                 |
| 1980         | 150,845                                                  | 51,798                                                   |
| 1981         | 154,428                                                  | 48,019                                                   |
| 1982         | 84,492                                                   | 64,931                                                   |
| 1983         | 110,407                                                  | 28,269                                                   |
| 1984         | 84,499                                                   | 34,984                                                   |
| 1985         | 116,143                                                  | 44,293                                                   |
| 1986         | 102,198                                                  | 56,869                                                   |
| 1987         | 274,372                                                  | 50,386                                                   |
| 1988         | 139,532                                                  | 69,911                                                   |
| 1989         | 102,122                                                  | 53,132                                                   |
| 1990         | 186,828                                                  | 54,889                                                   |
| 1991         | 148,221                                                  | 56,342                                                   |
| 1992         | 95,537                                                   | 68,153                                                   |
| 1993         | 166,581                                                  | 36,303                                                   |
| 1994         | 59,648                                                   | 144,862                                                  |
| 1995         | 179,870                                                  | 49,397                                                   |
| 1996         | 44,510                                                   | 47,849                                                   |
| 1997         | 200,712                                                  | 59,072                                                   |
| 1998         | 86,020                                                   | 133,908                                                  |
| 1999         | 57,195                                                   | 148,686                                                  |
| 2000         | 33,229                                                   | 123,866                                                  |
| 2001         | 177,332                                                  | 76,769                                                   |
| 2002         | 59,923                                                   | 122,965                                                  |
| 2003         | 291,803                                                  | 66,924                                                   |
| 2004         | -32,488                                                  | 126,280                                                  |
| 2005         | 118,320                                                  | 83,433                                                   |
| 2006         | 137,292                                                  | 235,711                                                  |
| 2007         | 454,018                                                  | 157,243                                                  |
| 2008         | 1,388,602                                                | 225,404                                                  |
| 2009         | -6,302                                                   | 239,299                                                  |
| 2010         | 190,711                                                  | 245,347                                                  |
| 2011         | -139,022                                                 | 446,438                                                  |

The strategy only had three losing years, but they all occurred in the last eight years. The draw-downs were also pretty well contained in the past, averaging about $75,000 per year until 2006. From 2006 and on, the yearly max draw-down averaged about $275,000.

Table 5.21 shows profitability by commodity.

| TABLE 5.21 Commodity   |   Winning Trades |   Losing Trades |   Total Profit ($) |   Profit-per-Trade ($) |
|------------------------|------------------|-----------------|--------------------|------------------------|
| Corn                   |              108 |             178 |             36,100 |                    126 |
| Soybeans               |              111 |             164 |            119,312 |                    433 |
| Bean Meal              |              101 |             171 |             68,740 |                    252 |
| Bean Oil               |              109 |             181 |             46,134 |                    159 |
| Wheat                  |              111 |             184 |             53,000 |                    179 |
| KC Wheat               |              108 |             169 |             71,262 |                    179 |
| Rough Rice             |               81 |             113 |             88,299 |                    455 |
| Live Cattle            |               96 |             203 |             -5,451 |                    -19 |
| Lean Hogs              |              107 |             192 |             16,480 |                     55 |
| Feeder Cattle          |              106 |             189 |              6,975 |                     23 |
| Coffee                 |              115 |             173 |            169,181 |                    587 |
| Cotton                 |              115 |             173 |            103,815 |                    384 |
| Orange Juice           |              111 |             146 |             62,137 |                    228 |
| Lumber                 |              111 |             177 |             65,978 |                    229 |
| Cocoa                  |               92 |             192 |            -24,500 |                     -9 |
| Sugar                  |              111 |             146 |             71,187 |                    276 |
| Copper                 |              104 |             186 |            101,799 |                    351 |
| Palladium              |               96 |             186 |            152,265 |                    539 |
| Silver                 |              115 |             188 |            214,764 |                    708 |
| Gold                   |              101 |             150 |            151,010 |                    601 |
| Platinum               |              109 |             217 |             24,874 |                     76 |
| London Copper          |              113 |             158 |            335,472 |                  1,237 |
| London Aluminum Alloy  |               53 |             137 |             11,030 |                     58 |
| London Aluminum        |               83 |             141 |             11,875 |                     53 |
| London Nickel          |              109 |             150 |            627,498 |                  2,422 |
| Crude Oil              |              845 |             164 |            104,489 |                    421 |
| Heating Oil            |              109 |             146 |            234,490 |                    919 |
| Reformulated Gas       |               88 |             157 |            150,611 |                    614 |
| Mini Natural Gas       |               36 |              63 |             19,212 |                    194 |
| Brent Crude            |               77 |             116 |            165,439 |                    857 |
| Japanese Yen           |              109 |             169 |            160,212 |                  5,763 |
| Swiss Franc            |              121 |             166 |            142,449 |                    496 |
| Canadian Dollar        |               99 |             199 |            -18,331 |                    -62 |
| British Pound          |              109 |             175 |            116,443 |                    410 |

TABLE 5.21

| Commodity           |   Winning Trades |   Losing Trades |   Total Profit ($) |   Profit-per-Trade ($) |
|---------------------|------------------|-----------------|--------------------|------------------------|
| Dollar Index        |              102 |             124 |            109,924 |                    486 |
| Australian Dollar   |               84 |             139 |             44,909 |                    201 |
| Mexican Peso        |               59 |             104 |             33,312 |                    204 |
| Euro-Currency       |              115 |             150 |            220,537 |                    832 |
| 30-Year Bonds       |              103 |             172 |             76,734 |                    279 |
| 10-Year Notes       |              105 |             154 |             88,000 |                    339 |
| 5-Year Notes        |               83 |             118 |             53,601 |                    266 |
| 2-Year Notes        |               72 |              99 |             52,812 |                    308 |
| Eurodollar          |              106 |             128 |             84,475 |                    361 |
| Australian Bond     |               85 |             160 |             30,531 |                    177 |
| Canadian Govt. Bond |               73 |             118 |             33,918 |                    177 |
| Euro Bund           |               73 |             101 |             67,261 |                    386 |
| Long Gilt           |              105 |             171 |             67,049 |                    242 |
| Spanish Bond        |               54 |              96 |             16,265 |                    108 |
| Simex JGB Bond      |               61 |             106 |             22,902 |                    137 |
| Hang Seng Index     |               93 |             133 |             79,499 |                    351 |
| Dax Index           |               76 |             113 |            197,275 |                  1,043 |
| Mini S&P            |               99 |             200 |             14,112 |                     47 |
| Mini Russell 2000   |               35 |              59 |              4,789 |                     50 |
| Mini Midcap         |               69 |             120 |             -8,651 |                    -46 |
| Mini Nasdaq         |               50 |              93 |             61,010 |                    426 |
| Nikkei              |               76 |              96 |             98,075 |                    570 |
| All Trade Average   |            2,976 |           4,137 |          2,756,675 |                    387 |
| Long Trade          |            1,594 |           2,086 |          1,895,123 |                    514 |
| Short Trade         |            1,382 |           2,051 |            861,542 |                    250 |

(

Continued

## ■ Conclusion

In this chapter we started the development of two trading strategies, one for stocks and one for commodities. Both used a Donchian entry, but the stock entry was counter-trend while the commodity strategy was trend-following. To  this  point,  we've  conditionally  developed  the  strategies  from  entry through exit. In the next chapter, we'll look at adding filters to try and make the strategies tradeable.

)

## Trading System Elements: Filters

I n  general,  filters  are  used  in  conjunction  with  the  entry  to  eliminate certain trades from being taken. When volatility in the S&amp;P was high in the late 1990s, it was common to employ a filter to avoid going long on a Friday or short on a Monday. The rationale was that many traders didn't want to risk being long over the weekend so they exited on Friday. That caused the market to go down on that day more often any other day of the week. Conversely, the money would flow back in on Monday so it had an up bias. Those are trading-day-of-the-week type filters.

Other  common  filters  are  seasonal,  volatility,  and  longer-term  trend. Seasonal filters use the seasonal tendencies of an instrument to avoid trading against historical bias. Many traders won't short reformulated gas going into the driving season, or short heating oil going into winter. For stocks, forms of a seasonal filter would be to avoid entering on a report day or an earnings day. Volatility filters are useful for keeping you out of an instrument that is going parabolic, or one whose trading range is so volatile that your stop is likely to be hit by the normal noise of its day-to-day moves. There's big profit potential in those situations, but also abnormal risk.  The longer-term trend filter is useful as an adjunct to a shorter-term system:  Y ou only take the trades in the direction of the longer-term trend.

I use filters in almost all my systems. Some are intended to enhance profitability, and some are strictly meant to avoid risk. First we'll develop filters for the stock system; then we'll look at improving the commodity system.

## ■ Trading-day-of-the-week Filter (Stocks)

Let's see if avoiding stock entry on a particular day of the week helps baseline performance.  Table 6.1 shows the performance of the baseline we carry over from last chapter. Added to that is logic that prohibits entry on the day indicated.

TABLE 6.1 Day of the Week Filters with Stocks

| Entry Prohibited   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to-Pain Ratio |
|--------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|----------------------|
| None*              |                              50 |                      70,877 |                         50,693 |               92,510 |                 1.40 |
| Monday             |                              48 |                      62,842 |                         49,007 |              102,360 |                 1.28 |
| Tuesday            |                              49 |                      65,249 |                         49,741 |               91,760 |                 1.31 |
| Wednesday          |                              52 |                      68,538 |                         47,013 |               91,176 |                 1.46 |
| Thursday           |                              51 |                      67,922 |                         44,802 |               93,204 |                 1.52 |
| Friday             |                              53 |                      70,020 |                         46,779 |               87,027 |                 1.50 |

* Baseline

It looks like the best entries are early in the week; if we skip trading on either Monday or  Tuesday, the stats drop off. Later in the week, the stats get better if entries are bypassed, but no day has such a large impact on trading that  it  should  receive  special  consideration  as  an  addition  to  the  baseline system.

There's one other trading-day-of-the-week type filter that's always worth looking at with stocks, and that's the periods around the end of the quarter and the start of the month. The rationale is that money managers perform window dressing on their portfolios at those times.

When the trades initiated on the last day of the month and those on the first day of the month were compared with baseline performance, the profit was identical: $50 per trade. Those days are just like any other with this strategy.

## ■ Longer-Term Trend Filter (Stocks)

Our  long-only  stock  strategy  enters  on  weakness  when  there  is  a  close below the lowest close of the preceding eight trading days.  Those trades can occur when the longer-term trend is either up or down. Let's look at only taking trades that set up when the longer-term trend is up. An easy way to  define  the  longer-term  trend  is  to  compare  today's  closing  price  with price some number of days ago. If price today is higher, the trend is up. Table 6.2 shows our baseline when the longer-term trend ranges from 30 to 90 bars ago.

TABLE 6.2 Adding a Longer-Term Trend Filter to Stocks

| Number of Bars for Longer-Term Trend   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to-Pain Ratio |
|----------------------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|----------------------|
| None*                                  |                              50 |                      70,877 |                         50,693 |               92,510 |                 1.40 |
| 30                                     |                              53 |                      35,227 |                         19,985 |               39,201 |                 1.76 |
| 40                                     |                              48 |                      33,761 |                         21,535 |               37,633 |                 1.57 |
| 50                                     |                              50 |                      35,620 |                         21,095 |               37,744 |                 1.69 |
| 60                                     |                              52 |                      37,565 |                         20,516 |               37,828 |                 1.83 |
| 70**                                   |                              54 |                      39,904 |                         21,026 |               41,467 |                 1.90 |
| 80                                     |                              52 |                      39,146 |                         21,219 |               38,044 |                 1.84 |
| 90                                     |                              51 |                      38,633 |                         21,620 |               46,537 |                 1.79 |

* Baseline

** New baseline

Trading with the longer-term trend causes performance to jump, as measured by our gain-to-pain metric. Note that the new baseline almost meets the minimum conditions for a tradeable system if we use the 70-day lookback filter.

- ■ Average profit-per-year is almost as large as the max draw-down.
- ■ If  you trade the strategy with $200,000, your max draw-down will be about 21 percent.
- ■ If you trade the strategy with $200,000, your average annual return will be about 20 percent, and the average max draw-down you will see each year is about 10.5 percent.

## ■ Volatility-Based Filters (Stocks)

I always check performance with two forms of volatility filter. Your entry setup can occur in a sleepy, almost sideways market, or in a very volatile up and down market. In the first case, your profitability potential is reduced from a normal setup.  You are taking the risk of entering the trade, but your profit potential isn't that good unless the market heats up quickly, and in the direction of the trade. T o filter out those lesser-profit potential trades, the first filter only accepts trades that meet a certain threshold volatility;

that's the low-volatility filter.  When volatility is way above normal, you have an increased probability of getting stopped out due to higher up and down market noise. The high-volatility filter bypasses trade entry when volatility is too high. There are a number of ways to measure volatility, like average range, average true range, or some measure of standard deviation.  We'll test both range and standard deviation. Table 6.3 shows results when trades are inhibited by the low-volatility filter because recent average range wasn't a large enough percentage of price.  The average range was computed over the five days previous to the entry.

TABLE 6.3 Low-Volatility Filter Based on Average Range for Stocks

| Average Range Greater than x Percent of Price   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to- Pain Ratio |
|-------------------------------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|-----------------------|
| N/A*                                            |                              54 |                      39,904 |                         21,026 |               41,467 |                  1.90 |
| 1                                               |                              54 |                      39,873 |                         21,015 |               41,467 |                  1.90 |
| 2                                               |                              58 |                      36,822 |                         20,052 |               34,354 |                  1.84 |
| 3                                               |                              67 |                      26,670 |                         15,757 |               23,047 |                  1.69 |

* Baseline

The low-volatility  filter  did  increase  profit-per-trade  by  screening  out trades that just didn't have good profit potential, but gain-to-pain was decreased, so this filter won't be added. Let's look at the high-volatility filter using average range.  Table 6.4 shows trade statistics.

TABLE 6.4 High-Volatility Filter Based on Range for Stocks

| Average Range Less than x Percent of Price   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to-Pain Ratio |
|----------------------------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|----------------------|
| N/A*                                         |                              54 |                      39,904 |                         21,026 |               41,467 |                 1.90 |
| 10                                           |                              53 |                      38,848 |                         20,863 |               41,467 |                 1.86 |
| 8                                            |                              51 |                      36,273 |                         20,578 |               41,467 |                 1.76 |
| 6                                            |                              48 |                      32,667 |                         19,859 |               40,797 |                 1.64 |
| 5                                            |                              47 |                      30,201 |                         18,114 |               40,327 |                 1.67 |

* Baseline

The  high-volatility  filter  did  screen  out  higher-volatility  stocks,  as seen by reduced profit-per-trade and reduced average max draw-down, but profitability came down faster than draw-down, so the gain-to-pain metric decreased. Maybe standard deviation volatility filters will be more successful.

Table 6.5 shows results using the low-volatility standard deviation filter. The  standard  deviation  computation  was  based  on  the  20  closing  prices previous to the day of the signal.

TABLE 6.5 Low-Volatility Filter Based on Standard Deviation for Stocks

| Standard Deviation Greater than x Percent of Price   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to- Pain Ratio |
|------------------------------------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|-----------------------|
| N/A*                                                 |                              54 |                      39,904 |                         21,026 |               41,467 |                  1.90 |
| 1                                                    |                              57 |                      39,011 |                         20,888 |               41,187 |                  1.87 |
| 2                                                    |                              67 |                      31,198 |                         17,366 |               29,045 |                  1.80 |
| 3**                                                  |                              84 |                      23,650 |                         11,491 |               17,207 |                  2.06 |
| 4                                                    |                              97 |                      16,028 |                          7,994 |               11,511 |                  2.01 |

Taking signals that only have a standard deviation of closing price that is greater than 3 percent of price increases profit-per-trade while decreasing average max draw-down and max draw-down. Note that the new baseline stock strategy is now tradeable.

The  average  annual  return  is  greater  than  the  max  draw-down.  If traded with $100,000, the return would average about 24 percent per year, the max draw-down over the past 12 years would have been about 17 percent, and the max draw-down you could expect each year was about 11.5 percent.

Let's see if the standard deviation high-volatility filter can make things even better. Table 6.6 shows results when trades are bypassed that have a standard deviation that is greater than x percent of price.

TABLE 6.6 High Volatility Filter Based on Standard Deviation on Stocks

| Standard Deviation Less than x Percent of Price   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to- Pain Ratio |
|---------------------------------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|-----------------------|
| N/A*                                              |                              84 |                      23,650 |                         11,491 |               17,207 |                  2.06 |
| 10                                                |                              84 |                      23,148 |                         11,469 |               17,207 |                  2.02 |
| 8                                                 |                              82 |                      22,402 |                         11,430 |               17,207 |                  1.96 |
| 6                                                 |                              78 |                      20,210 |                         10,701 |               17,207 |                  1.89 |

Results aren't improved with this filter, so it won't be added to the current baseline. Figure 6.1 shows the equity curve for the developed strategy.

FIGURE  6.1 Developed Strategy Equity Curve for Stocks

<!-- image -->

Note that the ugly 2008 draw-down we saw in the stock system equity curve from Chapter   5 is gone. This is primarily due to the addition of the 70-day longer-term fi  lter.  When the market plummeted in 2008, that fi  lter kept us out of most of the long trades. Table   6.7 is a year-by-year breakout of return and draw-down.

TABLE 6.7 Annual Return and Max Draw-Down for Stock System

|   Year | Yearly Profit ($)   |   Annual Max Draw-Down ($) |
|--------|---------------------|----------------------------|
|   2000 | 30,424              |                     12,875 |
|   2001 | 38,149              |                     11,682 |
|   2002 | 20,709              |                     10,674 |
|   2003 | 53,978              |                     10,476 |
|   2004 | 10,812              |                      8,171 |
|   2005 | 15,788              |                      4,712 |
|   2006 | 4,073               |                      5,365 |
|   2007 | 16,871              |                      6,762 |
|   2008 | - 9,422             |                     12,347 |
|   2009 | 54,054              |                      8,781 |
|   2010 | 14,749              |                     11,288 |
|   2011 | 9,315               |                     17,207 |

There was only one losing year (2008), and that year would have been about a 10 percent loss on a $100,000 account-not too bad when you consider that the S&amp;P was down over 38 percent that year. Table   6.8 shows the performance of each stock in our NASDAQ 100 basket.

| TABLE 6.8 Stock Symbol   |   Developed Stock Strategy: Winning Trades |   Performance Losing Trades |   by Symbol Total Profit ($) |   Profit-per-Trade ($) |
|--------------------------|--------------------------------------------|-----------------------------|------------------------------|------------------------|
| AAPL                     |                                         33 |                          12 |                        2,434 |                     54 |
| ADBE                     |                                         23 |                          10 |                        4,162 |                    126 |
| ADP                      |                                          4 |                           3 |                          141 |                     20 |
| ADSK                     |                                         23 |                          12 |                        1,185 |                     33 |
| AKAM                     |                                         36 |                          17 |                        2,894 |                     54 |
| ALTR                     |                                         18 |                          15 |                       -2,518 |                    -77 |
| ALXN                     |                                         24 |                          20 |                        1,116 |                     25 |
| AMAT                     |                                         25 |                          11 |                        2,475 |                     68 |
| AMGN                     |                                          5 |                           4 |                          302 |                     33 |
| APOL                     |                                         32 |                           4 |                        7,105 |                    197 |
| ATVI                     |                                         30 |                          11 |                        5,051 |                    123 |
| AVGO                     |                                          9 |                           2 |                          310 |                     28 |
| BBBY                     |                                         19 |                           5 |                        3,634 |                    151 |
| BIDU                     |                                         24 |                           6 |                        5,421 |                    180 |
| BIIB                     |                                         25 |                           8 |                        4,098 |                    124 |
| BMC                      |                                         15 |                           9 |                        1,307 |                     54 |
| BRCM                     |                                         33 |                          12 |                        5,967 |                    132 |
| CA                       |                                         14 |                          11 |                          196 |                      7 |
| CELG                     |                                         33 |                           9 |                        5,483 |                    130 |
| CERN                     |                                         24 |                           7 |                        6,062 |                    195 |
| CHKP                     |                                         21 |                           9 |                        2,605 |                     86 |
| CHRW                     |                                         11 |                           9 |                          592 |                     29 |
| CMCSA                    |                                          9 |                           6 |                          766 |                     51 |
| COST                     |                                          8 |                           2 |                        1,833 |                    183 |
| CSCO                     |                                         12 |                          11 |                           56 |                      2 |
| CTRP                     |                                         22 |                          13 |                        4,751 |                    135 |
| CTSH                     |                                         30 |                          14 |                        5,549 |                    126 |
| CTXS                     |                                         23 |                          15 |                       -1,621 |                    -43 |
| DELL                     |                                         13 |                           9 |                          306 |                     13 |
| DLTR                     |                                         17 |                           7 |                       21,202 |                     87 |
| DTV                      |                                          4 |                           6 |                          243 |                     24 |
| EBAY                     |                                         21 |                          11 |                        2,127 |                     66 |
| ESRX                     |                                         21 |                           9 |                        4,751 |                    158 |
| EXPD                     |                                         27 |                           7 |                        4,684 |                    137 |
| FAST                     |                                         19 |                          12 |                        1,760 |                     56 |
| FFIV                     |                                         40 |                          11 |                        5,771 |                    113 |
| FISV                     |                                          6 |                           6 |                          240 |                     20 |

TRADING SYSTEM ELEMENTS: FILTERS

TRADING SYSTEM ELEMENTS: FILTERS

| Stock Symbol TABLE 6.8   |   Winning Trades ( Continued ) |   Losing Trades |   Total Profit ($) |   Profit-per-Trade ($) |
|--------------------------|--------------------------------|-----------------|--------------------|------------------------|
| FLEX                     |                             20 |              11 |              1,464 |                     47 |
| FOSL                     |                             22 |              14 |              3,484 |                     96 |
| GILD                     |                             32 |               4 |              7,896 |                    219 |
| GMCR                     |                             31 |              20 |                473 |                      9 |
| GOLD                     |                             38 |              14 |              3,857 |                     74 |
| GOOG                     |                              9 |               6 |               -544 |                    -37 |
| GRMN                     |                             25 |              14 |              1,362 |                     34 |
| HSIC                     |                             11 |               8 |              1,711 |                     90 |
| INFY                     |                             25 |               9 |              4,831 |                    142 |
| INTC                     |                             13 |               4 |              2,298 |                    135 |
| INTU                     |                             19 |              11 |              3,153 |                    105 |
| ISRG                     |                             27 |              16 |              1,966 |                     45 |
| KLAC                     |                             30 |               9 |              6,481 |                    166 |
| LIFE                     |                             14 |              10 |              1,170 |                     48 |
| LINTA                    |                              5 |               6 |                357 |                     32 |
| LLTC                     |                             21 |               9 |              2,433 |                     81 |
| LRCX                     |                             33 |              14 |              4,557 |                     96 |
| MAT                      |                              8 |               4 |              1,174 |                     97 |
| MCHP                     |                             18 |              12 |                704 |                     23 |
| MNST                     |                             26 |              15 |              3,419 |                     83 |
| MRVL                     |                             26 |              16 |              5,299 |                    126 |
| MSFT                     |                              9 |               6 |                575 |                     38 |
| MU                       |                             36 |              16 |              5,002 |                     96 |
| MXIM                     |                             21 |               9 |              3,378 |                    112 |
| MYL                      |                             17 |               3 |              2,374 |                    118 |
| NFLX                     |                             35 |              20 |              2,726 |                     49 |
| NTAP                     |                             28 |              19 |              3,236 |                     68 |
| NUAN                     |                             37 |              18 |              6,257 |                    113 |
| NVDA                     |                             34 |              25 |                -46 |                     -1 |
| NWSA                     |                             10 |               6 |              1,186 |                     74 |
| ORCL                     |                             12 |              11 |               -116 |                     -6 |
| ORLY                     |                             16 |               9 |                594 |                     23 |
| PAYX                     |                              7 |               6 |                -92 |                     -8 |
| PCAR                     |                             18 |               8 |              1,578 |                     60 |
| PRGO                     |                             16 |               8 |              1,578 |                    108 |
| QCOM                     |                             21 |               7 |              4,387 |                    156 |
| RIMM                     |                             31 |              17 |              1,879 |                     39 |
| ROST                     |                             21 |               5 |              3,070 |                    118 |

| TABLE 6.8   |   ( Continued ) |    |        |     |
|-------------|-----------------|----|--------|-----|
| SBUX        |              19 |  7 |  3,386 | 130 |
| SHLD        |              16 | 13 | -1,350 | -47 |
| SIAL        |               3 |  8 |   -849 | -78 |
| SIRI        |              39 | 15 |  7,611 | 140 |
| SNDK        |              47 | 16 |  4,390 |  69 |
| SPLS        |              14 |  7 |  1,858 |  88 |
| SRCL        |              21 |  6 |  3,520 | 130 |
| STX         |              23 |  4 |  5,715 | 211 |
| SYMC        |              21 |  8 |  3,742 | 129 |
| TEVA        |              10 |  2 |  2,796 | 233 |
| TXN         |              13 | 10 |  1,133 |  49 |
| VMED        |              10 |  8 |    412 |  22 |
| VOD         |               8 |  5 |    848 |  65 |
| VRSN        |              27 | 15 |  2,486 |  59 |
| VRTX        |              33 | 15 |  2,650 |  55 |
| WCRX        |               4 |  3 |    243 |  34 |
| WFM         |              18 |  9 |  2,583 |  95 |
| WYNN        |              26 | 10 |  3,941 | 109 |
| XLNX        |              18 | 13 |  2,115 |  68 |
| XRAY        |               7 |  4 |    422 |  38 |
| YHOO        |              23 | 11 |  2,755 |  81 |

Scanning the results, only eight of the 100 didn't make money, and 37 averaged more than $100 a trade. Let's now further the development of the commodity strategy.

## ■ Trading-Day-of-the-Week Filter (Commodities)

There's a powerful trading-day-of-the-week type filter that I use in almost all my mid- to longer-term commodity trend-following strategies. It's a pullback filter . If the long setup exists, we wait for price to go down one day , and if the setup still exists, we enter the long position. For shorts, we wait for price to rally for one day. Most trend-following long signals occur on an up close.  The logic of this filter is to try to get a better price by waiting for a down close. Beyond that, this filter eliminates a lot of false entries, entries that occur at the top of the move, then go straight down to your catastrophic stop.

To illustrate, a run was made on the 56-commodity basket and, whenever today's close was less than yesterday's, a long trade was taken on the next open and exited on the open after that; reverse rules for shorts. The results are shown in Table 6.9.

| TABLE 6.9    | Long- and Short-Trade Breakout for Trading-Day-of-the-Week Filter   | Long- and Short-Trade Breakout for Trading-Day-of-the-Week Filter   | Long- and Short-Trade Breakout for Trading-Day-of-the-Week Filter   | Long- and Short-Trade Breakout for Trading-Day-of-the-Week Filter   |
|--------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
|              | Winners                                                             | Losers                                                              | Profit ($)                                                          | Profit-per-Trade ($)                                                |
| Long Trades  | 103,423                                                             | 96,495                                                              | 3,907,148                                                           | 19                                                                  |
| Short Trades | 103,743                                                             | 104,504                                                             | 1,660,935                                                           | 7                                                                   |

Not bad.  The addition of the filter would probably come close to covering transaction costs for the entry. Let's look at what happens when we only execute the long or short pullback filter when it is in the direction of the trend. Since we're using a 20-day Donchian entry, we'll use a 20-day trend look-back filter.  If  today's  close  is  higher  than  it  was  20  days  ago,  then the longer-term trend is up and we enter the one-day trades every time there's a down close. Reverse logic for shorts. The results are shown in Table 6.10.

| TABLE 6.10   | Long- and Short-Trade Breakout for Trading-Day-of-the-Week Filter with Trend Filter   | Long- and Short-Trade Breakout for Trading-Day-of-the-Week Filter with Trend Filter   | Long- and Short-Trade Breakout for Trading-Day-of-the-Week Filter with Trend Filter   | Long- and Short-Trade Breakout for Trading-Day-of-the-Week Filter with Trend Filter   |
|--------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
|              | Winners                                                                               | Losers                                                                                | Profit ($)                                                                            | Profit-per-Trade ($)                                                                  |
| Long Trades  | 47,582                                                                                | 42,862                                                                                | 3,270,100                                                                             | 36                                                                                    |
| Short Trades | 42,660                                                                                | 41,707                                                                                | 1,834,168                                                                             | 21                                                                                    |

That  filter  addition  would  cover  the  transaction  costs  of  the  whole trade-definitely worthwhile if the other stats aren't impacted. Let's try it with our baseline Donchian commodity system from Chapter 5. Table 6.11 shows the trading statistics.

| TABLE 6.11       | TABLE 6.11                    | Commodity Strategy with Pullback Filter   | Commodity Strategy with Pullback Filter   | Commodity Strategy with Pullback Filter   |                    |
|------------------|-------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|--------------------|
| Pullback Filter? | Average Profit- per-Trade ($) | Average Annual Return ($)                 | Average Annual Draw-Down ($)              | Max Draw- Down ($)                        | Gain-to-Pain Ratio |
| None*            | 378                           | 167,553                                   | 147,173                                   | 474,203                                   | 1.14               |
| Yes              | 430                           | 136,498                                   | 126,445                                   | 472,767                                   | 1.08               |

The  pullback  filter  did  add  profit-per-trade  to  the  baseline,  but  total profitability  as  measured  by  average  annual  return  decreased  by  almost

20 percent. Average draw-down did not come down nearly as fast. This is one of the few times I've seen that this filter did not help performance. Let's look at the longer-term trend filter next.

## ■ Longer-Term Trend Filter (Commodities)

This filter is identical to the one we implemented in the stock system. We only  take  trades  if  they  are  in  the  same  direction  as  the  longerterm trend, as determined by a comparison of today's close with that of x days ago. Table 6.12 shows trading results for look-backs ranging from 30 to 90 days.

| TABLE 6.12                     | Longer-Term Trend Filter on Commodities   | Longer-Term Trend Filter on Commodities   | Longer-Term Trend Filter on Commodities   | Longer-Term Trend Filter on Commodities   | Longer-Term Trend Filter on Commodities   |
|--------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| Trend Filter Look-Back in Days | Average Profit- per-Trade ($)             | Average Annual Return ($)                 | Average Annual Draw-Down ($)              | Max Draw- Down ($)                        | Gain-to-Pain Ratio                        |
| None*                          | 378                                       | 167,553                                   | 147,173                                   | 474,203                                   | 1.14                                      |
| 30                             | 416                                       | 151,116                                   | 146,063                                   | 513,398                                   | 1.03                                      |
| 40                             | 463                                       | 158,228                                   | 140,948                                   | 424,856                                   | 1.12                                      |
| 50                             | 467                                       | 152,796                                   | 136,426                                   | 464,345                                   | 1.12                                      |
| 60                             | 519                                       | 162,705                                   | 140,193                                   | 395,950                                   | 1.16                                      |
| 70**                           | 545                                       | 166,002                                   | 135,441                                   | 354,671                                   | 1.23                                      |
| 80                             | 559                                       | 165,919                                   | 138,583                                   | 342,742                                   | 1.20                                      |
| 90                             | 554                                       | 161,079                                   | 140,617                                   | 420,117                                   | 1.15                                      |

* Baseline

** New baseline

The 70-day look-back filter increases profit-per-trade by over 40 percent while  significantly  lowering  both  average  maximum  draw-down  and  max draw-down. It will be added to the existing strategy to form the new baseline.

## ■ Volatility-Based Filters (Commodities)

As we did with the stock strategy, we'll test low- and high-volatility filters based on standard deviation and average range. Table 6.13 shows results when we take only signaled trades that have a standard deviation greater than X dollars. The standard deviation measure is the standard deviation of closing price for the 20 days preceding the signal converted to dollars by multiplying the standard deviation point value by the dollars per trade for that commodity.

TABLE 6.13

Low-Volatility Filter Based on Standard Deviation on Commodities

| Take Trades with One Standard Deviation > $ x   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to- Pain Ratio |
|-------------------------------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|-----------------------|
| N/A*                                            |                             545 |                     166,002 |                        135,441 |              354,671 |                  1.23 |
| 100                                             |                             546 |                     165,728 |                        135,424 |              354,546 |                  1.22 |
| 150                                             |                             550 |                     164,790 |                        135,451 |              353,982 |                  1.22 |
| 200                                             |                             560 |                     163,356 |                        135,570 |              354,073 |                  1.20 |
| 250                                             |                             574 |                     161,537 |                        135,790 |              353,637 |                  1.19 |
| 300                                             |                             593 |                     159,267 |                        135,855 |              352,566 |                  1.17 |

* Baseline

The low-volatility filter does eliminate some of the less profitable trades, as shown by increasing profit-per-trade in Table 6.13, but it doesn't help with the draw-downs, so it won't be added to the baseline. Next we'll test the high volatility standard deviation filter. Table 6.14 shows trading results.

| TABLE 6.14                                    | High-Volatility Filter Based on Standard Deviation on Commodities   | High-Volatility Filter Based on Standard Deviation on Commodities   | High-Volatility Filter Based on Standard Deviation on Commodities   | High-Volatility Filter Based on Standard Deviation on Commodities   | High-Volatility Filter Based on Standard Deviation on Commodities   |
|-----------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| Take Trades with One Standard Deviation < $ x | Take Trades with One Standard Deviation < $ x                       | Average Profit- per-Trade ($) Average Return                        | Annual ($) Average Annual Draw-Down ($)                             | Max Draw- Down ($)                                                  | Gain-to- Pain Ratio                                                 |
| N/A*                                          | 545                                                                 | 166,002                                                             | 135,441                                                             | 354,671                                                             | 1.23                                                                |
| 2,000                                         | 481                                                                 | 140,017                                                             | 94,013                                                              | 197,578                                                             | 1.49                                                                |
| 1,500                                         | 461                                                                 | 129,392                                                             | 81,262                                                              | 174,542                                                             | 1.59                                                                |
| 1,000                                         | 384                                                                 | 98,256                                                              | 60,269                                                              | 137,611                                                             | 1.63                                                                |
| 900                                           | 362                                                                 | 89,546                                                              | 55,327                                                              | 121,582                                                             | 1.62                                                                |
| 800                                           | 354                                                                 | 83,435                                                              | 49,994                                                              | 100,037                                                             | 1.67                                                                |
| 700                                           | 331                                                                 | 73,115                                                              | 45,318                                                              | 106,570                                                             | 1.61                                                                |

* Baseline

The  high-volatility  standard  deviation  filter  does  improve  trading,  as shown  by  the  gain-to-pain  ratio.  Notice  how  the  draw-downs  have  been drastically reduced. Let's see if the low- and high-volatility filters based on range do a better job.

The low-volatility filter using average range was tested, and the results were about the same as the low-volatility standard deviation filter, so they won't be added to the baseline. Table 6.15 shows the high-volatility range filter results. The average range is for the 20 days preceding the entry, and the points have been converted to dollars by multiplying the average by the dollars per point of the commodity.

TABLE 6.15 High-Volatility Filter Based on Average Range on Commodities

| Take Trades with Average Range < $ x   |   Average Profit- per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw- Down ($) |   Gain-to-Pain Ratio |
|----------------------------------------|---------------------------------|-----------------------------|--------------------------------|----------------------|----------------------|
| N/A*                                   |                             545 |                     166,002 |                        135,441 |              354,671 |                 1.23 |
| 800                                    |                             407 |                      96,926 |                         48,847 |               89,669 |                 1.98 |
| 700**                                  |                             410 |                      91,354 |                         43,209 |               86,296 |                 2.11 |
| 600                                    |                             384 |                      82,041 |                         40,703 |               78,142 |                 2.02 |

* Baseline

** New baseline

In  this  case,  the  average  range  high-volatility  filter  outperformed the standard deviation filter. That's not always the case. Performance has jumped  due  to  this  filter  and  the  system  now  meets  our  criteria  for tradeability.

- ■ The average annual return exceeds the max draw-down and is over twice as large as the average max draw-down per year.
- ■ You  could  trade  the  strategy  as  is  with  $450,000  and  average  about 20 percent a year, with an average max draw-down of less than 10 percent, and a max draw-down over 30 years of less than 20 percent.

Before we leave the development of the commodity strategy, there's one other thing we need to look at based on the results of Table 6.15, which showed that we should bypass entries with a 20-day average range greater than $700. But suppose we enter a trade and things heat up. Maybe the  same  filter  should  signal  a  trade  exit  if  a  certain  volatility  limit  is exceeded.

Table 6.16 shows the results if a trade is exited should the average range of  the  last  20  trading  days  exceed  a  certain  dollar  limit.  If  the  condition exists on the close, exit is done on the next open.

| TABLE 6.16                          | Commodity Strategy: Exit Based on High-Volatility Filter   | Commodity Strategy: Exit Based on High-Volatility Filter   | Commodity Strategy: Exit Based on High-Volatility Filter   | Commodity Strategy: Exit Based on High-Volatility Filter   | Commodity Strategy: Exit Based on High-Volatility Filter   |
|-------------------------------------|------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|
| Exit Trades with Average Range >$ x | Average Profit- per-Trade ($)                              | Average Annual Return ($)                                  | Average Annual Draw-Down ($)                               | Max Draw- Down ($)                                         | Gain-to-Pain Ratio                                         |
| N/A*                                | 410                                                        | 91,354                                                     | 43,209                                                     | 86,296                                                     | 2.11                                                       |
| 1,000                               | 399                                                        | 88,979                                                     | 39,752                                                     | 83,837                                                     | 2.24                                                       |
| 900                                 | 395                                                        | 87,916                                                     | 38,158                                                     | 82,650                                                     | 2.30                                                       |
| 800**                               | 387                                                        | 86,793                                                     | 35,634                                                     | 81,150                                                     | 2.44                                                       |
| 700                                 | 337                                                        | 79,780                                                     | 33,705                                                     | 79,330                                                     | 2.36                                                       |

This  addition  does  improve  the  solution. The  gain-to-pain  ratio  now stands at 2.44. Figure   6.2 shows the resultant equity curve.

FIGURE  6.2 Developed Commodity Strategy Equity Curve

<!-- image -->

This  is  a  fairly  good-looking  equity  curve,  though  the  lessening  of  the upward slope over the last three years is a bit of a concern.  Table   6.17 shows a year-by-year breakout of performance.

| TABLE 6.17   | Annual Return and Max Draw-Down for Commodity Strategy   | Annual Return and Max Draw-Down for Commodity Strategy   |
|--------------|----------------------------------------------------------|----------------------------------------------------------|
| Year         | Yearly Profit ($)                                        | Annual Max Draw-Down ($)                                 |
| 1980         | 45,243                                                   | 31,602                                                   |
| 1981         | 131,473                                                  | 35,973                                                   |
| 1982         | 70,948                                                   | 26,559                                                   |
| 1983         | 60,062                                                   | 20,128                                                   |
| 1984         | 75,650                                                   | 23,651                                                   |
| 1985         | 80,800                                                   | 30,075                                                   |
| 1986         | 72,105                                                   | 42,244                                                   |
| 1987         | 176,109                                                  | 33,076                                                   |
| 1988         | 140,708                                                  | 19,920                                                   |
| 1989         | 72,787                                                   | 32,454                                                   |
| 1990         | 149,391                                                  | 22,837                                                   |
| 1991         | 103,496                                                  | 23,260                                                   |
| 1992         | 71,787                                                   | 27,965                                                   |
| 1993         | 174,368                                                  | 16,375                                                   |
| 1994         | 74,961                                                   | 35,434                                                   |
| 1995         | 107,427                                                  | 41,515                                                   |

TABLE 6.17

(

Continued

)

| Year    |   Yearly Profit ($) |   Annual Max Draw-Down ($) |
|---------|---------------------|----------------------------|
| 1996    |              70,475 |                     34,187 |
| 1997    |             111,771 |                     25,842 |
| 1998    |              77,517 |                     33,384 |
| 1999    |              40,987 |                     72,809 |
| 2000    |             107,739 |                     13,563 |
| 2001    |              49,441 |                     44,766 |
| 2002    |              77,130 |                     36,383 |
| 2003    |             131,397 |                     36,355 |
| 2004    |              47,863 |                     35,843 |
| 2005    |              90,391 |                     22,619 |
| 2006    |              60,636 |                     36,073 |
| 2007    |              77,027 |                     23,311 |
| 2008    |             172,057 |                     38,758 |
| 2009    |              25,429 |                     21,180 |
| 2010    |              56,932 |                     19,557 |
| 2011    |             -34,366 |                     46,111 |
| Average |              86,639 |                     31,369 |

## Lastly,  T able 6.18 shows performance by commodity.

| TABLE 6.18    | Developed Commodity Strategy: Performance by Commodity   | Developed Commodity Strategy: Performance by Commodity   | Developed Commodity Strategy: Performance by Commodity   | Developed Commodity Strategy: Performance by Commodity   |
|---------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Commodity     | Winning Trades                                           | Losing Trades                                            | Total Profit ($)                                         | Profit-per-Trade ($)                                     |
| Corn          | 79                                                       | 111                                                      | 25,675                                                   | 135                                                      |
| Soybeans      | 71                                                       | 94                                                       | 57,025                                                   | 345                                                      |
| Bean Meal     | 74                                                       | 108                                                      | 52,490                                                   | 288                                                      |
| Bean Oil      | 90                                                       | 100                                                      | 52,182                                                   | 274                                                      |
| Wheat         | 69                                                       | 123                                                      | 9,562                                                    | 49                                                       |
| KC Wheat      | 66                                                       | 114                                                      | 29,825                                                   | 165                                                      |
| Rough Rice    | 53                                                       | 73                                                       | 70,479                                                   | 559                                                      |
| Live Cattle   | 71                                                       | 142                                                      | -4,271                                                   | -21                                                      |
| Lean Hogs     | 77                                                       | 143                                                      | -1,520                                                   | -7                                                       |
| Feeder Cattle | 76                                                       | 113                                                      | 25,687                                                   | 135                                                      |
| Coffee        | 37                                                       | 40                                                       | 50,493                                                   | 655                                                      |
| Cotton        | 80                                                       | 92                                                       | 100,590                                                  | 584                                                      |
| Orange Juice  | 79                                                       | 114                                                      | 56,302                                                   | 291                                                      |
| Lumber        | 62                                                       | 81                                                       | 75,514                                                   | 528                                                      |
| Cocoa         | 60                                                       | 136                                                      | -16,080                                                  | -83                                                      |
| Sugar         | 79                                                       | 88                                                       | 55,238                                                   | 330                                                      |
| Copper        | 65                                                       | 93                                                       | 21,387                                                   | 135                                                      |
| Palladium     | 59                                                       | 96                                                       | 101,279                                                  | 653                                                      |
| (             | (                                                        | (                                                        | (                                                        | continued )                                              |

## TABLE 6.18

(

Continued

| Commodity             |   Winning Trades |   Losing Trades |   Total Profit ($) |   Profit-per-Trade ($) |
|-----------------------|------------------|-----------------|--------------------|------------------------|
| Silver                |               55 |              87 |            110,074 |                    775 |
| Gold                  |               56 |              88 |             54,440 |                    378 |
| Platinum              |               62 |             120 |             45,791 |                     25 |
| London Copper         |               44 |              54 |             41,545 |                    423 |
| London Aluminum Alloy |               40 |              78 |             39,240 |                    332 |
| London Aluminum       |               48 |              63 |             39,062 |                    351 |
| London Nickel         |               33 |              56 |             81,165 |                    911 |
| Crude Oil             |              525 |              60 |             61,059 |                    545 |
| Heating Oil           |               69 |              81 |             94,290 |                    628 |
| Reformulated Gas      |               50 |              63 |             81,408 |                    720 |
| Mini Natural Gas      |               20 |              30 |             15,675 |                    313 |
| Brent Crude           |               44 |              41 |             71,139 |                    836 |
| Japanese Yen          |               38 |              32 |             88,475 |                  1,263 |
| Swiss Franc           |               43 |              33 |             81,512 |                  1,072 |
| Canadian Dollar       |               61 |             107 |             26,179 |                    155 |
| British Pound         |               40 |              48 |            117,225 |                  1,332 |
| Dollar Index          |               57 |              68 |            104,734 |                    837 |
| Australian Dollar     |               45 |              74 |             22,470 |                    188 |
| Mexican Peso          |               45 |              57 |             36,549 |                    358 |
| Euro-Currency         |               14 |              12 |             51,774 |                  1,991 |
| 30-Year Bonds         |               47 |              67 |             43,500 |                    381 |
| 10-Year Notes         |               72 |              92 |             67,609 |                    412 |
| 5-Year Notes          |               61 |              78 |             52,085 |                    374 |
| 2-Year Notes          |               54 |              62 |             51,562 |                    444 |
| Eurodollar            |               80 |              90 |             66,399 |                    390 |
| Australian Bond       |               66 |              93 |             53,733 |                    337 |
| Canadian Govt. Bond   |               60 |              76 |             37,503 |                    275 |
| Euro Bund             |               41 |              32 |             93,161 |                  1,276 |
| Long Gilt             |               36 |              39 |             50,070 |                    667 |
| Spanish Bond          |               45 |              51 |             46,245 |                    481 |
| Simex JGB Bond        |               50 |              70 |             26,562 |                    221 |
| Hang Seng Index       |               19 |              20 |             37,149 |                    952 |
| Dax Index             |               15 |              23 |              9,075 |                    238 |
| Mini S&P              |               56 |              92 |              8,750 |                     59 |
| Mini Russell 2000     |                1 |               4 |              1,809 |                    361 |
| Mini Midcap           |               28 |              44 |              7,589 |                    105 |
| Mini Nasdaq           |               30 |              38 |             20,725 |                    304 |
| Nikkei                |               52 |              53 |             98,675 |                    939 |
| All Trade Average     |            2,976 |           4,137 |          2,756,675 |                    387 |
| Long Trade            |            1,594 |           2,086 |          1,895,123 |                    514 |
| Short Trade           |            1,382 |           2,051 |            861,542 |                    250 |

)

Looking  over  the  performance  by  commodity,  I'd  offer  the  following observations.

- ■ The  grains,  softs,  metals,  energies,  currencies,  and  financials  traded well as groups, while the meats and stock indices did not. This is typical of trend-following strategies. I've never found a good way to trade the meats, and the U.S. stock indices trade more like stocks than commodities.  They are best traded with a counter-trend approach.
- ■ Some commodities like coffee, nickel, the yen, the pound, the euro, the bund, the gilt, and most of the stock indices traded relatively infrequently. This is due to the influence of the volatility filter and the way those commodities are priced by the exchange. When the exchange settles on a dollar-per-point value for a commodity, sometimes they are priced so that a small percentage move causes a large dollar change (see the Relative Contract Risk section in Appendix B). The high-volatility filter will inhibit many of the trades in those commodities.
- ■ The long side makes almost three times as much money as the short side, and the profit-per-trade is almost twice as large. Again, this is typical.

This finishes the development of the commodity strategy. In later chapters we'll wrap money management around it so it fits your account size and risk-taking profile.

## ■ Conclusion

In this chapter, we concluded the development of a stock and a commodity strategy. They both now meet the criteria for being tradeable. For each rule /parameter value a computer run generated trades across the entire basket, and then an equity curve was built. From the equity curve, a gain-to-pain ratio was formed by dividing the average annual profit by the average annual max draw-down. That metric was used to determine whether the rule/parameter was added to the strategy to form a new baseline.  Y ou will have noted along the  way  that  we  rejected  some  solutions  that  increased  profit-per-trade  or total profit because the gain-to-pain metric indicted it wasn't a better solution. Chapter 7 will further address the importance of developing an integrated risk/reward metric like the gain-to-pain ratio instead of total profit or total profit per trade.

## Why  You Should Include Money Management Feedback in Your System Development

W hen I first started  to  develop  trading  systems,  I  used  total  profit or  average  profit-per-trade  as  development  performance  metrics; I  never looked at draw-down during the development process. When the system was finished I'd wrap money management around it and then judge how good it was. As you can see from the last three chapters, I now prefer to  include  a  simple  form  of  money  management  in  each  step  of  the  development process, and my development metric is average profit-per-year divided by average max draw-down per year-the gain-to-pain ratio. Using this process, I know from the start whether the system is tradeable from a risk/reward point of view. Additionally, I don't have to go back during the

107

money management process and see which system element is helping or hurting risk; I've found that out in the development process.

The major advantage of incorporating money management in each step is a better risk-to-reward system. But a side effect is that you can directly compare any type of system against any other with their respective gain-to-pain numbers. You can't do that using total profit and profit-per-trade metrics. With those metrics there's no way to compare longer-term, shorter-term, or scalping systems, and you certainly can't compare commodity, stock, and FX systems.

In this chapter, we'll go through an abbreviated version of the development process on our stock system and commodity systems, but with the development metric being profit-per-trade instead of gain-to-pain. At the end, the equity curves of the two sets of strategies will be compared. I think you'll agree that using a risk/reward metric like the gain-to-pain ratio in your step-by-step development leads to a better solution.

## ■ Development of the Stock System with a Total Profit-per-Trade Metric

Using the long-only Donchian entry, Table 7.1 shows the trading statistics across the 100-stock basket when the Donchian look-back period is varied from 20 days down to 2.

TABLE 7.1

## Profit-per-Trade Metric Development on Stocks: Donchian LookBack in Days

| Look-Back in Days   |   Average Profit-per-Trade ($) |   Average Annual Return ($) |   Average Annual Draw-Down ($) |   Max Draw-Down ($) |
|---------------------|--------------------------------|-----------------------------|--------------------------------|---------------------|
| 20*                 |                             90 |                      42,879 |                         68,393 |             190,044 |
| 18                  |                             87 |                      46,587 |                         70,715 |             184,490 |
| 16                  |                             77 |                      47,079 |                         72,058 |             192,191 |
| 14                  |                             69 |                      48,053 |                         71,727 |             190,794 |
| 12                  |                             61 |                      49,764 |                         69,125 |             191,484 |
| 10                  |                             55 |                      55,171 |                         66,642 |             175,396 |
| 8                   |                             45 |                      56,811 |                         66,607 |             177,774 |
| 6                   |                             35 |                      57,536 |                         69,582 |             150,370 |
| 4                   |                             21 |                      50,516 |                         67,370 |             138,584 |
| 2                   |                             14 |                      55,419 |                         59,321 |             107,455 |

* Baseline The highest profit-per-trade is $90 at a 20-bar look-back, so that's our baseline  entry.  Next,  dollar-based  catastrophic  stops  were  examined  and a dollar stop value of $2,500 increased the profit-per-trade to $98, so that stop was incorporated.  Table 7.2 shows the results with the time-based stop. Exit is accomplished after x days, if the stop hasn't been triggered.

| TABLE 7.2                           | Profit-per-Trade Metric Development on Stocks: Time-Based Exit   | Profit-per-Trade Metric Development on Stocks: Time-Based Exit   | Profit-per-Trade Metric Development on Stocks: Time-Based Exit   |
|-------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
| Exit on Close after x Days, y Value | Exit on Close after x Days, y Value                              | Average Profit-per-Trade ($)                                     | Average Annual Return ($)                                        |
| None*                               |                                                                  | 98                                                               | 46,622                                                           |
| 40                                  |                                                                  | 92                                                               | 46,460                                                           |
| 30                                  |                                                                  | 84                                                               | 45,197                                                           |
| 20                                  |                                                                  | 80                                                               | 49,225                                                           |
| 10                                  |                                                                  | 54                                                               | 42,616                                                           |

* Baseline

With this version of the strategy, the time-based exit didn't increase the profit-per-trade, so it won't be incorporated. With the original stock strategy, dollar-based profit targets made a significant difference.  Table 7.3 shows how they perform on this version.

| TABLE 7.3         | Profit-per-Trade Metric Development on Stocks: Profit Stops   | Profit-per-Trade Metric Development on Stocks: Profit Stops   |
|-------------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Profit Stop Value | Average Profit-per-Trade ($)                                  | Average Annual Return ($)                                     |
| None*             | 98                                                            | 46,622                                                        |
| $2,000            | 100                                                           | 47,626                                                        |
| $1,500**          | 101                                                           | 48,006                                                        |
| $1,000            | 96                                                            | 45,983                                                        |

* Baseline

** New baseline

With a profit stop value of $1,500, profit-per-trade and average profit per year go up marginally from the baseline, so we'll keep it as the new baseline and turn our attention to trading filters.

All the filter types we originally explored were re-examined using a profit-per-trade metric, and none could improve the current baseline with the exception of the look-back filter. The new baseline only takes the signaled trades if current price is above the price of 70 days ago; profit-per-trade improves to $104 per trade. Figure 7.1 shows the resultant equity curve.

FIGURE  7.1 Profi  t-per-Trade Metric Development: Resultant Equity Curve

<!-- image -->

Compare that with the equity curve in Figure   7.2  , which shows the gainto-pain metric development equity curve.

FIGURE  7.2 Gain-to-Pain Metric Development: Resultant Equity Curve

<!-- image -->

Lastly,   7.4 compares year-by-year performance between the two developed strategies.

Clearly the gain-to-pain solution is superior to the profi  t-per-trade solution in both profi  t-per-year and reduced draw-down. Now let's turn to the commodity system and redevelop it using a profi  t-per-trade development metric.

TABLE 7.4

## Comparison of Annual Return and Draw-Down for the Two Stock Strategies

| Year    |   Gain-to-pain-Strategy Profit |   Gain-to-Pain-Strategy Max Draw-Down ($) |   Profit-per-Trade- Strategy Profit ($) |   Profit-per-Trade-Strategy Max Draw-Down ($) |
|---------|--------------------------------|-------------------------------------------|-----------------------------------------|-----------------------------------------------|
| 2000    |                         34,710 |                                    17,431 |                                  26,324 |                                        28,613 |
| 2001    |                         35,731 |                                    24,303 |                                  14,960 |                                        57,379 |
| 2002    |                         34,969 |                                    13,006 |                                  -5,545 |                                        45,790 |
| 2003    |                         90,816 |                                    13,770 |                                  83,318 |                                        18,543 |
| 2004    |                         41,299 |                                    10,566 |                                  29,990 |                                        25,574 |
| 2005    |                         32,259 |                                    12,039 |                                  22,273 |                                        16,780 |
| 2006    |                         37,004 |                                    17,445 |                                  21,576 |                                        24,217 |
| 2007    |                         45,026 |                                    16,569 |                                  48,534 |                                        21,685 |
| 2008    |                        -15,502 |                                    25,461 |                                 -58,155 |                                        70,126 |
| 2009    |                        120,637 |                                    17,596 |                                 132,319 |                                        17,361 |
| 2010    |                         52,424 |                                    28,660 |                                  40,105 |                                        34,206 |
| 2011    |                         25,717 |                                    40,631 |                                  26,546 |                                        43,081 |
| Average |                         44,591 |                                    19,789 |                                  31,854 |                                        33,613 |

## ■ Development of the Commodity System with a Total Profit-per-Trade Metric

Table 7.5 shows the results of reversal trading using a number of Donchian entry look-back periods. Again, we're using a 56-commodity basket with data from 1980 until the end of 2011, and no transaction costs have been included.

TABLE 7.5

## Profit-Per-Trade Metric Development on Commodities: Donchian Look-Back

| Look-Back, Days   |   Average Profit-per-Trade ($) |   Average Annual Return ($) |
|-------------------|--------------------------------|-----------------------------|
| 10                |                            149 |                     135,933 |
| 20                |                            387 |                     169,384 |
| 30                |                            525 |                     150,091 |
| 40                |                            676 |                     141,309 |
| 50                |                            826 |                     136,619 |
| 60                |                            972 |                     132,232 |
| 70                |                          1,153 |                     131,384 |
| 80                |                          1,354 |                     132,660 |
| 90                |                          1,531 |                     133,462 |
| 100               |                          1,692 |                     131,651 |
| 110               |                          2,028 |                     141,089 |
| 120*              |                          2,037 |                     128,895 |
| 130               |                          2,004 |                     116,623 |

* Baseline A look-back of 120 days maximizes the profit-per-trade, so that will form our baseline for development. Next, we look at catastrophic stop levels.

As we did in our previous commodity system development, two volatility-based  catastrophic  stops  were  tested:  average  range  and  standard deviation. For both tests, the 20 days of closing price data prior to entry and the last 120 days of closing price data were used for the computations. The 120-day parameter value was better, as was the catastrophic stop based on standard deviation. Table 7.6 shows the results for multiples of the 120-day standard deviation stop value. Though profit-per-trade didn't actually improve with this stop value, some sort of stop protection is necessary for a longer-term trading system, and this was the best.

TABLE 7.6

## Profit-per-Trade Metric Development on Commodities: Standard Deviation Catastrophic Stop

| Multiple of 120-Day Standard Deviation Value   |   Average Profit-per-Trade ($) |   Average Annual Return ($) |
|------------------------------------------------|--------------------------------|-----------------------------|
| Baseline                                       |                          2,037 |                     128,895 |
| 1                                              |                          1,335 |                     125,631 |
| 2                                              |                          1,879 |                     134,683 |
| 3*                                             |                          2,020 |                     131,906 |

* New baseline

To complete the stop development, trailing stops and profit stops were explored (as was done in Chapter 5), but nothing improved the baseline. Next we'll look at filters.

The first filter explored was the pullback filter we tried on the commodity system in Chapter 6.  The pullback filter waits for a down day to go long, and an up day to go short, if the setup still exists. You'll remember that, for  the  strategy  developed  in  Chapter  6,  the  pullback  filter  did  improve the profit-per-trade but that the gain-to-pain ratio wasn't improved, so we didn't use it as a new baseline.  Table 7.7 shows what happens to our current baseline when the filter is added.

| TABLE 7.7        | Profit-per-Trade Metric Development on Commodities: Pullback Filter   | Profit-per-Trade Metric Development on Commodities: Pullback Filter   |
|------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|
| Pullback Filter? | Average Profit-per-Trade ($)                                          | Average Annual Return ($)                                             |
| None*            | 2,020                                                                 | 131,906                                                               |
| Yes**            | 2,268                                                                 | 129,533                                                               |

The pullback filter improves our profit-per-trade by $148, so it will be added to form the new baseline. Next we'll look at the longer-term trend filter.

The longer-term trend filter inhibits trades that aren't in the same direction as the longer-term trend. We used a comparison of price on the close of the day the signal is issued relative to that x days before to determine the longer-term trend. Since this strategy uses 120 days of information for entry, the comparison date has to be longer than 120 days.  Table 7.8 shows the results when the number of days of look-back is varied.

TABLE 7.8

## Profit-per-Trade Metric Development on Commodities: Longer-Term Trend Filter

| Look-Back, Days   |   Average Profit-per-Trade ($) |   Average Annual Return ($) |
|-------------------|--------------------------------|-----------------------------|
| Baseline          |                          2,268 |                     129,533 |
| 150               |                          2,449 |                     126,803 |
| 175               |                          2,545 |                     124,611 |
| 200*              |                          2,777 |                     130,367 |
| 225               |                          2,768 |                     126,459 |
| 250               |                          2,591 |                     111,997 |

* New baseline

Profit-per-trade peaked at $2,777 when a longer-term trend look-back filter of 200 days was used, so that filter will be added to form the new baseline.

The last set of filters to consider is the low- and high-volatility filters. For the volatility-based range and standard deviation calculations, both 20- and 120-day periods were examined.  Turns out, the average range filter provides better high- and low-volatility performance than the standard deviation filter, and the recent 20-day average range is better than the 120-day average range.  Table 7.9 summarizes the computer runs for the high-volatility filter.

TABLE 7.9

## Profit-per-Trade Metric Development on Commodities: High-Volatility Range-Based Filter

| High-Volatility Average Range Cutoff   |   Average Profit-per-Trade ($) |   Average Annual Return ($) |
|----------------------------------------|--------------------------------|-----------------------------|
| Baseline                               |                          2,777 |                     130,367 |
| 3,500                                  |                          2,741 |                     128,157 |
| 4,000                                  |                          2,805 |                     121,423 |
| 4,500*                                 |                          2,829 |                     132,553 |
| 5,000                                  |                          2,820 |                     132,217 |
| 5,500                                  |                          2,797 |                     131,215 |
| 6,000                                  |                          2,777 |                     130,367 |

* New baseline

Profi  t-per-trade peaked at $2,829 with a high-volatility cutoff   of $4,500, so that condition will be added to form the new baseline. Lastly, Table   7.10 shows the performance of the low-volatility fi  lter.

## TABLE 7.10

## Profit-per-Trade Metric Development on Commodities: LowVolatility Range-Based Filter

| Low-Volatility Average Range Threshold   |   Average Profit-per-Trade ($) |   Average Annual Return ($) |
|------------------------------------------|--------------------------------|-----------------------------|
| Baseline                                 |                          2,829 |                     132,553 |
| 100                                      |                          2,847 |                     131,044 |
| 200*                                     |                          2,938 |                     128,805 |
| 300                                      |                          3,207 |                     120,188 |

The profi  t-per-trade continued to increase for dollar threshold values up to $1,000, but the average annual profi  t continued to drop off   dramatically. Choosing a value of $200 seems a good compromise.

Figure   7.3 shows the equity curve for this strategy:

FIGURE  7.3 Profi  t-per-Trade Metric Development on Commodities: Equity Curve

<!-- image -->

Contrast that with the equity curve shown in Figure   7.4  , which shows the gain-to-pain metric results.

The  graph  using  the  profi  t-per-trade  metric  made  almost  50  percent more than the one using the gain-to-pain ratio, but look at the draw-down spikes you must endure to achieve that profi  t.  Table   7.11 shows a breakout of yearly performance, which further highlights the large draw-downs associated with the profi  t-per-trade solution.

FIGURE  7.4 Gain-to-Pain Metric Development on Commodities: Equity Curve

<!-- image -->

TABLE 7.11

Comparison of Annual Return and Draw-Down for the Two

Commodity Strategies

|   Year |   Gain-to-Pain Strategy Profit ($) |   Gain-to-Pain Max Draw-Down ($) | Profit-per-Trade Strategy Profit ($)   |   Profit-per-Trade Max Draw-Down ($) |
|--------|------------------------------------|----------------------------------|----------------------------------------|--------------------------------------|
|   1980 |                             45,243 |                           31,602 | -20,634                                |                               48,197 |
|   1981 |                            131,473 |                           35,973 | 195,283                                |                               44,209 |
|   1982 |                             70,948 |                           26,559 | 99,666                                 |                               41,161 |
|   1983 |                             60,062 |                           20,128 | 14,660                                 |                               43,403 |
|   1984 |                             75,650 |                           23,651 | 96,216                                 |                               35,092 |
|   1985 |                             80,800 |                           30,075 | 113,859                                |                               51,230 |
|   1986 |                             72,105 |                           42,244 | 61,105                                 |                               72,106 |
|   1987 |                            176,109 |                           33,076 | 155,198                                |                               66,272 |
|   1988 |                            140,708 |                           19,920 | -4,0271                                |                               65,527 |
|   1989 |                             72,787 |                           32,454 | 87,038                                 |                               42,337 |
|   1990 |                            149,391 |                           22,837 | 92,010                                 |                               57,057 |
|   1991 |                            103,496 |                           23,260 | -11,860                                |                               92,243 |
|   1992 |                             71,787 |                           27,965 | 18,887                                 |                               76,545 |
|   1993 |                            174,368 |                           16,375 | 156,109                                |                               40,861 |
|   1994 |                             74,961 |                           35,434 | 96,750                                 |                               84,190 |

( continued )

TABLE 7.11

Continued

| Year    |   Gain-to-Pain Strategy Profit ($) |   Gain-to-Pain Max Draw-Down ($) |   Profit-per-Trade Strategy Profit ($) |   Profit-per-Trade Max Draw-Down ($) |
|---------|------------------------------------|----------------------------------|----------------------------------------|--------------------------------------|
| 1995    |                            107,427 |                           41,515 |                                 80,867 |                               88,142 |
| 1996    |                             70,475 |                           34,187 |                                149,757 |                               64,542 |
| 1997    |                            111,771 |                           25,842 |                                157,502 |                               61,754 |
| 1998    |                             77,517 |                           33,384 |                                192,008 |                              105,575 |
| 1999    |                             40,987 |                           72,809 |                                160,316 |                               67,830 |
| 2000    |                            107,739 |                           13,563 |                                110,083 |                              117,708 |
| 2001    |                             49,441 |                           44,766 |                                 93,492 |                              121,311 |
| 2002    |                             77,130 |                           36,383 |                                143,004 |                               85,687 |
| 2003    |                            131,397 |                           36,355 |                                261,307 |                              125,771 |
| 2004    |                             47,863 |                           35,843 |                                 74,288 |                              159,238 |
| 2005    |                             90,391 |                           22,619 |                                137,495 |                               77,703 |
| 2006    |                             60,636 |                           36,073 |                                242,635 |                              291,045 |
| 2007    |                             77,027 |                           23,311 |                                159,792 |                              255,655 |
| 2008    |                            172,057 |                           38,758 |                                765,671 |                              336,827 |
| 2009    |                             25,429 |                           21,180 |                                -69,453 |                              454,177 |
| 2010    |                             56,932 |                           19,557 |                                306,867 |                              292,316 |
| 2011    |                            -34,366 |                           46,111 |                                 42,126 |                              401,255 |
| Average |                             86,639 |                           31,369 |                                128,805 |                              123,968 |

(

)

Table 7.11 shows that the average max draw-down for the profit-pertrade-metric strategy is almost four times as large as that of the gain-topain metric strategy. And the max draw-down of $454,177 for the profitper-trade-metric strategy is over six times as large as the $72,809 max draw-down for the gain-to-pain-metric strategy.

One last note for those who choose to develop commodity strategies: Over the 12-year period from 2000 to 2011, the profit-per-trade-metric strategy, which was developed without any consideration of risk, had 10 years with a max draw-down of $100,000 or more. In the 20 years before the year 2000, there was only one year where draw-down exceeded $100,000 (1998). This highlights the changing nature of commodity trading.  V olatility is much higher than it has ever been. And judging by the string of $200,000+ draw-down years from 2006 through 2011, volatility is still increasing. Y ou just have to develop strategies with a metric that includes risk.

## ■ Conclusion

In this chapter, the stock and commodity strategies were redeveloped using a  profit-per-trade  metric.  In  both  cases,  the  redeveloped  strategies  were inferior to the baselines in equity curve appearance and gain-to-pain ratio. In particular, the redeveloped commodity strategy suffered from the lack of a risk metric in development.

There is still work to do with these strategies. Money management overlays  will  be  applied  in  Chapters 12 through 15. But now let's turn to an exciting new way to develop strategies: bar scoring.

## Bar-Scoring: A New Trading Approach

T raditional system development has an obvious  drawback:  rules  are black or white; you can only enter when the entry logic conditions are  fully  met,  and  only  exit  when  an  exit  logic  condition  is  fully  met. There are no shades of gray like: this is a weak entry; this is a very strong entry; or this is a good entry even though one logic condition isn't met. In this chapter, I'll introduce a new system development approach I call bar-scoring,  which  grades  every  instrument's  profit  potential  each  bar. Each bar is scored using any number of user-defined criteria; the score is the expected value of the profit in a user-defined number of days after entry. When  the  bar  scores  high  the  chances  of  an  upward  move  are  good; when  the  bar  scores  low  the  chances  of  a  downward  move  are  good. Bar-scoring  can  be  used  as  a  standalone  entry  technique,  an  exit  technique, or as an aid to other entry criteria.

This chapter will introduce bar-scoring, provide a number of examples of scoring criteria, and outline the scoring process. After this introduction, a system will be developed on stock market daily-bar data.  That system will use bar-scoring as the final selection criteria for a group of possible trades selected by a traditional entry technique. The issue of curve-fitting will be addressed with the system by doing a BRAC test.

119

## ■ The Shortcoming of Traditional System Design Is Rigid Rules

In the Donchian system developed in Chapter 7, we used the Donchian 20-day high/low criteria, a 70-day trend filter, and a high-volatility filter to signal entry. If an instrument meets the criteria on a given day, a trade is entered. If it doesn't meet every criterion, it is bypassed. What if 100 instruments meet the entry conditions today? Is any set of entries better than another? Not by the rigid rules of traditional design. How about if an instrument's close above a 20-day high was also a close above an all-time high, but the volatility was $1 too high? Wouldn't that make a good entry? Bar-scoring is a way to quantify potential entries without requiring that specific entry criteria be met.

## ■ Introduction to Bar-Scoring

Bar-scoring  is  an  objective  way  to  classify  an  instrument's  movement potential every bar. The two parts to bar-scoring are the criterion and the resultant profit X days hence. Both the criterion and the number of days to measure profit are user-defined. Suppose you decide to use a 14-bar RSI as the criterion, and three days after entry as the point to measure profit.  You'd calculate the 14-bar RSI for each bar and tag that RSI value with the profit three days later, as if you' d entered a long trade on the open of the bar after the RSI bar.  Then you could sort the historical results by RSI value, keeping that RSI value with its profit that three-day period, from top to bottom into a number of bins. Each bin should contain an equal number of RSI samples. The results might look something like those is Table 8.1 for the NASDAQ 100 stocks from the year 2000 through the end of 2011.

| TABLE 8.1               | Bar-Scoring NASDAQ Stocks by 14-Day RSI and 3-Day Return   | Bar-Scoring NASDAQ Stocks by 14-Day RSI and 3-Day Return   | Bar-Scoring NASDAQ Stocks by 14-Day RSI and 3-Day Return   |
|-------------------------|------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|
| RSI Score               |                                                            | Number of Samples                                          | Average % Return in Three Days                             |
| Greater than 64.68      | Greater than 64.68                                         | 30,000                                                     | - 0.15                                                     |
| Between 60.12 and 64.68 | Between 60.12 and 64.68                                    | 30,000                                                     | - 0.13                                                     |
| Between 56.94 and 60.12 | Between 56.94 and 60.12                                    | 30,000                                                     | - 0.08                                                     |
| Between 54.30 and 56.94 | Between 54.30 and 56.94                                    | 30,000                                                     | - 0.06                                                     |
| Between 51.89 and 54.30 | Between 51.89 and 54.30                                    | 30,000                                                     | - 0.03                                                     |
| Between 49.54 and 51.89 | Between 49.54 and 51.89                                    | 30,000                                                     | - 0.01                                                     |
| Between 45.69 and 49.54 | Between 45.69 and 49.54                                    | 30,000                                                     | 0.01                                                       |
| Between 42.42 and 45.69 | Between 42.42 and 45.69                                    | 30,000                                                     | 0.04                                                       |
| Between 37.08 and 42.42 | Between 37.08 and 42.42                                    | 30,000                                                     | 0.11                                                       |
| Less than 37.08         | Less than 37.08                                            | 30,000                                                     | 0.17                                                       |

Table 8.1 shows the counter-trend nature of NASDAQ stocks. When the RSI is low , the stocks tend to rally, and when the RSI is high, the stocks tend to pull back.  Y ou could use a seven-day RSI criterion and a one-day return, or a 50-day RSI criterion and a 10-day return. Everything is user-defined.

Bar-scoring is most powerful when a number of independent measures are used and the results combined to form an aggregate bar score.  Y ou can cover different time frames by using lengths varying from short-term to long-term like a 3-day , 14-day , and 40-day RSI as criteria. Or you can use different stock properties like volume and acceleration as criteria. If more than one criterion is used, all have to use the same number of bars from entry as the profit measure to be meaningful. The sum of the individual scores is the score for that bar, and that score divided by the number of criteria that comprise it is the expected value of profit that many days in the future, had a trade been placed on the next open. High scores should be traded long, and low scores are shorting opportunities.  The bar score can also be used as an exit technique. If you're in a long position and the bar score is very low , exit the trade.

On the scoring side, if you're looking to trade short-term, measure the performance short-term-a one-, two-, or three-bar change. That doesn't mean you are limited to short-term criteria; you can use a 40-day RSI with the one-, two-, or three-day return. If you want to trade longer-term, measure the return 20, 40, or even more bars out.  You are limited only by your imagination. But the scores in the resultant bins tell you how good a job you did.  Y ou want separation-a wide range of values from the top scoring bin to the bottom scoring bin. If the range from biggest return to the largest loser is small, the criterion, or the number of days chosen for profit, isn't good and won't help much in picking out good bars to trade long or short.

Scoring can also be done with other strategy elements you are comfortable trading. I short-term trade in stocks by buying dips and using a profit target on the first day after entry. If the profit target is not hit, I get out on the open of the second day. I can trade with those exit rules, assuming I get in long at the open each day with the best bar-scoring stocks instead of buying the dip.  This gives me the benefit of an exit strategy I like.

Bar-scoring is applicable to any asset class, but in my opinion, it works best when there are a lot of instruments. In the commodity world, there are fewer than 100 liquid instruments. If you use bar-scoring to determine the best signals each bar, you'll only have a couple, at most, to choose from; same thing in foreign exchange (FX). But there are thousands of highly liquid U.S. stocks. Most systems will generate a bunch of trades each bar . Scoring those trades allows you to quantify the best of the best. Or , you can build a bar-scoring standalone system, because with all the candidates, something will surely have a high score each bar .

## ■ Bar-Scoring Examples

Like any other technique, you need a lot of samples to minimize curve-fi  tting. In this section, we'll look at some examples using both stocks and commodities. For the stock examples, continuous contract, daily-bar data on a basket of  3,372  stocks  going  back  to  the  year  2000  was  used. Across  these  data, there are about 3,500,000 bars of data where stock liquidity was greater than $20,000,000. For commodities, we'll use continuous contract, daily-bar data on a basket of 56 going back to 1980.  Across these data there are about 363,000 bars of data through the end of the year 2011. In both the stock and commodity examples, we'll break the scoring results into equal-size bins, as was done in the RSI example earlier in this chapter, but instead of using 10 bins, as was done in that example, we'll use 20 bins going forward, unless otherwise noted. In reality , the more bins you have the better.  The only constraint is that there are enough samples in each bin to minimize curve-fi  tting-many, many thousand.

## Scoring by a Bar  T ype Criterion

There are a number of ways to classify a bar. Candlesticks are one, and the relationship  of  the  open,  high,  low ,  and  close  is  another.  I  break  the  bar down into the relationship of the close to the open in one of four ways: close greater than open, and close in the upper half of the range; close greater than open, and close in the lower half of the range; close less than or equal to open, and close in the upper half of the range; and close less than or equal to open, and close in the lower half of the range. I extend the total number of categories from four to eight by adding the relationship of the close of the bar to yesterday's close.  The eight bar types are illustrated in Figure   8.1  .

FIGURE  8.1 Scoring by Bar Type

<!-- image -->

Table 8.2 shows bar type results for both stocks and commodities when the scoring metric is return the following day. For stocks, the profit is calculated as the percent change of the next bar's close relative to its open, and for commodities the profit is the dollar change of the next bar's close versus its open.

TABLE 8.2

## Bar-Scoring Example on Stock and Commodity Data by the Type of Daily Bar

| Stock Bar Type Breakout   | Stock Bar Type Breakout   | Commodity Bar Type Breakout   | Commodity Bar Type Breakout   |
|---------------------------|---------------------------|-------------------------------|-------------------------------|
| Bar Type                  | Percent Return            | Bar Type                      | Dollar Return                 |
| 1                         | -0.008                    | 1                             | -10.92                        |
| 2                         | 0.0054                    | 2                             | -3.32                         |
| 3                         | -0.0050                   | 3                             | -1.00                         |
| 4                         | 0.1045                    | 4                             | 7.49                          |
| 5                         | 0.0008                    | 5                             | 9.35                          |
| 6                         | -0.0007                   | 6                             | 12.66                         |
| 7                         | -0.0041                   | 7                             | 18.63                         |
| 8                         | 0.0038                    | 8                             | 16.04                         |

The returns on the stock side are relatively small, though bar-type 4 might be useful. On the commodity side, it's interesting to note that bar-types 5 through 8 all have a positive return, but in each case the close was less than yesterday's close.  This shows that although commodities trend on daily bars in the mid- to longer-term time frame, on a one-day basis they are counter-trend. Three of the four bar types that have an up close go down the next day.

## Scoring by the Number of Standard Deviations of Closing Price above/below Average Criterion

For each bar the standard deviation of closing price for the last 20 days is computed. Then the average of the last 20 closing-price bars is subtracted from the last closing price. This difference is divided by the standard deviation value to provide the number of standard deviations that the last closing price  is  above  or  below  the  20-day  average  price;  that  is  the  bar-scoring criterion. Table 8.3 shows price standard deviation results for both stocks and commodities when the profit is return five days after entry.

| Stock Num SD above/below Average   | Stock Num SD above/below Average   | Commodity Num SD above/below Average   | Commodity Num SD above/below Average   |
|------------------------------------|------------------------------------|----------------------------------------|----------------------------------------|
| Number of Standard Deviations      | Percent Return                     | Number of Standard Deviations          | Dollar Return                          |
| Greater than 2.10                  | -0.141                             | Greater than 2.03                      | 44.98                                  |
| Between 1.79 and 2.10              | -0.106                             | Between 1.74 and 2.03                  | 15.38                                  |
| Between 1.57 and 1.79              | -0.072                             | Between 1.52 and 2.03                  | 48.60                                  |
| Between 1.39 and 1.57              | -0.005                             | Between 1.33 and 2.03                  | 43.63                                  |
| Between 1.22 and 1.39              | 0.086                              | Between 1.14 and 1.33                  | 57.90                                  |
| Between 1.05 and 1.22              | 0.117                              | Between 0.95 and 1.14                  | 35.97                                  |
| Between 0.87 and 1.05              | 0.166                              | Between 0.75 and 0.95                  | 53.40                                  |
| Between 0.68 and 0.87              | 0.220                              | Between 0.53 and 0.75                  | 29.32                                  |
| Between 0.47 and 0.68              | 0.191                              | Between 0.30 and 0.53                  | 48.45                                  |
| Between 0.24 and 0.47              | 0.200                              | Between 0.05 and 0.30                  | 41.22                                  |
| Between 0.03 and 0.24              | 0.157                              | Between -0.20 and 0.05                 | 37.29                                  |
| Between -0.24 and 0.03             | 0.155                              | Between -0.44 and -0.20                | 10.70                                  |
| Between -0.48 and -0.24            | 0.126                              | Between -0.66 and -0.44                | -22.67                                 |
| Between -0.71 and -0.48            | 0.135                              | Between -0.86 and -0.66                | -11.85                                 |
| Between -0.93 and -0.71            | 0.164                              | Between -1.06 and -0.86                | -28.85                                 |
| Between -1.16 and -0.93            | 0.222                              | Between -1.25 and -1.06                | -26.17                                 |
| Between -1.38 and -1.16            | 0.380                              | Between -1.45 and -1.25                | -4.86                                  |
| Between -1.64 and -1.38            | 0.513                              | Between -1.68 and -1.45                | -10.35                                 |
| Between -1.99 and -1.64            | 0.485                              | Between -1.99 and -1.68                | -15.58                                 |
| Less than -4.23                    | 0.162                              | Less than -3.73                        | -13.19                                 |

When looking at these tables it is important to remember two things: The bins in the respective stock and commodity categories each contain the same number of trades, and all the days of stock history where liquidity is greater than  $20,000,000  are  represented,  as  is  every  day  that  every  commodity traded.  Looking  at  the  information  in T able  8.3,  a  number  of  interesting observations can be made on both the stock and commodity side. For stocks:

- ■ The counter-trend nature of stocks is evident.  The most positive five-day return bins occur when the standard deviation is strongly negative, as indicted by large negative SD values, and the strongest negative returns occur when price is strongly moving up, as is evident with strongly positive SD numbers.
- ■ Across all the five-day trades, the relentless upward bias of stocks can be seen: Sixteen of the bins have an average trade expectation that is positive

over five days, while only four have a negative trade expectation over five days. Also, the strongest positive expected value trade bin has a return of 0.513 percent, which is over three times the magnitude of the largest losing trade expected value of -0.141.

For commodities:

- ■ The trend-following nature of commodities is evident. Positive returns generally occur when SD is positive, and negative returns generally occur when the SD is negative. But there is a difference from stocks: The strongest returns are not at the extreme bins. The largest positive return occurs in the fifth bin down, while the largest negative return occurs in the sixth bin from the bottom.  Think about how this differs from conventional system development; we never tested for long commodity trades anywhere but near the top of the performance indicator, or short commodity trades anywhere but at the bottom extreme of an indicator. Barscoring picks out the best and worst performance, wherever it occurs.
- ■ The upward bias  is  evident  because  12  of  the  20  bins  have  a  positive return expectation.

Next let's look at a volume criterion for bar-scoring.

## Scoring by Number of Standard Deviations of Volume above/below Average Criterion

The computations for this criterion are the same as in the previous section, but volume is used instead of closing price. For commodities, the volume measure is volume across all contracts.  Table 8.4 shows the results when the last 20 days of volume are used in the standard deviation calculations and profit is calculated five days after entry.

Volume is a measure seldom talked about in the trading literature, but Table 8.4 shows that it can show opportunity. In stocks, those companies whose volume is one standard deviation or more below average can expect, on average, to see a two- to four-times-greater appreciation over the next five days than the others. And in commodities, high volume (bins 1 and 2) and  very  low  volume  (bin  20)  are  good  predictors  of  a  rise  in  price.  In fact, the best commodity bin in the price-based standard deviation case was $57.90, while volume bin 2 had a return of $58.

In  the  next  section,  we'll  develop  a  short-term  stock  system  using bar-scoring.

<!-- image -->

| Stock Num SD of Volume above/below Average   | Stock Num SD of Volume above/below Average   | Commodity Num SD of Volume above/below Average   | Commodity Num SD of Volume above/below Average   |
|----------------------------------------------|----------------------------------------------|--------------------------------------------------|--------------------------------------------------|
| Number of Standard Deviations                | Percent Return                               | Number of Standard Deviations                    | Dollar Return                                    |
| Greater than 2.27                            | 0.138                                        | Greater than 2.09                                | 42.43                                            |
| Between 1.55 and 2.27                        | 0.159                                        | Between 1.55 and 2.09                            | 58.00                                            |
| Between 1.11 and 1.55                        | 0.140                                        | Between 1.18 and 1.55                            | 17.27                                            |
| Between 0.80 and 1.11                        | 0.130                                        | Between 0.90 and 1.18                            | 35.13                                            |
| Between 0.57 and 0.80                        | 0.102                                        | Between 0.66 and 0.90                            | 13.07                                            |
| Between 0.37 and 0.57                        | 0.159                                        | Between 0.46 and 0.66                            | 37.37                                            |
| Between 0.21 and 0.37                        | 0.115                                        | Between 0.28 and 0.46                            | 19.58                                            |
| Between 0.07 and 0.21                        | 0.157                                        | Between 0.12 and 0.28                            | 20.15                                            |
| Between -0.06 and 0.07                       | 0.123                                        | Between -0.02 and 0.12                           | 8.16                                             |
| Between -0.16 and -0.06                      | 0.155                                        | Between -0.16 and -0.02                          | -5.24                                            |
| Between -0.27 and -0.16                      | 0.128                                        | Between -0.28 and -0.16                          | -13.71                                           |
| Between -0.36 and -0.27                      | 0.135                                        | Between -0.40 and -0.28                          | 4.78                                             |
| Between -0.45 and -0.36                      | 0.166                                        | Between -0.51 and -0.40                          | -11.01                                           |
| Between -0.55 and -0.45                      | 0.129                                        | Between -0.62 and -0.51                          | -4.28                                            |
| Between -0.66 and -0.55                      | 0.116                                        | Between -0.73 and -0.62                          | 16.24                                            |
| Between -0.75 and -0.66                      | 0.148                                        | Between -0.85 and -0.73                          | 8.39                                             |
| Between -0.87 and -0.75                      | 0.160                                        | Between -0.98 and -0.85                          | 4.41                                             |
| Between -1.03 and -0.87                      | 0.193                                        | Between -1.14 and -0.98                          | 22.81                                            |
| Between -1.25 and -1.03                      | 0.186                                        | Between -1.37 and -1.14                          | 8.55                                             |
| Less than -3.66                              | 0.417                                        | Less than -3.29                                  | 52.45                                            |

## ■ Example Stock System: Bar-Scoring with Defined Criteria

An effective way to use bar-scoring is as an adjunct to a fairly good entry.  The fairly good entry should generate a number of trades each bar. Bar-scoring then ranks the trades from top to bottom, and you only trade the best signals. Let's look at using standard deviation as our fairly good entry for a longonly stock system. We know that using daily-bar data stocks tend to move in a counter-trend manner. So we'll look to buy stocks whose last close is some number of standard deviations below their recent average price. Let's look at 10-day standard deviation and 20-day standard deviation to start. The results of entering on the next open and exiting on the open two days later for stocks meeting the standard deviation criteria are shown in  T able 8.5.

TABLE 8.5

|   Number of Days for SD and Average |   Number of Standard Deviations below Average for Entry on Next Open |   Average Percentage Profit-per-Trade |   Average Number of Trades per Day |
|-------------------------------------|----------------------------------------------------------------------|---------------------------------------|------------------------------------|
|                                  20 |                                                                  0.5 |                                 0.151 |                                324 |
|                                  20 |                                                                 0.75 |                                 0.173 |                                273 |
|                                  20 |                                                                  1.0 |                                 0.215 |                                220 |
|                                  20 |                                                                 1.25 |                                 0.265 |                                166 |
|                                  20 |                                                                 1.50 |                                 0.308 |                                117 |
|                                  10 |                                                                  0.5 |                                 0.223 |                                331 |
|                                  10 |                                                                 0.75 |                                 0.250 |                                275 |
|                                  10 |                                                                  1.0 |                                 0.288 |                                217 |
|                                  10 |                                                                 1.25 |                                 0.317 |                                157 |
|                                  10 |                                                                 1.50 |                                 0.327 |                                101 |

It's clear that using 10 days for the standard deviation is the better number to use for the two-day trade. The number of trades per day is about the same as the corresponding 20-day entry point, but the profit is higher in all cases. We'll use the 1.0 standard deviation point below the 10-day average  as  our  baseline  and  see  if  bar-scoring  can  significantly  improve profit-per-trade.

Using 10 days and one standard deviation below the average as entry criteria, there were 595,806 trades, which averaged 0.288 percent per trade. Some may question whether it's worth pursuing a strategy that yields such a low profit-per-trade. Since the trades last two days, you can trade about 125 two-day cycles in a year. Before compounding, that's 125 cycles per year times 0.288 percent per cycle, or 36 percent per year, before slippage and commission costs. In the previous calculations, no leverage was used. With 100 percent leverage, that number doubles to 72 percent per year. With compounding (as the account grows continue to trade the entire amount each cycle) the non-margined and margined cases grow to 43 percent and 105 percent, respectively. That's a very healthy return and, even with slippage and commission, it's probably worth trading if the risk side is relatively benign.

If we use 20 bins for our bar-scoring criteria, the 595,806 trades break down to about 30,000 samples per bin.  That's probably enough to minimize curve-fitting. But at the end of system development, we'll do a curve-fitting check with the BRAC procedure.

Our defined  entry  criterion  uses  price  action  over  10  days.  Let's  use two more price criteria to define how weak each trade actually is: a 10-day standard deviation measure and a 20-day standard deviation measure. Let's add a volume measure: the 20-day standard deviation of volume. We'll add one  volatility  measure:  the  10-day  standard  deviation  of  range,  normalized by price. And lastly, our eight-bin breakdown of bar type.  That's a total of five criteria to characterize each bar. Table 8.6 shows the resultant bins across the 595,806 trades.

The  numbers  that  are  in  bold  represent  performance  that's  greater than the overall average trade for the entry alone, which is 0.288 percent return-per-trade. The  other  numbers  are  penalty  numbers;  they  are  less than the 0.288 average. Since every bar receives a score from each of the five criteria, the highest ranking symbols each day are those that get a lot of above-average contributions and few less-than-average contributions. Note that the highest score a bar can achieve is the sum of the highest returns in each column: 0.387 + 0.418 + 0.535 + 1.768 + 0.475 = 3.583. Across the 585,806 bars, that score was never achieved.

The criteria reveal a lot about the stock market when short-term trading with daily bars:

- ■ Weak stocks with a high volatility have huge upside potential. The top 5 percent (bin 1) average a 1.768 percent gain over the next two days. And the lower the volatility, the worse the two-day returns, with the lowest 80 percent (bins 5 through 20) greatly underperforming the 0.288 percent return average.
- ■ The weaker the stock, as measured by the two standard deviations of price metrics, the better the performance, up to a point. Notice that the bottom 5 percent in each of those columns (last bin) underperform the 0.288 percent average performance. It probably means that some of the weakest stocks are really losers and won't bounce the way the other weak stocks do.
- ■ High  relative  volume  is  good,  except  when  volume  approaches  three standard deviations above the average; maybe those are being dumped. And low relative volume is good; maybe the strong hands know those aren't likely to fall further, so they don't sell.
- ■ Weak 10-day stocks that aren't weak 20-day stocks outperform as shown  by  bins  1  and  2  of  the  20-day  standard  deviation  of  price metric.

TABLE 8.6 Bar-Scoring Matrix: Five Criteria, Profit Two Days after Entry

| Bar Type                                                     | % Return         |   0.008 |   0.244 |   0.196 |   0.312 |   0.142 |   0.475 |   0.233 |   0.300 | N/A   | N/A   | N/A   | N/A         | N/A         | N/A         | N/A   | N/A     | N/A N/A   | N/A   | N/A   |
|--------------------------------------------------------------|------------------|---------|---------|---------|---------|---------|---------|---------|---------|-------|-------|-------|-------------|-------------|-------------|-------|---------|-----------|-------|-------|
| Daily                                                        | Bar Type Bin     |       1 |       2 |       3 |       4 |       5 |       6 |       7 |       8 | N/A   | N/A   | N/A   | N/A         | N/A         | N/A         | N/A   | N/A N/A | N/A       | N/A   | N/A   |
| Standard Deviation of Divided by Closing Price               | % Return         |   1.768 |   0.581 |   0.357 |   0.305 |   0.214 |   0.264 |   0.176 |   0.209 | 0.212 | 0.172 | 0.153 | 0.152       | 0.158 0.172 | 0.135       | 0.160 | 0.152   | 0.160     | 0.134 | 0.112 |
| 10-day Range                                                 | Range Bin        |   0.092 |   0.069 |   0.058 |   0.051 |   0.046 |   0.042 |   0.038 |   0.036 | 0.033 | 0.031 | 0.029 | 0.027 0.025 | 0.023       | 0.021       | 0.019 | 0.018   | 0.016     | 0.013 | 0.001 |
| Standard Deviations Volume Average                           | % Return         |   0.256 |   0.439 |   0.360 |   0.405 |   0.302 |   0.286 |   0.250 |   0.265 | 0.241 | 0.206 | 0.152 | 0.218       | 0.184 0.221 | 0.223       | 0.236 | 0.264   | 0.313     | 0.390 | 0.535 |
| Number of above the 20-Day                                   | SD of Volume Bin |    2.72 |    2.02 |    1.58 |    1.25 |    0.99 |    0.77 |    0.58 |    0.41 | 0.26  | 0.12  | -0.01 | -0.11       | -0.23 -0.34 | -0.45       | -0.57 | -0.70   | -0.86     | -1.09 | -2.93 |
| Number of Standard Deviations below the 20-Day Price Average | % Return         |   0.403 |   0.333 |   0.279 |   0.191 |   0.187 |   0.149 |   0.146 |   0.271 | 0.304 | 0.265 | 0.314 | 0.298       | 0.252       | 0.249 0.309 | 0.354 | 0.367   | 0.401     | 0.418 | 0.258 |
|                                                              | SD of Price Bin  |   -0.09 |    0.20 |    0.47 |    0.73 |    0.94 |    1.12 |    1.25 |    1.35 | 1.44  | 1.52  | 1.60  | 1.67        | 1.74 1.82   | 1.91        | 2.01  | 2.13    | 2.28      | 2.52  | 4.20  |
| Standard Deviations Price Average                            | % Return         |   0.151 |   0.219 |   0.214 |   0.181 |   0.238 |   0.324 |   0.243 |   0.278 | 0.294 | 0.315 | 0.320 | 0.380 0.341 | 0.387       | 0.368       | 0.361 | 0.359   | 0.302     | 0.307 | 0.160 |
| Number of below the 10-Day                                   | SD of Price Bin  |    1.04 |    1.09 |    1.14 |    1.18 |    1.23 |    1.27 |    1.31 |    1.36 | 1.41  | 1.46  | 1.51  | 1.57 1.63   | 1.69        | 1.76        | 1.84  | 1.93    | 2.04      | 2.22  | 2.84  |

BAR-SCORING: A NEW TRADING APPROACH

After each bar is scored by summing the contributions of the five criteria, the 585,806 bars are sorted by date, and then by score on the date. Table  8.7  shows  performance  across  the  top x scoring  trades  each  day. Sometimes there aren't x trades  on  a  given  day  because  there  aren't  that many stocks trading at one standard deviation below the 10-day average.  The percent of days that x trades occurs is also shown in the table.

TABLE 8.7

Bar-Scoring System: Performance by Top T rades per Day

|   Top Number of Trades Each Day |   Percent of Days the Number of Trades Occurs |   Average Percent Return-per-Trade |
|---------------------------------|-----------------------------------------------|------------------------------------|
|                               1 |                                           100 |                              0.739 |
|                               5 |                                          99.9 |                              0.509 |
|                              10 |                                          99.8 |                              0.441 |
|                              20 |                                          98.8 |                              0.398 |
|                              50 |                                          90.1 |                              0.352 |
|                             100 |                                          66.8 |                              0.318 |

x

In each of these cases, the average percent return-per-trade well exceeds our 0.288 percent average, so bar-scoring does allow us to significantly outperform the basic strategy.

Table 8.8 shows return and risk metrics when a simple form of money management is used: We'll trade x positions at a time by entering half of x positions each day at a position size of total equity divided by x . So if our starting equity is $50,000 and we want to trade 10 positions at a time, we buy five $5,000 positions on the first day, and five $5,000 positions on the second day. That has us fully invested, but not leveraged. Every succeeding day, five positions are exited and five new positions are entered at a position size of equity divided by 10.

| TABLE 8.8                 | Bar-Scoring System: Annual Performance for x Trades per Day   | Bar-Scoring System: Annual Performance for x Trades per Day   | Bar-Scoring System: Annual Performance for x Trades per Day   |
|---------------------------|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Number of Trades Each Day | Average Annual Percent Return                                 | Max Percent Draw-Down                                         | Average of 20 Largest Draw-Downs                              |
| 1                         | 90.6                                                          | 68.2                                                          | 39.3                                                          |
| 5                         | 52.4                                                          | 52.5                                                          | 26.9                                                          |
| 10                        | 46.1                                                          | 51.6                                                          | 22.7                                                          |
| 20                        | 48.2                                                          | 47.8                                                          | 21.1                                                          |
| 50                        | 47.2                                                          | 44.5                                                          | 18.2                                                          |

Table 8.8 shows that return and draw-down diminish as the number of trades each day goes from one to 10. From 10 to 50, the return stays about the same but draw-down continues to go lower. At 50 trades each day, we have a pretty good trading solution; the return is over 2.5 times greater than the average max draw-down, and it is also bigger than the max draw-down over the time frame. For those want smaller draw-downs, trade some fraction of the total equity instead of all of it.

## ■ Is Bar-Scoring Curve-Fitting?

In the previous example, we used all the data to build the scoring metrics  and  then  went  back  over  all  the  data  and  scored  each  bar. When we scored the first bar, we used all the bars we hadn't seen yet in real trading  to  assign  its  score.  Obviously,  this  is  curve-fitting;  we're  taking advantage of information that isn't available yet. So the question is: How bad is it? To answer that question, a BRAC test was done. Doing the  same  development  that  was  done  in  the  last  section,  the  strategy was redeveloped, but all the 2011 stock data was withheld. Then the curve-fit 2010 results from the original strategy were compared with the out-of-sample results for 2010 that were obtained with the redeveloped strategy on 2000 through 2010 data. Table 8.9 shows the results.

<!-- image -->

## Out-of-Sample BRAC Test Results versus Curve-Fit Results on Year 2011 Data

| Top Number of Trades Each Day   |   2011 Average Percent Return-per-Trade with Curve-Fit Strategy |   2011 Average Percent Return-per-Trade with Out-of-Sample Strategy |
|---------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------------|
| 1                               |                                                           0.143 |                                                               0.183 |
| 5                               |                                                           0.510 |                                                               0.433 |
| 10                              |                                                           0.486 |                                                               0.304 |
| 20                              |                                                           0.371 |                                                               0.382 |
| 50                              |                                                           0.306 |                                                               0.297 |
| 100                             |                                                           0.230 |                                                               0.231 |
| Average                         |                                                           0.341 |                                                               0.305 |

With the exception of the top 5 and top 10 trades' results, the two sets match up pretty well. Maybe the best comparison is the average line. The curve-fit  solution  outperforms  the  out-of-sample  data  strategy  by  about 12 percent.  There is an element of curve-fitting, but it probably inflates performance by only 10 to 15 percent.

## ■ Conclusion

A new strategy development tool was introduced in this chapter: bar-scoring. Bar-scoring  assigns  a  profit  expectation  to  each  bar  by  using  a  large  set of  similar  setups  and  their  average  return  over  the  expectation  period. Bar-scoring can be used for entries, for exits, or as an adjunct to some specific entry logic.

Bar-scoring does have a degree of inherent curve-fitting, but a BRAC test can give a fair estimate of the degree of overfitting.

## Avoid Being Swayed by the 'Well-Chosen Example'

J ack  Schwager  is  a  giant  in  the  futures  industry.  I  consider  his  book A Complete Guide to the Futures Markets to  be the most comprehensive and definitive  publication  on  futures  analysis  ever  written.  And  his  Market Wizard series of books show, in an entertaining way, that there are many ways to make money trading. But when I hear his name, the one thing that jumps to mind is what he had to say in an article for Futures magazine titled 'The Well-Chosen Example.'

If  you've  read  any  books  on  trading,  you've  run  across  it: The  author makes an authoritative statement like 'always look to fade the gap' or 'always look to trade in the direction of the trend,' and then shows a chart that has three perfect examples making his point. That's it-the total extent of the proof. Don't be taken in. Just because it's stated in print doesn't make it true. If you're going to be one of those who makes money trading, you need to question everything. This is a fun chapter for me because I'm going to question some of the repeating themes, and instead of using one chart to prove or disprove the claim, I'll be looking for a large body of trades to provide the answer.

## ■ A Divergence Is a Strong Signal

This is my favorite. I've seen this so many times in print, it just has to be true. A  divergence  occurs  when  price  makes  a  new  high  or  low ,  but  an accompanying momentum indicator doesn't. Commonly used momentum indicators  are  stochastics,  relative  strength  index  (RSI),  moving  average convergence divergence (MACD), and momentum itself. Divergence buy and sell signals look like the graphics in Figure 9.1.

The potential power of these signals is obvious. If they're right, they're picking the bottom or top of the previous move, which gives you a chance to get the whole move in the other direction, rather than just a piece of it like a trend-following strategy might get. Let's see how divergence trades work on stocks. Here are the rules we're testing:

- ■ Price divergence short setup:   Yesterday's close is a Donchian 14-day high, and it was higher than the last Donchian 14-day high. There was a Donchian 14-day low between these highs. T oday's close is less than yesterday's close.
- ■ Momentum divergence short setup:   Yesterday's momentum reading was lower than the momentum reading on the day of the previous 14-day Donchian high.
- ■ Divergence short entry: Enter short market on open.
- ■ Divergence short exit: Compile statistics for exits 5, 10, 15, 20, and 30 days after entry.
- ■ Price divergence buy setup:   Yesterday's close was a Donchian 14-day low , and it was lower than the last Donchian 14-day low. There was a 14-day Donchian high between the two lows. T oday's close is higher than yesterday's close.
- ■ Momentum divergence setup:   Yesterday's momentum reading was higher than the momentum reading on the day of the previous 14-day Donchian low.
- ■ Divergence buy entry: Enter long market on open.
- ■ Divergence buy exit: Compile statistics for exits 5, 10, 15, 20, and 30 days after entry.

FIGURE  9.1 Divergence Buy and Sell Signals

<!-- image -->

We're using 14-day Donchian highs and lows, so let's use a 14-day momentum calculation. The equation is:

<!-- formula-not-decoded -->

Table 9.1 shows the trade statistics across the Nasdaq 100 stock basket over the 2000-2011 time frame.

| TABLE 9.1   | Trading Stock Divergences with Various Hold Periods   | Trading Stock Divergences with Various Hold Periods   | Trading Stock Divergences with Various Hold Periods   | Trading Stock Divergences with Various Hold Periods   |
|-------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| Hold Period | Winning Trades                                        | Losing Trades                                         | Total Profit Percent                                  | Profit-per-Trade Percent                              |
| 5           | 2,343                                                 | 2,371                                                 | -534                                                  | -0.11                                                 |
| 10          | 2,282                                                 | 2,432                                                 | -1,228                                                | -0.26                                                 |
| 15          | 2,314                                                 | 2,400                                                 | -408                                                  | -0.09                                                 |
| 20          | 2,316                                                 | 2,398                                                 | -370                                                  | -0.08                                                 |
| 30          | 2,320                                                 | 2,394                                                 | -1,687                                                | -0.35                                                 |

I'd  call  the  results  unimpressive. There's  certainly  no  appreciable edge  trading  the  divergences,  or  doing  the  opposite  and  fading  the divergences. Let's look at trading divergences on commodities with the same rules.

Table 9.2 shows the statistics across the 56-commodity basket we've been using over the 1980-2011 time frame.

| TABLE 9.2   | Trading Commodity Divergences with Various Hold Periods   | Trading Commodity Divergences with Various Hold Periods   | Trading Commodity Divergences with Various Hold Periods   | Trading Commodity Divergences with Various Hold Periods   |
|-------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Hold Period | Winning Trades                                            | Losing Trades                                             | Total Profit ($)                                          | Profit-per-Trade ($)                                      |
| 5           | 2,368                                                     | 2,807                                                     | -319,551                                                  | -62                                                       |
| 10          | 2,313                                                     | 2,862                                                     | -623,435                                                  | -120                                                      |
| 15          | 2,321                                                     | 2,854                                                     | -980,151                                                  | -189                                                      |
| 20          | 2,311                                                     | 2,864                                                     | -1,037,318                                                | -200                                                      |
| 30          | 2,334                                                     | 2,841                                                     | -1,200,722                                                | -232                                                      |

These  results  are  significant. Trading  the  divergences  is  definitely  the wrong thing to do.  You should be fading them. When you get a long signal, sell on the next open; and when you get a short signal, buy on the next open. What about the momentum part? Our setups require that momentum and price be moving in the opposite direction on trade day. What if we fade the buy and sell signals when momentum is moving in the same direction as price? Here are the new rules:

New price buy setup:  Yesterday's close was a Donchian 14-day high, and it was higher than the last Donchian 14-day high. T oday's close is less than yesterday's.  There was a Donchian 14-day low before yesterday's high, and it was after the previous 14-day Donchian high.

- ■ New momentum buy setup: Yesterday's momentum reading was higher than on the day of the previous 14-day high.
- ■ New long entry: Enter long market on open.
- ■ New long exit: Compile statistics for exits 5, 10, 15, 20, and 30 days after entry.
- ■ New price sell setup:   Y esterday's close was a Donchian 14-day low , and it was lower than the last Donchian 14-day high.  T oday's close is higher than yesterday's. There was a Donchian 14-day high before yesterday's low, and it was after the previous 14-day Donchian low.
- ■ New momentum sell setup: Yesterday's momentum reading was lower than on the day of the previous 14-day low.
- ■ New short entry: Enter short market on open.
- ■ New short exit: Compile statistics for exits 5, 10, 15, 20, and 30 days after entry.

Table 9.3 shows the results on our 56-commodity basket.

| TABLE 9.3   | Fading Commodity Divergences with Various Hold Periods   | Fading Commodity Divergences with Various Hold Periods   | Fading Commodity Divergences with Various Hold Periods   | Fading Commodity Divergences with Various Hold Periods   |
|-------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Hold Period | Winning Trades                                           | Losing Trades                                            | Total Profit ($)                                         | Profit-per-Trade ($)                                     |
| 5           | 3,780                                                    | 3,118                                                    | 938,512                                                  | 136                                                      |
| 10          | 3,830                                                    | 3,068                                                    | 1,781,738                                                | 258                                                      |
| 15          | 3,814                                                    | 3,084                                                    | 2,133,203                                                | 309                                                      |
| 20          | 3,812                                                    | 3,086                                                    | 2,243,463                                                | 325                                                      |
| 30          | 3,815                                                    | 3,083                                                    | 3,112,355                                                | 451                                                      |

These results are very promising and could form the basis of a tradeable strategy. I think we can conclude that divergence trading doesn't have a significant edge in either stock or commodity trading; in fact, for commodities you'd be much better off trading in the opposite direction on each divergence signal.

## ■ Buy/Fade a Gap

Gaps are a subject in most trading books. An opening gap is formed when the open of a bar is outside the range of the previous bar. If that bar's range stays entirely outside the previous bar's range, it's a bar gap. Some of the prevailing theories on gaps are:

- ■ Gaps  on  longer  time-frame  charts  are  more  significant  than  those  on shorter time-frame charts; a gap on a weekly chart is more meaningful than one on a daily chart.
- ■ Price moves to fill the gap.
- ■ Gaps out of price consolidation signal the start of a breakout in the direction of the gap.
- ■ Gaps in the direction of a sustained move can signal continuation of the strong move, or exhaustion with a reversal in price imminent.

In this section we'll explore opening gaps and bar gaps for both stocks and commodities.

## Opening Gaps in Stocks

Using  our  100-stock  basket  of  Nasdaq  stocks,  gap-trade  statistics  were found on all the opening gaps in the 2000-2011 time frame. Gap trades are based on entering long on the open and exiting on the following open. A $5,000 position was taken in each trade. Table 9.4 summarizes the trade information.

Scanning the table, you could conclude the following:

- ■ Opening gaps aren't shorting opportunities. There was only one gap setup (the last  row)  where the long trades lost money. That means doing the opposite and shorting those setups would have made money, but it's only $2 per trade-not even enough to cover transaction costs.
- ■ All the gaps opening below yesterday's low made money on the long side. That's in keeping with the counter-trend nature of stocks: Weakness is a buying opportunity. Further, those opening below yesterday's low when the trend was down did better than those that occurred when the trend was up.

TABLE 9.4

| Opening Gap Description                                                         |   Winning Trades |   Losing Trades | Profit-per-Trade   |
|---------------------------------------------------------------------------------|------------------|-----------------|--------------------|
| Open below yesterday's low                                                      |           16,661 |          15,020 | $13                |
| Open above yesterday's high                                                     |           18,666 |          17,466 | $ 1                |
| Open below yesterday's low and trend up*                                        |            8,174 |           7,376 | $ 9                |
| Open below yesterday's low and trend down*                                      |            8,487 |           7,644 | $17                |
| Open above yesterday's high and trend up*                                       |            7,569 |           7,078 | $ 2                |
| Open above yesterday's high and trend down*                                     |           11,087 |          10,368 | $ 0                |
| Open one standard deviation, or greater below yesterday's low**                 |              729 |             658 | $16                |
| Open one standard deviation, or greater above yesterday's high**                |              818 |             767 | $ 9                |
| Open one standard deviation** or greater                                        |              358 |             347 | $ 7                |
| Open one standard deviation** or greater below yesterday's low and trend down*  |              371 |             311 | $26                |
| Open one standard deviation** or greater above yesterday's high and trend up*   |              492 |             451 | $16                |
| Open one standard deviation** or greater above yesterday's high and trend down* |              326 |             316 | -$ 2               |

*  Trend based on close versus close 20 days ago

** Standard deviation based on previous 20 closes

- ■ I think the most useful setup is the first: an open below yesterday's low , irrespective of trend. There are over 31,000 occurrences in the 12-year period, which averages to about 10 a day. This might prove to be a good starting point for a tradeable long-only stock strategy.

Let's do the same opening gap analysis on commodities.

## Opening Gaps in Commodities

Using our 56-commodity basket, the same opening gap statistics were compiled. Differences in this analysis are that gaps up are traded long, and gaps down are traded short. Gap trades are entered on the open the day of the gap  and  exited  on  the  next  open. A  one-lot  (one  contract)  position  was taken in each trade.  Table 9.5 summarizes the results.

The results were negative in 10 out of the 12 cases.  This parallels the way the pullback filter from Chapter 6 works on commodities: An up day is followed by a down day, a down day is followed by an up day , a down day in an uptrend gets a big bounce up the next day , and an up day in a down trend turns more strongly

## TABLE 9.5

| Opening Gap Description                                                         |   Winning Trades |   Losing Trades | Profit-per-Trade   |
|---------------------------------------------------------------------------------|------------------|-----------------|--------------------|
| Open below yesterday's low                                                      |           27,694 |          31,727 | -$13               |
| Open above yesterday's high                                                     |           30,088 |          33,380 | -$19               |
| Open below yesterday's low and trend up*                                        |           12,441 |          15,058 | -$32               |
| Open below yesterday's low and trend down*                                      |           15,138 |          16,552 | $ 3                |
| Open above yesterday's high and trend up*                                       |           16,896 |          18,341 | $ 6                |
| Open above yesterday's high and trend down*                                     |           13,080 |          14,930 | -$51               |
| Open one standard deviation or greater below yesterday's low**                  |            1,289 |           1,491 | -$27               |
| Open one standard deviation or greater above yesterday's high**                 |            1,332 |           1,578 | -$29               |
| Open one standard deviation** or greater                                        |              550 |             680 | -$60               |
| Open one standard deviation** or greater below yesterday's low and trend down*  |              731 |             801 | -$ 1               |
| Open one standard deviation** or greater above yesterday's high and trend up*   |              798 |             925 | -$ 9               |
| Open one standard deviation** or greater above yesterday's high and trend down* |              527 |             647 | -$65               |

down the next day.  The openings that gap up are particularly interesting as shortterm shorting opportunities, especially in light of the fact that commodities have an upward bias. It' s nice to find a way to make money trading against the bias.

One last note about opening gaps. Larry Williams introduced a shortterm trading system he called OOPS based on these gaps. His logic is that overnight news or opinion is occasionally so bullish or bearish for a given commodity that traders rush in at the opening and drive price to a gap opening. In the light of day, the true story causes a reversal of opinion and traders say 'oops' as they hastily cover their positions and price reverses.

Let's now look at bar gaps for both stocks and commodities.

## Bar Gaps in Stocks

If gaps are trading opportunities, a bar gap should be more meaningful than an opening gap because price maintained the gap for the entire bar. Let's look at two cases. First is a bar gap coming out of congestion.  There are many ways to define congestion, but a relatively simple one is to look at the recent range in relation to the standard deviation of closing price. If the range from the highest high to the lowest low over a recent period is less than one or two standard deviations of closing price over the same period, the stock is more or less range-bound. Using our 100-stock basket of Nasdaq stocks, statistics were found on all the bar gaps that occurred when the 10-day range was less than one standard deviation of price and less than two standard deviations of price. When a bar gap occurred, trade entry was the open of the day following the gap, and profit was taken five days later on the open. A $5,000 position was taken in each trade.  T able 9.6 summarizes the information.

TABLE 9.6 Bar Gaps out of Congestion on Nasdaq Stocks, 2000-2011

| Bar Gap Description                                 |   Winning Trades |   Losing Trades | Profit-per-Trade   |
|-----------------------------------------------------|------------------|-----------------|--------------------|
| Above congestion when range                         |              163 |             152 | $ 0.50             |
| < 1 standard deviation Above congestion when range  |             1257 |           1,290 | -$11.50            |
| < 2 standard deviations Below congestion when range |               95 |             113 | $16.50             |
| Below congestion when range                         |            1,076 |             791 | $63.00             |
| < 2 standard deviation                              |                  |                 |                    |

For stocks, bar gaps out of congestion are not breakouts in the direction of the gap. In fact, they're pretty good counter-trend setups. Note that a breakout above congestion when the 10-day range is less than two standard deviations of closing price actually leads to a small profit if we sell at the signal instead of buy. And buying stocks that gap down when the range is less than two standard deviations nets 1.26 percent per trade in five days ($63/$5,000). That's a noncompounded annual rate of over 60 percent if you could do trades consecutively .

Now let's look at bar gaps that occur when the stock isn't in congestion. For that case we can use a 10-day range that's larger than one or two standard deviations of price.  The results are shown in  Table 9.7.

| TABLE 9.7                                           | Bar Gaps without Congestion on Nasdaq Stocks, 2000-2011   | Bar Gaps without Congestion on Nasdaq Stocks, 2000-2011   | Bar Gaps without Congestion on Nasdaq Stocks, 2000-2011   |
|-----------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Bar Gap Description                                 | Winning Trades                                            | Losing Trades                                             | Profit-per-Trade                                          |
| Above congestion when range > 1 standard deviation  | 3,931                                                     | 3,882                                                     | -$ 7.50                                                   |
| Above congestion when range > 2 standard deviations | 2,837                                                     | 2,744                                                     | -$ 5.50                                                   |
| Below congestion when range > 1 standard deviation  | 3,455                                                     | 2,605                                                     | $59.00                                                    |
| Below congestion when range > 2 standard deviations | 2,492                                                     | 1,909                                                     | $53.50                                                    |

Gaps without congestion behave pretty much the same as gaps out of congestion: They are counter-trend setups. T able 9.8 summarizes the bar gap results without a congestion modifier; the gaps just break the 10-day high or 10-day low .

TABLE 9.8 Bar Gaps on Nasdaq Stocks, 2000-2011

| Bar Gap Description   |   Winning Trades |   Losing Trades | Profit-per-Trade   |
|-----------------------|------------------|-----------------|--------------------|
| Bar gap up            |            4,094 |           4,034 | -$ 7.50            |
| Bar gap down          |            3,568 |           2,700 | $56.50             |

Bar gaps up might be worth exploring as a short setup, while bar gaps down could probably be the start of a tradeable long-only strategy.

## Bar Gaps in Commodities

This section parallels the bar-gap analysis just presented for stocks. Using the 56-commodity basket over the 1980-2011 time frame, Table 9.9 shows the results of trading bar gaps out of 10-day congestion: Trade entry was on  the  open  following  the  gap  and  exit  was  done  on  the  open  five  days later.  Again, bar gaps up are long trades, and bar gaps down are short trades.

TABLE 9.9 Bar Gaps out of Congestion on Commodities

| Bar Gap Description                                 |   Winning Trades |   Losing Trades | Profit-per-Trade   |
|-----------------------------------------------------|------------------|-----------------|--------------------|
| Above congestion when range < 1 standard deviation  |              303 |             289 | -$75               |
| Above congestion when range < 2 standard deviations |            2,798 |           2,827 | -$88               |
| Below congestion when range < 1 standard deviation  |              274 |             259 | $ 5                |
| Below congestion when range < 2 standard deviations |            2,362 |           2,493 | -$34               |

As with stocks, commodity bar gaps out of congestion are not breakouts in the direction of the gap; they're counter-trend setups.

Table 9.10 shows the results when the commodity is not in congestion and it has a bar gap. Long trades are taken on the open after a bar gaps above the 10-day high when the non-congestion criterion is met, and short trades are taken on the open after a bar gaps below the 10-day low . Exit is done on the open five days after entry.

TABLE 9.10

## Bar Gaps without Congestion on Commodities

| Bar Gap Description                             |   Winning Trades |   Losing Trades | Profit-per-Trade   |
|-------------------------------------------------|------------------|-----------------|--------------------|
| Bar gap up when range > 1 standard deviation    |            8,238 |           7,818 | $ 50               |
| Bar gap up when range > 2 standard deviations   |            5,743 |           5,280 | $114               |
| Bar gap down when range > 1 standard deviation  |            7,107 |           7,286 | $ 14               |
| Bar gap down when range > 2 standard deviations |            5,019 |           5,052 | $ 37               |

Bar gaps when a commodity is not in congestion are a marker for a breakout in the direction of the trend. Because of the relative success of the long and short trades when the 10-day range is greater than two standard deviations of closing price, I looked at an added trend condition.  Table 9.11 shows the results when the bar gap is also in the direction of the 20-day trend.

TABLE 9.11

## Bar Gaps without Congestion on Commodities in the Direction of the Trend

| Bar Gap Description                                                                                                     |   Winning Trades |   Losing Trades | Profit-per-Trade   |
|-------------------------------------------------------------------------------------------------------------------------|------------------|-----------------|--------------------|
| Bar gap up when range > 2 standard deviations, and close the day before the gap greater than the close 20 days previous |            4,918 |           4,411 | $163               |
| Bar gap down when range > 2 standard deviations, and close the day before the gap less than the close 20 days previous  |            4,180 |           4,107 | $64                |

Clearly a bar gap out of congestion and in the direction of the trend is a good pointer to a trend continuation.  This entry logic might lead to a tradeable strategy.

## ■ Trade Fibonacci Retracements

The Fibonacci sequence was introduced by Leonardo of Pisa in 1202. It is a sequence formed by adding the previous number in the sequence to the current number to form the next number, with the first two numbers being 0 and 1, by definition.  The following is the start of the sequence:

<!-- formula-not-decoded -->

The significance of the sequence is that many recurring patterns in nature have similar patterns, or they have patterns that reduce to the ratio of adjacent Fibonacci numbers.  The Golden Ratio, in particular is a ratio well documented in the literature. It is the limit of the last two numbers near infinity of the sequence. So ratios based on the adjacent numbers shown above are:

```
First/Second  =  0,  1,  0.5,  0.667,  0.60,  0.625,  0.615,  0.619,  0.618, 0.618, 0.618 Second/First = 4, 1, 2, 1.5, 1.667, 1.6, 1.625, 1.615, 1.619, 1.618, 1.618, 1.618
```

As the sequence gets longer, the ratios between the numbers one, two, and three places apart converge to the following ratios:

```
One apart 55/89, 89/144 = 0.618 89/55, 144/89 = 1.618 Two apart 55/144, 89/233 = 0.382 144/55, 233/89 = 1.382 Three apart 55/233, 55/377 = 0.236 233/55, 377/55 = 1.236
```

These  are  the  Fibonacci  numbers  the  literature  regards  as  important, though some add 0.5 to the mix. The way these numbers are traded on the long side is to wait for a pullback from the trend of 23.6 percent, or 38.2 percent, or 50 percent, or 61.8 percent of the move, and then buy, expecting a reversal. Thus  they  are  regarded  as  support  points  where  an up-trend should resume its rally, or where a down-trend resumes its fall.

Conversely, the 1.236, 1.382, and 1.618 points are regarded as resistance points where profits should be taken or the position lightened up.

In this section we'll look at trading our stock and commodity baskets using the Fibonacci numbers as support.  The only element that needs to be defined is the price point that retracement or profit should be measured from. Let's use the same Donchian points we used in the divergence section of this chapter. If there is a 14-day Donchian low followed by a 14-day Donchian high, the trend must be up. We'll use the difference between the Donchian high and low points as the measuring point for a Fibonacci retracement and buy if there is a pullback of 23.6 percent, 38.2 percent, or 61.8 percent of  the  distance,  and  measure  reaction  after  that.  Conversely,  if  there  is  a 14-day high, followed by a 14-day low, the trend is down, and we'll look to  sell  at  up  moves  from  the  low  at  our  Fibonacci  retracement  points. Figure   9.2 shows buy and sell logic.

FIGURE  9.2 Fibonacci Retracement Buy/Sell Setups

<!-- image -->

The trading rules used are:

- ■ Long  trades:  If  the  last  Donchian  14-day  high  occurred  after  the  last 14-day low, the distance in points between the high and low is multiplied by the Fibonacci retracement fraction. That value is subtracted from the 14-day high to form the entry target. If there is a close below the entry target, a trade is entered on the next open. Trade profit is computed 5, 10, 15, and 20 days after entry.
- ■ Short  trades:  If  the  last  Donchian  14-day  low  occurred  after  the  last 14-day high, the distance in points between the high and low is multiplied by the Fibonacci retracement fraction. That value is added to the 14-day low to form the entry target. If there is a close above the entry target, a trade is entered on the next open.  Trade profit is computed 5, 10, 15, and 20 days after entry.

## Fibonacci Retracements with Stocks

Because of the difficulty  in  profitably  trading  stocks  from  the  short  side, we'll look at the long trades and short trades separately. Table 9.12 shows the results of taking long trades on the basket of Nasdaq stocks when the Fibonacci  retracement  level  is  23.6  percent  of  the  distance  from  the Donchian low to the Donchian high.

| TABLE 9.12                | Stock Trading Long: Fibonacci Retracements of 23.6 Percent   | Stock Trading Long: Fibonacci Retracements of 23.6 Percent   | Stock Trading Long: Fibonacci Retracements of 23.6 Percent   | Stock Trading Long: Fibonacci Retracements of 23.6 Percent   | Stock Trading Long: Fibonacci Retracements of 23.6 Percent   |
|---------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| Number of Days from Entry | Winning Trades                                               | Losing Trades                                                | Total Profit Percent                                         | Profit-per-Trade Percent                                     | Annualized Return Percent                                    |
| 5                         | 3,505                                                        | 3,104                                                        | 4,292                                                        | 0.65                                                         | 32.5                                                         |
| 10                        | 3,561                                                        | 3,048                                                        | 6,239                                                        | 0.94                                                         | 23.5                                                         |
| 15                        | 3,630                                                        | 2,979                                                        | 7,696                                                        | 1.16                                                         | 19.3                                                         |
| 20                        | 3,652                                                        | 2,957                                                        | 9,361                                                        | 1.42                                                         | 17.8                                                         |

The annualized return of the last column is just the average number of trading  days  per  year  (250)  divided  by  the  number  of  days  in  the  trade, multiplied by the profit-per-trade. The results are certainly positive with a nice annualized return for a five-day hold.  Table 9.13 shows the results for a retracement percent of 38.2.

These results are not nearly as good as the results with the 23.6 percent retracement.

TABLE 9.13

Stock Trading Long: Fibonacci Retracements of 32.8 Percent

|   Number of Days from Entry |   Winning Trades |   Losing Trades |   Total Profit Percent |   Profit-per-Trade Percent |   Annualized Return Percent |
|-----------------------------|------------------|-----------------|------------------------|----------------------------|-----------------------------|
|                           5 |            2,186 |           2,073 |                  1,296 |                       0.30 |                        15.0 |
|                          10 |            2,269 |           1,990 |                  2,099 |                       0.49 |                        12.2 |
|                          15 |            2,277 |           1,982 |                  2,958 |                       0.69 |                        11.5 |
|                          20 |            2,295 |           1,964 |                  3,898 |                       0.92 |                        11.5 |

Let's  now  look  at  the  short  side  with  a  23.6  retracement. Table  9.14 shows the results of going short when price closes over 23.6 percent of the down move above the 14-day Donchian low.

TABLE 9.14 Stock Trading Short: Fibonacci Retracements of 23.6 Percent

|   Number of Days from Entry |   Winning Trades |   Losing Trades |   Total Profit Percent |   Profit-per-Trade Percent |   Annualized Return Percent |
|-----------------------------|------------------|-----------------|------------------------|----------------------------|-----------------------------|
|                           5 |            3,372 |           4,035 |                 -2,601 |                      -0.35 |                       -17.5 |
|                          10 |            3,421 |           3,986 |                 -5,447 |                      -0.74 |                       -18.5 |
|                          15 |            3,380 |           4,027 |                 -6,744 |                      -0.91 |                       -15.2 |
|                          20 |            3,355 |           4,052 |                 -8,386 |                      -1.13 |                       -14.1 |

Again, it's very hard to trade stocks profitably form the short side.

So, does this mean that Fibonacci levels are a meaningful approach for  trading  stocks  from  the  long  side,  especially  at  the  23.6  retracement level? Not necessarily. If I were exploring retracement trading, I'd look at levels like 5 percent, 10 percent, 15 percent, 20 percent, and so on. If the results of that analysis were on the same level as the Fibonacci  retracement  levels,  I'd  conclude  that  in  trading,  numbers are numbers; there are no special ones. Table 9.15 shows the results of those runs.

Table 9.15 shows that the best retracement level probably lies between 20 and 25 percent in all cases. T o nail down whether the peak really is at 23.6 percent, another set of runs was made at 21, 22, 23, and 24 percent retracement levels. The peak actually occurs at 21 percent. The annualized five-day return for the 21 percent retracement level was 33.5 percent, 1 percent higher than the return at 23.6 percent. I think we can conclude that with very noisy data, like stock market data, numbers are just numbers; there are no magic ones.

TABLE 9.15

## Stock Trading Long: Various Retracements Levels

|   Retracement Percent |   Number of Days from Entry |   Winning Trades |   Losing Trades |   Total Profit Percent |   Profit-per-Trade Percent | Annualized Return Percent   |
|-----------------------|-----------------------------|------------------|-----------------|------------------------|----------------------------|-----------------------------|
|                     5 |                           5 |            4,546 |           4,196 |                  3,375 |                       0.39 | 19.5                        |
|                     5 |                          10 |            4,702 |           4,040 |                  7,344 |                       0.84 | 21.0                        |
|                     5 |                          15 |            4,789 |           3,953 |                  9,180 |                       1.05 | 17.5                        |
|                     5 |                          20 |            4,824 |           3,918 |                 10,598 |                       1.21 | 15.1                        |
|                    10 |                           5 |            4,366 |           4,019 |                  3,600 |                       0.43 | 21.5                        |
|                    10 |                          10 |            4,508 |           3,877 |                  6,989 |                       0.83 | 20.8                        |
|                    10 |                          15 |            4,556 |           3,829 |                  8,701 |                       1.04 | 17.3                        |
|                    10 |                          20 |            4,621 |           3,764 |                 10,362 |                       1.24 | 15.5                        |
|                    15 |                           5 |            4,132 |           3,739 |                  4,479 |                       0.57 | 28.5                        |
|                    15 |                          10 |            4,247 |           3,624 |                  7,259 |                       0.92 | 23.0                        |
|                    15 |                          15 |            4,307 |           3,564 |                  8,751 |                       1.11 | 18.5                        |
|                    15 |                          20 |            4,383 |           3,488 |                 10,455 |                       1.33 | 16.6                        |
|                    20 |                           5 |            3,789 |           3,383 |                  4,496 |                       0.63 | 31.5*                       |
|                    20 |                          10 |            3,884 |           3,288 |                  7,163 |                       1.00 | 25.0**                      |
|                    20 |                          15 |            3,920 |           3,252 |                  8,407 |                       1.17 | 19.5***                     |
|                    20 |                          20 |            3,961 |           3,211 |                  9,734 |                       1.36 | 17.0                        |
|                    25 |                           5 |            3,340 |           3,038 |                  3,702 |                       0.58 | 29                          |
|                    25 |                          10 |            3,421 |           2,957 |                  5,735 |                       0.90 | 22.5                        |
|                    25 |                          15 |            3,482 |           2,896 |                  7,150 |                       1.12 | 18.7                        |
|                    25 |                          20 |            3,544 |           2,834 |                  8,901 |                       1.40 | 17.5****                    |
|                    30 |                           5 |            2,876 |           2,646 |                  2,634 |                       0.48 | 24                          |
|                    30 |                          10 |            2,951 |           2,571 |                  4,076 |                       0.74 | 18.5                        |
|                    30 |                          15 |            2,979 |           2,543 |                  5,229 |                       0.95 | 15.8                        |
|                    30 |                          20 |            3,036 |           2,486 |                  6,951 |                       1.26 | 15.8                        |

## Fibonacci Retracements with Commodities

The  same  analysis  was  conducted  on  the  56-commodity  basket  over the  1980 through 2011 time frame. Table 9.16 shows the results using a Fibonacci retracement level of 23.6 percent for both long and short trades.

| TABLE 9.16                | Trading Fibonacci Retracements of 23.6 Percent on Commodities   | Trading Fibonacci Retracements of 23.6 Percent on Commodities   | Trading Fibonacci Retracements of 23.6 Percent on Commodities   | Trading Fibonacci Retracements of 23.6 Percent on Commodities   |
|---------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|
| Number of Days from Entry | Number of Days from Entry                                       | Winning Trades Losing Trades                                    | Total Profit($)                                                 | Profit-per-Trade ($)                                            |
| 5                         | 7,731                                                           | 8,085                                                           | 72,600                                                          | 4                                                               |
| 10                        | 7,892                                                           | 7,924                                                           | 66,974                                                          | 4                                                               |
| 15                        | 7,884                                                           | 7,932                                                           | -143,434                                                        | -10                                                             |
| 20                        | 7,804                                                           | 8,012                                                           | -817,468                                                        | -52                                                             |

Table 9.16 shows that a 23.6 percent retracement is more likely to signal a  trend  reversal  than  a  resumption  of  the  trend. The  bigger  retracement points had increasingly bigger losses as evidenced by the 38.2 retracement results shown in  Table 9.17.

| TABLE 9.17                | Trading Fibonacci Retracements of 38.2 Percent on Commodities   | Trading Fibonacci Retracements of 38.2 Percent on Commodities   | Trading Fibonacci Retracements of 38.2 Percent on Commodities   | Trading Fibonacci Retracements of 38.2 Percent on Commodities   |
|---------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|
| Number of Days from Entry | Number of Days from Entry                                       | Winning Trades                                                  | Trades Total Profit ($)                                         | Profit-per-Trade ($)                                            |
| 5                         | 5                                                               | 6,759                                                           | 7,334 -362,574                                                  | -26                                                             |
| 10                        | 10                                                              | 6,840                                                           | 7,253 -637,792                                                  | -46                                                             |
| 15                        | 15                                                              | 6,785                                                           | 7,308 -1,011,355                                                | -72                                                             |
| 20                        | 20                                                              | 6,744                                                           | 7,349 -1,362,637                                                | -97                                                             |

Clearly  Fibonacci  retracements  do  not  signal  a  trend  resumption  for commodities; they are more likely to signal a trend reversal.

## ■ Buy Stock Splits

On the face of it, this would appear to be a dubious strategy.  When the price of a stock splits, the number of shares that a trader owns moves up (reverse split) or down (normal split) in accordance with the split so that at the end of the process the dollar value of his or her stock remains unchanged. For instance, if you acquire 100 shares of stock xyz at a price of 60, and on the day of the split the price is still 60, and it splits 2 for 1, you will now own 200 shares at a price of 30. Before the split your 100 shares at 60 were worth $6,000, and after the split your 200 shares at $30 are worth $6,000.

To see if there really is something to the strategy, an analysis was conducted around all of the split dates on 3,400 highly liquid stocks from the start of 2000 until the end of 2011.  There were a total of 1,322. Long trade entry was done on the open some number of days before the split date and exited on the open some number of days after the split date. The performance metric used was percent profit appreciation over the holding period. Table 9.18 summarizes the results for normal splits.

Table 9.18 shows that there is a nice return for the strategy.  You want to get your position about a week before the split and exit shortly after. Based on profit-per-day of the holding period, entering six trading days before the split and exiting the day after the split looks to have the best return. T o see if the split return really outperformed the market, I accumulated profit statistics on the S&amp;P 500 ETF (symbol SPY) for every period a stock was in a split trade. Here's the apples-to-apples comparison.

| TABLE 9.18                                | Normal Split-Trade Statistics           | Normal Split-Trade Statistics   | Normal Split-Trade Statistics   |                                    |                          |
|-------------------------------------------|-----------------------------------------|---------------------------------|---------------------------------|------------------------------------|--------------------------|
| Number of Days before the Split for Entry | Number of Days after the Split for Exit | Number of Wining Split Trades   | Number of Losing Split Trades   | Average Profit-per-Trade (Percent) | Profit-per-Day (Percent) |
| 12                                        | 2                                       | 782                             | 540                             | 1.79                               | 0.12                     |
| 10                                        | 2                                       | 778                             | 548                             | 1.65                               | 0.13                     |
| 8                                         | 2                                       | 795                             | 542                             | 1.49                               | 0.14                     |
| 6                                         | 2                                       | 792                             | 551                             | 1.34                               | 0.15                     |
| 4                                         | 2                                       | 779                             | 567                             | 1.00                               | 0.14                     |
| 6                                         | 1                                       | 788                             | 554                             | 1.21                               | 0.15                     |
| 6                                         | 3                                       | 797                             | 542                             | 1.37                               | 0.14                     |

| Split winning trades:   | 788          |
|-------------------------|--------------|
| Split losing trades:    | 554          |
| Split profit-per-trade: | 1.21 percent |
| SPY winning trades:     | 735          |
| SPY losing trades:      | 607          |
| SPY profit-per-Trade:   | 0.13 percent |

So the split trades outperformed the market by an average of 1.08 percent per trade. Since the holding period is eight days, and there are about 254 trading days a year, you could do about 32 trades a year, if there were a  split  available  at  the  right  time. That's  32  times  1.21  percent,  or  about 39 percent per year, without any compounding. Of course the splits aren't going to line up perfectly, but these trades are definitely worth considering as an add-on to anything else you're trading.

Table 9.18 was for normal splits. Let's see if the same thing works for reverse splits.  T able 9.19 shows the trade results.

| TABLE 9.19                                | Reverse Split-Trade Statistics          | Reverse Split-Trade Statistics   | Reverse Split-Trade Statistics   |                                    |                          |
|-------------------------------------------|-----------------------------------------|----------------------------------|----------------------------------|------------------------------------|--------------------------|
| Number of Days before the Split for Entry | Number of Days after the Split for Exit | Number of Wining Split Trades    | Number of Losing Split Trades    | Average Profit-per-Trade (Percent) | Profit-per-Day (Percent) |
| 12                                        | 2                                       | 21                               | 37                               | -5.91                              | -0.39                    |
| 10                                        | 2                                       | 20                               | 38                               | -5.66                              | -0.44                    |
| 8                                         | 2                                       | 20                               | 38                               | -5.81                              | -0.52                    |
| 6                                         | 2                                       | 21                               | 37                               | -5.60                              | -0.62                    |
| 4                                         | 2                                       | 22                               | 36                               | -5.77                              | -0.82                    |
| 2                                         | 2                                       | 23                               | 35                               | -5.35                              | -1.07                    |
| 2                                         | 1                                       | 26                               | 32                               | -5.52                              | -1.38                    |

The reverse splits behave differently than the regular splits. They are excellent shorting opportunities.  T oo bad they happen so infrequently.

Why there is an edge when buying normal stock splits is a matter for speculation. The companies that do it usually do it so that stock is easier to accumulate for small investors. Maybe that's the reason, but I suspect the real reason is that less-sophisticated investors think they're getting something for nothing.

## ■ Buy Stocks that Pay Dividends

When you buy a stock that pays a dividend, on the day of the dividend payout that amount is subtracted from closing price by the exchange. So you get the dividend, but your position is adversely impacted by the same amount. This is another strategy that should be a zero-sum game over a small period of time around the dividend date (except for tax purposes), but let's see. The same stock database used for the split analysis was used again.  A position was bought in the stock one month before the dividend date. A month was used because you need to be a stock owner before the ex-dividend date and a month will generally assure that. On the open five days after the dividend date, the trade was exited and the dividend amount was added in to yield a percentage profit for the trade. Across the 3,400 stocks used, there were over 50,000 dividend payouts. The following are the stats over the 26-day trade:

| Winning trades:                   | 32,284       |
|-----------------------------------|--------------|
| Losing trades:                    | 22,503       |
| Average percent profit-per-trade: | 1.48 percent |

Not bad. There are almost 10 full 26-day periods a year. If you could average 1.48 percent per trade, your compound return would be almost 16 percent.

The news gets better if you consider the dividend as a percent of price. Table 9.20 shows the breakdown when the size of the dividend in relation to its price is considered.

The best trades occur when the dividend is a relatively high percentage of the entry price. Because of the large number of opportunities, a tradeable stock strategy might be built around timing entry into the dividend trades when the stock is in a short-term pullback.

TABLE 9.20

## Profit on Dividend Trades as a Function of Dividend Size versus Entry Price

| Dividend Criteria                                     |   Winning Trades |   Losing Trades |   Profit-per-Trade (Percent) |
|-------------------------------------------------------|------------------|-----------------|------------------------------|
| Dividend > 5 percent of entry price                   |              366 |             178 |                         5.81 |
| Dividend between 4 and 5 percent of entry price       |              215 |             105 |                         5.64 |
| Dividend between 3 and 4 percent of entry price       |              461 |             224 |                         4.85 |
| Dividend between 2 and 3 percent of entry price       |            1,356 |             709 |                         3.21 |
| Dividend between 1.5 and 2 percent of entry price     |            2,038 |           1,067 |                         2.74 |
| Dividend between 1 and 1.5 percent of entry price     |            4,234 |           2,745 |                         1.75 |
| Dividend between 0.75 and 1 percent of entry price    |            4,074 |           2,694 |                         1.50 |
| Dividend between 0.50 and 0.75 percent of entry price |            5,617 |           4,071 |                         1.20 |
| Dividend less than 0.5 percent of entry price         |           13,923 |          10,710 |                         0.97 |

## ■ Conclusion

In this chapter we looked at some issues that arise over and over again in the trading literature.  The point really wasn't to support or defame the claims. It was to show a methodology you can use to address these types of issues with your own analysis when you come across something that looks interesting or too good to be true.

## Trading Lore

I f  you read a lot about trading, you will see the same claims and maxims repeated over and over again. In this chapter, we'll examine some of this trading lore and see that a little analysis can uncover whether it's truth or not.

## ■ The Exit Is More Important than the Entry

I was looking at a trading-related web site and saw a posting stating that the exit is more important than the entry. The blogger stated that anyone can get in at some point as the trend unfolds, but the key is getting out near the end of the run. He further claimed that a good exit can even make money with a random entry. Those statements go against everything I  believe  about  trading,  so  I  asked  him  for  an  example.  He  pointed  me to words written by Van K. Tharp in Trade  Your  Way to Financial Freedom. Here's what was said:

Actually, it has been proven that with good exits and money management, you can even profit on random entries into the market. Take the following real life example: Tom Basso designed a simple, random-entry  trading  system. We  determine  the  volatility  of  the market by a 10-day exponential moving average of the average true range. Our initial stop was three times that volatility reading. Once entry occurred by a coin flip, the same three-times-volatility stop was trailed from the close. However, the stop could only move in our favor.  Thus, the stop moved closer whenever the markets moved in our favor or whenever volatility shrank. We also used a 1 percent risk model for our position sizing. . . . [Looks like a legit approach so far, random entry, stop exit.]

We ran it on 10 markets. And it was always in each market, either long or short depending upon a coin flip. . . it made money 100 percent of the time when a simple 1 percent money management system was added. . . . The system had a [trade success] reliability of 38 percent, which is about average for a trend-following system.

The fallacy of this approach is in the last paragraph. Since 'it was always in each market,' the strategy wasn't entering the markets randomly (after the first random entry); it was entering on a specific bar when the stop said to get in.  The stop was an entry signal for the next bar. It was a reversal system, but half the time it didn't reverse. And the expected value of the entry was so high that it overcame going in the wrong direction half the time.

Because the first paragraph provided a specific example of a random entry with a specific stop that I could test, I conducted the following analysis. I used data from my basket of 56 commodities, randomly entered each 100 times, and exited after the entry point when the stop criterion was met. That's 7,000 random trades across the basket per run. I did 100 runs, 700,000 random trades. The results? The average trade made $0.000025. Statistically,  that's  no  different  from  0. That's exactly the  same  answer  I' d get if I' d randomly entered and randomly exited. In other words, the exit is identical to a random exit.

Let's look at the second paragraph again. I contend that the only reason the strategy 'made money 100 percent of the time' is due to the power of the reversal entry. It's good enough to make money even when you enter in the wrong direction half the time. In the cases where you enter in the wrong direction, you'll quickly get stopped out and have the opportunity to get right with the trend on the next flip. So I randomly entered on day one of the data for each commodity and reversed trade direction every  time  the  stop  was  hit. The  results? Across  the  56  markets,  there were 6,261 wins and 9,736 losses, for a profit of $3,818,975, or $239 per trade. Remember the exit on this system is no better than an exit on a random bar system. The whole $4M is due to the entry. The bottom line is that this example doesn't prove how powerful the exit is; it proves the power of a good entry.

I believe that there are good exits and bad exits, but none can make you  money  on  a  random  entry  into  the  market. What  they  do  is  signal when your good entry (hopefully) has played out either in profit or loss and it's time to move on to the next trade. Good exits have these characteristics:

- ■ They don't take you out of the trade until the profit potential has had a chance to be realized.  Translation:  The stop is not too tight initially.
- ■ They take you out of the trade if the setup doesn't work out.  Translation: The stop is not too loose initially.
- ■ They don't cut off big winners prematurely. Translation: The stop stays outside of normal market noise as trade profit is accrued.
- ■ They keep most of your open-equity profit. Translation: When the move is over, the stop gets you out before you give back too much.

Also, what will be a good set of exits on one system will be a terrible set on another. Just look at the exits for our long-only stock system. Because we're scalping,  the  exits  are  tight  and  the  profit-target  is  modest. That  exit  logic would turn our Donchian-based commodity system into a loser. And the exits from the commodity strategy would make the stock strategy a loser.

## ■ Defining Money Management

Money management is: more important than the strategy; the most important factor for successful trading; the most important factor in becoming a long-term winner; the most significant part of any trading system.

If  you  search  the  Internet  or  read  the  money  management sections of trading books, you'll see a lot of statements like those. Is money management that important? Can we just throw away our trading strategy, become money management gurus, and then manage our way to success? I believe that, like 'the exit is more important than the entry,' those statements go way overboard. We'll see what money management can do for our two developed strategies in the rest of this book, but for now, please don't toss them away as unimportant.

If you read through the articles that accompany the money management statements, you'll see the same themes:

- ■ Most trading strategies win less than 50 percent of the time. If you don't manage them carefully, you can wind up broke.
- ■ A room full of PhDs was asked how much to bet each round on a strategy  that  made  as  much  as  it  lost  each  round  and  won  60  percent  of

- the rounds. Taking their bet size and randomly selecting outcomes for 100 rounds, only 10/8/6/4/2 percent had money at the end.
- ■ The Kelly criteria can make your 10 percent a year strategy a 50/100/150 /200 percent a year strategy .
- ■ The optimal money management strategy is optimal f /fixed risk/fixed size/fixed ratio.

One thing they have in common is that they all claim bad money management can make a winning strategy go bust, but they never claim average/ good/excellent money management can make a losing strategy a winner. If you have no edge, you can't win, even with the best money management. (Go to Vegas and find out.) So really, what's more important the edge or how you manage it?

The real issue I have with these claims is that most of them are actually deceiving.  The first bullet slams trend-following implying that strategies that win less than 50 percent of the time are riskier than strategies that win a lot.  Y ou used to see ads for strategies claiming 90/95/98 percent winners. Those ads were for options strategies where you're selling far-out-of-themoney puts or calls for a small premium. Wins were very small, but if you got tagged with a loser, you could give back everything you'd won, and a lot more.  Winning a high percentage of trades doesn't make a strategy less risky than one that doesn't. Until the early 2000s, the vast majority of commodity trading  advisors  (CTAs)  were  trend-followers  of  one  sort  or  another. As such, almost all of them had winning trade percentages less than 50 percent. If trend-following is such a risky strategy, why did the most successful traders in the world employ it? The answer is that when your winning trades make three to five times, on average, what your losers lose, it's a moneymaking deal.

The second and third bullets take gambling analogies and apply them to trading. The Kelly criterion only applies to binomial outputs like win or lose. Gamblers use it to determine optimal bet size when they know their trading edge, and the outcomes are like roulette:  You bet on red or black, and either win or lose. In trading you can win anything from $1 to $10,000 or more with a longer-term trend-following strategy, and lose anything from, say, $1 to $3,000. The occurrence rates at the extremes are low, while they're higher for small wins and losses. It's like a box of chocolates. Those  types  of  distributions  can't  be  meaningfully  analyzed using the Kelly criterion.

But let's do what these articles do and play with some numbers. Let's start with the Kelly criteria. In its simplest form, the amount we should bet when our edge (winning percent) is p , and our odds are 1-to-1 (if we win, we win $1 for every $1 bet, and get our bet back) is shown by the following formula:

<!-- formula-not-decoded -->

In the case where p = 60 percent and the odds are even-money, bet size is  20  percent  of  bankroll  each  time  you  bet.  If  the  odds  are  2-to-1  (win $2 for every $1 bet), the bet size is:

<!-- formula-not-decoded -->

If the winning percentage in this case stayed at 60 percent, the bet size would be 40 percent. Let's simulate the first case and look at results. A random number generator was used to yield 60 percent winning trades and 40 percent losing trades. Starting with a bankroll of $100, and betting 20 percent of the bankroll on each random draw, 100 draws were done for each run. To yield meaningful summary statistics, 1,000 runs were done.

At the end of the runs, the aggregate results showed:

- ■ 82 percent of the time the equity at the end of the 100-trade sequence was higher than the starting bankroll of $100.
- ■ 18  percent  of  the  time  the  ending  equity  was  less  than  the  starting bankroll.
- ■ 2 percent of the time the sequence went bust, defined as a point where equity got down to less than $5. (Note that results can never go negative because we're betting 20 percent of the existing equity each round. As the bankroll gets smaller, the magnitude of the bets also gets smaller, but never negative.)
- ■ The average ending result was $4,966.  The $100 grew to $4,966, almost a 5,000 percent return.

You might be thinking, 'What's so bad about that?' The only risk metrics  are  the  percent  of  the  time  you  finished  with  less  than  you  started (18 percent) and the percent of the time you went bust (about 2 percent). There are none of the metrics we used in Chapter 1 when a tradeable strategy was discussed. So I went back and found the draw-down metrics for the 1,000 runs.

- ■ The average biggest draw-down was 77.3 percent across the 1,000 runs.
- ■ 16 percent of the runs had draw-downs of 90 percent or greater.
- ■ The best run 'only' had a max draw-down of 36 percent.

When you start trading one of these 100-trade sequences, you expect to see a 77 percent draw-down in your bankroll at some point. I think the bottom line is that it's called 'gambling' for a reason. It isn't investing; it isn't trading; it isn't even wild speculation. Nobody would take their hard-earned money and subject themselves to trading in that fashion. Sure, you might take a throwaway amount of money to Vegas and bet that way for a weekend, but before you go you tell yourself, 'When this is gone, I'm done.'   You expect to lose it all. It's part/most of the entertainment.

Let's take the same trading scenario and do what a trader, not a gambler,  would do to determine how much to risk each trade. Our winning percentage is 60 percent, and we get $1 for every $1 bet when we win. Let's vary the bet size from 1 percent to 20 percent per trade and look at the outcomes. The results are shown in Table 10.1.

| TABLE 10.1                         | Traders Money Management for Gambling Scenario   | Traders Money Management for Gambling Scenario   | Traders Money Management for Gambling Scenario   | Traders Money Management for Gambling Scenario   |
|------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|
| Percent of Equity Risked per Trade | Average Percent Return                           | Average Max Draw-Down (%)                        | Max draw-Down (%)                                | Percent Bust                                     |
| 1                                  | 22                                               | 6.1                                              | 20.8                                             | 0                                                |
| 2                                  | 49                                               | 11.8                                             | 37.6                                             | 0                                                |
| 3                                  | 181                                              | 17.5                                             | 59.7                                             | 0                                                |
| 4                                  | 224                                              | 22.7                                             | 62.7                                             | 0                                                |
| 5                                  | 269                                              | 27.8                                             | 73.0                                             | 0                                                |
| 10                                 | 735                                              | 49.0                                             | 91.0                                             | 0                                                |
| 20*                                | 4,866                                            | 77.3                                             | 99.6                                             | 2                                                |

* Kelly criteria recommended bet size

I don't know about you, but I wouldn't trade this strategy at a bet size greater than 2 percent. And the worst one in the table, to me, is the Kelly recommended bet-size. One last note: As you peruse the money management literature, you'll run across another common statement: Never risk more than x percent on a trade.  The x percent is always less than 5, and usually between 1 and 3.  Those people are traders, not gamblers.

The last bulleted theme concerns the 'best' type of money management. The ones listed here (optimal f , fixed risk, fixed size, fixed ratio) are all formulas for the bet size to use, just like the Kelly criteria.  W e'll look at some in the money management chapters (Chapters 11-15), but to me the position size is one of the least-important elements of money management. Far more important are things like how you manage diversification, serial correlation of trades, whether the account size is small or large, and individual trade risk. The method of position sizing won't make much difference until you address those other issues.

## ■ Monte Carlo Analysis: The Best Way to Determine the Ultimate Trading Statistics of a Strategy

Monte Carlo analysis has proven useful in myriad scientific and analytical studies. A number of trading-related books and web sites have used it as a  means of finding the ultimate trading statistics of a strategy based on a sample of trades. Can this be done? I don't think so, but certainly not in the simplistic way most are doing it.

Most Monte Carlo trading simulations take a number of hypothetical trades,  put  the  results  in  a  file  and  then  randomly  pull  them  out one-by-one to form a trade sequence.  The trade sequence is used to build an equity curve, and statistics like return, draw-down, and flat-time are computed. This process is done hundreds or even thousands of times, and  summary  statistics  can  be  generated  from  the  entire  set  of  runs. Summary  statistics  might  include  largest  return,  largest  draw-down, average largest draw-down, probability of an x percent return, and probability of an x percent draw-down. The problem with this simplistic approach is explained here.

We've seen (in Chapter 2) that it takes thousands of trades to get away from curve-fitting. By the same logic, you can't define the ultimate distribution of those thousands of trades with a sample of 20 trades taken in real time.   The 20 trades that unfolded under the watchful eye of real time could have been a spectacularly successful trading period, or a representative trading period, or a spectacularly bad period.  Yet these Monte Carlo simulations are assuming that it represents the underlying distribution of the way this strategy will trade forever. Obviously, this situation represents 'garbage in/ garbage out.'

Suppose the analyst actually waits until there are thousands of trades either by using the development trade sample, or actually waiting for years until there are thousands of real-time trades. Obviously this is a better situation. But will it yield meaningful statistics? Still, probably not. One reason is that when you pull a trade randomly, you're getting one number: the profit or  loss  from  that  trade. As  we've  seen,  the  wart  of  mid-  to  longer-term trend-following is open-equity give-back. Your trade runs up to $8,000 of profit, but you only net $4,000 for the trade; you had an open-equity giveback of $4,000. This aspect of the trade is totally missing from the Monte Carlo analysis. That missing $4,000 is draw-down your simulation doesn't count in its statistics. Missing, too, is the fact that you enter x trades a day, on average, but sometimes you enter four times as many, and sometimes you don't get any entries for days/weeks/months.  That effect is also missing from the analysis.

I don't know of any Monte Carlo package for trading, that addresses the two issues above in a proper manner, but I will admit that the capability exists for someone to do it.  Would a Monte Carlo analysis that used thousands of trades, used the whole trading sequence for a trade, and appropriately modeled trading frequency yield a meaningful simulation? Still, probably not, for two reasons.

The reason that sometimes there are a number of trades in a day isn't totally random, like our Monte Carlo analysis engine assumes. Sometimes there are a slew of trades because a trading group like the metals or energies gets good/bad news and the whole group heads north/south. It is likely that trades in the same group triggered on or near the same day will have the same trade outcome: all small winners, or all large winners, or all small losers, or all large losers. This effect is not modeled. The Monte Carlo might take x trades, but one will be an oats trade in 1983 and the other a coffee trade in 2011, when they should be from the same group and the same day.  Those who think these shortcomings don't apply to stock systems should consider the  long-only  stock  strategy  developed  so  far  in  Chapters  4  through  6. When the market was crumbling in September through December 2008, the vast majority of the 'enter on weakness' trades from the strategy would be losers, and large losers at that. And trades might be triggered in nearly every one of our Nasdaq 100 basket stocks when the market opens down 300 to 500 Dow points. The Monte Carlo analysis engine won't capture the severity and duration of that period. It is highly likely that the trading statistics in our back-test for that period would be far worse than any Monte Carlo analysis could predict.

Lastly, the effects of money management can't be captured by a Monte Carlo analysis. We haven't discussed money management yet in this book, but it harnesses the raw power of your trading strategy and makes it more tradeable than if you took every trade signaled. A simple example will help. Suppose you have a trading system that intra-day trades soybeans, crude oil, and the yen. Suppose the basic strategy generates, on average, two trades per day in each of the three commodities. You've diligently developed the strategy  and  are  convinced  it's  minimally  curve-fit. Y ou've  found  in  your money management analysis that if you take a max of one trade per day in each commodity, your equity curve is much smoother and your drawdowns are much smaller. (The reason why this is so doesn't matter for this discussion, but it's probably true because of serial correlation in the trade stream of each individual commodity: winners on a given day beget other winners that day, while losers lead to other losers.) In any event, the Monte Carlo engine sees a max of three trades per day and randomly selects each day's trades. Sometimes, it will have three trades in one commodity, and sometimes it will have one in each commodity. Your money management rules are often violated. Since your money management rules were put in place for a better trading solution, the fact that they are ignored in the Monte Carlo analysis means that, on average, the Monte Carlo results will be worse than they should be.

If you do your development correctly for both your trading strategy and your money management overlay, the statistics of that development are your best estimate of what you'll experience going forward. Sure, 'your largest draw-down is always in the futures,' but those development statistics are probably a better indication of what that might be than any Monte Carlo analysis. In my opinion, Monte Carlo analysis tells you nothing useful beyond your development statistics.

## ■ Artificial Data

If we had unlimited data for something we wanted to trade, the development process would be simple. We don't, and so we're stuck doing the best we can with what's available. A number of authors have suggested that a way around this problem is to create synthetic data.  The most common approach is to take the existing data stream for a trading instrument and create a sequence based on the difference between today's close and yesterday's close. That difference stream is placed on a file and randomly sampled to create a sequential stream of differences data that can be used to create the artificial closing price data. This approach has flaws that are similar to those of the Monte Carlo analysis.

First, it assumes that the data difference we randomly pick today has nothing to do with the data difference before and after it. This is just not the  case.  It's  easy  to  show  the  serial  relationship  of  sequential  data  by correlating the data stream with the same data stream, but lagged one or more places. If you correlate a data stream with itself without a lag, you will get a correlation coefficient of 1 as the result. If you slide the data stream one place to the left (a lag of 1) and correlate the original stream with the lagged stream, you will get an answer ranging from -1 to 1. If the answer is 0, then the two data streams are uncorrelated and the difference that occurs today doesn't influence what will happen tomorrow. If that were the case, then the Monte Carlo practice of making artificial data from randomly generated differences would be valid (if that were the only problem with the approach). Let's make some runs and see if there is serial correlation. Using some stocks and commodities, the data differences streams were lagged up to 20 times and a correlation coefficient found between the lagged data and the original stream. Table 10.2 shows the max correlation coefficient and the number of days before there was a sign change for negative to positive or vice versa, signifying that the two streams were not correlated beyond that point.

TABLE 10.2 Serial Correlation of Commodity and Stock Streams

| Commodity                       | Highest Coefficient   | Sign Change   |
|---------------------------------|-----------------------|---------------|
| Corn                            | -0.09                 | 13 days       |
| Lean Hogs                       | -0.08                 | 19 days       |
| Coffee                          | -0.07                 | 11 days       |
| Copper                          | -0.08                 | 20 days       |
| Crude Oil                       | -0.12                 | 12 days       |
| Japanese Yen                    | -0.07                 | 14 days       |
| 30-Year Bond                    | -0.07                 | 11 days       |
| S&P 500                         | -0.06                 | 12 days       |
| Stock                           | Highest Coefficient   | Sign Change   |
| International Business Machines | -0.08                 | 13 days       |
| Microsoft Corp.                 | -0.09                 | 12 days       |
| Google                          | -0.07                 | 12 days       |
| Kellogg Co.                     | -0.14                 | 10 days       |

In every case, there was a perceptible negative correlation in the lagged data that lasted over two weeks.  The negative correlation means that up closes are followed by down closes, and down closes are followed by up closes, to a slight degree. This is in line with stocks acting in a counter-trend manner, and for commodities, it jives with the day-of-week filter we examined (in Chapter 6), where we wait for a down day to go long or an up day to go short.

This is not the only relationship in the trading data. Range has a shortlived but strong negative correlation, as shown in  Table 10.3.

| TABLE 10.3                            | Serial Correlation of Range for Stocks and Commodities   | Serial Correlation of Range for Stocks and Commodities   |
|---------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Commodity                             | Highest Coefficient                                      | Sign Change                                              |
| Corn                                  | -0.46                                                    | 4 days                                                   |
| Lean Hogs                             | -0.46                                                    | 4 days                                                   |
| Coffee                                | -0.45                                                    | 4 days                                                   |
| Copper                                | -0.44                                                    | 3 days                                                   |
| Crude Oil                             | -0.43                                                    | 3 days                                                   |
| Japanese Yen                          | -0.46                                                    | 5 days                                                   |
| 30-Year Bond                          | -0.48                                                    | 4 days                                                   |
| S&P 500                               | -0.48                                                    | 4 days                                                   |
| Stock Highest Coefficient             | Stock Highest Coefficient                                | Sign Change                                              |
| International Business Machines -0.46 | International Business Machines -0.46                    | 4 days                                                   |
| Microsoft Corp.                       | -0.45                                                    | 3 days                                                   |
| Google                                | -0.44                                                    | 5 days                                                   |
| Kellogg Co.                           | -0.43                                                    | 5 days                                                   |

Table 10.3 shows significant negative range correlation that lasts between three and five days in every tradeable tested. What this means to the trader is that a big range day has a tendency to be followed by a quiet period, and a small range day followed by bigger ranges. A number of trading filters can be built using this information. One of the most popular is to look for a breakout following an inside day (a day where today's smaller range is entirely contained within yesterday's bigger range).

These aren't the only issues with artificial data. If you trade a basket like the Nasdaq 100, or the basket we used to develop the futures strategy, there will be a strong correlation between some members. For the stocks, a big market day will see most of the Nasdaq 100 moving up or down in line with the market. For the commodities, there is strong correlation within each group (see Appendix B). An artificial data stream won't capture this important correlation effect. In fact, every data stream created this way will be non-correlated (correlation coefficient of 0) with every other artificially created stream. In my opinion, artificial data is worthless.

## ■ Never Add to a Loser

This adage arises from the dangers of martingale betting. In games with a near 50 percent chance of winning (like roulette, when you bet black or red), a martingale betting strategy would increase (usually double) the bet size with every loser. Eventually, you'll win, and a sequence of losing bets would end with a winner and you'd recoup your losses plus win the original bet.

In trading, a position is taken and as it goes against you into loss, a martingale strategy would be to double-up the position.  This is called 'averaging down,' and it requires a smaller move to the upside for your entire position to become profitable. Is this always bad?

Clearly the danger is risk of ruin if you continue to add to the loser. Eventually, if the position continues to move against you, you'll get a margin call or run out of additional trading equity. But never do it?

There may be a very sound reason to add to a loser: The increment you're adding on is a good trading opportunity in its own right. Forget the original trade for a moment; if the new increment is worth trading all by itself, why not?

Here's an example: Suppose we test a stock scalping strategy that buys a stock when it closes one standard deviation below its 10-day average price. We find something that's tradeable, but in our development, we see that buying at two standard deviations below price is better, but it doesn't happen as much. Why not take the trades at one standard deviation below the average, and if price continues to go against you and it gets down to two standard deviations below price, add on another unit? Here's the trade breakout for our basket of Nasdaq 100 stocks from 2000 until the end of 2011 when we buy a $5,000 position on the next open if the close is one standard deviation below the 10-day average:

Winning trades: 11,400

Losing trades: 5,138

Total profit: $619,363

Profit-per-trade: $37

Here are the stats when we add a $5,000 unit to the position size if price closes two standard deviations below the average:

Winning trades: 11,891

Losing trades: 4,647

Total profit: $754,658

Profit-per-trade: $46

In this case, the trade stats improved.  Whether you'd trade it or not would depend on the draw-downs, but the point is it's conceivable that adding to a loser could lead to a better trading solution.

## ■ Add to Winners

This seems like a natural thing to do, and if you search the Internet, you'll find that some of the people who tell you to never add to loser say it's actually the right thing to do to add to a winner. Is it?

Adding to a winner has one inherent problem:   You're 'averaging down' your winning position. If you're ahead $500 when you add on and the trade then goes down $300 from there, you'll be down $100 on the aggregate position, but you'd still be up $200 if you hadn't added on. The only reason you'd do that is if the increment you're adding on has a probability of making more than the original signal. Otherwise, you'd have just traded two units on the original signal. I've never seen a continuation signal that's more powerful than a properly designed entry signal into a trend. That's not to say one couldn't exist, but it doesn't make sense to be able to get into the trade later in the trend and make more than an entry already in the trend.

Note  that  I'm  not  discounting  short-,  medium-,  and  longer-term strategies  independently  taking  a  position  and  exiting  on  their  own rules as the trend strengthens. I'm talking about adding to a winner at some profit increment of the original strategy with the same exit rules in place.

## ■ Nobody Ever Got Hurt Taking a Profit

I'm not a psychologist, but after trading for over 30 years and talking to thousands of traders, I know the feelings that go with experiencing equity run-up and equity draw-down. When you're in run-up, you're in a state of euphoria. Everything about life is rosy. That feeling influences you to make the following trading mistakes:

- ■ Letting the few losers you have run past their exit points. ('Everything is working; I'm a trading genius; those losers will come back.')
- ■ Putting on too much size. ('I'm supposed to do one contract, but everything is working; I'm a genius; I'm doing two and if the trade starts well I might add another.')

In short, you deviate from your plan by overtrading.

When you're in draw-down, you've got the blues. Everyone and everything are out to get you.  Y ou tend to make these trading mistakes:

- ■ Bypass or delay trade entry. ('This trade looks risky and everything's going against me; I'm going to wait and see how it starts off before I take a position.')
- ■ Undersizing positions. ('I know I'm supposed to do two lots, but everything's going against me; I'm going to step into the trade and start with only one contract.')
- ■ Taking profits prematurely. ('I'm losing almost every trade; everything's going against me; this trade is in profit; I'm cashing it in; nobody ever got hurt taking a profit.')

I'm convinced this trading maxim is due to people in draw-down trying to justify a trading mistake to themselves.

The only way out of draw-down is to trade your plan and wait for winners to build back your equity. Going into a defensive crouch will only lead to smaller profits when things turn around and delay your recovery.

Overtrading while you're in run-up only means that draw-down, when it inevitably comes, will be deeper than it should have been.  You've spent a lot of time building a plan you're willing to put real dollars behind to trade in real time.  Trade that plan.

## ■ Thirty Trades Are Enough

When I do seminars, I always start with curve-fitting material like I presented in Chapter 2. Invariably, someone brings up that a trading expert has said, '30 trades is enough' history to characterize a trading system.  They're right. I've seen statements like that at least five times in print, and some of the people who made the statements really know their stuff. What the experts are confusing is the difference between actually characterizing a distribution and testing the distribution. Most statisticians will tell you that some minimum number of samples is needed before you can do certain tests on the data, like standard deviation t-tests or z-tests. The number most often used is 30 samples.  That doesn't mean 30 samples are enough to tell you all about the underlying distribution. Here's an example that should make this clear.

Suppose you pulled 30 pairs of socks out of a big barrel and 15 were black and 15 were white. You'd probably be pretty confident that the barrel was filled about half and half with black and white socks.

If  your  computer has 16-bit color, there are 65,536 different true colors. Suppose a barrel was filled with some random number of socks for each color. After 30 sock pulls, would you have any idea of the distribution? Of course not. You couldn't even know all the colors in the barrel until at least 65,536 draws.

The last example is like trading. Trades range from large losers to large winners. You can't define the distribution statistics with a small subset of trades.

## ■ The best system statistic is:

- ■ Sharpe ratio
- ■ Winning trade percentage
- ■ Profit factor
- ■ Ulcer index, Calmar ratio

Everyone's got their favorite set of metrics, but a good metric must include some measure of both risk and reward. Things like profit-per-trade and winning trade percentage only tell you part of the story.  You need some measure of risk for context. But even metrics that incorporate risk and reward have flaws; the Nobel prize-winning Sharpe ratio isn't perfect. Jack Schwager pointed out four  problems  with  the  Sharpe  ratio  in  his  classic book, A Complete Guide to the Futures Markets. So what should you use?

I  think  the  best  metric  really  isn't  a  metric;  it's  a  picture:  the  equity curve-the old, 'a picture is worth 1,000 words.' You can tell at a glance if  something's worth trading by looking at its equity growth. Figure 10.1 shows four equity curves that have the same profit, and all but the last have the same max draw-down over the one-year period being shown. What do you think of each one?

FIGURE  10.1 Four Equity Curves

<!-- image -->

Equity Curve 1 is probably the product of a strategy that trades a number of diff  erent instruments, and doesn't take big risks per trade or have a large open-equity give-back.  There are relatively long periods of draw-down when the strategy isn't working optimally, but it's a pretty steady ride.

Equity Curve 2 trades very infrequently with a relatively long period of time between the trades, and the trades either make or lose a relatively large amount. This would be a harder strategy to trade through, and a couple of large loses in a row could be disaster.

Equity Curve 3 shouts: 'Danger,  Will Robinson!'  The constant up-sloping periods of the equity curve are due to a lot of short-term profi  table trades, probably a scalping strategy just like our stock strategy. But the sharp  V's between the up-slopes show that the money management used is a martingale type. Trades are doubled up, or tripled up, and so forth until they recover. When they do recover, all or most of the loss is recovered.  This type of strategy will eventually go bust.

Equity Curve 4 is trading nirvana. The only equity curve you'll see like that is a bond or fi  xed-interest investment, but the amount you make will be relatively small.

When you look through trading magazines or investigate trading products on the Internet, note that there are very few that show equity curves.

They'll claim 90 percent winners, or average trades of 5 percent, or show charts with bars in red for short trades and bars in blue for long trades to show how effective their signals are, but very few show composite equity curves. In all likelihood the reason is that equity curves don't lie. You can spot in an instant whether a strategy is worth trading or not. The next time someone tries to tout their product to you, ask to see an equity curve.

## ■ Buy the Dogs of the Dow

The Dogs of the Dow is a strategy that is centered on dividends. At the start of the year, an investor spreads his or her money out equally over the 10 Dow Jones Industrial Average (DJIA or Dow) stocks that have the largest dividend as a percentage of price. Portfolio re-balance is done annually. Various Internet sources show that the strategy consistently outperforms the market as a whole. But when you consider the fact that stocks are best traded as counter-trend instruments, a price-based Dogs strategy needs to be examined.

Taking the Dow 30 stock list as it existed at the end of 2011, split and dividend adjusted stock files were created for each stock going back to 1980 (only 18 of those 30 stocks were trading in 1980). Then baseline buy-andhold performance was computed by equally investing in each Dow stock on the open of the first trading day of the month and cashing in all the shares at the close of the last trading day of the month. The equity at the end of the month was again equally invested across the stocks the next trading morning, and the process was continued through the end of 2011.

Next, the following Dogs strategy was run:

- ■ On the open of the first trading day of the month, equally invest in all Dow stocks whose close on the last trading day of the month was less than the close five days previous.
- ■ Close out all trades at the close of the last trading day of the month.
- ■ Reinvest and close monthly trades each month through the end of 2011.

Table 10.4 shows the annual results for both trading approaches since 1980.

You may note that the returns for buy and hold don't match your recollection of what happened to the Dow in a given year. In 2011 for example, the DJIA was up 5.53 percent while the buy-and-hold analysis shows a return stocks that have a bigger percentage move but advance less in price. Another difference is that the DJIA changes are annual percentage changes, while the two buy strategies compound returns monthly.

of only 3.8 percent. Part of the difference is due to the way the DJIA is computed. The DJIA computation does not equally weight each component like our equally sized trades do; it is formed by adding the prices of each component and dividing by the 'Dow Divisor.'   Thus, high-priced stocks that move a small percentage up may add more Dow points then lower-priced

| Year    |   Buy-and-Hold Return (Percent) |   Dogs of the Dow Price-Based Strategy |
|---------|---------------------------------|----------------------------------------|
| 1980    |                            23.0 |                                   45.2 |
| 1981    |                            -1.3 |                                   10.4 |
| 1982    |                            37.2 |                                   68.4 |
| 1983    |                            21.6 |                                   25.4 |
| 1984    |                             8.1 |                                   15.4 |
| 1985    |                            34.9 |                                   57.1 |
| 1986    |                            26.1 |                                   21.8 |
| 1987    |                            13.1 |                                   21.3 |
| 1988    |                            18.3 |                                   13.5 |
| 1989    |                            40.9 |                                   38.7 |
| 1990    |                             4.2 |                                   10.2 |
| 1991    |                            45.0 |                                   62.7 |
| 1992    |                            19.7 |                                    8.2 |
| 1993    |                            13.3 |                                   10.9 |
| 1994    |                            12.2 |                                    6.2 |
| 1995    |                            45.9 |                                   62.5 |
| 1996    |                            34.0 |                                   23.2 |
| 1997    |                            36.2 |                                   37.0 |
| 1998    |                            34.1 |                                   35.4 |
| 1999    |                            34.1 |                                   35.4 |
| 1999    |                            30.7 |                                   42.6 |
| 2000    |                            -0.1 |                                   -6.4 |
| 2001    |                            -3.5 |                                    9.7 |
| 2002    |                           -14.2 |                                   -2.9 |
| 2003    |                            30.4 |                                   34.0 |
| 2004    |                             6.8 |                                    8.2 |
| 2005    |                             2.6 |                                    4.9 |
| 2006    |                            22.4 |                                   29.0 |
| 2007    |                             9.7 |                                   10.6 |
| 2008    |                           -29.0 |                                  -21.6 |
| 2009    |                            32.2 |                                   48.0 |
| 2010    |                            12.7 |                                    9.1 |
| 2011    |                             3.8 |                                    6.2 |
| Average |                            17.8 |                                   23.3 |

The Dogs strategy averages 5.5 percent more per year than the buy-andhold strategy.  That might not seem like a lot, put if you started with $10,000 in 1980 and compounded the yearly returns for the two strategies, you'd wind up with just over a $1,300,000 using buy-and-hold while the Dogs strategy would have grown the equity to just over $5,000,000-quite a difference.  These are some other points  Table 10.4 raises:

- ■ Buying the Dogs each month outperforms the buy-and-hold strategy by over 30 percent annually.
- ■ The Dogs strategy had three losing years in the 32-year period, while the buy-and-hold strategy had five.
- ■ The Dogs strategy never had two losing years in a row, while buy-andhold had a three-year losing stretch.
- ■ The biggest losing year for both the Dogs and the buy-and-hold strategies was 2008, but the Dogs strategies lost over 25 percent less.
- ■ The Dogs strategy had a better year than the buy-and-hold strategy 23 out of the 32 years, over 70 percent of the time.

There are two reasons why the Dogs strategy so consistently beats buyand-hold:

1.  The most obvious reason is because the Dogs strategy only trades stocks that are in a short-term price decline. Due to the counter-trend nature of stocks, those stocks are due for a snap-back.
2.  But also contributing to the out-performance is what is not traded in the  Dogs  strategy:  those  stocks  that  are  in  short-term  price  run-up. The average monthly return for the Dogs strategy is 1.81 percent. The average monthly return for the stocks that are in short-term run-up is  1.25  percent.  That's  an  outperformance  by  the  Dogs  stocks  of 0.56 percent a month. If you used margin and traded 100 percent of your  equity  shorting  those  Dow  components  in  short-term  run-up, and traded 100 percent long on those in short-term pull-back, you'd make the 0.56 percent per month, on average. That compounds to a 6.9 percent annual rate-not bad in today's interest rate environment for a very risk-adverse trading approach.

Note that a shortcoming of this analysis is the use of the Dow components at the end of 2011 throughout the study. The use of the actual Dow components that were active each month would have changed the results to an unknown degree. But on the other side of the coin, both strategies were subjected to the identical data streams.

## ■ The Market Trends 5/10/20/30 Percent of the Time

If you're a trend-follower, your strategy should make good money when the market trends and get chopped up a bit when it doesn't. Most people who comment on 'market trendiness' say markets trend less than 50 percent of the time. I've seen 30 percent in print a number of times. In this section, we'll look at a simple way to get a gauge on market trendiness.

Welles  Wilder developed a method to measure market directional movement in his classic book, New Concepts in  T echnical  T rading Systems. Here's what he  said  about  his  method: 'Certainly  one  of  my  most  satisfying  achievements was the day I was actually able to reduce this concept (directional movement) to an absolute mathematical equation.' His Average Directional Movement Index (ADX) logic is coded in every analysis package I know off. Let's look at trendiness in commodities using ADX.

A basket of 56 commodities that included members of the grain, meat, metal, energy, soft, currency, and financial commodities was used with data going back to 1980, if the commodity traded that long. Trendiness was measured by computing the ADX for each market each day over some number of bars, and then counting the number of times the ADX value was greater than 20.  That number was divided by the number of trading days to determine the percentage of the time the market was trending, according to the  ADX metric. Table 10.5 shows the results for 14-, 20-, 40-, and 80-day ADX calculations.

As you scan down the columns, you'll note that the percentages, by year, for the 14-day and 20-day ADX are fairly consistent, while the 40-day and 80-day columns vary considerably from year to year.  Y ou can interpret these numbers to mean that shorter-term trends are relatively plentiful and happen consistently from year to year, while longer-term trends can be few and far between. Additionally, the period from 2000 on has been particularly hard for longer-term trend-following. In those 12 years, there were only three years where the 40-day and 80-day trends were above average. At the same time, 14-day and 20-day trendiness was above average seven out of the 12 years.

TABLE 10.5

Percentage of Days an ADX Value of 20 Is Exceeded

across 56 Commodities

| Year    |   14-Day ADX |   20-Day ADX |   40-Day ADX |   80-Day ADX |
|---------|--------------|--------------|--------------|--------------|
| 1980    |           61 |           46 |           31 |           38 |
| 1981    |           59 |           45 |           20 |           15 |
| 1982    |           64 |           48 |           24 |            8 |
| 1983    |           65 |           49 |           21 |            3 |
| 1984    |           63 |           46 |           21 |            8 |
| 1985    |           69 |           56 |           30 |           10 |
| 1986    |           60 |           43 |           23 |           12 |
| 1987    |           66 |           52 |           25 |            8 |
| 1988    |           61 |           45 |           18 |            9 |
| 1989    |           62 |           44 |           18 |            4 |
| 1990    |           63 |           52 |           26 |            6 |
| 1991    |           59 |           41 |           18 |            8 |
| 1992    |           63 |           48 |           22 |           11 |
| 1993    |           62 |           48 |           22 |           12 |
| 1994    |           59 |           44 |           25 |            6 |
| 1995    |           62 |           47 |           23 |            6 |
| 1996    |           63 |           46 |           20 |            5 |
| 1997    |           66 |           50 |           19 |            5 |
| 1998    |           63 |           46 |           21 |            5 |
| 1999    |           59 |           42 |           19 |            4 |
| 2000    |           63 |           45 |           17 |            4 |
| 2001    |           63 |           48 |           21 |            7 |
| 2002    |           59 |           44 |           23 |            7 |
| 2003    |           66 |           49 |           19 |            6 |
| 2004    |           65 |           48 |           20 |            9 |
| 2005    |           60 |           40 |           11 |            3 |
| 2006    |           54 |           36 |           15 |            3 |
| 2007    |           65 |           47 |           15 |            1 |
| 2008    |           69 |           57 |           34 |           11 |
| 2009    |           54 |           37 |           18 |           11 |
| 2010    |           63 |           48 |           22 |            2 |
| 2011    |           56 |           42 |           21 |            4 |
| Average |           62 |           46 |           21 |            8 |

## ■ Conclusion

The message in this chapter is the same as that in the last: Don't rely on what others say, what you hear, or what is in print. If you have doubts, structure a way to see if the claim is true. Most of the things I've learned about trading have been discovered by accident. I test something interesting and find something else that works, or works so poorly that doing the opposite is the way to go.

## Introduction to Money Management

I n Chapters 4, 5, and 6, we went through a development process that resulted in  two  trading  strategies:  a  short-term  scalping  strategy  for  stocks,  and  a longer-term trend-following strategy for commodities. I discussed the benefits of developing strategies with a limited money management step integrated into the process.  When the strategies are fully developed, they still aren't ready for trading. Another step must be taken to tailor the strategy to the account size to be traded, and the risk/reward appetite of the trader. That step answers questions such as these: What instruments should you trade? How much size do you trade? At what point should you increase your number of instruments, or size? And under what conditions do you cut back market exposure? These issues fall in the realm of money management. The purpose of this chapter is to introduce two money management concepts: position sizing, and small versus large account trading.  Then, in the next four chapters, we will develop specific money management solutions for our stock and commodity strategies.

## ■ Sizing Techniques

Most of the money management literature concerns position sizing. Various methods are used to determine how many shares of stock or how many contracts of a commodity should be bought or sold on a given signal. There

+                (        +                   ,     ( #         &amp;    -       #. &amp;     +   " &amp;     +   "     #$      %                            ! "

175

are two general types of sizing techniques. The fi  rst maintains a fi  xed size throughout the trading. This is the method we used in your system development when we used a $5,000 stock position at each signal for our stock scalping strategy, and one-lot commodity position for our trend-following strategy. When you use a fi  xed size for trading, equity growth is linear. If you make $10,000 a year and start with $50,000, at the end of fi  ve years your equity would be $100,000. Note that in the fi  rst year, your return was 20 percent ($10,000/$50,000), but in the last year your return was only 11.1 percent ($10,000/$90,000). For this reason the appropriate return metric  is  dollars  per  year,  not  percent. And  the  appropriate  draw-down metric is dollar draw-down, not percent draw-down.

The second general form of sizing techniques scales position size as the account changes. In the previous example, where 20 percent was the return the fi  rst  year,  size  would  be  scaled  up  so  the  20  percent  return per year is maintained. At the end of fi  ve years, the equity would be just under $125,000 and the return each year would have been 20 percent. In this case equity is rising exponentially. Figure   11.1 shows the equity run-up for the two strategies.

FIGURE  11.1 Non-Compounded Return (Fixed Size) versus Compounded Return (Increasing Size)

<!-- image -->

So what are some of the sizing techniques that let you take advantage of the exponential growth? We will look at some techniques using the commodity  strategy  that  was  fi  nished  in  Chapter    6  . That  strategy  had  7,113 trades and averaged $387 per trade.

## Optimal F

Optimal f is  a  sizing  method  popularized by Ralph Vince in money management books of the early 1990s. His method is an offshoot of the Kelly criterion and seeks to grow equity at an optimal rate. He actually developed the methodology much earlier than the book publication dates, as it was the  sizing  method  used  by  Larry Williams  when  he  ran  $10,000  to  over $1,000,000 in a 1982 trading contest. Like the Kelly criterion, optimal f does not look to manage risk. It is strictly concerned with growing equity as fast as possible.

To use the optimal f sizing strategy, the following steps must be taken:

- ■ Using the entire sequence of trades, the optimal f trading point must be found. This point can be located in a number of ways, but the simplest is  by brute force. You vary the optimal f fraction from 0.01 to 1.00 in steps of 0.01 until you find the point that maximizes the terminal wealth relative (TWR). The TWR is the product of the individual trade returns as a fraction of the largest loss when traded at a size of the fraction f . An example will clarify. Suppose your strategy has made 10 trades and the biggest loser was $1,000. An individual trade return would be:

Individual trade return = (1 + f * (trade profit/biggest loss))

So if the first trade made $400, and you were using an f value of 0.5, the trade return would be 1.20. That's a 20 percent profit on a starting value of 1. If the first trade lost $400, the trade return would be 0.80, which is a 20 percent loss on a starting value of 1.  When all the individual trade returns are multiplied together, you have the TWR value for that f value.  The optimal f value is the f value that yields the largest  TWR.

- ■ Once you have the optimal f value, you can determine the optimum trade sizing by dividing the largest loss by the optimal f fraction. If optimal f turned out to be 0.25 in our 10-trade example, we would divide the largest loss of $1,000 by 0.25 to get $4,000.  T o trade at optimal f , we would trade one contract for each $4,000 in our account.
- ■ A byproduct of the analysis  is  the  geometric  mean  return  (GMR)  for the strategy. The GMR is the n th root of the TWR at the optimal f point where n is  the number of trades. Vince claims that this is a measure of how good this strategy is at building wealth when a compounding money management sizing technique such as optimal f is  used.  I  have  tried to

verify this claim, but there are issues. The main problem is that the only number used for a trade is its profit or loss. It could have started out with a huge loss and ended up a big winner, or it could have had a large openequity give-back at the end. Neither of these trade problems would show up in the calculations. I think the gain-to-pain ratio on an equity curve that includes the profit or loss of every trade for every bar is a better way to measure the worth of a strategy.

Using the commodity strategies' 7,113 trades,  Table 11.1 summarizes the pertinent 'brute force' runs used to determine the optimal f trading point.

TABLE 11.1 Brute Force Results when Looking for Optimal F .

| Fraction f   |    TWR $ |     GMR |
|--------------|----------|---------|
| 0.88         | 5.63e+53 | 1.01755 |
| 0.89         | 6.41e+53 | 1.01757 |
| 0.90         | 7.02e+53 | 1.01758 |
| 0.91*        | 7.36e+53 | 1.01759 |
| 0.92         | 7.35e+53 | 1.01758 |
| 0.93         | 6.96e+53 | 1.01758 |
| 0.94         | 6.18e+53 | 1.01756 |

* Optimal f point

This table shows that trading at a fraction of 0.91 yields the highest  TWR, $7.53e+53-a staggering amount of money. Across the 7,113 trades, the largest  losing  trade  was  $9,783.  Dividing  the  largest  loser  by  the  optimal f amount of 0.91, we see that we should trade one contract for every $10,750.55 of equity.

When I tried to build an equity curve using this sizing, the strategy went bust after two years.  Trading a contract every $10,750.55 is just too aggressive. It wasn't until I used a value of $22,000 of equity per contract that I got a full run-through.  The statistics for that run were:

Average annual return: 358.1 percent

Average annual max draw-down: 62.8 percent

Max draw-down: 99.3 percent

I  believe  the  breakdown between theory and practice is due to the following:

- ■ Optimal f treats  trades  as  consecutive  instantaneous-outcome  events, just like gambling.  Y ou play one hand, and either win or lose. There's no

change in bankroll until the play is over. In trading, account equity can vary considerably while the trade plays out.

- ■ Optimal f places the next bet after the outcome of the current play is known, and the bankroll value is again fixed. In trading, trades can go on before the others are complete using the current bankroll amount. You can be in a number of losing trades at a time and be way oversized relative to the amount you would have on had the trades completed sequentially.

These points are borne out when I make the same equity run, but only use the closed trades; the results are very close to what optimal f predicts.

The bottom line is that if you make trades one at a time and wait for the first one to complete before entering the next, the optimal f value will hold up much better. And if the trades are relatively short, with equity buildup or loss during the trade period staying very small, optimal f will probably be very accurate. Still, you will go through enormous draw-downs.

## Fixed Risk or Fixed Fractional

This approach seeks to size so that every trade has the same risk. If you're trading  in  a  non-compounding  manner,  the  fixed  risk  will  be  a  dollar amount, like $2,000. If you're trading to compound returns, the fixed risk is a percent of equity, either closed equity, or open- plus closed-trade equity. The risk is based on the distance to the catastrophic stop-in other words, the max loss potential of the trade. The following breakout contrasts the non-compounding and compounding approaches:

Fixed Risk, Non-Compounding Example:

Corn trade with $200 risk per contract

Coffee trade with $1,000 risk per contract

Fixed risk of $1,500 per position

Account equity of $500,000

Solution: 7 corn contracts and 1 coffee contract (number of contracts

rounded down)

Fixed Risk, Compounding Example:

Corn trade with $200 risk per contract Coffee trade with $1,000 risk per contract Fixed risk of 1 percent per position Account equity of $500,000

Solution: 25 corn contracts and 5 coffee contracts With the non-compounding example, you'll note that if account equity were $50,000 or $5,000,000, the solution would be the same.

As a non-compounding example, let's compare the solution we had trading our commodity system with a one-lot at each signal versus a number of fixed risk amounts.  Table 11.2 shows the comparison.

TABLE 11.2 Comparison of Non-Compounding Sizing Approaches

| Approach          |   Average Annual Return (%) |   Average Annual Max Draw-Down (%) |   Max Draw-Down (%) |   Gain-to-Pain Ratio |
|-------------------|-----------------------------|------------------------------------|---------------------|----------------------|
| 1-Lot             |                      85,315 |                             34,419 |              74,977 |                 2.48 |
| $1,500 Fixed Risk |                      71,635 |                             30,549 |              51,862 |                 2.35 |
| $1,750 Fixed Risk |                      92,610 |                             37,267 |              66,558 |                 2.49 |
| $2,000 Fixed Risk |                     114,873 |                             43,043 |              74,931 |                 2.67 |
| $2,250 Fixed Risk |                     128,978 |                             50,314 |              86,543 |                 2.56 |
| $2,500 Fixed Risk |                     153,192 |                             58,367 |             104,375 |                 2.62 |

Table  11.2  shows  that  equalizing  the  risk  across  all  trades  can  lead  to a better trading solution than buying a one-lot at each trade. As the fixed risk number is raised further, the gain-to-pain ratio steadies out to a value of about 2.75. The variability is caused by the fractional contracts that are dropped in the rounding process. Also, for the lower fixed risk numbers, not all trades were taken, because the risk of even a one-lot exceeded the threshold of $1,500 or $2,000.

Let's now look at the compounding fixed-risk solution for a number of fixed-risk percentage values. Table 11.3 again uses all 7,113 trades in the commodity strategy.

| TABLE 11.3               | Performance when Fixed Risk Is Used in a Compounding Approach   | Performance when Fixed Risk Is Used in a Compounding Approach   | Performance when Fixed Risk Is Used in a Compounding Approach   | Performance when Fixed Risk Is Used in a Compounding Approach   |
|--------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|
| Percent Risked per Trade | Average Annual Return (%)                                       | Average Annual Max Draw-Down (%)                                | Max Draw-Down (%)                                               | Gain-to-Pain Ratio                                              |
| 1                        | 79.7                                                            | 19.9                                                            | 39.8                                                            | 4.00                                                            |
| 2                        | 162.6                                                           | 32.3                                                            | 61.6                                                            | 5.04                                                            |
| 3                        | 243.0                                                           | 41.4                                                            | 75.4                                                            | 5.87                                                            |
| 4                        | 316.9                                                           | 48.6                                                            | 84.5                                                            | 6.52                                                            |
| 5                        | 378.4                                                           | 54.0                                                            | 90.7                                                            | 7.01                                                            |
| 6                        | 424.3                                                           | 57.8                                                            | 95.4                                                            | 7.34                                                            |
| 7                        | 447.2                                                           | 61.5                                                            | 98.8                                                            | 7.27                                                            |

Table 11.3 raises a couple of interesting points:

- ■ The more risked per trade, the better the trading solution, as measured by  the  gain-to-pain  ratio. This  is  in  contrast  to  the  non-compounding fixed-risk case, where the gain-to-pain steadies out at sizes where fractional contracts cease to be a factor.
- ■ The fixed-risk solution is better than the optimal f solution. Table 11.4 compares the two runs.

## TABLE 11.4 Comparison of Optimal f and Fixed Risk Solutions

| Method                           |   Average Annual Return |   Average Annual Max Draw-Down |   Max Draw-Down |   Gain-to-Pain Ratio |
|----------------------------------|-------------------------|--------------------------------|-----------------|----------------------|
| Optimal f : $22,000 per contract |                   358.1 |                           62.8 |            99.3 |                 5.70 |
| Fixed risk: 7 percent            |                   447.2 |                           61.5 |            98.8 |                 7.27 |

Clearly, relating size to the risk of the trade is a better approach than risking the same number of contracts for each trade at a given equity value: The return and gain-to-pain ratios are higher, and both draw-down metrics are less. This approach, with small variations, is the approach most money managers use to size their trades.

## Fixed Ratio

This approach was detailed by Ryan Jones in his book, The  T rading Game. The approach increases size linearly at ever-increasing steps of equity. The steps increase each time by the delta amount, the amount your account equity must grow before you resize. If you start trading a $10,000 account and choose a delta value of $2,000, you trade one contract per trade until your account grows to $12,000. At that point the step is increased by the delta value to $4,000, and two contracts per trade are taken. Then when the account reaches $16,000, you can trade three contracts.

You can see from the way contracts are added that the biggest risk is assumed early on. If each trade has a $500 risk, you start out risking $500 on a $10,000 account, or 5 percent.  When the account hits the value of $12,000 and you're trading two contracts, the risk is 8.3 percent. At $16,000 and 3 contracts, the risk is 9.375 percent. At the next level, the risk decreases to 9.09 percent and continues to decrease from that point on. If you averaged $300 per trade and made 1,000 trades, at the end of the sequence, you'd only be risking less than 0.4 percent a trade, not even one-tenth of the level you started at.  Y ou'll also note that the smaller the delta value, the greater the risk. Using a delta of $1,000, the risk peaks at 12.5 percent per trade at four contracts, versus the peak of 9.375 percent at three contracts for the case where delta is $2,000.

Using our commodity strategy,  Table 11.5 shows the results when trading at a variety of delta values.

TABLE 11.5 Fixed Ratio Trading at Various Delta Levels

| Delta   |   Average Annual Return (%) |   Average Annual Max Draw-Down (%) |   Max Draw-Down (%) |   Gain-to-Pain Ratio |
|---------|-----------------------------|------------------------------------|---------------------|----------------------|
| $ 1,000 |                        28.8 |                               18.8 |                56.7 |                 1.53 |
| $ 2,000 |                        26.2 |                               16.2 |                47.6 |                 1.61 |
| $ 3,000 |                        24.7 |                               14.8 |                42.5 |                 1.67 |
| $ 5,000 |                        22.8 |                               13.2 |                36.3 |                 1.73 |
| $10,000 |                        20.3 |                               11.2 |                28.7 |                 1.81 |
| $20,000 |                        18.0 |                                9.4 |                22.3 |                 1.91 |
| $30,000 |                        16.7 |                                8.4 |                19.1 |                 1.99 |

This is a compounding approach, but the gain-to-pain ratios are lower than the two non-compounding approaches we looked at (one-lot trading and  fixed  risk). This  solution  doesn't  come  close  to  competing  with  the compounding fixed-risk approach. I think the problem is the very unequal approach to risk. At the start of a run the risk per trade is many times what it is at the end. Since you never know when draw-down will hit, why risk way more at any point in the trade stream?

## Sizing Summary

There's a reason most money managers use a fixed-risk trading approach. It's because it is a very fast way to build equity, and risk is equalized on every position by the sizing. Additionally, you can tailor the risk level so that draw-down is within your risk tolerance envelope. Given the equity buildup advantage of compounding equity versus a non-compounding approach, you may wonder why anyone would consider using a fixed size for trading. The answer is that no one probably would unless they have to. But the fact of the matter is, most traders have to. The reason is that their account size is too small to see the benefits of variable sizing.

## ■ Small versus Large Account Size

The best traditional money management sizing approach I know is to risk a small percentage of equity on each trade. But sometimes your account size won't let you do that. If you're trading commodities and your system has a $1,000 stop, the risk for one trade on a $10,000 account is 10 percent.  That's not a small risk to take on one trade. A small account is then defined as one that cannot be traded risking a small fixed percentage of equity on each trade.

This  point  illustrates  the  important  difference  between  small-account and large-account traders: Small-account traders are forced to take greater relative risk than large-account traders. Small-account traders are always a small number of adverse trades away from a margin call, while large-account traders who risk a small percentage of equity on each trade are always a very large number of adverse trades away from a margin call.

Because a small-account trader is on the edge, money management is crucial to success. It should be the aim of every small-account trader to grow his equity to large-account status so he can enjoy the benefits of large-account trading. Besides walking in from the edge, the large-account trader enjoys money management strategies not available to the small-account trader. In the remainder of this chapter, the appropriate performance metrics will be detailed for small accounts and large accounts.

## Small-Account Performance Metrics

There are many ways to measure the success of a trading system and the money management strategies used in trading it. The best methods seek to measure both return and risk. Small-account traders should be most concerned with risk because that is what will drive them from the game. In this section, three measures of risk will be examined: open- and closed-trade draw-down,  closed-trade  draw-down,  and  start-trade  draw-down.  Most traders use draw-down as a measure of the capital required to trade a given methodology. The maximum historical draw-down (sometimes multiplied by some factor to account for a future larger draw-down) plus margin requirements are deemed the requirements to successfully trade the methodology.  As will be shown, the conventional open- and closed-trade draw-down metric is really meaningless to the small-account trader. That's because it inflates the risk associated with trading a system and a given money management strategy. The closed-trade draw-down is a better measure of risk, but the best measure is a metric I've developed: start-trade draw-down. This is the draw-down a trader can expect to see when a given system and strategy are started.

On the reward side, annual return is a meaningful metric, but a better metric for the small-account trader is start-trade return. This is the average fi  rst-year return a trader can expect when he or she starts trading the system.

## Small-Account Metrics: Open- and Closed-Trade Draw-Down

If  the  equity  curve  is  built  by  taking  the  sum  of  closed-trade  equity  and  the profi  ts/losses in all open positions, the resultant equity curve is an open- and closed-trade equity curve. Open- and closed-trade equity corresponds to the bottom-line fi  gure on your brokerage statement each day . If a system and money management strategy are traded for a length of time, the resultant open- and closed-trade equity curve can be examined for draw-downs. A draw-down is defi  ned as a peak-to-trough equity drop, as shown in Figure   11.2  .

Figure   11.2 shows a number of draw-downs. The largest is used by many traders as a measure of the reserves above margin requirements needed to trade the strategy . For strategies that use trend-following systems, this is usually not true. A large part of the draw-down can be due to open-equity profit retracement. T o illustrate this, suppose that the graph is not the result of a number of trades, but the result of one trade. In that case, you got in the trade, had a drawdown of $1,000, built up to a trade profit of $4,000, had another draw-down of $2,000, built up an additional $3,000 of profit over the initial peak, and then ended the trade with a $3,000 draw-down to cash out the trade with a $4,000 profit. As a small-account trader , the worst position you were in was at the start when you went $1,000 below your starting equity (the start-trade draw-down for this trade).  The biggest draw-down of $3,000 was out of open-equity profits. It hurt to give back that $3,000, but that $3,000 draw-down had nothing to do with the minimum capital required to execute the trade. The capital required was start-trade draw-down ($1,000) plus the margin requirements.

FIGURE  11.2 Open- and Closed-Trade Equity Growth

<!-- image -->

Thus, open- and closed-trade draw-down figures can be misleading to a small-account trader. Using that draw-down figure plus margin requirements as the minimum required to trade the strategy will usually overstate the equity required.

## Small-Account Metrics: Closed-Trade Draw-Down

A closed trade equity curve is formed by adding the profit/loss from each trade as it ends to the previous equity, and plotting the result on the date the trade is liquidated. This draw-down figure will not include open-equity profit retracement since the trade results are not added to equity until the day the trade ends, but it also neglects to show if a winning trade was ever in a losing position. Since open-equity retracement on good trades can be much  larger  than  the  negative  segments  of  winning  trades,  closed-trade draw-down is a better reflection of the reserves needed to trade a strategy, but it still isn't exactly what the small-account trader is interested in.

## Small-Account Metrics: Start-Trade Draw-Down

This is the risk metric that the small-account trader should be most interested in. It is found by looking at the open- and closed-trade equity curve and finding the lowest equity point below the starting equity . In the equity curve in Figure 11.2, the start-trade draw-down would be $1,000. This is the figure a small-account trader is interested in because it, plus margin requirements, is the amount an account must have in starting equity to trade the methodology successfully , if the trader started trading at the start of the equity run. If an equity curve is generated at the start of each trade in the methodologies' hypothetical history , all the start-trade draw-downs can be found.  Thus, if there were 200 trades in the methodology back-testing, 200 equity curves would be generated and the start-trade draw-down for each one found.  This is extremely useful information to the small-account trader, because the largest start-trade drawdown can be found, as well as statistics on the entire start-trade draw-down distribution. The following example will illustrate the usefulness of start-trade draw-down and contrast it with the other two draw-down metrics.

## Small-Account Metrics: Draw-Down Example

The  open- and closed-trade equity curve shown in Figure   11.3 was built from the one-lot trades signaled by the Donchian trend-following commodity system developed in Chapters   4 through 6.

FIGURE  11.3 Donchian System Open- and Closed-Trade Equity Curve

<!-- image -->

The following are the draw-down metrics:

Average yearly maximum open- and closed-trade draw-down: $29,643

Average yearly maximum closed-trade draw-down: $20,552

Average yearly maximum start-trade draw-down: $22,136

Maximum open- and closed-trade draw-down: $81,150

Maximum closed-trade draw-down: $44,632

Maximum start-trade draw-down: $48,781

Notice that the closed-trade draw-down fi  gures correspond better to the start-trade average yearly and maximum results than the open- and closedtrade draw-down fi  gures. It is also evident that the open- and closed-trade draw-down fi  gures well overstate the amount required to trade this portfolio.

Byproducts  of  the  start-trade  analysis  are  two  useful  start-trade  graphs. These graphs show the distribution of all the start-trade draw-downs and oneyear profi  ts over the portfolio's history . Figure   11.4 shows an example of these distributions for the portfolio example used to illustrate draw-down.

FIGURE  11.4 Start-Trade Draw-Down/Start-Trade Profi  t Distributions

<!-- image -->

Looking  at  the  draw-down  graph  (top),  the  x-axis  is  the  cumulative percentage  probability  of  occurrence,  and  the  y-axis  is  the  draw-down. Entering at 70 percent, intersecting the plot, and reading over to the left, we see that there is a 60 percent probability that a trader will experience a  $7,400  or  less  start-trade  draw-down  when  this  portfolio  is  traded. The profit graph (bottom) is read the same way. A trader has a 10 percent chance his first-year  profits  will  be  $31,500  or  less;  conversely,  he  has  a 90 percent chance they will be $30,500 or more.

These graphs are powerful tools the small-account trader can use to gauge risk and reward when deciding what trading plan to implement.

## Large-Account Performance Metrics

Where the small-account trader should be most interested in start-trade draw-down as a survival metric, the large-account trader should be more interested in the reward he can receive for the risk he takes. An appropriate risk measure is the percentage of draw-down, both largest and annual, while annual percent return is a good return metric.

## Large-Account Performance Metric: Percentage of Draw-Down

The open- and closed-trade equity curve is used to yield the draw-down percent. As before, the peak-to-trough is the draw-down, but rather than use the dollar draw-down, a percentage is formed by dividing the draw-down dollar amount by the peak equity amount at the start of the draw-down.

The  largest  percent  draw-down  is  one  useful  metric,  and  another  is formed by finding the n -largest percentage draw-downs and dividing by n . If n is the number of years in the equity curve, this metric can be interpreted as the average max annual percentage draw-down, even though some years had more than one of the historical draw-downs, and some none.

## Large-Account Performance Metric: Annual Percent Return

One way to compute the average annual percent return is to take the starting and ending equity, and compute the average annual percent return using the following formula:

<!-- formula-not-decoded -->

Another useful way to compute annual percent return is to compute the percent return for each individual return year and average the results. Note that the results of the two methods will probably differ. If, for example, an account started at $100,000, ended the first year at $100,000, and ended the second year at $400,000, the annual percent return formula will yield 100 percent because on average the account doubled each year. But computing the annual return using the yearly returns, you'd see a 150 percent return (no gain the first year and 300 percent the second year).

## ■ Conclusion

This chapter introduced two money management concepts: position sizing, and  the  significant  difference  between  small-account  trading  and  largeaccount  trading.  Chapter  12  and  Chapter  14  will  be  devoted  to  finding small-account money management and large-account money management solutions for our commodity system. Chapter 13 and Chapter 15 will do the same for our stock system. In those chapters a variety of money management techniques will be explored to further enhance the tradeability of our strategies.

## Traditional Money Management Techniques for Small Accounts: Commodities

I n this chapter, small account money management techniques will be illustrated using the commodity strategy developed in Chapters 4 through 6. Then, specific money management rules will be developed for account sizes ranging from $20,000 to $100,000.

It is important to remember that small-account traders should be most concerned about limiting risk. The techniques presented in this chapter all look to limit risk but some, when applied to a given strategy, won't increase the  gain-to-pain  metric. That  doesn't  mean  they  shouldn't  be  adopted  as part of your trading solution. Look at the risk reduction they offer as the final arbiter of whether they should be used or not.

191

## ■ Diversification

To minimize risk, it is best to trade a number of independent commodities. Commodities are independent of each other if there is no tendency for one to rise or fall when the other does. Dependent commodities, such as those within a commodity group, tend to move in tandem. If trading capital limits the number of commodities that can be traded simultaneously, avoid trading a number of commodities from the same group. If a draw-down starts in one, it is likely to occur in the others.

The following example will highlight this point. Looking at the historical performance of the commodities in our Donchian commodity strategy, the currency group has performed well. Suppose the two sets of commodities in  T able 12.1 are compared.

TABLE 12.1 Non-Diversified versus Diversified Portfolios

| Non-Diversified Commodities   |   Total Profit ($) | Diversified Commodities   |   Total Profit ($) |
|-------------------------------|--------------------|---------------------------|--------------------|
| Japanese Yen                  |             88,475 | Soybeans                  |             57,025 |
| Swiss Franc                   |             81,512 | Feeder Cattle             |             25,687 |
| Dollar Index                  |            104,734 | Cotton                    |            100,590 |
| Euro-Currency                 |             51,744 | Palladium                 |            101,279 |
| Canadian Dollar               |             26,179 | Crude Oil                 |             61,059 |
| Australian Dollar             |             22,470 | Dollar Index              |            104,734 |
| British Pound                 |            117,225 | 10-Year Notes             |             67,609 |
| Mexican Peso                  |             36,549 |                           |                    |
| Total Profit                  |            528,888 |                           |            517,983 |

The two sets make about the same profits over the time frame from 1980 through December 2011, but the non-diversified set contains all currencies,  and  the  other  a  set  of  commodities  that  is  nominally  uncorrelated. Building an equity curve and performing a start-trade draw-down analysis, Table 12.2 shows trading results for each portfolio.

| TABLE 12.2      | Trading Results: Diversified versus Non-Diversified Portfolios   | Trading Results: Diversified versus Non-Diversified Portfolios   |
|-----------------|------------------------------------------------------------------|------------------------------------------------------------------|
| Portfolio       | Average Start-Trade Draw-Down ($)                                | Max Start-Trade Draw-Down ($)                                    |
| Non-Diversified | 4,305                                                            | 19,017                                                           |
| Diversified     | 3,203                                                            | 14,998                                                           |

These  results  illustrate  the  diversification  advantage. The  average  max draw-down is about 25 percent lower in the diversified set, and the maximum draw-down is about 20 percent less than the non-diversified portfolios', but the total profit is about the same. Diversification is a powerful money management technique for the small-account trader.

## ■ Limiting Group Exposure, First-N-in-a-Group Trading

A diversification tactic that the small-account trader can use is firstN -in-agroup trading. Rather than select one commodity from each group and wait for a signal in that commodity, select all the commodities you are willing to trade in that group and take the first N signals that come up, where N is the exposure your account size and risk-taking makeup dictate. Table 12.3 shows the pertinent trade data for each of the 56 commodities in the basket.

TABLE 12.3 Donchian System: Performance by Commodity

| Commodity             |   Winning Trades |   Losing Trades |   Total Profit ($) |   Profit-Per-Trade ($) |
|-----------------------|------------------|-----------------|--------------------|------------------------|
| Corn                  |               79 |             111 |             25,675 |                    135 |
| Soybeans              |               71 |              94 |             57,025 |                    345 |
| Bean Meal             |               74 |             108 |             52,490 |                    288 |
| Bean Oil              |               90 |             100 |             52,182 |                    274 |
| Wheat                 |               69 |             123 |              9,562 |                     49 |
| KC Wheat              |               66 |             114 |             29,825 |                    165 |
| Rough Rice            |               53 |              73 |             70,479 |                    559 |
| Live Cattle           |               71 |             142 |             -4,271 |                    -21 |
| Lean Hogs             |               77 |             143 |             -1,520 |                     -7 |
| Feeder Cattle         |               76 |             113 |             25,687 |                    135 |
| Coffee                |               37 |              40 |             50,493 |                    655 |
| Cotton                |               80 |              92 |            100,590 |                    584 |
| Orange Juice          |               79 |             114 |             56,302 |                    291 |
| Lumber                |               62 |              81 |             75,514 |                    528 |
| Cocoa                 |               60 |             136 |            -16,080 |                    -83 |
| Sugar                 |               79 |              88 |             55,238 |                    330 |
| Copper                |               65 |              93 |             21,300 |                    135 |
| Palladium             |               59 |              96 |            101,279 |                    653 |
| Silver                |               55 |              87 |            110,074 |                    775 |
| Gold                  |               56 |              88 |             54,440 |                    378 |
| Platinum              |               62 |             120 |              4,579 |                     25 |
| London Copper         |               44 |              54 |             41,545 |                    423 |
| London Aluminum Alloy |               40 |              78 |             39,240 |                    332 |
| London Aluminum       |               48 |              63 |             39,062 |                    351 |

## TABLE 12.3

| Commodity           |   Winning Trades |   Losing Trades |   Total Profit ($) |   Profit-Per-Trade ($) |
|---------------------|------------------|-----------------|--------------------|------------------------|
| London Nickel       |               33 |              56 |             81,165 |                    911 |
| Crude Oil           |               52 |              60 |             61,059 |                    545 |
| Heating Oil         |               69 |              81 |             94,290 |                    628 |
| Reformulated Gas    |               50 |              63 |             81,408 |                    720 |
| Mini Natural Gas    |               20 |              30 |             15,675 |                    313 |
| Brent Crude         |               44 |              41 |             71,139 |                    836 |
| Japanese Yen        |               38 |              32 |             88,475 |                   1263 |
| Swiss Franc         |               43 |              33 |             81,512 |                   1072 |
| Canadian Dollar     |               61 |             107 |             26,179 |                    155 |
| British Pound       |               40 |              48 |            117,225 |                   1332 |
| Dollar Index        |               57 |              68 |            104,734 |                    837 |
| Australian Dollar   |               45 |              74 |             22,470 |                    188 |
| Mexican Peso        |               45 |              57 |             36,549 |                    358 |
| Euro-Currency       |               14 |              12 |             51,774 |                   1991 |
| 30-Year Bonds       |               47 |              67 |             43,500 |                    381 |
| 10-Year Notes       |               72 |              92 |             67,609 |                    412 |
| 5-Year Notes        |               61 |              78 |             52,085 |                    374 |
| 2-Year Notes        |               54 |              62 |             51,562 |                    444 |
| Eurodollar          |               80 |              90 |             66,399 |                    390 |
| Australian Bond     |               66 |              93 |             53,733 |                    337 |
| Canadian Govt. Bond |               60 |              76 |             37,503 |                    275 |
| Euro Bund           |               41 |              32 |             93,161 |                   1276 |
| Long Gilt           |               36 |              39 |             50,070 |                    667 |
| Spanish Bond        |               45 |              51 |             46,245 |                    481 |
| Simex JGB Bond      |               50 |              70 |             26,562 |                    221 |
| Hang Seng Index     |               19 |              20 |             37,149 |                    952 |
| Dax Index           |               15 |              23 |              9,075 |                    238 |
| Mini S&P            |               56 |              92 |              8,750 |                     59 |
| Mini Russell 2000   |                1 |               4 |              1,809 |                    361 |
| Mini Midcap         |               28 |              44 |              7,589 |                    105 |
| Mini Nasdaq         |               30 |              38 |             20,725 |                    304 |
| Nikkei              |               52 |              53 |             98,675 |                    939 |
| All Trade Average   |             2976 |            4137 |          2,756,675 |                    387 |
| Long Trade          |             1594 |            2086 |          1,895,123 |                    514 |
| Short Trade         |             1382 |            2051 |            861,542 |                    250 |

Looking over the basket, Table 12.4 shows a breakout of the best commodities in each group followed by the second-best commodities. 'Best' is somewhat subjective, but total profit was the base criteria with liquidity and volatility as considerations.

| TABLE 12.4   | Best Commodities              |
|--------------|-------------------------------|
| Group        | 'Best' Commodities            |
| Grains       | Soybeans, Rough Rice          |
| Meats        | Feeder Cattle, N/A            |
| Softs        | Cotton, Lumber                |
| Metals       | Silver, Palladium             |
| Currencies   | Dollar Index, British Pound   |
| Energies     | Heating Oil, Reformulated Gas |
| Financials   | 10-Year Note, Euro Bond       |

First the best commodities were traded as a portfolio (baseline portfolio) and a one-lot trade was taken in each. Then the portfolio was augmented (augmented portfolio) with the second-tier commodities and traded firstone-in-a-group, meaning only one of the two commodities in each group could be in a trade at the same time. If the second commodity in that group signaled a trade while the first was still in a trade, that trade was bypassed. Table 12.5 shows the results of each run.

TABLE 12.5 Diversification Example: FirstN -in-a-Group

| Portfolio          |   Average First-Year Return ($) |   Average Start-Trade Draw-Down ($) |   Max Start-Trade Draw-Down ($) |   Gain-to-Pain Ratio |
|--------------------|---------------------------------|-------------------------------------|---------------------------------|----------------------|
| Baseline Portfolio |                          15,653 |                               3,808 |                          17,284 |                 4.09 |
| Augmented          |                          19,943 |                               3,857 |                          20,752 |                 5.17 |

These results show that even adding second-tier commodities and trading first-in-a-group improves results when measured by the gain-to-pain ratio. The reasons this strategy outperforms the fixed portfolio strategy are:

- ■ The benefits of diversification are enhanced since most groups will always have a trade ongoing in this strategy, while a group might not be represented for a significant period of time in the fixed portfolio strategy.
- ■ More trades will be made over the same time frame, which will lead to faster equity growth.

There's one more point that can be made with these portfolios: It's better  to  diversify  with  second-tier  commodities  than  to  double-up  on  the top-tier set. That point is illustrated in Table 12.6. The table compares the performance attained by trading two contracts at each signal with the baseline portfolio, which contains the top-tier commodities, versus one trade at each signal for the augmented commodity portfolio.

| TABLE 12.6          | Diversification Example: Two-Lot of Top Tier Commodities versus One-Lot of Augmented Portfolio   | Diversification Example: Two-Lot of Top Tier Commodities versus One-Lot of Augmented Portfolio   | Diversification Example: Two-Lot of Top Tier Commodities versus One-Lot of Augmented Portfolio   | Diversification Example: Two-Lot of Top Tier Commodities versus One-Lot of Augmented Portfolio   |
|---------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Portfolio           | Average First- Year Return ($)                                                                   | Average Start-Trade Draw-Down ($)                                                                | Max Start-Trade Draw-Down ($)                                                                    | Gain-to-Pain Ratio                                                                               |
| Baseline Portfolio  | 31,306                                                                                           | 7,616                                                                                            | 34,568                                                                                           | 4.09                                                                                             |
| Augmented Portfolio | 30,263                                                                                           | 4,003                                                                                            | 17,180                                                                                           | 7.56                                                                                             |

Again, diversification is a powerful tactic for the small-account trader. By adding second-tier commodities, the gain-to-pain ratio for the augmented portfolio is almost 85 percent higher than the baseline portfolio when trading two lots of the best commodities in each group at each signal.

## ■ Limit Trade Risk on Entry

When a  trade  is  originated,  the  trade  risk  is  the  distance,  converted  to dollars, from the entry point to the catastrophic stop loss point; that is, the maximum dollar amount that can be lost on the trade. Because our threestandard-deviation stop is volatility-based, some trades will have a relatively small  dollar  risk  and  some  a  relatively  large  dollar  risk.  Using  the 'limit trade risk entry' money management strategy, trades with a high trade risk are bypassed.

Table 12.7 shows the results of bypassing trades with a catastrophic stop value that exceeds a certain limit. All 56 commodities were used for the analysis.

| TABLE 12.7       | Limit Trade Risk on Entry     | Limit Trade Risk on Entry         | Limit Trade Risk on Entry     | Limit Trade Risk on Entry   |
|------------------|-------------------------------|-----------------------------------|-------------------------------|-----------------------------|
| Trade Risk Limit | Average First-Year Return ($) | Average Start-Trade Draw-Down ($) | Max Start-Trade Draw-Down ($) | Gain-to-Pain Ratio          |
| All Trades       | 76,134                        | 9,597                             | 64,996                        | 7.93                        |
| $3,000           | 64,257                        | 8,255                             | 46,652                        | 7.78                        |
| $2,000           | 54,674                        | 6,000                             | 34,327                        | 9.11                        |
| $1,000           | 24,750                        | 3,524                             | 23,773                        | 7.02                        |

The results shows that bypassing trades with an initial stop greater than $2,000 away from the entry price increases the gain-to-pain ratio from the baseline 7.93 to 9.11, a 15 percent improvement.

## ■ Limit Open-Trade Risk

At any point in time, open-trade risk can be defined as the distance from the current price to the stop price converted to dollars. If an open position is in either profit or loss and its current price is $4,000 from its catastrophic stop point, its trade risk at that point is $4,000.  There is always a risk of giving part or all of it back. This money management technique closes the trade when a certain dollar amount of open-trade risk is reached. Note that this can also be looked at as a form of profit-taking. T able 12.8 shows performance when trades are exited if they reach a certain dollar amount of open-trade risk.

## TABLE 12.8 Limit Open-Trade Risk

Table 12.8 shows that exiting trades when the trade risk grows above $6,000 is a better trading solution than the baseline, as indicted by the gainto-pain ratio of 8.94. In fact, all runs that closed trades with greater than $6,000 of open-trade risk outperformed the baseline.

| Open-Trade Risk Threshold for Trade Exit   |   Average First-Year Return ($) |   Average Start-Trade Draw-Down ($) |   Max Start-Trade Draw-Down ($) |   Gain-to-Pain Ratio |
|--------------------------------------------|---------------------------------|-------------------------------------|---------------------------------|----------------------|
| No Exit                                    |                          76,134 |                               9,597 |                          64,996 |                 7.93 |
| > $10,000                                  |                          71,908 |                               8,603 |                           9,358 |                 8.36 |
| > $8,000                                   |                          71,334 |                               8,118 |                          45,983 |                 8.78 |
| > $6,000                                   |                          61,890 |                               7,822 |                          49,623 |                 8.94 |
| > $4,000                                   |                          49,021 |                               7,365 |                          49,021 |                 6.66 |

## ■ Limit Total Portfolio Open-Trade Risk

At certain times, it seems like all the groups are moving together . I remember thinking in the second half of 2008 that if I knew how one energy , or one financial, or one stock index, or one metal was going to close for the day , I' d know how every commodity in all those groups was going to close.  Times like that are opportunities to make a fortune, or get crushed. Since a small-account trader must control risk to stay in the game, something should be done to limit exposure when a number of groups are moving up and down together in large sweeps.

This  small-account  money  management  technique  looks  at  the  opentrade risk across all ongoing trades, and if the sum of the individual opentrade risks exceeds a dollar limit, the trade with the largest open-trade risk is closed. Again, note that this technique is also a form of profit-taking: The trade with the largest open-trade risk will be deeply in profit if the portfolio limit is  hit. T able  12.9  shows  the  performance for a number of portfolio open-trade limits.

TABLE 12.9 Limit Portfolio Open-Trade Risk

| Portfolio Open-Trade Risk Threshold for Exit of a Trade ($)   |   Average First- Year Return ($) |   Average Start-Trade Draw-Down ($) |   Max Start-Trade Draw-Down ($) |   Gain-to-Pain Ratio |
|---------------------------------------------------------------|----------------------------------|-------------------------------------|---------------------------------|----------------------|
| No Exit                                                       |                           76,134 |                               9,597 |                          64,996 |                 7.93 |
| > 100,000                                                     |                           75,677 |                               9,592 |                          64,996 |                 7.89 |
| > 80,000                                                      |                           73,744 |                               9,579 |                          64,996 |                 7.70 |
| > 70,000                                                      |                           69,254 |                               9,313 |                          60,806 |                 7.44 |

Limiting portfolio open-trade risk did not improve the trading solution in terms of the gain-to-pain ratio, but the risk metrics of average start-trade draw-down and max start-trade draw-down were reduced. This technique will be a tool we'll try and use as we proceed to find small-account trading solutions for various account sizes.

## ■ Limit Total Number of Open Trades

As the number of open trades varies in real-time trading, the biggest risk/ reward  opportunities  occur  when  you  have  a  relatively  large  number  of trades on. This small-account money management technique looks to limit risk exposure by capping the number of open trades.  Table 12.10 shows the performance when the number of open trades is limited.

| TABLE 12.10               | Limiting the Total Number of Open Trades   | Limiting the Total Number of Open Trades   | Limiting the Total Number of Open Trades   |                    |
|---------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------|
| Max Number of Open Trades | Average First-Year Return ($)              | Average Start-Trade Draw-Down ($)          | Max Start-Trade Draw-Down ($)              | Gain-to-Pain Ratio |
| All Trades                | 76,134                                     | 9,597                                      | 64,996                                     | 7.93               |
| 40                        | 75,904                                     | 9,595                                      | 64,996                                     | 7.91               |
| 30                        | 71,253                                     | 9,471                                      | 64,996                                     | 7.52               |
| 20                        | 56,762                                     | 8,312                                      | 55,932                                     | 6.83               |

Again, the gain-to-pain ratio was not improved by limiting the total number  of  open  trades  at  a  time,  but  look  at  the  steady  decrease  in  average start-trade draw-down as the number of trades allowed is decreased. The max start-trade draw-down also shows a healthy decrease as the number is more severely curtailed. Another technique we'll try to use when we build specific trading solutions for the small account trader is limiting the number of trades that are on at a time.

## ■ Fixed Portfolios

When tailoring a money management approach for small accounts, it is helpful to build portfolios from the bottom up rather than the top down. Start with the best one or two commodities in each group and use small-account money management techniques to get the best solution you can. As equity grows, a larger portfolio can be fashioned by building on the first, rather than starting all over again. In this section, portfolios for various account sizes will be presented from small to relatively large. Each portfolio uses risk limitation, diversification across the groups, and a firstN -in-a-group trading approach. The smallest portfolio was built by selecting the lowest-risk, best-performing commodities. Risk was always considered first. Successful portfolios build on the last by adding more commodities to each group.

## Starter Portfolio Commodities

The smallest portfolio contains the following, shown in  Table 12.11.

| TABLE 12.11   | Starter Portfolio Commodities   |             |
|---------------|---------------------------------|-------------|
| Group         | Starter Portfolio Commodities   |             |
| Grains        | Soybeans, Rough Rice            | 199         |
| Meats         | Feeder Cattle                   |             |
| Softs         | Cotton, Lumber                  |             |
| Metals        | Silver, Palladium               |             |
| Currencies    | Dollar Index, British Pound     | COMMODITIES |
| Energies      | Heating Oil, Reformulated Gas   |             |
| Financials    | Euro Bond, Euro Dollar          |             |

## Starter Portfolio Small-Account Money Management

The starter portfolio uses the small-account money management techniques and limits shown in  Table 12.12.

| TABLE 12.12                              | Starter Portfolio Money Management Techniques and Limits   | Starter Portfolio Money Management Techniques and Limits   |
|------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|
| Small-Account Money Management Technique | Small-Account Money Management Technique                   | Used?/Limit                                                |
| First- N -in-a-Group                     | First- N -in-a-Group                                       | No/N/A                                                     |
| Limit Trade Risk on Entry                | Limit Trade Risk on Entry                                  | Yes/$2,000                                                 |
| Limit Max Open-Trade Risk                | Limit Max Open-Trade Risk                                  | Yes/$5,500                                                 |
| Limit Max Portfolio Risk                 | Limit Max Portfolio Risk                                   | Yes/$15,000                                                |
| Limit Max Number of Trades               | Limit Max Number of Trades                                 | No/N/A                                                     |

## Starter Portfolio Performance

The starter portfolio has these summary start-trade statistics:

Average fi  rst-year profi  t: $18,389

Average start-trade draw-down: $2,843

Max start-trade draw-down: $12,023

Figure   12.1 shows the start-trade graphs for the starter portfolio:

<!-- image -->

FIGURE  12.1 Start-Trade Statistics for Starter Portfolio

Looking at the top graph, starting to trade the starter portfolio at any point in time over the period 1980 to 2011, a trader would face the following risk profi  le:

- ■ There was a 100 percent chance start-trade draw-down would have been less than $12,023.

- ■ There was an 80 percent chance start-trade draw-down would have been less  than  $5,000.  Conversely, there was a 20 percent chance it would have been greater.
- ■ There was a 60 percent chance start-trade draw-down would have been less  than  $2,600.  Conversely, there was a 40 percent chance it would have been greater.
- ■ There was a 40 percent chance start-trade draw-down would have been less than $800. Conversely, there was a 60 percent chance it would have been greater.
- ■ There was a 20 percent chance start-trade draw-down would have been less than $303. Conversely, there was an 80 percent chance it would have been greater.

Looking at the bottom graph, starting to trade the starter portfolio at any point in time over the period 1980 to 2011, a trader would face the following profitability probabilities at the one year from start-trade date:

- ■ There was a 100 percent chance that first-year profit would have been less than $53,000.
- ■ There was an 80 percent chance that first-year profit would have been less than $29,000. Conversely, there was a 20 percent chance it would have been greater.
- ■ There was a 60 percent chance that first-year profit would have been less than $21,000. Conversely, there was a 40 percent chance it would have been greater.
- ■ There was a 40 percent chance that first-year profit would have been less than $17,000. Conversely, there was a 60 percent chance it would have been greater.
- ■ There was a 20 percent chance that first-year profit would have been less than $11,000. Conversely, there was an 80 percent chance it would have been greater.
- ■ There was a 0 percent chance that the first year would lose more than $7,000.

Figure 12.2 shows the starter portfolio open- and closed-trade equity curve.

FIGURE  12.2 Open- and Closed-Trade Equity Curve for the Starter Portfolio

<!-- image -->

The yearly returns and max open and closed trade draw-down for each year are shown in  Table   12.13  .

TABLE 12.13

Annual Return and Max Draw-Down for Starter Portfolio

|   Year |   Yearly Profit ($) |   Annual Max Draw-Down ($) |
|--------|---------------------|----------------------------|
|   1980 |              -6,203 |                     10,583 |
|   1981 |              28,909 |                      3,915 |
|   1982 |              21,224 |                      5,848 |
|   1983 |              20,164 |                      8,237 |
|   1984 |              20,920 |                      7,448 |
|   1985 |              11,983 |                      7,807 |
|   1986 |                 897 |                     12,485 |
|   1987 |              49,777 |                      6,756 |
|   1988 |              15,522 |                      8,071 |
|   1989 |              29,769 |                      7,128 |
|   1990 |              16,116 |                      6,171 |
|   1991 |              28,593 |                      4,578 |
|   1992 |              31,095 |                      3,551 |
|   1993 |              19,501 |                      6,537 |
|   1994 |              -2,622 |                     12,880 |
|   1995 |              19,043 |                      5,605 |
|   1996 |              19,493 |                      7,309 |
|   1997 |              36,528 |                      8,044 |
|   1998 |              16,643 |                      7,098 |
|   1999 |               8,306 |                     13,067 |

## TABLE 12.13 ( Continued )

| Year    |   Yearly Profit ($) |   Annual Max Draw-Down ($) |
|---------|---------------------|----------------------------|
| 2000    |              36,086 |                      4,482 |
| 2001    |              13,356 |                      8,630 |
| 2002    |              15,314 |                      9,312 |
| 2003    |              18,712 |                      8,313 |
| 2004    |              38,018 |                      6,510 |
| 2005    |              32,560 |                      5,355 |
| 2006    |               5,077 |                     12,720 |
| 2007    |              27,984 |                      3,146 |
| 2008    |              19,897 |                      4,225 |
| 2009    |               6,124 |                      6,217 |
| 2010    |              19,378 |                      6,446 |
| 2011    |              -1,975 |                      4,707 |
| Average |              19,430 |                      6,662 |

This  portfolio  can  be  traded  with  account  equity  ranging  from $20,000  to  $40,000.  An  aggressive  trader  with  account  equity  of $20,000 can expect to net $18,389 in the first year of trading (average start-trade  one-year  return).  He  or  she  should  expect  to  see  a  starttrade draw-down of $2,843, but it could be as high as $12,023 or more. Sometime during the year, the trader should expect to see an open- and closed-trade draw-down of $8,484. If the max start-trade draw-down is experienced, it would be a 60 percent draw-down from his starting equity.  For  enduring  the  draw-down  pain,  the  reward  is  outstanding: The average  first-year  return  of  $18,389  is  over  a  90  percent  return on starting equity. With $40,000 to start, the more conservative trader should expect this gain/pain profile:

- ■ Expected return for first year of 46 percent
- ■ Max start-trade draw-down of 30 percent
- ■ Average start-trade draw-down of 7 percent

Let's look at the next size of portfolio, the mid-size portfolio, for accounts that start or grow to the point where a trader is comfortable with its risk/ reward expectations.

## Mid-Size Portfolio Commodities

The mid-size portfolio contains the commodities shown in Table 12.14.

| Group         | Mid-Size Portfolio Commodities                            |
|---------------|-----------------------------------------------------------|
| Grains        | Soybeans, Rough Rice, KC Wheat, Corn                      |
| Meats         | Feeder Cattle                                             |
| Softs         | Cotton, Lumber, Sugar, Coffee                             |
| Metals        | Copper, Palladium, London Aluminum, London Copper         |
| Currencies    | Dollar Index, British Pound, Swiss Franc, Canadian Dollar |
| Energies      | Heating Oil, Crude Oil, Mini Natural Gas, London Brent    |
| Financials    | Euro Bund, Eurodollar, 10-Year Notes, 30-Year Bond        |
| Stock Indices | Nikkei, Hang Seng, Mini Nasdaq                            |

## Mid-Size Portfolio Small-Account Money Management

The mid-size portfolio  uses  the  small-account  money  management  techniques and limits shown in  Table 12.15.

TABLE 12.15 Mid-Size Portfolio Money Management Techniques and Limits

| Small-Account Money Management Technique   | Used?/Limit   |
|--------------------------------------------|---------------|
| First- N -in-a-Group                       | No/N/A        |
| Limit Trade Risk on Entry                  | Yes/$2,000    |
| Limit Max Open-Trade Risk                  | Yes/$6,000    |
| Limit Max Portfolio Risk                   | Yes/$16,000   |
| Limit Max Number of Trades                 | Yes/11        |

## Mid-Size Portfolio Performance

The mid-size portfolio has these summary start-trade statistics:

Average first-year profit:

$27,303

Average start-trade draw-down:

$3,790

Max start-trade draw-down:

$19,331

Figure 12.3 shows the start-trade graphs for the mid-size portfolio.

Looking at the top graph, starting to trade the mid-size portfolio at any point in time over the period 1980 to 2011, a trader would face the following risk profile:

- ■ There was a 100 percent chance start-trade draw-down would have been less than $19,331.

FIGURE  12.3 Start-Trade Statistics for Mid-Size Portfolio

<!-- image -->

- ■ There was an 80 percent chance start-trade draw-down would have been less  than  $7,000.  Conversely, there was a 20 percent chance it would have been greater.
- ■ There was a 60 percent chance start-trade draw-down would have been less  than  $3,200.  Conversely, there was a 40 percent chance it would have been greater.
- ■ There was a 40 percent chance start-trade draw-down would have been less  than  $1,800.  Conversely, there was a 60 percent chance it would have been greater.
- ■ There was a 20 percent chance start-trade draw-down would have been less than $700. Conversely, there was an 80 percent chance it would have been greater.

Looking at the bottom graph, starting to trade the mid-size portfolio at any point in time over the period 1980 to 2011, a trader would face the following profi  tability probabilities at the one year from start-trade date:

- ■ There was a 100 percent chance that fi  rst-year profi  t would have been less than $71,000.
- ■ There was an 80 percent chance that fi  rst-year profi  t would have been less than $41,000. Conversely, there was a 20 percent chance it would have been greater.
- ■ There was a 60 percent chance that fi  rst-year profi  t would have been less than $32,000. Conversely, there was a 40 percent chance it would have been greater.
- ■ There was a 40 percent chance that fi  rst-year profi  t would have been less than $24,000. Conversely, there was a 60 percent chance it would have been greater.
- ■ There was a 20 percent chance that fi  rst-year profi  t would have been less than $18,000. Conversely, there was an 80 percent chance it would have been greater.
- ■ There was a 0 percent chance that the fi  rst year would lose more than $13,000.

Figure   12.4 shows the mid-size portfolio open- and closed-trade equity curve.

<!-- image -->

FIGURE  12.4 Open- and Closed-Trade Equity Curve for the Mid-Size Portfolio

The yearly returns and max open- and closed-trade draw-down for each year are shown in  Table   12.16  .

| Year    |   Yearly Profit ($) |   Annual Max Draw-Down ($) |
|---------|---------------------|----------------------------|
| 1980    |               3,449 |                     14,567 |
| 1981    |              54,370 |                      6,409 |
| 1982    |              37,931 |                      8,226 |
| 1983    |              22,464 |                      8,795 |
| 1984    |              44,761 |                     10,609 |
| 1985    |              42,239 |                     13,142 |
| 1986    |               1,097 |                     14,443 |
| 1987    |              57,723 |                      9,049 |
| 1988    |              20,936 |                     15,709 |
| 1989    |              31,074 |                      8,565 |
| 1990    |              14,636 |                      9,340 |
| 1991    |              51,338 |                      4,304 |
| 1992    |              36,635 |                      9,231 |
| 1993    |              36,424 |                      9,136 |
| 1994    |              31,631 |                     12,011 |
| 1995    |              43,385 |                      5,661 |
| 1996    |              13,065 |                     14,637 |
| 1997    |              34,847 |                      8,642 |
| 1998    |              41,441 |                      8,131 |
| 1999    |              20,592 |                     16,372 |
| 2000    |              40,031 |                      5,103 |
| 2001    |              -1,670 |                     21,640 |
| 2002    |              22,452 |                      9,230 |
| 2003    |              37,351 |                      9,420 |
| 2004    |              47,030 |                     10,654 |
| 2005    |              40,573 |                      6,572 |
| 2006    |              22,336 |                     15,195 |
| 2007    |              19,428 |                     10,704 |
| 2008    |              24,127 |                     10,714 |
| 2009    |              21,940 |                      7,910 |
| 2010    |              31,611 |                      6,768 |
| 2011    |              -7,607 |                     11,990 |
| Average |              29,301 |                     10,403 |

This  portfolio  can  be  traded  with  equity  ranging  from  $40,000  to $60,000.  An  aggressive  trader  with  account  equity  of  $40,000  can expect to net $27,303 in the first year of trading (average start-trade one-year return). He or she should expect to see a start-trade draw-down of $3,790, but it could be as high as $19,331 or more. Sometime during the year, the trader should expect to see an open- and closed-trade draw-down  of  $11,847.  If  the  max  start-trade  draw-down  is  experienced,  it  would  be  a  48  percent  draw-down  from  his  or  her  starting equity.  For  enduring  the  draw-down  pain,  the  reward  is  outstanding: The average  first-year  return  of  $27,303  is  over  a  68  percent  return on starting equity. With $40,000 to start, the more conservative trader should expect this gain/pain profile:

- ■ Expected return for first year of 46 percent
- ■ Max start-trade draw-down of 32 percent
- ■ Average start-trade draw-down of 6 percent

Let's develop the last small account portfolio for accounts that start or grow to the point where a trader is comfortable with its risk/reward expectations.

## Full-Size Portfolio Commodities

The full-size portfolio contains the commodities shown in  Table 12.17.

| TABLE 12.17   | Full-Size Portfolio Commodities                                                                                                                 |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Group         | Full-Size Portfolio Commodities                                                                                                                 |
| Grains        | Soybeans, Rough Rice, KC Wheat, Corn, Bean Meal, Bean Oil, Wheat                                                                                |
| Meats         | Feeder Cattle                                                                                                                                   |
| Softs         | Cotton, Lumber, Sugar, Coffee, Orange Juice                                                                                                     |
| Metals        | Copper, Palladium, London Aluminum, London Copper, Silver, Copper, Platinum, London Aluminum Alloy, London Nickel                               |
| Currencies    | Dollar Index, British Pound, Swiss Franc, Canadian Dollar, Japanese Yen, Mexican Peso, Australian Dollar, Euro-Currency                         |
| Energies      | Heating Oil, Crude Oil, Mini Natural Gas, London Brent, Reformulated Gas                                                                        |
| Financials    | Euro Bund, Eurodollar, 10-Year Notes, 30-Year Bond, 5-Year Notes, 2-Year Notes, Australian Bond, Canadian Government Bond, Long Gilt, Simex JGB |
| Stock Indices | Nikkei, Hang Seng, Mini Nasdaq, DAX, Mini S&P , Mini Russell, Mini Midcap                                                                       |

## Full-Size Portfolio Small-Account Money Management

The  full-size  portfolio  uses  the  small-account  money  management  techniques and limits shown in  Table 12.18.

| Small-Account Money Management Technique   | Used?/Limit   |
|--------------------------------------------|---------------|
| First- N -in-a-Group                       | Yes/6         |
| Limit Trade Risk on Entry                  | Yes/$2,000    |
| Limit Max Open-Trade Risk                  | Yes/$6,000    |
| Limit Max Portfolio Risk                   | No/N/A        |
| Limit Max Number of Trades                 | Yes/16        |

## Full-Size Portfolio Performance

The full-size portfolio has these summary start-trade statistics:

Average fi  rst-year profi  t:

$39,461

Average start-trade draw-down:

$4,778

Max start-trade draw-down:

$25,454

Figure   12.5 shows the start-trade graphs for the full-size portfolio.

<!-- image -->

FIGURE  12.5 Start-Trade Statistics for Full-Size Portfolio

COMMODITIES

Looking at the top graph, starting to trade the full-size portfolio at any point in time over the period 1980 to 2011, a trader would face the following risk profile:

- ■ There was a 100 percent chance start-trade draw-down would have been less than $25,454.
- ■ There was an 80 percent chance start-trade draw-down would have been less  than  $8,000.  Conversely, there was a 20 percent chance it would have been greater.
- ■ There was a 60 percent chance start-trade draw-down would have been less  than  $4,500.  Conversely, there was a 40 percent chance it would have been greater.
- ■ There was a 40 percent chance start-trade draw-down would have been less  than  $2,500.  Conversely, there was a 60 percent chance it would have been greater.
- ■ There was a 20 percent chance start-trade draw-down would have been less than $1,000. Conversely, there was an 80 percent chance it would have been greater.

Looking at the bottom graph, starting to trade the full-size portfolio at any point in time over the period 1980 to 2011, a trader would face the following profitability probabilities at the one year from start-trade date:

- ■ There was a 100 percent chance that first-year profit would have been less than $100,000.
- ■ There was an 80 percent chance that first-year profit would have been less than $60,000. Conversely, there was a 20 percent chance it would have been greater.
- ■ There was a 60 percent chance that first-year profit would have been less than $40,000. Conversely, there was a 40 percent chance it would have been greater.
- ■ There was a 40 percent chance that first-year profit would have been less than $35,000. Conversely, there was a 60 percent chance it would have been greater.
- ■ There was a 20 percent chance that first-year profit would have been less than $22,000. Conversely, there was an 80 percent chance it would have been greater.

- ■ There was a 0 percent chance that the fi  rst year would lose more than $10,000.

Figure   12.6 shows the full-size portfolio open- and closed-trade equity curve.

FIGURE  12.6 Open- and Closed-Trade Equity Curve for the Full-Size Portfolio

<!-- image -->

The yearly returns and max open- and closed-trade draw-down for each year are shown in  Table   12.19  .

TABLE 12.19

Annual Return and Max Draw-Down for Full-Size Portfolio This  portfolio  can  be  traded  with  equity  ranging  from  $60,000  to $100,000. An aggressive trader with account equity of $60,000 can expect to  net  $39,461  in  the  first  year  of  trading  (average  start-trade  first-year return). He or she should expect to see a start-trade draw-down of $4,778, but  it  could  be  as  high  as  $25,454  or  more.  Sometime  during  the  year, the trader should expect to see an open- and closed-trade draw-down of $14,148. If the max start-trade draw-down is experienced, it would be a 42 percent draw-down from the portfolio's starting equity. For enduring the draw-down pain, the reward is outstanding:  The average first-year return of $39,461 is over a 65 percent return on starting equity. With $100,000 to start, the more conservative trader should expect this gain/pain profile:

|   Year |   Yearly Profit ($) |   Annual Max Draw-Down ($) |
|--------|---------------------|----------------------------|
|   1980 |              10,031 |                     12,234 |
|   1981 |              64,665 |                     13,531 |
|   1982 |              66,735 |                     10,530 |
|   1983 |              42,364 |                      9,792 |
|   1984 |              42,295 |                     13,703 |
|   1985 |              72,497 |                      9,201 |
|   1986 |               7,785 |                     14,227 |
|   1987 |              77,500 |                     10,193 |
|   1988 |              61,394 |                     15,740 |
|   1989 |              42,167 |                     11,370 |
|   1990 |              53,424 |                     10,780 |
|   1991 |              53,228 |                     10,105 |
|   1992 |              31,514 |                     13,311 |
|   1993 |              80,113 |                      7,947 |

| Year    |   Yearly Profit ($) |   Annual Max Draw-Down ($) |
|---------|---------------------|----------------------------|
| 1994    |              41,025 |                     22,439 |
| 1995    |              29,696 |                      9,827 |
| 1996    |              39,722 |                     24,309 |
| 1997    |              52,418 |                     14,557 |
| 1998    |              52,209 |                     15,501 |
| 1999    |              15,139 |                     23,822 |
| 2000    |              48,605 |                     10,425 |
| 2001    |              15,413 |                     12,654 |
| 2002    |              17,583 |                     16,166 |
| 2003    |              74,353 |                     12,400 |
| 2004    |              27,764 |                     20,458 |
| 2005    |              41,668 |                     12,709 |
| 2006    |              18,786 |                     20,736 |
| 2007    |              42,512 |                     16,766 |
| 2008    |              51,359 |                     15,714 |
| 2009    |              30,537 |                     11,422 |
| 2010    |              41,025 |                     13,183 |
| 2011    |               5,761 |                     17,264 |
| Average |              42,227 |                     14,148 |

- ■ Expected return for first year of 39 percent
- ■ Max start-trade draw-down of 25 percent
- ■ Average start-trade draw-down of 5 percent

## ■ Conclusion

In this chapter, three portfolios with specific money management rules were developed that the small-account trader can trade with account equity ranging from $20,000 to $100,000. Table 12.20 summarizes performance.

TABLE 12.20

## Comparison of Start-Trade and Open- and Closed-Trade Performance Metrics on  Three Portfolios for the Small-Account  Trader

| Metric                                    | Starter Portfolio   | Mid-Size Portfolio   | Full-Size Portfolio   |
|-------------------------------------------|---------------------|----------------------|-----------------------|
| Equity Requirement to Trade ($)           | 20,000-40,000       | 40,000-60,000        | 60,000-100,000        |
| Average Start-Trade First-Year Return ($) | 18,389              | 27,303               | 39,461                |
| Average Start-Trade Draw-Down ($)         | 2,843               | 3,790                | 4,778                 |
| Max Start-Trade Draw-Down ($)             | 12,023              | 19,331               | 25,454                |
| Start-Trade Gain-to-Pain Ratio            | 6.47                | 7.20                 | 8.26                  |
| Average Annual Return                     | 19,290              | 29,253               | 42,227                |
| Average Annual Max Draw-Down ($)          | 8,484               | 11,847               | 14,148                |
| Max Open- and Closed-Trade Draw-          | 13,067              | 21,460               | 28,146                |
| Down ($)                                  |                     |                      |                       |
| Open- and Closed-Trade Equity Gain-to-    | 2.27                | 2.47                 | 2.98                  |
| Pain Ratio                                |                     |                      |                       |

Note that as the portfolios build, the gain-to-pain ratios show that the trading solution gets better.  This is true despite the fact that the bigger portfolios add commodities that don't trade as well with our strategy as those in the smaller portfolios.  This is due to greater and greater diversification.  The small-account trader should look to move up to the next size portfolio as soon as account equity grows to a point where he or she is comfortable with the risk/reward profile of the bigger portfolio.

## Traditional Money Management Techniques for Small Accounts: Stock Strategy

I n this chapter, small-account money management techniques will be illustrated using the stock strategy developed in Chapters 4 through 6. A key difference between the commodity basket and the stock basket is the lack of a strong group structure with the stocks. Though there is a spectrum of industries in the current Nasdaq 100, the correlation of the stocks one-toanother is relatively high.  The Nasdaq 100 is composed of stocks that are in the index because they are highly liquid and they move. Thus there is very little that can be done with diversification money management techniques. In this chapter, specific money management rules will be developed for account sizes ranging from $20,000 to $100,000.

## ■ Stock Strategy Performance Metrics

In the last two chapters, start-trade draw-down was presented as the most meaningful metric for small-account traders. That is always true because open-trade give-back from profitable trades is indistinguishable from los-

215

ing trade draw-down. With a scalping system like the stock strategy we developed in Chapters 4 through 6, the open-trade give-back will be much smaller than for a longer-term trend-following strategy. Maybe open- and closed-trade draw-down, or closed-trade draw-down is close enough to the actual start-trade draw-down statistics so that we don't have to go through the lengthy process of building the start-trade statistics. T o gain insight into this issue, I used 10 stocks of the 100-stock Nasdaq basket and built openand closed-trade equity statistics, closed trade statistics, and start-trade statistics for comparison.  The following list shows the results:

Average yearly maximum open- and closed-trade draw-down: $3,343

Average yearly maximum closed-trade draw-down: $3,321

Average yearly maximum start-trade draw-down: $3,274

Maximum open- and closed-trade draw-down: $8,148

Maximum closed-trade draw-down: $7,789

Maximum start-trade draw-down: $7,572

Notice that the average and maximum draw-down statistics are very close in  all  cases.  For  the  development  in  this  chapter,  we  will  use  open-  and closed-trade draw-down statistics instead of start-trade statistics.

## ■ Position Sizing

Most brokerage firms allow clients 100 percent leverage when trading on the long side, as we're doing with our Nasdaq 100 long-only strategy. So with a $20,000 account, a client could control up to $40,000 in stock. Let's look at the return and draw-down statistics when the strategy is traded using a position size of $5,000 per trade and the max number of stocks held at a time is varied from one to eight.  Table 13.1 shows the trading results.

| TABLE 13.1                 | Performance as a Function of Max Number of Stock Positions   | Performance as a Function of Max Number of Stock Positions   | Performance as a Function of Max Number of Stock Positions   | Performance as a Function of Max Number of Stock Positions   |
|----------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| Number of $5,000 Positions | Average Annual Profit ($)                                    | Average Annual Max Draw-Down ($)                             | Max Draw-Down ($)                                            | Gain-to-Pain Ratio                                           |
| 1                          | 462                                                          | 1,720                                                        | 4,140                                                        | 0.27                                                         |
| 2                          | 2,823                                                        | 2,507                                                        | 4,990                                                        | 1.13                                                         |
| 3                          | 4,558                                                        | 3,292                                                        | 5,498                                                        | 1.38                                                         |
| 4                          | 4,972                                                        | 3,737                                                        | 5,916                                                        | 1.33                                                         |
| 5*                         | 7,656                                                        | 4,301                                                        | 7,520                                                        | 1.78                                                         |
| 6                          | 8,115                                                        | 5,317                                                        | 9,416                                                        | 1.53                                                         |
| 7                          | 9,527                                                        | 6,069                                                        | 10,786                                                       | 1.56                                                         |
| 8                          | 10,555                                                       | 6,069                                                        | 11,504                                                       | 1.74                                                         |

The gain-to-pain ratio, formed by dividing average annual profit by average annual max draw-down, shows that carrying a max of five positions offers the best trading solution. On the practical side, the average and max draw-down figures for that solution are too large for a $20,000 account; the average max draw-down per year exceeds 21 percent, and the max drawdown is over 37 percent. Let's see if we can use other money management techniques to reduce the risk.

## ■ Position Hedging

A shortcoming of our stock strategy is the fact that we only trade from the long side. When the market turns down as it did in 2000-2001 and 2008, most of the long trades will lose. Let's try adding a downside hedge to the baseline strategy. An easy way to do that is to sell short one or more $5,000 positions  of  a  market  surrogate  like  the  exchange-traded  fund  (ETF)  for S&amp;P 500 (stock symbol SPY). Since eight positions is the most we can trade with a $20,000 account, we can carry up to three hedged positions with our max of five long positions before we have to reduce the number of long positions by one. Another note is that some accounts (usually retirement accounts) are prohibited from short-selling, so they can't hedge in this manner.  There are other hedging techniques available to these accounts, such as buying inverse ETFs or put options, so this is not a limitation of the money management technique.

Table 13.2 shows the results when we hedge with one to three SPY positions.

| TABLE 13.2                      | Hedging with Short SPY Positions   | Hedging with Short SPY Positions   | Hedging with Short SPY Positions   | Hedging with Short SPY Positions   |
|---------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|
| Number of Long/ Short Positions | Average Annual Profit ($)          | Average Annual Max Draw-Down ($)   | Max Draw- Down ($)                 | Gain-to-Pain Ratio                 |
| 5/0*                            | 7,656                              | 4,301                              | 7,520                              | 1.78                               |
| 5/1                             | 7,428                              | 3,933                              | 6,931                              | 1.89                               |
| 5/2**                           | 7,202                              | 3,792                              | 6,589                              | 1.90                               |
| 5/3                             | 6,974                              | 3,823                              | 7,271                              | 1.82                               |

*Baseline

** New baseline

The hedging strategy significantly helps in the draw-down department. With five longs and two shorts, profitability is reduced by about $450 per year, but average max draw-down and max draw-down are reduced even more. Since risk is what we're trying to minimize in the small account, we'll keep the 5/2 solution as the new baseline.

It  might  surprise  some  that  this  hedging  strategy  has  such  a  large impact on performance. It would seem that you're just neutralizing two of  the  longs  with  the  two  shorts. The  reality  is  that  the  average  long trade makes about 1 percent in two days, a compounded rate of over 250 percent a year. The SPY, on average, loses just a small fraction of that amount.

As one last refinement, there may be times when the market is in a severe  down-turn  and  the  70-day  trend  filter  reduces  the  number  of stocks that can trade to a small fraction of the total 100. Maybe the SPY hedge shouldn't be on when the number of trades falls below a certain threshold? This concept was tested, and it turns out that the hedge of two SPY positions should only be on when there are two or more active Nasdaq 100 trades. Table   13.3 compares this new baseline solution with the old.

TABLE 13.3 Limiting the Hedge by Number of Ongoing Trades

| Number of Long/Short Positions   |   Average Annual Profit ($) |   Average Annual Max Draw-Down ($) |   Max Draw- Down ($) |   Gain-to-Pain Ratio |
|----------------------------------|-----------------------------|------------------------------------|----------------------|----------------------|
| 5/2*                             |                       7,202 |                              3,792 |                6,589 |                 1.90 |
| 5/2 if at least 2 trades**       |                       6,786 |                              3,242 |                6,099 |                 2.09 |

*Baseline This trading solution could be used for accounts ranging from $20,000 to $40,000. For the small-account trader with a high pain threshold a willingness to trade it with $20,000, the following is the type of ride he or she can expect:

** New baseline

Figure   13.1 shows the equity curve for the baseline stock strategy.

<!-- image -->

FIGURE  13.1 Equity Curve for Stock System when Positions Are Limited to Five Longs and Two Short Hedges

Table 13.4 shows the year-by-year return and max draw-down.

TABLE 13.4 Small-Account Money Management Stock Strategy: Open- and Closed-Trade Equity Curve, Year-by-Year Performance

|   Year |   Yearly Profit ($) |   Annual Max Draw-Down ($) |
|--------|---------------------|----------------------------|
|   2000 |               8,933 |                      4,341 |
|   2001 |              14,601 |                      3,763 |
|   2002 |              15,175 |                      3,360 |
|   2003 |               9,228 |                      2,423 |
|   2004 |               5,028 |                      2,777 |
|   2005 |               7,345 |                      1,728 |
|   2006 |                 255 |                      3,242 |
|   2007 |               5,877 |                      1,820 |
|   2008 |                 165 |                      4,650 |
|   2009 |               9,593 |                      2,545 |
|   2010 |               6,900 |                      2,150 |
|   2011 |              -1,665 |                      6,099 |

Average annual return: 34 percent

Average max draw-down per year: 16 percent

Max draw-down: 30 percent

A more conservative trader choosing to trade with $40,000 of account equity would see half the pain and half the reward.

As the account grows, the trader can shift to better solutions. Table 13.5 shows mixes of longs and short hedges that maximize the gain-to-pain ratio for a given number of long positions.

## TABLE 13.5 Small-Account Stock Trading Solutions

| Number of Long/Short Positions   |   Average Annual Profit ($) |   Average Annual Max Draw- Down ($) |   Max Draw- Down ($) |   Gain-to- Pain Ratio |   Minimum Account Size to Cover Margin for $5,000 Positions ($) |
|----------------------------------|-----------------------------|-------------------------------------|----------------------|-----------------------|-----------------------------------------------------------------|
| 5/2                              |                       6,786 |                               3,242 |                6,099 |                  2.09 |                                                          17,500 |
| 9/3                              |                      10,414 |                               4,857 |               10,277 |                  2.14 |                                                          30,000 |
| 11/4                             |                      11,771 |                               5,461 |               10,854 |                  2.16 |                                                          37,500 |
| 12/5                             |                      12,631 |                               5,812 |               11,176 |                  2.17 |                                                          42,500 |
| 13/6                             |                      13,137 |                               6,057 |               11,147 |                  2.17 |                                                          47,500 |
| 18/7                             |                      15,598 |                               7,085 |               13,191 |                  2.20 |                                                          62,500 |

For  each  long/short  solution,  the  number  of  indicted  hedge  positions was placed only if there were that many Nasdaq long positions, or greater. Table 13.5 indicates that as the account equity grows, better trading solutions, as measured by the gain-to-pain ratio, are available. There is a point (seven $5,000 SPY positions) where the number of hedge positions can't be increased because there aren't enough average Nasdaq trades to increase the gain-to-pain ratio.

There is a way to take advantage of the gaps between minimum account sizes for each solution: to increase trade size from $5,000 upward for both the long and hedge trades to maintain exposure near the max dollar commitment the brokerage will allow to be traded for the account size. If you're trading the 5/2 solution, and account equity has grown to $25,000, and the brokerage allows two-to-one leverage, you can put on $50,000 of trades across your five longs and two shorts.  Your trade size can then be just over $7,000 a position instead of $5,000. The trader should take advantage of these solutions as his or her account grows with the ultimate goal of building the account to large account status.

## ■ Conclusion

In  this  chapter,  we  developed  small-account  trading  solutions  for  the Donchian stock strategy. Because of the lack of a group structure, and the high  correlation  among  the  100  stock  components,  most  of  the  smallaccount  money  management  techniques  we  used  with  the  commodity strategy weren't effective with the stock strategy. But hedging with short positions in the S&amp;P 500 SPY ETF allowed our stock strategy to have an average annual profit greater than the max draw-down and over twice as large as the average annual max draw-down.

## Traditional Money Management Techniques for Large Accounts: Commodities

T he previous two chapters detailed  the  problems  faced  by  the  smallaccount trader. With a small account, he or she is forced to take more relative  risk  than  a  large-account  trader. Taking  a  $2,000-risk  trade  with $20,000 account equity means the small-account trader is risking 10 percent of capital; he or she is always a small number of adverse trades away from a margin call. A large-account trader can employ money management techniques  that  result  in  a  far  lower  relative  risk.  Employing  these  strategies ensures  that  the  large-account  trader  is  many,  many  adverse  trades  away from a margin call. His or her smaller relative risk can be managed to yield a solid return.

There is also a key difference in the development of a finalized money management overlay for the large account. In our small-account development,  we  were  most  concerned  with  limiting  risk,  so  in  some  cases  we accepted a tactic that didn't improve the quality of the trading solution as

221

measured by the gain-to-pain ratio. With large accounts, we want the best trading solution available, so all decisions will be based on the gain-to-pain ratio. At the end of development, leverage in the form of the amount risked per trade will bring that solution to a risk level acceptable to the trader.

The large-account trader will use some of the same money management strategies as the small-account trader: limit risk, diversify, and limit group exposure. An additional technique that the large-account trader can use is a buy strategy that allows n -lot trades with a small, constant risk exposure. Before these strategies are detailed, the fixed-risk sizing technique we will use will be reviewed.

## ■ Fixed-Risk Sizing

In this money management approach, a fixed percentage of equity is risked on each trade. It is implemented by multiplying the fixed percentage by account equity on the day of the trade to determine the dollar amount to be risked. Then, the strategy's trade risk is used to determine the number of contracts that should be traded to risk the desired amount. For example, if account size is $150,000 and the fixed percentage the trader has decided to risk is 3 percent, $4,500 could be risked on a trade signal (0.03 multiplied by $150,000). If the trade risk for a signal is $600 (distance to initial stop, converted to dollars), seven contracts would be bought or sold on the signal (a fractional number of contracts is rounded down).  This example illustrates that a sizeable account is required to implement this conservative money management strategy; otherwise the fixed percentage of equity will be too small to support even a one-contract trade.

This strategy was tested on the Donchian trend-following strategy across the  56-commodity  database  (1980-2011).  A  starting  account  equity  of $1,000,000 was used.  Table 14.1 highlights performance metrics for various fixed-risk percentages.

| TABLE 14.1               | Fixed-Risk Performance    | Fixed-Risk Performance           | Fixed-Risk Performance   | Fixed-Risk Performance   |
|--------------------------|---------------------------|----------------------------------|--------------------------|--------------------------|
| Percent Risked per Trade | Average Annual Return (%) | Average Annual Max Draw-Down (%) | Max Draw-Down (%)        | Gain-to-Pain Ratio       |
| 1                        | 90.6                      | 17.5                             | 39.8                     | 5.17                     |
| 2                        | 207.9                     | 29.0                             | 61.6                     | 7.17                     |
| 3                        | 347.1                     | 37.8                             | 75.4                     | 9.18                     |
| 4                        | 503.4                     | 44.9                             | 84.5                     | 11.21                    |

Table 14.1 highlights a number of points regarding the fixed-risk sizing strategy:

- ■ Excellent returns can be achieved with a small fixed-risk percentage.
- ■ As fixed-risk percentage increases, so do the annual return and drawdown. Though  not  shown,  this  trend  continues  until  a  fixed-risk  percentage is reached that causes a draw-down to exceed account equity so trading stops.
- ■ The ratio of return to risk is continually increasing, though at a decreasing rate, as the gain-to-pain ratio shows.  This means that the more risk a trader can take, the greater the relative reward.

The recommended way to trade this approach is to mentally determine the  largest  percentage  draw-down  you  could  trade  through  and  select  a fixed-risk percentage that yields a max draw-down number less than that amount. If the return is satisfactory for that draw-down, trading can commence with the strategy. Many will overestimate the draw-down they can sustain because of the lure of potentially larger returns. They will rationalize the ease of sustaining a 39 percent draw-down to achieve a 208 percent return, but when the draw-down occurs in real trading, reality may set in. Only a small percentage of traders can watch an account diminish by 40 or 50 percent and remain with the approach, even if that was the expected eventuality going into trading.

## ■ Portfolio Selection

As we saw during development of the small-account portfolios in Chapter 12, not all the commodities are worth trading.  There are three losing commodities: live cattle, lean hogs, and cocoa. Those will be left out of the largeaccount  portfolio. Table  14.2  shows  the  commodities  that  will  form  the basis for development.

| TABLE 14.2   | Commodity Portfolio for Large Account                                                                                       |
|--------------|-----------------------------------------------------------------------------------------------------------------------------|
| Group        | Commodities                                                                                                                 |
| Grains       | Rough Rice, Bean Oil, Bean Meal, Soybeans, Corn, KC Wheat, Wheat                                                            |
| Meats        | Feeder Cattle                                                                                                               |
| Softs        | Cotton, Sugar, Lumber, Coffee, Orange Juice                                                                                 |
| Metals       | Copper, Silver, Gold, Palladium, Platinum, London Aluminum, London Aluminum Alloy, London Copper, London Nickel ( continued |

TABLE 14.2

Continued )

| Group         | Commodities                                                                                                                                                     |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Currencies    | Mexican Peso, Dollar Index, British Pound, Japanese Yen, Swiss Franc, Canadian Dollar, Australian Dollar, Euro-Currency                                         |
| Energies      | Heating Oil, Reformulated Gas, Brent Crude, Crude Oil, Mini Natural Gas                                                                                         |
| Financials    | Euro Bund, Eurodollar, 2-Year Note, 10-Year Note, 30-Year Bond, 5-Year Note, Australian Bond, Canadian Government Bond, Long Gilt, Spanish Bond, Simex JGB Bond |
| Stock Indices | Nikkei, Mini Nasdaq, Hang Seng, DAX, Mini Russell, Mini Midcap, Mini S&P                                                                                        |

(

Table 14.3 shows performance for various fixed-risk percentage values on the new portfolio.

TABLE 14.3 Fixed-Risk Performance on Large Portfolio

|   Percent Risked per Trade |   Average Annual Return (%) |   Average Annual Max Draw-Down (%) |   Max Draw-Down (%) |   Gain-to-Pain Ratio |
|----------------------------|-----------------------------|------------------------------------|---------------------|----------------------|
|                          1 |                        89.9 |                               16.9 |                39.0 |                 5.32 |
|                          2 |                       208.8 |                               28.2 |                60.6 |                 7.40 |
|                          3 |                       353.5 |                               37.0 |                74.5 |                 9.55 |
|                          4 |                       519.5 |                               44.2 |                83.8 |                11.75 |

The draw-downs are still too large for the strategy to be tradeable.

Our portfolio contains some groups with a lot of commodities: The financial group has 11, the metals have 9, and the currencies have 8. Let's limit group exposure and see if the draw-downs can be reduced.

## ■ First-N-in-a-Group

In this money management approach, group exposure is limited to N commodities. If a group, like the grains, is in N commodity trades and a new grain trade is signaled, that trade is bypassed.  Table 14.4 shows performance when group exposure is capped at N commodities and 1 percent of equity is risked per trade.

The gain-to-pain ratio shows there's a modest performance enhancement when group exposure is limited to a max of seven.  There is also a small drop TABLE 14.4

| Max Number in Group   |   Average Annual Return (%) |   Average Annual Max Draw-Down (%) |   Max Draw-Down (%) |   Gain-to-Pain Ratio |
|-----------------------|-----------------------------|------------------------------------|---------------------|----------------------|
| All Trades*           |                        89.9 |                               16.9 |                39.0 |                 5.32 |
| 4                     |                        67.4 |                               14.3 |                30.3 |                 4.71 |
| 5                     |                        78.4 |                               15.1 |                32.8 |                 5.19 |
| 6                     |                        84.6 |                               16.2 |                35.8 |                 5.22 |
| 7**                   |                        87.9 |                               16.4 |                37.4 |                 5.36 |
| 8                     |                        89.1 |                               16.7 |                39.0 |                 5.34 |

in average max draw-down and max draw-down. That money management rule will be added to form the new baseline.

## ■ Limit Trade Risk on Entry

This technique is the same as we explored in Chapter 12. When a trade is originated,  the  trade  risk  is  the  distance,  converted  to  dollars,  from  the entry point to the catastrophic stop loss point. Because our three standard deviation stop is volatility-based,  some trades will have a relatively small risk, and some a relatively large risk. Using this money management strategy, trades with a high trade risk are bypassed. Table 14.5 shows results for a range of entry-risk thresholds.

TABLE 14.5

Limit Trade Risk on Entry

| Trade Risk Limit   |   Average Annual Return (%) |   Average Annual Max Draw-Down (%) |   Max Draw-Down (%) |   Gain-to-Pain Ratio |
|--------------------|-----------------------------|------------------------------------|---------------------|----------------------|
| All Trades*        |                        87.9 |                               16.4 |                37.4 |                 5.36 |
| $6,000             |                        87.8 |                               16.4 |                37.4 |                 5.35 |
| $5,000             |                        87.1 |                               16.4 |                37.4 |                 5.31 |
| $4,000             |                        86.7 |                               16.3 |                36.8 |                 5.32 |
| $3,000             |                        83.5 |                               16.3 |                37.2 |                 5.06 |
| $2,000             |                        77.4 |                               15.8 |                34.3 |                 4.90 |

*Baseline

You might be surprised that this tactic didn't improve our trading solution: The  $2,000 trade risk  limit  worked  very  well  in  our  small-  account development. The  reason  is  the  normalization  that  takes  place  with  our

Limiting Exposure to Max

N

in a Group sizing  approach.  If,  for  a  given  equity  level,  our  large-account  sizing  approach  were  to  take  a  10-lot  of  a  trade  with  a  $2,000  entry  trade  risk, it  would take a 5-lot of a trade with a $4,000 entry trade risk. The total risk for the position is the same. In the small account where we're trading one-lots of everything, the $4,000 position has twice the risk of the $2,000 position. This normalization in large-account trading makes no one trade riskier than any other; hence they all should be used. Let's look at the next large-account money management tactic.

## ■ Limit the Total Number of Open Trades

Again, this is the same strategy used for the small-account money management analysis in Chapter 12. If the number of ongoing open trades reaches a limit, signaled trades are bypassed. Table 14.6 shows the pertinent trade statistics when the number of open trades is capped.

TABLE 14.6

| Max Number of Open Trades   |   Average Annual Return (%) |   Average Annual Max Draw-Down (%) |   Max Draw-Down (%) |   Gain-to-Pain Ratio |
|-----------------------------|-----------------------------|------------------------------------|---------------------|----------------------|
| All Trades*                 |                        87.9 |                               16.4 |                37.4 |                 5.36 |
| 35                          |                        87.7 |                               16.4 |                37.4 |                 5.35 |
| 30**                        |                        87.5 |                               16.3 |                37.4 |                 5.37 |
| 25                          |                        81.3 |                               15.3 |                36.6 |                 5.31 |

*Baseline

**New baseline

The results show that this money management technique only marginally improves results. Limiting open trades to a max of 30 will be added as the new baseline. That this tactic did not significantly improve results is more surprising than the fact that eliminating risky trades did not improve performance. There definitely is an ebb and flow in the number of open tradessometimes many, sometimes few. It would seem to make sense that both risk and reward increase when there are a relatively high number of trades, so  limiting  trades  should  reduce  the  draw-downs,  but  for  this  strategy  it barely makes a difference. It's my experience that this money management tactic  works  best  with  longer-term  trend-following  strategies;  those  that hold trades longer and consequentially have a higher profit-per-trade as well as a larger open-equity give-back.

Limit the Total Number of Open Trades

## ■ Limit the Percentage of Open-Trade Risk

This technique is similar to the small-account money management strategy of  limiting  the  open-trade  dollar  risk  of  a  trade  to  a  max  amount. The difference is that instead of a fixed dollar cap, a percentage value is formed by dividing the dollar value of the open-trade risk by total account equity.  Open  trades  that  exceed  a  percentage  value  limit  of  equity  are exited. Note that this is a form of profit-taking; trades that reach the limit are deeply in profit, and the exit is done at the peak profit of the trade to that point. Table 14.7 shows results when this technique is added to the baseline.

TABLE 14.7 Limit the Max Open-Trade Risk Percentage

| Trades Limited to a Max Open-Trade Percent of Equity   |   Average Annual Return (%) |   Average Annual Max Draw-Down (%) |   Max Draw-Down (%) |   Gain-to-Pain Ratio |
|--------------------------------------------------------|-----------------------------|------------------------------------|---------------------|----------------------|
| All*                                                   |                        87.5 |                               16.3 |                37.4 |                 5.37 |
| 8                                                      |                        80.7 |                               16.1 |                37.3 |                 5.01 |
| 7                                                      |                        78.1 |                               16.1 |                37.4 |                 4.85 |
| 6                                                      |                        76.2 |                               15.7 |                34.7 |                 4.85 |
| 5                                                      |                        72.2 |                               15.4 |                36.5 |                 4.68 |

* Baseline

This  technique  does  not  improve  the  trading  solution  and  will  not  be added.

## ■ Limit the Percentage of Total Portfolio Open-Trade Risk

This technique is similar to the small-account money management strategy of limiting the total portfolio open-trade dollar risk to a max amount. The difference is that instead of a fixed dollar cap, a percentage value is formed by dividing the total portfolio dollar value of open-trade risk by total account equity. If the limit is exceeded, the trade with the largest open-trade risk is exited. Note that this is a form of profit-taking; the trade that is exceeded will be deeply in profit, and the exit is done at the peak profit of the trade to that point. Table 14.8 shows results when this technique is added to the baseline.

| Trades Limited to a Max Open-Trade Percent of Equity   |   Average Annual Return (%) |   Average Annual Max Draw-Down (%) |   Max Draw-Down (%) |   Gain-to-Pain Ratio |
|--------------------------------------------------------|-----------------------------|------------------------------------|---------------------|----------------------|
| All*                                                   |                        87.5 |                               16.3 |                37.4 |                 5.37 |
| 50                                                     |                        84.4 |                               16.1 |                36.7 |                 5.24 |
| 40                                                     |                        77.9 |                               15.3 |                35.1 |                 5.09 |
| 30                                                     |                        62.6 |                               14.8 |                29.0 |                 4.23 |

This  technique  does  not  improve  the  trading  solution  and  will  not  be added. The fact that there is a change from the baseline when trades are exited if the total percentage of open-trade risk is 50 percent of the portfolio signifi  es that there is a large variation in the percentage of portfolio open-trade risk; 50 percent of account equity is a lot, especially when we're only risking 1 percent of equity at trade origination. It would seem that curtailing trades when portfolio risk is at the large extremes would be the prudent thing to do, but  Table   14.8 clearly shows otherwise (with this strategy). In my experience this money management technique is eff  ective with strategies that have a relatively large open-trade equity give-back.

Figure   14.1 shows open- and closed-trade equity buildup for the baseline large-account money management solution on our commodity strategy.  The equity is plotted on a logarithmic scale.

FIGURE  14.1 Open- and Closed-Trade Equity Curve for Commodity Strategy

<!-- image -->

Table   14.9 shows the year-by-year returns and draw-downs.

<!-- image -->

## Annual Return and Max Draw-Down for Large-Account Trading of the Commodity Strategy

| Year    |   Yearly Profit (%) |   Annual Max Draw-Down (%) |
|---------|---------------------|----------------------------|
| 1980    |                12.5 |                       11.7 |
| 1981    |                98.3 |                       13.9 |
| 1982    |               123.8 |                       13.1 |
| 1983    |                73.1 |                        8.7 |
| 1984    |                92.0 |                       13.9 |
| 1985    |                89.2 |                       15.6 |
| 1986    |                46.6 |                       12.4 |
| 1987    |               421.1 |                       17.8 |
| 1988    |                92.9 |                       15.1 |
| 1989    |                36.8 |                       26.8 |
| 1990    |               173.0 |                       18.8 |
| 1991    |               120.5 |                       12.6 |
| 1992    |                54.5 |                       14.6 |
| 1993    |               159.3 |                       12.1 |
| 1994    |                70.7 |                       18.8 |
| 1995    |               130.8 |                       15.9 |
| 1996    |                58.4 |                       22.3 |
| 1997    |               111.0 |                       17.6 |
| 1998    |               105.1 |                       23.5 |
| 1999    |                28.6 |                       27.8 |
| 2000    |               103.3 |                        8.5 |
| 2001    |                11.0 |                       21.7 |
| 2002    |                37.7 |                       20.7 |
| 2003    |               202.2 |                       15.9 |
| 2004    |                32.6 |                       15.6 |
| 2005    |                44.9 |                       20.2 |
| 2006    |                26.5 |                       17.0 |
| 2007    |                61.3 |                       15.3 |
| 2008    |               107.4 |                       12.1 |
| 2009    |                29.9 |                       11.5 |
| 2010    |                45.8 |                        9.1 |
| 2011    |                 0.5 |                       19.4 |
| Average |                87.5 |                       16.3 |

Note a few observations concerning the yearly numbers:

- ■ Risk is obviously increasing over time. For the first half of the run (1980 through 1995), only one year had a max draw-down of 20 percent or greater. Over the second half, six years did. Also, the average max drawdown for the first half of the run was 15.1 percent per year, while it was 17.4 percent per year over the last 16 years of the run.

TECHINQUES FOR LARGE ACCOUNTS: COMMODITIES

- ■ Profitability  is  decreasing.  Over  the  first  16  years,  the  average  profit-per-year  was  112.2  percent.  It  was  62.9  percent  over  the  second 16-year    period. Also,  the  last  year  shown  had  the  worst  profit  in  the whole 32-year period (not even 1 percent).
- ■ These tendencies indicate there was been a shift in the way commodities trade. I  attribute  it  to  increased  volatility,  but  I  don't  think  it's  a  onetime step change. I believe that starting around the time of the dot-com bubble, more and more money found its way into the commodity asset class and that money was not traded/invested in the same way as it had in the past: by money managers trying to make money on the long side as prices went up, and on the short side as prices went down. An increasing percentage of it is being traded/invested by managers collecting a sector, whether it be energies, metals, financials, and so forth.  That makes price movement choppier as the two methodologies collide.
- ■ We are almost to the point where there is enough historical data to generate thousands of trades over commodity data from the mid- to late-1990s on. Developing a minimally curve-fit solution over that data set would yield an entirely different solution set than what we have in this book, and probably better than what we have here over that time frame.

One of the advantages of large-account trading is that you're not stuck with a one-point trading solution like you are with the small accounts.  You can tailor the resultant solution to your risk-taking preference by varying the amount you risk per trade while leaving the rest of the money management rules as is. Table 14.10 shows results when the percentage of equity risked per trade is varied from small to rather large.

| TABLE 14.10                        | Performance versus Percent of Equity Risked per Trade   | Performance versus Percent of Equity Risked per Trade   | Performance versus Percent of Equity Risked per Trade   | Performance versus Percent of Equity Risked per Trade   |
|------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
| Percent of Equity Risked per Trade | Average Annual Return (%)                               | Average Annual Max Draw-Down (%)                        | Max Draw-Down (%)                                       | Gain-to-Pain Ratio                                      |
| 0.25                               | 18.5                                                    | 4.8                                                     | 11.8                                                    | 3.85                                                    |
| 0.50                               | 39.8                                                    | 9.1                                                     | 21.7                                                    | 4.37                                                    |
| 0.75                               | 62.9                                                    | 12.9                                                    | 30.1                                                    | 4.88                                                    |
| 1                                  | 87.5                                                    | 16.3                                                    | 37.4                                                    | 5.37                                                    |

Again, the greater the pain a trader can take in the form of draw-down, the greater the relative reward, as the increasing gain-to-pain ratio shows.

## ■ Conclusion

This chapter has shown that if we risk 0.5 percent of equity per trade, limit group exposure to a max of seven trades at a time, and limit the number of total trades to 30 or fewer, we have a very tradeable solution for large accounts: an average annual return of over 39 percent, a max draw-down in the last 32 years of 21.7 percent, and an expected max draw-down of under 10 percent each year. But the beauty of large-account trading is that you're not stuck with a one-point trading solution like you are with the small accounts.  Y ou can tailor the resultant solution to your risk-taking preference by varying the amount you risk per trade while leaving the rest of the money management rules as is.

One last note about the large-account money management techniques: You may have noticed that the performance gains, aside from the fixed-risk sizing, were at best marginal; the difference in the gain-to-pain ratio only increased from 5.17 to 5.37. The fixed-risk sizing did contribute a jump in performance over the gain-to-pain ratio we achieved in Chapter 12 with our full-size portfolio, a value of 2.98. The reason for the small increase after the fixed-risk sizing was due to the way the commodity strategy was developed: Each rule and parameter value maximized the reward-to-risk ratio. There simply wasn't much left for the money management to do on the risk side once each trade was put on at a size that equalized trade risk across the portfolio.

In the next chapter, we'll develop a large-account money management solution for the stock strategy.

## Traditional Money Management Techniques for Large Accounts: Stocks

C hapter 14 introduced the large account tactics a trader can use to tailor a system to a desired set of performance metrics. In this chapter we'll apply some of those tactics to the stock strategy we developed in Chapters 4 through 6. As noted in the small account money management chapter for stocks (Chapter 13), groups are not applicable to the NASDAQ stocks.

## ■ Fixed-Rate Sizing

This is the identical money management approach we used last chapter with the commodity system: A fixed percentage of equity is risked on each trade. It is implemented by multiplying the fixed percentage by account equity on the day of the trade to determine the dollar amount to be risked. Then, the strategy's trade risk is used to determine the number of shares that should be traded to risk the desired amount. For the stock system, we do not have a

233

catastrophic stop, so the trade risk will have to be another measure of volatility . In Chapter 13, we used the three standard deviations of closing price, converted to dollars by multiplying the point value by the number of shares bought with the $5,000 position. Let's use that again.

This tactic was tested on the Donchian counter-trend-following strategy across the NASDAQ 100-stock basket (2000-2011). Starting account equity of $1,000,000 was used.  Table 15.1 highlights performance metrics for various fixed-risk percentages.

TABLE 15.1 Fixed-Risk Performance on the Stock Strategy

| Percent Risked Per Trade   |   Average Annual Return(%) |   Average Annual Largest Draw-Down(%) |   Max Draw- Down(%) |   Gain-to-Pain Ratio |
|----------------------------|----------------------------|---------------------------------------|---------------------|----------------------|
| 0.5                        |                       19.6 |                                   8.3 |                16.6 |                 2.38 |
| 1*                         |                       45.8 |                                  16.7 |                32.4 |                 2.74 |
| 2                          |                      123.8 |                                  32.5 |                60.7 |                 3.81 |
| 3                          |                      251.4 |                                  47.3 |                85.4 |                 5.31 |

*Baseline

Table 15.1 shows that the average annual return is greater than the max draw-down and more than twice as large as the average max draw-down in all cases; we are assured of a tradeable solution. For the rest of the development we'll use 1 percent as the amount risked per trade. Let's look to limit the number of trades that are open at a time.

## ■ Limit the Total Number of Open Trades

This is the same strategy used with the large-account money management commodity system. If the number of ongoing open trades reaches a threshold, new signaled trades are passed. Table 15.2 shows the pertinent starttrade statistics when the number of open trades is capped.

TABLE 15.2 Limit the Total Number of Open Trades

| Max Number of Open Trades   |   Average Annual Return (%) |   Average Annual Max Draw-Down (%) |   Max Draw- Down (%) |   Gain-to-Pain Ratio |
|-----------------------------|-----------------------------|------------------------------------|----------------------|----------------------|
| All Trades*                 |                        45.8 |                               16.7 |                 32.4 |                 2.74 |
| 45**                        |                        45.7 |                               16.3 |                 32.4 |                 2.80 |
| 40                          |                        45.1 |                               16.3 |                 32.4 |                 2.76 |
| 35                          |                        44.6 |                               16.1 |                 32.4 |                 2.76 |
| 30                          |                        42.9 |                               15.8 |                 32.4 |                 2.72 |
| 25                          |                        39.4 |                               15.6 |                 32.4 |                 2.53 |

The results show that limiting the number of trades to 45 is the best trading solution, as measured by the gain-to-pain ratio. That condition will be added to the baseline to form the new baseline.

## ■ Position Hedging

As  we  saw  in  the  development  of  small-account  money  management rules  for  our  stock  system,  hedging  one  or  more  long  positions  with short positions in a market surrogate like the SPY ETF can help performance. Table 15.3 shows the baseline with a number of short hedges added.

TABLE 15.3 Hedging with Short SPY Positions

| Max Number Long/ Short Positions   |   Average Annual Return (%) |   Average Annual Max Draw-Down (%) |   Max Dr |   Gain-to-Pain Ratio |
|------------------------------------|-----------------------------|------------------------------------|----------|----------------------|
| 45/0*                              |                        45.7 |                               16.3 |     32.4 |                 2.80 |
| 45/1                               |                        44.2 |                               15.2 |     30.6 |                 2.90 |
| 45/2**                             |                        44.6 |                               15.0 |     27.2 |                 2.96 |
| 45/3                               |                        43.3 |                               15.8 |     25.5 |                 2.74 |
| 45/4                               |                        43.1 |                               16.7 |     27.8 |                 2.58 |

* Baseline

** New baseline

The results show that this money management technique brings down both average max draw-down and max draw-down significantly from the baseline. We'll  add  two  SPY  hedges  to  the  existing  money  management overlay to form the new baseline.

## ■ Limit Trade Risk on Entry

This technique is the same as we explored in the small account money management chapter for commodities (Chapter 12).  When a trade is originated, the trade risk is the distance, converted to dollars, from the entry point to the catastrophic stop-loss point. Because our three-standard-deviation stop is volatility-based, some trades will have a relatively small risk, and some a relatively large risk. Using this money management strategy, trades with a

235

STOCKS

high trade risk are bypassed. Table 15.4 shows results for a range of entryrisk limits.

| TABLE 15.4           | Limit Trade Risk on Entry   | Limit Trade Risk on Entry        | Limit Trade Risk on Entry   | Limit Trade Risk on Entry   |
|----------------------|-----------------------------|----------------------------------|-----------------------------|-----------------------------|
| Trade Risk Limit ($) | Average Annual Return (%)   | Average Annual Max Draw-Down (%) | Max Draw- Down (%)          | Gain-to-Pain Ratio          |
| All Trades*          | 44.6                        | 15.0                             | 27.2                        | 2.96                        |
| 1,200                | 41.8                        | 15.6                             | 25.5                        | 2.68                        |
| 1,000                | 40.5                        | 15.6                             | 25.5                        | 2.60                        |
| 800                  | 36.9                        | 14.7                             | 25.5                        | 2.51                        |
| 600                  | 28.2                        | 12.3                             | 25.9                        | 2.30                        |

*Baseline

No improvement is seen with this money management technique so the baseline will remain unchanged.

## ■ Other Large-Account Money Management Techniques

In the large account money management development chapter for the commodity system (Chapter 14), we looked at two other large-account money management techniques: limit open-trade risk and limit total portfolio open-trade risk.  Those techniques will not help our stock strategy.  We have a $300 scalping profit-target in place, and both of those techniques are a form of profit-taking.

## ■ Tradeable Solutions for the Stock System

The final large-account money management overlay for our stock system is:

- ■ Limit the number of trades to 45 or less.
- ■ Hedge with two short SPY position.

We saw that when trading this overlay at 1 percent fixed per position, the strategy averaged 44.6 percent per year, had a 15.0 percent average max draw-down, and a max draw-down in the last 12 years of 27.2 percent.

Table   15.5 shows performance using the same money management overlay, but varying the amount risked per trade.

TABLE 15.5

Large-Account Stock Performance at Various Risk Levels

|   Amount Risked per Trade(%) |   Average Annual Return (%) |   Average Annual Max Draw-Down (%) |   Max Draw- Down (%) |   Gain-to-Pain Ratio |
|------------------------------|-----------------------------|------------------------------------|----------------------|----------------------|
|                            1 |                        44.6 |                               15.0 |                 27.2 |                 2.96 |
|                          0.8 |                        33.4 |                               12.1 |                 21.8 |                 2.76 |
|                          0.6 |                        23.5 |                                9.0 |                 16.4 |                 2.61 |
|                          0.4 |                        14.5 |                                5.9 |                 10.8 |                 2.46 |
|                          0.2 |                         6.3 |                                2.8 |                  5.1 |                 2.26 |

You can see that the higher the amount risked, the better the trading solution in terms of the gain-to-pain ratio. But some risk-averse traders might opt for the 0.2 percent-risked-per-trade solution.  There is no 'right' choice, only what's right for you.

Figure    15.1  shows  open-  and  closed-trade  equity  buildup  for  the 0.6 percent risked-per-trade case.

FIGURE  15.1 Open- and Closed-Trade Equity Curve for Stock Solution when Traded at 0.6 Percent of Equity per  Trade

<!-- image -->

Lastly, Table   15.6 shows the yearly return and max draw-down for the stock solution traded at 0.6 percent of equity.

## Annual Return and Draw-Down for Large-Account Stock Solution Traded at 0.6 Percent of Equity per Trade

|   Year |   Yearly Profit (%) |   Annual Max Draw-Down (%) |
|--------|---------------------|----------------------------|
|   2000 |                29.1 |                        8.8 |
|   2001 |                37.7 |                        9.6 |
|   2002 |                36.2 |                        8.5 |
|   2003 |                66.6 |                       10.2 |
|   2004 |                 6.1 |                        6.6 |
|   2005 |                 8.4 |                        4.7 |
|   2006 |                -7.3 |                       11.0 |
|   2007 |                20.1 |                        5.3 |
|   2008 |                -5.0 |                        9.7 |
|   2009 |                67.3 |                        7.5 |
|   2010 |                10.5 |                        9.8 |
|   2011 |                12.3 |                       16.4 |

## ■ Conclusion

In this chapter we developed a large-account money management overlay for the stock strategy developed in Chapters 4 through 6. Taking the first solution from Table 15.4 that has a max draw-down around 20 percent, we see that the gain-to-pain ratio is 2.61 when the money management overlay is traded at 0.6 percent of equity per trade. In Chapter 14, we developed a large-account overlay for the commodity strategy. Choosing the first commodity solution with a max draw-down near 20 percent, we see that the solution traded at 0.5 percent of equity had the following performance:

Average annual return: 39.8 percent

Average annual max draw-down: 9.1 percent

Max draw-down: 21.7 percent

Gain-to-pain ratio: 4.37

Table 15.7 shows the significant differences among these strategies.

TABLE 15.7

## Summary of Differences among Strategies

|                     | Stock Strategy   | Commodity Strategy   |
|---------------------|------------------|----------------------|
| Instruments Traded  | Stocks           | Commodities          |
| Trading Methodology | Counter-Trend    | Trend-Following      |
| Trade Horizon       | Short-Term       | Mid-Term             |

Even though the differences are huge, I contend that these strategies can be directly compared through their respective gain-to-pain ratios.  The commodity strategy is  better  than  the  stock  strategy  because  its  gain-to-pain ratio is more than 65 percent higher than the stock strategy.

Does that mean we should discard the stock strategy and only trade the commodity strategy? The next chapter will show that trading both (if your account is large enough) provides a better solution than either alone.

## Trading the Stock and Commodity Strategies Together

I n Chapter 14 and Chapter 15, we developed large account money management overlays for our stock and commodity strategies. Stock traders may opt to only trade the stock strategy, while commodity traders may only feel comfortable with the commodity strategy. But there are some traders who would trade both, if there were a good reason to do so.

In this chapter, we'll test whether the two can be traded together to yield a trading solution that is better than either alone. Since the stock strategy was only traded from the year 2000, we'll limit commodity trades to the same time frame.

## ■ The Mechanics of Trading Two (or More) Strategies Together

There  are  a  number  of  ways  to  trade  two  strategies  together,  but  the two that have the least associated bookkeeping are segregated equity and combined equity. In segregated equity, you split your account equity into two  pieces  and  trade  each  strategy  independently  on  its  assigned  equity.

Physically, this can easily be done with sub-accounts with your brokerage firm. A variation on the segregated approach is to periodically combine the equity in the two accounts and split the money back in the same proportion as it was originally allocated. In the combined equity approach, all strategies are traded out of the total funds. We'll test the simplest approach: trading on the combined equity.

## ■ Trading the Stock and Commodity Strategies on Combined Equity

If the stock and commodity strategies were traded together at their full fixedrisk percentages, the leverage used would be much greater than trading either alone on the same amount of equity. For that reason, the fixed-risk percentages need to be adjusted down. If we want an apples-to-apples comparison of the combined strategy versus either alone, the fixed-risk percentages need to be halved (the same idea as trading the full fixed-risk percentage on half the equity). Table 16.1 compares the combined strategy performance with the performance of each strategy traded alone when the fixed-risk amount is halved in the combined system run. Note that the commodity performance shown is only for January 2000 through the end of 2011.

| TABLE 16.1   | Apples-to-Apples Comparison of Individual Strategy Performance and Combined Strategy Performance, 2000-2011   | Apples-to-Apples Comparison of Individual Strategy Performance and Combined Strategy Performance, 2000-2011   | Apples-to-Apples Comparison of Individual Strategy Performance and Combined Strategy Performance, 2000-2011   | Apples-to-Apples Comparison of Individual Strategy Performance and Combined Strategy Performance, 2000-2011   |
|--------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Strategy     | Average Annual Return (%)                                                                                     | Average Annual Max Draw-Down (%)                                                                              | Max Draw-Down (%)                                                                                             | Gain-to-Pain Ratio                                                                                            |
| Stock        | 23.5                                                                                                          | 9.0                                                                                                           | 16.4                                                                                                          | 2.61                                                                                                          |
| Commodity    | 26.6                                                                                                          | 11.0                                                                                                          | 21.7                                                                                                          | 2.42                                                                                                          |
| Both         | 25.5                                                                                                          | 6.0                                                                                                           | 8.6                                                                                                           | 4.25                                                                                                          |

The table shows that trading the two strategies together is a better solution than trading either alone; the gain-to-pain ratio rises to over $4 of return for every $1 of draw-down.  That performance increase is due to a large reduction in average annual max draw-down and max draw-down.

Table 16.1 reflects performance if the stock and commodity strategies are allocated 50 percent of account equity each. Perhaps a better solution would be to overweight one strategy.  T o keep the apples-to-apples comparison going, let's have each solution sum to a total of one, just as the half and half of the previous run does. Table 16.2 shows performance outcomes for various weightings.

<!-- image -->

Apples-to-Apples Comparison of Individual Strategy Performance and Combined Strategy Performance, 2000-2011, for Various Weightings

| Commodity Fraction/ Stock Fraction   |   Average Annual Return (%) |   Average Annual Max Draw-Down (%) |   Max Draw- Down (%) |   Gain-to-Pain Ratio |
|--------------------------------------|-----------------------------|------------------------------------|----------------------|----------------------|
| 0.5/0.5*                             |                        25.5 |                                6.0 |                  8.6 |                 4.25 |
| 0.55/0.45                            |                        25.7 |                                6.2 |                  9.0 |                 4.15 |
| 0.45/0.55**                          |                        25.3 |                                5.9 |                  9.3 |                 4.29 |
| 0.40/0.60                            |                        24.8 |                                6.0 |                 10.0 |                 4.13 |

A marginal increase is seen when we overweight the stock side and underweight the commodity side by 10 percent.

Lastly, since the max draw-downs are relatively small on the combined strategy runs, we can leverage up from the baseline leverage by scaling with a multiplier. If, for example, the base fixed-risk leverage was 0.5 percent per trade and we scaled up by 10 percent, the new fixed-risk leverage would be 0.5 multiplied by 1.1, or 0.55 percent. Table 16.3 shows results for a number of increased leverage factors.

| TABLE 16.3          | Increasing the Leverage on the Baseline   | Increasing the Leverage on the Baseline   | Increasing the Leverage on the Baseline   | Increasing the Leverage on the Baseline   |
|---------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| Leverage Multiplier | Average Annual Return (%)                 | Average Annual Max Draw-Down (%)          | Max Draw- Down (%)                        | Gain-to-Pain Ratio                        |
| 1                   | 25.3                                      | 5.9                                       | 9.3                                       | 4.29                                      |
| 1.1                 | 27.8                                      | 6.4                                       | 10.2                                      | 4.34                                      |
| 1.2                 | 30.8                                      | 7.0                                       | 11.1                                      | 4.40                                      |
| 1.3                 | 33.4                                      | 7.6                                       | 12.0                                      | 4.39                                      |
| 1.4                 | 36.3                                      | 8.2                                       | 12.9                                      | 4.43                                      |
| 1.5                 | 39.2                                      | 8.7                                       | 13.7                                      | 4.51                                      |

Again you'll note that the more risk you can assume, the greater the relative reward. Any of these solutions is tradeable.

## ■ Conclusion

In  this  chapter  we  developed  a  money  management  overlay  to  trade  the stock and commodity strategies together. The resultant overlay had performance that was much better than either strategy alone. This performance increase was due to a large reduction in both draw-down metrics. The best solution is to trade the commodity strategy at 45 percent of its large-account money management allocation, and the stocks at 55 percent of their large-account money management allocation. If it is desired to increase the return, those allocations can be multiplied by a leverage factor to yield the performance shown in the Table 16.3.

This  chapter  suggests  why  system  development  should  be  an  ongoing process. Even if you have a very tradeable strategy, finding and adding new ones can lead to even better trading solutions.  The key, of course, is that they need to be different-not necessarily in the instruments they trade, but different enough that the resultant equity curve is not highly correlated with the equity curves of your current systems.

## Understanding the Formulas

T his appendix will provide practical details behind some of the formulas used throughout the book.

## ■ Standard Deviation

Standard deviation is a measure of dispersion from the mean.  The formula is:

where:

<!-- formula-not-decoded -->

n = the number of samples in the group

x i = the i th sample in the group

μ = the mean of a group that has n samples

σ = the standard deviation of the samples in the group

245

The formula may look imposing, but it is really very simple to compute. You find the mean of the samples in the group by adding up all the values and then dividing by the number of samples.  Then you sum all the squared values of the mean minus the sample value and divide that sum by the number of samples minus one to yield a value called the variance. Lastly, you take the square root of the variance.  You may see this formula with n as the divisor instead of n - 1.  That formula is used on an entire population of samples like all the heights of all the people in the world. When you're computing the standard deviation on a sample of the entire population, like the heights of all the people in the United States, you use the n - 1 value. For large sample size, it makes little difference.

In this book, the samples are usually closing prices over some period. A 20-day standard deviation of closing price would be found using the closes of  the  last  20  days  as  the  group  sample  in  the  formula.  But  standard  deviation can be used on other samples, such as range (daily high minus the daily low).  When the top-to-bottom range of samples is small, the standard deviation will be small, and when it is large, the standard deviation will be relatively large. Thus for a tradeable that goes through benign periods and trending periods, the standard deviation of the closes, or the range, will expand or contract with the volatility.

The significance  of  the  standard  deviation,  or  one-sigma  value,  is  that for a normally distributed group (looks like a bell-shaped curve) the range of  values  one  standard  deviation  below  the  mean  to  one  standard  deviation above the mean constitute approximately 68 percent of the values in a sample group.  The two-sigma range (the one-sigma value multiplied by two) above and below the mean includes approximately 95 percent of the values, while the three-sigma range includes about 99.7 percent of the sample values. A distribution does not have to be normally distributed to use the standard deviation formula. It still yields a measure of dispersion from the mean for other distributions.

## ■ Volatility Measures and Comparison

Besides standard deviation, average range and average true range are other commonly used measures of volatility in trading systems.  The difference between average range and average true range is that average true range adds the distance between yesterday's bar and today's bar if today's bar is a gap bar. Average range just includes the distance from the high to the low for each bar used to compute the average. I've found very little diff  erence in using average true range or average range, so I pretty much just use one: average range. There is a big diff  erence between using range and standard deviation as volatility measures.

The primary diff  erence is that standard deviation accounts for directional volatility, while average range doesn't. The two data streams in fi  gure   A.1 will yield the same average range number over the 18 bars shown because the distance from the high to the low each day is the same in both streams. But the standard deviation calculation will have a much higher standard deviation number for the fi  rst stream because the closes are trending. In this case standard deviation captures the real volatility better than average range.  The bottom line is that I always check both measures when I use a volatility fi  lter.

FIGURE A.1 Non-Directional and Directional Data Streams

<!-- image -->

## ■ Correlation

Correlation is the degree to which two data streams move in the same direction. There is a mathematical formula called the Pearson correlation coeffi  cient that measures correlation values, referred to as r , in the range -1 to 1. If two data streams yield a value of 1, they are perfectly correlated and rise and fall together, although not necessarily at the same rate.  When the output is -1, they are perfectly negatively correlated and when one rises the other falls-again, not necessarily at the same rate. For values close to 0, the two data streams are non-correlated and the data streams move independently of each other. Figure   A.2 shows pairs of data streams and their associated correlation coeffi cients.

FIGURE A.2 Correlation Coeffi cients for  Various Data Pairs

<!-- image -->

The formula to compute the Pearson correlation coeffi cient is:

<!-- formula-not-decoded -->

where:

n = the number of samples in the group

x i = the i th sample in data stream 1

y i = the i th sample in data stream 2

r = the Pearson correlation coeffi cient

This is another formula that looks complex, but it can be calculated in a  single  pass  of  the  two  data  streams  (stream x and  stream y ).  If  the  two streams are paired, as you go down the two columns you make three calculations: the sum of the product of the two data points, ∑ x i y i ; the sum of the x points, ∑ x i ; and the sum of the y points, ∑ y i .  Then just insert in the formula and solve for r .

There are many uses for correlation. In Appendix B, it will be used to show the degree of correlation between commodities in the same group. It can also be used to show the degree of serial correlation in a data stream. Serial correlation is the degree to which previous data in the stream infl  uences the value of succeeding data. If a stream has a high degree of serial correlation, up-moves in the stream will be followed by other up-moves, and down-moves followed by down-moves. Serial correlation can be exploited for gain. Suppose the profit for each trade is put in a file sequentially and correlated with the same file lagged by one place. If the correlation of the two streams is positive, it means winning trades have a tendency to follow a period of winning trades, and losing trades follow losers. In real trading, when you have a good winning streak you might up the size of your trades to take advantage of expected additional winners, and when in a losing streak, reduce size or even cut off trading.

In trading, perhaps the best use of correlation is to illustrate the power of diversification in money management. If the difference in consecutive closing prices of two trading variables is normally distributed, a third variable formed by summing the first two will have the following standard deviation:

<!-- formula-not-decoded -->

where:

- σ 1 is the standard deviation of the change in closes of the first variable
- σ 2 is the standard deviation of the change in closes of the second variable
- is the standard deviation of the change in closes of the new variable
- 12 is the correlation coefficient between the two variables
- σ 3 r

Think of the first two variables as trades in your portfolio that move in price from day to day (hopefully in the direction of your trade). The third variable is the portfolio value.  The standard deviation of portfolio value represents the movement of the portfolio, either up or down. It is instructive to assign some values to the variables and look at outcomes, as Table A.1 illustrates.

TABLE A.1 Portfolio Outcomes Based on Two Variables

|   Variable 1 Standard Deviation (Points) |   Variable 2 Standard Deviation (Points) |   Correlation between 1 and 2 |   Variable 3 Standard Deviation (Points) |
|------------------------------------------|------------------------------------------|-------------------------------|------------------------------------------|
|                                        5 |                                        5 |                             1 |                                       10 |
|                                        5 |                                        5 |                             0 |                                      7.1 |
|                                        5 |                                        5 |                            -1 |                                        0 |

The first row in the table has Variable 1 and Variable 2 perfectly correlated. When the close of Variable 1 is up, so is that of Variable 2. When the close of Variable 1 is down, so is that of Variable 2. They are moving in perfect lock-step. Since the standard deviation of both  Variable 1 and  Variable 2

is the same (a value of 5), the portfolio moves as if you're trading two contracts of the same tradeable (10 points).

The second row highlights the rationale behind the diversification used in traditional money management. With no correlation between Variable 1 and Variable 2, the portfolio moves less than the sum of the two variables' standard deviations, but more either variable alone. Some people make the argument that if your portfolio is fully diversified with uncorrelated assets, your risk actually goes down.  This two-variable portfolio shows that the risk doesn't go down. With each additional uncorrelated variable portfolio risk does go up, but at a decreasing rate.

The last row shows trading nirvana. If you could successfully trade two instruments at the same time that are perfectly negatively correlated, you would have no risk. There are commodities that are negatively correlated to a high degree like the Dollar Index and the Japanese yen, but finding a strategy that makes money on both while long at the same time, or short at the same time is the problem.

The two-variable formula above can be easily extended to any number of tradeables, trading any number of contracts/shares of either long or short positions.

## Understanding Futures

C ommodity trading is a zero-sum game. For each contract traded, there will be a buyer and a seller. For traders, not hedgers, the buyer believes the price of the commodity is going up, while the seller believes the price is going down. Price movement up from the entry price of the trade will cause the buyer to have a profitable position (positive open-trade equity, or run-up), while the seller will be in the red by the exact same amount the buyer is ahead (negative open-trade equity, or draw-down).  When either the buyer or seller closes out a position, that trade is ended with either a profit or loss (closed-trade profit or loss).

Commodities are traded by a number of exchanges in the United States and abroad.  The exchange is really a sponsor of the commodity being traded and administers trading to include the size of the contract, the hours it is traded,  the  delivery  months  traded,  minimum  movement  of  price,  and margin requirements.

## ■ The Contract

The basis of trading is the commodity contract. It has a specific start date and an expiration date.  The contract is an obligation to either buy or provide the underlying commodity at the price the trade is entered at upon contract expiration. The seller commits to provide the underlying deliverable. Most trades are ended before contract expiration, so a trader can exit his position before first notice day, and neither provide nor take delivery of the contract. There are commodity contracts for a variety of raw materials and foodstuffs like copper or corn. The vast majority of these are settled in the physical deliverable. A  seller  of  a  copper  contract  would  have  to  deliver  25,000 pounds of high-grade copper upon contract expiration, while a buyer of corn would receive 5,000 bushels of corn.

Each  contract  has  a  specific  size  and  a  specific  trading  start  date  and contract expiration date. As a trader, you will probably want to trade the most liquid month. Generally the most liquid month has the highest reported volume and open interest. It is called the front month because most speculative traders are making their trades on that contract. Volume is the total number of contracts traded on a given day. It is reported in two ways: by contract, or across all contracts. Open interest is the total number of paired contract positions. If the open interest is reported at 10,000 contracts, it means that there are 10,000 long positions and 10,000 short positions.

## ■ Contract Pricing

As a trader, it is crucial to understand the potential risk and reward of any position you enter. Risk and reward depend on the type of contract you are trading (oats versus the S&amp;P , for example), the relative recent volatility of the commodity, and the way it is priced by the exchange. The size of a corn contract is 5,000 bushels. If the price of a bushel goes up a penny, the value of the corn contract has just increased by $50 ($0.01 × 5,000). If the price of a copper contract goes down by a penny, the value of the copper contract has decreased by $250 ($0.01 × 25,000) where 25,000 is the number of pounds of high-grade copper in one contract.

## ■ Relative Contract Risk

The corn and copper examples illustrate that a one-cent move in copper nets five times as large a change in contract value as a one-cent move in corn.

Is trading copper five times as risky as trading corn? The answer depends on the volatility of the underlying commodity. If corn's price movement is five times as volatile as copper, their contract risks are approximately equal. Volatility can be measured in any number of ways, but I prefer to use the standard deviation of the closing prices. (See Appendix A for information regarding standard deviation.) The standard deviation is just the dispersion of price from its average price over some time frame.  The formula for standard deviation is:

<!-- formula-not-decoded -->

where:

n = the number of samples in the group

x i = the i th sample in the group

μ = the mean of a group that has n samples

σ = the standard deviation of the samples in the group

To  determine  the  relative  risk  of  each  contract,  the  average  40-day standard deviation of the closes over the trading life of the contract was computed. For analysis purposes, continuous contracts were used.  Table B.1 shows the underlying commodity; its mean standard deviation over its life; its max and min standard deviation over its lifetime; and the dollar value of the average standard deviation.

TABLE B.1 Range of Volatility by Commodity

| Commodity     |   Average SD in Points |   Max SD in Points |   Min SD in Points | Average SD in Dollars   |
|---------------|------------------------|--------------------|--------------------|-------------------------|
| Corn          |                   7.68 |              50.50 |               1.32 | $384                    |
| Oats          |                   6.46 |              74.20 |               1.28 | $323                    |
| Soybeans      |                  19.60 |             101.00 |               3.64 | $978                    |
| Soy Meal      |                   6.37 |              39.70 |               1.34 | $634                    |
| Bean Oil      |                   0.80 |               4.63 |               0.20 | $483                    |
| Wheat         |                  11.00 |              61.30 |               2.46 | $553                    |
| KC Wheat      |                  10.40 |              74.80 |               1.92 | $522                    |
| Rough Rice    |                   0.30 |               1.83 |               0.04 | $594                    |
| Live Cattle   |                   1.46 |               7.37 |               0.36 | $585                    |
| Lean Hogs     |                   2.18 |               7.84 |               0.55 | $873                    |
| Feeder Cattle |                   1.49 |               6.69 |               0.32 | $747                    |

( continued )

| Commodity        |   Average SD in Points |   Max SD in Points |   Min SD in Points | Average SD in Dollars   |
|------------------|------------------------|--------------------|--------------------|-------------------------|
| Coffee           |                   6.12 |              46.50 |               1.19 | $2,297                  |
| Cotton           |                   1.99 |               7.64 |               0.48 | $996                    |
| Lumber           |                  11.50 |              77.70 |               1.36 | $1,260                  |
| Cocoa            |                  65.00 |             229.00 |               12.5 | $650                    |
| Sugar            |                   0.57 |               5.78 |               0.11 | $639                    |
| Orange Juice     |                   4.43 |              30.20 |               0.72 | $665                    |
| Copper           |                   3.24 |              19.50 |               0.50 | $811                    |
| Palladium        |                  10.50 |             115.00 |               0.76 | $1,054                  |
| Silver           |                  33.50 |             877.00 |               2.69 | $1,672                  |
| Gold             |                   9.84 |              98.30 |               1.23 | $983                    |
| Platinum         |                  16.40 |             166.00 |               2.35 | $820                    |
| London Copper    |                  61.30 |             514.00 |               11.6 | $1,532                  |
| London Alloy     |                  32.90 |             273.00 |               6.77 | $658                    |
| London Al.       |                  48.30 |             308.00 |               9.63 | $1,207                  |
| London Nickel    |                 354.00 |            3183.00 |               34.4 | $2,123                  |
| Crude Oil        |                   1.09 |               5.11 |               0.13 | $1,095                  |
| Natural Gas      |                   0.23 |               1.72 |               0.01 | $2,328                  |
| Heating Oil      |                   0.30 |               0.14 |              0.005 | $1,270                  |
| Unleaded Gas     |                   0.33 |               0.20 |              0.008 | $1,417                  |
| Japanese Yen     |                  0.013 |              0.057 |              0.001 | $1,596                  |
| Swiss Franc      |                  0.012 |              0.039 |              0.003 | $1,523                  |
| Can. Dollar      |                 0.0058 |              0.021 |             0.0006 | $579                    |
| British Pound    |                  0.026 |               0.12 |             0.0053 | $1,601                  |
| Dollar Index     |                   1.30 |               3.82 |               0.25 | $1,303                  |
| Mexican Peso     |                 0.0017 |             0.0094 |            0.00045 | $839                    |
| Australian Doll. |                  0.010 |              0.033 |             0.0025 | $1,028                  |
| Euro-Currency    |                  0.018 |              0.052 |             0.0056 | $2,241                  |
| 30-Year Bond     |                   1.36 |               5.14 |               0.28 | $1,364                  |
| 10-Year Note     |                  0.995 |               2.93 |               0.21 | $995                    |
| 5-Year Note      |                   0.67 |               1.75 |               0.15 | $670                    |
| 2-Year Note      |                   0.30 |               0.85 |              0.066 | $596                    |
| Euro-Dollar      |                   0.19 |               1.42 |              0.004 | $484                    |
| Australian Bond  |                   0.19 |               0.82 |              0.051 | $1,095                  |
| Canadian Bond    |                   0.94 |               2.40 |               0.26 | $640                    |
| Euro-Bund        |                   0.80 |               1.95 |               0.22 | $760                    |
| Long Gilt        |                   1.04 |               3.77 |               0.28 | $797                    |
| Spanish Bond     |                   0.87 |               2.20 |               0.26 | $825                    |
| Simex JGB        |                   0.89 |               3.22 |               0.24 | $822                    |
| S&P500           |                  14.70 |              81.00 |               1.22 | $6,128                  |
| Nasdaq 100       |                  88.00 |             465.00 |               11.4 | $8,800                  |
| Nikkei           |                 529.00 |            1558.00 |                110 | $2,646                  |

Table B.1 clearly shows that there is a big difference between contracts. The average 40-day standard deviation results in a variance of $8,800 for a full-size Nasdaq 100 contract, but only $323 for oats. It is clearly much riskier to trade a Nasdaq 100 contract than an oat contract. Moreover, the max and min variance within a given commodity shows that at different times there is a big difference within the same commodity. The Nasdaq 100 has an average volatility of $8,800, but it has been as low as $1,140 and as high as $46,500, a very large range.  This is the reason I advocate using stops relative to recent volatility.

## ■ Commodity Groups

It is convenient to group commodities into categories.  The most commonly used grouping refers to the grains (or agriculturals), meats, metals, energies, currencies, financials, softs, and stock indices. The following breakout is my grouping of the commodities that I develop trading systems across:

| Grains        | Meats           | Softs             |               |
|---------------|-----------------|-------------------|---------------|
| Corn          | Live Cattle     | Coffee            |               |
| Oats          | Lean Hogs       | Cocoa             | 255           |
| Soybeans      | Feeder Cattle   | Cotton            |               |
| Soymeal       |                 | Sugar             |               |
| Bean Oil      | Metals          | Orange Juice      |               |
| Wheat         | Gold            | Lumber            |               |
| KC Wheat      | Copper          |                   | UNDERSTANDING |
| Rough Rice    | Palladium       | Currencies        |               |
|               | Platinum        | Australian Dollar |               |
| Energies      | London Nickel   | Euro-Currency     |               |
| Crude Oil     | London Copper   | Swiss Franc       |               |
| Natural Gas   | London Alloy    | Canadian Dollar   |               |
| Heating Oil   | London Aluminum | British Pound     | FUTURES       |
| Unleaded Gas  | Silver          | Mexican Peso      |               |
|               |                 | Japanese Yen      |               |
| Stock Indices | Financials      | Eurodollar        |               |
| S&P 500       | 30-Year Bond    |                   |               |
| Nasdaq 100    | 10-Year Note    |                   |               |
| Russell 2000  | 5-Year Note     |                   |               |
| Midcap 400    | 2-Year Note     |                   |               |
| Nikkei        | Australian Bond |                   |               |
|               | Euro Bund       |                   |               |
|               | Spanish Bond    |                   |               |
|               | Long Gilt       |                   |               |
|               | Dollar Index    |                   |               |

The reason to group commodities is that, generally, those in the same group are highly correlated with each other. For money management reasons it is much more advantageous to trade a basket of commodities that are lowly correlated to each other than a basket that is high correlated, even if each basket makes the same amount of money over time. The reason to avoid correlated commodities is that they tend to move together. A good trade in one will be a good trade across all, and a bad trade in one will generally be a bad trade for all the other commodities highly correlated to it. It is the bad trades to watch out for. A number of trades losing at the same time will cause a big pullback in your trading equity (draw-down). On the other hand, it is much more likely that an uncorrelated basket will not frequently have bad trades together.  They tend to move on their own individual fundamentals independently of each other.

When a correlation algorithm is used on two data sets, the correlation number that is returned will range from -1 to +1. A -1 value means the two data sets move in the opposite direction at each data point. A value of +1 means the two data sets move in the same direction at each data point. I use a value of 0.40 as a significant positive correlation between two data streams.

Tables B.2 through B.9 show the correlation among all the commodities in each group.  They were generated using the Pearson correlation algorithm.

| TABLE B.2   | TABLE B.2   | Correlation among Grain Commodities   | Correlation among Grain Commodities   | Correlation among Grain Commodities   | Correlation among Grain Commodities   | Correlation among Grain Commodities   | Correlation among Grain Commodities   | Correlation among Grain Commodities   |
|-------------|-------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
| Grains      | Grains      | Grains                                | Grains                                | Grains                                | Grains                                | Grains                                | Grains                                | Grains                                |
| Commodity   | Corn        | Oats                                  | Soybeans                              | Soy Meal                              | Bean Oil                              | Wheat                                 | KC Wheat                              | Rough Rice                            |
| Corn        | 1           | 0.50                                  | 0.62                                  | 0.54                                  | 0.48                                  | 0.51                                  | 0.51                                  | 0.17                                  |
| Oats        | 0.50        | 1                                     | 0.40                                  | 0.37                                  | 0.29                                  | 0.42                                  | 0.41                                  | 0.15                                  |
| Soybeans    | 0.62        | 0.40                                  | 1                                     | 0.82                                  | 0.68                                  | 0.40                                  | 0.37                                  | 0.17                                  |
| Soy Meal    | 0.54        | 0.37                                  | 0.82                                  | 1                                     | 0.35                                  | 0.36                                  | 0.33                                  | 0.15                                  |
| Bean Oil    | 0.48        | 0.29                                  | 0.68                                  | 0.35                                  | 1                                     | 0.30                                  | 0.38                                  | 0.13                                  |
| Wheat       | 0.51        | 0.42                                  | 0.40                                  | 0.36                                  | 0.30                                  | 1                                     | 0.87                                  | 0.13                                  |
| KC Wheat    | 0.51        | 0.41                                  | 0.37                                  | 0.33                                  | 0.38                                  | 0.87                                  | 1                                     | 0.13                                  |
| Rough Rice  | 0.17        | 0.15                                  | 0.17                                  | 0.15                                  | 0.13                                  | 0.13                                  | 0.13                                  | 1                                     |

To use Table B.2, enter the first commodity you are interested in from the left of the table and move across the row until you hit the column that intersects with the second commodity you are interested in. For example, corn is correlated at a level of 1 with itself and 0.5 with oats. Looking over all the relationships, it is clear that all the members of the grain group are significantly correlated with one or more of the other commodities, with the  exception of rough rice, which isn't significantly correlated with any other grain group member.

TABLE B.3

Correlation among Meat Commodities

| Meats         | Meats       | Meats     | Meats         |
|---------------|-------------|-----------|---------------|
| Commodity     | Live Cattle | Lean Hogs | Feeder Cattle |
| Live Cattle   | 1           | 0.35      | 0.75          |
| Lean Hogs     | 0.35        | 1         | 0.32          |
| Feeder Cattle | 0.75        | 0.32      | 1             |

The cattle members (live cattle and feeder cattle) are significantly correlated with one another.  The cattle members and hogs are correlated at the 0.25 to 0.35 range with each other-not significant correlation, but on the threshold.

TABLE B.4

Correlation among Soft Commodities

| Softs        | Softs   | Softs   | Softs   | Softs   | Softs   | Softs        |
|--------------|---------|---------|---------|---------|---------|--------------|
| Commodity    | Coffee  | Cocoa   | Cotton  | Lumber  | Sugar   | Orange Juice |
| Coffee       | 1       | 0.11    | 0.01    | 0.02    | 0.05    | 0.03         |
| Cocoa        | 0.11    | 1       | 0.04    | 0.02    | 0.09    | 0.01         |
| Cotton       | 0.01    | 0.04    | 1       | 0.08    | 0.02    | 0.04         |
| Lumber       | 0.02    | 0.02    | 0.08    | 1       | 0.08    | 0.02         |
| Sugar        | 0.05    | 0.09    | 0.02    | 0.08    | 1       | 0.02         |
| Orange Juice | 0.03    | 0.01    | 0.04    | 0.02    | 0.02    | 1            |

None of the members of the softs group show a significant correlation with any other member. I treat them as totally independent of each other. I should note that the softs group is really a 'cats and dogs' group.  Things that don't readily fit in another group are lumped here. Clearly the fundamentals driving each of these commodities are very different, as are the areas that primarily produce them.

As shown in Table B.5, the precious or semi-precious metal members of this group (silver, gold, and platinum) are all highly correlated with each other. Palladium, which is an industrial white metal used primarily in catalytic  converter  production,  is  more  highly  correlated  with  the  precious metal group than the industrial metal members (copper and the London metals). All the industrial metals are highly correlated with each other.

UNDERSTANDING FUTURES

| London Nickel         | 0.31   | 0.05      | 0.09   | 0.08   | 0.06     | 0.40          | 0.35            | 0.45            | 1             |
|-----------------------|--------|-----------|--------|--------|----------|---------------|-----------------|-----------------|---------------|
| London Aluminum       | 0.51   | 0.16      | 0.12   | 0.13   | 0.17     | 0.52          | 0.75            | 1               | 0.45          |
| London Aluminum Alloy | 0.46   | 0.17      | 0.15   | 0.18   | 0.13     | 0.46          | 1               | 0.75            | 0.35          |
| London Copper         | 0.78   | 0.16      | 0.16   | 0.15   | 0.14     | 1             | 0.46            | 0.52            | 0.40          |
| Platinum              | 0.25   | 0.57      | 0.52   | 0.58   | 1        | 0.14          | 0.13            | 0.17            | 0.06          |
| Gold                  | 0.22   | 0.41      | 0.67   | 1      | 0.58     | 0.15          | 0.18            | 0.13            | 0.08          |
| Silver                | 0.23   | 0.39      | 1      | 0.67   | 0.52     | 0.16          | 0.15            | 0.12            | 0.09          |
| Palladium             | 0.21   | 1         | 0.39   | 0.41   | 0.57     | 0.16          | 0.17            | 0.16            | 0.05          |
| Copper                | 1      | 0.21      | 0.23   | 0.22   | 0.25     | 0.78          | 0.46            | 0.51            | 0.31          |
| Commodity             | Copper | Palladium | Silver | Gold   | Platinum | London Copper | London Aluminum | London Aluminum | London Nickel |

As shown in Table B.6, all the members of the energy group are significantly correlated with one or more of the other commodities of the group.

TABLE B.6

Correlation among Energy Commodities

| Energies     | Energies   | Energies    | Energies    | Energies     |
|--------------|------------|-------------|-------------|--------------|
| Commodity    | Crude Oil  | Natural Gas | Heating Oil | Unleaded Gas |
| Crude Oil    | 1          | 0.28        | 0.85        | 0.79         |
| Natural Gas  | 0.28       | 1           | 0.32        | 0.35         |
| Heating Oil  | 0.85       | 0.32        | 1           | 0.74         |
| Unleaded Gas | 0.79       | 0.35        | 0.74        | 1            |

All  the  major  currencies  (euro,  yen,  franc,  pound,  and  dollar)  are  all highly correlated with each other. The yen, franc, and pound tend to move up  and  down  together,  while  the  dollar  moves  in  the  opposite  direction of  those  three  (high  negative  correlation).  Note  that  the  dollar  and  euro have an almost perfect negative correlation, -0.97. The minor currencies (Canadian dollar, Australian dollar, and Mexican peso) are not highly correlated with the major currencies, nor are they highly correlated with each other. It is my experience that these three currencies are much harder to trade than the majors.

Table B.8 illustrates that all U.S. financials are highly correlated with each other, and the degree of correlation is highest with instruments closest in maturity length (30-year bond and 10-year note, 10-year note and 5-year note,  etc.). All  U.S.  financials  are  also  highly  correlated  with  the  foreign financials, but the degree of correlation is less than within the U.S. financial group. Likewise, all foreign financials are highly correlated with each other, and the highest correlation occurs within instruments from the same region (Spanish bond, Euro bund, and Long gilt, which are all European instruments).

The U.S. stock indices are highly correlated to all members of that group, and significantly correlated with the Nikkei (Table B.9).

UNDERSTANDING FUTURES

Correlation among Currency Commodities

TABLE B.7

| Euro Currency     | 0.38         | 0.91        | 0.13            | 0.63          | -0.97        | -0.16        | 0.19       | 1                    |
|-------------------|--------------|-------------|-----------------|---------------|--------------|--------------|------------|----------------------|
| Australian Dollar | 0.09         | 0.12        | 0.31            | 0.20          | -0.18        | 0.01         | 1          | 0.19                 |
| Mexican Peso      | -0.14        | -0.20       | 0.02            | -0.07         | 0.12         | 1            | 0.01       | -0.16                |
| Dollar Index      | -0.57        | -0.91       | -0.14           | -0.73         | 1            | 0.12         | -0.18      | -0.97                |
| British Pound     | 0.41         | 0.65        | 0.20            | 1             | -0.73        | -0.07        | 0.20       | 0.63                 |
| Canadian Dollar   | 0.15         | 0.16        | 1               | 0.20          | -0.14        | 0.02         | 0.31       | 0.13                 |
| Swiss Franc       | 0.54         | 1           | 0.16            | 0.65          | -0.91        | -0.20        | 0.12       | 0.91                 |
| Japanese Yen      | 1            | 0.54        | 0.15            | 0.41          | -0.57        | -0.14        | 0.09       | 0.38                 |
| Commodity         | Japanese Yen | Swiss Franc | Canadian Dollar | British Pound | Dollar Index | Mexican Peso | Australian | Dollar Euro-Currency |

TABLE B.8 Correlation among Financial Commodities

| Long Gilt       | 0.48         | 0.46         | 0.49        | 0.49        | 0.34       | 0.35            | 0.74      | 0.70         | 1         |
|-----------------|--------------|--------------|-------------|-------------|------------|-----------------|-----------|--------------|-----------|
| Spanish Bond    | 0.53         | 0.51         | 0.48        | 0.43        | 0.33       | 0.46            | 0.77      | 1            | 0.70      |
| Euro Bund       | 0.61         | 0.62         | 0.60        | 0.56        | 0.46       | 0.45            | 1         | 0.77         | 0.74      |
| Australian Bond | 0.44         | 0.46         | 0.52        | 0.55        | 0.39       | 1               | 0.45      | 0.46         | 0.35      |
| Eurodollar      | 0.71         | 0.77         | 0.83        | 0.88        | 1          | 0.39            | 0.46      | 0.33         | 0.34      |
| 2-Year Note     | 0.76         | 0.88         | 0.94        | 1           | 0.88       | 0.55            | 0.56      | 0.43         | 0.49      |
| 5-Year Note     | 0.87         | 0.96         | 1           | 0.94        | 0.83       | 0.52            | 0.60      | 0.48         | 0.49      |
| 10-Year Note    | 0.95         | 1            | 0.96        | 0.88        | 0.77       | 0.46            | 0.62      | 0.51         | 0.46      |
| 30-Year Bond    | 1            | 0.95         | 0.87        | 0.76        | 0.71       | 0.44            | 0.61      | 0.53         | 0.48      |
| Commodity       | 30-Year Bond | 10-Year Note | 5-Year Note | 2-Year Note | Eurodollar | Australian Bond | Euro Bund | Spanish Bond | Long Gilt |

UNDERSTANDING FUTURES

Stock Indices

| Commodity    |   S&P 500 |   Nasdaq 100 |   Russell 2000 |   Midcap 400 |   Nikkei |
|--------------|-----------|--------------|----------------|--------------|----------|
| S&P 500      |         1 |         0.81 |           0.79 |         0.85 |     0.39 |
| Nasdaq 100   |      0.81 |            1 |           0.78 |         0.77 |     0.44 |
| Russell 2000 |      0.79 |         0.78 |              1 |         0.92 |     0.36 |
| Midcap 400   |      0.85 |         0.77 |           0.92 |            1 |     0.35 |
| Nikkei       |      0.39 |         0.44 |           0.36 |         0.35 |        1 |

## ■ Margin

A major difference between commodity trading and equity trading is the leverage involved.  When executing a commodity trade, you do not have to pay the full value of the contract.  Y ou only have to have sufficient funds in your account to meet the exchange's current margin requirements for the contract. If for example, corn is currently trading at $3 a bushel, the value of the contract is $15,000. The exchange may have a current margin requirement of $500 to control the contract.  With an account equity of $1,000 you could buy or sell two contracts under those margin requirements. In that case you would be fully margined, a dangerous position to be in. If the price moved against your position by even a penny, you would face a margin call. In that case you would have to either liquidate some or all of your position, or add funds to meet the margin call.

To illustrate the leverage involved, suppose you went long two contracts with the $1,000 in your account and the price of corn moved up $0.10 from $3.00 to $3.10.  That's only a 3.33 percent increase in price, but it is an open equity profit  of  $500  per  contract.  On  the  two  contracts,  you  would  be ahead $1,000, or 100 percent on your account equity. In equity trading, you can usually only margin at a max of twice the amount in your account.  With the same $2,000 in your equity account, you would be fully margined if you bought 200 shares of a stock trading at $10 per share. If the price of the equity went up 3.33 percent, it would now be trading at $10.33 per share. Your 200 shares would be worth $2,066.66 and you would be ahead $66.66 on your $1,000 equity, or 6.67 percent. The leverage of the fully margined corn trade is about 15 times larger than the fully leveraged stock trade.

It is dangerous to trade commodities fully leveraged. If price moves rapidly against your positions, you can lose more than you have in your account. In the case of the fully leveraged corn trade, a move of $0.15 against your position (a relatively small move in corn) would cause an open equity decrease of $750 per contract in your account. Holding two contracts, your original $1,000 account would now be debit $500.

Most experienced commodity traders don't even consider margin requirements when trading. Their money management considers risk from a draw-down probability standpoint, and they leverage to experience drawdowns within their personal risk tolerance, not to margin requirements. Most traders have a tough time trading through 20 percent draw-downs so they build a trading plan that keeps them inside their comfort zone. Margin requirements are no help because they are a lagging indicator of risk. The exchanges react after the fact to price moves or volatility with margin requirement changes. If a commodity experiences increased volatility, they will move margin requirements higher, but as a trader it's too late: You've already experienced the increased volatility at the reduced margin levels.

## ■ Electronic Contracts

Futures were traded in pits from the start of domestic commodity trading until the last decade. The plot of the movie Trading Places revolves around orange juice futures, and the pit is prominently shown. As technology advanced electronic trading started, most notably in the S&amp;P futures. Now almost all trading is done electronically.

A typical electronically traded contract operates much of the weekday with short down periods. For example, the yen traded on the Chicago Mercantile Exchange (CME) trades electronically from 5 PM EST to 4 PM EST . That contract still has a pit which trades from 8:20 AM EST to 3 PM EST .

The trader should be careful when trading electronic contracts during the night and early morning. Volume drops off dramatically from the peak daytime hours. A practice I use for market orders based on the close is to enter the order when the pit session opens, if the commodity still has a pit, or when the old daytime pit session opened. In the case of the yen, I'd place a market order at 8:20 AM EST .

## Understanding Continuous Contracts

I f you're conducting an analysis using stock or commodity data, you need to account for real-trading data disruptions. In commodities, that means the trading transactions that occur when the front-month contract you're trading nears its last day of trading, and you exit that contract and enter a position in the new lead contract. For stocks, it means the change that happens to the data stream due to splits and dividends.  This appendix shows how continuous contracts can be constructed and used so that hypothetical testing on the contract provide the same results as real-time trading across these disruptions.

## ■ Properly Accounting for Stock Splits and Dividends

Most stock data vendors offer a choice of data formats that includes the actual historical stock prices for each day (raw data), a price stream that is

+                (        +                   ,     ( #         &amp;    -       #. &amp;     +   " &amp;     +   "     #$      %                            ! "

adjusted for stock splits (split-adjusted), and a price stream that is adjusted for the dividends the company has paid over time (dividend-adjusted). All the information in these historical price streams is required to correctly determine the change in any given equity over a period of time. Unfortunately, each of these price streams alone will yield incorrect results if a dividend or stock split has occurred after the date of the calculations.

## Problems with the Actual-Price File

To illustrate, we'll use the IBM price stream as an example. On May 5, 1999, IBM had a two-for-one stock split. On the close of trading for that day the price of IBM was $236.25. IBM issued two shares for every one outstanding and adjusted the price to $118.125. The dollar value of each shareholder's stock remained the same, because each shareholder now owned double the number of shares at half the pre-split price.  Table C.1 shows the actual-price data file for IBM following closes around the time of the split.

| TABLE C.1   | Actual Prices for IBM around Split Time   |
|-------------|-------------------------------------------|
| Date        | Close                                     |
| 5/24/1999   | 223.75                                    |
| 5/25/1999   | 221.1875                                  |
| 5/26/1999   | 236.25                                    |
| 5/27/1999   | 116                                       |
| 5/28/1999   | 116                                       |
| 6/1/1999    | 112                                       |

If you used the actual-price data file for analysis, and you entered a long trade on the close of May 24, 1999, and exited the trade on the close of June 1, 1999, your trade would have lost about 112 points, or 50 percent. In reality, the two shares of stock after the split would have been worth $224 on June 1, 1999, and you would have actually made a marginal amount on the trade.  Looking  at  this  example,  you  might  think  the  only  problem  with the actual-price data stream occurs across splits. There is another problem: The  actual-price  data  stream  yields  incorrect  results  because  it  doesn't account for dividend payouts.

To  illustrate,  IBM  issued  an  $0.18  per  share  dividend  on  February  7, 2005. Table C.2 shows the actual-price data file around this time.

<!-- image -->

| Date     |   Close |
|----------|---------|
| 2/4/2005 |   94.51 |
| 2/7/2005 |   94.53 |
| 2/8/2005 |   94.13 |
| 2/9/2005 |    92.7 |

If  you  used  this  data  stream  and  entered  a  long  trade  on  the  close  of February 7, 2005, and exited on the close of February 8, 2005, you would show a loss of $0.40 per share. Due to the $0.18 dividend, you really would have lost only $0.22 per share.

Using the actual-price data stream, one can rationalize that if you eliminate bad trades around splits, you will get fairly accurate results because the effect of the dividends is small. This may be true for some analyses, but for some studies the effect of dividends is crucial. From 1980 to March 2005, the total IBM dividend payout was $64.32. During that time IBM appreciated a total of 238.8 points across two stock splits. Ignoring dividends, IBM grew 383 percent since 1980.  When dividends are included, the actual growth was 473 percent, a significant difference.

## Problems with the Split-Adjusted File

Using the split-adjusted data stream for analysis causes similar problems. The  breakout  in Table  C.3  shows  the  actual-price  closes  and  the  splitadjusted closes for a few days surrounding IBM's last split.

TABLE C.3 Actual and Split-Adjusted Prices for IBM around Split Time

| Date      |   Actual-Price Close |   Article I. Split-Adjusted Close |
|-----------|----------------------|-----------------------------------|
| 5/24/1999 |               223.75 |                           111.875 |
| 5/25/1999 |             221.1875 |                         110.59375 |
| 5/26/1999 |               236.25 |                           118.125 |
| 5/27/1999 |                  116 |                               116 |
| 5/28/1999 |                  116 |                               116 |
| 6/1/1999  |                  112 |                               112 |

The split-adjusted data stream is formed by dividing the actual price level by the split value, in this case by two and before May 26, 1999. One other stock split has occurred in IBM since 1980, and that was in 1996. On that two-for-one split, the actual-price values on the split day, and earlier, would be divided by four.  The problem with using split-adjusted data is the fact that day-to-day price changes and daily ranges are divided by the split value.  The actual change in price from May 25, 1999, until the close of the next trading day is a little more than 15 points, but the split-adjusted data only reflects about 7.5 points.

This can cause a number of analysis problems. If you are using any form of volatility- or range-based system, the values artificially change from split to split. Furthermore, trades will change. If IBM were to split two-for-one again, the split-adjusted change from May 26, 1999, until May 27, 1999, would change from about 7.5 to about 3.75.

The split-adjusted price stream also shares a problem in common with the actual-price data stream:  The changes due to dividends are not included.

## Problems with the Dividend-Adjusted File

The dividend-adjusted file is formed by going back in time and subtracting the  cumulative  dividends  paid  from  the  actual-price  data. The  breakout  in Table C.4 shows the actual-price closes and the dividend-adjusted closes across the latest dividend distribution, the $0.18 dividend on February 7, 2005.

| TABLE C.4   | Actual and Dividend-Adjusted Prices for IBM around Dividend Time   | Actual and Dividend-Adjusted Prices for IBM around Dividend Time   |
|-------------|--------------------------------------------------------------------|--------------------------------------------------------------------|
| Date        | Actual-Price Close                                                 | Dividend-Adjusted Close                                            |
| 2/4/2005    | 94.51                                                              | 94.33                                                              |
| 2/7/2005    | 94.53                                                              | 94.35                                                              |
| 2/8/2005    | 94.13                                                              | 94.13                                                              |
| 2/9/2005    | 92.7                                                               | 92.7                                                               |

Using  the  dividend-adjusted  file,  the  correct  daily  change  of  $0.22  is shown from February 7, 2005, until February 8, 2005. The problem with using this file is the fact that, as we go back in time, the prices get further and further away from the actual prices. On January 2, 1980, the dividendadjusted close was -2.828, while the actual IBM price on that date was 62.5.

## Stock Data Problem Summary

None of the price streams accurately reflect what really occurred over time. It's clear that actual prices must be involved, as well as the split and dividend information. But there isn't a price stream available that provides all the information required.

## The Solution

There is a simple solution to the problem. The three data streams can be manipulated to yield a price stream that accurately reflects what happened across any period of time. Following are the steps used in the algorithm:

1.  The  actual-price  data  and  the  split-adjusted  data  are  used  to  find  the multiplying factor for each day due to splits. Each day the split-adjusted close is divided into the actual close to determine the multiplying factor. Going back in time, the factor will be 1 until the first split.  Then it will change according to the split (2-1, 3-1, 1-3, etc.). At each split the multiplying factor will change.
2.  Use the actual-price data and the dividend-adjusted data to determine the cumulative amount of dividends taken out over time. Each day the dividend-adjusted close is subtracted from the actual-price close to determine the cumulative dividends paid put from that date forward.
3.  Construct  a  back-adjusted  continuous  contract  by  multiplying  the actual-price data each day by the factor for that day, and subtract the accumulated dividends for that date.
4.  Write out the date, open, high, low , and close of the back-adjusted contract, and add a final field: the actual closing price that day.

Table C.5 shows the first and last line of the continuous contract for IBM.

| TABLE C.5   | Continuous Contract Data for Actual Prices for IBM   | Continuous Contract Data for Actual Prices for IBM   | Continuous Contract Data for Actual Prices for IBM   | Continuous Contract Data for Actual Prices for IBM   |              |
|-------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|--------------|
| Date        | Open                                                 | High                                                 | Low                                                  | Close                                                | Actual Close |
| 1/2/1980    | -210.0938                                            | -208.5938                                            | -210.5938                                            | -210.5938                                            | 62.5         |
| 3/14/2005   | 93.79                                                | 94.04                                                | 92.5                                                 | 93.04                                                | 93.04        |

This data stream accurately reflects the appreciation of IBM over the 25year period. The difference between the close on March 14, 2005, and the close on January 2, 1980 is about 303 points, the sum of the 238-point price appreciation across splits, and the $64 in dividends paid out over the years.

Note that this data file contains all the information needed to compute accurate changes in both points, and in percent. Each daily change is identical to the actual change that occurred over time so point changes are accurate. When that total is divided by the actual price the accurate percentage change over the time frame can be determined. Table C.6 shows a few days of  the  continuous contract and the actual-price data. Note how the daily price changes are the same in both data streams.

TABLE C.6

## Continuous Contract Changes Match Actual-Price Changes

| Date      |   Continuous Contract Close |   Actual-Price Close | Price Change   |
|-----------|-----------------------------|----------------------|----------------|
| 8/7/1997  |                     -15.671 |              107.375 | N/A            |
| 8/8/1997  |                     -17.796 |               105.25 | -2.125         |
| 8/11/1997 |                     -20.046 |                103.0 | -2.25          |
| 8/12/1997 |                    -19.6085 |             103.4375 | +0.4375        |
| 8/13/1997 |                     -18.671 |              104.375 | +0.9375        |

The day-to-day price changes of both the continuous contract and the actual-price contract are identical, so the continuous contract reflects the historical change in points accurately. T o determine the percentage change over any period of time, the point change is found using the continuous price data, and then the percentage change is found by dividing by the actual price, which is the last entry on each continuous contract data line.

Note that intraday changes can also be accurately determined. Table C.7 shows data from a fictional day on the continuous contract.

| TABLE C.7   | Fictional Continuous Contract Day of Data   | Fictional Continuous Contract Day of Data   | Fictional Continuous Contract Day of Data   | Fictional Continuous Contract Day of Data   |              |
|-------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|--------------|
| Date        | Open                                        | High                                        | Low                                         | Close                                       | Actual Close |
| xx/xx/xxxx  | -10                                         | -5                                          | -12                                         | -8                                          | 60           |

Let's assume that your strategy entered a long trade at -6 on the continuous contract. The actual-price entry can be determined using the known relationship  between  the  continuous  contract  close  and  the  actual-price close. The actual-price close is 68 points higher than the continuous contract close, so the trade entry at -6 on the continuous contract occurred at an actual price of $62.

Notice that until the first split or dividend, the actual-price open, high, low, and close will be identical to the corresponding continuous contract data.

## The Difference the Right Data Makes

To illustrate the difference the data stream makes, we will look at a trading strategy on IBM using the continuous contract, the actual-price contract, the split-adjusted contract, and the dividend-adjusted contract. The following rules were used for the trading strategy:

- ■ Buy at the close if the close is below the 10-day moving average of the close.  Place  a  profit  stop  15  percent  above  the  entry,  and  a  stop  loss 15 percent below the entry.

- ■ Exit the trade if price closes above the 10-day moving average of price, and the trade has lasted at least 20 trading days.
- ■ Exit the trade if the stop loss is exceeded on a closing basis.
- ■ Exit the trade if the profit stop is exceeded on a closing basis.

Table C.8 shows trading results on the four data streams.

| TABLE C.8    | Trade Statistics on Continuous, Actual-Price, Split-Adjusted, and Dividend-Adjusted Data   | Trade Statistics on Continuous, Actual-Price, Split-Adjusted, and Dividend-Adjusted Data   | Trade Statistics on Continuous, Actual-Price, Split-Adjusted, and Dividend-Adjusted Data   | Trade Statistics on Continuous, Actual-Price, Split-Adjusted, and Dividend-Adjusted Data   |
|--------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Contract     | Winning Trades                                                                             | Losing Trades                                                                              | Points of Profit                                                                           | Percentage Points of Profit                                                                |
| Continuous   | 120                                                                                        | 96                                                                                         | 195.1                                                                                      | 249.1                                                                                      |
| Actual-Price | 119                                                                                        | 99                                                                                         | -60.7                                                                                      | 100.2                                                                                      |
| Split        | 120                                                                                        | 97                                                                                         | 28.6                                                                                       | 208.6                                                                                      |
| Dividend     | 173                                                                                        | 184                                                                                        | -103.2                                                                                     | -906.3                                                                                     |

Though the number of winning trades and losing trades for the actualprice and split-adjusted contracts are close to the actuals over the 25-year time frame, there is a big disparity in both the total number of points of profit and the total number of percentage points of profit.

Regarding  the  dividend-adjusted  results,  the  winning  system  actually looks like a loser. In the case of percentage points, the dividend-adjusted file goes back to around zero on January 2, 1980. Small daily changes divided by the small numbers yield very large percentage winners and losers. The net effect is a result badly skewed by these trades.  The reason the points of profit are so far off has to do with the stops and profit stops. Taking 15 percent of a small number leaves an even smaller number. These stops and profit stops were hit much more often than actually would have happened and the total result does not reflect the real trading.

The continuous contract not only reflects reality, it yields better results than the same system on the other price streams.  This will almost always be the case with a successful system because the continuous contract has more range  over  the  data  stream  than  the  other  contracts.  In  essence,  there  is more profit to be gotten.

## Stock Continuous Contract Summary

If  you develop stock strategies on data streams that go back more than a few years, your results are inaccurate, and they may be very inaccurate. If you had used a data stream that included properly adjusted prices using the actual price, splits,  and  dividends,  your  results  would  reflect  actual  trading and would most likely be better than the hypothetical results generated by the other price streams. Kind of makes you wonder if you passed on a holy grail system because the data problem dropped performance into the marginal zone.

## ■ Properly Accounting for Commodity Contract Rollover

It is much easier to account for trading disruptions with commodities. The only adjustment that has to be made is for rollover from the current contract to the next one as the current contract nears expiration.  The way this is done is to form an artificial data stream that pieces the contracts together. At the close on the day that the roll from one contract to the next is accomplished, the difference between the new contract close and the old contract close is added to all the previous data points (open, high, low , and close).  This backadjustment raises or lowers all the previous data so that the prices don't match the historical contract prices, but the correct relationship between open, high, low, and close is maintained, as is the difference in closing prices from day to day.

Almost  all  data  providers  offer  these  continuous  contracts,  and  some provide the ability for the user to select the criteria for rolling from the current lead contract to the next. The most common criterion is when the open interest in the next lead exceeds the open interest in the current lead. Different roll criteria will lead to data streams that differ slightly, but they're all valid streams.

## More Curve-Fitting Examples

M ost of the time, curve-fitting is due to not having enough data in the development sample. This leads to a small sample of trades, which doesn't come close to representing the infinite sample. But there are times when  curve-fitting  sneaks  unnoticed  into  your  work. This  appendix  will highlight  some  cases. The  point  of  these  examples  is  that  curve-fitting  is costly. If you don't realize your strategy is curve-fit, you can lose many thousands of dollars trading it before you either figure out what the problem was or quit the trading, never knowing why your holy grail failed.

## ■ Case 1: Stock Pairs Trading

I wanted to see if I could develop a stock strategy that traded a pair of correlated stocks.  When the normally correlated pair started to diverge in price, I' d sell the one going up and buy the one going down, and then wait until they got in sync again and exit with a profit.  The advantages of a strategy like this are that the risk should be relatively small, and you're evenly exposed on both the long and short side, so market ups and downs would have a minimal impact.

I  took  my  liquid  basket  of  stocks  and  correlated  each  one  with  every other one, and those that averaged a correlation coefficient of greater than 0.4 over the lifetime of the pair went into my development basket. With a liquid basket of about 1,300 liquid stocks, I found about 300 pairs for my development basket.

I then developed a strategy around the 300 pairs and things looked good. But when I went to trade the developed strategy, results were disappointing. I didn't know if it was market conditions or just a bad time for the strategy. It turns out I had introduced a major degree of curve-fitting into the process.

When I did the correlations, I used all the data to determine if the stocks were correlated. That was wrong. Many of the stocks met the correlation conditions up to a certain point, then stopped, or stopped for a while and then met the conditions again. I should have used every pair that met the average correlation number of 0.4 during the time it was correlated. Those pairs that met the correlation condition at some time during their lifetime, but not at the end of the entire period of the data sample, would have degraded the trading strategy, because at the point they lost correlation they wandered independently and I was trading them as if they'd revert back to normal. Those trades would have been mostly losers.

When I went back and redeveloped, including every pair that met the correlation  condition  during  their  lifetime,  the  strategy  was  no  longer tradeable.

The moral of this story is that when you use information based on data that hasn't occurred in time yet, you are introducing a degree of curve-fitting. That can be okay if the curve-fitting is minimal.  That's exactly the case with the bar-scoring technique introduced in this book. But if you do that, you need to do a Build, Rebuild, and Repair (BRAC) test to determine how much impact the curve-fitting has on your solution.

## ■ Case 2: Using Limit Orders on Daily-Bar Stock Data

I  developed a long-only stock system that entered on limit orders placed before the market opened. I'd place anywhere from 50 to 200 orders, but I only wanted to keep 20. I had software that would cancel the other orders when I hit 20, so the only problem was when more than 20 hit on the open.

When that happened, I'd manually close the excess by taking those with the biggest profit or smallest loss in the first few minutes of trading. In my back-tests, I'd keep everything that hit the limit on the open, and for the rest, if any, I' d randomly select the number needed from all those that filled after the open.  The hypothetical performance numbers were astronomical.

When I started to trade, results diverged almost immediately from the hypotheticals  over  the  traded  time  frame.  I  tracked  down  the  following problems:

- ■ My real trading didn't get all the trades that my hypotheticals said I should get on the open, even when price clearly traded below the limit order entry price. I got about 8 out of 10, but these trades were historically better than those that filled later in the day, so missing any hurt overall performance. Also, I got slippage in real time that I didn't account for in the hypotheticals. If the limit order was 100, and the stock opened at 99, my hypotheticals would give me the 99, but in reality I'd sometimes get the 99, but mostly I'd get somewhere between 99 and 100.
- ■ Randomly picking the trades that filled after the open was too optimistic. I got way more bad ones than good in real time.  Those stocks run through the limit order and keep heading south. The ones that trade through the limit and recover, you might not get.

Those issues made the strategy only so-so.  This example is typical of limit order systems; you really never know how much worse than expected it's going to be.

## ■ Case 3: Bar-Scoring Using Profit-per-Trade

As introduced in this book, bar-scoring allows you to use any user-defined criterion you want. I thought I'd check out using the past profitability over the last n trades as a bar-scoring criterion. Suppose n was the last 10 trades. At every bar, I' d look back over the last 10 trades in that stock and assign the average profitability of those trades to the bar. When I added that criterion to the four or five I was already using, the average profitability of the top scoring trades jumped way up. I was suspicious of the results and started looking for where I could be curve-fitting. It turns out that if you use every bar for a trade and your trades last two or more days, some of your last 10 trades are still not closed out. I was keeping the profit each day for the trades  that  hadn't  closed  out  and  these  numbers  were  being  used  in  the scoring matrices.  They skewed the whole matrix to predict what would happen with that trade. But since the trade was already in, profit or loss information was being introduced when it shouldn't have. I fixed the problem by only using closed trades, and the profit-per-trade criterion turned out to be only marginal.

## ■ Conclusion

There are lots of ways to curve-fit. Most of the time it's because you don't have enough trades in your development sample. A BRAC test will uncover that problem. Other times curve-fitting can be very subtle.  The bottom line is that if results get dramatically better when you do something, closely examine what you just did.

## I N D E X

| A                                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Acceleration factor, usage, 80                                                                                                                                         |
| Accounts equity, range, 204 small-account performance metrics, 183-184                                                                                                 |
| Account size contrast, 183-189 gaps, advantages, 220 smallness, impact, 28 Actual-price changes, continuous contract                                                   |
| changes (comparison), 270 Actual-price data file, usage, 266 usage, 269 Actual-price file, problems, 266-267                                                           |
| ADX. See Average Directional Movement Index Always-in-the-market system, reversal signal exit (occurrence), 66 Annualized return, 62 trading days, average number, 146 |
| Annual percent return, 188-189                                                                                                                                         |
| Annual return. See Commodity strategy; Full-size portfolio; Mid-size draw-down, comparison, 111t                                                                       |
| increase, 68 starter portfolio, 202f                                                                                                                                   |
| portfolio                                                                                                                                                              |
| Annual return/max draw-down commodity strategy, 85t                                                                                                                    |
| stock strategy, 74t                                                                                                                                                    |
| stock system, 94t                                                                                                                                                      |

| Artificial data, 161-164 Monte Carlo practice, 162 Augmented portfolio, top tier commodities (one-lot/two-lot contrast), 196t Auto-trading software, usage, 28 Average annual profit, division, 217                                                                                                                                                                 | 277   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| Average annual return decrease, 75 max draw-down, contrast, 5, 93, 101 Average Directional Movement Index (ADX) logic, coding, 172 value, excess (days percentage), 173t Average max draw-down decrease, 68 increase, 75 Average profit-per-trade, problems, 68 Average range, 246-247 Average range catastrophic stop, 79t Average start-trade draw-down, 204, 208 |       |

## B

Back-adjusted continuous contract,

construction, 269

Back-test.

See

Tradeable strategy

impediment, 24-29

Bar gaps

analysis, 142

breakouts, contrast, 141

commodities, 142-143

+                (        +                   ,     ( #         &amp;    -       #. &amp;     +   " &amp;     +   "     #$      %                            ! "

| Bar gaps ( continued ) congestion, absence, 143t congestion absence, 141t, 143t commodities, 142-143 NASDAQ stocks, 141t NASDAQ stocks, 142t congestion, absence, 141t stocks, 140-142 Bars. See Daily bars; Intra-day bars data, comparison, 54t, 55t, 56t dual order assumption, 24 component, 25-26 number, push/persistence (proportion), 47f   | Breakout systems, buy/sell stop placement, 25 Brokerage firms, leverage (allowance), 216 Brute force, results. See Optimal F Build, Rebuild, and Compare (BRAC) strategy , example, 20-23 out-of-sample testing, contrast, 23-24 Build, Rebuild, and Compare (BRAC) test, success, 23 Buy-and-hold, FX pairs (contrast), 37 Buy-and-hold average profit-per-day, 41 Buy-and-hold performance. See Baseline buy- and-hold performance Buy-and-hold profit-per-trade, average, 34, 36 Buy and hold strategy, buy Dogs of the Dow strategy (contrast), 170t   | Breakout systems, buy/sell stop placement, 25 Brokerage firms, leverage (allowance), 216 Brute force, results. See Optimal F Build, Rebuild, and Compare (BRAC) strategy , example, 20-23 out-of-sample testing, contrast, 23-24 Build, Rebuild, and Compare (BRAC) test, success, 23 Buy-and-hold, FX pairs (contrast), 37 Buy-and-hold average profit-per-day, 41 Buy-and-hold performance. See Baseline buy- and-hold performance Buy-and-hold profit-per-trade, average, 34, 36 Buy and hold strategy, buy Dogs of the Dow strategy (contrast), 170t   | Breakout systems, buy/sell stop placement, 25 Brokerage firms, leverage (allowance), 216 Brute force, results. See Optimal F Build, Rebuild, and Compare (BRAC) strategy , example, 20-23 out-of-sample testing, contrast, 23-24 Build, Rebuild, and Compare (BRAC) test, success, 23 Buy-and-hold, FX pairs (contrast), 37 Buy-and-hold average profit-per-day, 41 Buy-and-hold performance. See Baseline buy- and-hold performance Buy-and-hold profit-per-trade, average, 34, 36 Buy and hold strategy, buy Dogs of the Dow strategy (contrast), 170t   | Breakout systems, buy/sell stop placement, 25 Brokerage firms, leverage (allowance), 216 Brute force, results. See Optimal F Build, Rebuild, and Compare (BRAC) strategy , example, 20-23 out-of-sample testing, contrast, 23-24 Build, Rebuild, and Compare (BRAC) test, success, 23 Buy-and-hold, FX pairs (contrast), 37 Buy-and-hold average profit-per-day, 41 Buy-and-hold performance. See Baseline buy- and-hold performance Buy-and-hold profit-per-trade, average, 34, 36 Buy and hold strategy, buy Dogs of the Dow strategy (contrast), 170t   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bar-scoring, 119                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| example, 122f                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     | 19                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 19                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 19                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 19                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 122f                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| type, scoring,                                                                                                                                                                                                                                                                                                                                      | Buy stop, placement, 25                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Buy stop, placement, 25                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Buy stop, placement, 25                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Buy stop, placement, 25                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| usage, 25                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| bar type                                                                                                                                                                                                                                                                                                                                            | C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| criterion, 122-123                                                                                                                                                                                                                                                                                                                                  | Calmar ratio, 168                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Calmar ratio, 168                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Calmar ratio, 168                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Calmar ratio, 168                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                     | Catastrophic dollar stop, commodity                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Catastrophic dollar stop, commodity                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Catastrophic dollar stop, commodity                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Catastrophic dollar stop, commodity                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| closing prices, standard deviation, 124t                                                                                                                                                                                                                                                                                                            | system, 77t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | system, 77t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | system, 77t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | system, 77t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| criteria, 127                                                                                                                                                                                                                                                                                                                                       | Catastrophic stop level, long-only stock                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Catastrophic stop level, long-only stock                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Catastrophic stop level, long-only stock                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Catastrophic stop level, long-only stock                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| curve-fitting, examination, 131                                                                                                                                                                                                                                                                                                                     | results (contrast)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | results (contrast)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | results (contrast)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | results (contrast)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| defined criteria, stock system (example),                                                                                                                                                                                                                                                                                                           | exit intra-day, 70t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | exit intra-day, 70t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | exit intra-day, 70t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | exit intra-day, 70t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 126-131                                                                                                                                                                                                                                                                                                                                             | exit on close, 70t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | exit on close, 70t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | exit on close, 70t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | exit on close, 70t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| examples, 122-126                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| stocks/commodities data, 123t                                                                                                                                                                                                                                                                                                                       | next day exit, 69t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | next day exit, 69t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | next day exit, 69t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | next day exit, 69t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| introduction, 120-121                                                                                                                                                                                                                                                                                                                               | Catastrophic stops, 76-79 addition. See Commodities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Catastrophic stops, 76-79 addition. See Commodities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Catastrophic stops, 76-79 addition. See Commodities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Catastrophic stops, 76-79 addition. See Commodities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| matrix, criteria, 129t                                                                                                                                                                                                                                                                                                                              | average range, 79t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | average range, 79t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | average range, 79t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | average range, 79t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| NASDAQ stocks, RSI/3-day return, 120t                                                                                                                                                                                                                                                                                                               | dollar stop, testing, 77                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | dollar stop, testing, 77                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | dollar stop, testing, 77                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | dollar stop, testing, 77                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| profit-per-trade, usage, 275-276                                                                                                                                                                                                                                                                                                                    | risk-avoidance measure, 71-72                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | risk-avoidance measure, 71-72                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | risk-avoidance measure, 71-72                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | risk-avoidance measure, 71-72                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| shortcoming, 120                                                                                                                                                                                                                                                                                                                                    | trigger, 70                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | trigger, 70                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | trigger, 70                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | trigger, 70                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| standard deviation number, 125                                                                                                                                                                                                                                                                                                                      | usage. See Swiss Franc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | usage. See Swiss Franc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | usage. See Swiss Franc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | usage. See Swiss Franc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| stock system, defined criteria (example),                                                                                                                                                                                                                                                                                                           | value, variation, 20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | value, variation, 20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | value, variation, 20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | value, variation, 20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 126-131                                                                                                                                                                                                                                                                                                                                             | Chart paradigm, 24                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Chart paradigm, 24                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Chart paradigm, 24                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Chart paradigm, 24                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| system                                                                                                                                                                                                                                                                                                                                              | Chicago Mercantile Exchange (CME), exchange                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Chicago Mercantile Exchange (CME), exchange                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Chicago Mercantile Exchange (CME), exchange                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Chicago Mercantile Exchange (CME), exchange                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| annual performance, 130t                                                                                                                                                                                                                                                                                                                            | trades, 263                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | trades, 263                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | trades, 263                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | trades, 263                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| performance, 130t                                                                                                                                                                                                                                                                                                                                   | Closed-trade draw-down, 184-185                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Closed-trade draw-down, 184-185                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Closed-trade draw-down, 184-185                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Closed-trade draw-down, 184-185                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Baseline buy-and-hold performance,                                                                                                                                                                                                                                                                                                                  | Closed-trade equity curve. See Donchian                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Closed-trade equity curve. See Donchian                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Closed-trade equity curve. See Donchian                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Closed-trade equity curve. See Donchian                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| determination, 32                                                                                                                                                                                                                                                                                                                                   | system; Full-size portfolio; Mid-size                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | system; Full-size portfolio; Mid-size                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | system; Full-size portfolio; Mid-size                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | system; Full-size portfolio; Mid-size                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Baseline Donchian stock strategy, 72                                                                                                                                                                                                                                                                                                                | portfolio                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | portfolio                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | portfolio                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | portfolio                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Baseline leverage, increase, 243t                                                                                                                                                                                                                                                                                                                   | commodity strategy, 228f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | commodity strategy, 228f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | commodity strategy, 228f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | commodity strategy, 228f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Baseline portfolio, 196                                                                                                                                                                                                                                                                                                                             | correspondence, 185                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | correspondence, 185                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | correspondence, 185                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | correspondence, 185                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Bookkeeping, 241-242                                                                                                                                                                                                                                                                                                                                | starter portfolio, 202f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | starter portfolio, 202f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | starter portfolio, 202f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | starter portfolio, 202f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Breakouts. See Standard deviation                                                                                                                                                                                                                                                                                                                   | Closed-trade equity growth,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Closed-trade equity growth,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Closed-trade equity growth,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Closed-trade equity growth,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     | 184f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 184f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 184f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 184f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| marker, 143                                                                                                                                                                                                                                                                                                                                         | open-trade performance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | open-trade performance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | open-trade performance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | open-trade performance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| metals/foreign stock indices,                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     | (comparison), 213t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | (comparison), 213t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | (comparison), 213t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | (comparison), 213t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 78                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     | metrics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | metrics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | metrics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | metrics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                     | performance metrics,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | performance metrics,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | performance metrics,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | performance metrics,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| entries, 52                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     | Closed-trade                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Closed-trade                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Closed-trade                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Closed-trade                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

| Closing prices, standard deviation, 124t            | portfolio. See Large accounts.                              |       |
|-----------------------------------------------------|-------------------------------------------------------------|-------|
| bar-scoring, 123-125                                | profitability, 86t-87t                                      |       |
| range, 140-141                                      | profit-per-trade metric development                         |       |
| CME. See Chicago Mercantile Exchange                | commodities, 112t                                           |       |
| Combined equity, stock/commodity strategies         | commodities, pullback filter, 112t                          |       |
| (trading), 242-243                                  | Donchian look-back, 111t                                    |       |
| Commodities. See Full-size portfolio; Mid-size      | equity curve, 114f                                          |       |
| portfolio                                           | high-volatility range-based filter, 113t                    |       |
| addition. See Second-tier commodities.              | low-volatility range-based filter, 114t                     |       |
| average range, high-volatility filter, 101t         | profit stops, 83-87                                         |       |
| bar gaps, 142-143                                   | pullback filter, 112t, 139                                  |       |
| congestion, absence, 143t                           | purchase, counter-trend strategy (usage),                   |       |
| trend direction, 143t                               | 34-35                                                       |       |
| bar-scoring example, 123t                           | range, serial correlation, 163t                             |       |
| baseline entry signal, 65                           | ranking, 195t                                               |       |
| basket, opening gaps, 140t                          | small accounts, money management                            |       |
| buying strategy results, average dollar profit-     | techniques, 191                                             |       |
| per-monthly transaction, 34t                        | standard deviation                                          |       |
| congestion, bar gaps, 142t                          | catastrophic stop, 78t                                      |       |
| contract rollover, accounting, 272                  | low-volatility filter, 100t                                 |       |
| divergences                                         | streams, serial correlation, 162t                           |       |
| fading, 137t                                        | system                                                      |       |
| trading, 136t                                       | catastrophic dollar stop, 77t                               |       |
| diversification example, 196f                       | development, total profit-per-trade metric (usage), 111-116 | 279   |
| dollar-based profit stops, 83t                      | equity curve, 84f 34-35                                     | INDEX |
| Donchian midpoint catastrophic stop, 78t            | three-step process, results,                                |       |
| Donchian system, performance, 193t-194t             | time-based exits, 82-83                                     |       |
| exit stops. See Exit stops.                         | top tier commodities, one-lot/two-lot                       |       |
| Fibonacci retracements, 148-149                     | contrast, 196t                                              |       |
| trading, 148t, 149t                                 | traders, margin requirements, 262-263                       |       |
| gain-to-pain metric development, equity curve, 115f | trades, standard error/sample size (contrast), 18f          |       |
| graphs, separation, 63                              | transaction costs, accounting, 27                           |       |
| grouping, reason, 256 groups, 255-259               | trend-following entry, entry power, 48f summary, 54-56      |       |
| longer-term trend filter, 99                        | volatility-based filters, 99-105                            |       |
| list, 99t                                           | volatility range, 253t-254t                                 |       |
| profit-per-trade metric development,                | Commodities strategy                                        |       |
| 113t                                                | annual return/max draw-down, 85t,                           |       |
| moving average system                               | 102t-103t                                                   |       |
| catastrophic stop, addition, 21t, 22t               | comparison, 115t-116t                                       |       |
| days, number, 20t                                   | development, 101, 103t-104t                                 |       |
| look-back trend filter, addition, 22t               | selection, 116                                              |       |
| N-day look-back filter, addition, 21t               | high-volatility filter, exit basis, 101t                    |       |
| opening gaps, 139-140                               | pullback filter, usage, 98t Commodity strategy              |       |
| parabolic trailing stop, 81t                        | differences, summary,                                       |       |
| performance, 104t-105t                              | 237t                                                        |       |

```
Commodity strategy ( continued ) equity curve, development, 102f large-account trading, annual return/max draw-down, 229t open-trade equity curve/closed-trade equity curve, 228f performance, 242 trading, 241 usage, 179, 183 Commodity Systems Inc. (CSI), contract data, 18 Commodity trading day of the week, 97-99 process, 230 trend-following strategy, one-day return, 42t zero sum game, 251 Commodity Trading Advisor (CTA) average annual yearly performance, 2-3 average return, risk (impact), 3 gains, absence (duration), 3 high return, high draw-down (relationship), 3 performance, 2t return performance numbers, 2 risk, contrast, 3f trend-followers, 156 Complete Guide to the Futures Markets, A (Schwager), 167 Compounded return, non-compounded return (contrast), 176f Compounding approach, fixed risk (usage), 180t Continuous contacts analysis problems, 268 changes, actual-price changes (comparison), 270t data, 269t day of data, 270t reality, 271 solution, 269-270 Continuous contacts, understanding, 265 Contract printing, 252 Contract risk. See Relative contract risk relative risk, determination, 253 Contracts. See Electronic contracts Correlation algorithm, 256 coefficients. See Data. formulas, 247-250 uses, 248-249
```

```
Counter-trend buy strategies, determination, 32 Counter-trend entry techniques, comparison, 56-63 Counter-trend-following pairs, 38 Counter-trend-following stock entry Donchian entry, 61-62 note, 63 observations, 63 rate of change, 60 RSI, 58-59 single moving entry, 57 stochastics, usage, 59-60 two moving averages, 58 Counter-trend-following strategies, 41t Counter-trend strategies, usage, 34-35 Counter-trend systems, usage, 25-26 CTA. See Commodity Trading Advisor Cumulative dividends, determination, 269 Currency commodities, correlation, 260t correlation. See Major currencies. one lot units, usage, 35 types, 35 Curve-fit results, out-of-sample BRAC test results (contrast), 131t Curve-fitting, 8-19 development practices, usage, 8-11 effects, minimization, 19-20 examples, 8, 273 comparison, 12 problem, 24 testing, 19-24 example, 20-24 out-of-sample testing, contrast, 23-24 trade number, proportion, 12-15 hypothesis (testing), trade data (usage), 16-19 Cut-off trading, 249 D Daily-bar commodity data, trend-following entry techniques (comparison), 49-56 Daily bars, 32-40 data, comparison, 54t impact. See Markets. tendencies, 40 Daily-bar stock data
```

| counter-trend entry techniques, comparison, 56-63         | commodities, 83t risk reduction, 83                                  |       |
|-----------------------------------------------------------|----------------------------------------------------------------------|-------|
| limit orders, usage, 274-275                              | Dollar-based stop, deficiencies (impact), 78                         |       |
|                                                           | Dollar risk,                                                         |       |
| Data                                                      | 196                                                                  |       |
| comparison. See Historical data.                          | Dollar stop, testing, 77 Domestic commodities, CSI contract data, 18 |       |
| curve-fitting, usage, 8-11                                | Donchian, Richard, 53                                                |       |
| pairs, correlation coefficients, 248f                     | Donchian entry, 53                                                   |       |
| sample, parameter values, 22-23                           | counter-trend-following stock entry, 61-62                           |       |
| usage. See Trade.                                         | 62f                                                                  |       |
| DAX futures index, 78                                     | entry power, 53f,                                                    |       |
| Delta levels, 182t                                        |                                                                      |       |
|                                                           | Donchian highs/lows, 134, 136-137, 146                               |       |
| Deviation stop. See Volatility-based deviation            | Donchian look-backs, 108t                                            |       |
| stop                                                      | profit-per-trade metric development,                                 |       |
| Directional data streams, 247f                            | usage, 75t                                                           |       |
| Directional volatility, standard deviation                | Donchian midpoint catastrophic stop,                                 |       |
| accounts (difference), 247                                | commodities, 78t                                                     |       |
| Divergence                                                | Donchian points, usage, 144-146                                      |       |
| buy entry, 134                                            | Donchian stock strategy, 72 Donchian system                          |       |
| buy exit, 134 buy/sell signals,                           | closed-trade equity                                                  |       |
| 135f                                                      | curve, 186f                                                          |       |
|                                                           | performance, 193t-194t                                               |       |
| short exit, 134 trading, 136t                             | Donchian trend-following strategy, testing, 222                      | 281   |
| Divergence signal                                         | Draw-down. See Closed-trade draw-down; Open-trade draw-down          |       |
| impact, 23 strength, 134-137                              | contrast. See Average annual return.                                 | INDEX |
| Diversification, 192-193                                  | example, 186-188                                                     |       |
| benefits, 196                                             | maximum, 4-5                                                         |       |
| examples, 196f, 197f                                      | measure. See Normal draw-down.                                       |       |
| Diversified portfolios                                    | metrics, 187-188 percentage, 188                                     |       |
| non-diversified portfolios, contrast, 192t                |                                                                      |       |
| trading results, 192t                                     | relationship. See High return.                                       |       |
| Dividend-adjusted file, problems, 268                     |                                                                      |       |
| Dividend-adjusted results, 271                            | E                                                                    |       |
| Dividends                                                 |                                                                      |       |
| accounting, 265-272 cumulative amount, determination, 269 | Electronic-contract commodities, usage, 41 Electronic contracts, 263 |       |
| determination. See Cumulative dividends.                  | Electronic trading, 263                                              |       |
| payouts, 151                                              | Elliott wave cycle, 45                                               |       |
| trades, profit, 152t                                      | Energy commodities, correlation, 259t                                |       |
| Dogs of the Dow, trading strategy, 169-172                | Entries, 45                                                          |       |
| average, 171                                              | baseline, formation, 76                                              |       |
| buy and hold strategy, contrast, 170t                     | criterion, 128                                                       |       |
| Dollar-based FX pairs, commodities                        | Donchian entry, 53                                                   |       |
| (comparison), 36t                                         | element, importance, 46-49                                           |       |
| Dollar-based pairs, trend-following, 38                   | elimination. See False entries.                                      |       |
| Dollar-based profit stops                                 | examples, 47                                                         |       |

|       | Entries ( continued )                                            | commodity example, 76-82                        |
|-------|------------------------------------------------------------------|-------------------------------------------------|
|       | importance, exits (comparison),                                  | stock example, 69-72                            |
|       | 153-155                                                          |                                                 |
|       | number, abnormality, 48-49 price, dividend size (contrast), 152t | F                                               |
|       | setup, occurrence, 91-92                                         | False entries, elimination, 97                  |
|       | system, 49                                                       | Fast market conditions, impact, 27              |
|       | techniques, comparison, 54t, 55t, 56t                            | Fibonacci levels, impact, 148                   |
|       | testing, 56                                                      | Fibonacci numbers, importance, 144              |
|       | trade risk, limitation, 196, 225-226                             | Fibonacci retracements                          |
|       | ranking, 196t trend-followers, 46                                | buy/sell setups, 145f                           |
|       |                                                                  | commodities, 148-149                            |
|       | Entry power, 48f, 49f, 50f                                       | level, 45                                       |
|       | Donchian entry, 53f, 62f                                         | stocks, trading long, 146t, 147t                |
|       | rate of change (ROC), 52f, 60f                                   | stocks, trading short, 147t                     |
|       | single moving average, 57f                                       | trading, 143-149                                |
|       | standard deviation breakouts, 52f                                | commodities, 148t, 149t                         |
|       | standard deviation entry, 61f                                    | Fibonacci sequence, introduction, 143-144       |
|       | stochastic, 51f                                                  | Filters. See Volatility                         |
|       | two moving averages, 58f                                         | Filters, types, 89                              |
|       | Equity                                                           | re-examination, 109                             |
|       | risk per trade, performance/percent                              | Finalized money management overlay,             |
|       | (contrast), 230t                                                 | development, 221-222                            |
|       | stock/commodity strategies (trading). See                        | Financial commodities, correlation, 261t        |
| 282   | Combined equity.                                                 | First-N-in-a-group, 224-225                     |
|       | Equity curve, 102                                                | diversification example, 196t                   |
| INDEX | building, 179                                                    | trading, 193-196                                |
|       | commodities gain-to-pain metric development, 115f                | First notice day, 252 Fixed fractional, 180-182 |
|       | profit-per-trade metric development, 114f                        | Fixed moving averages, reaction, 80             |
|       | system, 84f                                                      | Fixed portfolios, 199-210                       |
|       | development. See Commodity strategy.                             | Fixed-rate sizing, 233-234                      |
|       | example, 168f                                                    | Fixed ratio, 182-183                            |
|       | gain-to-pain metric development, 110f                            | trading, delta levels, 182t                     |
|       | commodities, 115f                                                | Fixed risk, 180-182                             |
|       | positions, limitation, 218t                                      | compounding example, 180                        |
|       | profit-per-trade metric development, 110f                        | non-compounding, example, 180                   |
|       | trades, variation, 168                                           | performance. See Large portfolios.              |
|       | Exchange traded fund (ETF), 217                                  | solutions, Optimal F (comparison), 181t         |
|       | Exits                                                            | usage, compounding approach, 180t               |
|       | importance, entries (contrast), 153-155                          | Fixed-risk percentage, determination, 224       |
|       | quality, 154-155                                                 | Fixed-risk performance, 222t                    |
|       | signals, commodity example. See Reversal                         | Fixed-risk sizing, 222-223                      |
|       | stock example. See Time-based exits.                             | Flat time                                       |
|       |                                                                  | design metric, 4                                |
|       | trading days example, 72t                                        | 4                                               |
|       | trading system elements, 65                                      | duration,                                       |
|       | Exit stops                                                       | Foreign Exchange (Forex) (FX) pairs             |
|       | catastrophic stop, 69                                            | buy-and-hold, contrast, 37                      |

| commodities, comparison, 36t results, average dollar                                    | Gold trades, standard error/sample size (contrast), 17f                  |       |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|-------|
| profit-per-monthly                                                                      |                                                                          |       |
| transaction, 35t                                                                        | Good until canceled stop loss, usage, 9                                  |       |
| tendency analysis, 39                                                                   | Grain commodities, correlation, 256t                                     |       |
| three-step process, results, 35-36                                                      | Group exposure, limiting, 193-196                                        |       |
| trading, 37                                                                             |                                                                          |       |
| trend-following strategy , one-day return, 42t trend tendencies, average dollar profit- | H                                                                        |       |
| per-monthly transaction, 38t trend-following, average dollar profit-per-                | Hedging. See Short SPY positions limitations, 218t                       |       |
| monthly transaction, 37t trend-following tendencies, 39t                                | strategy, impact, 218                                                    |       |
| trending perspective, 36-40                                                             | High return, high draw-down (relationship), 3                            |       |
|                                                                                         | High-volatility filter                                                   |       |
| Foreign Exchange (Forex) (FX) transaction costs, accounting, 27                         | commodities                                                              |       |
| Foreign stock indices, 78                                                               | average range, 101t                                                      |       |
| Formulas, understanding,                                                                | standard deviation, 100t                                                 |       |
| 245                                                                                     | exit basis, 101t                                                         |       |
| Full-size portfolio                                                                     | High-volatility filter,                                                  |       |
| annual return, 211t-212t closed-trade equity curve,                                     | stocks range, 92t                                                        |       |
| 211f commodities, 208                                                                   | standard deviation, 93t                                                  |       |
| list, 208t                                                                              | High-volatility range-based filter, commodities (profit-per-trade metric |       |
| max draw-down,                                                                          | development), 113t                                                       |       |
| 211t-212t open-trade equity curve,                                                      | Hill, John, 54                                                           |       |
| 211f performance, 209-212                                                               | Lundy,                                                                   |       |
|                                                                                         | Hill, 54                                                                 | 283   |
| small-account money management, 208-209 rules/limits, 209t                              | Historical data, comparison, 8                                           |       |
| start-trade statistics, 209f                                                            | Hold periods, example, 136t, 137t                                        | INDEX |
| Fully leveraged commodities, trading, 262                                               |                                                                          |       |
| trading, 210-211                                                                        |                                                                          |       |
| Futures, understanding, 251                                                             | I                                                                        |       |
|                                                                                         | IBM                                                                      |       |
| G                                                                                       | actual prices continuous contract data, 269t dividend time, 267t, 268t   |       |
| Gain-to-pain metric development commodities, equity curve, 115f equity curve, 110f      | split time, 266t, 267t appreciation, data stream, 269                    |       |
| ratio                                                                                   |                                                                          |       |
| Gain-to-pain                                                                            | data file, 269                                                           |       |
| decrease, 75                                                                            | data impact, difference, 270-271                                         |       |
| formation, 218                                                                          | dividend, issue, 266-267                                                 |       |
| increase, 68                                                                            | dividend-adjusted prices, dividend                                       |       |
| reduction, 182 solution,                                                                | time, 258t                                                               |       |
| Gain-to-pain superiority, 110                                                           | split-adjusted prices, split time, 267t                                  |       |
| Gaps 138-143                                                                            | Illiquidity, stop inactivity, 10 Infinite data pool, usage, 8            |       |
| buying/fading, opening, 138                                                             | Infinite sample                                                          |       |
| Geometric mean return                                                                   | mean, positive level, 15                                                 |       |
| (GMR), 178-179 GMR. See Geometric mean return                                           | results (difference reduction), sample size                              |       |
| Golden Ratio, 144                                                                       | increase (impact), 12f                                                   |       |

| Infinite sample ( continued ) size, increase, 18 variance, explanation, 14-15 Instruments, trading (benefit), In-the-market stop, risk control, Intra-day bars commodities, trading, 41 FX pairs, trading, 42-43   | Limit trade risk entry money management strategy, usage, 197 Long entry, 75, 137 best parameter, 66 Longer-term traders, strategy, 19 Longer-term trend filters, 89 addition, 91t commodities, 99 stocks, 90-91 Longer-term trend-following strategies, 76   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 39                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                              |
| 71                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                    | Long exit, 137                                                                                                                                                                                                                                               |
| stock trading, 40-41                                                                                                                                                                                               |                                                                                                                                                                                                                                                              |
| J Jones, Ryan, 182                                                                                                                                                                                                 | Long-only stock trade results, catastrophic stop level (contrast) exit intra-day, 70t                                                                                                                                                                        |
| K                                                                                                                                                                                                                  | exit on close, 70t next day exit, 69t                                                                                                                                                                                                                        |
| Kelly criteria, usage, 156-159                                                                                                                                                                                     | stats, look-back, 68t Long-only strategy, 67                                                                                                                                                                                                                 |
| L                                                                                                                                                                                                                  | Long position, exit (result), 9 Long-trade breakout, 98t                                                                                                                                                                                                     |
| Lane, George, 50 Large-account money management,                                                                                                                                                                   | Look-back breakout, 66 Look-back filter                                                                                                                                                                                                                      |
| techniques, 236 Large-account performance metrics, 188 annual percent return, 188-189                                                                                                                              | addition. See Commodities. days, number (variation), 20 usage, 91. See also Swiss Franc. Losers, addition (avoidance),                                                                                                                                       |
| draw-down percentage, 188 Large accounts commodity portfolio, 223t-224t                                                                                                                                            | 164-165 Low-volatility filter standard deviation, commodities, stocks, average range, 92t                                                                                                                                                                    |
| money management techniques commodities, 221                                                                                                                                                                       | 100t Low-volatility range-based filter,                                                                                                                                                                                                                      |
| stocks, 233 trading, annual return/max Commodity strategy. stock performance. See                                                                                                                                  | commodities (profit-per-trade metric                                                                                                                                                                                                                         |
| draw-down. See Large-account Risk Large-account stock solution, annual                                                                                                                                             | development), 114t M                                                                                                                                                                                                                                         |
| return/ draw-down, 238t Large-account traders                                                                                                                                                                      | MACD. See Moving Average Convergence Divergence Major currencies, correlation, 259                                                                                                                                                                           |
| money management strategies, 222 small-account traders, contrast, 184                                                                                                                                              | Margin, 259-263                                                                                                                                                                                                                                              |
| Large-account trading, advantages, 230                                                                                                                                                                             | requirements, 262-263 Market class, tendencies,                                                                                                                                                                                                              |
| Large portfolios, fixed risk performance,                                                                                                                                                                          | 31 Markets                                                                                                                                                                                                                                                   |
| Leonardo of Pisa, 144                                                                                                                                                                                              | change, examination, 5                                                                                                                                                                                                                                       |
| Leverage, involvement, 262                                                                                                                                                                                         | differences                                                                                                                                                                                                                                                  |
| Limit orders                                                                                                                                                                                                       | daily bars, impact,                                                                                                                                                                                                                                          |
| popularity, 27-29                                                                                                                                                                                                  | 32-40 intra-day bars, impact,                                                                                                                                                                                                                                |
| slippage, concerns (absence),                                                                                                                                                                                      | resistance, reduction, 32                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                    | 40-43                                                                                                                                                                                                                                                        |
| 27 systems usage, 28                                                                                                                                                                                               |                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                    | stop placement, 10                                                                                                                                                                                                                                           |
| price, purchase, 28                                                                                                                                                                                                |                                                                                                                                                                                                                                                              |
| Limit                                                                                                                                                                                                              |                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                    | example,                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                    | 172                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                    | trades, percentage                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                    | 224t                                                                                                                                                                                                                                                         |

| Martingale betting, dangers, 164 Max draw-down. See Commodity strategy; Full- size portfolio; Mid-size portfolio average annual return, contrast, 5, 93, 101 average profit-per-year, comparison, 91 commodity strategy, 102t-103t   | days, number (variation), 20 reversal system, usage, 16 system. See Commodities; (MACD), 134   |       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|-------|
|                                                                                                                                                                                                                                      | Swiss Franc. usage, 82t Moving Average Convergence Divergence                                  |       |
| performance, 204-208 small-account money management, 204                                                                                                                                                                             | Non-compounded return (fixed size),                                                            |       |
| techniques/limits, 204t                                                                                                                                                                                                              | compounded return (contrast), 176f                                                             | INDEX |
| Mid-term trend-following strategies, 76                                                                                                                                                                                              | comparison, 180t                                                                               |       |
| tolerance, 5                                                                                                                                                                                                                         |                                                                                                |       |
| Momentum sell setup, 137 Money management. See Full-size portfolio; Mid-size portfolio                                                                                                                                               | diversified portfolios, contrast, trading results, 192t                                        |       |
| defining, effects, 161                                                                                                                                                                                                               | 4                                                                                              |       |
| Max N, exposure (limitation), 224-225 open trade risk                                                                                                                                                                                | bar gaps, 142t congestion                                                                      |       |
| Max percentage, limitation, 227t Max 204, 208                                                                                                                                                                                        | absence, bar gaps, 141t                                                                        |       |
| start-trade draw-down,                                                                                                                                                                                                               | bar gaps, 141t                                                                                 |       |
| commodities, correlation,                                                                                                                                                                                                            | opening gaps, 140t                                                                             |       |
| Meat 257t                                                                                                                                                                                                                            | NASDAQ 100 basket                                                                              |       |
| Metal commodities, correlation, 258t                                                                                                                                                                                                 | trade, example, 163-164                                                                        |       |
| Metals, indices, 78                                                                                                                                                                                                                  | NASDAQ 100 basket, stock performance,                                                          |       |
| Mid-size                                                                                                                                                                                                                             | 94                                                                                             |       |
| portfolio annual return, 207t                                                                                                                                                                                                        | N-day average, variation. See Swiss Franc                                                      |       |
| closed-trade equity curve, 206f                                                                                                                                                                                                      | N-day look-back filter, addition. See Commodities                                              |       |
| commodities, 203-204 list, 204t                                                                                                                                                                                                      | N-day look-back trend filter, usage. See Swiss                                                 |       |
| max draw-down, 207t                                                                                                                                                                                                                  | Franc (Wilder                                                                                  |       |
| 206f                                                                                                                                                                                                                                 | New Concepts in Technical Trading System Jr.), 50, 80                                          |       |
| open-trade equity curve,                                                                                                                                                                                                             |                                                                                                | 285   |
| start-trade statistics, 205f                                                                                                                                                                                                         | Non-compounding sizing approaches,                                                             |       |
| Momentum divergence short setup, 134                                                                                                                                                                                                 | Non-direction data streams, 247f                                                               |       |
|                                                                                                                                                                                                                                      | Non-diversified portfolios                                                                     |       |
|                                                                                                                                                                                                                                      | 192t                                                                                           |       |
| 155-159                                                                                                                                                                                                                              | Normal draw-down, measure, 4                                                                   |       |
|                                                                                                                                                                                                                                      | Normal return, measure,                                                                        |       |
| feedback, inclusion,                                                                                                                                                                                                                 |                                                                                                |       |
| 107                                                                                                                                                                                                                                  | N signals, 194                                                                                 |       |
| introduction, 175                                                                                                                                                                                                                    |                                                                                                |       |
| statements, examination, 155-156 strategy. See Limit trade risk entry money                                                                                                                                                          | O                                                                                              |       |
| management strategy.                                                                                                                                                                                                                 | OOPS (short-term trading system), 140                                                          |       |
| optimum, 156                                                                                                                                                                                                                         | Opening gaps                                                                                   |       |
| techniques, 191                                                                                                                                                                                                                      | commodities, 139-140                                                                           |       |
| traders, 158t                                                                                                                                                                                                                        | baskets, 140t                                                                                  |       |
| Monte Carlo analysis, 159-161                                                                                                                                                                                                        | NASDAQ stocks, 139t                                                                            |       |
| engine, assumptions, 160                                                                                                                                                                                                             | shorting opportunities, absence, 138                                                           |       |
| Monte Carlo simulations, 159                                                                                                                                                                                                         | stocks, 138-139 Open-trade dollar risk, limitation, 228                                        |       |
| trading Moving average                                                                                                                                                                                                               | Open-trade draw-down, 184-185                                                                  |       |

| Open-trade equity curve. See Donchian system; Full-size portfolio; Mid-size portfolio commodity strategy, 228f correspondence, 185 starter portfolio, 202f Open-trade equity growth, 184f Open-trade performance metrics, performance metrics (comparison), 213t   | open-trade performance metrics /closed-trade performance metrics (comparison), 213t open-trade risk, limitation, 197-198 ranking, 198t   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                                                                                    | performance. See Full-size portfolio; Mid-                                                                                               |
| closed-trade                                                                                                                                                                                                                                                       | size portfolio.                                                                                                                          |
|                                                                                                                                                                                                                                                                    | selection, 223-224 small-account money management. See                                                                                   |
| Open-trade risk, limitation, 197, 227. See                                                                                                                                                                                                                         | Full- size portfolio; Mid-size portfolio.                                                                                                |
| also Max open trade risk percentage                                                                                                                                                                                                                                | trading, equity (ranges), 212                                                                                                            |
| Open-trade risk, percentage. See Total portfolio                                                                                                                                                                                                                   | Position hedging, 217-220, 235                                                                                                           |
| max open-trade risk percentage; portfolio open-trade risk                                                                                                                                                                                                          | Position sizing, 216-217 money management literature,                                                                                    |
| Total                                                                                                                                                                                                                                                              | summary, 182                                                                                                                             |
| trades, total number (limitation),                                                                                                                                                                                                                                 | 175 techniques, 175-182                                                                                                                  |
| Open 198, 226, 234-235 ranking, 198t, 226t, 234t-235t                                                                                                                                                                                                              | metal members,                                                                                                                           |
| Optimal F, 178-180                                                                                                                                                                                                                                                 | Precious Price divergence short                                                                                                          |
|                                                                                                                                                                                                                                                                    | 257                                                                                                                                      |
|                                                                                                                                                                                                                                                                    | setup, 134 Price sell setup, 137                                                                                                         |
| brute force results, 178t                                                                                                                                                                                                                                          | Profitability                                                                                                                            |
| fixed risk solutions, comparison, 181t                                                                                                                                                                                                                             | decrease, 230                                                                                                                            |
| strategy, steps, 178 trade perspective, 178-179                                                                                                                                                                                                                    | impact, 165-166                                                                                                                          |
| value, 178                                                                                                                                                                                                                                                         | probabilities, 206                                                                                                                       |
| Out-of-sample BRAC test results, curve-fit results (contrast), 131t                                                                                                                                                                                                | Profitability, commodity categories, 86t-87t Profit factor, 167                                                                          |
| Out-of-sample methodology, 24 Out-of-sample testing                                                                                                                                                                                                                | Profit-per-trade average, 14                                                                                                             |
| contrast. See Build, Rebuild, and Curve-fitting.                                                                                                                                                                                                                   | decrease, 68 improvement, pullback filter                                                                                                |
| Compare;                                                                                                                                                                                                                                                           |                                                                                                                                          |
| value, 23                                                                                                                                                                                                                                                          | (impact), 113 increase, 75                                                                                                               |
| Overtrading, impact, 166                                                                                                                                                                                                                                           | absence, stop loss (impact), 71 time-based exit, impact, 109                                                                             |
| P Pairs. See Foreign Exchange pairs trading, trend-following tendencies, Parabolic stop, example, 81t                                                                                                                                                              | peak, 113-114 usage, 275-276                                                                                                             |
|                                                                                                                                                                                                                                                                    | values, standard deviation, 13-14 metric                                                                                                 |
| 39t                                                                                                                                                                                                                                                                | Profit-per-trade development commodities equity curve, 114f                                                                              |
| Parabolic Time/Price System, 80                                                                                                                                                                                                                                    | 113t                                                                                                                                     |
| Parabolic trailing stop, commodities, 81t Pearson Correlation Coefficient, 247-248                                                                                                                                                                                 | longer-term trend filter, pullback filter, 112t                                                                                          |
|                                                                                                                                                                                                                                                                    | equity curve, 110f                                                                                                                       |
| Performance metrics. See Full-size                                                                                                                                                                                                                                 |                                                                                                                                          |
| portfolio; Large-account performance metrics;                                                                                                                                                                                                                      | profit stops, 109t                                                                                                                       |
| Mid-size portfolio; Small-account                                                                                                                                                                                                                                  | stops commodity                                                                                                                          |
|                                                                                                                                                                                                                                                                    | Profit example, exit strategy, 73                                                                                                        |
| performance metrics See Full-size portfolio; Mid-size                                                                                                                                                                                                              | 83-87 profit-per-trade metric                                                                                                            |
| portfolio                                                                                                                                                                                                                                                          | development,                                                                                                                             |
| Portfolio.                                                                                                                                                                                                                                                         | 109t stock example, 73-75                                                                                                                |
| commodities. See Full-size portfolio commodities; Mid-size                                                                                                                                                                                                         | targets                                                                                                                                  |
|                                                                                                                                                                                                                                                                    | Profit                                                                                                                                   |
| portfolio                                                                                                                                                                                                                                                          | basis, standard deviation counts (usage),                                                                                                |
| commodities.                                                                                                                                                                                                                                                       |                                                                                                                                          |
|                                                                                                                                                                                                                                                                    | 84t                                                                                                                                      |

| exits, scalping strategies, 73-74 results, stock strategy, 73t                                          | Risk per trade, performance/percent (contrast). See Equity                               |       |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-------|
| Pruitt, George, 54                                                                                      | Risk-reward goals, meeting, 4                                                            |       |
| Pullback filter                                                                                         | ROC. See Rate of change                                                                  |       |
| impact, 113                                                                                             | RSI. See Relative Strength Index                                                         |       |
| usage, 98t, 112t                                                                                        | S                                                                                        |       |
| R                                                                                                       | Sample size increase, impact. See Infinite sample results. standard error, contrast. See |       |
| Random exit, 154 Rate of change (ROC), 51-52 counter-trend-following stock entry, entry power, 52f, 60f | Commodities; Gold trades. Scalping strategies, 73-74 Schwager, Jack, 133, 167            |       |
| 60 usage, 60 (variation), 198                                                                           |                                                                                          |       |
| open trades                                                                                             |                                                                                          |       |
| Real-time trading,                                                                                      | Seasonal filters, 89                                                                     |       |
| contract risk, 252-255                                                                                  | Second-tier commodities, addition,                                                       |       |
| Relative                                                                                                | 196                                                                                      |       |
| Relative Strength Index (RSI), 134                                                                      | Sell stop, placement, 25                                                                 |       |
| counter-trend-following stock entry, 58-59                                                              | Semi-precious metal members, 257                                                         |       |
| 80-day entry signals, 61 entry power, 50f, 59f                                                          | Sequential data, serial relationship, 162 Sharpe ratio, 167                              |       |
| Retracement, 45                                                                                         | Short entry, 75, 137                                                                     |       |
| levels, stock trading long, 148t                                                                        | best parameter, 66                                                                       |       |
| Return                                                                                                  | Shorter-term traders, strategy, 19                                                       |       |
| expectations, 208                                                                                       | Short exit, 137                                                                          |       |
| high draw-down, relationship. See High                                                                  | Short SPY positions, hedging, 236                                                        | 287   |
| return.                                                                                                 | ranking, 217t, 235t                                                                      |       |
| max draw-down, contrast. See Average                                                                    | Short-trade breakout, 998t                                                               | INDEX |
| annual return.                                                                                          | Single moving average                                                                    |       |
| measure. See Normal return.                                                                             | counter-trend-following stock entry, 57                                                  |       |
| metrics, 130                                                                                            | entry power, 57f                                                                         |       |
| Return-per-trade, 128                                                                                   | Sizing. See Fixed-risk sizing                                                            |       |
| Return/risk expectations, 1-3                                                                           | approaches. See Non-compounding sizing                                                   |       |
| Reversal exit signals                                                                                   | approaches. summary, 183                                                                 |       |
| commodity example, 75-76 stock example, 66-69                                                           | techniques. See Position sizing.                                                         |       |
| Reversal trading commodities, Donchian look-                                                            | form, 177                                                                                |       |
| backs (usage), 75t                                                                                      | Slippage, problem, 74                                                                    |       |
| 151                                                                                                     | Small-account metrics                                                                    |       |
| Reverse splits, behavior, Reverse split-trade statistics, 150t                                          | closed-trade draw-down, 184-185                                                          |       |
| Risk                                                                                                    |                                                                                          |       |
|                                                                                                         | draw-down example, 186-188                                                               |       |
| control, addition, 9 increase,                                                                          | open-trade draw-down, 184-185                                                            |       |
| 229                                                                                                     | start-trade draw-down, 185-186                                                           |       |
| levels, large-account stock performance, 237t metrics, 130                                              | Small-account money management. See Full-size Starter                                    |       |
| usage, 186-187                                                                                          | portfolio; Mid-size portfolio; portfolio                                                 |       |
| minimization, 193                                                                                       | stock strategy, open-trade equity curve                                                  |       |
| performance. See Fixed-risk performance.                                                                | /closed-trade equity curve, 219t                                                         |       |
| sizing. See Fixed-risk sizing.                                                                          | strategy, 228                                                                            |       |
| worst-case scenario, 4                                                                                  | technique, 197-198                                                                       |       |

Small-account performance metrics, 183-184 Small accounts money management approach, customization, 200 money management techniques commodities, 191 stock strategy, 215 Small-account stock trading solutions, 219t Small-account trader, diversification (impact), 197 Small account trader portfolios, open-trade performance metrics/closed-trade performance metrics (comparison), 213t Small-account traders, large-account traders (contrast), 184 Smoothed values, example, 51 Soft commodities, correlation, 257t Split-adjusted data, usage, 269 Split-adjusted file, problems, 267-268 Split dates, analysis, 149 Split trades, performance, 150 Split-trade statistics, 150t. See also Reverse splittrade statistics SPY ETF, performance, 235 SPY positions, hedging. See Short SPY positions Standard deviation. See Profit-per-trade accounts, difference. See Directional volatility. basis, low-volatility filter, 93t breakouts, 52-53 entry power, 52f catastrophic stop, commodities, 78t profit-per-trade metric development, 112t counter-trend-following stock entry, 61 counts, profit targets (basis), 84t entry entry power, 61f percentage profit, 127t formula, 245-246 significance, 245 t-tests/z-tests, usage, 167 Standard error computation, 17 function, explanation, 14 sample size, contrast. See Commodities; Gold trades. strategies, impact, 19

Starter portfolio annual return, 202t-203t closed-trade equity curve, 202f commodities, 199 max-draw-down, 202t-203t open-trade equity curve, 202f performance, 200 small-account money management, 199 start-trade statistics, 200f trading, 202 Start-trade draw-down, 185-186 comparison, 187f Start-trade profit distributions, 187f Start-trades, comparison, 213t Start-trade statistics. See Full-size portfolio; Mid-size portfolio; Starter portfolio Stochastics counter-trend-following stock entry, 59-60 entry power, 51f, 60f Stock index commodities, correlation, 262t Stocks average range, low-volatility filter, 92t bar gaps, 140-142 bar-scoring, example, 123t baseline entry signal, 65 basket, performance, 33 buying strategy results, average percentage profit-per-month, 33t data, problem, 258 database, upward bias, 40-41 day of the week filters, 90t divergences, trading, 136t high-volatility filter, basis, 92t longer-term trend filter, 90-91 addition, 91t low-volatility filter, standard deviation basis, 93t opening gaps, 138-139 pairs, trading, 273-274 performance. See Large-account stock performance. positions, performance (max number), 216t-217t profit-per-trade metric development, 108t time-based exit, 109t purchase, dividends (production), 152-153 range, serial correlation, 163t solution, open-trade equity curve/closedtrade equity curve, 237f

| split-trade statistics, 150t                                                | inactivity. See Illiquidity.                                                 |       |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------|-------|
| standard deviation, high volatility filter, 93t                             | placement, 10                                                                |       |
| strategy, 215                                                               | stock example. See Profit stops.                                             |       |
| performance metrics, 216                                                    | Strategies. See Commodity strategy; Stock                                    |       |
| strategy equity curve, 74f                                                  | strategy                                                                     |       |
| development, 94f                                                            | combination, trading mechanics, 241                                          |       |
| streams, serial correlation, 162t                                           | performance, comparison, 242t, 243t                                          |       |
| three-step process, 32-33                                                   | Survivorship basis, 33                                                       |       |
| trade, look-back, 66t                                                       | Swiss Franc                                                                  |       |
| transaction costs, accounting, 26-27                                        | risk control, addition, 9                                                    |       |
| volatility-based filters, 91-97                                             | trending, 9                                                                  |       |
| weakness, 128                                                               | Swiss Franc, moving average system                                           |       |
| Stock splits                                                                | catastrophic stop, usage, 10t, 11t                                           |       |
| accounting, 265-272                                                         | look-back filter, usage, 10t, 11t                                            |       |
| purchase, 149-151                                                           | N-day average, variation, 9t                                                 |       |
| Stock strategy                                                              | N-day look-back trend filter, usage, 10t                                     |       |
| annual return, draw-down                                                    | Synthetic data, creation, 161-162                                            |       |
| (comparison), 111t                                                          | System development, money management                                         |       |
| annual return/max draw-down, 74t                                            | feedback (inclusion), 107                                                    |       |
| performance, 242                                                            | System statistics, example, 168                                              |       |
| profit targets results, 73t                                                 |                                                                              |       |
| short-coming, 217 trading, 241-243                                          | T                                                                            |       |
| Stock strategy, performance, 95t-97t                                        | Tendency analysis, usage, 40                                                 |       |
| Stock system                                                                | Terminal wealth relative (TWR), 178                                          | 289   |
| annual return/max draw-down, 94t development, total profit-per-trade metric | Tharp, Van K., 153                                                           |       |
| (usage), 108-111                                                            | Time-based exits commodity example, 82-83, 82t                               | INDEX |
| equity curve, position limitation, 218f                                     | impact, 109                                                                  |       |
| example, bar-scoring/defined criteria,                                      | profit-per-trade metric development, 109t                                    |       |
| 126-131                                                                     | stock example, 72-73                                                         |       |
| tradeable solutions, 236-238                                                | Top tier commodities, one-lot/two-lot                                        |       |
| Stock trading day of the week filter, 90                                    | (contrast), 196t                                                             |       |
| difficulty, 57                                                              | Total portfolio max open-trade risk percentage,                              |       |
| Fibonacci levels, impact, 147                                               | limitation, 228t                                                             |       |
| intra-day bars, usage, 40-41                                                | Total portfolio open-trade risk                                              |       |
| long                                                                        | limitation, 197-198                                                          |       |
| Fibonacci                                                                   | percentage, limitation, 227-230 Total profit (increase), stop loss (impact), |       |
| retracements, 146t, 147t retracement levels, 148t                           | 71 Total                                                                     |       |
| short, Fibonacci retracements, 147t                                         | profit-per-trade metric                                                      |       |
| solutions. See Small-account stock trading                                  | commodity system, 111-116                                                    |       |
| solutions.                                                                  | stock system, 108-111                                                        |       |
|                                                                             | Trade                                                                        |       |
| trend-following/counter-trend-following strategies, one-day return, 41t     | data, usage, 16-19                                                           |       |
| Stop loss                                                                   | development samples, 160                                                     |       |
| usage. See Good stop loss.                                                  | distributions, tightness, 15                                                 |       |
| until canceled variation, 11                                                | entry, bypass/delay, 166                                                     |       |
| Stops. See Trailing stops                                                   | gambling analogies, 156                                                      |       |

| infinite distribution, trade samples (random selection), 13f            | Trading day of the week filter commodities, 97-99                     |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------|
| infinite number                                                         | long-trade breakout, 98t                                              |
| generation, 13                                                          | short-trade breakout, 98t                                             |
| impact, 12                                                              | stocks, 90                                                            |
| number                                                                  | trend filter, usage, 98t                                              |
| sufficiency, 166-169                                                    | Trading Game, The (Jones), 182                                        |
| number, proportion. See Curve-fitting.                                  | Trading range systems, usage, 25-26                                   |
| percentage, 168                                                         | Trading system elements                                               |
| point, assumption, 25                                                   | entries, 65                                                           |
| samples, selection, 13f                                                 | exits, 65                                                             |
| sequence, usage, 178                                                    | filters, 89                                                           |
| yield, back-test (usage), 15-16                                         | Trailing stops, 79-82                                                 |
| Tradeable strategy                                                      | basis, moving averages (usage), 82t                                   |
| back-testing, 7                                                         | development, 81                                                       |
| curve-fit, examination, 5                                               | example, 80f                                                          |
| defining, 1                                                             | Transaction costs, accounting, 26-27                                  |
| design process, initiation (ease), 4-5                                  | realism, 25                                                           |
| development, 7                                                          | Trend filter, usage, 98t                                              |
| steps, 7                                                                | Trend-following entry                                                 |
| reality shock, 3                                                        | power, commodities, 54-56                                             |
| Tradeable system performance (gauging),                                 | rules, 47                                                             |
| metrics (usage), 4                                                      | techniques,                                                           |
|                                                                         | comparison, 49-56 Trend-following long signals, occurrence,           |
| Trade risk                                                              | 97                                                                    |
| distance, 235-236 increase, 182, 198                                    | Trend-following pairs, 38 Trend-following strategies,                 |
| limitation, 196. See also Open-trade risk.                              | 41t, 156 commodities, trading, 42t                                    |
| ranking, 196t Trade risk on entry, limitation, 225-226,                 |                                                                       |
| 235-236                                                                 | FX pairs, trading, 42t                                                |
| ranking, 236t                                                           | one-day return. See Commodity trading. performance, determination, 32 |
| Traders, money management,                                              | stocks, trading, 41t                                                  |
| 158t 153                                                                | Trending tendencies                                                   |
| Trade Your Way to Financial Freedom (Tharp), Trading. See Stock trading | analysis, 66                                                          |
| days, exit, 72t                                                         | Trend tendencies, results, 38t                                        |
| ideas, historical data (comparison), 8                                  | t-tests, usage, 167                                                   |
| information, 153                                                        | moving averages                                                       |
|                                                                         | Two                                                                   |
| mistakes, 166 Monte Carlo packaging, absence, 160                       | counter-trend-following stock entry, 58 entry power, 58f              |
| results, diversified/non-diversified portfolios (contrast), 192t        | See Terminal wealth                                                   |
|                                                                         | TWR. relative                                                         |
| solution, improvement, 228 statistics, determination, 159-161           | U                                                                     |
| strategy, development, 8                                                |                                                                       |
| system curve-fitting effects, minimization,                             | Ulcer index, 167 Ultimate Trading Advantage,                          |
| 19-20 success, measurement, 184-185                                     | The (Hill, et al.), 54                                                |
|                                                                         | U.S. financials, correlation, 259                                     |

| V                                                                                                                         | Volume, standard deviations (bar-scoring), 125               |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| Volatility filters, 89                                                                                                    | results, 126t                                                |
| level, examination, 5 measures/comparison, formula, 246-247 range, 253t-254t standard deviation accounts, difference. See | W Wilder                                                     |
| Directional volatility.                                                                                                   | Jr., J. Welles, 50, 80 Williams, Larry, 140                  |
| Volatility-based catastrophic stops, testing, 112 Volatility-based deviation stop, 225                                    | Winners, addition, 165 Winning position, averaging down, 165 |
| Volatility-based filters commodities, 99-105                                                                              | Z                                                            |
| stocks, 91-97 Volatility-based profit target, 83                                                                          | z-tests, usage, 167                                          |