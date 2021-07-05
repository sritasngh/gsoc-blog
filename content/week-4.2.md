Title: Coding Period Week-4 meeting-2
Date: 2021-06-29 15:00-16:00 (IST)
Category: Coding Period
Tags: coding-period, week-4, gsoc-21, fossology, scancode, license-scanner
Author: Sarita Singh
Summary: This is the second of week-4 meeting during coding period. Working on scancode license relevant text highlight.

<h2> Attendees </h2>
<ul> 
<li> <a href="https://github.com/GMishx"> Gaurav Mishra </a>
<li> <a href="https://github.com/mcjaeger"> Michael C. Jaeger</a>
<li> <a href="https://github.com/avinal"> Avinal Kumar </a>
<li> <a href="https://github.com/itssingh"> Sarita Singh </a>
</li>
</ul>

<h2> Updates </h2>
<ul>
<li> Populated ScanCode wrapper to include copyright and author information.
<li> Currently using FOSSology copyright and author database tables to insert these information.
<li> FOSSology Scheduler is calling ScanCode for copyright and author along with licenses.  
</ul>
<h2> Discussions </h2>
<ul>
<li> Asked how to copyright agent is generating hash for copyright and author tables?
<ul><li> Hash is md5(content). </ul>
<li> What is clearing table in copyright agent database <a href= https://github.com/fossology/fossology/blob/master/src/copyright/agent/database.cc#L248-L308> here</a>?
<ul>
<li> This code block creates copyright_decision table.
<li> This table is used to store user's decision.
<li> Similarly there are license_decision table which stores user's clearing decision for licenses.
</ul> 
<li> Gaurav explained how copyright agent/user finding works.
<ul>
<li> Agent findings contain what scanners has found, if a user makes changes in the agents finding that changes will be recorded into copyright_event table.
<li> For the same pfile that agent will give edited result.
<li> User finding table records user_decision during clearing in the UI and that content is inserted into copyright_decision table in the database.
<li> These clearing results are helpful during creating report.
<li> Scancode will also include reporting.
</ul>
<li> Avinal asked question about how to reuse an upload for different agent without reloading?
<ul>
<li> Gaurav explained following:
<li> Under Jobs go to Schedule agents, there select an upload to analyse and the agent who will do analysis.
</ul>
<li> Gaurav suggested a FOSSology Using: End-to-end workflow video on YouTube <a href= FOSSology Using: End-to-end workflow> link</a>
</ul>
<h2> Upcoming Plans </h2> 
<ul> 
<li> Creating tables for scancode copyright and author.
<li> Watch end-to-end fossology workflow video and understand fossology UI and working.
</ul>