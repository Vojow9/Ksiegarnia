#!/usr/bin/env bash

mongoexport --db ksiegarniadb --collection customers --out customers.json
mongoexport --db ksiegarniadb --collection authors --out authors.json
mongoexport --db ksiegarniadb --collection books --out books.json
mongoexport --db ksiegarniadb --collection admins --out admins.json
mongoexport --db ksiegarniadb --collection bookcovers --out bookcovers.json
