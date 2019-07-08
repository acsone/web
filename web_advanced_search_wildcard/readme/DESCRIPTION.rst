This module adds new options to advanced search of char, many2one,
many2many and one2many fields:

* *starts with* (uses the domain *=ilike %<search string>*),
* *don't starts with* (uses the domain *not ilike %<search string>*),
* *ends with* (uses the domain *=ilike <search string>%*),
* *don't ends with* (uses the domain *not ilike <search string>%*),
* *matches* (uses the domain *=ilike <search string>*).

