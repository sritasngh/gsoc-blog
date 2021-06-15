Title: Coding Period Week-1 meeting
Date: 2021-06-11 17:00-18:00 (IST)
Category: Coding Period
Tags: coding-period, week-1, gsoc-21, fossology, scancode, license-scanner
Author: Sarita Singh
Summary: This is the first meeting during coding period. Working on scancode wrapper.

<h2> Attendees </h2>
<ul> 
<li> <a href="https://github.com/GMishx"> Gaurav Mishra </a>
<li> <a href="https://github.com/ag4ums"> Anupam Ghosh </a>
<li> <a href="https://github.com/mcjaeger"> Michael C. Jaeger</a>
<li> <a href="https://github.com/shaheemazmalmmd"> Shaheem Azmal </a>
<li> <a href="https://github.com/hastagAB"> Ayush Bhardwaj </a>
<li> <a href="https://github.com/avinal"> Avinal Kumar </a>
<li> <a href="https://github.com/itssingh"> Sarita Singh </a>
</li>
</ul>

<h2> Current update </h2>
<ul> 
<li> Working on populating database for license scanning.
<li> Trying different approach to highlight matched text on scanning a code file.
</ul>
<h2> Discussion </h2>
<ul>
<li> What is pfile and why are we using it?
<ul>
<li>We are using pfile to keep record of user's input file.
<li> It's name is derived by using query 

```sql
select pfile_sha1 || '.' || pfile_md5 ||'.'|| pfile_size AS pfilename from pfile where pfile_pk=___
```
</ul>
<li> What is license_candidate in ojo databasehandler? 
<ul>
<li> license_candidate is used to temporary hold the licenses found by ojo, there can be a case when an invalid license is detected by ojo, it can't be added to license_ref table unless verified.
<li> No need to add in scancode databasehandler.
</ul>
<li> What is groupId in ojo databasehandler?
<ul>
<li> groupId is used for the candidate license.
</ul>
<li> After removing +, -or-later here, why are we adding them again here?
<ul>
<li> We don't know what suffix will be used in the license available in the database, so first we remove them from scanned license but in the next block of code we add them so that we can search in database for match.
</ul>
<li> About text highlighting
<ul>
<li> Problem:
<ul> 
<li> Unable to parse the text due to double quote present inside the text string.
<li> Using <a href=https://gist.github.com/itssingh/88af21dc2ff8229a7cb8bff1d5bb3cdd#file-match-cc> this </a> code to highlight match text, since this code is using string buffer, it has limited size.
</ul>
<li> Solution:
<ul>
<li> I can use escape character to escape double quote in the matched text. But then I have to do this thing again while matching <a href=https://gist.github.com/itssingh/88af21dc2ff8229a7cb8bff1d5bb3cdd#file-match-cc> here </a> to highlight. 
<li> For the second problem, Gaurav suggested to divide the scanned result into a certain range of characters and scan for match.
<li> Scancode default JSON output escapes these double quotes and gives valid JSON so Anupam suggested to use that and think about optimising that later. But again I can't use <a href=https://gist.github.com/itssingh/88af21dc2ff8229a7cb8bff1d5bb3cdd#file-match-cc> this </a> code.
<li> Michael suggested to use line number and transform that to position using number of characters present in a line. (It will be inaccurate as the code file could have irregular number of characters per line.)
<li> I asked if I couldn't find anything working then I can talk to Phillip and update about the same.
</ul>
</ul>
</ul>
<h2> Conclusion and Upcoming Plans </h2> 
<ul>
<li> Got clarity about populating database.
<li> Find a way for text highlighting problem.
<li> Work upon UI for license scanning before the next meeting.
</ul>
