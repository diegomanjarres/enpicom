# Enpicom application


## 1. Rosalind mmch
Not yet Implemented

## 2. Rosalind corr

Run `python3 corr.py`. the input file is in the same folder as `input.fasta`
I used the library Bio for reading fasta files, may require installation.

## 3. API

It's inside the **API** folder.

to run:
`npm i`
`npm test` (optional)
`npm start`

 I didn't make many special assumptions, just tried to make it the easiest case possible.
examples for the two endpoints:

`curl -X GET 'http://localhost:3000/sequences?query=A&distance=20'`

`curl --data-raw  '{"sequence":"ATCTC"}' -H "Content-Type: application/json" -X POST http://localhost:3000/sequences`

## 4. Scalability

If scaling up for many concurrent users, it would be useful to containerize (docker) and to use a non volatile storage (database).

The containerization makes it possible to use load balancing and autoscaling, to use more instances when the traffic gets higher.

Also, It may be needed to limit the access, by number of queries and require some permission to post.

If the posting is very heavy or has peaks, it might be needed to use async communication (queue) to receive the requests and save them with backpressure.

There are many other ways to improve the availability of the service or reduce it's cost, but they all depend on the specifics of the load.
