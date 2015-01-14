# -*- coding: utf-8 -*-
"""ERR100: First line is always wrong.

---
layout:     post
error_code: ERR100
source:     Nobody
source_url: ???
title:      ERR100&#58; Firse line is always wrong.
date:       2014-06-10 12:31:19
categories: writing
---

The first line always is always wrong.

"""


def check(text):

    error_code = "PL000"
    msg = "First line always has an error."

    return [(1, 1, error_code, msg)]
