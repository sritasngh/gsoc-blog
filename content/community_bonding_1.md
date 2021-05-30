Title: Community Bonding Period Meeting-1
Date: 2021-05-28 17:00-18:00 (IST)
Category: Community-Bonding
Tags: community-bonding, gsoc-21, fossology, scancode, license-scanner, ojo
Author: Sarita Singh
Summary: This is the first meeting during community bonding period. Wrapper(Ninka), spdx-key dispute had been discussed.

<h2> Organiser </h2>
<ul> <li> <a href="https://github.com/GMishx"> Gaurav Mishra </a> </li> </ul>

<h2> Attendees </h2>
<ul> 
<li> <a href="https://github.com/GMishx"> Gaurav Mishra </a>
<li> <a href="https://github.com/ag4ums"> Anupam Ghosh </a>
<li> <a href="https://github.com/hastagAB"> Ayush Bhardwaj </a>
<li> <a href="https://github.com/avinal"> Avinal Kumar </a>
<li> <a href="https://github.com/itssingh"> Sarita Singh </a>
</li>
</ul>

<h2> Discussion </h2>
<ul>
<h3> <strong> About the current update </strong> </h3>
<ul> 
<li> Learnt PHP, SQL database
<li> Lerning API on which Gaurav has suggested to leave it for now.
<li> Working on a project using PHP, SQL, Twig template, should be completed before the next meet.
<li> Gaurav suggested to make GSoC timeline accessible to everyone and prepare a meeting report for others. 
</ul>
<h3><strong> About the wrapper</strong></h3>
<ul>
<li> I found the <a href="https://github.com/itssingh/fossology/tree/master/src/ninka"> Ninka wrapper</a> to be the suitable match for scancode plugin for FOSSology:
<ul> <li> useful functions for license integration are available so some changes or addition should work. 
<li> I have already used this wrapper to create a <a href="https://github.com/itssingh/scanology"> prototype </a>. 
 <li> I asked mentors if it could work on which Gaurav confirmed to yes. </ul></ul>
<h3><strong> About spdx key dispute </strong></h3>
<ul>
<li> A NOMOS and ScanCode scan output <a href=" https://docs.google.com/spreadsheets/d/1lgAVHofEXyVLa7ocrl8rGjuNulY7VgF-WGOQVqYkmoE/edit#gid=680720653"> comparison list </a>.
<ul> 
<li> same licenses with slight variation in spdx key ex. LGPL-2.1-or-later (scancode) and LGPL-2.1+ (NOMOS) will be taken care as <a href="https://github.com/itssingh/fossology/blob/master/src/ojo/agent/ojoregex.hpp"> ojo agent </a> does.
<li> Write a regex to make license keys case insensitive ex. inner-net-2.0 (scancode) and InnerNet-2.00 (NOMOS).
<li> Add new license to the license database table. </ul></ul>
<h3> <strong> About the Project Proposal </strong> 
</h3> 
<ul>
<li> Gaurav said everything looks fine in the proposal except the UI part. Ninka wrapper UI could work for license integration. copyright and email will required changes.
<li> Once license integration will be completed, have to see for parallel processing supported by scancode to optimize the speed.
</ul></ul>
<h2> Conclusion and Further Plans </h2> 
<ul>
<li> Ninka Wrapper finalised
<li> Spdx key dispute solved
<li> Create scancode Jinja template
<li> Add new scan output to wrapper
<li> Fork and create a branch for development and mention the same in blog/wiki.
<li> Add a timeline section in blog/wiki as provided in the project proposal.
<li> Prepare a prototype/plan for the next week.
</ul>
