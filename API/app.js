
const levenshtein = require('fast-levenshtein');

const app = module.exports;


app.sequences = []

app.add = ( sequence)=>{
    app.sequences.push(sequence)
}

app.find =(query, distance) =>
  app.sequences.filter(
    (seq) => levenshtein.get(query,seq) <= distance
  )
