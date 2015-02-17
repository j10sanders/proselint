# -*- coding: utf-8 -*-
"""MAU103: Redundancy.

---
layout:     post
error_code: MAU103
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      abbetor
date:       2014-06-10 12:31:19
categories: writing
---

Points out use redundant phrases.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "MAU103"
    msg = "Redundancy. Use '{}' instead of '{}'."

    redundancies = [
        ["admitted",          ["self-admitted"]],
        ["affidavit",         ["sworn affidavit"]],
        ["alumnus",           ["former alumnus"]],
        ["antithetical",      ["directly antithetical"]],
        ["approximately",     ["approximately about"]],
        ["associate",         ["associate together(?: in groups)?"]],
        ["ATM",               ["ATM machine"]],
        ["bivouac",           ["temporary bivouac", "bivouac camp"]],
        ["blend",             ["blend together"]],
        ["but",               ["but nevertheless"]],
        ["charged with...",   ["accused of a charge"]],
        ["circumstances of",  ["circumstances surrounding"]],
        ["circumstances",     ["surrounding circumstances"]],
        ["close",             ["close proximity"]],
        ["collaborate",       ["collaborate together"]],
        ["collaborator",      ["fellow collaborator"]],
        ["collaborators",     ["fellow collaborators"]],
        ["colleagues",        ["fellow colleagues"]],
        ["combine",           ["combine together"]],
        ["complacent",        ["self-complacent"]],
        ["confessed",         ["self-confessed"]],
        ["connect",           ["connect together"]],
        ["consensus",         ["(?:general )?consensus of opinion"]],
        ["consolidate",       ["consolidate together"]],
        ["continues to",      ["still continues to"]],
        ["couple",            ["couple together"]],
        ["crisis",            ["serious crisis"]],
        ["eliminate",         ["entirely eliminate"]],
        ["fact",              ["actual fact"]],
        ["facts",             ["true facts"]],
        ["forecast",          ["future forecast"]],
        ["founding fathers",  ["founding forefathers"]],
        ["free",              ["free and gratis"]],
        ["free",              ["free gratis"]],
        ["full",              ["completely full"]],
        ["fundamentals",      ["basic fundamentals"]],
        ["gift",              ["free gift"]],
        ["interact",          ["interact with each other"]],
        ["merge",             ["merge together"]],
        ["mingle",            ["mingle together"]],
        ["mix",               ["mix together"]],
        ["necessity",         ["absolute necessity"]],
        ["obvious",           ["blatantly obvious"]],
        ["pause",             ["pause for a moment"]],
        ["planning",          ["advance planning"]],
        ["plans",             ["future plans"]],
        ["pooled",            ["pooled together"]],
        ["potable water",     ["potable drinking water"]],
        ["recruit",           ["new recruit"]],
        ["reelected",         ["reelected for another term"]],
        ["refer",             ["refer back"]],
        ["regress",           ["regress back"]],
        ["repay them",        ["repay them back"]],
        ["repay",             ["repay back"]],
        ["repeat",            ["repeat again"]],
        ["repeat",            ["repeat back"]],
        ["repeat",            ["repeat the same"]],
        ["repeated",          ["repeated the same"]],
        ["reprieve",          ["temporary reprieve"]],
        ["respite",           ["brief respite"]],
        ["retirement",        ["retiral", "retiracy"]],
        ["retreat",           ["retreat back"]],
        ["return",            ["return back"]],
        ["RSVP",              ["please RSVP"]],
        ["scrutinize",        ["closely scrutinize"]],
        ["software",          ["software program"]],
        ["surrounded",        ["surrounded on all sides"]],
        ["the nation",        ["the whole entire nation"]],
        ["timpani",           ["timpani drum"]],
        ["throughout the",    ["throughout the entire"]],
        ["twins",             ["pair of twins"]],
        ["vacancy",           ["unfilled vacancy"]],
        ["veteran",           ["former veteran"]],
        ["visible",           ["visible to the eye"]],
        ["vocation",          ["professional vocation"]],
        ["while",             ["while at the same time"]],
    ]

    return preferred_forms_check(text, redundancies, err, msg)