#!/usr/bin/env bash

mongo ksiegarniadb --eval "db.dropDatabase()"


mongoimport --db ksiegarniadb --collection customers --drop --file customers.json
mongoimport --db ksiegarniadb --collection authors --drop --file authors.json
mongoimport --db ksiegarniadb --collection books --drop --file books.json
mongoimport --db ksiegarniadb --collection admins --drop --file admins.json
mongoimport --db ksiegarniadb --collection bookcovers --drop --file bookcovers.json
