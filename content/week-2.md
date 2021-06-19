Title: Coding Period Week-2 meeting
Date: 2021-06-18 17:00-18:00 (IST)
Category: Coding Period
Tags: coding-period, week-2, gsoc-21, fossology, scancode, license-scanner, gist links
Author: Sarita Singh
Summary: This is the second meeting during coding period. Working on scancode UI.

<h2> Attendees </h2>
<ul> 
<li> <a href="https://github.com/GMishx"> Gaurav Mishra </a>
<li> <a href="https://github.com/mcjaeger"> Michael C. Jaeger</a>
<li> <a href="https://github.com/shaheemazmalmmd"> Shaheem Azmal </a>
<li> <a href="https://github.com/avinal"> Avinal Kumar </a>
<li> <a href="https://github.com/itssingh"> Sarita Singh </a>
</li>
</ul>

<h2> Updates </h2>
<ul>
<li> Able to escape double quote and get a valid JSON output for matched license text. Gist <a href=https://gist.github.com/itssingh/6590e3e560c895aba9a6b9f6e6c7656d#file-license_template-html-L14> link </a> to the code.
<li> Text highlighting for license highlighting is working. Gist <a href= https://gist.github.com/itssingh/c0bc32b2895ae67540d8eeabdb4e418b> link </a> to code.
<li> UI for license scanning is working fine.
</ul>
<h2> Discussions </h2>
<ul>
<li> ModuleNotFoundError: No module named 'scancode'. Gaurav suggested to install scancode with root privilege.
<li> Tested database queries, working but unless UI won't work can't say if it'll work for scancode or not.
<li> FOSSology uses python with later version than 3.6 which is required for scancode. Gaurav said we can make python3.6 as default version for fossology but for now make scancode installation working on my local system and we'll discuss about the same later.
</ul>
<h2> Conclusion and Upcoming Plans </h2> 
<ul>
<li> Fixing bug for license scanning. Checkout the <a href=https://github.com/itssingh/fossology/tree/feat/newagent%2Fscancode-toolkit> code </a>.
<li> Text highlighting problem solved I'll try to integrate this before next meet on friday.
<li> Once done with license scanning, I'll start writing Unit test for scancode agent and UI testing. 
<li> There is a meeting on coming Tuesday.
</ul>