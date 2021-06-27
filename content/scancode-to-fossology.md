Title: Integrating ScanCode to FOSSology
Date: 2021-05-20
Category: Integrating ScanCode to FOSSology
Tags: community-bonding, gsoc-21, fossology, scancode, license-scanner
Author: Sarita Singh
Summary: I am going to write about my GSoC'21 project.

<h2>Organization</h2>
FOSSology

<h2>Mentors</h2>
<ul>
<li> <a href="https://github.com/mcjaeger"> Michael C. Jaeger</a>
<li> <a href="https://github.com/GMishx"> Gaurav Mishra </a>
<li> <a href="https://github.com/hastagAB"> Ayush Bhardwaj </a>
<li> <a href="https://github.com/sjha2048"> Sahil Jha</a>
</ul>

<h2> Project Information</h2>
<p>
<strong>Nomos</strong> and <strong>Monk</strong> are the two leading scanners FOSSology uses for license detection and Copyright for scanning <code><em>copyright</em>, <em>URL</em>, <em>emails,</em></code> and <code><em>holders</em></code> name. FOSSology approach is to detect licenses with either a large (large: 2500 regexes) dataset of regex patterns (nomos) or a full string comparison against license full texts (large: ~400 texts) (monk). <strong>Atarashi</strong> license scanner implements multiple text statistics and information retrieval algorithms. 

<p>
<strong>ScanCode Toolkit</strong> is a very established license scanner similar to Nomos or Monk. It is a simple python based command line scanner that runs on Windows, Linux, and Mac. It implements a number of different approaches and integrates these into one application for identifying and classifying license-relevant content in packages.
</p>
<p>
The <strong> basic idea </strong> is to use the command line interface from the ScanCode package in order to be called right from the FOSSology application. FOSSology will pass a single file and take the result from the ScanCode command line call. Scan result will include license name, the SPDX key, Score, Copyright and Holder name, Emails, and URLs present in the given code and as requested by the user.
</p>

<a href="https://itssingh.github.io/gsoc-blog/timeline.html"> Proposed Timeline </a>