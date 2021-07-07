const validate = module.exports
const errMessage = "sequence is not valid"
validate.GETMiddleware = (req,res,next) => {
  if (!validateSequence(req.query.query)){
    return res.status(400).send(errMessage);
  }
  next()
}

validate.POSTMiddleware = (req,res,next) => {
  if (!req.body || !validateSequence(req.body.sequence)){
    return res.status(400).send(errMessage);
  }
  next()
}

const validateSequence = (seq) => seq.match(/^[ATCG]+$/g) !== null
