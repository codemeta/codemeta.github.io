
library(jsonlite)
library(readr)

write_json(list(codemetaterms = fromJSON(toJSON(read_csv("data/codemetaterms.csv")))),
           "data/codemetaterms.json",
           pretty=TRUE, auto_unbox=TRUE)



write_json(list(schematerms = fromJSON(toJSON(read_csv("data/schematerms.csv")))),
           "data/schematerms.json",
           pretty=TRUE, auto_unbox=TRUE)
