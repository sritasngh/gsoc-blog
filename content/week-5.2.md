Title: Coding Period Week-5 meeting-2
Date: 2021-07-10 17:30-18:00 (IST)
Category: Coding Period
Tags: coding-period, week-5, gsoc-21, fossology, scancode, copyright agent
Author: Sarita Singh
Summary: This is the fifth week meeting during coding period.

<h2> Attendees </h2>
<ul> 
<li> <a href="https://github.com/mcjaeger"> Michael C. Jaeger</a>
<li> <a href="https://github.com/GMishx"> Gaurav Mishra </a>
<li> <a href="https://github.com/avinal"> Avinal Kumar </a>
<li> <a href="https://github.com/itssingh"> Sarita Singh </a>
</li>
</ul>
<h2> Updates </h2>
<ul>
<li> Added ScanCodeFindings table in Copyright Browser on UI.
<li> Working on populating this table with scancode_copyright data.
</ul>
<h2> Discussions </h2>
<ul>
<h3> Integrating scancode UI with copyright UI</h3> 
<li> Copyright UI could be modified to integrate Scancode_Copyright and Scancode_Author UI.
<li> CopyrightDao could be modified to include scancode copyright and author data too, no need to create a separate file for scancodeDao.
<li> Users Findings are independent of any agent so no agentID has to be update in the copyright UI code for scancode but we have to take care for the type.
<li> Gaurav suggested to use different type for copyright statement from what is used by copyright agent. Scancode will be using <a style="color:#8ee1ef">scancode_statement </a> for copyright type and <a style="color:#8ee1ef">statement </a>is used by copyright agent.
<li> Two new tables named <a style="color:#8ee1ef">scancode_copyright_event </a>, and <a style="color:#8ee1ef">scancode_author_event </a> are required to store Deactivated ScanCode findings statements and Deactivated Author statements respectively.
<li> At several places in copyright code to generate report copyright agent is hard coded, figure out some way to add scancode data also.
<h3> Discussion regarding Documentation</h3>
<li> Gaurav gave <a href= https://github.com/fossology/fossology/pull/2040/files#diff-8e7c89ac20d0fcd6aa91a097accabecfdebf47343da0d71fbb4edc8527309c00> this </a> as a reference to add copyright in the project code files.
<li> Michael suggested to look into <a href=https://github.com/fossology/fossology/wiki/Coding-Style#default-license-and-file-headers>coding guidelines</a> for default license for the project code files.
<li> Micheal suggested prepare a document for fossology wiki section like other agents have.
<li> Gaurav in the last GSoC meeting suggested to document the working of scancode agent for first evaluation and adding comments to the code written till now.  
</ul></ul>
<h2> Upcoming Plans </h2> 
<ul> 
<li> Documentation for scancode project in my project <a href= https://github.com/itssingh/fossology/wiki> wiki </a> .
<li> Refactor code written till now.
<li> Populating scancode copyright UI table.
</ul>