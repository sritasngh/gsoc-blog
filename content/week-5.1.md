Title: Coding Period Week-5 meeting-1
Date: 2021-07-06 15:00-16:00 (IST)
Category: Coding Period
Tags: coding-period, week-5, gsoc-21, fossology, scancode, copyright agent
Author: Sarita Singh
Summary: This is the third meeting during coding period. Working on scancode license relevant text highlight.

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
<li> Created UI Wireframes with Figma for ScanCode copyright and author.
</ul>
<h2> Discussions </h2>
<ul>
<li> The first idea is to have a separate browser for ScanCode agent <a href= https://www.figma.com/file/Kj3DQlhNXkZkq6DgpdfXFt/Untitled?node-id=0%3A1> link </a>.
<ul>
<li> Michael suggested not to use these as ScanCode-Toolkit project is recognized mainly for it's license scanning now keeping only Copyright and Author information in this section whereas licenses in another section will be confusing for users.
<li> Gaurav also didn't approve this idea.
</ul>
<li> The second idea is to reuse existing Copyright and Email/URL/Author browser <a href= https://www.figma.com/file/Kj3DQlhNXkZkq6DgpdfXFt/Untitled?node-id=12%3A8> link </a>.
<ul>
<li> Reusing copyright and Email/URL/Author browser section seems to be nice idea.
<li> Michael didn't find navigation between ScanCode agent and FOSSology Copyright agent using drop-down a good options. It seems to be lost. So instead of drop-down using tabs would looks nice.
<li> No need to repeat users finding for ScanCode agent as user is not interested in providing decision for a particular agent but instead they do for a file. 
</ul>
<li> Michael proposed following idea instead
<img src="images/copyright_browser.png" alt="Italian Trulli"> <center> for Copyright Browser </center> <img src="images/author_browser.png" alt="Italian Trulli"> <center> for Email/URL/Author Browser</center>
<ul>
<li> It reuses Copyright and Author browser space.
<li> There is no redundant user decision for copyright agent.
<li> Looks nice to all the attendees.
</ul>
<li> Discussion regarding how to display scanner findings in the Copyright/Email/Url/Author clearing section for a file.
<ul>
<li> Michael, Avinal and Sarita disused to add a column named source in the scanner finding table like license table in the clearing section. 
<ul><li> Under this source column two keyword could be use one 'S' for ScanCode findings and 'F' for FOSSology Copyright agent findings.
</ul>
<li> Gaurav suggested not to use this idea because for the same copyright statement, Fossology and ScanCode can have different scan result.
<ul><li> In case of license, there is License_ref table which provides same license name for all the different agents for a license do no mismatching is there.
<li> Doing same for Copyright will require lot of time.
</ul> 
<li> Gaurav Suggested two ideas for the same
<ul>
<li> There can be two tabs to switch between ScanCode Findings and FOSSology Copyright Findings.
<li> Second idea is to ask user about a default agent out of FOSSology copyright and ScanCode for an upload and display copyright/email/url/author result by the default agent.
<li> Michael didn't find the second idea much convincing.
<li> Gaurav would like to discuss further in the next meeting.
</ul>
</ul>
<h2> Upcoming Plans </h2> 
<ul> 
<li> Implement Micheal's proposed idea for copyright browser and Email/URL/Author Browser.
<li> Take feedback from other mentors too. 
</ul>