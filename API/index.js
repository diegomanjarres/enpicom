const express = require('express')
const myApp = require('./app')
const validate = require('./validate')
var bodyParser = require('body-parser')

const app = express()
app.use(bodyParser.json())
const port = 3000

app.get('/sequences', validate.GETMiddleware, (req, res) => {
  const {query, distance} = req.query
  result = myApp.find(query,distance)
  res.json({result})
})

app.post('/sequences', validate.POSTMiddleware, (req, res) => {
  myApp.add(req.body.sequence)
  return res.status(201).send()
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
